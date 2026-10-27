# q14

- adopted: `agg1`
- components: 0 skills; 3,905 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: tool_guidance.md (generic evidence rules: open the 10-Ks in parallel including the earliest year's, a snippet or third-party page is a lead, "read from" only if a retrieve call returned it, plus a multi-year ratio paragraph)
candidates: agg1
change: Added a tool guide. It says to open every needed 10-K in one turn, including the earliest year's. It bars third-party sites as sources for figures in the calculation. It gives an FCF-margin recipe: default capex is PP&E purchases, intangibles are a sensitivity, and the as-reported figure stays in the headline with the distorting line named. It also asks for year-by-year trend direction.
observed: Base1 opened the FY2024 and FY2023 10-Ks and never opened the FY2022 10-K. Under the same empty base harness, the inv1 rollout used stockanalysis and MarketBeat snippets for capex and submitted at turn 2 without any parse call. agg1 searched with filters at turn 1 and parsed the FY2024 and FY2022 10-Ks in parallel at turn 2. It retrieved CFO, capex, intangibles and revenue for each at turn 3, submitted at turn 4 for $0.208 with two 10-K sources, and the figures matched the comparative columns. Its answer showed pp changes per year and an ex-inventory sensitivity. The final numbers (224.16%, 11.26%, 12.75%) were the same as base1's and inv1's. The gain is sourcing quality and a fuller presentation, not a different value. Base1 already behaved well, and there is one rollout for agg1.
verdict: confounded

component: skills/fcf_margin_trend/SKILL.md and the systemprompt.md trigger line
candidates: dom1
change: Added a skill, loaded by a trigger line in systemprompt.md. It carries the FCF recipe (capex definition, open the oldest year's 10-K, report the as-reported series with the distortion, state direction). It also embeds Zillow's figures as leads to re-verify.
observed: dom1 spent turn 1 on load_skill. It then searched, parsed the FY2024 and FY2022 10-Ks at turn 3, retrieved at turn 4, and submitted at turn 5 for $0.210. This is about the same cost as agg1's 4 turns and $0.208, and about the same as base1's $0.200. Its answer reached the same values and added the ex-inventory sensitivity (~24.77%). That sensitivity also appeared in agg1, which had no skill. The embedded Zillow figures did not change retrieval, since it re-read them from the filings. The load turn bought no visible gain over the tool_guidance rule.
verdict: no observed effect

component: LongTermMEMORY.md, guardrails.md and the inv1 candidate (no edit proposed)
candidates: inv1
change: No change from base. The harness is the same as base1's.
observed: The inv1 rollout under the unchanged harness differed from base1 in sourcing. It ran an empty web_search and an edgar_search for only the FY2024 and FY2023 10-Ks. It then submitted at turn 2 from web-search snippets, stockanalysis and MarketBeat, with no parse or retrieve call. Its answer listed those third-party sources and had garbled trend wording ("fell from 11.26% in FY2023 to 12.75% in FY2024, a recovery"). Base1 under the same harness parsed both 10-Ks and retrieved the rows. The base harness therefore gives unstable sourcing behavior on this task. It is two rollouts of the same harness, one of which never opened a filing.
verdict: no observed effect

## Transferable lesson
- **cue**: A multi-year ratio or trend question (for example FCF margin, payout, margin by year) where the latest 10-K carries comparative columns. An unguided run may answer from aggregator snippets or open only the newest filings, and one year may be distorted by discontinued operations.
- **lesson**: In tool_guidance.md, add a generic multi-year rule. It should say to open the 10-Ks in parallel in one turn, including the earliest year asked, and retrieve all line items for every year in one call per document. A figure from an aggregator or snippet must not enter the calculation, and the answer may say "read from" only if a retrieve call returned the figure. Keep the as-reported series in the headline and name the line behind any outlier year. Give the direction year by year in percentage points. Do not add a skill, and do not embed company figures.
- **evidence**: The tool_guidance.md row (agg1) and the inv1 rollout row. Under the unchanged base harness, one run opened the 10-Ks (base1), and another (inv1) submitted at turn 2 from stockanalysis and MarketBeat snippets with no parse call. agg1 parsed the FY2024 and FY2022 10-Ks at turn 2 and retrieved at turn 3, then gave a year-by-year pp trend. The dom1 skill row shows the same content as a skill adding a load turn (5 turns, $0.210) with no gain over agg1 (4 turns, $0.208).
- **confidence**: low. All runs reached the same figures, there is one rollout per arm, and base1 already sourced from 10-Ks. The evidenced gain is more reliable sourcing and a fuller presentation, not a different value, and the inv1 contrast is a single rollout.
