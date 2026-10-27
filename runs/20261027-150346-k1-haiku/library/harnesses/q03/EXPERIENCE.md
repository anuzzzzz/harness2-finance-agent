# q03

- adopted: `agg1`
- components: 0 skills; 4,161 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, open both releases with parse_html_page then retrieve_information, cite only opened documents, plain text with no citation markup, never send an empty query, one headline with a labelled alternate)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. Snippets are leads only. The Q3 FY25 release (guidance) and the Q4 FY25 release (actual) must both be opened and retrieved from. Only opened documents may be listed as sources. The answer is plain text. inv1 and agg1 added a rule to give a single headline and label the alternate reference point (high end versus midpoint). dom1's version was a shorter bullet set.
observed: base1 made two searches, one with a null query. It took 10.8–10.9% and 11.6% from snippets and opened neither release. It listed the unopened Business Wire page and the just-style article, leaked raw <cite index> markup, and gave two competing headline answers (+70 vs high end, +75 vs midpoint). inv1, dom1 and agg1 each parsed both releases and retrieved the guided range (10.8%–10.9%) and the actual (11.6%), including the company's own "above the high-end of its plan by 0.7 percentage points" sentence. All three listed only the two opened releases and leaked no markup. inv1 and agg1 gave +70 bps as the headline with +75 as a labelled alternate. dom1 did the same through its skill's contract. The figures were identical in all four runs, so the effect was on verification, sourcing and presentation, not the number. dom1 and agg1 still made null-query or off-target searches despite the rule (dom1 made a null-query web_search, and agg1 made two unproductive edgar_search calls). The rules were bundled with other edits in every run, and each candidate is one rollout.
verdict: confounded

component: tool_guidance.md (embedded task-fact lead for TJX: Q4 release URL, snippet figures 10.8–10.9% and 11.6%, a warning about look-alike FY26 releases)
candidates: inv1
change: Listed the Q4 FY25 release URL, the snippet figures labelled "re-confirm", and a note that the Q3 FY25 release URL was unknown and had to be found via edgar_search.
observed: inv1 skipped discovery and ran a CIK-filtered edgar_search in turn 1 that returned both releases. It parsed both in turn 2. It retrieved the figures in turn 3 and submitted in turn 5. agg1 had no lead, and its CIK-filtered edgar_search in turn 1 returned only a 10-Q and the 10-K, so it needed two more empty edgar_searches and two web_searches before finding the Q3 release. inv1's lead did not change any figure. The comparison is one rollout each, and the filters and the lead differ together.
verdict: confounded

component: skills/guidance_vs_actual_margin_bps/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill for margin-versus-range comparison in bps. It covers where the guidance sits, the high-end versus midpoint choice, stated-rate rounding, and an answer contract. It carries the TJX facts as snippet-derived leads. systemprompt.md gained a sentence telling the agent to call load_skill for such questions.
observed: dom1 made a failed web_search, loaded the skill, then made a null-query web_search anyway. It parsed both releases and retrieved the figures. It took 5 turns and reached the same answer, with the same sources and the same headline-plus-alternate structure, as inv1 and agg1, which had no skill. A first retrieval from the Q4 release correctly reported that it contained no Q4 outlook, so the agent went to the Q3 release. The skill added no visible behavior beyond what the always-on rules gave. Its separate effect is not isolated, since the shorter tool_guidance was bundled with it.
verdict: no observed effect

component: systemprompt.md (trigger line only)
candidates: dom1
change: Added one sentence telling the agent to call load_skill with `guidance_vs_actual_margin_bps`.
observed: dom1 called load_skill in turn 1 after a failed search. No skill-equipped run lacks the trigger, so its separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A "beat or miss versus the prior quarter's guidance range, in bps" question. The guidance sits in the previous quarter's earnings release and the actual in the target quarter's release. The base run answers from snippets, opens neither, lists unopened pages as sources, leaks citation markup, and gives two competing headline numbers (against the high end and against the midpoint).
- **lesson**: In tool_guidance.md, require that the guided low and high ends and the actual each be retrieved from an opened primary release (parse_html_page, then retrieve_information). Also require that only opened documents be listed as sources, plain text with no citation markup, no empty-query searches, and one headline reference point (the one the company's own variance sentence uses) with the other labelled as an alternate. Keep the procedure in always-on tool_guidance and do not add a skill, since the skill-equipped run behaved the same as the skill-free runs.
- **evidence**: Row 1. base1 opened nothing, listed unopened sources, leaked <cite> markup and gave two headline answers. inv1, dom1 and agg1 opened both releases, retrieved the same figures, listed only the two opened releases and gave a +70 bps headline with +75 labelled. Row 3 shows dom1's skill run matching the skill-free runs on figures and sourcing, at the same turn count of 5. Reference-point and sourcing hygiene differ across the base and edited runs, and the figure was identical in all four.
- **confidence**: low. One rollout per candidate, and the rules were bundled with a lead or a skill in each edited run. The evidence concerns verification and presentation, not accuracy.
