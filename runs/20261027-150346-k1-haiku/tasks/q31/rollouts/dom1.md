## Rollout `dom1`
- outcome: submitted
- turns: 5; cost: $0.006; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "scenario_projection_margin"})
  result: ---
  name: scenario_projection_margin
  description: Project a line (gross profit, operating income) from a base-year figure using an assumed growth rate and an assumed margin change in bps, with the base margin rebuilt from filed statements.
  ---
  ANALYTIC MOVE: calculate. Inputs are the base-year revenue, the base-year cost line or margin (from filed statements), the assumed growth rate and the assumed margin change. The result is the projected-year dollar figure.
  
  1. Base year. Take "YE 2024" or "FY2024" as the fiscal year ended on the filing's balance-sheet date. Retrieve total revenue and cost of sales from the Consolidated Statements of Operations in the 10-K or the Q4 8-K EX-99.1. Check the unit (thousands vs millions) and keep full precision.
  2. Margin definition. Many issuers print no "gross profit" line. If so, derive gross profit = total revenues - total cost of sales, and state that it is derived. Say whether cost of sales includes depreciation and amortization. Do not swap in a segment or shop-level margin that the company reports on a different basis unless you label it as an alternate. Applying a segment margin to consolidated revenue mixes bases.
  3. Projection. Revenue in year N = base revenue x (1+g)^(N - base year). "30% CAGR from 2024 to 2026" means two compounding periods. Margin in year N = base margin - bps/10,000, where 500 bps is 5.00 percentage points. Gross profit = projected revenue x projected margin. Cross-check as base gross profit x (1+g)^n minus the bps change x projected revenue.
  4. Answer contract: the base revenue, the cost of sales, the derived gross profit and margin (with units and period); the projected revenue; the projected margin; the formula and unrounded arithmetic; the final figure rounded as the question asks (for example "neares
  …[truncated 814 chars]
- edgar_search({"search_query": "Dutch Bros 10-K 2024 annual report total revenue gross profit", "start_date": "2025-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 45, "page": 1, "results": [{"form": "ARS", "file_date": "2025-03-31", "period_ending": "2024-12-31", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-25-000104", "document": "p24788dutchbrothers2024ar-.pdf", "description": "ARS", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000104/p24788dutchbrothers2024ar-.pdf"}, {"form": "8-K", "file_date": "2025-02-12", "period_ending": "2025-02-12", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-25-000035", "document": "a2024-q4_ex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000035/a2024-q4_ex991.htm"}, {"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-25-000048", "document": "bros-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000048/bros-20241231.htm"}, {"form": "DEF 14A", "file_date": "2025-03-31", "period_ending": "2025-05-13", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-25-000102", "document": "bros-20250331.htm", "description": "DEF 14A", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000102/bros-20250331.htm"}, {"form": "10-K", "file_date": "2025-03-20", "period_ending": "2024-12-31", "company": "MSC INCOME FUND, INC.  (MSIF)  (CIK 0001535778)", "ciks": ["0001535778"], "accession": "0001535778-25-000073", "document": "msif-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1535778/000153577825000073/msif-
  …[truncated 5,367 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000035/a2024-q4_ex991.htm", "key": "bros_q4"})
  result: SUCCESS: The result has been saved to the data storage under the key: bros_q4. (37,297 characters)
  The data_storage currently contains the following keys:
  bros_q4
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Dutch Bros Q4 2024 release, extract the full-year 2024 total revenues and total cost of sales (in thousands), and any gross profit line, and state the units and period. Also quote the company-operated shop gross margin figure. Document: {{bros_q4}}"})
  result: **Period and units:** Fiscal year ended December 31, 2024 (full year). Figures are in thousands of U.S. dollars, unaudited, from the Condensed Consolidated Statements of Operations.
  
  | Item | FY 2024 (in thousands) |
  |---|---|
  | Total revenues | $1,281,015 |
  | Total cost of sales | $940,886 |
  | Gross profit (consolidated) | Not reported |
  
  - **Gross profit:** The release has no consolidated gross profit line. Calculated from the figures above, total revenues less cost of sales would be $340,129 thousand, but this is my derivation, not a company-reported number.
  - **Company-operated shop gross profit:** $259,959 thousand, reported in the company-operated shop results and the non-GAAP reconciliation.
  
  **Company-operated shop gross margin (FY 2024):** 22.3%. The release says this includes 130 bps of pre-opening costs and improved 130 bps year over year from 21.0%.
  
  **Note on cost of sales:** The $940,886 thousand consolidated cost of sales includes depreciation and amortization. The segment table shows "segment cost of sales" of $849,162 thousand, which excludes D&A, so it should not be substituted for the consolidated figure.

### Turn 4  (stop_reason=end_turn)
**Answer: BROS 2026 gross profit is about $467 million** (derived, unrounded ≈ $466.57M).

**Base year (FY2024, from the Q4 2024 earnings release, EX-99.1, in thousands of USD):**
- Total revenues: $1,281,015K
- Total cost of sales: $940,886K (includes depreciation and amortization)
- The release has no consolidated gross profit line, so I derived it: $1,281,015K − $940,886K = $340,129K.
- Derived gross margin: $340,129K / $1,281,015K = 26.5515%.

**Projection:**
- Revenue in 2026 = $1,281,015K × (1.30)² = $1,281,015K × 1.69 = $2,164,916.35K (about $2,164.92M). The 30% CAGR covers two compounding periods, 2024 to 2026.
- Margin in 2026 = 26.5515% − 5.00 pts = 21.5515%.
- Gross profit = $2,164,916.35K × 21.5515% ≈ $466,572K, or about $466.57M.

**Cross-check:** Base gross profit × 1.69 = $574,818.01K. Less 5.00% × $2,164,916.35K = $108,245.82K. Result: $466,572.19K, which matches.

**Rounded to the nearest million:** $467 million.

**Alternate reading not used:** The company-operated shop gross margin of 22.3% is a segment measure on a different basis. Applying it to consolidated revenue would mix bases, so I did not use it. The segment cost of sales ($849,162K) also excludes D&A, so I used the consolidated cost of sales instead.

```json
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000035/a2024-q4_ex991.htm",
            "name": "Dutch Bros Inc. Q4 and FY2024 earnings release (Form 8-K EX-99.1)"
        }
    ]
}
…[truncated 4 chars]

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "Answer: BROS 2026 gross profit is about $467 million (derived, unrounded ≈ $466.57M).\n\nBase year (FY2024, from the Q4 2024 earnings release, Form 8-K EX-99.1, in thousands of USD):\n- Total revenues: $1,281,015K\n- Total cost of sales: $940,886K (includes depreciation and amortization)\n- The release has no consolidated gross profit line, so gross profit is derived: $1,281,015K − $940,886K = $340,129K.\n- Derived gross margin: $340,129K / $1,281,015K = 26.5515%.\n\nProjection:\n- 2026 revenue = $1,281,015K × (1.30)^2 = $1,281,015K × 1.69 = $2,164,916.35K (about $2,164.92M). The 30% CAGR covers two compounding periods, 2024 to 2026.\n- 2026 margin = 26.5515% − 5.00 percent
…[truncated 831 chars])

### Final answer
Answer: BROS 2026 gross profit is about $467 million (derived, unrounded ≈ $466.57M).

Base year (FY2024, from the Q4 2024 earnings release, Form 8-K EX-99.1, in thousands of USD):
- Total revenues: $1,281,015K
- Total cost of sales: $940,886K (includes depreciation and amortization)
- The release has no consolidated gross profit line, so gross profit is derived: $1,281,015K − $940,886K = $340,129K.
- Derived gross margin: $340,129K / $1,281,015K = 26.5515%.

Projection:
- 2026 revenue = $1,281,015K × (1.30)^2 = $1,281,015K × 1.69 = $2,164,916.35K (about $2,164.92M). The 30% CAGR covers two compounding periods, 2024 to 2026.
- 2026 margin = 26.5515% − 5.00 percentage points = 21.5515%.
- Gross profit = $2,164,916.35K × 21.5515% ≈ $466,572K, or about $466.57M.

Cross-check: base gross profit × 1.69 = $574,818.01K; less 5.00% × $2,164,916.35K = $108,245.82K; result $466,572.19K, which matches.

Rounded to the nearest million: $467 million.

Alternate reading not used: the company-operated shop gross margin of 22.3% is a segment measure on a different basis, so applying it to consolidated revenue would mix bases. The segment cost of sales ($849,162K) excludes D&A, so the consolidated cost of sales was used instead.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000035/a2024-q4_ex991.htm",
            "name": "Dutch Bros Inc. Q4 and FY2024 earnings release (Form 8-K EX-99.1)"
        }
    ]
}