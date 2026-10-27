# Tool guidance

Before searching, decide which document and period the question needs: company, form type (10-K, 10-Q, 8-K exhibit 99.1 or shareholder letter) and fiscal period. Then search with those filters, not the question's wording.

- `edgar_search`: pass the ticker or CIK, a date range, and the form type. If it returns 0 results, change the filters once; if still nothing, use `web_search` for the primary document. A first `web_search` with an empty query or 0 results is not a reason to repeat it; go to `edgar_search`.
- `parse_html_page`: store each primary document under a clear key (for example `abnb_10k_2024`). When the question is about a full fiscal year, open the annual filing (10-K) in the same turn as any earnings-release exhibit, instead of rebuilding the year from quarters.
- `retrieve_information`: ask one targeted question at a time. On long filings, use `input_character_ranges`. Ask for the exact figure with its period, unit and label, and the row quoted verbatim. Text extraction of tables can garble rows, so if a row is unclear, re-ask in another document rather than inferring.

Enough evidence means the figure was read from an annual or period-matching column in a primary document that was actually opened, with its period, unit and label matching the question. A sum of quarters is only a cross-check on a reported annual figure, not the answer's primary support. A figure seen only in a search result is a lead.

In this task (Airbnb FY2024 stock-based compensation adjustment): the Q4 2024 shareholder letter (8-K EX-99.1, d915198dex991.htm) gives its Adjusted EBITDA reconciliation by quarter only, with no full-year column. The annual figure ($1,407 million, versus $1,120 million for 2023, per the income-statement footnote) is also in the FY2024 10-K (abnb-20241231.htm). Confirm the annual line in the 10-K (the stock-based compensation line in the cash flow statement or the Adjusted EBITDA reconciliation) and cite it.

Before `submit_final_result`, re-check each figure against the retrieved text: period, units, label, and rounding as reported. State which document each figure came from. Submit while budget remains.
