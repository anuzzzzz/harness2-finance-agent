## Rollout `base1`
- outcome: submitted
- turns: 4; cost: $0.200; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Zillow Group annual report net cash provided by operating activities capital expenditures", "ciks": ["1617640"], "form_types": ["10-K"], "start_date": "2023-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 3, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-11", "period_ending": "2024-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-25-000016", "document": "z-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm"}, {"form": "10-K", "file_date": "2023-02-15", "period_ending": "2022-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-23-000010", "document": "z-20221231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm"}, {"form": "10-K", "file_date": "2024-02-15", "period_ending": "2023-12-31", "company": "ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640)", "ciks": ["0001617640"], "accession": "0001617640-24-000022", "document": "z-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm", "key": "z2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: z2024. (467,105 characters)
  The data_storage currently contains the following keys:
  z2024
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm", "key": "z2023"})
  result: SUCCESS: The result has been saved to the data storage under the key: z2023. (503,493 characters)
  The data_storage currently contains the following keys:
  z2024
  z2023
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Zillow 10-K text: {{z2024}} — extract (1) Net cash provided by operating activities for 2024, 2023, 2022; (2) Purchases of property and equipment and capitalized software (capex, including any capitalized software/internal-use software line) for 2024, 2023, 2022; (3) Total revenue for 2024, 2023, 2022. Give exact figures in millions with the table source."})
  result: | Metric (in millions) | 2024 | 2023 | 2022 | Source |
  |---|---|---|---|---|
  | Net cash provided by operating activities | $428 | $354 | $4,504 | Consolidated Statements of Cash Flows (Item 8) |
  | Purchases of property and equipment | $(143) | $(135) | $(115) | Consolidated Statements of Cash Flows, investing activities |
  | Purchases of intangible assets (includes capitalized software) | $(28) | $(30) | $(25) | Consolidated Statements of Cash Flows, investing activities |
  | Total revenue | $2,236 | $1,945 | $1,958 | Consolidated Statements of Operations (Item 8) |
  
  **Notes:**
  - The cash flow statement has no separate "capitalized software" line. The filing says capitalized internal-use software is recorded within purchases of intangible assets (Note 2), so that line is the closest match. The purchases of property and equipment line is separate.
  - If you define capex as property and equipment plus intangible asset purchases, the totals are $171M (2024), $165M (2023), and $140M (2022). The MD&A states the 2024 figure as $171M.
  - The 2022 operating cash flow of $4,504M is inflated by the Zillow Offers wind-down, mainly a $3,904M decrease in inventory. It is not comparable to 2023 or 2024.
- retrieve_information({"prompt": "From this Zillow 10-K text: {{z2023}} — extract (1) Net cash provided by operating activities for 2023, 2022, 2021; (2) Purchases of property and equipment and capitalized software (capex) for 2023, 2022, 2021; (3) Total revenue for 2023, 2022, 2021. Give exact figures in millions."})
  result: **Zillow Group, Inc. (fiscal years ended December 31, in millions)**
  
  | Metric | 2023 | 2022 | 2021 |
  |---|---|---|---|
  | Net cash provided by (used in) operating activities | $354 | $4,504 | $(3,177) |
  | Purchases of property and equipment | $(135) | $(115) | $(74) |
  | Purchases of intangible assets | $(30) | $(25) | $(31) |
  | Total capex (property and equipment + intangible assets) | $165 | $140 | $105 |
  | Total revenue | $1,945 | $1,958 | $2,132 |
  
  Notes:
  - The filing does not show a line item called "capitalized software." The closest line is "Purchases of intangible assets," which also includes purchased content, so the capex totals above are property and equipment plus intangible asset purchases.
  - The 2022 and 2021 operating cash flows include discontinued operations (Zillow Offers), which the company did not separate in the cash flow statement. The 2022 figure is largely driven by the $3.9 billion decrease in inventory as Zillow Offers wound down. The 2021 figure reflects the inventory build during that business.

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Zillow Group (CIK 1617640) – Approximate Free Cash Flow (CFO − Capex) and FCF margin, FY2022–FY2024**\n\n**Inputs (from Zillow's 10-K filings for FY2023 and FY2024, $ millions):**\n\n| Metric | FY2022 | FY2023 | FY2024 |\n|---|---|---|---|\n| Net cash from operating activities (CFO) | 4,504 | 354 | 428 |\n| Purchases of property and equipment | 115 | 135 | 143 |\n| Purchases of intangible assets (incl. capitalized internal-use software) | 25 | 30 | 28 |\n| Capex used (PP&E + intangibles) | 140 | 165 | 171 |\n| Total revenue | 1,958 | 1,945 | 2,236 |\n\nNote: Zillow's cash flow statement has no standalone \"capitalized software\" line. Capitalized software sits within purc
…[truncated 1,706 chars])

### Final answer
**Zillow Group (CIK 1617640) – Approximate Free Cash Flow (CFO − Capex) and FCF margin, FY2022–FY2024**

**Inputs (from Zillow's 10-K filings for FY2023 and FY2024, $ millions):**

| Metric | FY2022 | FY2023 | FY2024 |
|---|---|---|---|
| Net cash from operating activities (CFO) | 4,504 | 354 | 428 |
| Purchases of property and equipment | 115 | 135 | 143 |
| Purchases of intangible assets (incl. capitalized internal-use software) | 25 | 30 | 28 |
| Capex used (PP&E + intangibles) | 140 | 165 | 171 |
| Total revenue | 1,958 | 1,945 | 2,236 |

Note: Zillow's cash flow statement has no standalone "capitalized software" line. Capitalized software sits within purchases of intangible assets, so I used PP&E plus intangibles as the capex proxy.

**Free cash flow (CFO − Capex):**
- FY2022: 4,504 − 140 = 4,364
- FY2023: 354 − 165 = 189
- FY2024: 428 − 171 = 257

**FCF margin (FCF ÷ Total revenue):**
- FY2022: 4,364 ÷ 1,958 = 222.88%
- FY2023: 189 ÷ 1,945 = 9.72%
- FY2024: 257 ÷ 2,236 = 11.49%

**Trend:** The margin fell sharply from FY2022 to FY2023 (222.88% to 9.72%) and then recovered modestly in FY2024 (to 11.49%). Over the full period, the endpoint comparison is a large decline, but that is distorted by FY2022. In 2022, operating cash flow was inflated by the wind-down of Zillow Offers, mainly a roughly $3.9 billion decrease in inventory. That figure reflects a one-time unwinding of the business rather than recurring cash generation. Excluding FY2022, the trend is an improvement: FCF margin rose from about 9.72% in FY2023 to about 11.49% in FY2024, as CFO rose and revenue grew while capex stayed modest.

Caveat: FY2022 CFO also includes discontinued operations, which the company did not separate in the cash flow statement.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm",
            "name": "Zillow Group FY2024 Form 10-K"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764024000022/z-20231231.htm",
            "name": "Zillow Group FY2023 Form 10-K"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1617640/000161764023000010/z-20221231.htm",
            "name": "Zillow Group FY2022 Form 10-K"
        }
    ]
}