## Rollout `static1`
- outcome: submitted
- turns: 4; cost: $0.097; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Dutch Bros annual report 2024 total revenue cost of sales gross margin", "ciks": ["BROS"], "form_types": ["10-K"], "start_date": "2025-01-01"})
  result: {"total_matching_documents": 1, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-25-000048", "document": "bros-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000048/bros-20241231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000048/bros-20241231.htm", "key": "bros10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: bros10k. (450,132 characters)
  The data_storage currently contains the following keys:
  bros10k
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Dutch Bros 10-K: {{bros10k}}. Find total revenue for fiscal 2024 and fiscal 2023 (in thousands), total cost of sales for 2024, and gross profit / gross margin for 2024 as reported (or computed as revenue minus cost of sales). Quote the exact figures and the line items they come from."})
  result: **Fiscal 2024 and 2023 total revenue (Consolidated Statements of Operations, in thousands):**
  
  - **Total revenues, 2024: $1,281,015**
  - **Total revenues, 2023: $965,776**
  
  These are the sum of two revenue lines:
  
  | Revenue line | 2024 | 2023 |
  |---|---|---|
  | Company-operated shops | $1,165,830 | $857,939 |
  | Franchising and other | $115,185 | $107,837 |
  | **Total revenues** | **$1,281,015** | **$965,776** |
  
  **Cost of sales, 2024:** $940,886 (reported as "Cost of sales" in the statement of operations)
  
  **Gross profit and gross margin, 2024:**
  
  - Gross profit = $1,281,015 − $940,886 = **$340,129** (about $340.1 million)
  - Gross margin = $340,129 ÷ $1,281,015 = **about 26.6%** (26.55%)
  
  The 10-K does not report a gross profit line on the face of the income statement, so this figure is computed. Cost of sales includes depreciation and amortization, occupancy costs, and pre-opening costs. The company's segment table reconciles to the same total: company-operated shop gross profit of $259,959 plus franchising and other gross profit of $80,170 equals $340,129.

### Turn 4  (stop_reason=tool_use)
**Answer: BROS 2026 gross profit is about $467 million** (based on FY2024 revenue of $1,281.0M and a 26.55% gross margin, grown at 30% CAGR with a 5-point margin compression).

**Step 1: FY2024 baseline from the 10-K (fiscal year ended Dec 31, 2024)**
- Total revenues: $1,281,015K (company-operated shops $1,165,830K plus franchising and other $115,185K).
- Cost of sales: $940,886K. The 10-K has no gross profit line on the face of the income statement, so I computed it.
- Gross profit: $1,281,015K − $940,886K = $340,129K.
- Gross margin: $340,129K ÷ $1,281,015K = 26.55% (0.265515).

**Step 2: Project 2026 revenue (two years of 30% CAGR from 2024)**
- Growth factor: 1.30² = 1.69.
- 2026 revenue: $1,281.015M × 1.69 = $2,164.92M.

**Step 3: Compress gross margin by 500 bps**
- 2026 margin: 26.55% − 5.00 pts = 21.55% (0.215515).

**Step 4: 2026 gross profit**
- $2,164.92M × 0.215515 = $466.57M, which rounds to **$467 million**.

**Assumptions:** "500bps" is read as 5 percentage points, and the margin is the computed gross margin (revenue less cost of sales, which includes occupancy, D&A and pre-opening costs), since the 10-K reports no gross profit line.

**Sources:**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000048/bros-20241231.htm",
            "name": "Dutch Bros Inc. (BROS) Form 10-K for fiscal year ended December 31, 2024"
        }
    ]
}
- submit_final_result({"final_result": "BROS 2026 gross profit ≈ $467 million.\n\nSteps:\n1. FY2024 (10-K, FYE 12/31/2024): total revenues $1,281,015K; cost of sales $940,886K; gross profit (computed) = $340,129K; gross margin = 26.55%.\n2. 2026 revenue at 30% CAGR over two years: $1,281.015M × 1.30² = $2,164.92M.\n3. 2026 gross margin: 26.55% − 5.00 pts (500 bps) = 21.55%.\n4. 2026 gross profit: $2,164.92M × 21.55% = $466.57M ≈ $467M.\n\nAssumptions: 500 bps read as 5 percentage points; gross margin computed as revenue less cost of sales (the 10-K reports no gross profit line).\n\nSources:\n{\n    \"sources\": [\n        {\n            \"url\": \"https://www.sec.gov/Archives/edgar/data/1866581/000186658125000048
…[truncated 144 chars])

### Final answer
BROS 2026 gross profit ≈ $467 million.

Steps:
1. FY2024 (10-K, FYE 12/31/2024): total revenues $1,281,015K; cost of sales $940,886K; gross profit (computed) = $340,129K; gross margin = 26.55%.
2. 2026 revenue at 30% CAGR over two years: $1,281.015M × 1.30² = $2,164.92M.
3. 2026 gross margin: 26.55% − 5.00 pts (500 bps) = 21.55%.
4. 2026 gross profit: $2,164.92M × 21.55% = $466.57M ≈ $467M.

Assumptions: 500 bps read as 5 percentage points; gross margin computed as revenue less cost of sales (the 10-K reports no gross profit line).

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000048/bros-20241231.htm",
            "name": "Dutch Bros Inc. (BROS) Form 10-K for fiscal year ended December 31, 2024"
        }
    ]
}