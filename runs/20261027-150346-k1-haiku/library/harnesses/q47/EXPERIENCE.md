# q47

- adopted: `agg1`
- components: 1 skill; 2,591 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: inv1, agg1 (dom1 added a shorter three-bullet version)
change: Went from empty to a rule set. A snippet is a lead, not evidence. Both the guidance and the actual must be read from opened primary documents. Cite only opened documents. Write plain text with no citation markup. inv1 and agg1 also added a rule to cross-check draft-marked documents in a second source and a note that PDFs cannot be parsed. inv1 also embedded task facts (the verified guidance range and the URLs) in this file. agg1 added a rule not to lean on figures from unopened filings.
observed: base1 opened only the Q1 letter. It took the $43.5B actual from a search snippet, listed the unopened Q3 letter and a Yahoo transcript as sources, and leaked raw <cite index> markup. inv1, dom1 and agg1 all parsed the Q3 letter and retrieved the $43.5B actual from it, and none leaked markup. agg1's sources include the Q3 10-Q, which it never parsed, and it leaned on a snippet-based claim about it. This is the failure the rule was written to prevent. dom1 also mentioned an unopened 10-Q snippet figure as a caveat, and did not list it as a source. The answer was MISS, -7.45% in every run, so the effect was on verification and presentation, not the number. The skill-carrying runs show the same behavior, so the guidance cannot be separated from the skill.
verdict: confounded

component: skills/guidance_vs_actual_midpoint/SKILL.md (plus the trigger line in systemprompt.md)
candidates: dom1, agg1
change: Added an on-demand skill for beat/miss against guidance midpoint. It takes guidance from the release that first gave it. It reads the actual from the target period's own release, not a snippet. It computes (actual - midpoint) / midpoint, says where the actual sits against the range, and gives an answer contract with a caveat for drafts. It carries the Shift4 figures and URLs, including the $43.5B actual. systemprompt.md gained a line telling the agent to load it.
observed: Both runs loaded the skill in turn 1 after a failed web_search. Both then made a null-query web_search, parsed the Q1 and Q3 letters and ran one retrieval per letter. The turn count was 4, the same as inv1, which had no skill. The skill supplied URLs, so no discovery was needed, and inv1's task-fact lead in tool_guidance did the same. Neither the skill nor the trigger changed the number. Their separate effect cannot be shown, since the skill-free run (inv1) behaved the same way and carried its own lead. Both skill runs made a wasted empty-query search.
verdict: confounded

component: systemprompt.md
candidates: dom1, agg1
change: Added one sentence telling the agent to call load_skill with `guidance_vs_actual_midpoint` for beat/miss-versus-guidance questions.
observed: Both called load_skill first (after one failed search). No skill-equipped run lacks the trigger, so its separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

component: base run behavior (reference, not an edit)
candidates: base1
change: No edit. The base run parsed only the Q1 letter.
observed: base1 found the Q3 actual in a search snippet in turn 1. It never opened the Q3 letter. Its final answer carried unopened sources and caveats saying the Q1 text looked like a draft.
verdict: no observed effect

## Note on convergence
All four runs, with or without edits, gave the same verdict and figure: a MISS of 7.45%, from $46.0-48.0B guidance (midpoint $47.0B) against $43.5B. The record therefore shows differences in verification, sourcing and presentation only.

## Transferable lesson
- **cue**: A "beat or miss versus guidance" question that needs two documents, the release that issued the guidance and the release that reports the actual. The base run opens the guidance document but takes the actual from a search snippet, lists the unopened actual-period document as a source, and leaks citation markup.
- **lesson**: In tool_guidance.md, state that for a guidance-vs-actual question every figure in the calculation, the guided range and the actual, must be read from an opened primary document (parse_html_page, then retrieve_information), and that only opened documents may be listed as sources. Add a rule to cross-check the guidance in a second opened document if the parsed text carries draft markers or internal inconsistencies, and to write plain text with no citation markup. Keep the beat/miss arithmetic and the answer contract in an on-demand skill. Do not list a 10-Q or transcript in sources, or cite a figure from one, unless it was retrieved.
- **evidence**: tool_guidance.md row. base1 took $43.5B from a snippet, listed unopened sources, and leaked <cite> markup. inv1, dom1 and agg1 all parsed both letters and retrieved both figures, and none leaked markup. agg1 still listed an unopened 10-Q and relied on a snippet, so the rule needed a "no unopened sources" clause. The number was identical in all runs.
- **confidence**: low. One rollout per candidate, and the guidance, the skill and the task-fact leads were bundled in every edited run. The evidence concerns verification behavior, not accuracy.
