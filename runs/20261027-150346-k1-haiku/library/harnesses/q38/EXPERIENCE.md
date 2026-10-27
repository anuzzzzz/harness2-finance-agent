# q38

- adopted: `agg1`
- components: 0 skills; 4,751 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, open both releases with parse_html_page then retrieve_information, two-document guidance-vs-actual procedure, cite only opened documents, plain text with no citation markup, no null-query searches, stated-versus-computed margin handling)
candidates: inv1, agg1
change: Went from empty to a rule set. Both the Q3 release (guidance) and the Q4 release (actual) must be opened. A figure the company states for the quarter is preferred to a subtraction from the 10-K. The unrounded computed margin is the headline, and the rounded stated margin is a labelled alternate. Only opened documents may be sources. Output is plain text.
observed: base1 never opened a Q4 release. It derived Q4 EBITDA by subtracting nine-month from FY figures, took Gross Bookings from a transcript, listed an unopened ARS PDF and an unopened transcript, and gave "about 29 bps". inv1 and agg1 each parsed both releases, retrieved the stated Q4 figures ($112.8M and $4,278.9M), and listed only the two opened releases. Neither leaked markup. inv1 ran an edgar_search for the Q4 release and finished in 4 turns. agg1 finished in 3 turns. The headline was about +28.6 bps in both, with +25 bps as the rounded alternate. base1 reported +29 bps, the same sign, and a figure within rounding of the others. So the effect shows in verification and sourcing, not in the verdict. The rules were bundled with a task-fact lead in both runs, and each candidate is one rollout.
verdict: confounded

component: tool_guidance.md (task-fact lead: Q3 and Q4 release URLs, guided 2.3-2.4% margin, derived fallback figures)
candidates: inv1, agg1
change: inv1 carried the Q3 URL, the guided range, a search route to the Q4 release (edgar_search filed Feb 2025) and the subtraction-derived figures as a fallback. agg1 trimmed this to the two verified URLs and dropped the subtraction fallback.
observed: inv1 found the Q4 release through edgar_search in turn 1 and used no fallback. agg1 skipped discovery and parsed both URLs in turn 1, with 3 turns total. The retrieved guidance and actuals matched the leads in both runs. The leads saved turns without changing any figure. The content is specific to this task and does not transfer.
verdict: no observed effect

component: skills/guidance_margin_vs_actual_bps/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill covering the guidance-versus-actual margin comparison in bps: the midpoint, the definition check, a stated-versus-computed rule and an answer contract. It carried the Lyft facts and flagged the Q4 dollar figures as unconfirmed. systemprompt.md gained a line telling the agent to load it.
observed: dom1 loaded the skill in turn 1. It then ran a web_search that returned 0 results, ran edgar_search, and ran a null-query web_search. It parsed the Q4 release only. It took the guidance range from the skill text and never opened the Q3 release in this run. Its sources list included the 10-K, which it never opened, which is the failure the guidance rules target. It took 5 turns. Its figures matched inv1 and agg1. The skill was the only edit in dom1, and the cost shows no gain over the skill-free runs. No run isolates the skill from the missing sourcing rules. The trigger line cannot be separated from the skill.
verdict: confounded

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A "beat or miss versus the prior quarter's guidance, in bps or %" question where the actual period's earnings release exists on EDGAR but web_search returns it poorly or not at all. The base run answers from snippets, a transcript and a 10-K subtraction.
- **lesson**: In tool_guidance.md, state that guidance and actual must each be read from an opened release (the guidance from the prior-quarter release, the actual from the period's own release). Tell the agent to find the period's release with edgar_search, using the CIK and a filing-date window about 5-6 weeks after period end, when web_search misses it. Say a company-stated quarterly figure is preferred to deriving the quarter by full-year-minus-nine-months subtraction. Add a rule to cite only opened documents. Do not carry a skill for this procedure.
- **evidence**: tool_guidance.md row. base1 never opened a Q4 release, derived the quarter by subtraction and listed unopened sources. inv1 and agg1 opened both releases and retrieved the stated quarterly figures. Both listed only the two opened documents. dom1, which had only a skill, opened just the Q4 release, took the guidance from skill text, and listed an unopened 10-K. The verdict and the bps figure were the same across all runs, so the evidence concerns sourcing and verification.
- **confidence**: low. Each candidate is a single rollout, and the guidance rules were bundled with a task-fact lead in inv1 and agg1. The contrast shows differences in sourcing behavior and no difference in the answer.
