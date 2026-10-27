## Rollout `agg1`
- outcome: submitted
- turns: 3; cost: $0.005; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm", "key": "uber_q4_2023"})
  result: SUCCESS: The result has been saved to the data storage under the key: uber_q4_2023. (49,646 characters)
  The data_storage currently contains the following keys:
  uber_q4_2023
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Uber Q4 2023 earnings release, find the full-year 2023 Adjusted EBITDA reconciliation table. List every line item with its exact value and sign (in $ millions), starting from net income (loss) attributable to Uber, and state the total Adjusted EBITDA. Also confirm the period and unit. Text: {{uber_q4_2023}}"})
  result: **Period and unit:** Year ended December 31, 2023 (January 1 to December 31, 2023), in US$ millions.
  
  **Full-year 2023 Adjusted EBITDA reconciliation** (signs as presented in the release, where parentheses are deductions):
  
  | Line item | FY2023 ($M) |
  |---|---|
  | Net income attributable to Uber Technologies, Inc. | 1,887 |
  | *Add (deduct):* | |
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
  
  **Check:** 1,887 + 269 + 213 − 48 + 633 − 1,844 + 823 + 1,935 + 9 + 84 + 36 + 4 + 51 = 4,052. This matches the release's full-year Adjusted EBITDA of $4,052 million, up 137% from $1,713 million in 2022.

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "Answer: Uber's largest adjustment to Adjusted EBITDA for the fiscal year ended December 31, 2023 was Stock-based compensation expense, an add-back of $1,935 million, or $1.935 billion (about $1.94 billion when rounded to two decimals).\n\nHow it was derived:\n- I opened Uber's Q4 2023 earnings release (8-K EX-99.1 dated February 7, 2024) and retrieved the full-year 2023 Adjusted EBITDA reconciliation, in US$ millions.\n- Starting from Net income attributable to Uber Technologies, Inc. of 1,887, the line items are: non-controlling interests net of tax +269; provision for income taxes +213; income from equity method investments (48); interest expense +633; other (income) expe
…[truncated 1,178 chars])

### Final answer
Answer: Uber's largest adjustment to Adjusted EBITDA for the fiscal year ended December 31, 2023 was Stock-based compensation expense, an add-back of $1,935 million, or $1.935 billion (about $1.94 billion when rounded to two decimals).

How it was derived:
- I opened Uber's Q4 2023 earnings release (8-K EX-99.1 dated February 7, 2024) and retrieved the full-year 2023 Adjusted EBITDA reconciliation, in US$ millions.
- Starting from Net income attributable to Uber Technologies, Inc. of 1,887, the line items are: non-controlling interests net of tax +269; provision for income taxes +213; income from equity method investments (48); interest expense +633; other (income) expense, net (1,844); depreciation and amortization +823; stock-based compensation expense +1,935; legal, tax and regulatory reserve changes and settlements +9; goodwill and asset impairments/loss on sale of assets, net +84; acquisition, financing and divestitures related expenses +36; loss on lease arrangement, net +4; restructuring and related charges +51. Accelerated lease costs, COVID-19 response initiatives and mass arbitration fees are zero for 2023.
- The lines sum to 4,052, which matches the reported full-year Adjusted EBITDA of $4,052 million.
- Ranking by absolute value: stock-based compensation (+1,935, add-back) is largest. The runner-up is Other (income) expense, net (1,844), which is a deduction rather than an add-back, so it does not qualify as the largest adjustment. The largest add-back and the largest absolute item are therefore the same line.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm",
            "name": "Uber Technologies Q4 2023 earnings press release (Form 8-K EX-99.1, February 7, 2024)"
        }
    ]
}