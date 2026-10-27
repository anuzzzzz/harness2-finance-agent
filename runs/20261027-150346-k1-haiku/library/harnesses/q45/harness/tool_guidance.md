# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1), fiscal period. Use edgar_search with company and date filters. If web_search returns 0 results, retry once with a shorter query, then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (store it under a clear key), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP basis in the retrieved text.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K EX-99.1.
- Prefer the annual filing (10-K) for a full-year figure. If a document gives only quarterly columns, sum the four quarters and also look for a full-year figure elsewhere in the same document (e.g. a footnote or cash-flow statement). Cross-check the two. If the 10-K is cheap to open, confirm the full-year figure there too.
- Use input_character_ranges on long filings rather than re-reading everything.
- Cite only documents you opened and retrieved from. Do not list a filing as a source, or attribute a specific figure to it, unless you retrieved that figure from it. Say plainly if a figure came from a different document.
- Write the final answer in plain text with no citation markup. State the figure, period and unit, how it was derived, and the source of each figure. Submit with submit_final_result as soon as the figure is verified in the primary text.

Lead for this task (re-confirm in the text): Airbnb FY2024 stock-based compensation add-back in Adjusted EBITDA. The Q4 2024 8-K EX-99.1 (https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm) reconciles by quarter only: 295, 382, 362 and 368, summing to $1,407M. The FY2024 10-K is https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm. Units are $ millions. Do not confuse this with the $1,424M equity credit in the stockholders' equity statement.
