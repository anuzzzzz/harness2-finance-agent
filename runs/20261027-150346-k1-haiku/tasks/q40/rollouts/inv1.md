## Rollout `inv1`
- outcome: submitted
- turns: 3; cost: $0.097; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb_10k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_10k_2024. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb_10k_2024
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K text, find the Adjusted EBITDA reconciliation table in the MD&A non-GAAP section. List every line item between Net income and Adjusted EBITDA, exactly as labeled, with FY2024 and FY2023 amounts in $ millions. Also quote the company's stated definition of Adjusted EBITDA and its explanation for excluding these items. Text: {{abnb_10k_2024}}"})
  result: **Adjusted EBITDA Reconciliation (MD&A, Key Business Metrics and Non-GAAP Financial Measures)**
  
  The filing lists 2023 before 2024. Amounts are in $ millions, and parentheses denote negative values.
  
  | Line item (as labeled) | FY2023 | FY2024 |
  |---|---|---|
  | Net income | $4,792 | $2,648 |
  | *Adjusted to exclude the following:* | | |
  | Provision for (benefit from) income taxes | (2,690) | 683 |
  | Other expense, net | 137 | 40 |
  | Interest income | (721) | (818) |
  | Depreciation and amortization | 44 | 65 |
  | Stock-based compensation expense | 1,120 | 1,407 |
  | Acquisition-related impacts | (3) | (7) |
  | Lodging taxes, host withholding taxes, and transactional taxes, net | 974 | 23 |
  | **Adjusted EBITDA** | **$3,653** | **$4,041** |
  
  I checked the arithmetic, and both columns sum correctly to Adjusted EBITDA. The reconciliation table's "Other expense, net" label differs from the income statement's "Other income (expense), net."
  
  **Stated definition**
  
  The filing defines the measure as: "Adjusted EBITDA: Net income adjusted for: provision for (benefit from) income taxes; other income (expense), net; interest income; depreciation and amortization; stock-based compensation expense; acquisition-related impacts consisting of gains (losses) recognized on changes in the fair value of contingent consideration arrangements, and lodging taxes for which we may have joint and several liability with hosts for collecting and remitting such taxes, withholding taxes on payments made to hosts and any related settlements, and transactional taxes where there is significant uncertainty as to how the taxes apply to our platform."
  
  **Stated explanation for excluding these items**
  
  "The above items are excluded from our Adjusted EBITDA measure because they are non-cash in nature, or because t
  …[truncated 173 chars]

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "Airbnb starts its Adjusted EBITDA reconciliation at net income and makes eight adjustment lines before arriving at Adjusted EBITDA. I checked the figures against the FY2024 Form 10-K (MD&A, Key Business Metrics and Non-GAAP Financial Measures). Amounts are in $ millions, with FY2024 and FY2023 shown as the 10-K presents them.\n\nReconciliation (line items as labeled in the 10-K):\n\n| Line item | FY2023 | FY2024 |\n|---|---|---|\n| Net income | 4,792 | 2,648 |\n| Provision for (benefit from) income taxes | (2,690) | 683 |\n| Other expense, net | 137 | 40 |\n| Interest income | (721) | (818) |\n| Depreciation and amortization | 44 | 65 |\n| Stock-based compensation expense |
…[truncated 1,764 chars])

### Final answer
Airbnb starts its Adjusted EBITDA reconciliation at net income and makes eight adjustment lines before arriving at Adjusted EBITDA. I checked the figures against the FY2024 Form 10-K (MD&A, Key Business Metrics and Non-GAAP Financial Measures). Amounts are in $ millions, with FY2024 and FY2023 shown as the 10-K presents them.

Reconciliation (line items as labeled in the 10-K):

| Line item | FY2023 | FY2024 |
|---|---|---|
| Net income | 4,792 | 2,648 |
| Provision for (benefit from) income taxes | (2,690) | 683 |
| Other expense, net | 137 | 40 |
| Interest income | (721) | (818) |
| Depreciation and amortization | 44 | 65 |
| Stock-based compensation expense | 1,120 | 1,407 |
| Acquisition-related impacts | (3) | (7) |
| Lodging taxes, host withholding taxes, and transactional taxes, net | 974 | 23 |
| Adjusted EBITDA | 3,653 | 4,041 |

Arithmetic check: FY2024 2,648 + 683 + 40 − 818 + 65 + 1,407 − 7 + 23 = 4,041. FY2023 4,792 − 2,690 + 137 − 721 + 44 + 1,120 − 3 + 974 = 3,653. Both columns foot.

Adjustments, in plain terms:
1. Income tax provision or benefit is added back or removed.
2. Other income/expense, net is removed. The reconciliation labels this "Other expense, net," while the income statement uses "Other income (expense), net."
3. Interest income is subtracted, since it is non-operating income.
4. Depreciation and amortization is added back.
5. Stock-based compensation expense is added back.
6. Acquisition-related impacts are removed. Per the 10-K definition, these are gains or losses from changes in the fair value of contingent consideration arrangements, plus certain lodging, withholding and transactional tax exposures tied to the platform.
7. Lodging taxes, host withholding taxes and transactional taxes, net are added back. The 10-K ties this to taxes where Airbnb may have joint and several liability with hosts, or where the tax treatment on its platform is significantly uncertain.

Stated rationale: the company says these items are excluded because they are non-cash in nature, or because their amount and timing are unpredictable and not driven by core results of operations, which it says makes comparisons with prior periods and competitors less meaningful.

Note: The 10-K reconciliation shows only annual figures. The quarterly 8-K earnings releases carry the same line items by quarter, but I did not open those documents, so I have not relied on them.