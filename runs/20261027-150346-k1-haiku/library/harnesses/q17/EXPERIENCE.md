# q17

- adopted: `agg1`
- components: 0 skills; 3,350 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, cite only opened documents, plain text with no citation markup, no empty-query search)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. Open the primary 10-K with parse_html_page and confirm each figure with retrieve_information. List only documents that were retrieved from. Write plain text with no `<cite>` tags. Never run an empty-query web_search. inv1 and agg1 added comparative-column sourcing and a PDF note. dom1 had a shorter four-bullet version.
observed: base1 began with an empty-query web_search. Its answer leaked raw `<cite index>` markup and listed the FY2022 10-K, which it never parsed. inv1, dom1 and agg1 produced no markup in the final answer and made no empty-query search. inv1 and dom1 listed only the two 10-Ks they parsed, and inv1 and dom1 noted that FY2022 GBV came from the FY2023 10-K's comparative column. agg1 parsed the FY2022 10-K and retrieved from it before listing it, so its source list was honest. All four runs gave the same 13.29%, 13.54% and 13.57%. Each candidate is a single rollout. In inv1 the rules came with a task-fact lead, and in dom1 with a skill.
verdict: confounded

component: tool_guidance.md (comparative-columns rule: take each year from the latest filing that carries it, and open an older 10-K only if a year is missing)
candidates: inv1, agg1
change: A multi-year ratio rule. Use the latest filing's comparative columns, cross-check a year that appears in two filings, and say which filing supplied each figure. inv1 told the agent to take FY2022 from the FY2023 10-K. agg1 said to open the older 10-K only when a year is missing.
observed: inv1 parsed the FY2024 and FY2023 10-Ks in turn 1 and finished in 3 turns. agg1 first parsed only the FY2024 10-K, found that it lacked FY2022 GBV, then searched for and parsed the FY2022 10-K, and took 7 turns. inv1's task-fact lead named the right two filings, which agg1 did not have. So the speed difference tracks the lead and not the rule.
verdict: confounded

component: tool_guidance.md (task-fact lead: Airbnb inputs, URLs, resulting rates)
candidates: inv1
change: Embedded the revenue and GBV figures, the 10-K URLs, and the note that the FY2022 10-K was never opened. agg1 removed this from its version.
observed: inv1 parsed both 10-Ks directly, with no search, and finished in 3 turns at $0.218. The figures were still retrieved from the opened text. agg1, without the lead, searched and took 7 turns at $0.225. dom1, with its skill lead, took 4 turns at $0.218. The answers were identical. The lead saved turns only. It carries no value for other tasks.
verdict: no observed effect

component: skills/marketplace_take_rate/SKILL.md and the systemprompt.md trigger line
candidates: dom1
change: An on-demand skill giving the ratio definition, where the volume metric and revenue live, the point that the latest 10-K covers only two years of GBV, the answer shape (one line per year plus one sentence), and percentage-point changes from unrounded values. It carried the verified Airbnb facts. The system prompt got a line telling the agent to load it.
observed: dom1 loaded the skill in turn 1 and parsed both 10-Ks in turn 2. It gave the tightest answer, with one line per year, a trend sentence and unrounded ratios. It took one more turn than inv1, which had no skill. Its +0.04 and 0.29 point figures come from unrounded math, while the agg1 and inv1 comments use roughly +0.03 and 0.28. The effect cannot be separated from dom1's tool_guidance rules or from the skill's embedded task facts.
verdict: confounded

component: tool_guidance.md (answer-shape rule: follow the shape the question asks for, such as one line per year and a one-sentence comment)
candidates: agg1
change: A single sentence telling the agent to follow the requested answer shape before listing inputs and calculations.
observed: agg1's answer gave three year lines and a comment, but its comment sentence was long, and caveats and basis sections followed. The inv1 and dom1 answers were similar in shape without this rule (dom1's skill had a similar contract). The base1 answer was longer, with a context paragraph. No clean contrast.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A multi-year ratio or trend question where the latest 10-K carries three years of the numerator but only two years of the denominator metric. The base run is numerically right but its final answer lists an earlier-year filing it never opened and leaks citation markup.
- **lesson**: In tool_guidance.md, state that each year's inputs come from the latest filing's comparative columns. If a year is missing, open the older filing and retrieve from it before listing it, and say which filing supplied each figure. Add that only documents retrieved from may be listed as sources, that the answer is plain text with no citation markup, and that empty-query searches are not allowed. Do not add a skill for a ratio that needs two retrievals and a division.
- **evidence**: tool_guidance rows. base1 leaked `<cite>` markup and listed the unopened FY2022 10-K. inv1, dom1 and agg1 produced clean plain-text answers with source lists that matched what they opened. agg1 opened the FY2022 10-K and retrieved from it before citing it. inv1 and dom1 used the FY2023 10-K comparative column and said so. All four gave the same ratios, so the contrast is in sourcing and presentation, not accuracy. dom1's skill added a turn and nothing visible beyond what the guidance already gave.
- **confidence**: low. One rollout per candidate. The sourcing rules were bundled with task-fact leads or a skill in every edited run. The figures did not change across runs. This is the same pattern seen in earlier entries (q35, q44, q45, q47).
