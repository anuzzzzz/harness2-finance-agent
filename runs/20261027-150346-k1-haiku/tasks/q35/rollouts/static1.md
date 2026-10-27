## Rollout `static1`
- outcome: submitted
- turns: 5; cost: $0.149; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Uber Adjusted EBITDA reconciliation 2023 annual report", "ciks": ["UBER"], "start_date": "2024-01-01", "end_date": "2024-12-31"})
  result: {"total_matching_documents": 11, "page": 1, "results": [{"form": "8-K", "file_date": "2024-05-08", "period_ending": "2024-05-08", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000017", "document": "uberq124earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000017/uberq124earningspressrelea.htm"}, {"form": "8-K", "file_date": "2024-08-06", "period_ending": "2024-08-06", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000024", "document": "uberq224earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000024/uberq224earningspressrelea.htm"}, {"form": "8-K", "file_date": "2024-02-07", "period_ending": "2024-02-07", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000008", "document": "uberq423earningspressrelea.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm"}, {"form": "8-K", "file_date": "2024-02-14", "period_ending": "2024-02-06", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001552781-24-000039", "document": "e24041_ex99-2.htm", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1543151/000155278124000039/e24041_ex99-2.htm"}, {"form": "8-K", "file_date": "2024-10-31", "period_ending": "2024-10-31", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-24-000033", "document": "uberq324earningspressrelea.htm", "description": 
  …[truncated 2,248 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm", "key": "q4_2023"})
  result: SUCCESS: The result has been saved to the data storage under the key: q4_2023. (49,646 characters)
  The data_storage currently contains the following keys:
  q4_2023
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000012/uber-20231231.htm", "key": "10k_2023"})
  result: SUCCESS: The result has been saved to the data storage under the key: 10k_2023. (691,795 characters)
  The data_storage currently contains the following keys:
  q4_2023
  10k_2023
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this document, find the Adjusted EBITDA reconciliation table for the full year ended December 31, 2023 (year ended 2023). List every reconciling line item from Net income (loss) down to Adjusted EBITDA with its exact dollar amount in millions for the year 2023. Identify the largest adjustment by absolute value. {{q4_2023}}"})
  result: ## FY2023 Adjusted EBITDA Reconciliation (Year Ended December 31, 2023)
  
  The reconciliation starts with net income attributable to Uber Technologies, Inc. (the table's first line, not net income including non-controlling interests).
  
  | Reconciling Line Item | FY2023 ($ millions) |
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
  
  The line items sum to the reported total: 1,887 + 269 + 213 − 48 + 633 − 1,844 + 823 + 1,935 + 9 + 84 + 36 + 0 + 0 + 4 + 51 + 0 = 4,052.
  
  **Largest adjustment by absolute value:** Stock-based compensation expense, at $1,935 million. The next largest is Other (income) expense, net, at $(1,844) million.
- retrieve_information({"prompt": "From this 10-K, find the Adjusted EBITDA reconciliation table for the year ended December 31, 2023. List every reconciling line item from Net income (loss) to Adjusted EBITDA with exact amounts in millions for 2023. {{10k_2023}}"})
  result: The 2023 Adjusted EBITDA reconciliation in the 10-K (Item 7, "Reconciliations of Non-GAAP Financial Measures") starts from net income attributable to Uber Technologies, Inc., not from net income including non-controlling interests.
  
  | (In millions) | Year Ended December 31, 2023 |
  |---|---|
  | Net income (loss) attributable to Uber Technologies, Inc. | $1,887 |
  | **Add (deduct):** | |
  | Net income attributable to non-controlling interests, net of tax | 269 |
  | Provision for (benefit from) income taxes | 213 |
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
  
  The reconciling items sum to the reported $4,052 million. Several line items have no 2023 amount (shown as "—"): accelerated lease costs, COVID-19 response initiatives, and mass arbitration fees.

### Turn 4  (stop_reason=end_turn)
**Answer: Stock-based compensation expense, $1.94 billion ($1,935 million), was Uber's largest adjustment to Adjusted EBITDA for FY2023.**

**Method**

I pulled the Adjusted EBITDA reconciliation for the year ended December 31, 2023 from Uber's FY2023 10-K and checked it against the Q4 2023 earnings release (filed February 7, 2024). Both show the same figures in millions of dollars:

| Reconciling line item | FY2023 ($M) |
|---|---|
| Net income attributable to Uber | 1,887 |
| Net income attributable to non-controlling interests, net of tax | 269 |
| Provision for income taxes | 213 |
| Income from equity method investments | (48) |
| Interest expense | 633 |
| Other (income) expense, net | (1,844) |
| Depreciation and amortization | 823 |
| **Stock-based compensation expense** | **1,935** |
| Legal, tax, and regulatory reserve changes and settlements | 9 |
| Goodwill and asset impairments/loss on sale of assets, net | 84 |
| Acquisition, financing and divestitures related expenses | 36 |
| Loss on lease arrangement, net | 4 |
| Restructuring and related charges | 51 |
| Accelerated lease costs, COVID-19 response initiatives, mass arbitration fees | 0 (—) |
| **Adjusted EBITDA** | **4,052** |

**Check:** 1,887 + 269 + 213 − 48 + 633 − 1,844 + 823 + 1,935 + 9 + 84 + 36 + 4 + 51 = 4,052, which matches the reported total.

**Largest adjustment:** Ranked by absolute value, stock-based compensation of $1,935M is the largest. The next largest is Other (income) expense, net at $(1,
…[truncated 599 chars]

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "Answer: Stock-based compensation expense, $1.94 billion ($1,935 million), was Uber's largest adjustment to Adjusted EBITDA for the fiscal year ended December 31, 2023.\n\nMethod: I pulled the Adjusted EBITDA reconciliation for the year ended December 31, 2023 from Uber's FY2023 10-K and checked it against the Q4 2023 earnings release (filed February 7, 2024). Both show the same figures in millions of dollars:\n\n- Net income attributable to Uber: 1,887\n- Net income attributable to non-controlling interests, net of tax: 269\n- Provision for income taxes: 213\n- Income from equity method investments: (48)\n- Interest expense: 633\n- Other (income) expense, net: (1,844)\n- De
…[truncated 1,346 chars])

### Final answer
Answer: Stock-based compensation expense, $1.94 billion ($1,935 million), was Uber's largest adjustment to Adjusted EBITDA for the fiscal year ended December 31, 2023.

Method: I pulled the Adjusted EBITDA reconciliation for the year ended December 31, 2023 from Uber's FY2023 10-K and checked it against the Q4 2023 earnings release (filed February 7, 2024). Both show the same figures in millions of dollars:

- Net income attributable to Uber: 1,887
- Net income attributable to non-controlling interests, net of tax: 269
- Provision for income taxes: 213
- Income from equity method investments: (48)
- Interest expense: 633
- Other (income) expense, net: (1,844)
- Depreciation and amortization: 823
- Stock-based compensation expense: 1,935
- Legal, tax, and regulatory reserve changes and settlements: 9
- Goodwill and asset impairments/loss on sale of assets, net: 84
- Acquisition, financing and divestitures related expenses: 36
- Loss on lease arrangement, net: 4
- Restructuring and related charges: 51
- Accelerated lease costs, COVID-19 response initiatives, mass arbitration fees: 0
- Adjusted EBITDA: 4,052

Check: 1,887 + 269 + 213 - 48 + 633 - 1,844 + 823 + 1,935 + 9 + 84 + 36 + 4 + 51 = 4,052, which matches the reported total.

Largest adjustment: Ranked by absolute value, stock-based compensation of $1,935M is the largest. The next largest is Other (income) expense, net at $(1,844)M, which is a deduction. Rounded to two decimals, $1,935M is $1.94B.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000012/uber-20231231.htm",
            "name": "Uber Technologies, Inc. Form 10-K for fiscal year ended December 31, 2023"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm",
            "name": "Uber Technologies, Inc. Q4 2023 earnings press release (Form 8-K Ex. 99.1)"
        }
    ]
}