## Rollout `base1`
- outcome: submitted
- turns: 4; cost: $0.016; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Uber fourth quarter 2023 results Adjusted EBITDA reconciliation full year 2023") → 0 results: 
- edgar_search({"search_query": "Uber Adjusted EBITDA reconciliation 2023 annual report", "ciks": ["UBER"], "start_date": "2024-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 16, "page": 1, "results": [{"form": "8-K", "file_date": "2024-05-08", "period_ending": "2024-05-08", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000017", "document": "uberq124earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000017/uberq124earningspressrelea.htm"}, {"form": "8-K", "file_date": "2024-08-06", "period_ending": "2024-08-06", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000024", "document": "uberq224earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000024/uberq224earningspressrelea.htm"}, {"form": "8-K", "file_date": "2025-02-05", "period_ending": "2025-02-05", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-25-000004", "document": "uberq424earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315125000004/uberq424earningspressrelea.htm"}, {"form": "8-K", "file_date": "2024-02-07", "period_ending": "2024-02-07", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000008", "document": "uberq423earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm"}, {"form": "8-K", "file_date": "2024-02-14", "period_ending": "2024-02-06", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001552781-24-000039", "document": "e24041_ex99-2.htm
  …[truncated 4,098 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 9 results: Uber Technologies, Inc - Form 8-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1543151/000154315123000004/uberq422earningspressrelea.htm>; Uber Technologies, Inc - Form 8-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1543151/000154315123000021/uberq223earningspressrelea.htm>; Press release dated February 7, 2024 <https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm>; Uber Technologies, Inc - Form 10-Q - FY2023 <https://www.sec.gov/Archives/edgar/data/1543151/000154315123000016/uber-20230331.htm>; Uber Announces Results for Fourth Quarter and Full Year 2023 <https://www.nasdaq.com/press-release/uber-announces-results-for-fourth-quarter-and-full-year-2023-2024-02-07>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm", "key": "uber_q4_2023"})
  result: SUCCESS: The result has been saved to the data storage under the key: uber_q4_2023. (49,646 characters)
  The data_storage currently contains the following keys:
  uber_q4_2023
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Uber Q4 2023 press release, find the full-year 2023 (twelve months ended December 31, 2023) Adjusted EBITDA reconciliation table, which starts from Net income (loss) and lists adjustments (e.g., depreciation and amortization, provision for (benefit from) income taxes, net interest expense, net unrealized (gains) losses on equity investments, stock-based compensation, etc.). List every line item with its full-year 2023 amount in millions, and identify the largest adjustment in absolute value. {{uber_q4_2023}}"})
  result: ## Full-Year 2023 Adjusted EBITDA Reconciliation (Year Ended December 31, 2023)
  
  The release starts from **Net income attributable to Uber Technologies, Inc.** rather than consolidated net income. The table has no separate line for net unrealized gains on equity investments. Those gains sit inside "Other (income) expense, net."
  
  | Line item | FY2023 ($ millions) |
  |---|---|
  | Net income attributable to Uber Technologies, Inc. | 1,887 |
  | Net income attributable to non-controlling interests, net of tax | 269 |
  | Provision for income taxes | 213 |
  | Income from equity method investments | (48) |
  | Interest expense | 633 |
  | Other (income) expense, net | (1,844) |
  | Depreciation and amortization | 823 |
  | Stock-based compensation expense | 1,935 |
  | Legal, tax, and regulatory reserve changes and settlements | 9 |
  | Goodwill and asset impairments/loss on sale of assets, net | 84 |
  | Acquisition, financing and divestitures related expenses | 36 |
  | Accelerated lease costs related to cease-use of ROU assets | — |
  | COVID-19 response initiatives | — |
  | Loss on lease arrangement, net | 4 |
  | Restructuring and related charges | 51 |
  | Mass arbitration fees, net | — |
  | **Adjusted EBITDA** | **4,052** |
  
  The line items sum to the reported $4,052 million.
  
  **Largest adjustment in absolute value: Stock-based compensation expense, $1,935 million.** The next largest is Other (income) expense, net, at $(1,844) million, which is the line that contains the net unrealized gains on equity investments ($1.6 billion net benefit for the year, per the release).

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: Stock-based compensation expense, about $1.94 billion ($1,935 million), was Uber's largest adjustment to Adjusted EBITDA for FY2023.**\n\n**Method:** I pulled Uber's Q4 and full-year 2023 earnings release (furnished on Form 8-K, February 7, 2024), which contains the full-year Adjusted EBITDA reconciliation. The release reports full-year 2023 Adjusted EBITDA of $4,052 million, with <cite index=\"5-3\">net income attributable to Uber Technologies, Inc. of $1,887 million</cite> for the year.\n\n**FY2023 reconciliation (in $ millions), as I read it from the release:**\n\n| Line item | FY2023 |\n|---|---|\n| Net income attributable to Uber Technologies, Inc. | 1,887 |\
…[truncated 2,100 chars])

### Final answer
**Answer: Stock-based compensation expense, about $1.94 billion ($1,935 million), was Uber's largest adjustment to Adjusted EBITDA for FY2023.**

**Method:** I pulled Uber's Q4 and full-year 2023 earnings release (furnished on Form 8-K, February 7, 2024), which contains the full-year Adjusted EBITDA reconciliation. The release reports full-year 2023 Adjusted EBITDA of $4,052 million, with <cite index="5-3">net income attributable to Uber Technologies, Inc. of $1,887 million</cite> for the year.

**FY2023 reconciliation (in $ millions), as I read it from the release:**

| Line item | FY2023 |
|---|---|
| Net income attributable to Uber Technologies, Inc. | 1,887 |
| Net income attributable to non-controlling interests, net of tax | 269 |
| Provision for income taxes | 213 |
| Income from equity method investments | (48) |
| Interest expense | 633 |
| Other (income) expense, net | (1,844) |
| Depreciation and amortization | 823 |
| Stock-based compensation expense | 1,935 |
| Legal, tax, and regulatory reserve changes and settlements | 9 |
| Goodwill and asset impairments/loss on sale of assets, net | 84 |
| Acquisition, financing and divestitures related expenses | 36 |
| Loss on lease arrangement, net | 4 |
| Restructuring and related charges | 51 |
| Other items (accelerated lease costs, COVID-19 response, mass arbitration fees) | — |
| **Adjusted EBITDA** | **4,052** |

The line items sum to the reported $4,052 million, which checks the table.

**Largest adjustment:** The largest add-back by absolute value is stock-based compensation expense of $1,935 million, or about **$1.94 billion**. The next largest item is Other (income) expense, net, at $(1,844) million, which is a deduction rather than an add-back. It mainly reflects net unrealized gains on equity investments, which the release describes as a <cite index="6-5">net tailwind (pre-tax) primarily due to net unrealized gains related to the revaluation of Uber's equity investments.</cite>

**Caveat:** I took these figures from the earnings release rather than the 10-K's non-GAAP section. The release's full-year numbers are the ones I used, and I did not separately verify them against the 10-K.

**Sources:**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm",
            "name": "Uber Announces Results for Fourth Quarter and Full Year 2023 (8-K Exhibit 99.1, February 7, 2024)"
        },
        {
            "url": "https://www.nasdaq.com/press-release/uber-announces-results-for-fourth-quarter-and-full-year-2023-2024-02-07",
            "name": "Nasdaq copy of Uber Q4 and FY2023 results press release"
        }
    ]
}