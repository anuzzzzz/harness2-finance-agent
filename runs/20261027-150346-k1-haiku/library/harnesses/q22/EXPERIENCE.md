# q22

- adopted: `agg1`
- components: 0 skills; 4,501 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (headline-basis rule: use figures as printed in the same table, show the narrative-precision version as a labelled alternate, never build an input by adding a reported change to another year's figure)
candidates: inv1, agg1 (dom1 carried the same rule inside its skill)
change: The base file was empty. The rule fixes the headline ratio on the printed Key Business Metrics table values and demotes the one-decimal narrative counts to an alternate. It also forbids a derived input.
observed: base1 headlined $160.56, $163.44 and $166.40. The 2024 figure used a derived 491.5M nights (448.2 + 43.3), which no filing prints, and the table-based figures sat in a caveat. inv1, dom1 and agg1 all headlined $160.44, $163.51 and $166.23 from the printed tables, and gave $160.56 and $163.44 as labelled alternates. They also said that no precise 2024 total exists. The change is visible in the headline numbers and in the framing. The same task-fact block was present in inv1 and agg1, and dom1 had its own skill, so the rule cannot be separated from those leads. Which basis is the "right" one is a judgment call.
verdict: confounded

component: tool_guidance.md (plan the fewest filings; no null-query searches)
candidates: inv1, agg1
change: Told the agent that each 10-K's comparative table covers two or three years, so it should not open a filing whose years another opened filing already covers. Also banned empty or null web_search queries.
observed: base1 opened all three 10-Ks, including the FY2022 one, which was redundant, and issued a null-query web_search in turn 2. inv1 and agg1 opened only the FY2024 and FY2023 10-Ks and finished in 3 turns, with no web_search at all. dom1 also opened two 10-Ks but took 5 turns. This was a turn and cost reduction (about $0.22 against $0.45). The Airbnb URLs in the same file also let the agents skip discovery, so the effects overlap.
verdict: confounded

component: tool_guidance.md (Airbnb task-fact block: 10-K URLs and verified table values)
candidates: inv1, agg1
change: Listed the FY2024 and FY2023 10-K URLs, the verified table values and the precomputed ratios.
observed: inv1 and agg1 parsed both URLs in turn 1 and skipped discovery. Their retrieved values matched the leads, so no figure changed. These are task-specific facts that save turns, and the agents did re-retrieve the values from the opened text.
verdict: helped

component: skills/kpi_ratio_from_reported_metrics/SKILL.md plus the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill carrying the same headline-basis procedure and the task facts, and a one-line trigger in systemprompt.md.
observed: dom1 called load_skill first, then ran an edgar_search and then parsed the two 10-Ks. It took 5 turns against 3 for the skill-free inv1 and agg1, and reached the identical answer. The extra turns came from the load_skill call and the discovery search. The skill and the trigger line were never run separately.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A multi-year per-unit ratio question (such as GBV per night) built from a company KPI table that is printed rounded to whole millions. The same 10-K narrative gives one-decimal counts for some years but not for the latest year. The base run mixes the narrative counts with a count it derives by adding a reported change.
- **lesson**: In tool_guidance.md, state which basis the headline ratio uses: the figures as printed in one table, from the fewest filings that cover the years asked. Show any narrative-precision ratio beneath it as a labelled alternate, and bar building an input by adding a reported delta to another year's figure. Keep this as always-on tool_guidance text and do not add a skill, because the procedure is short.
- **evidence**: The headline-basis row and the fewest-filings row. base1 headlined $160.56, $163.44 and $166.40, with the 2024 input derived as 448.2 + 43.3. inv1, dom1 and agg1 headlined the printed-table ratios of $160.44, $163.51 and $166.23. Each gave the narrative alternates, said no precise 2024 count exists, and opened two filings instead of three. The skill row shows the skill-equipped run needing 5 turns against 3 for the skill-free runs, with the same answer.
- **confidence**: low. There was one rollout per candidate, and the rules came bundled with a task-fact block in every edited run. Whether the printed-table basis or the narrative-precision basis is the better headline is a judgment call that the record does not settle.
