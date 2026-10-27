# Tool guidance

Before searching, decide which document and period the question needs: company, form type (10-K, 10-Q, 8-K EX-99.1) and fiscal period. As of the current date, use the most recent filing that covers the question. Search with ticker or CIK, form type and date filters, not the question's wording. If `edgar_search` returns 0 results, change the filters once, then fall back to `web_search` for the primary document.

- `parse_html_page`: store each primary document under a clear key (for example `msci_10k_2024`).
- `retrieve_information`: ask one targeted question at a time. Ask for the table or sentence quoted verbatim, with its period and units. On long filings, use `input_character_ranges`.
- Enough evidence means every figure used in a calculation was read from the text of a primary document opened with `parse_html_page` and `retrieve_information`. A search snippet or third-party page is only a lead.

Calculations: take the components from the retrieved table, state which rows (years) were summed and why, and carry full precision until the final rounding. When a question asks for a share or percentage, state the denominator you used (for example, the table's total or the present value) in one clause. Use the denominator that matches the numerator's basis, and give any other basis only as a secondary note.

Task fact (verified, MSCI lease-maturity question): MSCI's FY2024 10-K (filed 2025-02-07, accession 0001408198-25-000053, URL https://www.sec.gov/Archives/edgar/data/1408198/000140819825000053/msci-20241231.htm) has the operating lease maturity table in Note 7 "Leases". The values are in thousands. 2025 is 30,220, 2026 is 30,361, 2027 is 24,421, 2028 is 23,931, 2029 is 16,573 and thereafter is 40,099. Total lease payments are 165,605, interest is (19,601) and the present value is 146,004. "Next three years" as of April 2025 means 2025–2027, which sum to 85,002. That is 51.33% of the undiscounted total of 165,605. Re-confirm these against the opened filing before submitting.

Before `submit_final_result`, re-check each figure against the retrieved text for period, units and rows summed. Submit while budget remains, and include the sources dictionary.
