# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1), fiscal period. Use edgar_search with company and date filters. If web_search returns 0 results, retry once with a short non-empty query (never an empty one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (clear key), then ask retrieve_information one targeted question at a time. Confirm each figure's period, unit and GAAP/non-GAAP basis in the retrieved text. Check that listed components sum to the stated total before ranking or comparing them.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K EX-99.1.
- When the question asks for the "largest" item, rank by absolute value and report the sign and direction of each top candidate (add-back or deduction). Name the runner-up when it is close.
- Cite only documents you opened and retrieved from. Do not list a press-release mirror, article or filing you saw only in search results. Do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags; quote figures directly. State the figure, period and unit, how it was derived, and the source of each figure. Submit with submit_final_result as soon as the figures are verified.

Task fact (verified in one run, re-confirm in the text): in this task, Uber's Q4/FY2023 earnings release (8-K EX-99.1, https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm) has a full-year Adjusted EBITDA reconciliation, in $ millions. It starts from net income attributable to Uber (1,887) and reaches Adjusted EBITDA of 4,052. The largest add-back is stock-based compensation expense at 1,935. The next largest is "Other (income) expense, net" at (1,844), a deduction. D&A is 823 and interest expense is 633.
