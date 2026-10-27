<file path="tool_guidance.md">
# Tool guidance

Before searching, decide which document and period the question needs: company, form type (10-K, 10-Q, 8-K exhibit 99.1 or shareholder letter) and fiscal period. Then search with those filters, not the question's wording.

- `edgar_search`: pass the ticker or CIK, a date range, and the form type. If it returns 0 results, change the filters once. If it still returns nothing, use `web_search` for the primary document. Do not repeat a `web_search` that came back empty.
- `parse_html_page`: store each primary document under a clear key (for example `abnb_10k_2024`). When the question is about a full fiscal year, open the 10-K in the same turn as any earnings-release exhibit. Quarterly shareholder letters often give reconciliations by quarter only, with no annual column.
- `retrieve_information`: ask one targeted question at a time. On long filings, use `input_character_ranges`. Ask for the exact figure with its period, unit and row label, quoted verbatim. Table extraction can garble rows. If a row is unclear, check it in another document or table (for example the cash flow statement or a footnote) instead of inferring.

Enough evidence means the figure was read from an annual or period-matching column in a primary document that was actually opened, with period, unit and label matching the question. A sum of quarters is only a cross-check on a reported annual figure, not the primary support. A figure seen only in a search result or a third-party page is a lead, not evidence.

Before `submit_final_result`, re-check each figure against the retrieved text: period, units, label, and rounding as reported. State which document and table each figure came from. Submit while budget remains.
</file>

<notes>
kept -> inv1 (generic parts only: open the 10-K for full-year questions, quarterly sums are only a cross-check, empty-search fallback) -> base1 never opened the 10-K and derived 1,407 from a quarterly sum with an unconfirmed Q4. inv1 opened the 10-K at turn 2 and read the annual line directly, at $0.099 and 4 turns. Counts: 1/1 base run affected, so this is weak evidence, but the rule is cheap and generic.
dropped -> inv1's Airbnb-specific paragraph -> it is task-specific, not reusable, and invites a pointer-to-source shortcut. The library lesson says to keep company-specific URLs and figures out.
dropped -> dom1 skill non_gaap_adjustment_lookup and its systemprompt trigger line -> dom1 spent turn 1 loading the skill and reached the same 1,407 as inv1 at about the same cost ($0.095 against $0.099). The skill embedded task-specific facts, and the gain is already covered by the one-line 10-K rule in tool guidance. This avoids adding always-on prompt text.
kept -> verification guidance from the q44/q09 library (primary document opened, per-figure sourcing, re-check before submit) -> folded into tool_guidance as short generic lines.
No rollout produced nothing: base1, inv1 and dom1 all submitted, so no edit is flagged unsafe on that ground.
</notes>