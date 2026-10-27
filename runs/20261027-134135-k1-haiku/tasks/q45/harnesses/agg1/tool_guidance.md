# Tool guidance

Before searching, decide which document and period the question needs: company, form type (10-K, 10-Q, 8-K exhibit 99.1 or shareholder letter) and fiscal period. Then search with those filters, not the question's wording.

- `edgar_search`: pass the ticker or CIK, a date range, and the form type. If it returns 0 results, change the filters once. If it still returns nothing, use `web_search` for the primary document. Do not repeat a `web_search` that came back empty.
- `parse_html_page`: store each primary document under a clear key (for example `abnb_10k_2024`). When the question is about a full fiscal year, open the 10-K in the same turn as any earnings-release exhibit. Quarterly shareholder letters often give reconciliations by quarter only, with no annual column.
- `retrieve_information`: ask one targeted question at a time. On long filings, use `input_character_ranges`. Ask for the exact figure with its period, unit and row label, quoted verbatim. Table extraction can garble rows. If a row is unclear, check it in another document or table (for example the cash flow statement or a footnote) instead of inferring.

Enough evidence means the figure was read from an annual or period-matching column in a primary document that was actually opened, with period, unit and label matching the question. A sum of quarters is only a cross-check on a reported annual figure, not the primary support. A figure seen only in a search result or a third-party page is a lead, not evidence.

Before `submit_final_result`, re-check each figure against the retrieved text: period, units, label, and rounding as reported. State which document and table each figure came from. Submit while budget remains.
