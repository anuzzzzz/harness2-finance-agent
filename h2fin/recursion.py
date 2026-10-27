"""Harness² task-level recursion (parallel mode) and harnessing-level reflection.

For one task with budget k:

    base_i      i=1..k   rollouts of the base harness H0             (the reference set)
    inv_i/dom_i i=1..k   proposer edits on one dimension each, from the shared evidence
                         (library included), each rolled out once   (probes)
    agg_i       i=1..k   independent compositions from base + all 2k candidates, rolled out once
    select               k>1: blind choice among the k finals' answers; k=1: trivial
    reflect              experience record; library gains the chosen harness only if a lesson
                         with evidence came out of it

The grader never appears here. Base rollout 1 is also the "base condition" of the experiment.
"""

from __future__ import annotations

import json
import random
import re
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from . import harness, prompts, render
from .agent import Trajectory, run_agent
from .library import Library, has_experience
from .llm import LLM, text_of

RunFn = Callable[[str, harness.Tree, str], Trajectory]   # (question, tree, label) -> rollout


def _pmap(fn, items, workers: int):
    """Map in order, with up to `workers` threads (1 = plain loop)."""
    items = list(items)
    if workers <= 1 or len(items) <= 1:
        return [fn(x) for x in items]
    with ThreadPoolExecutor(max_workers=min(workers, len(items))) as ex:
        return list(ex.map(fn, items))


@dataclass
class Stage:
    label: str
    dim: str
    tree: harness.Tree
    notes: str = ""
    keep_base: bool = False
    error: str = ""
    reply: str = ""
    cost_usd: float = 0.0


@dataclass
class TaskRecord:
    task_id: str
    k: int
    rollouts: dict[str, Trajectory] = field(default_factory=dict)
    stages: dict[str, Stage] = field(default_factory=dict)
    chosen: str = ""
    selection_why: str = ""
    selection_ids: dict[str, str] = field(default_factory=dict)
    control_chosen: str = ""
    control_why: str = ""
    experience: dict | None = None
    edits_record: str = ""
    library_added: bool = False
    editor_cost_usd: float = 0.0
    total_cost_usd: float = 0.0
    errors: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "task_id": self.task_id, "k": self.k,
            "rollouts": {lbl: t.to_dict() for lbl, t in self.rollouts.items()},
            "stages": {lbl: {"dim": s.dim, "notes": s.notes, "keep_base": s.keep_base, "error": s.error,
                             "cost_usd": s.cost_usd, "inventory": harness.inventory(s.tree),
                             "tree": s.tree} for lbl, s in self.stages.items()},
            "chosen": self.chosen, "selection_why": self.selection_why, "selection_ids": self.selection_ids,
            "control_chosen": self.control_chosen, "control_why": self.control_why,
            "experience": self.experience, "edits_record": self.edits_record,
            "library_added": self.library_added, "editor_cost_usd": round(self.editor_cost_usd, 6),
            "total_cost_usd": round(self.total_cost_usd, 6), "errors": self.errors,
        }


def _evidence(task_id: str, question: str, base: harness.Tree, refs: list[Trajectory], lib: Library) -> str:
    parts = [f"# TASK `{task_id}`\n\n{question}", "# BASE HARNESS (the tree you edit)\n\n" + harness.render(base)]
    parts.append("# BASE ROLLOUTS (full trajectories under the base harness)\n\n" +
                 "\n\n".join(render.trajectory_md(t) for t in refs))
    libtxt = lib.context_text()
    parts.append(libtxt if libtxt else "# LIBRARY\n\n_(empty — this is the first task)_")
    return "\n\n".join(parts)


def _editor_call(editor: LLM, evidence: str | list[str], mission: str, *, max_tokens: int = 24000) -> tuple[str, float]:
    """Evidence goes in the system prompt as cached blocks (shared across the stages of one task);
    the stage's mission is the user turn."""
    blocks = [evidence] if isinstance(evidence, str) else list(evidence)
    system = [{"type": "text", "text": b, "cache_control": {"type": "ephemeral"}} for b in blocks[:3] if b]
    resp = editor.complete(system=system, messages=[{"role": "user", "content": mission}], max_tokens=max_tokens)
    return text_of(resp), resp.get("_cost_usd", 0.0)


def _stage_from_reply(label: str, dim: str, base: harness.Tree, reply: str, cost: float) -> Stage:
    tree, notes, keep = harness.apply_patch(base, reply)
    st = Stage(label=label, dim=dim, tree=tree, notes=notes, keep_base=keep, reply=reply, cost_usd=cost)
    errs = harness.validate(tree)
    if errs:
        st.error = "; ".join(errs)
        st.tree = dict(base)   # a proposal that fails validation is thrown away entire
        st.keep_base = True
    return st


def blind_select(editor: LLM, question: str, pool: dict[str, Trajectory], *, bp: prompts.BenchPrompts,
                 seed: str) -> tuple[str, str, dict[str, str], float]:
    """Pick one delivered answer from `pool` with the harnesses hidden and the ids shuffled.
    Returns (chosen_label, why, id_map, cost). Trivial when at most one answer was delivered."""
    labels = list(pool)
    delivered = [lbl for lbl in labels if pool[lbl].submitted]
    if len(delivered) <= 1:
        chosen = delivered[0] if delivered else labels[0]
        why = "trivial: single candidate" if len(labels) == 1 else "trivial: at most one candidate delivered"
        return chosen, why, {}, 0.0
    rng = random.Random(seed)
    order = list(delivered)
    rng.shuffle(order)
    ids = {lbl: chr(ord("A") + i) for i, lbl in enumerate(order)}
    cands = "\n\n".join(f"## Candidate {ids[lbl]}\n\n{render.answer_md(pool[lbl])}" for lbl in order)
    mission = prompts.select(bp, len(order)) + f"\n\n# THE QUESTION\n\n{question}\n\n# THE CANDIDATES\n\n{cands}"
    try:
        reply, cost = _editor_call(editor, "# SELECTION\n\n(candidates follow in the message)", mission, max_tokens=8000)
        m = re.search(r"```choice\s*(\S+?)\s*```", reply)
        pick = m.group(1).strip().strip("`") if m else ""
        inv = {v: k_ for k_, v in ids.items()}
        chosen = inv.get(pick.upper(), order[0])
        w = re.search(r"<why>(.*?)</why>", reply, re.S)
        why = (w.group(1).strip() if w else reply.strip())[:2000]
        return chosen, why, ids, cost
    except Exception as e:  # noqa: BLE001
        return order[0], f"selector failed: {e}", ids, 0.0


def run_task_parallel(*, task_id: str, question: str, k: int, base: harness.Tree, lib: Library,
                      run: RunFn, editor: LLM, bp: prompts.BenchPrompts = prompts.FINANCE,
                      out_dir: Path | None = None, log=None, seed: int = 0, workers: int = 2,
                      base_reps: int = 0, extra_arms: dict[str, harness.Tree] | None = None) -> TaskRecord:
    log = log or (lambda s: None)
    rec = TaskRecord(task_id=task_id, k=k)
    out = Path(out_dir) if out_dir else None

    def save(label: str, t: Trajectory) -> None:
        rec.rollouts[label] = t
        if out:
            d = out / "rollouts"
            d.mkdir(parents=True, exist_ok=True)
            (d / f"{label}.json").write_text(json.dumps(t.to_dict(), indent=1), encoding="utf-8")
            (d / f"{label}.md").write_text(render.trajectory_md(t), encoding="utf-8")

    # 1. reference rollouts
    log(f"[{task_id}] rollouts base1..base{k}")
    refs = _pmap(lambda i: run(question, base, f"base{i}"), range(1, k + 1), workers)
    for t in refs:
        save(t.label, t)

    evidence = _evidence(task_id, question, base, refs, lib)

    # 2. propose (INV, DOM) × k, then probe each once
    specs = [(f"{dim.lower()}{i}", dim, i) for i in range(1, k + 1) for dim in ("INV", "DOM")]

    def propose_one(spec):
        lbl, dim, i = spec
        log(f"[{task_id}] propose {lbl}")
        try:
            reply, cost = _editor_call(editor, evidence, prompts.propose(bp, dim, k=k, index=i))
        except Exception as e:  # noqa: BLE001
            reply, cost = "", 0.0
            rec.errors.append(f"{lbl}: editor failed: {e}")
        return _stage_from_reply(lbl, dim, base, reply, cost)

    for st in _pmap(propose_one, specs, workers):
        rec.editor_cost_usd += st.cost_usd
        if st.error:
            rec.errors.append(f"{st.label}: {st.error}")
        rec.stages[st.label] = st
        log(f"[{task_id}] candidate {st.label}: {'KEEP_BASE' if st.keep_base else harness.inventory(st.tree)}")
    cands = [s_ for s_ in rec.stages.values() if s_.dim in ("INV", "DOM")]
    log(f"[{task_id}] rollouts {', '.join(s_.label for s_ in cands)}")
    for t in _pmap(lambda s_: run(question, s_.tree, s_.label), cands, workers):
        save(t.label, t)

    # 3. compose k finals from base + pool, roll out each once
    pool_text = "\n\n".join(render.pool_md(lbl, st.dim, st.notes or st.error, base, st.tree, rec.rollouts[lbl])
                            for lbl, st in rec.stages.items() if st.dim in ("INV", "DOM"))
    def compose_one(i: int) -> Stage:
        lbl = f"agg{i}"
        log(f"[{task_id}] compose {lbl}")
        mission = prompts.aggregate(bp, k=k, index=i) + "\n\n# THE CANDIDATE POOL\n\n" + pool_text
        try:
            reply, cost = _editor_call(editor, evidence, mission)
        except Exception as e:  # noqa: BLE001
            reply, cost = "", 0.0
            rec.errors.append(f"{lbl}: composer failed: {e}")
        return _stage_from_reply(lbl, "AGG", base, reply, cost)

    aggs = _pmap(compose_one, range(1, k + 1), workers)
    for st in aggs:
        rec.editor_cost_usd += st.cost_usd
        if st.error:
            rec.errors.append(f"{st.label}: {st.error}")
        rec.stages[st.label] = st
        log(f"[{task_id}] final {st.label}: {'KEEP_BASE' if st.keep_base else harness.inventory(st.tree)}")
    log(f"[{task_id}] rollouts {', '.join(s_.label for s_ in aggs)}")
    for t in _pmap(lambda s_: run(question, s_.tree, s_.label), aggs, workers):
        save(t.label, t)

    # 4. selection among the k finals (answers only, harnesses hidden)
    finals = [f"agg{i}" for i in range(1, k + 1)]
    rec.chosen, rec.selection_why, rec.selection_ids, cost = blind_select(
        editor, question, {lbl: rec.rollouts[lbl] for lbl in finals}, bp=bp, seed=f"{seed}:{task_id}")
    rec.editor_cost_usd += cost
    if rec.selection_why.startswith("selector failed"):
        rec.errors.append(rec.selection_why)

    # 4b. matched-cost control: extra base rollouts, then the same blind selection over all base
    # runs. This answers "would re-running the base harness and picking blind have done as well?"
    if base_reps > 0:
        extra = [f"ctl{i}" for i in range(2, base_reps + 2)]
        log(f"[{task_id}] control rollouts {', '.join(extra)}")
        for t in _pmap(lambda lbl: run(question, base, lbl), extra, workers):
            save(t.label, t)
        pool = {lbl: rec.rollouts[lbl] for lbl in ["base1", *extra]}
        rec.control_chosen, rec.control_why, _, cost = blind_select(editor, question, pool, bp=bp, seed=f"{seed}:{task_id}:ctl")
        rec.editor_cost_usd += cost

    # 4c. fixed comparison arms (e.g. a hand-written guidance harness), one rollout each
    if extra_arms:
        log(f"[{task_id}] arm rollouts {', '.join(extra_arms)}")
        for t in _pmap(lambda item: run(question, item[1], item[0]), list(extra_arms.items()), workers):
            save(t.label, t)

    # 5. reflect → library
    record = [
        evidence,
        "# CANDIDATES\n\n" + pool_text,
        "# FINALS\n\n" + "\n\n".join(render.pool_md(lbl, "AGG", rec.stages[lbl].notes or rec.stages[lbl].error,
                                                   base, rec.stages[lbl].tree, rec.rollouts[lbl]) for lbl in finals)
        + f"\n\n# DELIVERED\n\nThe answer from `{rec.chosen}` was delivered. Selection note: {rec.selection_why}",
    ]
    try:
        reply, cost = _editor_call(editor, record, prompts.experience(bp), max_tokens=16000)
        rec.editor_cost_usd += cost
        rec.edits_record, rec.experience = _parse_experience(reply)
    except Exception as e:  # noqa: BLE001
        rec.errors.append(f"reflection failed: {e}")
    chosen_tree = rec.stages[rec.chosen].tree if rec.chosen in rec.stages else base
    if has_experience(rec.experience) and chosen_tree != base:
        exp = dict(rec.experience or {})
        exp["edits"] = rec.edits_record
        rec.library_added = lib.add(task_id, chosen_tree, why=rec.selection_why, label=rec.chosen, experience=exp)
    elif has_experience(rec.experience):
        # The reference implementation stores the adopted tree even when it equals the base; the
        # lesson is still worth keeping, so store it with the base tree.
        exp = dict(rec.experience or {})
        exp["edits"] = rec.edits_record
        rec.library_added = lib.add(task_id, chosen_tree, why=rec.selection_why, label=rec.chosen, experience=exp)

    rec.total_cost_usd = sum(t.cost_usd for t in rec.rollouts.values()) + rec.editor_cost_usd
    if out:
        for lbl, st in rec.stages.items():
            harness.write_tree(st.tree, out / "harnesses" / lbl)
            (out / "harnesses" / f"{lbl}.reply.md").write_text(st.reply, encoding="utf-8")
        (out / "record.json").write_text(json.dumps(rec.to_dict(), indent=1), encoding="utf-8")
    return rec


def _parse_experience(reply: str) -> tuple[str, dict | None]:
    edits = re.search(r"<edits>(.*?)</edits>", reply, re.S)
    exp = re.search(r"<experience>(.*?)</experience>", reply, re.S)
    edits_txt = edits.group(1).strip() if edits else ""
    if not exp or "NO_ENTRY" in reply.split("<experience>")[0][-200:]:
        return edits_txt, None
    body = exp.group(1)
    out: dict[str, str] = {}
    for f in ("cue", "lesson", "evidence", "confidence"):
        m = re.search(rf"^{f}:\s*(.+?)(?=^\w+:|\Z)", body, re.S | re.M)
        if m:
            out[f] = " ".join(m.group(1).split())
    return edits_txt, out if has_experience(out) else None
