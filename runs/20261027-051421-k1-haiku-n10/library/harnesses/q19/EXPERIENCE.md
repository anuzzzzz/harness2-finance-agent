# q19

- adopted: `agg1`
- components: 1 skill; 2,954 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: tool_guidance.md
candidates: inv1, agg1
change: Went from empty to a fallback for SEC 403s. inv1 says don't retry edgar_search, make one web_search fallback, parse the sec.gov URL, and confirm snippet figures in the filing text. agg1 says 403s are common, go straight to web_search, and say plainly when figures came from a search excerpt.
observed: In inv1, the agent tried parse_html_page first (turn 1), got a 403, then ran one web_search and submitted in 2 turns. It disclosed that the figures were not re-checked. In agg1, the agent still called edgar_search once (turn 2), which returned 403, before the web_search that worked. It submitted in 3 turns and disclosed the search-excerpt basis. base1 hit edgar_search 403 twice and submitted with no disclosure. dom1, with no guidance, hit 403 four times (turns 2-4) and then labelled the figures "Verified". All five runs reached the same 85,002 / 51.33%. The edits changed the amount of flailing and the honesty of the sourcing statement, not the number. The guidance cannot be separated from the other edits in agg1, and inv1 and agg1 each have only one rollout.
verdict: confounded

component: LongTermMEMORY.md
candidates: inv1
change: Stored the MSCI 10-K URL and lease schedule, labelled unconfirmed, plus the denominator choice.
observed: The inv1 agent went straight to parse_html_page on the stored URL (turn 1), which saved the discovery step. The 403 blocked it, and the final figures matched the memory entry and base1. The run cannot show whether the memory helped or merely repeated what the search excerpt returned. The entry is also task-specific.
verdict: confounded

component: skills/lease_maturity_schedule/SKILL.md
candidates: dom1, agg1
change: Added a skill covering the lease maturity procedure: latest 10-K, first N rows, undiscounted denominator, footing check, answer contract. dom1 also embedded the MSCI figures as a task fact. agg1 removed those figures and added a "say if from search excerpt" line.
observed: Both runs loaded the skill in turn 1 and produced footing checks (rows sum to 165,605; minus interest gives 146,004). Both labelled 58.22% as a secondary PV figure. Both left out raw cite tags. base1 and inv1 had no footing check, and base1 and inv1 left raw cite-tag artefacts in the answer. dom1 embedded the figures it later reported as "verified", so the skill content may have anchored it. agg1 had no embedded figures and reached the same numbers via search.
verdict: helped

component: systemprompt.md
candidates: dom1, agg1
change: Added one trigger line that tells the agent to call load_skill with lease_maturity_schedule for maturity questions.
observed: Both runs called load_skill as their first action. The skill only loaded because of this line.
verdict: helped

component: skills/lease_maturity_schedule/SKILL.md (embedded MSCI task fact)
candidates: dom1
change: Hard-coded the MSCI schedule and the expected 85,002 / 51.33% in the skill text.
observed: dom1 stated "Verified figures" and said it confirmed them from search text, although it had also been given them in the skill. That blurs which source the figures came from. Because the other runs got the same figures without the skill text, the embedded fact added no accuracy.
verdict: hurt

## Transferable lesson
- **cue**: Primary-source fetch tools (EDGAR search or page parsing) fail with HTTP 403 in this environment, and the agent can only reach filing text through web_search excerpts.
- **lesson**: In tool_guidance.md, state the order of the fallback (try one targeted web_search with company, form, year and table name, then the sec.gov URL if a parse is wanted) and require that the answer says whether the table came from an opened filing or from a search excerpt. Do not put task-specific figures in a skill or in LongTermMEMORY.md. In dom1 they were followed by an unwarranted "Verified" label.
- **evidence**: Rows for tool_guidance.md (confounded in outcome, but run contrast on wasted calls and sourcing disclosure: base1 and dom1 flailed on 403s, and dom1 mislabelled "Verified"; inv1 and agg1 disclosed the basis) and the embedded-fact row for dom1 (hurt on provenance only, since the numbers were the same in all runs).
- **confidence**: low. All runs gave identical numbers, the guidance effect rests on one rollout per candidate, and the guidance was always combined with other edits.
