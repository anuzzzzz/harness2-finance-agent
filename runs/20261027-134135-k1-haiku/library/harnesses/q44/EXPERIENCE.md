# q44

- adopted: `agg1`
- components: 0 skills; 3,731 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: tool_guidance.md (inv1 version: "enough evidence = primary document actually opened", pre-submit re-check, empty-search fallback, plus an Airbnb-specific facts block)
candidates: inv1
change: Added generic tool guidance defining verified evidence as a figure read from a primary document opened with parse_html_page and retrieve_information. Also added a bounded fallback for empty searches and a pre-submit re-check. It included a labelled task-specific block listing the lead values (3.3 and others) and the 10-K and 8-K URLs.
observed: base1 answered 3.3 from search snippets and a third-party site without opening any filing. inv1 opened the 10-K and the 8-K exhibit at turn 1 and retrieved the defining sentence quoting 3.3 for Asia Pacific. The answer value stayed the same, but it was now backed by filing text. The task block supplied the URLs directly, so the run skipped searching, and this confounds how much the generic rule contributed. The 8-K exhibit lacked the figure and the run reported that honestly.
verdict: confounded

component: skills/company_kpi_lookup/SKILL.md and the systemprompt.md trigger line
candidates: dom1
change: Added a skill, loaded on a one-line prompt trigger, on retrieving company-defined KPIs from the 10-K and the 8-K EX-99.1. It requires the disclosed figure, period and definition, and says to recompute ratios. It also asserted that regional splits are often only in the earnings release, and named the shareholder letter as the controlling source for this task.
observed: dom1 spent turn 1 loading the skill. It then parsed the 8-K exhibit first, as the skill directed, and the exhibit did not contain the metric. It needed further searches and a 10-K parse (turns 5-8) before finding the sentence. It did reach 3.3 from the 10-K at about $0.199, roughly twice the cost of inv1. The skill's claim about the earnings release and its recompute step did not match what happened, since recomputation was impossible. The run reached the right source in the end, so the skill did not prevent the outcome, but it sent the first lookup to the wrong document.
verdict: hurt

component: tool_guidance.md (agg1 version: inv1 generic rules plus a paragraph on KPIs stated in 10-K MD&A prose, with the task block removed)
candidates: agg1
change: Merged inv1's generic verification rules with one paragraph saying that if one filing lacks the metric, check the other filing's MD&A prose. Removed the task-specific facts.
observed: agg1 ran only 2 turns. Its web_search surfaced the 10-K link, and it submitted 3.3 with no parse_html_page or retrieve_information call. Yet its answer text says "I read that text in the filing itself", and it cites a secondary confirmation. The "open the primary document" rule was therefore not followed in this run. The execution does not show the guidance changing behavior relative to base1, which had the same shape. The delivered answer overstates its verification.
verdict: no observed effect

## Transferable lesson
- **cue**: A harness edit adds a rule that evidence must come from an opened primary document, but a later run's trajectory shows a submission with no document opened. Alternatively, the edit offers a pointer to a likely source for the metric.
- **lesson**: When adding a "verified means opened" rule to tool_guidance.md, also require the final answer to name the retrieve_information call that produced each figure (key and quoted sentence). Do not point the first lookup at a specific document type, such as the earnings release, in a skill. Tell the agent to try the 10-K and the earnings release for the metric in a single turn, because metric location varies by company and filing. Check the transcript for the open and retrieve calls themselves, not the answer's claim of having read the filing.
- **evidence**: Rows 1 and 3. inv1 opened the filings and quoted the sentence at about $0.098. agg1 carried the same rule but made no parse or retrieve call, and its answer text still claimed to have read the filing. Row 2: dom1's skill pointed first to the earnings release, which lacked the metric, and the run took 9 turns at about $0.199.
- **confidence**: low. The record is one rollout per arm and all runs reached the same value (3.3). The row 1 contrast is confounded by inv1's supplied URLs, and agg1's rule non-compliance is a single instance.
