"""Rebuild results/README.md from every results/*.json summary."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"


def main() -> None:
    rows = []
    for p in sorted(RESULTS.glob("*.json")):
        s = json.loads(p.read_text(encoding="utf-8"))
        pct = lambda x: f"{100 * x:.1f}%"  # noqa: E731
        rows.append(
            f"| `{s['run_id']}` | {s['models']['executor'].replace('claude-', '')} / "
            f"{s['models']['editor'].replace('claude-', '')} | {s['k']} | {s['n_tasks']} | "
            f"{'on' if s.get('web_search') else 'off'} | {pct(s['base']['correct'])} → {pct(s['harness2']['correct'])} | "
            f"{pct(s['base']['pass_rate'])} → {pct(s['harness2']['pass_rate'])} | "
            f"{s['paired']['h2_better']}/{s['paired']['base_better']}/{s['paired']['tie']} | "
            f"${s['base']['mean_cost_usd']:.2f} → ${s['harness2']['mean_task_cost_usd']:.2f} | ${s['total_cost_usd']:.2f} |")
    lines = ["# Results", "",
             "One row per run. *correct* = every rubric criterion passed (Vals' accuracy); *pass rate* = share of "
             "criteria passed. *paired* = tasks where Harness² beat / lost to / tied the base on pass rate. "
             "Each run's full summary is the JSON next to this file; trajectories are in the run's workflow artifact.", "",
             "| run | executor / editor | k | tasks | web search | correct (base → H²) | pass rate (base → H²) | paired W/L/T | cost per task (base → H²) | run total |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    lines += rows or ["| _(no runs yet)_ | | | | | | | | | |"]
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS / 'README.md'} ({len(rows)} runs)")


if __name__ == "__main__":
    main()
