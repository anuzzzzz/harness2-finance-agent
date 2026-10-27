# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. Use edgar_search with the company and form filters rather than the question's wording. If web_search returns nothing, retry once with a short non-empty query (never an empty or null one), then use edgar_search or a known primary URL.
- A search snippet, result title or your own memory is a lead, not evidence. Every figure that enters a calculation, the start value and the end value alike, must be retrieved from a document you opened with parse_html_page (one clear key per document) and queried with retrieve_information. Ask one targeted question at a time, and confirm the period, unit (thousands vs millions) and GAAP/non-GAAP basis in the retrieved text.
- A 10-K's income statement carries three fiscal years. For a multi-year growth question, open the latest 10-K first and read all needed years from that one table. Open an earlier 10-K only for a year the latest one does not cover, or to cross-check a figure.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit. Use input_character_ranges on long filings.
- Before submitting, re-check each figure in the calculation against the retrieved text, and confirm the number of periods (for example, 2022 to 2024 is 2 years). Carry full precision and round only the final result.
- Cite only documents you opened and retrieved from. Do not list a filing, aggregator page or spreadsheet seen only in search results, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text with no citation markup. State each figure with its period, unit and source, then the calculation, then the result. Leave out remarks about your own recollection. Submit with submit_final_result as soon as the figures are verified.

Task facts (Palantir revenue CAGR 2022 to 2024; re-confirm in the opened text):
- FY2024 10-K: https://www.sec.gov/Archives/edgar/data/1321655/000132165525000022/pltr-20241231.htm (filed 2025-02-18). In an earlier run it was found by edgar_search but never opened. Its revenue was only quoted from a snippet as $2,865,507K, so retrieve it from the filing's income statement.
- FY2023 10-K: https://www.sec.gov/Archives/edgar/data/1321655/000132165524000022/pltr-20231231.htm. It was opened and retrieved from. Revenue in $ thousands: 2023 $2,225,012; 2022 $1,905,871; 2021 $1,541,889.
- Do not use an aggregator's rounded revenue figure.
