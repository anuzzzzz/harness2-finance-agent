"""Turn trajectories, harness trees and the library into the text the editors read."""

from __future__ import annotations

import json

from . import harness
from .agent import Trajectory


def _cut(s: str, n: int) -> str:
    s = s or ""
    return s if len(s) <= n else s[:n] + f"\n…[truncated {len(s) - n:,} chars]"


def trajectory_md(t: Trajectory, *, text_chars: int = 1500, input_chars: int = 700,
                  output_chars: int = 1800, answer_chars: int = 7000) -> str:
    lines = [f"## Rollout `{t.label}`",
             f"- outcome: {t.stop}{' — ' + t.error[:300] if t.error else ''}",
             f"- turns: {t.turns}; cost: ${t.cost_usd:.3f}; submitted: {t.submitted}", ""]
    for s in t.steps:
        lines.append(f"### Turn {s.turn}  (stop_reason={s.stop_reason})")
        if s.thinking_chars:
            lines.append(f"_(thought for {s.thinking_chars:,} chars; not shown)_")
        if s.text:
            lines.append(_cut(s.text, text_chars))
        for ws in s.searches:
            res = ws.get("results") or []
            shown = "; ".join(f"{r.get('title') or ''} <{r.get('url') or ''}>" for r in res[:5])
            err = f" ERROR {ws['error']}" if ws.get("error") else ""
            lines.append(f"- web_search(query={json.dumps(ws.get('query'))}){err} → {len(res)} results: {shown}")
        for c in s.calls:
            arg = json.dumps(c.get("input"), ensure_ascii=False)
            lines.append(f"- {c['name']}({_cut(arg, input_chars)})")
            tag = "ERROR" if c.get("is_error") else "result"
            if c["name"] == "submit_final_result":
                continue
            lines.append(f"  {tag}: " + _cut(str(c.get('output', '')), output_chars).replace("\n", "\n  "))
        lines.append("")
    lines.append("### Final answer" + ("" if t.submitted else " (NOT submitted — nothing was delivered)"))
    lines.append(_cut(t.final_answer if t.submitted else (t.fallback_text and f"[last text, undelivered] {t.fallback_text}") or "(none)", answer_chars))
    return "\n".join(lines)


def answer_md(t: Trajectory, answer_chars: int = 9000) -> str:
    if t.submitted:
        return _cut(t.final_answer, answer_chars)
    return "(no answer was delivered)"


def tree_md(tree: harness.Tree) -> str:
    return harness.render(tree)


def pool_md(label: str, dim: str, notes: str, base: harness.Tree, tree: harness.Tree,
            rollout: Trajectory) -> str:
    return "\n".join([
        f"# Candidate `{label}` ({dim})",
        "## Editor notes", notes.strip() or "(none)", "",
        "## Diff against base", "```diff", harness.diff(base, tree), "```", "",
        trajectory_md(rollout, text_chars=1000, output_chars=1200, answer_chars=5000), "",
    ])
