# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1), fiscal period. Use edgar_search with company and date filters. If web_search returns 0 results, retry once with a short non-empty query (never an empty one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information targeted questions. Confirm each figure's period, unit and GAAP/non-GAAP basis in the retrieved text.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K EX-99.1.
- Non-GAAP reconciliation questions ("largest adjustment", "biggest add-back"):
  - Retrieve the full reconciliation table for the exact fiscal period, with every line item and its sign. Check that the lines sum to the reported total (e.g. Adjusted EBITDA) before ranking.
  - Rank by absolute value. State the sign and direction (add-back or deduction) of each top candidate, name the runner-up when it is close, and say if the largest add-back differs from the largest absolute item. Give the line name as the company labels it, in the unit the question asks for.
  - If the release gives only quarterly columns, look for a full-year column, or sum the four quarters and cross-check against the 10-K.
- Cite only documents you opened and retrieved from. Do not list a press-release mirror, article or filing seen only in search results, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. State the figure, period and unit, how it was derived, and the source of each figure. Submit with submit_final_result as soon as the figures are verified.

Task fact (verified in earlier runs, re-confirm in the text): Uber FY2023, Q4 2023 earnings release (8-K EX-99.1, 2024-02-07, https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm). Its full-year Adjusted EBITDA reconciliation, in $ millions, starts from net income attributable to Uber of 1,887 and totals 4,052. The largest add-back is stock-based compensation expense at 1,935. "Other (income) expense, net" at (1,844) is a close second in size but is a deduction. D&A is 823 and interest expense is 633.
