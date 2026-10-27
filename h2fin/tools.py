"""The finance agent's tools.

Descriptions and parameters follow vals-ai/finance-agent (MIT) so the base harness is as close
as possible to the published one. Two substitutions keep the whole thing runnable with only an
Anthropic key:

* `edgar_search` uses the SEC's own full-text search (efts.sec.gov) instead of sec-api.io.
* `web_search` is Claude's hosted web-search tool (a server tool) instead of Tavily.

Everything else (`parse_html_page`, `retrieve_information`, `submit_final_result`) keeps the
published semantics. `load_skill` exists only when the harness carries skills.
"""

from __future__ import annotations

import json
import os
import re
import time
from dataclasses import dataclass, field
from typing import Any, Callable

import requests

from . import config
from .llm import LLM, text_of

DATE_RE = r"^\d{4}-\d{2}-\d{2}$"
EFTS_URL = "https://efts.sec.gov/LATEST/search-index"
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
MAX_STORED_CHARS = 2_500_000        # per stored document
MAX_RETRIEVE_CHARS = 700_000        # per key inserted into one retrieve prompt
MAX_TOOL_OUTPUT_CHARS = 40_000      # cap on what goes back into the conversation


def _ua() -> str:
    # SEC asks for a descriptive User-Agent with contact details.
    return os.environ.get("SEC_USER_AGENT", "harness2-finance-agent research (github.com)")


@dataclass
class ToolContext:
    """Everything a tool call needs besides its arguments."""

    retriever: LLM
    http: Any = field(default_factory=requests.Session)   # anything with .get(url, ...)
    state: dict[str, str] = field(default_factory=dict)   # the data storage
    skills: dict[str, str] = field(default_factory=dict)  # name -> SKILL.md body
    as_of: str = config.AS_OF_DATE
    sec_sleep: float = 0.12                                # SEC fair-access: <=10 req/s
    tickers: dict[str, str] | None = None
    http_retries: int = 4


# --------------------------------------------------------------------------- schemas

def tool_schemas(ctx: ToolContext, *, web_search: bool, max_web_searches: int) -> list[dict]:
    tools: list[dict] = []
    if web_search:
        tools.append({"type": config.WEB_SEARCH_TOOL_TYPE, "name": "web_search",
                      "max_uses": max_web_searches})
    tools += [EDGAR_SEARCH, PARSE_HTML_PAGE, RETRIEVE_INFORMATION]
    if ctx.skills:
        tools.append(load_skill_schema(ctx.skills))
    tools.append(SUBMIT_FINAL_RESULT)
    return tools


SUBMIT_FINAL_RESULT = {
    "name": "submit_final_result",
    "description": (
        "Submits the final answer to the user. You should include your final answer, as well as any "
        "necessary reasoning, justification, calculations, and explanation. Finally, you should "
        "provide any sources used to answer the question. You MUST use this tool to submit your "
        "final result. The user will not see your response if you do not use this tool to submit. "
        "You will not be able to continue working after this tool is called; the conversation will "
        "be ended."
    ),
    "input_schema": {
        "type": "object",
        "properties": {"final_result": {"type": "string",
                                        "description": "The final result to submit to the agent"}},
        "required": ["final_result"],
    },
}

EDGAR_SEARCH = {
    "name": "edgar_search",
    "description": (
        "Search the SEC EDGAR database (full-text search of filings and their attachments). "
        "You should provide a search query. You can also optionally provide a start date, an end "
        "date, a page number, top N results, a list of form types, and/or a list of CIKs or tickers. "
        "The results are returned as a list of dictionaries, each containing the metadata for a "
        "filing document, including the URL of the document. It does not contain the full text of "
        "the filing; use parse_html_page on a result's url to read it."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "search_query": {"type": "string", "description": (
                "The case-insensitive search-term or phrase to search the contents of filings and "
                "their attachments. Exact phrases can be matched by enclosing them in quotation "
                'marks ("exact phrase"); terms outside quotes are all required (implicit AND). '
                "Wildcards (*) are supported at the end of a word.")},
            "form_types": {"type": "array", "items": {"type": "string"}, "description": (
                "(optional) Limits search to specific EDGAR form types (e.g., ['8-K', '10-Q']). "
                "Default: all form types")},
            "ciks": {"type": "array", "items": {"type": "string"}, "description": (
                '(optional) Filters results to filings from specified CIKs, e.g. ["0001811414", '
                '"1318605"]. Leading zeros are optional. A ticker symbol (e.g. "NFLX") is also '
                "accepted and resolved to its CIK. Default: all CIKs")},
            "start_date": {"type": "string", "description": (
                f"(optional) Start date for the search range in yyyy-mm-dd format. If the value is "
                f"later than {config.AS_OF_DATE}, it will be set to {config.AS_OF_DATE}."),
                "default": "2001-01-01"},
            "end_date": {"type": "string", "description": (
                f"(optional) End date for the search range in yyyy-mm-dd format. If the value is "
                f"later than {config.AS_OF_DATE}, it will be set to {config.AS_OF_DATE}."),
                "default": config.AS_OF_DATE},
            "page": {"type": "integer", "description": (
                "(optional) Used for pagination. Each page contains up to 100 matching documents. "
                "Default: 1"), "default": 1},
            "top_n_results": {"type": "integer", "maximum": 100, "default": 20, "description": (
                "(optional) Return only the first N results of the page (max 100). Default: 20")},
        },
        "required": ["search_query"],
    },
}

PARSE_HTML_PAGE = {
    "name": "parse_html_page",
    "description": (
        "This tool is used to parse the contents of an HTML page and save it to the agent's data "
        "storage system. The tool will retrieve the HTML page from the URL provided, then parse it "
        "from HTML to plain text. Finally, it will save it to the agent's data storage system under "
        "the key provided. You can use the retrieve_information tool to later retrieve information "
        "about the stored page."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "url": {"type": "string", "description": "The URL of the HTML page to parse"},
            "key": {"type": "string",
                    "description": "The key to use when saving the result in the conversation's data storage."},
        },
        "required": ["url", "key"],
    },
}

RETRIEVE_INFORMATION = {
    "name": "retrieve_information",
    "description": (
        "This tool allows you to retrieve data from previously saved documents from the agent's data "
        "storage system, by applying an LLM prompt to the stored document.\n\n"
        "To use the tool, you will need to provide a prompt. This prompt will include both the query "
        "to be sent to the LLM, as well as the keys of files you have previously saved to the data "
        "storage system.\n\n"
        'For example, if you want to analyze data stored under the key "financial_report", your '
        'prompt should look like the following:\n"Analyze the following financial report and '
        'extract the revenue figures: {{financial_report}}"\n\n'
        "The {{key_name}} will be replaced with the full text of the document stored under that key "
        "before the query is sent.\n\n"
        "IMPORTANT: Your prompt MUST include at least one key from the data storage using this exact "
        "format: {{key_name}}. If you don't use this exact format with double braces, the tool will "
        "fail to retrieve the information.\n\n"
        "You can also optionally only pass *a portion* of each document to the LLM, rather than the "
        "entire document. This can be used to avoid token limit errors or improve efficiency. To do "
        "so, use the input_character_ranges parameter to specify which portions of documents to "
        'extract. For example, if "financial_report" contains "Annual Report 2023" and you specify: '
        '[{"key": "financial_report", "start": 1, "end": 6}], then only "nnual" will be inserted '
        "into the prompt (characters 1 through 5, as end is exclusive)."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "prompt": {"type": "string", "description": (
                "The prompt that will be passed to the LLM. You MUST include at least one data "
                "storage key in the format {{key_name}} - for example: 'Summarize this 10-K filing: "
                "{{company_10k}}'. The content stored under each key will replace the {{key_name}} "
                "placeholder.")},
            "input_character_ranges": {"type": "array", "description": (
                "An optional list of character range specifications for extracting only portions "
                "of documents. Each object should have 'key' (the document key), 'start' (start "
                "character index, inclusive), and 'end' (end character index, exclusive). By "
                "default, the full document is used if this parameter is not provided or if a key "
                "is not included in the list."),
                "items": {"type": "object", "properties": {
                    "key": {"type": "string"}, "start": {"type": "integer"}, "end": {"type": "integer"}},
                    "required": ["key", "start", "end"]}},
        },
        "required": ["prompt"],
    },
}


def load_skill_schema(skills: dict[str, str]) -> dict:
    listing = "\n".join(f"- {name}: {_skill_description(body)}" for name, body in sorted(skills.items()))
    return {
        "name": "load_skill",
        "description": (
            "Load one of the reusable workflow skills available to you and return its full "
            "instructions. Available skills:\n" + listing
        ),
        "input_schema": {
            "type": "object",
            "properties": {"name": {"type": "string", "description": "The skill name, exactly as listed"}},
            "required": ["name"],
        },
    }


def _skill_description(body: str) -> str:
    m = re.search(r"^description:\s*(.+)$", body, re.M)
    return m.group(1).strip().strip('"') if m else "(no description)"


# --------------------------------------------------------------------------- helpers

def _sec_get(ctx: ToolContext, url: str, **kw) -> requests.Response:
    """GET from sec.gov with the fair-access pause and retry on 429/503."""
    delay = 2.0
    last = None
    for attempt in range(ctx.http_retries + 1):
        time.sleep(ctx.sec_sleep)
        r = ctx.http.get(url, headers={"User-Agent": _ua(), "Accept-Encoding": "gzip, deflate"},
                         timeout=60, **kw)
        if r.status_code in (429, 503) and attempt < ctx.http_retries:
            time.sleep(delay)
            delay *= 2
            last = r
            continue
        return r
    return last  # type: ignore[return-value]


def _clamp_dates(start: str | None, end: str | None, as_of: str) -> tuple[str, str]:
    start = start or "2001-01-01"
    end = end or as_of
    for name, v in (("start_date", start), ("end_date", end)):
        if not re.match(DATE_RE, v):
            raise ValueError(f"{name} '{v}' is not in yyyy-mm-dd format")
    if end > as_of:
        end = as_of
    if start > as_of:
        start = as_of
    if start > end:
        raise ValueError(f"Parameter start_date '{start}' was set to a date that is later than end_date '{end}'")
    return start, end


def resolve_ciks(ctx: ToolContext, ciks: list[str]) -> list[str]:
    out = []
    for c in ciks:
        c = str(c).strip()
        if c.isdigit():
            out.append(c.zfill(10))
            continue
        if ctx.tickers is None:
            r = _sec_get(ctx, TICKERS_URL)
            r.raise_for_status()
            data = r.json()
            ctx.tickers = {v["ticker"].upper(): str(v["cik_str"]).zfill(10) for v in data.values()}
        cik = ctx.tickers.get(c.upper())
        if not cik:
            raise ValueError(f"Unknown ticker '{c}'. Provide a numeric CIK instead.")
        out.append(cik)
    return out


def _hit_to_row(hit: dict) -> dict:
    src = hit.get("_source", {})
    adsh = src.get("adsh", "")
    fid = hit.get("_id", "")
    filename = fid.split(":", 1)[1] if ":" in fid else ""
    ciks = src.get("ciks") or []
    url = ""
    if adsh and filename and ciks:
        url = f"https://www.sec.gov/Archives/edgar/data/{int(ciks[0])}/{adsh.replace('-', '')}/{filename}"
    return {
        "form": src.get("form"),
        "file_date": src.get("file_date"),
        "period_ending": src.get("period_ending"),
        "company": (src.get("display_names") or [""])[0],
        "ciks": ciks,
        "accession": adsh,
        "document": filename,
        "description": src.get("file_description"),
        "url": url,
    }


# --------------------------------------------------------------------------- implementations

def edgar_search(args: dict, ctx: ToolContext) -> str:
    q = args.get("search_query") or ""
    if not q.strip():
        raise ValueError("search_query must not be empty")
    start, end = _clamp_dates(args.get("start_date"), args.get("end_date"), ctx.as_of)
    params: dict[str, Any] = {"q": q, "dateRange": "custom", "startdt": start, "enddt": end}
    forms = args.get("form_types")
    if forms:
        if not isinstance(forms, list):
            raise ValueError("The parameter form_types must be a list if provided")
        params["forms"] = ",".join(str(f) for f in forms)
    ciks = args.get("ciks")
    cik_list: list[str | None] = [None]
    if ciks:
        if not isinstance(ciks, list):
            raise ValueError("The parameter ciks must be a list if provided")
        cik_list = resolve_ciks(ctx, ciks)[:5] or [None]   # one query per CIK; EFTS filters one entity at a time
    page = int(args.get("page") or 1)
    if page > 1:
        params["page"] = page
    top_n = int(args.get("top_n_results") or 20)
    hits: list[dict] = []
    total = 0
    for cik in cik_list:
        q = dict(params)
        if cik:
            q["ciks"] = cik
        r = _sec_get(ctx, EFTS_URL, params=q)
        if r.status_code != 200:
            raise ValueError(f"EDGAR full-text search returned HTTP {r.status_code}: {r.text[:300]}")
        data = r.json()
        hits += data.get("hits", {}).get("hits", [])
        total += int(data.get("hits", {}).get("total", {}).get("value") or 0)
    rows = [_hit_to_row(h) for h in hits[: max(1, min(top_n, 100))]]
    out = {"total_matching_documents": total, "page": page, "results": rows}
    if not rows:
        out["hint"] = ("No documents matched. Try fewer/shorter terms, drop the form filter, widen the "
                       "dates, or check the company's CIK/ticker.")
    return json.dumps(out, default=str)[:MAX_TOOL_OUTPUT_CHARS]


def _html_to_text(html: str) -> str:
    try:
        from bs4 import BeautifulSoup  # type: ignore
        soup = BeautifulSoup(html, "html.parser")
        for s in soup(["script", "style"]):
            s.extract()
        text = soup.get_text()
    except Exception:
        text = re.sub(r"<[^>]+>", " ", html)
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    return "\n".join(c for c in chunks if c)


def parse_html_page(args: dict, ctx: ToolContext) -> str:
    url = args.get("url") or ""
    key = args.get("key") or ""
    if not url or not key:
        raise ValueError("Both url and key are required")
    if "sec.gov" in url:
        r = _sec_get(ctx, url)
    else:
        r = ctx.http.get(url, headers={"User-Agent": _ua()}, timeout=60)
    if r.status_code != 200:
        raise ValueError(f"HTTP {r.status_code} when fetching {url}")
    ctype = (r.headers.get("content-type") or "").lower()
    if "pdf" in ctype or url.lower().endswith(".pdf"):
        raise ValueError("The URL points to a PDF, which this tool cannot parse. Find an HTML version.")
    text = _html_to_text(r.text)
    if not text:
        raise ValueError("HTML output was empty")
    truncated = len(text) > MAX_STORED_CHARS
    text = text[:MAX_STORED_CHARS]
    note = ""
    if key in ctx.state:
        note = "WARNING: The key already exists in the data storage. The new result overwrites the old one.\n"
    ctx.state[key] = text
    keys = "\n".join(ctx.state.keys())
    return (f"{note}SUCCESS: The result has been saved to the data storage under the key: {key}. "
            f"({len(text):,} characters{'; truncated' if truncated else ''})\n"
            f"The data_storage currently contains the following keys:\n{keys}\n")


def retrieve_information(args: dict, ctx: ToolContext) -> str:
    prompt = args.get("prompt") or ""
    ranges = args.get("input_character_ranges") or []
    if not re.search(r"{{[^{}]+}}", prompt):
        raise ValueError(
            "ERROR: Your prompt must include at least one key from data storage in the format "
            "{{key_name}}. Please try again with the correct format. You can add documents to the "
            "data storage with parse_html_page.")
    rdict: dict[str, tuple[int, int]] = {}
    for spec in ranges:
        if not isinstance(spec, dict) or not all(k in spec for k in ("key", "start", "end")):
            raise ValueError("ERROR: Each range specification must have 'key', 'start', and 'end' fields.")
        rdict[spec["key"]] = (int(spec["start"]), int(spec["end"]))
    keys = re.findall(r"{{([^{}]+)}}", prompt)
    for rk in rdict:
        if rk not in keys:
            raise ValueError(f"ERROR: The key '{rk}' is specified in input_character_ranges but is not "
                             f"referenced in the prompt. Keys in prompt: {', '.join(set(keys))}")
    for k in keys:
        if k not in ctx.state:
            raise KeyError(f"ERROR: The key '{k}' was not found in the data storage. Available keys "
                           f"are: {', '.join(ctx.state.keys())}. Use parse_html_page to add keys.")
    filled = prompt
    notes = []
    for k in dict.fromkeys(keys):
        doc = ctx.state[k]
        if k in rdict:
            s, e = rdict[k]
            doc = doc[s:e]
        if len(doc) > MAX_RETRIEVE_CHARS:
            notes.append(f"[note: {k} was truncated to its first {MAX_RETRIEVE_CHARS:,} characters; "
                         f"use input_character_ranges to read a later portion]")
            doc = doc[:MAX_RETRIEVE_CHARS]
        filled = filled.replace("{{" + k + "}}", doc)
    resp = ctx.retriever.complete(system=None, messages=[{"role": "user", "content": filled}],
                                  max_tokens=4096)
    return (text_of(resp) + ("\n" + "\n".join(notes) if notes else ""))[:MAX_TOOL_OUTPUT_CHARS]


def load_skill(args: dict, ctx: ToolContext) -> str:
    name = (args.get("name") or "").strip()
    if name not in ctx.skills:
        raise KeyError(f"Unknown skill '{name}'. Available: {', '.join(sorted(ctx.skills))}")
    return ctx.skills[name]


def submit_final_result(args: dict, ctx: ToolContext) -> str:
    fr = args.get("final_result")
    if not fr or not str(fr).strip():
        raise ValueError("Final result must not be empty")
    return str(fr)


IMPLS: dict[str, Callable[[dict, ToolContext], str]] = {
    "edgar_search": edgar_search,
    "parse_html_page": parse_html_page,
    "retrieve_information": retrieve_information,
    "load_skill": load_skill,
    "submit_final_result": submit_final_result,
}
