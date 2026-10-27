# q10

- adopted: `agg1`
- components: 0 skills; 3,435 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: a snippet or memory is a lead, and every endpoint figure must be retrieved from an opened primary document; cite only opened documents; plain text with no markup; no empty-query searches; read all years from the latest 10-K's three-year table)
candidates: inv1, dom1, agg1
change: The base file was empty and all three candidates replaced it with a rule set. The rules require the end value, not just the start value, to be retrieved from an opened filing. They prefer the single latest 10-K because it carries three years of columns. They allow only opened documents as sources, ban recollection remarks, and require a re-check of the period count (2022 to 2024 is 2 years). inv1 and agg1 also said to carry full precision and round only at the end.
observed: base1 parsed only the FY2023 10-K. It took the FY2024 revenue from a search snippet, then wrote that the FY2024 10-K MD&A "shows" it. It listed the unopened FY2024 10-K and a Bullfincher page as sources, included an aside about its own wrong recollection, and issued a null-query search. inv1, dom1 and agg1 each parsed the FY2024 10-K in turn 1 or 2 and retrieved 2,865,507 and 1,905,871 from its income statement. Each listed only opened documents, and none made a null-query search or an aside. The CAGR of 22.62% was the same in all four runs, so the difference is in verification and sourcing, not the number. inv1 also listed the FY2023 10-K as a source and said it matched the 2022 figure. That claim was not backed by a retrieval from that filing in this run. Each candidate is a single rollout.
verdict: confounded

component: tool_guidance.md (Palantir task-fact block with the 10-K URLs and revenue figures)
candidates: inv1
change: Embedded the FY2024 and FY2023 10-K URLs and the revenue values, labelled to be re-confirmed. It marked the FY2024 figure as unverified.
observed: inv1 skipped discovery search, parsed the FY2024 10-K in turn 1 and finished in 3 turns, against 4 for agg1 and 5 for dom1. agg1 had no lead and still reached the same filing with one edgar_search. The figures were identical. The lead saved at most a turn or two. It carries no value for other companies.
verdict: no observed effect

component: skills/multi_year_cagr/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill for CAGR. It covers the period count, taking both endpoints from the same statement, units, a total-growth cross-check and an answer contract, and it carries the Palantir facts. systemprompt.md gained a sentence telling the agent to load it.
observed: dom1 called load_skill first, then edgar_search, parse, one retrieval and submit, taking 5 turns. inv1 and agg1 had no skill and reached the same answer in 3 and 4 turns. dom1's answer added a total-growth cross-check of 50.35% and a note that both endpoints came from one filing. The skill was bundled with its own tool_guidance rules, so its separate effect is not isolated. No extra accuracy is visible, and it cost extra turns.
verdict: no observed effect

component: systemprompt.md, LongTermMEMORY.md, guardrails.md
candidates: dom1 (systemprompt trigger line only); none for the others
change: dom1 added one trigger sentence to systemprompt.md. Memory and guardrails stayed empty in all candidates.
observed: dom1 loaded the skill first. No run isolates the trigger from the skill.
verdict: no observed effect

## Transferable lesson
- **cue**: A simple multi-year growth or ratio question (CAGR, YoY) where the latest 10-K's three-year comparative table covers both endpoints. The base run opens only an older filing, takes the newer endpoint from a search snippet, and then cites the unopened latest filing as the source of that figure.
- **lesson**: In tool_guidance.md, state that every figure entering the calculation, the end value as well as the start value, must be retrieved from a parsed primary document. Say to open the latest 10-K first and read all needed years from its single comparative table, and to list as sources only documents actually retrieved from. Do not add a skill for the CAGR arithmetic, because it is one line and the skill-equipped run only added turns.
- **evidence**: The tool_guidance.md row, which is confounded because all three candidates carried similar rules and each is one rollout. base1 took the end value from a snippet, listed unopened sources, and made a null-query search. inv1, dom1 and agg1 each parsed the FY2024 10-K, retrieved both endpoints from its table, and listed only opened documents. The skill row shows no gain from the skill, since the skill-free runs were equally correct and faster.
- **confidence**: low. One rollout per candidate, and the rules were bundled with task-fact leads or a skill in some runs. The number was the same everywhere, so the record shows only a difference in sourcing and verification.
