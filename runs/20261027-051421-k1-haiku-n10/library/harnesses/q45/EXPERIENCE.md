# q45

- adopted: `agg1`
- components: 1 skill; 3,132 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: tool_guidance.md
candidates: inv1, agg1
change: Went from empty to a bounded fallback for SEC 403s. It says to pass a non-empty query, not to retry edgar_search after one failure, to make one or two targeted web_searches, to cite only URLs seen in tool output, and to say whether a figure came from an opened filing or a search excerpt. agg1 trimmed it and added that parse_html_page cannot read PDFs.
observed: base1 hit edgar_search 403 twice, issued a null-query web_search, and cited a Q3 10-Q URL that never appeared in its tool results, with no disclosure. inv1 made two targeted web_searches, submitted in 2 turns, and wrote "from a search excerpt, not an opened copy". agg1 made no failed fetch, ran several searches, and also disclosed the excerpt basis. dom1, which had no tool guidance, tried parse_html_page on the sec.gov URL (403) and then on the PDF (error) before searching. It still disclosed the excerpt basis, because the skill asked for that. All four runs reached the same $1,407M, so the effect is on wasted calls and sourcing honesty, not on the number. Each candidate has one rollout and other edits were bundled with it.
verdict: confounded

component: skills/non_gaap_adjustment_lookup/SKILL.md
candidates: dom1, agg1
change: Added a skill for pulling a named add-back from a non-GAAP reconciliation. It names the full-year column, notes the cash-flow SBC figure may differ, and requires a footing check and an answer contract. dom1 also embedded Airbnb URLs and an "unconfirmed $1,407M" note. agg1 removed both and added "say plainly if from a search excerpt".
observed: Both runs loaded the skill at turn 1 and produced the same footing arithmetic (2,648+683+40−818+65+1,407−7+23 = 4,041), which base1 and inv1 did not show. dom1 and agg1 gave the same figure and the same 2023 comparative. agg1 ran about five searches and cost $0.090, against $0.037 for dom1 and $0.024 for inv1. The footing check is visible only in the skill runs, but the skill was bundled with the trigger line, and in agg1 with the tool guidance too. The dom1 URL and figure block added nothing visible: dom1 still tried the 403 URL and the PDF. Since the figure matched in every run, it is not clear whether the "unconfirmed" note affected behavior.
verdict: confounded

component: systemprompt.md (trigger line to load non_gaap_adjustment_lookup)
candidates: dom1, agg1
change: Added one line telling the agent to load the skill for add-back or adjustment questions in a non-GAAP reconciliation. dom1 also made a trivial "calculations" to "calculation" wording change, which agg1 dropped.
observed: Both dom1 and agg1 called load_skill as their first action. base1 and inv1 never loaded a skill. The trigger works mechanically. The skill's own contribution is confounded, as in the skill row.
verdict: helped

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: No candidate changed them. Both stayed empty.
observed: Not applicable. The editors declined to store the 1,407 figure because no run read it from an opened filing.
verdict: no observed effect

## Transferable lesson
- **cue**: A "what was the adjustment/add-back for X in year Y" question on a non-GAAP reconciliation, where sec.gov fetches return 403, PDFs cannot be parsed, and the figure is reachable only through web_search excerpts.
- **lesson**: In tool_guidance.md, state the fallback order: one targeted web_search naming company, form, year and reconciliation table, with a non-empty query. Do not call edgar_search again after a 403, do not call parse_html_page on PDFs, and cite only URLs that appeared in tool output. In the skill's answer contract, require a footing check (net income plus the listed adjustments equals the reported total) and a plain statement of whether the figure came from an opened filing or a search excerpt. Do not embed the task's figure or URLs in a skill.
- **evidence**: tool_guidance.md row (base1 flailed on two 403s, used a null query and cited an unseen URL; inv1 and agg1 avoided those failures and disclosed the excerpt basis) and the skill row (dom1 and agg1 produced footing checks that base1 and inv1 lacked). Both rows are confounded, and the figure was identical across all four runs.
- **confidence**: low. One rollout per candidate, bundled edits, and no difference in the final number. The record shows only differences in wasted calls, disclosure and footing evidence.
