# q21

- adopted: `agg1`
- components: 0 skills; 3,589 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, open the primary 10-K, re-ask when a retrieval is truncated, "not disclosed" only after both the note and Item 1A are queried, no null-query search, cite only opened documents, plain text)
candidates: inv1, agg1 (dom1 carried a shorter set of rules together with a skill)
change: Went from empty to a rule set. The 10-K is opened with parse_html_page. A truncated retrieval is re-asked more narrowly. Counterparties and percentages may be named only if a retrieved passage states them. Older-period documents are not cited. Searches never have a null query. The answer is plain text.
observed: base1 ran a null-query web_search. It cited an unopened 2020 424B4 and brought in its two-vendor disclosure. It also asserted "Citizens Bank appears to be the sponsor" after the retrieved note named no bank. inv1 and agg1 parsed the 10-K directly and listed only that filing. Neither cited the 424B4. inv1 stated plainly that no vendor name or share is disclosed. agg1 labelled the Citizens link as inferred from the settlement-line wording, and its retrieval at turn 5 supports the inference. agg1 took 7 turns and $0.47, against 3 turns and $0.12 for inv1, because its first broad retrieval returned empty and it re-asked. All three edited runs reached the same substantive finding: one unnamed vendor, no percentages. The rules were bundled with leads or skill content in every edited run, and each candidate is a single rollout.
verdict: confounded

component: tool_guidance.md (Shift4 task-fact leads: 10-K URL, Note 1 text, Item 1A single-processor fact)
candidates: inv1
change: Embedded the verified filing URL and the key disclosure facts from base1's retrieval, labelled "re-confirm".
observed: inv1 skipped discovery and parsed the 10-K in its first turn. It finished in 3 turns, the fewest of any run. agg1 had no leads, found the same URL with one edgar_search, and reached the same answer. The leads saved a turn or two and changed no figure. The content is specific to this task and will not carry over.
verdict: helped

component: tool_guidance.md (concentration-question checklist: Note 1 plus Item 1A, quote each dependency, say whether named and quantified, state exit terms, keep customer and merchant limits separate)
candidates: agg1 (the same content appeared as a skill in dom1)
change: Added one line to the always-on guidance giving the structure of a concentration answer. It also restated the sources-dictionary format, which base1 omitted.
observed: agg1's answer is organized into vendor, processor, sponsor bank and suppliers, with customer concentration reported separately, and ends with the sources dictionary. inv1 reached a similar structure without the checklist line, so the line's own effect is not isolated. The restated sources format fixed base1's omission of the dictionary, and inv1 and dom1 also included one.
verdict: confounded

component: skills/concentration_risk_disclosure/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill covering where concentration disclosures live, an answer contract, and as-of checks. It embedded the Shift4 facts. systemprompt.md gained a line telling the agent to load it.
observed: dom1 called load_skill first, then ran an edgar_search that turned out unnecessary, then parsed and retrieved. It took 5 turns, against 3 for inv1, which had no skill. Its answer included quoted passages with page numbers and a "not named" statement, and it said no termination notice period is stated. inv1's answer was comparable in substance but had fewer page references. The skill's benefit is not separable from dom1's own tool_guidance.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks about a company's dependency or concentration risk (vendor, processor, sponsor bank, supplier) as of a fiscal year-end. The base run finds the 10-K note but then adds a counterparty name it inferred and cites an older prospectus it never opened.
- **lesson**: In tool_guidance.md, add rules that a counterparty name or percentage may appear in the answer only if a retrieved passage from an opened document states it, otherwise it is labelled an inference. A truncated retrieval is re-asked more narrowly. "Not disclosed" is written only after both the financial-statement concentration note and the Item 1A risk factor have been queried. An older-period document is not cited or used. Keep this as always-on guidance without a skill.
- **evidence**: First row, where base1 asserted Citizens and cited an unopened 2020 424B4, while inv1 and agg1 parsed the 10-K, labelled the sponsor inference or left it out, and cited only the 10-K. Skill row, where dom1's skill run took 5 turns against 3 for inv1 with equivalent content.
- **confidence**: low. The rules were bundled with leads in inv1 and with a skill in dom1, each candidate is one rollout, and all edited runs reached the same disclosure finding, so the evidence concerns sourcing discipline rather than accuracy.
