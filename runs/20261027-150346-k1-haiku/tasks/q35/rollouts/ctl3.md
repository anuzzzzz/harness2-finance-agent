## Rollout `ctl3`
- outcome: submitted
- turns: 4; cost: $0.019; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Uber 2023 full year Adjusted EBITDA reconciliation net income benefit from income taxes equity-based compensation") → 0 results: 
- edgar_search({"search_query": "Uber Technologies annual report 2023 Adjusted EBITDA reconciliation", "ciks": ["UBER"], "start_date": "2024-01-01", "end_date": "2024-12-31"})
  result: {"total_matching_documents": 11, "page": 1, "results": [{"form": "8-K", "file_date": "2024-05-08", "period_ending": "2024-05-08", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000017", "document": "uberq124earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000017/uberq124earningspressrelea.htm"}, {"form": "8-K", "file_date": "2024-08-06", "period_ending": "2024-08-06", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000024", "document": "uberq224earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000024/uberq224earningspressrelea.htm"}, {"form": "8-K", "file_date": "2024-02-07", "period_ending": "2024-02-07", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000008", "document": "uberq423earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm"}, {"form": "8-K", "file_date": "2024-10-31", "period_ending": "2024-10-31", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000033", "document": "uberq324earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000033/uberq324earningspressrelea.htm"}, {"form": "8-K", "file_date": "2024-02-14", "period_ending": "2024-02-06", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001552781-24-000039", "document": "e24041_ex99-2.htm
  …[truncated 2,248 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 9 results: Uber Technologies, Inc - Form 8-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1543151/000154315123000036/uberq323earningspressrelea.htm>; Uber Technologies, Inc - Form 8-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1543151/000154315123000013/uberq123earningspressrelea.htm>; Uber Technologies, Inc - Form 8-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1543151/000154315123000021/uberq223earningspressrelea.htm>; Uber Technologies, Inc - Form 10-Q - FY2023 <https://www.sec.gov/Archives/edgar/data/1543151/000154315123000039/uber-20230930.htm>; Uber Technologies, Inc - Form 10-Q - FY2023 <https://www.sec.gov/Archives/edgar/data/1543151/000154315123000025/uber-20230630.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315125000004/uberq424earningspressrelea.htm", "key": "q4_2024_pr"})
  result: SUCCESS: The result has been saved to the data storage under the key: q4_2024_pr. (45,464 characters)
  The data_storage currently contains the following keys:
  q4_2024_pr
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm", "key": "q4_2023_pr"})
  result: SUCCESS: The result has been saved to the data storage under the key: q4_2023_pr. (49,646 characters)
  The data_storage currently contains the following keys:
  q4_2024_pr
  q4_2023_pr
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this document, find the full-year 2023 (Year Ended December 31, 2023) Adjusted EBITDA reconciliation table. List every line item with its amount in millions for year ended December 31, 2023, and identify the item with the largest absolute adjustment. Document: {{q4_2023_pr}}"})
  result: ## FY2023 Adjusted EBITDA Reconciliation (Year Ended December 31, 2023)
  
  | Line item | Amount ($M) |
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
  
  The items sum to $4,052M, which matches the reported figure.
  
  **Largest absolute adjustment:** Stock-based compensation expense, at $1,935M. The next largest is Other (income) expense, net, at $(1,844)M, which is a deduction, so its absolute value is $1,844M.
- retrieve_information({"prompt": "From this document, find the full-year 2023 (Year Ended December 31, 2023) Adjusted EBITDA reconciliation table. List every line item with its amount in millions for year ended December 31, 2023. Document: {{q4_2024_pr}}"})
  result: The Adjusted EBITDA reconciliation for the year ended December 31, 2023 is below, in millions. The document's headline covers 2024, but this table includes a 2023 column.
  
  | Line item | Year Ended Dec 31, 2023 |
  |---|---|
  | Net income attributable to Uber Technologies, Inc. | $1,887 |
  | **Add (deduct):** | |
  | Net income attributable to non-controlling interests, net of tax | 269 |
  | (Income) from equity method investments | (48) |
  | Provision for income taxes | 213 |
  | Other (income) expense, net | (1,844) |
  | Interest expense | 633 |
  | **Income from operations** | **1,110** |
  | **Add (deduct):** | |
  | Depreciation and amortization | 823 |
  | Stock-based compensation expense | 1,935 |
  | Legal, tax, and regulatory reserve changes and settlements | 9 |
  | Goodwill and asset impairments/loss on sale of assets | 84 |
  | Acquisition, financing and divestitures related expenses | 36 |
  | Loss on lease arrangements, net | 4 |
  | Restructuring and related charges, net | 51 |
  | **Adjusted EBITDA** | **$4,052** |

### Turn 4  (stop_reason=tool_use)
**Answer: Stock-based compensation expense, at about $1.94 billion ($1,935 million), was Uber's largest adjustment to EBITDA for FY2023.**

**Method:** I pulled Uber's Adjusted EBITDA reconciliation for the year ended December 31, 2023 from its Q4 2023 earnings release and checked the same figures against the 2023 column of its Q4 2024 release. Both show the same numbers. I then ranked the adjustments by absolute size.

**FY2023 reconciliation (in $ millions):**

| Line item | Amount |
|---|---|
| Net income attributable to Uber Technologies, Inc. (starting point) | 1,887 |
| Net income attributable to non-controlling interests, net of tax | 269 |
| Provision for income taxes | 213 |
| (Income) from equity method investments | (48) |
| Interest expense | 633 |
| Other (income) expense, net | (1,844) |
| Depreciation and amortization | 823 |
| **Stock-based compensation expense** | **1,935** |
| Legal, tax, and regulatory reserve changes and settlements | 9 |
| Goodwill and asset impairments/loss on sale of assets | 84 |
| Acquisition, financing and divestitures related expenses | 36 |
| Loss on lease arrangements, net | 4 |
| Restructuring and related charges | 51 |
| **Adjusted EBITDA** | **4,052** |

**Ranking:** Stock-based compensation ($1,935M) is the largest add-back. The largest deduction, Other (income) expense, net ($1,844M), is smaller in absolute terms. Depreciation and amortization ($823M) is the next largest add-back. The items sum to $4,052M, which matches repor
…[truncated 229 chars]
- submit_final_result({"final_result": "**Answer: Stock-based compensation expense, about $1.94 billion ($1,935 million), was Uber's largest adjustment to EBITDA for the fiscal year ended 12/31/2023.**\n\nMethod: I took Uber's Adjusted EBITDA reconciliation for the year ended December 31, 2023 from the Q4 2023 earnings release and cross-checked the 2023 column in the Q4 2024 earnings release. Both show the same figures. I then ranked the adjustments by absolute size.\n\nFY2023 reconciliation ($ millions):\n- Net income attributable to Uber Technologies, Inc. (starting point): 1,887\n- Net income attributable to non-controlling interests, net of tax: 269\n- Provision for income taxes: 213\n- (Income) from equity m
…[truncated 1,619 chars])

### Final answer
**Answer: Stock-based compensation expense, about $1.94 billion ($1,935 million), was Uber's largest adjustment to EBITDA for the fiscal year ended 12/31/2023.**

Method: I took Uber's Adjusted EBITDA reconciliation for the year ended December 31, 2023 from the Q4 2023 earnings release and cross-checked the 2023 column in the Q4 2024 earnings release. Both show the same figures. I then ranked the adjustments by absolute size.

FY2023 reconciliation ($ millions):
- Net income attributable to Uber Technologies, Inc. (starting point): 1,887
- Net income attributable to non-controlling interests, net of tax: 269
- Provision for income taxes: 213
- (Income) from equity method investments: (48)
- Interest expense: 633
- Other (income) expense, net: (1,844)
- Depreciation and amortization: 823
- Stock-based compensation expense: 1,935
- Legal, tax, and regulatory reserve changes and settlements: 9
- Goodwill and asset impairments/loss on sale of assets: 84
- Acquisition, financing and divestitures related expenses: 36
- Loss on lease arrangements, net: 4
- Restructuring and related charges: 51
- Adjusted EBITDA: 4,052

Ranking: Stock-based compensation ($1,935M) is the largest add-back. The largest deduction, Other (income) expense, net ($1,844M), is smaller in absolute terms. The items sum to $4,052M, matching reported Adjusted EBITDA.

Caveat: The figures come from the earnings releases, not the 10-K's own reconciliation table, which I did not open.

{
    "sources": [
        {
            "url": "https://s23.q4cdn.com/407969754/files/doc_earnings/2023/q4/earnings-result/Uber-Q4-23-Earnings-Press-Release.pdf",
            "name": "Uber Announces Results for Fourth Quarter and Full Year 2023 (Q4 2023 earnings press release)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm",
            "name": "Uber Q4 2023 earnings press release (Form 8-K, SEC EDGAR)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315125000004/uberq424earningspressrelea.htm",
            "name": "Uber Q4 2024 earnings press release (Form 8-K, SEC EDGAR), 2023 comparative column"
        }
    ]
}