# q29

- adopted: `agg1`
- components: 0 skills; 3,997 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: numeric CIK for edgar_search, no null-query web_search, snippet is a lead, cite only opened documents, plain text with no citation markup)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. It requires a numeric CIK and bans empty queries. It treats snippets as leads, allows only opened documents as sources and bans citation markup.
observed: base1 failed edgar_search with the ticker "SAVE", ran a null-query web_search, and listed an unopened Simple Flying article as a "cross-check". inv1, dom1 and agg1 each parsed the 10-K in their first or second turn, made no failed or null calls, and listed only the 10-K. None cited an article. All three also carried a task lead with the CIK and 10-K URL, which removed the need for any discovery search. So the rules and the lead cannot be separated. Each is a single rollout.
verdict: confounded

component: tool_guidance.md (list-question procedure: copy the filing's own table, re-ask if retrieval is truncated, confirm row count, mark non-GAAP and non-additive rows)
candidates: inv1, agg1 (dom1 carried the same content in its skill)
change: Tells the agent to retrieve the whole KPI table in a dedicated call, re-ask on truncation, check the row count, and flag averages, rates and non-GAAP rows. It also says to keep metrics from elsewhere in the filing in a separate, labelled line.
observed: base1's retrieval was truncated, and it wrote "I pulled the full 10-K to confirm the remaining rows" without a second retrieval. inv1 got all 16 rows in one call. agg1 ran an extra verbatim retrieval and quoted the table with footnote (B). dom1 reported the footnote. All three reached the same 16 rows and values as base1, so the table was already complete in base1. The effect is on verification and presentation (row count, non-GAAP labels, a unit column), not on the figures.
verdict: confounded

component: tool_guidance.md (task-fact lead: CIK, 10-K URL, table name; inv1 also listed the 16 rows and values)
candidates: inv1, dom1, agg1
change: Pre-seeded the location of the KPI table, labelled "re-confirm". inv1 also listed all 16 FY2024 values. dom1 put the row values in its skill. agg1 kept only the CIK, URL and table name.
observed: All three skipped discovery and parsed the 10-K in turn 1 or 2. inv1 finished in 3 turns and agg1 in 4. dom1's final answer said the table "matches the task's reference list", which is unsupported wording induced by the seeded values. The lead saved turns without changing any figure. The row values add nothing, because the table is retrieved anyway.
verdict: helped (for turns); the seeded values were a mild hazard (dom1)

component: skills/company_kpi_list_from_10k/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill covering the KPI-list procedure and answer contract, plus a systemprompt line telling the agent to load it.
observed: dom1 loaded the skill in turn 1 and then took 4 turns, against 3 for inv1 (no skill) and 4 for agg1 (no skill). All three gave the same 16-row table. dom1's footnote and non-GAAP notes were also present in agg1's skill-free answer. No behavior is visible that the skill-free runs lacked.
verdict: no observed effect

component: systemprompt.md (trigger line only)
candidates: dom1
change: One sentence telling the agent to load the skill for KPI-list questions.
observed: dom1 called load_skill first. No skill-free run shows the trigger's separate effect.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A "list the company's KPIs/operating statistics for fiscal year X" question answerable from one table in the latest 10-K's MD&A. The base run already finds the right table, but it uses a ticker where a CIK is required, issues a null-query search, lists an unopened secondary article as a "cross-check", and claims it confirmed rows after a truncated retrieval.
- **lesson**: Put the sourcing and completeness rules in always-on tool_guidance.md: numeric CIK for edgar_search, no null queries, only opened documents as sources, and no "cross-check" against unopened pages. For list questions, retrieve the company's own table in a dedicated call, re-ask if the output is cut off, and confirm the row count. Do not seed the expected row values into the guidance, because a run then wrote that its answer "matches the task's reference list". Keep this out of a skill, because the procedure is short and the skill run took no fewer turns.
- **evidence**: Rows 1 and 2 are confounded with each other and with the lead. The execution contrast is base1 against all three edited runs: base1 had a failed ticker call, a null search, an unopened article in its sources and an unverified completeness claim. The edited runs had none of these and listed only the 10-K. The skill row shows dom1 (skill) matching inv1 and agg1 (no skill). The lead row shows dom1's unsupported "reference list" remark.
- **confidence**: low. Each candidate is one rollout, the rules were bundled with a task lead in every edited run, and all four runs produced the same 16 values, so the evidence concerns hygiene and sourcing, not accuracy.
