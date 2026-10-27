# q31

- adopted: `agg1`
- components: 0 skills; 3,627 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, cite only opened documents, no empty-query searches, failed fetch is not a source, plain text with no citation markup)
candidates: inv1, dom1 (shorter version), agg1
change: Went from empty to a rule set. Open the primary SEC document with parse_html_page and confirm figures with retrieve_information. Never send an empty query. On a failed fetch such as HTTP 403, switch to the SEC HTML exhibit. A URL that failed to load or was seen only in search is not a source. No citation markup.
observed: base1 hit a 403 on the Business Wire page and still listed that URL as a source. It also issued a null-query web_search. inv1, dom1 and agg1 went straight to the SEC 8-K EX-99.1 and listed only that exhibit. None issued a null-query search. All reached the same figure ($466.57M, rounded to $467M) as base1. The effect is on sourcing hygiene and efficiency, not the number. Each candidate is one rollout, and the rules were bundled with other edits.
verdict: confounded

component: tool_guidance.md (derived-metric and projection rules: derive gross profit when no line is printed, label the shop-level 22.3% margin as an alternate, state the compounding periods, 500 bps as 5.00 points, cross-check by a second route)
candidates: inv1, agg1 (dom1 carried the same content in its skill)
change: Added explicit procedure for a missing gross profit line and a look-alike segment measure, plus a two-route arithmetic cross-check.
observed: base1 already derived consolidated gross profit ($340,129K) and gave the correct arithmetic without these rules. inv1, dom1 and agg1 added a labelled cross-check (574,818 − 108,246 = 466,572). They also named the shop-margin alternate. agg1 even quantified it (about $341M). The additions show up as presentation, and the base answer was already right.
verdict: no observed effect

component: tool_guidance.md (embedded Dutch Bros task-fact lead: 8-K URL, figures, 26.55% vs 22.3%)
candidates: inv1
change: Embedded the exhibit URL and verified FY2024 figures, labelled "re-confirm".
observed: inv1 parsed the exhibit in turn 1 with no discovery search and finished in 2 turns. agg1 had no lead and needed an edgar_search first, so 4 turns. dom1 needed 5 turns, partly from the skill load. The figures were identical, so the lead saved turns without changing accuracy. The content is specific to this company and does not transfer.
verdict: no observed effect

component: skills/scenario_projection_margin/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill for growth-plus-margin-bps projections, covering the derived base margin, the margin-basis warning, compounding periods and an answer contract. It carries the Dutch Bros facts. systemprompt.md gained a line telling the agent to load it.
observed: dom1 loaded the skill first, then ran a discovery search, parsed the 8-K, made one retrieval and submitted, 5 turns in all. inv1 reached the same answer in 2 turns with no skill. The skill's procedure duplicates the tool_guidance projection bullets. The sourcing was clean in dom1, but it was also clean in the skill-free inv1 and agg1 runs. Its tool_guidance carried a cite-only-opened rule as well.
verdict: no observed effect

component: LongTermMEMORY.md, guardrails.md
candidates: none
change: Left empty in every candidate.
observed: Nothing to observe.
verdict: no observed effect

## Transferable lesson
- **cue**: A what-if or projection question (growth rate plus margin change) where the base-year metric is not a printed line, so the agent must derive it from revenue and cost of sales. A similarly named segment margin also exists. The base run does the arithmetic correctly but cites a page that returned HTTP 403 and issues a null-query search.
- **lesson**: In tool_guidance.md, put short general rules for sourcing and failed fetches. On a 403 or failed fetch, switch once to the SEC HTML exhibit. A URL that failed to load is never listed as a source. Never send an empty query. Add one line saying that a derived metric must be labelled as derived, with its formula, and that a look-alike segment measure may appear only as a labelled alternate. Keep the arithmetic procedure in tool_guidance and do not add a skill, because the skill-equipped run took 5 turns against 2 and 4 for the skill-free runs, with the same answer.
- **evidence**: Rows 1 and 4. base1 listed an unopened, 403-blocked URL and issued a null-query search. inv1, dom1 and agg1 listed only the opened SEC exhibit. The skill-free inv1 and agg1 runs match the skill-equipped dom1 run on both the number and the sourcing, so the skill adds turns and nothing visible.
- **confidence**: low. One rollout per candidate, the rules were bundled with other edits, and all four runs reached the same figure. The contrast is in sourcing hygiene and turn count, not in accuracy.
