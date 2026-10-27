# q09

- adopted: `agg1`
- components: 1 skill; 3,094 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: inv1, agg1
change: Went from empty to a rule set. A search snippet is a lead, not evidence. Open the primary filing with parse_html_page and confirm each figure, period and GAAP/non-GAAP basis with retrieve_information. parse_html_page cannot read PDFs. Use the company-stated rounded figure for the headline and an unrounded recomputation only as a labelled cross-check. Write plain text. Submit once verified. dom1 did not carry it.
observed: base1 made three web_search calls and never opened a filing. It submitted 139.77 bps from a 10-Q figure rounded to 27% and from a news-site copy of the guidance. inv1 and agg1 parsed both SEC releases and retrieved 25.5% ± 1.5% and 26.9% before submitting, and headlined 140 bps. dom1 reached the same behaviour with no tool_guidance, because its skill said to retrieve from the filing text. So the retrieval behaviour appears under either carrier, and the two cannot be separated.
verdict: confounded

component: skills/guidance_vs_actual/SKILL.md
candidates: inv1, dom1, agg1
change: Added an on-demand skill with the procedure. The actual comes from the target-quarter release. The guidance comes from the prior quarter's Outlook table. Keep GAAP and non-GAAP separate. The headline is the actual minus the guidance midpoint, with 1 percentage point = 100 bps. State the position against the range ends. It includes the two SEC URLs as unverified leads. inv1 adds "use the company-stated rounded figure for the headline". dom1 adds a caution about which basis an "above the high end" claim refers to. agg1 merges both.
observed: All three loaded the skill in turn 1 and went to the Q2 and Q3 EX-99.1 releases. The loaded skill prompted the correct document pair in 4 to 5 turns, against base1's search-only run. All three skill runs retrieved the same figures, 25.5% guidance and 26.9% actual, and reported +140 bps against the midpoint. The skill and the tool_guidance rule were not varied independently, except that dom1 had the skill alone and still verified. The skill probably drove the document pairing. Its effect on the number is unclear, because base1 used the same midpoint.
verdict: confounded

component: systemprompt.md
candidates: inv1, dom1, agg1
change: Added one trigger line telling the agent to call load_skill with `guidance_vs_actual` when a question asks whether a company beat or missed its guidance.
observed: Every candidate called load_skill as its first action. No run without the trigger exists on a skill-equipped harness, so its separate effect is not shown.
verdict: no observed effect

component: skills/guidance_vs_actual/SKILL.md (headline rounding and cross-check rule)
candidates: inv1, dom1, agg1
change: The headline uses the company-stated percentages (26.9% − 25.5% = 140 bps). The unrounded value is shown only as a cross-check.
observed: base1 headlined the unrounded 139.77 bps. inv1 gave 140 bps and did no cross-check. agg1 gave 140 bps and cross-checked at about 139.79. dom1 gave 140 bps and cross-checked at 139.33, which is miscalculated, since 1832/6811 is about 26.898%. The rule changed which number is the headline, and one candidate's cross-check was arithmetically wrong. The record does not show which headline is better.
verdict: confounded

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks how a company's result compared with its own prior guidance, in bps, % or $. The base agent answers from web-search snippets and never opens the two earnings releases. The guidance sits in the prior quarter's release, and GAAP and non-GAAP figures sit side by side.
- **lesson**: Add a skill, triggered by one line in systemprompt.md, that fixes the document pair (actual from the target-quarter EX-99.1, guidance from the prior quarter's Outlook table) and requires each figure to be retrieved from those parsed releases with its GAAP/non-GAAP basis. Pair it with a tool_guidance.md rule that snippets are leads only. Also decide explicitly whether the headline uses the company-stated rounded percentage or the unrounded recomputation, and show the other as a labelled cross-check. Compute the cross-check carefully.
- **evidence**: Edit rows for tool_guidance.md and for the skill. base1 used snippets and a news-site copy. inv1, dom1 and agg1 all parsed the Q2 and Q3 SEC releases and retrieved 25.5% ± 1.5% and 26.9%. dom1 shows the skill alone sufficed to trigger retrieval. The rounded-versus-unrounded headline row shows base1 gave 139.77 while the others gave 140, and dom1's cross-check was wrong.
- **confidence**: low. Each candidate is a single rollout, and the guidance midpoint was the same in all runs including base1. The record shows a difference in verification behaviour, not a demonstrated difference in answer quality. The better headline convention (140 or 139.77) is not established.
