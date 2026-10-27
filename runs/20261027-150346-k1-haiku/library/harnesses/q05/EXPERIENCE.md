# q05

- adopted: `agg1`
- components: 1 skill; 3,030 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: inv1, agg1 (dom1 carried a shorter three-bullet version)
change: Went from empty to a rule set. A search snippet or press-release summary is a lead, not evidence. Match the filing year to the year the question names, and do not silently substitute an other-year event. Open the primary document with parse_html_page and confirm with retrieve_information. Cite only documents actually opened. inv1 also embedded the BBSI 2024 proxy and 8-K URLs as task leads. agg1 added a PDF note and a rule to say plainly when a fact comes from an unopened lead. dom1's version was shorter: lead-not-evidence, match the filing year, no PDFs.
observed: base1 found the 2024 DEF 14A and 8-K through edgar_search but never opened them. It answered "Mark S. Finn" from 2025 snippets, admitted he was not on the 2024 slate, and listed sources it had not read. All three edited runs parsed the 2024 DEF 14A at their first or second action and retrieved the nominee table. Each reached the same finding: eight incumbents, no new nominee. inv1 made its two retrievals on the proxy only and said the 8-K was unopened. agg1 and dom1 also opened the 8-K and cited only opened documents. The skill was present in dom1 and agg1, and inv1 embedded the URLs as leads in guidance. So the shift from snippets to the primary proxy cannot be assigned to the guidance alone. It plausibly came from the guidance, the leads, or both.
verdict: confounded

component: skills/board_nominee_lookup/SKILL.md
candidates: dom1, agg1
change: Added an on-demand skill that separates nominated (DEF 14A Proposal 1), elected (8-K Item 5.07) and appointed (8-K Item 5.02 or press release). The primary answer is the slate on that year's proxy. A later appointment or search narrative is reported separately, labelled, and cited only if opened. Includes a check that the nominee count matches the 8-K elected count. Carries BBSI URLs as leads. agg1's version also said the following year's proxy may describe a search run in the question year, and put the Finn item in as a labelled lead.
observed: Both runs loaded the skill first. Both parsed the proxy and the 8-K in the same turn, ran two retrievals and submitted in 4 turns. Both gave the eight-person slate, confirmed the election against the 8-K, and put Finn in a separate, labelled "later, unverified" line. dom1 said Finn came from "research notes". agg1 said it had not opened the 2025 documents. inv1 reached the same slate without the skill, in 4 turns, but did not open the 8-K. The skill's visible contribution is the 8-K count cross-check and the labelled separation. The leads in the skill also supplied the URLs, so the direct route is not isolated. The Finn item was never verified in any edited run. The base run's snippets suggested the 2025 proxy describes a 2024 search ending in Finn. No edited run opened the 2025 proxy to test whether that answers the question's "nominated in 2024" framing. Neither "no new nominee" nor "Finn" is established as the better headline by this record.
verdict: confounded

component: systemprompt.md
candidates: dom1, agg1
change: Added one sentence telling the agent to call load_skill with `board_nominee_lookup` when asked who was nominated, elected or appointed to a board in a given year.
observed: Both candidates called load_skill as their first action. No skill-equipped run lacks the trigger, so its separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks who was nominated, appointed or elected to a board (or similar governance event) in a named year. The base run finds that year's proxy and 8-K in search results but never opens them. It answers from a later year's snippets, a press release or a following-year proxy narrative, and lists unopened sources.
- **lesson**: In tool_guidance.md, state that a governance-event question is answered from the filing for the year the question names (DEF 14A for nominees, 8-K Item 5.07 for votes, Item 5.02 for appointments). Open that filing and retrieve the full slate with each person's status before answering. A later-year item that looks like an answer must be shown as a separate, labelled item, and cited only if its document was opened. Keep company-specific URLs in an on-demand skill, not in always-on text. If a later-year document appears to bear on the question (for example a proxy describing a prior-year search), open it before deciding whether it changes the headline.
- **evidence**: The tool_guidance.md row and the skill row. base1 never parsed the 2024 proxy and answered "Finn" from snippets, while admitting he was not on the slate. inv1, dom1 and agg1 all parsed the 2024 DEF 14A and retrieved the same eight-nominee list. dom1 and agg1 also opened the 8-K and reconciled the count. All three labelled the Finn item as separate and unopened. The contrast is in verification and framing. No run opened the 2025 proxy, so which framing is the better answer is not tested here.
- **confidence**: low. One rollout per candidate. Guidance, skill and leads moved together, so the carrier is not isolated. The shared finding of no new nominee never checked the 2025 document that base1's snippets pointed to.
