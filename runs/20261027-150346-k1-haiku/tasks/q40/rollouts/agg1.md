## Rollout `agg1`
- outcome: submitted
- turns: 3; cost: $0.099; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb10k. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb10k
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K text, find the Non-GAAP Financial Measures section with the Adjusted EBITDA reconciliation table. List every line from Net income to Adjusted EBITDA in the order shown, with labels exactly as printed, the amounts for 2024 and 2023 (in $ millions), and any footnote or stated reason for each adjustment. Also state the definition of Adjusted EBITDA as given. Text: {{abnb10k}}"})
  result: ## Adjusted EBITDA Reconciliation (Airbnb, Inc. FY2024 10-K)
  
  The table appears under Item 7, "Key Business Metrics and Non-GAAP Financial Measures – Adjusted EBITDA Reconciliation." Amounts are in $ millions. The table has no numbered footnotes, so the stated reason column reflects the general explanation the filing gives for the adjustments.
  
  | Line item (as printed) | 2023 | 2024 | Footnote / stated reason |
  |---|---|---|---|
  | Net income | $4,792 | $2,648 | Starting point (GAAP) |
  | *Adjusted to exclude the following:* | | | Section label, no amount |
  | Provision for (benefit from) income taxes | (2,690) | 683 | None printed; defined as an adjustment in the Adjusted EBITDA definition |
  | Other expense, net | 137 | 40 | None printed; defined as an adjustment in the Adjusted EBITDA definition |
  | Interest income | (721) | (818) | None printed; defined as an adjustment in the Adjusted EBITDA definition |
  | Depreciation and amortization | 44 | 65 | None printed; defined as an adjustment in the Adjusted EBITDA definition |
  | Stock-based compensation expense | 1,120 | 1,407 | None printed; defined as an adjustment in the Adjusted EBITDA definition |
  | Acquisition-related impacts | (3) | (7) | None printed; defined as gains (losses) recognized on changes in fair value of contingent consideration arrangements |
  | Lodging taxes, host withholding taxes, and transactional taxes, net | 974 | 23 | None printed; defined as lodging taxes (joint and several liability with hosts), withholding taxes on host payments and related settlements, and transactional taxes with significant uncertainty |
  | **Adjusted EBITDA** | **$3,653** | **$4,041** | Result |
  | Adjusted EBITDA Margin | 37% | 36% | Adjusted EBITDA divided by revenue |
  
  **General stated reason for the adjustments:** The filin
  …[truncated 1,212 chars]

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "Airbnb (NASDAQ: ABNB) starts its Adjusted EBITDA reconciliation at GAAP net income and then adds back or deducts the items below. Figures are from the FY2024 Form 10-K, Item 7 (Adjusted EBITDA reconciliation), in $ millions, for 2024 and 2023.\n\nReconciliation (sign shown as the adjustment applied to net income):\n1. Net income: 2024 = 2,648; 2023 = 4,792 (GAAP starting point)\n2. Provision for (benefit from) income taxes: 2024 = +683; 2023 = (2,690) deduction\n3. Other expense, net: 2024 = +40; 2023 = +137 (add-back)\n4. Interest income: 2024 = (818) deduction; 2023 = (721) deduction\n5. Depreciation and amortization: 2024 = +65; 2023 = +44\n6. Stock-based compensation ex
…[truncated 1,838 chars])

### Final answer
Airbnb (NASDAQ: ABNB) starts its Adjusted EBITDA reconciliation at GAAP net income and then adds back or deducts the items below. Figures are from the FY2024 Form 10-K, Item 7 (Adjusted EBITDA reconciliation), in $ millions, for 2024 and 2023.

Reconciliation (sign shown as the adjustment applied to net income):
1. Net income: 2024 = 2,648; 2023 = 4,792 (GAAP starting point)
2. Provision for (benefit from) income taxes: 2024 = +683; 2023 = (2,690) deduction
3. Other expense, net: 2024 = +40; 2023 = +137 (add-back)
4. Interest income: 2024 = (818) deduction; 2023 = (721) deduction
5. Depreciation and amortization: 2024 = +65; 2023 = +44
6. Stock-based compensation expense: 2024 = +1,407; 2023 = +1,120
7. Acquisition-related impacts: 2024 = (7) deduction; 2023 = (3) deduction
8. Lodging taxes, host withholding taxes, and transactional taxes, net: 2024 = +23; 2023 = +974
9. Adjusted EBITDA: 2024 = 4,041; 2023 = 3,653

Check (foots to the stated totals):
- 2024: 2,648 + 683 + 40 − 818 + 65 + 1,407 − 7 + 23 = 4,041 ✓
- 2023: 4,792 − 2,690 + 137 − 721 + 44 + 1,120 − 3 + 974 = 3,653 ✓

Definition and stated rationale: Airbnb defines Adjusted EBITDA as net income adjusted for the items above. Acquisition-related impacts are gains or losses from changes in the fair value of contingent consideration arrangements. The lodging, host withholding and transactional tax item covers lodging taxes for which Airbnb may have joint and several liability with hosts, withholding taxes on host payments and related settlements, and transactional taxes where how the taxes apply to its platform is significantly uncertain. The company says these items are excluded because they are non-cash, or because their amount and timing are unpredictable and not driven by core results, which makes comparisons with prior periods and competitors less meaningful. The reconciliation table has no numbered footnotes beyond this general explanation.

Note: The 2023 tax line is a large benefit of (2,690), which is why 2023 net income is well above 2024 net income while Adjusted EBITDA rose from 3,653 to 4,041 (about 10.62% growth: 4,041 / 3,653 − 1 = 10.62%). The filing's underlying reason for the 2023 tax benefit was not checked in this review.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year 2024 (SEC EDGAR)"
        }
    ]
}