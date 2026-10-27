# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1 earnings release) and fiscal period. Use edgar_search with company and date filters, not the question's wording. If web_search returns nothing, retry once with a short non-empty query. Never send an empty or null query. Then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document). Then ask retrieve_information one targeted question at a time. Confirm each figure's period, unit and GAAP/non-GAAP basis in the retrieved text. Use input_character_ranges on long filings.
- parse_html_page cannot read PDFs, and some commercial sites return HTTP 403. On a failed fetch, do not retry the same URL. Switch once to the SEC HTML filing or exhibit for the same document.
- When a metric the question names (for example gross profit or gross margin) is not a reported line, derive it from reported lines (for example revenue minus cost of sales). Say it is derived and give the formula. Check whether the company reports a similarly named segment measure, and say which one you used and why.
- For what-if or projection questions, retrieve the base-year inputs from source text. Apply the stated growth and margin change exactly as worded, and state the compounding periods (for example 2024 to 2026 is two years). Carry full precision, round only the final number to the unit the question asks, and cross-check the result by a second route (for example base profit at the old margin less the margin change times projected revenue).
- Cite only documents you opened and retrieved from. A URL that failed to load, or that you saw only in search results, is not a source. Write the final answer in plain text with no citation markup. State each figure with its period, unit and source, then the calculation, then the conclusion. Submit with submit_final_result as soon as the figures are verified.

Task facts (Dutch Bros, BROS; verified in the opened text of one earlier run, so re-confirm quickly):
- The FY2024 figures are in the Q4/FY2024 earnings release, 8-K EX-99.1, filed 2025-02-12: https://www.sec.gov/Archives/edgar/data/1866581/000186658125000035/a2024-q4_ex991.htm. Units are $ thousands.
- Year ended Dec 31, 2024: total revenues 1,281,015; cost of sales 940,886 (includes depreciation and amortization).
- The consolidated statements of operations carry no gross profit line. Consolidated gross profit derived is 340,129 (26.55%).
- "Company-operated shop gross margin" of 22.3% (shop gross profit 259,959 on shop revenues of 1,165,830) is a different, segment-only measure. If you use it instead of the consolidated margin, label it as an alternate.
