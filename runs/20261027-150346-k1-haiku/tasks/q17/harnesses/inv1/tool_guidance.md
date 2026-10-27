# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1), fiscal periods. Use edgar_search with the company CIK, form type and dates, not the question's wording. If web_search returns 0 results, retry once with a short non-empty query (never an empty or null query), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document). Then ask retrieve_information one targeted question at a time. Confirm each figure's period, unit and GAAP/non-GAAP basis in the retrieved text before it enters a calculation.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K EX-99.1.
- Multi-year ratio or trend questions: a 10-K carries comparative columns (income statement three years, key metrics two or three years). Take each year from the latest filing that carries it. When the same year appears in two filings, check that the two figures agree, and say if a later filing restated one.
- Carry full precision through the calculation and round only the final figure (two decimals for ratios and percentages). Recompute each ratio once from the retrieved inputs before submitting.
- Cite only documents you opened and retrieved from. Do not list a filing as a source, or attribute a figure to it, unless that figure was retrieved from it. Say plainly if a figure came from a comparative column in a different year's filing.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags or quoted passages carrying such tags. Give each figure with its period, unit and source, then the calculation, then the result in the form the question asks for. Submit with submit_final_result as soon as the figures are verified.

Task facts (Airbnb take rate, revenue / Gross Booking Value; verified in an earlier run, re-confirm in the text). Units are $ millions.
- FY2022: revenue 8,399, GBV 63,212. FY2023: revenue 9,917, GBV 73,252. FY2024: revenue 11,102, GBV 81,784.
- GBV is in the 10-K MD&A "Key Business Metrics" table. Revenue is in the Results of Operations / income statement.
- The FY2023 10-K (https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm) gave FY2022 and FY2023. The FY2024 10-K (https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm) gave FY2023 and FY2024. The FY2022 10-K was never opened, so do not list it as a source unless you retrieve from it.
- Resulting take rates: 13.29%, 13.54%, 13.57%. The rate is roughly flat, with a small rise in 2023 and almost none in 2024.
