# q05

- adopted: `agg1`
- components: 0 skills; 3,979 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: tool_guidance.md (inv1 version: generic rules plus a board/nominee paragraph, open the in-year DEF 14A first, match verb and year, later filings only as leads, plus a BBSI-specific URL block)
candidates: inv1
change: Added guidance to open the proxy filed in the question's year in the same turn as any 8-K and to retrieve the full nominee list with each person's new/incumbent status. It requires the verb and year to match, so a later appointment does not answer a "nominated in 2024" question. It also embedded the BBSI DEF 14A URLs and said the earlier run had missed the nominee.
observed: base1 found the 2024 DEF 14A through edgar_search and never opened it. It submitted Mark S. Finn, an April 2025 appointee, while admitting he was not on the 2024 ballot, and it cited a post-as-of-date proxy. inv1 parsed the DEF 14A at turn 1 and ran two retrieves at turns 2-3, which returned the eight incumbent nominees with no new nominee. It submitted at turn 4 for $0.016 with a single primary source. The URL block let it skip the search, so how much the generic rule contributed is confounded. It also made one retrieve with the full-document character range, which was redundant.
verdict: confounded

component: tool_guidance.md (agg1 version: inv1's generic rules, the BBSI URL block removed, Item 5.07 added, plain-text output)
candidates: agg1
change: Kept the generic rule to open the in-year proxy and match the action and year, and to give the full slate with new/incumbent status, saying plainly if none is new. It removed the company-specific facts and added 5.07 8-Ks.
observed: agg1 ran edgar_search with the ticker filter at turn 1 and got the DEF 14A. A second, unfiltered search returned noise from unrelated issuers. It parsed the proxy at turn 2 and retrieved the slate at turn 3, with quotes ("Election of eight directors..." and "All of our director nominees are currently serving on the Board."). It submitted at turn 4 for $0.009 with no hints. It reached the same slate as inv1 and dom1 and did not use the 2025 appointee. It never opened the 8-K that reports the vote, though the guidance mentions it. One rollout.
verdict: helped

component: skills/board_nominee_lookup/SKILL.md and the systemprompt.md trigger line
candidates: dom1
change: Added a skill, loaded on a prompt trigger, covering the proxy, 5.02 and 5.07 sources, the new-versus-incumbent test via "director since", and a rule against using later appointees. It embedded BBSI's accession number and slate as items to verify.
observed: dom1 spent turn 1 on load_skill. It then ran an edgar_search, parsed the DEF 14A at turn 3 and retrieved the slate with ages and director-since years at turn 4. It ran an 8-K search, which returned 0 results, and submitted at turn 6 for $0.009. The answer is the same as inv1's and agg1's, and it reported the Finn appointment as outside 2024. It never opened the 8-K that reports the vote and admitted this in a caveat. The load turn and the empty search added turns with no visible gain over tool guidance.
verdict: no observed effect

component: systemprompt.md (trigger line for load_skill)
candidates: dom1
change: Added one sentence telling the agent to load board_nominee_lookup for board nominee, appointment or election questions.
observed: dom1 followed it at turn 1. The only effect visible is the extra load turn, since inv1 and agg1 reached the same slate without it.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks who was nominated, appointed or elected to a board or office "in <year>". The base run finds the in-year proxy in its search results but never opens it, and answers with a person from a later-dated press release or proxy while admitting the mismatch.
- **lesson**: In tool_guidance.md, add a generic rule for year-scoped officer and board questions. Open the proxy (DEF 14A) filed in the named year with parse_html_page, retrieve the full nominee list with new or incumbent status, and match the verb and year to the question. Later-dated filings are leads only. If no nominee is new, say so and list the slate. Keep company URLs and names out of the rule, and do not build a skill, since the skill added a load turn with no gain.
- **evidence**: Rows 1-3. base1 submitted a 2025 appointee without opening the 2024 proxy. inv1 and agg1 each opened it and retrieved the eight-person slate in 4 turns, and dom1 did the same in 6 turns including the skill load. agg1 reached this with no company-specific content.
- **confidence**: low. One rollout per arm, all three edited runs gave the same slate, and the inv1 URL block confounds its row. The evidenced gain is sourcing from the correct-year primary document and a plain statement that no new nominee existed, not a different set of names.
