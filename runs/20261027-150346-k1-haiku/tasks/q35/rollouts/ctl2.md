## Rollout `ctl2`
- outcome: submitted
- turns: 5; cost: $0.017; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Uber 2023 annual results adjusted EBITDA reconciliation") → 0 results: 
- edgar_search({"search_query": "Uber Adjusted EBITDA reconciliation 2023 stock-based compensation depreciation amortization", "ciks": ["UBER"], "start_date": "2024-01-01", "end_date": "2024-12-31"})
  result: {"total_matching_documents": 11, "page": 1, "results": [{"form": "8-K", "file_date": "2024-05-08", "period_ending": "2024-05-08", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000017", "document": "uberq124earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000017/uberq124earningspressrelea.htm"}, {"form": "8-K", "file_date": "2024-08-06", "period_ending": "2024-08-06", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000024", "document": "uberq224earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000024/uberq224earningspressrelea.htm"}, {"form": "8-K", "file_date": "2024-02-07", "period_ending": "2024-02-07", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000008", "document": "uberq423earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm"}, {"form": "8-K", "file_date": "2024-10-31", "period_ending": "2024-10-31", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000033", "document": "uberq324earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000033/uberq324earningspressrelea.htm"}, {"form": "8-K", "file_date": "2024-02-14", "period_ending": "2024-02-06", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001552781-24-000039", "document": "e24041_ex99-2.htm
  …[truncated 2,248 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Uber Technologies, Inc - Form 10-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1543151/000154315124000012/uber-20231231.htm>; Uber Technologies, Inc - Form 10-Q - FY2023 <https://www.sec.gov/Archives/edgar/data/1543151/000154315123000039/uber-20230930.htm>; Uber Technologies, Inc - Form 8-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1543151/000154315123000021/uberq223earningspressrelea.htm>; Uber Technologies, Inc - Form 10-Q - FY2023 <https://www.sec.gov/Archives/edgar/data/1543151/000154315123000025/uber-20230630.htm>; Uber Technologies, Inc - Form 8-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1543151/000154315123000036/uberq323earningspressrelea.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm", "key": "q4_2023_pr"})
  result: SUCCESS: The result has been saved to the data storage under the key: q4_2023_pr. (49,646 characters)
  The data_storage currently contains the following keys:
  q4_2023_pr
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Uber Q4 2023 press release, extract the full Adjusted EBITDA reconciliation table for the Year Ended December 31, 2023 column (in millions), listing every line item and its amount. Then identify the largest adjustment (add-back) by absolute amount. {{q4_2023_pr}}"})
  result: ## Adjusted EBITDA Reconciliation, Year Ended December 31, 2023 (in millions)
  
  | Line item | Amount |
  |---|---|
  | Net income attributable to Uber Technologies, Inc. | $1,887 |
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
  | **Adjusted EBITDA** | **$4,052** |
  
  The line items sum to $4,052 million, which matches the reported figure.
  
  ## Largest adjustment
  
  The largest adjustment by absolute amount is **stock-based compensation expense of $1,935 million**. The next largest is the Other (income) expense, net deduction of $1,844 million. The starting line, net income attributable to Uber, is not an adjustment and is excluded from this comparison.

### Turn 4  (stop_reason=end_turn)
**Answer: Stock-based compensation expense, at $1.935 billion (about $1.94 billion), was Uber's largest adjustment to Adjusted EBITDA for fiscal 2023.**

**How I got there**

1. Uber's FY2023 reconciliation starts from net income attributable to Uber of $1,887 million and adds back or deducts the items needed to reach Adjusted EBITDA. The search results confirmed the starting figure and the $4,052 million total in the Q4 2023 earnings release. 
Net income (loss) attributable to Uber Technologies, Inc. · $ · 595 · $ · 1,429 · $ · (9,141) · $ · 1,887

2. I pulled the full year-ended December 31, 2023 table from the Q4 2023 press release. The line items were:
   - Net income attributable to non-controlling interests, net of tax: $269M
   - Provision for income taxes: $213M
   - Income from equity method investments: $(48)M
   - Interest expense: $633M
   - Other (income) expense, net: $(1,844)M
   - Depreciation and amortization: $823M
   - Stock-based compensation expense: $1,935M
   - Legal, tax, and regulatory reserve changes and settlements: $9M
   - Goodwill and asset impairments/loss on sale of assets, net: $84M
   - Acquisition, financing and divestitures related expenses: $36M
   - Loss on lease arrangement, net: $4M
   - Restructuring and related charges: $51M
3. Check: $1,887 + 269 + 213 − 48 + 633 − 1,844 + 823 + 1,935 + 9 + 84 + 36 + 4 + 51 = $4,052M, which matches reported Adjusted EBITDA.
4. Comparing magnitudes, stock-based compensation ($1,935M) is the largest. T
…[truncated 869 chars]

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: Stock-based compensation expense, at $1.935 billion (about $1.94 billion), was Uber's largest adjustment to Adjusted EBITDA for the fiscal year ended December 31, 2023.**\n\n**How I got there**\n\n1. I started from Uber's FY2023 Adjusted EBITDA reconciliation. Its starting point is net income attributable to Uber of $1,887 million, and the press release reports Adjusted EBITDA of $4,052 million for the year. The Q4 2023 release shows the annual reconciliation column (in millions) with net income of $1,887 for the year.\n\n2. The full-year line items, from the Q4 2023 press release, were:\n   - Net income attributable to non-controlling interests, net of tax: $269M
…[truncated 1,754 chars])

### Final answer
**Answer: Stock-based compensation expense, at $1.935 billion (about $1.94 billion), was Uber's largest adjustment to Adjusted EBITDA for the fiscal year ended December 31, 2023.**

**How I got there**

1. I started from Uber's FY2023 Adjusted EBITDA reconciliation. Its starting point is net income attributable to Uber of $1,887 million, and the press release reports Adjusted EBITDA of $4,052 million for the year. The Q4 2023 release shows the annual reconciliation column (in millions) with net income of $1,887 for the year.

2. The full-year line items, from the Q4 2023 press release, were:
   - Net income attributable to non-controlling interests, net of tax: $269M
   - Provision for income taxes: $213M
   - Income from equity method investments: $(48)M
   - Interest expense: $633M
   - Other (income) expense, net: $(1,844)M
   - Depreciation and amortization: $823M
   - Stock-based compensation expense: $1,935M
   - Legal, tax, and regulatory reserve changes and settlements: $9M
   - Goodwill and asset impairments/loss on sale of assets, net: $84M
   - Acquisition, financing and divestitures related expenses: $36M
   - Loss on lease arrangement, net: $4M
   - Restructuring and related charges: $51M

3. Check: $1,887 + 269 + 213 − 48 + 633 − 1,844 + 823 + 1,935 + 9 + 84 + 36 + 4 + 51 = $4,052M, which matches reported Adjusted EBITDA.

4. Ranking by absolute size, stock-based compensation ($1,935M) is the largest adjustment. The next largest is Other (income) expense, net at $(1,844)M, which is a deduction that removes a non-operating gain rather than an add-back. Depreciation and amortization ($823M) and interest expense ($633M) are well below both.

**Caveat:** The line-item values were extracted from the press release text. I did not check each figure against the 10-K's own reconciliation table, though the 10-K covers the same period and should match.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm",
            "name": "Uber Q4 2023 earnings press release (Form 8-K Exhibit 99.1, February 7, 2024)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000012/uber-20231231.htm",
            "name": "Uber Technologies, Inc. Form 10-K for fiscal year ended December 31, 2023"
        }
    ]
}