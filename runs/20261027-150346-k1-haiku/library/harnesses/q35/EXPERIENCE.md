# q35

- adopted: `agg1`
- components: 0 skills; 3,898 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, open the primary document, cite only opened documents, plain text with no citation markup, no empty-query searches)
candidates: inv1, dom1, agg1
change: Went from empty to a short rule set. Open the primary 8-K EX-99.1 or filing with parse_html_page and confirm figures with retrieve_information. List only documents that were opened. Write the answer in plain text with no `<cite>` tags. Never run a null-query web_search. inv1 and agg1 also added a note that PDFs cannot be parsed, and a rule that listed components must sum to the stated total.
observed: base1 opened with a null-query web_search, then an edgar_search, a second null-query web_search, a parse and a retrieve. That took 4 turns. Its final answer leaked raw `<cite index=...>` markup and listed a Nasdaq mirror it never opened. inv1, dom1 and agg1 went straight to parse_html_page and one retrieve_information, finishing in 2-3 turns. None leaked markup, and each listed only the opened 8-K. All four runs gave the same figure, SBC $1,935M, and the reconciliation summed to 4,052 in each. All three edited candidates also carried a task-fact lead with the exact URL, which may account for the direct route, so the rules cannot be separated from the lead. Each candidate is one rollout.
verdict: confounded

component: tool_guidance.md ("largest adjustment" ranking rule: rank by absolute value, give the sign and direction, name the runner-up)
candidates: inv1, dom1, agg1
change: Added a rule for non-GAAP "largest adjustment" questions. Retrieve the whole reconciliation, rank by absolute size, state whether each item is an add-back or a deduction, and name a close runner-up. In dom1 and agg1 this sat in a dedicated bullet block, and in inv1 it was a single bullet.
observed: SBC +1,935 and Other (income) expense, net (1,844) are close in size and opposite in sign. base1 mentioned the runner-up only in passing and said its content was net unrealized gains. inv1, dom1 and agg1 each stated the sign and the runner-up explicitly. agg1 added that the largest add-back and the largest absolute item are the same line. The answer was SBC in every run, so the rule changed explanation and not the result. No candidate went without it, so its separate effect is not shown.
verdict: confounded

component: tool_guidance.md (task-fact lead: Uber Q4 2023 8-K EX-99.1 URL and the reconciliation figures)
candidates: inv1, dom1, agg1
change: Each embedded the release URL and the figures (SBC 1,935, Other (1,844), total 4,052), labelled "re-confirm in the text".
observed: All three skipped discovery search and parsed the release in turn 1. base1 needed web_search and edgar_search to find it. All three retrieved the figures from the opened text, not from the lead. inv1 finished in 2 turns and dom1 and agg1 in 3, so the lead saved turns without changing the answer. Putting task facts in always-on text carries no transfer value, and it did not alter the outcome here.
verdict: no observed effect

component: systemprompt.md, skills/, LongTermMEMORY.md, guardrails.md
candidates: none changed them
change: Left unchanged. No skill was added in any candidate.
observed: None. The task was one retrieval from one document, and all runs completed it without a skill.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks for the largest or smallest line in a non-GAAP reconciliation (adjustment, add-back). The full-year table is in one earnings-release exhibit. The base run gets the right figure but leaks `<cite>` markup, lists an unopened mirror or secondary page as a source, and wastes turns on empty-query searches.
- **lesson**: In tool_guidance.md, state four things. Retrieve the entire reconciliation table with signs and check that it sums to the reported total. Rank by absolute value and state each top item's direction, naming a close opposite-signed runner-up. Cite only documents that were parsed and retrieved from. Write the answer in plain text with no citation markup, and never issue an empty-query search. Do not add a skill, since this is a single retrieval.
- **evidence**: tool_guidance rows. base1 leaked `<cite>` tags, listed the unopened Nasdaq page and began with null-query searches, over 4 turns. inv1, dom1 and agg1 all parsed the 8-K once, retrieved the full table, confirmed the 4,052 sum, named the (1,844) runner-up with its sign, and listed only the opened 8-K, in 2-3 turns. The figure ($1,935M) was identical across all runs, so the contrast is in presentation and sourcing, not accuracy.
- **confidence**: low. One rollout per candidate, the rules and the task-fact lead were bundled in every edited run, and the number did not change.
