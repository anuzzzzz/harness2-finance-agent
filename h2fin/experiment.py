"""Run the experiment: Harness² over the Finance Agent public set, then grade.

    python -m h2fin.experiment --tasks 10 --k 1 --executor haiku --editor sonnet --judge sonnet

One run produces both conditions: `base1` is the base harness (the base condition) and the
chosen final is the Harness² condition. Everything is written under runs/<run_id>/.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import random
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from . import config, harness, prompts
from .agent import Trajectory, run_agent
from .judge import judge_answer
from .library import Library
from .llm import LLM, supports_web_search
from .recursion import run_task_parallel

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "public.csv"


def load_tasks(path: Path = DATA, *, n: int | None = None, seed: int = 42, categories: list[str] | None = None) -> list[dict]:
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    tasks = []
    for i, r in enumerate(rows):
        tasks.append({
            "task_id": f"q{i + 1:02d}",
            "question": r["Question"].strip(),
            "answer": r["Answer"].strip(),
            "category": r["Question Type"].strip(),
            "expert_minutes": r.get("Expert time (mins)", ""),
            "rubric": json.loads(r["Rubric"]),
        })
    if categories:
        tasks = [t for t in tasks if t["category"] in categories]
    # A fixed, stratified order: shuffle within each category, then deal round-robin so a short
    # run still spans the question types. The stream order matters because the library accumulates.
    rng = random.Random(seed)
    groups: dict[str, list[dict]] = defaultdict(list)
    for t in tasks:
        groups[t["category"]].append(t)
    order = sorted(groups, key=lambda c: (-len(groups[c]), c))
    for c in order:
        rng.shuffle(groups[c])
    dealt: list[dict] = []
    while any(groups.values()):
        for c in order:
            if groups[c]:
                dealt.append(groups[c].pop())
    return dealt[:n] if n else dealt


def _log_factory(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    f = open(path, "a", encoding="utf-8")

    def log(msg: str) -> None:
        line = f"{datetime.now(timezone.utc).strftime('%H:%M:%S')} {msg}"
        print(line, flush=True)
        f.write(line + "\n")
        f.flush()
    return log


def build_llms(args, log):
    if args.offline:
        from . import mock
        return mock.build(args, log)
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("ANTHROPIC_API_KEY is not set (add it as a repository secret for Actions runs)")
    exec_llm = LLM(args.executor, effort=args.executor_effort, log=log)
    editor = LLM(args.editor, effort=args.editor_effort, log=log)
    judge = LLM(args.judge, effort=args.judge_effort, log=log)
    retriever_factory = lambda: LLM(args.executor, effort=args.executor_effort, log=log)  # noqa: E731
    return exec_llm, editor, judge, retriever_factory, None


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--tasks", type=int, default=10, help="number of public questions (fixed shuffled order)")
    p.add_argument("--k", type=int, default=1, help="Harness² task-level budget k (parallel mode)")
    p.add_argument("--executor", default="haiku")
    p.add_argument("--editor", default="sonnet")
    p.add_argument("--judge", default="sonnet")
    p.add_argument("--executor-effort", default=None, help="output_config.effort for the executor (default: model default)")
    p.add_argument("--editor-effort", default=None)
    p.add_argument("--judge-effort", default=None)
    p.add_argument("--judge-votes", type=int, default=3)
    p.add_argument("--no-web-search", action="store_true", help="EDGAR-only executor (no hosted web search)")
    p.add_argument("--max-web-searches", type=int, default=8)
    p.add_argument("--max-turns", type=int, default=50)
    p.add_argument("--max-run-cost", type=float, default=4.0, help="USD ceiling per rollout")
    p.add_argument("--max-total-cost", type=float, default=60.0, help="stop starting new tasks past this USD total")
    p.add_argument("--categories", nargs="*", default=None)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--workers", type=int, default=2, help="parallel rollouts/editor calls within a stage")
    p.add_argument("--run-id", default=None)
    p.add_argument("--out", default="runs")
    p.add_argument("--offline", action="store_true", help="scripted models + canned HTTP; no network, no key")
    args = p.parse_args(argv)

    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + f"-k{args.k}-{args.executor}"
    out = Path(args.out) / run_id
    out.mkdir(parents=True, exist_ok=True)
    log = _log_factory(out / "log.txt")
    exec_llm, editor, judge, retriever_factory, http = build_llms(args, log)
    if not args.offline and not args.no_web_search:
        sup = supports_web_search(exec_llm.model)
        if sup is False:
            log(f"{exec_llm.model} does not support the web search server tool; running EDGAR-only")
            args.no_web_search = True

    manifest = {
        "run_id": run_id, "started": datetime.now(timezone.utc).isoformat(), "args": vars(args),
        "models": {"executor": exec_llm.model, "editor": editor.model, "judge": judge.model},
        "prices": config.PRICES, "web_search_tool": None if args.no_web_search else config.WEB_SEARCH_TOOL_TYPE,
        "as_of_date": config.AS_OF_DATE,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")

    tasks = load_tasks(n=args.tasks, seed=args.seed, categories=args.categories)
    base = harness.base_tree()
    harness.write_tree(base, out / "base_harness")
    lib = Library(out / "library")
    lib.rebuild_index()

    def run_fn(question: str, tree: harness.Tree, label: str, task_id: str) -> Trajectory:
        return run_agent(question, tree, exec_llm, task_id=task_id, label=label,
                         retriever_factory=retriever_factory, http=http,
                         web_search=not args.no_web_search, max_web_searches=args.max_web_searches,
                         max_turns=args.max_turns, max_cost_usd=args.max_run_cost, log=log)

    records = []
    total = 0.0
    for t in tasks:
        tdir = out / "tasks" / t["task_id"]
        if (tdir / "record.json").is_file():   # resume
            rec = json.loads((tdir / "record.json").read_text(encoding="utf-8"))
            records.append(rec)
            total += rec["total_cost_usd"]
            log(f"[{t['task_id']}] resumed from disk")
            continue
        if total > args.max_total_cost:
            log(f"stopping: spent ${total:.2f} > --max-total-cost ${args.max_total_cost:.2f}")
            break
        t0 = time.time()
        rec = run_task_parallel(
            task_id=t["task_id"], question=t["question"], k=args.k, base=base, lib=lib,
            run=lambda q, tree, lbl, _tid=t["task_id"]: run_fn(q, tree, lbl, _tid),
            editor=editor, bp=prompts.FINANCE, out_dir=tdir, log=log, seed=args.seed, workers=args.workers)
        total += rec.total_cost_usd
        log(f"[{t['task_id']}] done in {time.time() - t0:.0f}s, task ${rec.total_cost_usd:.2f}, total ${total:.2f}")
        records.append(rec.to_dict())

    # ---- grade (the only place answers and rubrics are read)
    log("grading")
    graded = []
    judge_cost = 0.0
    for rec in records:
        t = next(x for x in tasks if x["task_id"] == rec["task_id"])
        g = {"task_id": t["task_id"], "category": t["category"], "k": rec["k"], "chosen": rec["chosen"],
             "rollouts": {}, "stage_keep_base": {lbl: s["keep_base"] for lbl, s in rec["stages"].items()},
             "stage_errors": {lbl: s["error"] for lbl, s in rec["stages"].items() if s["error"]},
             "library_added": rec["library_added"], "total_cost_usd": rec["total_cost_usd"],
             "editor_cost_usd": rec["editor_cost_usd"], "errors": rec["errors"]}
        for lbl, traj in rec["rollouts"].items():
            v = judge_answer(judge, question=t["question"], expert=t["answer"], rubric=t["rubric"],
                             response=traj["final_answer"] if traj["submitted"] else "", votes=args.judge_votes)
            judge_cost += v["cost_usd"]
            g["rollouts"][lbl] = {"correct": v["correct"], "pass_rate": round(v["pass_rate"], 4),
                                  "delivered": traj["submitted"], "stop": traj["stop"], "turns": traj["turns"],
                                  "cost_usd": traj["cost_usd"], "criteria": v["criteria"], "votes": v["votes"]}
        graded.append(g)
        (out / "tasks" / t["task_id"] / "graded.json").write_text(json.dumps(g, indent=1), encoding="utf-8")

    summary = summarize(graded, manifest, judge_cost)
    (out / "summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    (out / "summary.md").write_text(summary_md(summary), encoding="utf-8")
    results = ROOT / "results"
    results.mkdir(exist_ok=True)
    (results / f"{run_id}.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    log(f"wrote {out / 'summary.md'}")
    print(summary_md(summary))
    return 0


def _mean(xs):
    xs = list(xs)
    return (sum(xs) / len(xs)) if xs else 0.0


def summarize(graded: list[dict], manifest: dict, judge_cost: float) -> dict:
    n = len(graded)
    k = graded[0]["k"] if graded else 1

    def cond(g, lbl):
        return g["rollouts"].get(lbl) or {"correct": False, "pass_rate": 0.0, "delivered": False, "cost_usd": 0.0}

    base = [cond(g, "base1") for g in graded]
    h2 = [cond(g, g["chosen"]) for g in graded]
    wins = sum(1 for b, h in zip(base, h2) if h["pass_rate"] > b["pass_rate"])
    losses = sum(1 for b, h in zip(base, h2) if h["pass_rate"] < b["pass_rate"])
    by_cat: dict[str, dict] = {}
    cats = defaultdict(list)
    for g in graded:
        cats[g["category"]].append(g)
    for c, gs in sorted(cats.items()):
        by_cat[c] = {"n": len(gs),
                     "base_correct": _mean(cond(g, "base1")["correct"] for g in gs),
                     "h2_correct": _mean(cond(g, g["chosen"])["correct"] for g in gs),
                     "base_pass_rate": _mean(cond(g, "base1")["pass_rate"] for g in gs),
                     "h2_pass_rate": _mean(cond(g, g["chosen"])["pass_rate"] for g in gs)}
    stage_stats: dict[str, dict] = {}
    for lbl in sorted({l for g in graded for l in g["rollouts"]}):
        rs = [g["rollouts"][lbl] for g in graded if lbl in g["rollouts"]]
        stage_stats[lbl] = {"n": len(rs), "correct": _mean(r["correct"] for r in rs),
                            "pass_rate": _mean(r["pass_rate"] for r in rs),
                            "delivered": _mean(r["delivered"] for r in rs),
                            "mean_cost_usd": _mean(r["cost_usd"] for r in rs),
                            "keep_base": _mean(g["stage_keep_base"].get(lbl, False) for g in graded if lbl in g["stage_keep_base"]) if lbl.startswith(("inv", "dom", "agg")) else None}
    any_base = _mean(any(cond(g, f"base{i}")["correct"] for i in range(1, k + 1)) for g in graded)
    any_final = _mean(any(cond(g, f"agg{i}")["correct"] for i in range(1, k + 1)) for g in graded)
    return {
        "run_id": manifest["run_id"], "models": manifest["models"], "k": k, "n_tasks": n,
        "web_search": manifest.get("web_search_tool") is not None,
        "base": {"correct": _mean(b["correct"] for b in base), "pass_rate": _mean(b["pass_rate"] for b in base),
                 "delivered": _mean(b["delivered"] for b in base), "mean_cost_usd": _mean(b["cost_usd"] for b in base)},
        "harness2": {"correct": _mean(h["correct"] for h in h2), "pass_rate": _mean(h["pass_rate"] for h in h2),
                     "delivered": _mean(h["delivered"] for h in h2),
                     "mean_task_cost_usd": _mean(g["total_cost_usd"] for g in graded),
                     "mean_editor_cost_usd": _mean(g["editor_cost_usd"] for g in graded)},
        "paired": {"h2_better": wins, "base_better": losses, "tie": n - wins - losses},
        "any_of_k": {"base": any_base, "finals": any_final},
        "by_category": by_cat, "by_stage": stage_stats,
        "library_entries": sum(1 for g in graded if g["library_added"]),
        "errors": sum(len(g["errors"]) for g in graded),
        "judge_cost_usd": round(judge_cost, 4),
        "total_cost_usd": round(sum(g["total_cost_usd"] for g in graded) + judge_cost, 4),
        "tasks": [{"task_id": g["task_id"], "category": g["category"], "chosen": g["chosen"],
                   "base": {kk: cond(g, "base1")[kk] for kk in ("correct", "pass_rate", "delivered")},
                   "h2": {kk: cond(g, g["chosen"])[kk] for kk in ("correct", "pass_rate", "delivered")},
                   "cost_usd": g["total_cost_usd"]} for g in graded],
    }


def summary_md(s: dict) -> str:
    pct = lambda x: f"{100 * x:.1f}%"  # noqa: E731
    lines = [f"# Run `{s['run_id']}`", "",
             f"executor `{s['models']['executor']}` · editor `{s['models']['editor']}` · judge `{s['models']['judge']}` · "
             f"k={s['k']} · tasks={s['n_tasks']} · web search {'on' if s['web_search'] else 'off'}", "",
             "| condition | correct (all criteria) | criteria pass rate | delivered | cost / task |",
             "|---|---|---|---|---|",
             f"| base harness | {pct(s['base']['correct'])} | {pct(s['base']['pass_rate'])} | {pct(s['base']['delivered'])} | ${s['base']['mean_cost_usd']:.2f} |",
             f"| Harness² k={s['k']} | {pct(s['harness2']['correct'])} | {pct(s['harness2']['pass_rate'])} | {pct(s['harness2']['delivered'])} | ${s['harness2']['mean_task_cost_usd']:.2f} (incl. ${s['harness2']['mean_editor_cost_usd']:.2f} editor) |",
             "",
             f"Paired by task (criteria pass rate): Harness² better {s['paired']['h2_better']}, base better {s['paired']['base_better']}, tie {s['paired']['tie']}.",
             f"Library entries written: {s['library_entries']}. Stage errors: {s['errors']}. Judge cost ${s['judge_cost_usd']:.2f}. Total ${s['total_cost_usd']:.2f}.", "",
             "## By stage", "", "| stage | n | correct | pass rate | delivered | KEEP_BASE | mean cost |", "|---|---|---|---|---|---|---|"]
    for lbl, st in s["by_stage"].items():
        kb = "" if st["keep_base"] is None else pct(st["keep_base"])
        lines.append(f"| {lbl} | {st['n']} | {pct(st['correct'])} | {pct(st['pass_rate'])} | {pct(st['delivered'])} | {kb} | ${st['mean_cost_usd']:.2f} |")
    lines += ["", "## By category", "", "| category | n | base correct | H² correct | base pass rate | H² pass rate |", "|---|---|---|---|---|---|"]
    for c, v in s["by_category"].items():
        lines.append(f"| {c} | {v['n']} | {pct(v['base_correct'])} | {pct(v['h2_correct'])} | {pct(v['base_pass_rate'])} | {pct(v['h2_pass_rate'])} |")
    lines += ["", "## Tasks", "", "| task | category | base | H² (chosen) | cost |", "|---|---|---|---|---|"]
    for t in s["tasks"]:
        b, h = t["base"], t["h2"]
        lines.append(f"| {t['task_id']} | {t['category']} | {'✓' if b['correct'] else '✗'} {pct(b['pass_rate'])} | "
                     f"{'✓' if h['correct'] else '✗'} {pct(h['pass_rate'])} ({t['chosen']}) | ${t['cost_usd']:.2f} |")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    sys.exit(main())
