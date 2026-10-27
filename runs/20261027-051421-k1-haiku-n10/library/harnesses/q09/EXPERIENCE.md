# q09

- adopted: `agg1`
- components: 1 skill; 2,848 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: skills/guidance_vs_actual/SKILL.md (procedure: compare actual to the prior-quarter guidance midpoint, check the range, split GAAP from non-GAAP)
candidates: dom1, agg1
change: Added a skill covering where guidance and actuals live, actual minus midpoint as the default, a range check, and a warning that "above the high end" refers to non-GAAP. The version in dom1 also told the agent to headline the company-reported rounded figure. The version in agg1 told it to headline the one-decimal reported figure and not to use the 10-Q's whole-percent column.
observed: All four runs reached the same core number, 139.77 bps vs the 25.5% midpoint (26.8977% actual), including base1 and inv1 with no skill. The skill therefore did not change the headline arithmetic. It changed presentation. In dom1 (turn 3) the skill's "rounded company figure" instruction led the agent to give 150 bps off the 10-Q's whole-percent 27%, which is a rounding artifact. agg1 loaded the skill at turn 1 and headlined "about 140 bps (139.77 unrounded)", and it also gave range checks. base1 and inv1 had no skill and got the GAAP vs non-GAAP separation from their own reasoning. Both candidates ran once, and the skill was bundled with other edits.
verdict: confounded

component: skills/guidance_vs_actual/SKILL.md ("Task fact" block with Micron figures)
candidates: dom1
change: Embedded the Micron guidance (25.5% ± 1.5%) and actuals (1,832 / 6,811) in the skill text, labelled "re-check".
observed: The dom1 agent's answer matched the embedded figures. It still searched in turn 2 and tried a 10-Q parse, which returned 403. Its sources list the 10-Q and a Nasdaq reprint, and it does not say they were unopened. The base and inv1 agents found the same figures by search alone in 1 to 2 turns, so the embedded block added no accuracy. It also adds provenance risk. dom1 is the only run with the block.
verdict: no observed effect

component: systemprompt.md (trigger line to call load_skill guidance_vs_actual)
candidates: dom1, agg1
change: Added one line telling the agent to load the skill for beat-or-miss-vs-guidance questions. A trivial wording tweak ("calculations" to "calculation") was also made.
observed: Both dom1 and agg1 called load_skill as their first action (turn 1). Without the line there is no load, as in base1 and inv1. The line works as a trigger, but the skill's own effect is confounded (see the skill row).
verdict: helped

component: tool_guidance.md (bounded 403 fallback, disclosure of excerpt-only figures)
candidates: inv1, agg1
change: Went from empty to guidance on the two-document structure of guidance questions, one targeted web_search after a 403, no retry loops, and a requirement to describe excerpt-only figures as such. agg1 trimmed it. inv1 also asked for the difference on both unrounded and reported figures.
observed: inv1 submitted in 1 turn and ended its answer with "I did not open the full filings, so these figures are from excerpts." agg1 submitted in 2 turns and said the one-decimal figure was computed from dollars and not seen in the release. It made no parse_html_page call. base1 tried the 403-prone parse (turn 1), then cited the 10-Q, release and IR deck with no disclosure. dom1, without such guidance, hit a 403 at turn 2 and did not disclose. The numbers were identical across runs. The guidance affected call economy and disclosure, and each candidate has one rollout.
verdict: confounded

component: LongTermMEMORY.md (Micron guidance and actuals, labelled unconfirmed)
candidates: inv1
change: Stored the guidance and actual URLs and figures from excerpts, and noted that the "above the high end" remark is non-GAAP.
observed: inv1 went to a single web_search and then submitted in 1 turn. It reproduced the memory figures and its GAAP vs non-GAAP caveat. It is unclear whether the memory saved effort or merely repeated what the search returned. The entry is specific to one task and will not fire for other questions.
verdict: confounded

## Transferable lesson
- **cue**: A "how much did the company beat or miss its own guidance" question where the guidance is a midpoint ± range, the filing reports the actual both as a rounded percent and as dollar amounts, and sec.gov fetches return 403.
- **lesson**: In the skill for guidance-vs-actual questions (skills/guidance_vs_actual/SKILL.md), tell the agent to compute the headline from the dollar figures. For a one-decimal reported margin it should use the press release's figure, never the 10-Q's whole-percent column. It should show the unrounded variance against the midpoint beside the headline, and give the range position. Do not tell it to headline "the company-reported rounded figure" without that qualifier. In dom1 that wording produced a 150 bps headline from a rounded 27%, while agg1 and inv1, which fixed the rounding source, gave about 140 bps (139.77 unrounded).
- **evidence**: The skill row (dom1 vs agg1, confounded on whether the skill helped, but the dom1 turn-3 150 bps headline and the agg1 140/139.77 headline are a concrete contrast in rounding handling) and the tool_guidance row (disclosure of excerpt-only figures).
- **confidence**: low. All runs reached 139.77 bps, one rollout each, and the skill was bundled with the trigger line and tool guidance. The record supports only the narrow point about the rounding source.
