## Rollout `dom1`
- outcome: submitted
- turns: 3; cost: $0.005; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm", "key": "uber_q4_2023"})
  result: SUCCESS: The result has been saved to the data storage under the key: uber_q4_2023. (49,646 characters)
  The data_storage currently contains the following keys:
  uber_q4_2023
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Uber Q4 2023 earnings release, find the Adjusted EBITDA reconciliation table for the full year ended December 31, 2023 (in $ millions). List every line item with its exact label and value and sign, starting from net income (loss) attributable to Uber, and state the reported total Adjusted EBITDA for the full year. Also list the full-year figures for stock-based compensation expense, other (income) expense net, D&A, interest expense, and any other items. Document: {{uber_q4_2023}}"})
  result: **Adjusted EBITDA Reconciliation, Year Ended December 31, 2023 (in $ millions)**
  
  Source: Uber Q4 2023 earnings release (EX-99.1), "Reconciliations of Non-GAAP Measures."
  
  | Line item | FY2023 | Sign / direction |
  |---|---|---|
  | Net income (loss) attributable to Uber Technologies, Inc. | $1,887 | Starting point (positive) |
  | *Add (deduct):* | | |
  | Net income attributable to non-controlling interests, net of tax | 269 | Add (positive) |
  | Provision for (benefit from) income taxes | 213 | Add (positive) |
  | Income from equity method investments | (48) | Deduct (negative) |
  | Interest expense | 633 | Add (positive) |
  | Other (income) expense, net | (1,844) | Deduct (negative); net other income of $1,844 is removed |
  | Depreciation and amortization | 823 | Add (positive) |
  | Stock-based compensation expense | 1,935 | Add (positive) |
  | Legal, tax, and regulatory reserve changes and settlements | 9 | Add (positive) |
  | Goodwill and asset impairments/loss on sale of assets, net | 84 | Add (positive) |
  | Acquisition, financing and divestitures related expenses | 36 | Add (positive) |
  | Accelerated lease costs related to cease-use of ROU assets | — | Nil |
  | COVID-19 response initiatives | — | Nil |
  | Loss on lease arrangement, net | 4 | Add (positive) |
  | Restructuring and related charges | 51 | Add (positive) |
  | Mass arbitration fees, net | — | Nil |
  | **Adjusted EBITDA** | **$4,052** | |
  
  I checked the arithmetic: the items sum to $4,052 million.
  
  **Reported full-year 2023 Adjusted EBITDA: $4,052 million**, up 137% from $1,713 million in 2022.
  
  **Key figures requested:**
  - **Stock-based compensation expense:** $1,935 million (added back)
  - **Other (income) expense, net:** $(1,844) million (deducted; this was net other income. It consists mainly of interest income of $484
  …[truncated 843 chars]

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "Answer: Uber's largest adjustment to Adjusted EBITDA for FY2023 (year ended December 31, 2023) was Stock-based compensation expense, an add-back of $1,935 million, or $1.935 billion (about $1.94 billion when rounded to two decimals).\n\nHow I verified it: I opened Uber's Q4 2023 earnings release (EX-99.1, dated 2024-02-07) and pulled the full-year \"Reconciliations of Non-GAAP Measures\" table, which is in $ millions. The reconciliation runs as follows:\n\n- Net income attributable to Uber Technologies, Inc.: 1,887\n- Net income attributable to non-controlling interests, net of tax: 269\n- Provision for income taxes: 213\n- Income from equity method investments: (48)\n- Int
…[truncated 1,290 chars])

### Final answer
Answer: Uber's largest adjustment to Adjusted EBITDA for FY2023 (year ended December 31, 2023) was Stock-based compensation expense, an add-back of $1,935 million, or $1.935 billion (about $1.94 billion when rounded to two decimals).

How I verified it: I opened Uber's Q4 2023 earnings release (EX-99.1, dated 2024-02-07) and pulled the full-year "Reconciliations of Non-GAAP Measures" table, which is in $ millions. The reconciliation runs as follows:

- Net income attributable to Uber Technologies, Inc.: 1,887
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
- Accelerated lease costs, COVID-19 response initiatives, and mass arbitration fees: nil

Check: the items sum to 4,052, which matches the reported full-year Adjusted EBITDA of $4,052 million.

Ranking: Stock-based compensation (+1,935) is the largest add-back and also the largest adjustment by absolute size. Other (income) expense, net (1,844) is close in size but is a deduction, since it removes net other income from the starting point. Those two are the only items above $1 billion. Depreciation and amortization (823) and interest expense (633) are smaller.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm",
            "name": "Uber Technologies Q4 2023 earnings press release (Form 8-K EX-99.1, dated 2024-02-07)"
        }
    ]
}