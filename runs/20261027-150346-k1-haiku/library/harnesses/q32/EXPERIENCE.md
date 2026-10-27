# q32

- adopted: `agg1`
- components: 0 skills; 3,260 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, cite only opened documents, no null-query searches, plain text with no citation markup, verify rather than caveat)
candidates: inv1, dom1 (shorter three-bullet version), agg1
change: Went from empty to a rule set. A snippet is a lead and the primary 10-Q must be opened. Only opened documents may be listed as sources. Plain text, with no unchecked-figures caveat. inv1 and agg1 added a rule against empty queries. They also added a rule to resolve "last N months as of date X" to the year-to-date column of the latest periodic filing, plus a sum check.
observed: base1 ran a null-query web_search, quoted the Q3 press release's "66% vs 71%" line from a snippet, listed that unopened press release as a source, and closed with a caveat that the figures were unchecked against the raw filing. inv1 and dom1 listed only the opened 10-Q and wrote no such caveat. agg1 made a null-query search (turn 2) despite the rule against it. It also listed Financial_Report.xlsx, which it never opened, as a source. It added a claim that "the 10-Q's MD&A also reports a 66% purchase share ... in press coverage", which was not retrieved. The figures were identical in all four runs (69.67% / 30.33%), so the differences are in sourcing and presentation only. Each candidate is one rollout, and the edits were bundled with the task fact (inv1) or the skill (dom1).
verdict: confounded

component: tool_guidance.md (embedded task-fact lead: 10-Q URL, table location, figures)
candidates: inv1
change: Gave the 10-Q URL, the location of the origination table, and the expected figures, labelled "re-confirm in the text".
observed: inv1 skipped discovery and parsed the 10-Q in turn 1. It finished in 3 turns, against 4 for dom1 and agg1 and 5 for base1. It retrieved the same figures the lead gave. The lead saved turns and changed no number. It will not transfer to other questions.
verdict: no observed effect

component: skills/period_mix_from_filing/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill for category-mix questions over a year-to-date window. It names the 10-Q Item 2 table as the source, keeps the quarter and the prior year as labelled context, adds a unit check and a sum check, and carries task facts. A trigger sentence was added to systemprompt.md.
observed: dom1 loaded the skill in turn 1, then parsed the 10-Q and ran one retrieval for exact headers and units. It took 4 turns. inv1 reached the same answer in 3 turns with no skill. The skill added a turn and no visible benefit. Its guidance on labelled context did appear in dom1's answer, but inv1 and agg1 also gave the quarter and prior year as context without the skill. The trigger line cannot be separated from the skill.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in all candidates.
observed: Nothing to observe.
verdict: no observed effect

## Transferable lesson
- **cue**: A simple lookup or mix-percentage question whose answer sits in one table of the latest periodic filing. The base run finds and opens that filing correctly, but it also quotes a press-release sentence from a search snippet, lists the unopened release as a source, and issues a null-query search.
- **lesson**: In tool_guidance.md, state that only documents actually parsed and retrieved from may be listed as sources or quoted. A figure or sentence seen only in a snippet is left out or labelled snippet-only. Also say never to send a null or empty search query. Do not add a skill, because the procedure is one table retrieval and a sum check, and a skill-equipped run took an extra turn with the same answer. Also check that no source appears in the final list without a retrieval, because one adopted candidate carrying such a rule still listed an unopened Financial_Report.xlsx.
- **evidence**: The tool_guidance.md row. base1 listed the unopened press release and sent a null query, while inv1 and dom1 listed only the opened 10-Q. agg1 carried the same rule but still sent a null query and listed an unopened xlsx, which shows the rule alone is not enforced. The skill row shows dom1 needed one more turn than skill-free inv1 for an identical answer.
- **confidence**: low. Each candidate is one rollout, and the sourcing rules were bundled with a task-fact lead or a skill. All four runs gave the same numbers, so the evidence concerns sourcing hygiene and not accuracy.
