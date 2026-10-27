# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. If edgar_search returns other companies (name matching is loose), retry once with the ticker or full legal name and the filing-year date window. Then try web_search with a short non-empty query (never empty or null) and look for an sec.gov URL, then use a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary filing with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm each figure's period, unit and line-item definition in the retrieved text. Use input_character_ranges on long filings. A figure seen only in a snippet may not enter the final calculation until it is confirmed in an opened document.
- Prefer the 10-K (face financial statements) over a press release. One 10-K carries both year-end balance-sheet columns and three years of income-statement lines, so open the latest 10-K before any older filing.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit.
- For a ratio, retrieve numerator and denominator inputs separately, each with period and unit. If the question does not fix the convention (for example, average versus ending balance), compute the standard one as the headline and show the alternate on one line. Carry full precision and round only the final number. Re-check each input against the retrieved text just before submitting.
- Cite only documents you opened and retrieved from. Do not list a press release, article or PDF seen only in search results, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. State each figure with its period, unit and source, then the calculation, then the conclusion. Submit with submit_final_result as soon as the figures are verified.

Lead for this task (United States Steel Corp., FY2024 inventory turnover; from search snippets only, so re-confirm in the opened text):
- The FY2024 10-K appeared in search as https://www.sec.gov/Archives/edgar/data/1163302/000116330225000018/x-20241231.htm (company CIK 1163302, ticker X). Open it and retrieve the consolidated statements of operations and balance sheet.
- Snippets from the Q4 2024 earnings release suggested cost of sales of $14,060M for 2024 and inventories of $2,168M at 12/31/2024 versus $2,128M at 12/31/2023 ($ millions). These are unverified.
- U.S. Steel's income statement may show depreciation, depletion and amortization as a separate line outside cost of sales. Confirm this in the filing. If so, use the reported cost of sales line and say so in one sentence.
