"""The editable harness: a small tree of files around a frozen model.

Surface (the subset of Harness²'s eight components that an API tool loop can carry):

    systemprompt.md            role and procedure        ALWAYS ON
    guardrails.md              standing rules            ALWAYS ON
    LongTermMEMORY.md          durable domain facts      ALWAYS ON
    tool_guidance.md           how to use the tools      ALWAYS ON
    skills/<name>/SKILL.md     reusable workflow         ON DEMAND via the load_skill tool

Scripts, subagents and plugins are not on this surface: the executor is a Messages API tool
loop, not a coding agent, so there is nowhere for them to run. That is a deliberate narrowing
and the README says so.
"""

from __future__ import annotations

import difflib
import os
import re
from pathlib import Path

from . import config

Tree = dict[str, str]

ALWAYS_ON = ("systemprompt.md", "guardrails.md", "LongTermMEMORY.md", "tool_guidance.md")
SKILL_RE = re.compile(r"^skills/([A-Za-z0-9_-]+)/SKILL\.md$")

# vals-ai/finance-agent INSTRUCTIONS_PROMPT (MIT), with the question moved to the user turn.
BASE_SYSTEM_PROMPT = f"""\
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is {config.AS_OF_DATE_HUMAN}.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When you have the final answer, you should call the `submit_final_result` tool with it. Your submission will not be processed unless you call this tool.

You should include any necessary step-by-step reasoning, justification, calculations, or explanation in your answer. You will be evaluated both on the accuracy of the final answer, and the correctness of the supporting logic.

When possible, please provide any calculated answers to at least two decimal places (e.g. 18.78% rather than 19%). Please do not round intermediate steps in any calculations - you should only round your final answer.

At the end of your answer, you should provide your sources in a dictionary with the following format:
{{
    "sources": [
        {{
            "url": "https://example.com",
            "name": "Name of the source"
        }},
        ...
    ]
}}
"""


# A control arm: the one rule a person would write after watching the base agent answer from web
# snippets. Hand-written once, never edited by the loop. If Harness² only ties this, all it found
# was the obvious.
STATIC_TOOL_GUIDANCE = """\
# Tool guidance

- Answer from primary documents. Find the relevant SEC filing with edgar_search (company, form type, date range), open it with parse_html_page, and read the figures with retrieve_information. Web search results and third-party sites are leads, not evidence.
- Before using a figure, check that its period, units and basis match the question. Show the calculation.
- Call submit_final_result with the answer and its sources before running out of turns.
"""


def static_tree() -> Tree:
    t = base_tree()
    t["tool_guidance.md"] = STATIC_TOOL_GUIDANCE
    return t


def base_tree() -> Tree:
    return {
        "systemprompt.md": BASE_SYSTEM_PROMPT,
        "guardrails.md": "",
        "LongTermMEMORY.md": "",
        "tool_guidance.md": "",
    }


def skills_of(tree: Tree) -> dict[str, str]:
    out = {}
    for rel, body in tree.items():
        m = SKILL_RE.match(rel)
        if m:
            out[m.group(1)] = body
    return out


def always_on_text(tree: Tree) -> str:
    return "\n".join(tree.get(f, "") for f in ALWAYS_ON)


def system_blocks(tree: Tree) -> list[dict]:
    """The executor's system prompt, assembled from the always-on components."""
    parts = [tree.get("systemprompt.md", "").strip()]
    for fname, heading in (("guardrails.md", "Standing rules"),
                           ("LongTermMEMORY.md", "Durable facts"),
                           ("tool_guidance.md", "Tool guidance")):
        body = tree.get(fname, "").strip()
        if body:
            parts.append(f"# {heading}\n\n{body}")
    text = "\n\n".join(p for p in parts if p)
    return [{"type": "text", "text": text, "cache_control": {"type": "ephemeral"}}]


def validate(tree: Tree) -> list[str]:
    """Return the reasons a tree is unusable (empty list = valid). Mirrors Harness²'s
    'discard the whole proposal' rules, restricted to this surface."""
    errors: list[str] = []
    for rel in tree:
        if rel not in ALWAYS_ON and not SKILL_RE.match(rel):
            errors.append(f"{rel}: not on the editable surface")
    sp = tree.get("systemprompt.md", "")
    if not sp.strip():
        errors.append("systemprompt.md is empty")
    for needle, what in ((config.AS_OF_DATE_HUMAN, "the as-of date"), ("submit_final_result", "the submit instruction"),
                         ('"sources"', "the sources format")):
        if needle not in sp:
            errors.append(f"systemprompt.md no longer contains {what} ({needle!r}); the task frame must survive edits")
    on = always_on_text(tree)
    if len(on) > config.ALWAYS_ON_CHAR_CAP:
        errors.append(f"always-on text is {len(on):,} chars; cap is {config.ALWAYS_ON_CHAR_CAP:,}")
    trigger_text = tree.get("systemprompt.md", "") + "\n" + tree.get("guardrails.md", "")
    for name, body in skills_of(tree).items():
        fm = re.match(r"^---\n(.*?)\n---", body, re.S)
        if not fm:
            errors.append(f"skills/{name}/SKILL.md: missing YAML frontmatter")
            continue
        head = fm.group(1)
        nm = re.search(r"^name:\s*(.+)$", head, re.M)
        if not nm or nm.group(1).strip().strip('"') != name:
            errors.append(f"skills/{name}/SKILL.md: frontmatter name must be '{name}'")
        if not re.search(r"^description:\s*\S", head, re.M):
            errors.append(f"skills/{name}/SKILL.md: frontmatter needs a description")
        if name not in trigger_text:
            errors.append(f"skills/{name}/SKILL.md: '{name}' is never named in systemprompt.md or "
                          f"guardrails.md (no trigger line)")
    return errors


# --------------------------------------------------------------------------- editor output

FILE_RE = re.compile(r'<file\s+path="([^"]+)">\n?(.*?)</file>', re.S)
DELETE_RE = re.compile(r'<delete\s+path="([^"]+)"\s*/>')
NOTES_RE = re.compile(r"<notes>(.*?)</notes>", re.S)


def apply_patch(base: Tree, reply: str) -> tuple[Tree, str, bool]:
    """Apply an editor reply to `base`. Returns (new_tree, notes, keep_base)."""
    notes_m = NOTES_RE.search(reply)
    notes = notes_m.group(1).strip() if notes_m else ""
    files = FILE_RE.findall(reply)
    deletes = DELETE_RE.findall(reply)
    if not files and not deletes:
        return dict(base), notes or reply.strip()[:2000], True
    tree = dict(base)
    for rel in deletes:
        tree.pop(rel.strip(), None)
    for rel, body in files:
        rel = rel.strip()
        body = body.rstrip("\n") + "\n" if body.strip() else ""
        tree[rel] = body
    keep = all(tree.get(k) == base.get(k) for k in set(tree) | set(base))
    return tree, notes, keep


def diff(base: Tree, tree: Tree) -> str:
    out = []
    for rel in sorted(set(base) | set(tree)):
        a = base.get(rel, "")
        b = tree.get(rel, "")
        if a == b:
            continue
        d = difflib.unified_diff(a.splitlines(), b.splitlines(), fromfile=f"base/{rel}",
                                 tofile=f"new/{rel}", lineterm="", n=2)
        out.append("\n".join(d))
    return "\n\n".join(out) if out else "(no changes from base)"


def render(tree: Tree) -> str:
    """The whole tree as fenced files, for prompts."""
    parts = []
    for rel in sorted(tree, key=lambda r: (r not in ALWAYS_ON, r)):
        body = tree[rel]
        parts.append(f'<file path="{rel}">\n{body.rstrip()}\n</file>' if body.strip()
                     else f'<file path="{rel}">\n(empty)\n</file>')
    return "\n\n".join(parts)


def inventory(tree: Tree) -> str:
    sk = len(skills_of(tree))
    return f"{sk} skill{'s' if sk != 1 else ''}; {len(always_on_text(tree)):,} always-on chars"


def write_tree(tree: Tree, root: Path) -> None:
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    for rel, body in tree.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8")


def read_tree(root: Path) -> Tree:
    root = Path(root)
    tree: Tree = {}
    for p in root.rglob("*"):
        if p.is_file():
            rel = p.relative_to(root).as_posix()
            tree[rel] = p.read_text(encoding="utf-8")
    return tree
