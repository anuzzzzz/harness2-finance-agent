"""The grader. It lives outside the improvement loop and only ever sees final answers.

Scoring follows the public Finance Agent rubric format: each question carries `correctness`
criteria and one `contradiction` criterion. An answer is *correct* (Vals' accuracy) when every
criterion passes; `pass_rate` (criteria passed / criteria) is reported alongside because it has
far more resolution on a 50-question set. With `votes` > 1 each criterion takes the majority of
independent judge samples, as Vals does with the mode of three.
"""

from __future__ import annotations

import json
import re
from collections import Counter

from . import prompts
from .llm import LLM, text_of


def _parse(text: str, n: int) -> list[bool] | None:
    m = re.search(r"\[.*\]", text, re.S)
    if not m:
        return None
    try:
        arr = json.loads(m.group(0))
    except json.JSONDecodeError:
        return None
    if not isinstance(arr, list) or len(arr) < n:
        return None
    out = []
    for item in arr[:n]:
        v = item.get("pass") if isinstance(item, dict) else None
        out.append(bool(v) if isinstance(v, bool) else str(v).lower() in ("true", "yes", "pass"))
    return out


def judge_answer(llm: LLM, *, question: str, expert: str, rubric: list[dict], response: str,
                 votes: int = 3) -> dict:
    n = len(rubric)
    if not response.strip():
        return {"correct": False, "pass_rate": 0.0, "criteria": [False] * n, "votes": [],
                "delivered": False, "cost_usd": 0.0, "judge_calls": 0}
    user = prompts.judge_user(question, expert, rubric, response)
    tallies: list[list[bool]] = []
    cost = 0.0
    calls = 0
    for _ in range(max(1, votes)):
        resp = llm.complete(system=prompts.JUDGE_SYSTEM, messages=[{"role": "user", "content": user}],
                            max_tokens=2000)
        cost += resp.get("_cost_usd", 0.0)
        calls += 1
        parsed = _parse(text_of(resp), n)
        if parsed is None:  # one retry on a malformed verdict
            resp = llm.complete(system=prompts.JUDGE_SYSTEM, messages=[{"role": "user", "content": user}],
                                max_tokens=2000)
            cost += resp.get("_cost_usd", 0.0)
            calls += 1
            parsed = _parse(text_of(resp), n)
        tallies.append(parsed if parsed is not None else [False] * n)
    crit = []
    for i in range(n):
        c = Counter(t[i] for t in tallies)
        crit.append(c[True] > c[False])
    return {"correct": all(crit), "pass_rate": (sum(crit) / n) if n else 0.0, "criteria": crit,
            "votes": tallies, "delivered": True, "cost_usd": round(cost, 6), "judge_calls": calls}
