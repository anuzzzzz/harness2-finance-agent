# q09

- adopted: `agg1`
- components: 0 skills; 4,224 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: tool_guidance.md (generic verification rules: "enough evidence = primary document actually opened", parallel opening of documents, pre-submit re-check)
candidates: inv1, agg1
change: Both added a tool guide that defines verified evidence as a figure read from a primary document opened with parse_html_page and retrieve_information. Both tell the agent to open the needed documents in parallel and to re-check each figure before submitting.
observed: base1 ran 2 web searches and submitted in one turn from snippets, with no parse or retrieve call, and computed the actual from 10-Q dollars. inv1 opened both press releases in parallel at turn 1 and retrieved verbatim guidance and actual rows at turn 2. agg1 had a rough start (an empty web_search and an edgar_search), then parsed both releases in parallel at turn 2 and retrieved the rows at turn 3. In both runs the answer is now backed by document text. The values did not change materially. Base also reached about 139.77 bps. Each arm is a single rollout, so the contribution of this rule specifically is not isolated.
verdict: helped

component: tool_guidance.md (guidance-versus-actual procedure: prior-quarter release for guidance, same GAAP/non-GAAP basis, midpoint benchmark, range position, show both unrounded and reported-rounded bps)
candidates: inv1 (shorter version without the dual-precision rule), agg1 (full version)
change: Gives a generic recipe for beat/miss questions. The guidance comes from the prior quarter's release and the actual from the current one. The basis must match. The difference is measured against the midpoint, and the position within the range is stated. agg1 also requires both the unrounded and the reported-rounded bps figures.
observed: inv1 reported 140 bps from the rounded 26.9% only, and did not compute the unrounded figure. agg1 reported 139.77 bps (unrounded) and 140 bps (rounded), the range position (about 10.23 bps below the high end), and the non-GAAP cross-check. The agg1 answer is more complete, and it was the delivered one. However, base1 also computed 139.77 and noted the range, without this guidance, so the added value is only the explicit dual-precision display. One rollout per arm.
verdict: confounded

component: skills/guidance_vs_actual/SKILL.md and the systemprompt.md trigger line
candidates: dom1
change: Added a skill, loaded on a one-line prompt trigger, that carries the beat/miss recipe plus Micron-specific URLs and the earlier read figures labelled as leads to verify.
observed: dom1 spent turn 1 on load_skill, then parsed both releases in parallel at turn 2 and retrieved the rows at turn 3. It reached the same 139.77 / 140 bps answer with range position, in 5 turns at about $0.005. That is similar to inv1 (3 turns, about $0.005), which used tool guidance only. The skill added a turn and no visible gain. It also embedded task-specific URLs and figures, which are not reusable. It did not cause any wrong behavior.
verdict: no observed effect

component: tool_guidance.md (task-specific fact block with the Micron URLs and the guidance lead)
candidates: inv1
change: Listed the Q2/Q3 release and 10-Q URLs and flagged them as not yet read from the documents.
observed: inv1 went straight to parsing the two releases at turn 1 with no search. agg1, which dropped the block, spent turn 1 on an empty web_search and an edgar_search before finding the same URLs. That cost one to two turns, and the cost was still small ($0.016 against $0.005). The block therefore saved effort but is confounded with the rest of inv1's edit and is not reusable.
verdict: confounded

## Transferable lesson
- **cue**: A question asks whether a company beat or missed its own guidance and by how much (basis points, dollars or percent), and the base run answers from search snippets with no filing opened.
- **lesson**: In tool_guidance.md, add a generic guidance-versus-actual paragraph. It should say to open the prior-quarter release (Business Outlook) and the current-quarter release in parallel with parse_html_page, match GAAP to GAAP, benchmark against the guidance midpoint, and report both the unrounded difference (margin $ / revenue $) and the difference using the release's rounded percentage. It should also say where the actual fell in the guided range. Keep company-specific URLs and figures out of the library version. Do not add a skill for this, because a skill added a load turn with no observed gain.
- **evidence**: The "guidance-versus-actual procedure" row and the "generic verification rules" row. In inv1 and agg1 both releases were opened in parallel and the rows were quoted. inv1 gave only the rounded 140 bps, while agg1's dual-precision rule produced 139.77 and 140 with range position. The skill row shows dom1 reaching the same result with an extra load turn.
- **confidence**: low. There is one rollout per arm, and base1 already reached 139.77 bps from snippets, so the evidenced gain is mainly document-backed sourcing and a fuller presentation, not a different value.
