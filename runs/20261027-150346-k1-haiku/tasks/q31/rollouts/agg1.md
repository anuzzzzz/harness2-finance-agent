## Rollout `agg1`
- outcome: submitted
- turns: 4; cost: $0.005; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Dutch Bros annual report 2024 total revenue cost of sales", "ciks": ["BROS"], "start_date": "2025-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 5, "page": 1, "results": [{"form": "ARS", "file_date": "2025-03-31", "period_ending": "2024-12-31", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-25-000104", "document": "p24788dutchbrothers2024ar-.pdf", "description": "ARS", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000104/p24788dutchbrothers2024ar-.pdf"}, {"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-25-000048", "document": "bros-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000048/bros-20241231.htm"}, {"form": "8-K", "file_date": "2025-02-12", "period_ending": "2025-02-12", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-25-000035", "document": "a2024-q4_ex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000035/a2024-q4_ex991.htm"}, {"form": "DEF 14A", "file_date": "2025-03-31", "period_ending": "2025-05-13", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-25-000102", "document": "bros-20250331.htm", "description": "DEF 14A", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000102/bros-20250331.htm"}, {"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-25-000048", "document": "exh1012025-02x07dutchmaf.htm", "description": "EX-10.1", "url": "https://www.sec.gov/Archives/edgar/data/1866581/00018665812500004
  …[truncated 34 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000035/a2024-q4_ex991.htm", "key": "q4release"})
  result: SUCCESS: The result has been saved to the data storage under the key: q4release. (37,297 characters)
  The data_storage currently contains the following keys:
  q4release
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this earnings release, extract full-year 2024 and full-year 2023 total revenue, total cost of sales (or cost of goods sold), and gross profit / gross margin if reported, in thousands of dollars. Also state the period and whether figures are GAAP. Document: {{q4release}}"})
  result: ## Full-Year Results (in thousands of USD)
  
  | Item | FY2024 (year ended Dec 31, 2024) | FY2023 (year ended Dec 31, 2023) |
  |---|---|---|
  | Total revenues | $1,281,015 | $965,776 |
  | Cost of sales | $940,886 | $714,480 |
  | Consolidated gross profit (not reported; derived as revenue minus cost of sales) | $340,129 (26.6% margin) | $251,296 (26.0% margin) |
  | Company-operated shop gross profit (reported) | $259,959 (22.3% of company-operated shop revenue) | $180,235 (21.0% of company-operated shop revenue) |
  
  ## Notes
  
  - **Source:** Condensed Consolidated Statements of Operations for the year ended December 31, 2024 and 2023. The release does not report a consolidated gross profit or gross margin line.
  - **Derived figures:** The consolidated gross profit and margin are my calculations. Margins use total revenues as the denominator.
  - **Company-operated shop gross profit:** This is a reported operating subtotal, not a consolidated line item. Its margin is calculated on company-operated shop revenue ($1,165,830K in 2024; $857,939K in 2023), not total revenue. It is not labeled non-GAAP in the release. Its cost base includes depreciation and amortization.
  - **GAAP status:** Total revenues, cost of sales, and the income statement are presented under U.S. GAAP. The release labels its financial tables "unaudited."
  - **Non-GAAP:** The release's non-GAAP measures (such as company-operated shop contribution and adjusted EBITDA) are not used in the figures above.

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "Answer: Dutch Bros (BROS) 2026 gross profit is approximately $467 million under the stated assumptions (30% revenue CAGR, gross margin down 500 bps from YE 2024).\n\n1) Base-year inputs (FY2024, unaudited, GAAP, in thousands of USD), from the Q4 2024 earnings release (Exhibit 99.1, filed 2025-02-12):\n- Total revenues: $1,281,015\n- Cost of sales: $940,886\n- The release does not report a consolidated gross profit line, so it is derived: Gross profit = Total revenues − Cost of sales = 1,281,015 − 940,886 = $340,129 (thousand)\n- FY2024 gross margin = 340,129 / 1,281,015 = 26.55% (26.5515%)\n\n2) Assumptions applied:\n- Revenue CAGR 30% over two compounding periods (2024 to 
…[truncated 1,382 chars])

### Final answer
Answer: Dutch Bros (BROS) 2026 gross profit is approximately $467 million under the stated assumptions (30% revenue CAGR, gross margin down 500 bps from YE 2024).

1) Base-year inputs (FY2024, unaudited, GAAP, in thousands of USD), from the Q4 2024 earnings release (Exhibit 99.1, filed 2025-02-12):
- Total revenues: $1,281,015
- Cost of sales: $940,886
- The release does not report a consolidated gross profit line, so it is derived: Gross profit = Total revenues − Cost of sales = 1,281,015 − 940,886 = $340,129 (thousand)
- FY2024 gross margin = 340,129 / 1,281,015 = 26.55% (26.5515%)

2) Assumptions applied:
- Revenue CAGR 30% over two compounding periods (2024 to 2026): 2026 revenue = 1,281,015 × 1.3² = 1,281,015 × 1.69 = $2,164,916 (thousand)
- Gross margin compression of 500 bps = 5.00 percentage points: 2026 margin = 26.5515% − 5.00% = 21.5515%

3) Calculation:
- 2026 gross profit = 2,164,916 × 21.5515% = $466,572 (thousand) ≈ $466.57 million
- Cross-check (second route): 2024 gross profit grown at 30% twice = 340,129 × 1.69 = 574,818; less margin change × 2026 revenue = 0.05 × 2,164,916 = 108,246; result = 574,818 − 108,246 = 466,572 (thousand). Matches.

4) Conclusion: Rounded to the nearest million, 2026 gross profit ≈ $467 million.

Note on basis: "gross margin" here means consolidated gross margin (revenue less cost of sales). The release also reports a company-operated shop gross profit subtotal of $259,959 thousand in 2024 (22.3% of company-operated shop revenue of $1,165,830 thousand). It is a different basis and is not used above. If the shop-level measure were used, the result would differ (roughly $341 million under the same growth and compression applied to shop revenue), so I label it as an alternate only.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000035/a2024-q4_ex991.htm",
            "name": "Dutch Bros Inc. Q4 2024 earnings release (Exhibit 99.1, Form 8-K filed 2025-02-12)"
        }
    ]
}