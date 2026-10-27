# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1), fiscal period. Use edgar_search with company and date filters, not the question's wording. If web_search returns 0 results, retry once with a shorter query, then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (store it under a clear key), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP basis in the retrieved text. Use input_character_ranges on long filings.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K EX-99.1.
- Prefer the annual 10-K for full-year figures and for prior-year comparatives (it carries both years). Cite only documents you opened and retrieved from.
- When the filing itself states a ratio or rate (effective tax rate, margin, growth %), that company-stated figure is the headline input. Compute any change or delta (in bps or points) from the stated figures. Show the rate recomputed from unrounded dollar amounts as one labelled cross-check line, and state which basis the "Delta" line uses. Do not present two deltas as equal answers.
- Before submitting, recompute each division and subtraction once and make sure the answer follows the exact format the question prescribes (e.g. "Delta: XXXbps").
- Write the final answer in plain text, no citation markup. Submit with submit_final_result as soon as the figures are verified in the primary text.

Task fact (verified in a prior run; re-confirm in text): Oracle FY2024 10-K (https://www.sec.gov/Archives/edgar/data/1341439/000095017024075605/orcl-20240531.htm), MD&A "Provision for Income Taxes", states effective tax rate 10.9% (FY2024) vs 6.8% (FY2023). Underlying $M: provision 1,274 / 623; pre-tax income 11,741 / 9,126. The 19.2% / 16.3% figures in footnote (5) are non-GAAP-adjusted rates, not the GAAP effective rate the question asks about.
