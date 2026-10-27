## Rollout `inv1`
- outcome: submitted
- turns: 2; cost: $0.004; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm", "key": "uber_q4_2023"})
  result: SUCCESS: The result has been saved to the data storage under the key: uber_q4_2023. (49,646 characters)
  The data_storage currently contains the following keys:
  uber_q4_2023
  
- retrieve_information({"prompt": "From {{uber_q4_2023}}, find the full-year 2023 Adjusted EBITDA reconciliation table (in millions). List every line item from net income (loss) attributable to Uber through Adjusted EBITDA with its full-year 2023 amount, and confirm the total Adjusted EBITDA figure."})
  result: The FY2023 Adjusted EBITDA reconciliation (in millions, year ended December 31, 2023):
  
  | Line item | FY2023 |
  |---|---|
  | Net income attributable to Uber Technologies, Inc. | $1,887 |
  | Add (deduct): | |
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
  
  I confirmed the total: the line items sum to $4,052 million, which matches the reported full-year 2023 Adjusted EBITDA of $4,052 million (up 137% from $1,713 million in 2022).

### Turn 2  (stop_reason=tool_use)
- submit_final_result({"final_result": "Answer: Uber's largest adjustment to EBITDA for fiscal year 2023 (year ended December 31, 2023) was Stock-based compensation expense, an add-back of $1.935 billion (1,935 in millions, about $1.94 billion when rounded to two decimals).\n\nHow I verified it: I opened Uber's Q4/FY2023 earnings release (Form 8-K, Exhibit 99.1) and pulled the full-year 2023 Adjusted EBITDA reconciliation, which is presented in millions of dollars:\n\n- Net income attributable to Uber Technologies, Inc.: 1,887\n- Net income attributable to non-controlling interests, net of tax: 269\n- Provision for income taxes: 213\n- Income from equity method investments: (48)\n- Interest expense: 633\n- Other 
…[truncated 1,147 chars])

### Final answer
Answer: Uber's largest adjustment to EBITDA for fiscal year 2023 (year ended December 31, 2023) was Stock-based compensation expense, an add-back of $1.935 billion (1,935 in millions, about $1.94 billion when rounded to two decimals).

How I verified it: I opened Uber's Q4/FY2023 earnings release (Form 8-K, Exhibit 99.1) and pulled the full-year 2023 Adjusted EBITDA reconciliation, which is presented in millions of dollars:

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
- Adjusted EBITDA: 4,052

Check: the items sum to 4,052 (1,887 + 269 + 213 − 48 + 633 − 1,844 + 823 + 1,935 + 9 + 84 + 36 + 4 + 51 = 4,052), which matches the reported total.

Ranking by absolute value: the largest item is stock-based compensation at 1,935 (an add-back, increasing Adjusted EBITDA). The runner-up is Other (income) expense, net at (1,844), which is a deduction that reduces Adjusted EBITDA. The two are close in size, but SBC is the larger.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315124000008/uberq423earningspressrelea.htm",
            "name": "Uber Technologies Q4 and FY2023 Earnings Press Release (Form 8-K Exhibit 99.1)"
        }
    ]
}