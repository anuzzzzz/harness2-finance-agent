# q04

- adopted: `agg1`
- components: 1 skill; 3,206 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: skills/guidance_range_width/SKILL.md
candidates: inv1, dom1, agg1
change: Added a skill for "how wide was the guidance range" questions across quarters. It maps each guided quarter to the prior quarter's release and defines range as a percent of midpoint as (high − low) / midpoint, the full width. It also requires the question's prescribed line template and decimals, with unrounded working beneath. dom1 additionally embedded the AMD figures as "hypotheses to re-check". inv1 and agg1 had no embedded figures. agg1 added a working block (source basis, midpoint footing) and a "never use the guided quarter's own release" rule.
observed: All three loaded the skill at turn 1 and then ran 3–4 targeted searches. The same guidance figures (5.7, 6.7, 7.5, 7.1, each ±$0.3B) came out in every run, including base1, which had no skill. The visible change is format. base1 headlined 10.53 / 8.96 / 8.00 / 8.45% against the question's "[X.X]%" template and appended a half-width alternative. inv1, dom1 and agg1 all gave 10.5 / 9.0 / 8.0 / 8.5% in the template, with full width stated. dom1's embedded figures did not change the searches it ran, and it still called its figures confirmed from excerpts. The skill was bundled with the system-prompt carve-out in every candidate, so the skill's own effect cannot be separated from the format override. Each candidate has one rollout.
verdict: confounded

component: systemprompt.md (trigger line to load guidance_range_width)
candidates: inv1, dom1, agg1
change: Added one line telling the agent to load the skill for questions about guidance or outlook range width.
observed: All three candidates called load_skill as their first action (turn 1). base1 never loaded a skill. The trigger works mechanically. The skill's value is confounded (see the skill row).
verdict: helped

component: systemprompt.md (carve-out: a prescribed output format controls precision)
candidates: inv1, dom1, agg1
change: Changed the blanket "at least two decimal places" sentence so a question's prescribed format, including decimals, overrides it. Unrounded values go only in the supporting working.
observed: This is the clearest behavior contrast in the record. base1, under the unmodified blanket rule, gave two-decimal percentages against "[X.X]%". All three edited runs gave one decimal and kept the unrounded figures in the working. All three candidates made the edit together with the skill, which also states the format rule, so the two cannot be separated. The contrast against base1 is consistent across 3 of 3 candidate runs versus 1 base run.
verdict: helped

component: tool_guidance.md
candidates: inv1, agg1
change: Went from empty to guidance: pass a non-empty query, do not retry 403s, run one targeted web_search per period, treat a title-only listing as not evidence, cite only URLs seen in tool output, and disclose whether figures came from excerpts or opened documents.
observed: base1 submitted after four searches whose results are logged as titles and URLs only, and cited a q42024991.htm URL that did not appear in its logged search results. inv1 and agg1 ran per-period searches and said the figures came from excerpts. inv1 again cited a CNBC URL that is not in its logged search results. agg1's answer contained raw cite tags despite the "no raw citation tags" line. dom1 had no tool guidance and also disclosed the excerpt basis, because its skill asked for that. Neither edited run did anything visibly different in call count. The URL-discipline effect is not demonstrated, and one rollout each stands behind the comparison.
verdict: no observed effect

component: skills/guidance_range_width/SKILL.md (embedded AMD task figures)
candidates: dom1
change: Hard-coded the four AMD midpoints and ±$300M in the skill text, labelled as unconfirmed excerpt-derived hypotheses.
observed: dom1 searched anyway and reached the same figures as inv1 and agg1, which had no embedded figures. Its answer did not call them unverified. It said they were "confirmed" from excerpts, which blurs provenance, but the numbers were the same as in the runs without the embedded text.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: No candidate changed them. Both stayed empty.
observed: Not applicable.
verdict: no observed effect

## Transferable lesson
- **cue**: A multi-period question that supplies its own output template with a stated precision (for example "[X.X]%"), while the base system prompt carries a blanket "at least two decimal places" rule.
- **lesson**: In systemprompt.md, change the blanket two-decimal sentence so that a question-prescribed format, including decimals, overrides it. State that unrounded values belong only in the working beneath the formatted lines. Repeat the rule in the relevant SKILL.md answer contract. Check it by comparing the final lines against the template's decimal places.
- **evidence**: The systemprompt carve-out row. base1 (blanket rule) gave 10.53% against "[X.X]%". inv1, dom1 and agg1 (carve-out plus skill) all gave 10.5% with unrounded working shown. The guidance figures were identical in every run, so only the presentation differed.
- **confidence**: low. One base rollout and one rollout per candidate. The carve-out was always bundled with the skill, so the system-prompt edit cannot be separated from the skill's format step. The record shows the format contrast, not which component caused it.
