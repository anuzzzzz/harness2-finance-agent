# q44

- adopted: `agg1`
- components: 1 skill; 3,179 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: inv1, agg1 (dom1 did not change it)
change: Both added sequencing guidance: pick the document and period first, treat a search snippet as a lead only, open the primary filing with parse_html_page and ask retrieve_information a targeted question, and write plain text without citation markup. agg1 also added a note that parse_html_page cannot read PDFs, a rule not to say a filing "reports" a figure unless it was retrieved, and a rule to report the company-stated rounded figure.
observed: base1 submitted 3.3 from search snippets after one empty web_search and one edgar_search, and its answer leaked raw <cite index> markup. inv1 tried the PDF letter, hit the PDF parse error, then parsed the HTML 10-K and retrieved the "Geographic Mix" passage, confirming 3.3 before submitting. agg1 went straight to the 10-K and retrieved the passage in 4 turns, and its answer had no markup and said "retrieved and verified". dom1 had no such guidance and cited the 10-K as the source without ever fetching it. It saw the 10-K only as a search-result title. The final figure was 3.3 in every run, so the guidance changed verification and presentation rather than the number. Each candidate is one rollout, and agg1 also carried the skill.
verdict: confounded

component: skills/kpi_metric_lookup/SKILL.md (plus the trigger line in systemprompt.md)
candidates: dom1, agg1
change: Added an on-demand skill for company-reported operating metrics: find the controlling source, read the figure from retrieved text, match period and definition, state exclusions, use the company's precision, and sanity-check against neighbouring figures. It includes an unverified task lead. systemprompt.md gained one sentence telling the agent to load it.
observed: dom1 and agg1 both loaded the skill in turn 1. dom1 still did not fetch the filing, although the skill's step 2 says to. It wrote that the 10-K "reports" the figure and added an unverified assumption that regional figures share the "excluding experiences" basis. agg1 loaded the skill, parsed the 10-K and retrieved the definition and exclusion text, so its answer stated the basis accurately. The skill supplied a lead with the 10-K URL, which agg1 used directly (skipping the PDF error that inv1 hit), but that may have come from the lead or from the tool_guidance PDF note. The skill's definition-and-exclusion step matches the extra detail in agg1's answer, but agg1 also had the tool_guidance edit, and dom1's contrast shows the skill alone did not force verification.
verdict: confounded

component: systemprompt.md
candidates: dom1, agg1
change: Added one sentence: for company-reported operating-metric questions, call load_skill with `kpi_metric_lookup`.
observed: Both candidates called load_skill first. The trigger fired, but there is no run without it on a skill-equipped harness, so its effect on the outcome is not isolated from the skill's content.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks for a single reported KPI that web search returns as a snippet, often from a PDF letter, while the filing's HTML is parseable. The base harness has no rule that a snippet must be confirmed in the primary text.
- **lesson**: In tool_guidance.md, state that parse_html_page cannot read PDFs, so use the HTML 10-K or the 8-K EX-99.1 from edgar_search. Require retrieve_information to confirm the figure, period and definition in the fetched filing before submission, and forbid saying a filing "reports" a figure that was not retrieved. Put this rule in always-on tool_guidance rather than only in an on-demand skill.
- **evidence**: The base1 vs inv1/agg1 contrast is the only one where behaviour diverged. base1 submitted from snippets with leaked markup. inv1 and agg1, which carried the verify-in-primary-text guidance, retrieved the "Geographic Mix" passage before submitting. dom1 loaded the skill but never fetched the filing and still claimed the 10-K reported the figure. The skill alone therefore did not enforce verification. Tool_guidance and skill effects are confounded within agg1.
- **confidence**: low. One rollout per candidate, and the figure was 3.3 in every run, so the evidence shows a verification-behaviour difference and not an accuracy difference.
