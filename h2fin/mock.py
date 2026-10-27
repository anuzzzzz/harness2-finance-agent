"""Offline stand-ins: scripted models and canned HTTP, so the whole loop runs without a key.

The script is deliberately dumb but exercises every stage: tool calls (including load_skill when
a skill exists), editor file blocks, composition, selection, reflection and grading.
"""

from __future__ import annotations

import json

from . import prompts
from .llm import MockLLM

EFTS_HIT = {
    "_id": "0001065280-25-000044:nflx-20241231.htm",
    "_source": {"ciks": ["0001065280"], "period_ending": "2024-12-31", "display_names": ["NETFLIX INC  (NFLX)  (CIK 0001065280)"],
                "file_date": "2025-01-27", "form": "10-K", "adsh": "0001065280-25-000044", "file_description": "10-K"},
}
HTML = "<html><body><h1>Annual report</h1><p>Total Q4 2024 shares repurchased: 1,165,827. Q4 2023: 5,477,608.</p></body></html>"


class FakeResponse:
    def __init__(self, text: str = "", payload=None, status: int = 200, ctype: str = "text/html"):
        self.text = text
        self._payload = payload
        self.status_code = status
        self.headers = {"content-type": ctype}

    def json(self):
        return self._payload

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")


class FakeHTTP:
    def get(self, url, **kw):
        if "efts.sec.gov" in url:
            return FakeResponse(payload={"hits": {"total": {"value": 1}, "hits": [EFTS_HIT]}}, ctype="application/json")
        if "company_tickers" in url:
            return FakeResponse(payload={"0": {"cik_str": 1065280, "ticker": "NFLX", "title": "NETFLIX INC"}}, ctype="application/json")
        return FakeResponse(text=HTML)


def _n_assistant(payload: dict) -> int:
    return sum(1 for m in payload.get("messages", []) if m.get("role") == "assistant")


def _tool_use(name: str, inp: dict, i: int) -> dict:
    return {"type": "tool_use", "id": f"toolu_mock_{i}", "name": name, "input": inp}


def executor_script(payload: dict) -> dict:
    tools = {t.get("name") for t in payload.get("tools", [])}
    sys_text = " ".join(b.get("text", "") for b in (payload.get("system") or []) if isinstance(b, dict))
    has_skill = "load_skill" in tools
    n = _n_assistant(payload)
    plan = []
    if has_skill:
        plan.append(("load_skill", {"name": "edgar_figures"}))
    plan += [("edgar_search", {"search_query": '"issuer purchases of equity securities"', "ciks": ["NFLX"], "form_types": ["10-K"]}),
             ("parse_html_page", {"url": "https://www.sec.gov/Archives/edgar/data/1065280/000106528025000044/nflx-20241231.htm", "key": "nflx_10k"}),
             ("retrieve_information", {"prompt": "Extract the Q4 2024 and Q4 2023 shares repurchased: {{nflx_10k}}"})]
    if n < len(plan):
        name, inp = plan[n]
        return {"content": [{"type": "text", "text": f"Step {n + 1}: calling {name}."}, _tool_use(name, inp, n)], "stop_reason": "tool_use"}
    marker = " [skill-informed]" if has_skill else ""
    guard = " [guarded]" if "Standing rules" in sys_text else ""
    answer = (f"Q4 2024: 1,165,827 shares; Q4 2023: 5,477,608 shares. Change = -78.72%.{marker}{guard}\n"
              '{"sources": [{"url": "https://www.sec.gov/Archives/edgar/data/1065280/000106528025000044/nflx-20241231.htm", "name": "Netflix 10-K FY2024"}]}')
    return {"content": [_tool_use("submit_final_result", {"final_result": answer}, n)], "stop_reason": "tool_use"}


def retriever_script(payload: dict) -> dict:
    return {"content": [{"type": "text", "text": "Q4 2024 repurchased 1,165,827 shares; Q4 2023 repurchased 5,477,608 shares."}]}


SKILL = """\
---
name: edgar_figures
description: Pull one figure from a stored filing with a targeted retrieve_information question.
---
1. Name the table or section that holds the figure (e.g. "Issuer Purchases of Equity Securities").
2. Ask retrieve_information for that section only, with the period and units spelled out.
3. Repeat the figure back with its period before using it in arithmetic.
"""


def editor_script(payload: dict) -> dict:
    mission = payload["messages"][-1]["content"] if isinstance(payload["messages"][-1]["content"], str) else ""
    if "YOUR DIMENSION: INV" in mission:
        reply = ('<file path="tool_guidance.md">\nAfter parse_html_page, ask retrieve_information ONE targeted question per figure.\n</file>\n\n'
                 "<notes>\nbase1 turn 3 asked for two figures in one prompt; split them.\n</notes>")
    elif "YOUR DIMENSION: DOM" in mission:
        reply = (f'<file path="skills/edgar_figures/SKILL.md">\n{SKILL}</file>\n\n'
                 '<file path="guardrails.md">\nWhen a figure must be read from a stored filing, call load_skill with `edgar_figures`.\n</file>\n\n'
                 "<notes>\nbase1 turn 3: figure taken without naming its table; a skill carries the procedure.\n</notes>")
    elif "composing THE final harness" in mission:
        reply = ('<file path="tool_guidance.md">\nAfter parse_html_page, ask retrieve_information ONE targeted question per figure.\n</file>\n\n'
                 f'<file path="skills/edgar_figures/SKILL.md">\n{SKILL}</file>\n\n'
                 '<file path="guardrails.md">\nWhen a figure must be read from a stored filing, call load_skill with `edgar_figures`.\n</file>\n\n'
                 "<notes>\nkept -> tool_guidance (inv1) -> inv1 rollout split the question\nkept -> skill (dom1) -> dom1 rollout loaded it at turn 1\n</notes>")
    elif "choosing which of" in mission:
        reply = "<why>\nCandidate A states both figures with periods.\n</why>\n\n```choice\nA\n```"
    elif "complete record of one improvement round" in mission:
        reply = ("<edits>\ncomponent: tool_guidance.md\ncandidates: inv1, agg1\nchange: one question per figure\n"
                 "observed: inv1 turn 3 asked a narrower question than base1\nverdict: helped\n</edits>\n\n"
                 "<experience>\ncue: a question needs two figures from the same stored filing\n"
                 "lesson: in tool_guidance.md, instruct one retrieve_information question per figure, each naming its period\n"
                 "evidence: edit row tool_guidance.md (inv1 vs base1 turn 3)\nconfidence: low, single rollout\n</experience>")
    else:
        reply = "<notes>\nKEEP_BASE\n</notes>"
    return {"content": [{"type": "text", "text": reply}]}


def judge_script(payload: dict) -> dict:
    user = payload["messages"][-1]["content"]
    n = user.count("\n", user.find("CRITERIA:"), user.find("AGENT RESPONSE")) - 2
    n = max(n, 1)
    good = "[skill-informed]" in user or "[guarded]" in user
    arr = [{"id": i + 1, "pass": good or (i % 2 == 0), "reason": "mock"} for i in range(n)]
    return {"content": [{"type": "text", "text": json.dumps(arr)}]}


def build(args, log):
    def route(payload: dict) -> dict:
        system = payload.get("system")
        if isinstance(system, str) and system == prompts.JUDGE_SYSTEM:
            return judge_script(payload)
        if payload.get("tools"):
            return executor_script(payload)
        if isinstance(system, list) and system:
            return editor_script(payload)
        return retriever_script(payload)

    exec_llm = MockLLM(args.executor, route, log=log)
    editor = MockLLM(args.editor, route, log=log)
    judge = MockLLM(args.judge, route, log=log)
    return exec_llm, editor, judge, (lambda: MockLLM(args.executor, route, log=log)), FakeHTTP()
