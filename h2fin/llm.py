"""A thin Messages API client with retries and cost accounting (no SDK dependency).

Every call returns the raw response dict plus a computed USD cost, and the client keeps a
running `Usage` total. `MockLLM` implements the same interface for offline runs.
"""

from __future__ import annotations

import json
import os
import random
import threading
import time
from dataclasses import dataclass, field
from typing import Any, Callable

import requests

from . import config


@dataclass
class Usage:
    calls: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    cache_creation_input_tokens: int = 0
    cache_read_input_tokens: int = 0
    web_search_requests: int = 0
    cost_usd: float = 0.0

    def add(self, other: "Usage") -> None:
        for k in ("calls", "input_tokens", "output_tokens", "cache_creation_input_tokens",
                  "cache_read_input_tokens", "web_search_requests"):
            setattr(self, k, getattr(self, k) + getattr(other, k))
        self.cost_usd += other.cost_usd

    def to_dict(self) -> dict:
        return {
            "calls": self.calls,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "cache_creation_input_tokens": self.cache_creation_input_tokens,
            "cache_read_input_tokens": self.cache_read_input_tokens,
            "web_search_requests": self.web_search_requests,
            "cost_usd": round(self.cost_usd, 6),
        }


def price_usage(model: str, u: dict) -> Usage:
    """USD cost of one response's `usage` object under the price table."""
    p = config.PRICES.get(model)
    inp = int(u.get("input_tokens", 0) or 0)
    out = int(u.get("output_tokens", 0) or 0)
    cw = int(u.get("cache_creation_input_tokens", 0) or 0)
    cr = int(u.get("cache_read_input_tokens", 0) or 0)
    ws = int(((u.get("server_tool_use") or {}).get("web_search_requests", 0)) or 0)
    cost = 0.0
    if p:
        rates = p
        if "long" in p and (inp + cw + cr) > p["long_threshold"]:
            rates = p["long"]
        cost = (inp * rates["input"] + out * rates["output"] + cw * rates["cache_write"]
                + cr * rates["cache_read"]) / 1e6
    cost += ws * config.WEB_SEARCH_USD_PER_CALL
    return Usage(calls=1, input_tokens=inp, output_tokens=out, cache_creation_input_tokens=cw,
                 cache_read_input_tokens=cr, web_search_requests=ws, cost_usd=cost)


class LLMError(RuntimeError):
    pass


class LLM:
    """One model, one role. `complete()` is synchronous and retries transient failures."""

    def __init__(self, model: str, *, api_key: str | None = None, effort: str | None = None,
                 auto_cache: bool = True, max_retries: int = 8, timeout: int = 900,
                 session: requests.Session | None = None, log: Callable[[str], None] | None = None):
        self.model = config.resolve_model(model)
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY", "")
        if not self.api_key:
            raise LLMError("ANTHROPIC_API_KEY is not set")
        self.effort = effort
        self.auto_cache = auto_cache
        self.max_retries = max_retries
        self.timeout = timeout
        self.session = session or requests.Session()
        self.usage = Usage()
        self.log = log or (lambda s: None)
        self._lock = threading.Lock()

    # The mock overrides this one method.
    def _post(self, payload: dict) -> dict:
        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": config.API_VERSION,
            "content-type": "application/json",
        }
        delay = 2.0
        last_err = ""
        for attempt in range(self.max_retries + 1):
            try:
                r = self.session.post(config.API_URL, headers=headers, json=payload, timeout=self.timeout)
            except requests.RequestException as e:  # network blip
                last_err = f"network error: {e}"
                r = None
            if r is not None:
                if r.status_code == 200:
                    return r.json()
                body = r.text[:2000]
                last_err = f"HTTP {r.status_code}: {body}"
                if r.status_code == 400 and "cache_control" in body and payload.get("cache_control"):
                    # The account/model rejects top-level automatic caching: drop it and retry.
                    self.log("automatic prompt caching rejected; retrying without it")
                    self.auto_cache = False
                    payload = {k: v for k, v in payload.items() if k != "cache_control"}
                    continue
                if r.status_code in (400, 401, 403, 404, 413):
                    raise LLMError(last_err)
                retry_after = r.headers.get("retry-after")
                if retry_after:
                    try:
                        delay = max(delay, float(retry_after))
                    except ValueError:
                        pass
            if attempt == self.max_retries:
                break
            sleep = min(delay * (2 ** attempt), 120) * (0.8 + 0.4 * random.random())
            self.log(f"{self.model}: {last_err[:120]} -- retrying in {sleep:.0f}s")
            time.sleep(sleep)
        raise LLMError(f"{self.model}: giving up after {self.max_retries} retries: {last_err}")

    def complete(self, *, system: str | list[dict] | None, messages: list[dict],
                 tools: list[dict] | None = None, tool_choice: dict | None = None,
                 max_tokens: int = 8192, effort: str | None = None) -> dict:
        payload: dict[str, Any] = {"model": self.model, "max_tokens": max_tokens, "messages": messages}
        if system:
            payload["system"] = system
        if tools:
            payload["tools"] = tools
        if tool_choice:
            payload["tool_choice"] = tool_choice
        eff = effort or self.effort
        if eff:
            payload["output_config"] = {"effort": eff}
        if self.auto_cache:
            payload["cache_control"] = {"type": "ephemeral"}
        t0 = time.time()
        resp = self._post(payload)
        u = price_usage(self.model, resp.get("usage", {}))
        with self._lock:
            self.usage.add(u)
        resp["_cost_usd"] = u.cost_usd
        resp["_usage"] = u.to_dict()
        resp["_elapsed_s"] = round(time.time() - t0, 2)
        resp["_model"] = self.model
        return resp


def model_capabilities(model: str, api_key: str | None = None, timeout: int = 30) -> dict | None:
    """GET /v1/models/{id}; None when the lookup fails (callers then assume support)."""
    key = api_key or os.environ.get("ANTHROPIC_API_KEY", "")
    try:
        r = requests.get(f"https://api.anthropic.com/v1/models/{config.resolve_model(model)}",
                         headers={"x-api-key": key, "anthropic-version": config.API_VERSION}, timeout=timeout)
        if r.status_code == 200:
            return r.json()
    except requests.RequestException:
        pass
    return None


def supports_web_search(model: str) -> bool | None:
    info = model_capabilities(model)
    if not info:
        return None
    try:
        return bool(info["capabilities"]["server_tools"]["web_search"]["supported"])
    except (KeyError, TypeError):
        return None


def text_of(resp: dict) -> str:
    """All text blocks of a response, joined."""
    return "\n".join(b.get("text", "") for b in resp.get("content", []) if b.get("type") == "text").strip()


class MockLLM(LLM):
    """Scripted stand-in: `script(payload) -> response dict` decides what comes back."""

    def __init__(self, model: str, script: Callable[[dict], dict], **kw):
        kw.setdefault("api_key", "mock")
        super().__init__(model, **kw)
        self.script = script
        self.auto_cache = False

    def _post(self, payload: dict) -> dict:
        resp = self.script(payload)
        resp.setdefault("usage", {"input_tokens": 1000, "output_tokens": 200})
        resp.setdefault("stop_reason", "end_turn")
        resp.setdefault("role", "assistant")
        return json.loads(json.dumps(resp))
