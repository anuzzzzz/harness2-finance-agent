<file path="tool_guidance.md">
# Tool guidance

Before searching, decide which document and period the question needs: company, form type (10-K, 10-Q, 8-K exhibit 99.1 or shareholder letter) and fiscal period. Then search with those filters, not the question's wording.

- `edgar_search`: pass the ticker or CIK, a date range, and the form type. If it returns 0 results, change the filters once. If it still returns nothing, use `web_search` for the company's investor-relations PDF.
- `web_search`: use it to find primary documents. A snippet or third-party page (statistics aggregators, blogs) is a lead, not evidence. If it returns 0 results, rephrase once, then move to `edgar_search`.
- `parse_html_page`: store each primary document under a clear key (for example `abnb_10k_2024`).
- `retrieve_information`: ask one targeted question at a time. On long filings, use `input_character_ranges`. Ask for the exact figure with its period, unit and definition, and for the sentence or row quoted verbatim.

Enough evidence means the figure was read from the text of a primary document that was actually opened with `parse_html_page` and `retrieve_information`, and its period, unit and definition match the question. A figure that appeared only in a search result is not yet verified, so open its source or the filed 10-K or 8-K and confirm it. If the primary document cannot be opened, say so in the answer and name the secondary source.

Company-defined KPIs (for example average nights per booking, ADR, users by region) are often stated in a prose sentence in the 10-K MD&A rather than in a table, and the earnings release may not contain them. If one document's retrieval says the metric is absent, check the other filing (10-K MD&A, or 8-K EX-99.1) before concluding it is not disclosed. Quote the defining sentence, and note the period (full year vs quarter) and any scope qualifier such as "excluding experiences."

Before `submit_final_result`, re-check each figure against the retrieved text: period, region or segment, units, and rounding as reported. If the company reports a rounded figure and a secondary source gives more precision, give the company's figure and label the other as secondary. Submit while budget remains.
</file>

<notes>
kept (revised) -> inv1 tool_guidance -> base1 turn 2 answered 3.3 from a search snippet and a third-party site, never calling parse_html_page or retrieve_information; inv1 opened the 10-K and confirmed the figure in 3 turns at $0.098 versus $0.199 for dom1. I kept the generic "primary document actually opened" rule and the pre-submit re-check.
revised -> inv1 task-specific Airbnb block -> removed. It would be a stale, unverifiable-for-other-tasks always-on fact that enters the library and could mislead later tasks.
revised -> dom1 company_kpi_lookup skill -> dropped as a skill and folded into tool_guidance as one paragraph. In dom1 turns 4-8 the 8-K EX-99.1 had no regional figure and the 10-K prose sentence did, so the useful lesson is "if one document lacks the metric, check the other filing and the MD&A prose." This avoids an extra trigger line and an extra load_skill turn.
dropped -> dom1 systemprompt trigger line and skill -> its claim that regional splits are often only in the earnings release was contradicted by its own rollout, where the 10-K held the figure. The "recompute the ratio" step was not possible with the disclosed data.
note -> all three rollouts (base1, inv1, dom1) submitted and reached 3.3, so no edit is tied to an unsubmitted run. The gain is in verification from primary source, not in the answer. Evidence is 1 rollout per arm, so the edit is kept small.
</notes>