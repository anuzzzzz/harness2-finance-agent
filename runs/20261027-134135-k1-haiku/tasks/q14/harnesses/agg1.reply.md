<file path="tool_guidance.md">
# Tool guidance

Before searching, decide which documents and periods the question needs: company, form type (10-K, 10-Q, 8-K exhibit 99.1), and fiscal periods. Search with those filters, not the question's wording. Use only documents dated on or before April 07, 2025.

- `edgar_search`: pass the ticker or CIK, a date range, and the form type. If it returns 0 results, change the filters once. If it still returns nothing, use `web_search` for the primary document. Do not repeat an empty `web_search`.
- `web_search`: use it to find primary documents. A snippet or third-party page (data aggregators, blogs) is a lead, not evidence.
- `parse_html_page`: store each primary document under a clear key. For multi-year or full-year questions, open the 10-K filings in parallel in one turn, including the 10-K of the earliest year asked. The latest 10-K covers three years of income and cash-flow columns, and the earliest year's own 10-K is the cross-check.
- `retrieve_information`: ask one targeted question per document and request several related lines at once (for example CFO, capex lines and total revenue for every year shown). Ask for exact figures with period, unit and row label. If a row is unclear, check it in a second table or note.

Enough evidence means each figure in the calculation was read from a period-matching column of a primary document that was opened and retrieved. Do not cite a third-party site or snippet as the source of a figure that enters the calculation. Do not say a figure was "read from" a filing unless a retrieve call returned it.

Multi-year ratio or trend questions (for example FCF margin = (CFO − capex) / revenue):
- State the formula and capex definition. Default capex is "Purchases of property and equipment". Show purchases of intangible assets as a labelled sensitivity.
- Show each year's inputs, result and the unrounded arithmetic. Give the trend direction year by year (up or down, in percentage points) and across the whole span.
- If one year is distorted (discontinued operations, inventory liquidation), keep the as-reported figure in the headline and name the line that drives the distortion. Say what the comparable years show.

Before `submit_final_result`, re-check each figure for period, units and label, and state which document each came from. Write plain text with no citation tags. Submit while budget remains.
</file>

<notes>
kept -> inv1 (no edit proposed) -> the harness otherwise stays at base; base1 sourced CFO, capex and revenue from opened 10-Ks, while the inv1 rollout (same harness) submitted at turn 2 using stockanalysis/MarketBeat snippets and no parse call, so sourcing varied across the two base-harness runs (1 of 2 never opened a filing); I added a short generic evidence rule to tool_guidance.md.
revised -> dom1 skill fcf_margin_trend -> I dropped the skill: it costs a load turn (5 turns, $0.21 against base1's 4 turns, $0.20) and embeds Zillow-specific figures. Its useful parts (open the earliest year's 10-K, capex definition, as-reported series plus the distortion, year-by-year direction) are carried as a few generic lines in tool_guidance.md, with no company values and no skill or trigger line.
dropped -> dom1 systemprompt trigger line -> there is no skill to trigger, so systemprompt.md stays at base.
kept -> dom1 behaviour (open FY2022 10-K, ex-inventory sensitivity) -> single rollout, so it is folded into the generic distortion rule, not added as separate always-on text.
</notes>