"""The executor: one Messages API tool loop per task, under one harness tree.

Loop rules follow vals-ai/finance-agent: the run ends only when `submit_final_result` is called
or the turn limit is hit; a text-only reply gets "Continue."; on a limit the answer is empty
(Vals scores that as wrong). A cost ceiling per run is added so a runaway loop cannot eat the
budget.
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, field, asdict
from typing import Any

from . import harness, tools
from .llm import LLM, LLMError, Usage, text_of


@dataclass
class Step:
    turn: int
    text: str = ""
    thinking_chars: int = 0
    searches: list[dict] = field(default_factory=list)   # server-side web searches
    calls: list[dict] = field(default_factory=list)      # client tool calls + results
    stop_reason: str = ""
    cost_usd: float = 0.0


@dataclass
class Trajectory:
    task_id: str
    label: str
    question: str
    steps: list[Step] = field(default_factory=list)
    final_answer: str = ""          # "" unless submit_final_result was called
    fallback_text: str = ""         # last assistant text, for the editors' eyes only
    submitted: bool = False
    turns: int = 0
    stop: str = ""                  # submitted | max_turns | max_cost | error
    error: str = ""
    usage: dict = field(default_factory=dict)
    cost_usd: float = 0.0
    elapsed_s: float = 0.0
    harness_label: str = ""

    def to_dict(self) -> dict:
        d = asdict(self)
        return d


def _blocks_to_dicts(content: list[dict]) -> list[dict]:
    # Blocks come back as plain dicts from the REST client; strip our private keys only.
    return [b for b in content if isinstance(b, dict)]


def run_agent(question: str, tree: harness.Tree, llm: LLM, *, task_id: str, label: str,
              retriever_factory=None, http=None, web_search: bool = True,
              max_web_searches: int = 8, max_turns: int = 50, max_cost_usd: float = 4.0,
              max_tokens: int = 16000, log=None) -> Trajectory:
    """`retriever_factory()` must return a fresh LLM for this run's retrieve_information calls
    (so their cost is attributable to the run); default is a sibling of `llm`."""
    log = log or (lambda s: None)
    t0 = time.time()
    traj = Trajectory(task_id=task_id, label=label, question=question, harness_label=label)
    if retriever_factory is None:
        retriever_factory = lambda: LLM(llm.model, api_key=llm.api_key, effort=llm.effort,  # noqa: E731
                                        auto_cache=llm.auto_cache, log=llm.log)
    ctx = tools.ToolContext(retriever=retriever_factory(), skills=harness.skills_of(tree))
    if http is not None:
        ctx.http = http
    schemas = tools.tool_schemas(ctx, web_search=web_search, max_web_searches=max_web_searches)
    system = harness.system_blocks(tree)
    messages: list[dict] = [{"role": "user", "content": [{"type": "text", "text": f"Question:\n{question}"}]}]
    run_usage = Usage()
    turn = 0

    def spent() -> float:
        return run_usage.cost_usd + ctx.retriever.usage.cost_usd

    try:
        while True:
            if turn >= max_turns:
                traj.stop = "max_turns"
                break
            if spent() > max_cost_usd:
                traj.stop = "max_cost"
                break
            turn += 1
            resp = llm.complete(system=system, messages=messages, tools=schemas, max_tokens=max_tokens)
            cost = resp.get("_cost_usd", 0.0)
            run_usage.add(Usage(**{k: v for k, v in resp["_usage"].items()}))
            content = _blocks_to_dicts(resp.get("content", []))
            stop = resp.get("stop_reason", "")
            step = Step(turn=turn, stop_reason=stop, cost_usd=cost)
            step.text = "\n".join(b.get("text", "") for b in content if b.get("type") == "text").strip()
            step.thinking_chars = sum(len(b.get("thinking", "") or "") for b in content if b.get("type") == "thinking")
            # Server-side searches and their results, for the record.
            for b in content:
                if b.get("type") == "server_tool_use":
                    step.searches.append({"id": b.get("id"), "query": (b.get("input") or {}).get("query"), "results": []})
                elif b.get("type") == "web_search_tool_result":
                    res = b.get("content")
                    entry = next((s for s in step.searches if s["id"] == b.get("tool_use_id")), None)
                    if entry is None:
                        entry = {"id": b.get("tool_use_id"), "query": None, "results": []}
                        step.searches.append(entry)
                    if isinstance(res, list):
                        entry["results"] = [{"title": r.get("title"), "url": r.get("url"), "page_age": r.get("page_age")}
                                            for r in res if isinstance(r, dict)][:10]
                    elif isinstance(res, dict):
                        entry["error"] = res.get("error_code")
            if step.text:
                traj.fallback_text = step.text
            # Keep the assistant turn verbatim (thinking + encrypted search results must round-trip).
            messages.append({"role": "assistant", "content": content})

            tool_uses = [b for b in content if b.get("type") == "tool_use"]
            if stop == "pause_turn" or (stop == "tool_use" and not tool_uses):
                traj.steps.append(step)
                continue  # resend as-is; the API continues the server-side loop

            if stop == "tool_use" and tool_uses:
                results = []
                done = False
                for tu in tool_uses:
                    name = tu.get("name", "")
                    args = tu.get("input") or {}
                    impl = tools.IMPLS.get(name)
                    rec: dict[str, Any] = {"name": name, "input": args}
                    t1 = time.time()
                    c0 = ctx.retriever.usage.cost_usd
                    try:
                        if impl is None:
                            raise KeyError(f"unknown tool {name}")
                        out = impl(args, ctx)
                        is_err = False
                    except Exception as e:  # tool errors go back to the model, as in Vals
                        out, is_err = f"{type(e).__name__}: {e}", True
                    rec["output"] = out
                    rec["is_error"] = is_err
                    rec["elapsed_s"] = round(time.time() - t1, 2)
                    rec["cost_usd"] = round(ctx.retriever.usage.cost_usd - c0, 6)
                    step.calls.append(rec)
                    if name == "submit_final_result" and not is_err:
                        traj.final_answer = out
                        traj.submitted = True
                        traj.stop = "submitted"
                        done = True
                        break
                    results.append({"type": "tool_result", "tool_use_id": tu["id"], "content": out, "is_error": is_err})
                traj.steps.append(step)
                if done:
                    break
                messages.append({"role": "user", "content": results})
                continue

            # Text-only turn (end_turn / max_tokens / stop_sequence): nudge, as Vals does.
            traj.steps.append(step)
            messages.append({"role": "user", "content": [{"type": "text", "text": "Continue."}]})
    except LLMError as e:
        traj.stop = "error"
        traj.error = str(e)[:2000]
        log(f"[{task_id}/{label}] LLM error: {traj.error[:200]}")
    except Exception as e:  # noqa: BLE001 — never lose a trajectory to a crash
        traj.stop = "error"
        traj.error = f"{type(e).__name__}: {e}"[:2000]
        log(f"[{task_id}/{label}] crash: {traj.error[:200]}")

    # retrieve_information calls were billed to this run's own retriever; fold them in.
    run_usage.add(ctx.retriever.usage)
    traj.turns = turn
    traj.usage = run_usage.to_dict()
    traj.cost_usd = round(run_usage.cost_usd, 6)
    traj.elapsed_s = round(time.time() - t0, 1)
    return traj
