# q25

- adopted: `agg1`
- components: 1 skill; 2,867 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (section-summary rules: map the Item 1A headings first, retrieve in small pieces, gate absence claims on a targeted empty retrieval, check the draft against retrieved text, plain text, cite only opened documents)
candidates: inv1, agg1
change: Went from empty to a rule set for summarizing a filing section. inv1's version was longer and also carried a task-fact block with the 10-K URL and the three Legal and Regulatory headings. agg1's version was shorter and added a rule that broad retrieve_information output can be truncated, so ask for one or two groups per call. Both stated that an absence claim needs a targeted empty retrieval.
observed: base1 turn 5 turned one broad retrieval into a flat claim in the final answer that ERISA, the ACA, FCPA and government contracts are absent from Item 1A. Neither inv1 nor agg1 repeated that claim. inv1 retrieved the heading list first, then the legal group, then a cross-group scan. agg1 retrieved a regulation table, then a narrower pass on client funds, cybersecurity, international and accounting. Both flagged that the cross-group items are summaries. agg1's closing caveat admitted a truncated sub-point, which was honest but left the ACH bank-failure detail incomplete. The same rules were present alongside a skill in agg1, and dom1 reached the same behavior with a skill and no tool_guidance, so the carrier is not isolated. One rollout each.
verdict: confounded

component: skills/risk_factor_summary/SKILL.md (plus the trigger line in systemprompt.md)
candidates: dom1, agg1
change: Added an on-demand skill for summarizing a risk-factor category from Item 1A. It covers checking the fiscal year-end, using Item 1A as the controlling section, and scanning all sub-headings for regulation-driven items. Each item is given as heading, named law, mechanism and stated consequence, grouped with the company's own sub-heading first. It also adds a completeness retrieval, a ban on absence claims without a targeted check, and an answer contract. agg1's version added a "map first" step and replaced the duplicated leads with one brief lead. systemprompt.md gained a line telling the agent to load the skill.
observed: Both runs loaded the skill in turn 1. dom1 then ran a retrieval and several follow-ups. It added foreign-law and AI follow-ups, named FTC, CPRA and BIPA, and put "not covered / not verified" in the answer, though it did not run an exact-term search for the absence. agg1 did not map headings first despite the skill saying to, and went straight to a regulation table. inv1, with no skill, reached a similar grouped structure and took 4 turns against 6 and 7 for the skill runs. So the skill's added value over the guidance alone cannot be shown, and its map-first step was not followed in agg1.
verdict: confounded

component: systemprompt.md (trigger line for the risk_factor_summary skill)
candidates: dom1, agg1
change: One sentence telling the agent to call load_skill with `risk_factor_summary` for 10-K risk-factor summary questions.
observed: Both runs called load_skill as their first action. No skill-equipped run lacks the trigger, so its separate effect is not shown.
verdict: no observed effect

component: tool_guidance.md (task-fact block: filing URL, fiscal year-end, and the three Legal and Regulatory headings)
candidates: inv1 (a shorter lead sits in the skill for dom1 and agg1)
change: Embedded Paylocity-specific facts in always-on text, labelled "re-confirm in the text".
observed: inv1 went straight to parse_html_page in turn 1, with no discovery search before parsing. Its follow-up edgar_search was redundant. base1 needed an edgar_search first. The three headings were retrieved from the text again. The answers were similar in content across all runs, so the lead saved at most a turn and the content did not change.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

component: base run behavior (reference, not an edit)
candidates: base1
change: No edit. The base run did one search, one parse and three retrievals.
observed: base1's regulatory coverage was reasonable, but its final answer asserted that ERISA, the ACA, FCPA and government contracts are not in Item 1A. That came from a single LLM retrieval over a 298k-character document, with a retrieval caveat that it saw no formatting. Its first retrieval was truncated and was not re-run. All edited candidates dropped or caveated that claim.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks to summarize or list a category of risk factors (regulatory, cybersecurity, competitive) from a long 10-K, and the only extraction tool is an LLM retrieval over one huge parsed document. Outputs are truncated, and the agent tends to turn one broad retrieval into a flat "the filing does not mention X" statement.
- **lesson**: In tool_guidance.md, state that retrieve_information output over a long filing is a summary that can be truncated. Ask for one or two headings or groups per call. Say a topic is absent only after a targeted retrieval for that exact term returns nothing, and then phrase it as "not found in the retrieved text". End the answer with a line on what was not verified. Put the Item 1A sub-heading-first, scan-other-groups procedure in a skill if one is used, but keep the absence and truncation rules in always-on tool_guidance, where they do not depend on a load_skill call.
- **evidence**: The tool_guidance and skill rows. base1 stated the ERISA/ACA/FCPA/government-contract absence from one broad retrieval and left a truncated first retrieval unrepeated. inv1 (guidance only), dom1 (skill only) and agg1 (both) all dropped or caveated that claim and added an unverified-items line, and none made the flat absence claim. dom1 conceded that it had not run an exact-term absence check and said so. Because guidance and skill were never varied independently, the carrier is not established.
- **confidence**: low. One rollout per candidate, a single-task contrast against the base, and the answer content was similar across all runs. The record shows a difference in how unverified claims were handled, not in accuracy.
