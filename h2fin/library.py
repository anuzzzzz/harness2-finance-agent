"""The improvement harness: adopted harnesses plus evidence-backed lessons from earlier tasks.

    <root>/INDEX.md
    <root>/harnesses/<task_id>/harness/<rel>
    <root>/harnesses/<task_id>/EXPERIENCE.md

Only entries whose reflection produced a real lesson (cue + lesson + evidence) are stored, as in
the reference implementation.
"""

from __future__ import annotations

import re
from pathlib import Path

from . import harness


def has_experience(exp: dict | None) -> bool:
    return isinstance(exp, dict) and all(isinstance(exp.get(k), str) and exp[k].strip()
                                         for k in ("cue", "lesson", "evidence"))


class Library:
    def __init__(self, root: Path, *, max_context_chars: int = 60_000):
        self.root = Path(root)
        self.max_context_chars = max_context_chars

    @property
    def index(self) -> Path:
        return self.root / "INDEX.md"

    def entries(self) -> list[str]:
        d = self.root / "harnesses"
        return sorted(p.name for p in d.iterdir() if p.is_dir()) if d.is_dir() else []

    def add(self, task_id: str, tree: harness.Tree, *, why: str, label: str, experience: dict | None) -> bool:
        if not has_experience(experience):
            return False
        d = self.root / "harnesses" / task_id
        harness.write_tree(tree, d / "harness")
        exp = experience or {}
        lines = [f"# {task_id}", "", f"- adopted: `{label}`", f"- components: {harness.inventory(tree)}", ""]
        if why.strip():
            lines += ["## Why this was chosen", why.strip(), ""]
        if exp.get("edits"):
            lines += ["## What each edit did", str(exp["edits"]).strip(), ""]
        lines += ["## Transferable lesson"]
        lines += [f"- **{f}**: {str(exp[f]).strip()}" for f in ("cue", "lesson", "evidence", "confidence") if exp.get(f)]
        (d / "EXPERIENCE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        self.rebuild_index()
        return True

    def rebuild_index(self) -> None:
        rows = ["# Library", "",
                "Each entry is an earlier task whose harness was chosen, stored with its full "
                "component tree and why it was picked.", ""]
        names = self.entries()
        if not names:
            rows.append("_(empty — this is the first task)_")
        for name in names:
            ed = self.root / "harnesses" / name
            tree = harness.read_tree(ed / "harness")
            cue = _field(ed / "EXPERIENCE.md", "cue")
            rows += [f"## `harnesses/{name}/`", f"- harness: {harness.inventory(tree)}"]
            if cue:
                rows.append(f"- cue: {cue}")
            rows.append("")
        self.root.mkdir(parents=True, exist_ok=True)
        self.index.write_text("\n".join(rows) + "\n", encoding="utf-8")

    def context_text(self) -> str:
        """The library as prompt text (most recent entries first, under a char cap)."""
        names = self.entries()
        if not names:
            return ""
        parts = ["# LIBRARY: adopted harnesses from earlier tasks", self.index.read_text(encoding="utf-8")]
        total = sum(len(p) for p in parts)
        for name in reversed(names):
            ed = self.root / "harnesses" / name
            block = "\n".join([f"## Entry `{name}`", (ed / "EXPERIENCE.md").read_text(encoding="utf-8"),
                               "### Harness files", harness.render(harness.read_tree(ed / "harness")), ""])
            if total + len(block) > self.max_context_chars:
                parts.append(f"_(older entries omitted for length: {name} and earlier)_")
                break
            parts.append(block)
            total += len(block)
        return "\n\n".join(parts)


def _field(path: Path, name: str) -> str:
    if not path.is_file():
        return ""
    m = re.search(rf"^- \*\*{name}\*\*:\s*(.+)$", path.read_text(encoding="utf-8"), re.M)
    return m.group(1).strip() if m else ""
