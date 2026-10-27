# q02

- adopted: `agg1`
- components: 1 skill; 2,998 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. A snippet is a lead, not evidence. Open each primary 10-K with parse_html_page, then run retrieve_information one figure at a time. Never send an empty query. Cite only opened documents. Write plain text with no citation markup. inv1 added a plan for multi-year questions needing two 10-Ks, a recalculation and narrative-consistency check, and an embedded block of Netflix leads. dom1 kept a four-bullet version. agg1 kept the general rules and dropped the task leads.
observed: base1 ran one edgar_search and two web_searches, one of them with a null query. It never parsed or retrieved anything, and it leaked <cite> markup. It listed unopened filings (the FY2022 ARS PDF, the FY2023 10-K) as sources and attributed the 2020-2022 figures to the PDF. Its narrative also called a $0.09 move "sharp". inv1, dom1 and agg1 all parsed 10-Ks and retrieved the ARM values from them. None leaked markup, and each listed only opened filings. The headline numbers were the same in all four runs: $10.82 to $11.70, +$0.88, +8.13%. The effect was on verification and sourcing, not on the figure. Every edited run also carried other edits, so the rules cannot be isolated. Each candidate is one rollout.
verdict: confounded

component: tool_guidance.md (embedded Netflix lead block with URLs and the six ARM values)
candidates: inv1
change: Embedded the metric's name (ARM), the consolidated-versus-regional warning, the annual values and the 10-K URLs, labelled unverified.
observed: inv1 skipped discovery and parsed the FY2024 and FY2019 10-Ks in turn 1. It then opened the FY2021 and FY2020 10-Ks separately and took 9 turns, against 4 for dom1 and agg1. Its values matched the lead. It gained per-year driver text for 2020 and 2021, which dom1 and agg1 lacked. The lead mostly saved the discovery search, did not change a figure, and carries no transfer value.
verdict: no observed effect

component: skills/multi_year_kpi_trend/SKILL.md
candidates: dom1, agg1
change: Added an on-demand skill covering six steps. Map the question's term to the company's own KPI. Plan which 10-Ks cover the window, using three-year comparative columns. Use the company-wide row and label reported versus constant-currency figures. Compute change, % change and CAGR with the correct year count, plus each YoY change. Finish with an answer contract. agg1's version added an overlap/restatement check and a "say plainly when a driver was not retrieved" rule. Both carry Netflix leads.
observed: Both skill runs loaded it in turn 1. They then parsed three 10-Ks (FY2024, FY2022, FY2019) and ran one retrieval each, then submitted in 4 turns. That is about half the turns of inv1, with the same figures. Both added CAGR (1.58%) and per-year changes, and both said which period carried the gain. agg1 stated that the 2020 and 2021 drivers were not retrieved. dom1 said the same for 2021 and 2023, but it left 2020 undeclared. inv1, which had no skill, also produced CAGR and a year table, so the output is similar. The skill did save turns by pre-planning the filings, but the run that carried its content as an always-on lead (inv1) is not a clean comparison.
verdict: confounded

component: systemprompt.md (trigger line for load_skill multi_year_kpi_trend)
candidates: dom1, agg1
change: Added one sentence telling the agent to load the skill for multi-year KPI questions.
observed: Both runs called load_skill as their first action. No skill-equipped run lacks the trigger, so its separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: No change.
verdict: no observed effect

## Transferable lesson
- **cue**: A multi-year trend question about a company-reported KPI (ARPU/ARM, subscribers, margin). Each 10-K shows only about three years of the metric. The base run answers from snippets, opens no filing, leaks citation markup, and lists unopened filings and PDFs as sources.
- **lesson**: In tool_guidance.md, require every yearly value to be retrieved from an opened 10-K (parse_html_page, then retrieve_information). Tell the agent to choose the filings whose three-year comparative columns cover the window before searching. Say to cite only opened documents, to state plainly which years' drivers were not retrieved, and to write plain text with no citation markup. Keep the CAGR and year-by-year procedure in a skill or in always-on text, but do not count on it to enforce sourcing.
- **evidence**: The tool_guidance.md row shows base1 opening nothing, leaking markup and listing unopened filings. inv1, dom1 and agg1 opened 10-Ks and cited only those. The skill row shows both skill runs finishing in 4 turns on three planned 10-Ks, against 9 turns for the skill-free inv1. That row is confounded.
- **confidence**: low. Each candidate is a single rollout, the rules were bundled with a skill or a lead in every edited run, and the headline numbers were identical across all four runs. The evidence supports a difference in sourcing and verification behavior, plus a possible turn saving from planning filings up front, not a difference in accuracy.
