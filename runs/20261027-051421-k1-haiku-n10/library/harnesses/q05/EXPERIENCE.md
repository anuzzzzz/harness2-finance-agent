# q05

- adopted: `agg1`
- components: 0 skills; 1,525 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: skills/board_nominee_lookup/SKILL.md
candidates: inv1, dom1
change: Added a skill for "who was nominated/appointed/elected to the board in year Y". It separates nominee, appointee and selected-but-seated-later, and orders sources with year-Y filings first and the next year's proxy as retrospective. inv1 also embedded unverified BBSI facts and told the agent to open the PRE 14A and the 8-K. dom1 embedded similar BBSI facts and a three-category classification.
observed: Both runs loaded it at turn 1 and then opened the June 2024 8-K, which base1 never did. inv1 also opened the 2024 PRE 14A. Both reached the same facts as base1 (an eight-person incumbent slate, Finn selected in 2024 and seated April 7, 2025). The framing changed. inv1 and dom1 led with "no new person nominated in 2024" and treated Finn as a caveat or secondary point. base1 and agg1 led with Finn. Cause and effect are not separable: each candidate has one rollout, the skill was bundled with the trigger line (and, in inv1, with tool guidance), and the embedded task facts may have steered the framing. The skill did produce better evidence-gathering (opened year-Y filings, slate confirmed by voting results) without changing the underlying facts.
verdict: confounded

component: systemprompt.md (trigger line to load board_nominee_lookup)
candidates: inv1, dom1
change: Added one line telling the agent to load the skill for questions about who was nominated, appointed or elected to a board in a given year.
observed: Both inv1 and dom1 called load_skill as their first action (turn 1). base1 and agg1 never loaded a skill. The trigger works mechanically. The value of what it loads is confounded (see the skill row).
verdict: helped

component: tool_guidance.md
candidates: inv1
change: Went from empty to guidance on searching by company, form and calendar year, passing a non-empty query, not retrying sec.gov 403s, and opening IR-site URLs with parse_html_page. It said to treat snippets as leads and cite only URLs seen in tool output.
observed: inv1 made no edgar_search call and no null-query search. It ran two targeted searches, then parse_html_page on IR-site URLs, which succeeded, and it labelled each source "opened" or "excerpt". It cost $0.033, with 4 turns. dom1 had no guidance and made a failed null-query web_search and an edgar_search 403 (turn 2), then a second null-query search (turn 3). base1 and agg1, also without guidance, hit the same edgar_search 403 and null-query search. This is the clearest contrast in the record, but it rests on one guided rollout against three unguided ones, and it was bundled with the skill.
verdict: helped

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: No candidate changed them. Both stayed empty.
observed: Not applicable.
verdict: no observed effect

## Transferable lesson
- **cue**: A "who was nominated / appointed / elected in year Y" question where the later-year proxy describes a year-Y search but the formal seating or vote falls in year Y+1. The agent can reach company IR-site filings, while sec.gov search returns 403 and null-query searches return nothing.
- **lesson**: In tool_guidance.md, state the fallback order: a non-empty web_search naming company, form type and year, then parse_html_page on the IR-site filing URLs that the results return, with no edgar_search after a 403 and no null query. Require the answer to label each source "opened" or "excerpt". Open the year-Y voting-results 8-K or proxy before answering, rather than relying only on a later retrospective proxy paragraph. Do not embed the task's names in a skill, and use the answer contract to require both readings (year-Y slate and selected-but-seated-later) with dates, so that the choice of reading is explicit.
- **evidence**: The tool_guidance.md row (inv1 avoided the 403 and null-query detours that base1, dom1 and agg1 all hit, and opened the PRE 14A and 8-K from IR-site URLs). The skill row (inv1 and dom1 opened the year-Y 8-K that base1 skipped, but the resulting framing differed from base1 and agg1 with the facts unchanged, so which reading the question wants is not settled by the record).
- **confidence**: low. One rollout per candidate, bundled edits, and identical underlying facts in all four runs. The record supports only the fallback-order and labelling advice, not a claim about which reading of "nominated" gives the better answer.
