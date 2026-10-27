"""Leak audit for a finished run: every web search query and result URL, flagged if it touches a
domain that could carry the answer key, plus answer-length stats per stage.

    python -m h2fin.audit runs/<run_id>
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

from . import config

SUSPECT = set(config.WEB_SEARCH_BLOCKED_DOMAINS)
SUSPECT_TITLE = ("benchmark", "finance agent", "vals ai", "leaderboard", "public.csv")


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print(__doc__)
        return 2
    run = Path(argv[0])
    flagged, n_search, n_results = [], 0, 0
    lengths: dict[str, list[int]] = defaultdict(list)
    for rj in sorted(run.glob("tasks/*/rollouts/*.json")):
        t = json.loads(rj.read_text(encoding="utf-8"))
        label = t["label"]
        if t.get("submitted"):
            lengths[label].append(len(t.get("final_answer", "")))
        for step in t.get("steps", []):
            for ws in step.get("searches", []):
                n_search += 1
                q = ws.get("query") or ""
                for r in ws.get("results", []):
                    n_results += 1
                    url = (r.get("url") or "").lower()
                    title = (r.get("title") or "").lower()
                    if any(d in url for d in SUSPECT) or any(w in title for w in SUSPECT_TITLE):
                        flagged.append((t["task_id"], label, q, f"{url}  [{title[:60]}]"))
    print(f"run {run.name}: {n_search} web searches, {n_results} result URLs, {len(flagged)} flagged")
    for task, label, q, url in flagged:
        print(f"  LEAK? {task}/{label}: query={q!r} -> {url}")
    print("\nmean submitted-answer length (chars) per stage:")
    for label in sorted(lengths):
        xs = lengths[label]
        print(f"  {label:6s} n={len(xs):2d} mean={sum(xs) / len(xs):8.0f}")
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
