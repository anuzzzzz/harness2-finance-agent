## Rollout `dom1`
- outcome: submitted
- turns: 3; cost: $0.099; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb_10k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_10k_2024. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb_10k_2024
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K, find the reconciliation of Net income (loss) to Adjusted EBITDA table in the Non-GAAP Financial Measures section. List every line item in order, with the FY2024 and FY2023 amounts (in $ millions, noting parentheses as negatives), the Adjusted EBITDA totals, and any footnote or stated reason describing why items are excluded (e.g., stock-based compensation, lodging taxes, interest income, acquisition-related impacts). Quote the exact line labels. Document: {{abnb_10k_2024}}"})
  result: **Source:** Item 7, MD&A, "Non-GAAP Financial Measures," subsection "Adjusted EBITDA Reconciliation" (10-K p. 37). The table is stated "in millions, except percentages."
  
  | Line item (exact label) | FY2024 | FY2023 |
  |---|---|---|
  | Revenue | $11,102 | $9,917 |
  | Net income | $2,648 | $4,792 |
  | *Adjusted to exclude the following:* | | |
  | Provision for (benefit from) income taxes | 683 | (2,690) |
  | Other expense, net | 40 | 137 |
  | Interest income | (818) | (721) |
  | Depreciation and amortization | 65 | 44 |
  | Stock-based compensation expense | 1,407 | 1,120 |
  | Acquisition-related impacts | (7) | (3) |
  | Lodging taxes, host withholding taxes, and transactional taxes, net | 23 | 974 |
  | **Adjusted EBITDA** | **$4,041** | **$3,653** |
  | Adjusted EBITDA Margin | 36% | 37% |
  
  **Sign convention:** The table shows each adjustment as the amount added to or subtracted from net income. The 10-K's income statement shows "Other income (expense), net" as (40) for 2024 and (137) for 2023, but the reconciliation adds back the expense as a positive 40 and 137. Likewise, interest income is deducted as a negative, and the 2023 tax benefit is deducted as a negative.
  
  **Check:** 2024: $2,648 + 683 + 40 − 818 + 65 + 1,407 − 7 + 23 = $4,041. 2023: $4,792 − 2,690 + 137 − 721 + 44 + 1,120 − 3 + 974 = $3,653.
  
  **Stated reasons for exclusions:**
  
  - **Stated reason (general, following the table):** "The above items are excluded from our Adjusted EBITDA measure because they are non-cash in nature, or because the amount and timing of these items are unpredictable, not driven by core results of operations, and renders comparisons with prior periods and competitors less meaningful."
  - **Definition (Non-GAAP table in the same section):** Adjusted EBITDA is net income adjusted for:
    - provision fo
  …[truncated 673 chars]

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "Airbnb starts from Net income and adds back or subtracts the items below to reach Adjusted EBITDA. I opened the FY2024 Form 10-K and checked the reconciliation table in Item 7 (MD&A, Non-GAAP Financial Measures, p. 37). All figures are in $ millions.\n\nReconciliation, in the order shown (FY2024 / FY2023):\n1. Net income: 2,648 / 4,792\n2. Provision for (benefit from) income taxes: add 683 / (2,690). The 2023 benefit is deducted.\n3. Other expense, net: add 40 / 137\n4. Interest income: deduct (818) / (721)\n5. Depreciation and amortization: add 65 / 44\n6. Stock-based compensation expense: add 1,407 / 1,120\n7. Acquisition-related impacts: deduct (7) / (3)\n8. Lodging taxe
…[truncated 1,534 chars])

### Final answer
Airbnb starts from Net income and adds back or subtracts the items below to reach Adjusted EBITDA. I opened the FY2024 Form 10-K and checked the reconciliation table in Item 7 (MD&A, Non-GAAP Financial Measures, p. 37). All figures are in $ millions.

Reconciliation, in the order shown (FY2024 / FY2023):
1. Net income: 2,648 / 4,792
2. Provision for (benefit from) income taxes: add 683 / (2,690). The 2023 benefit is deducted.
3. Other expense, net: add 40 / 137
4. Interest income: deduct (818) / (721)
5. Depreciation and amortization: add 65 / 44
6. Stock-based compensation expense: add 1,407 / 1,120
7. Acquisition-related impacts: deduct (7) / (3)
8. Lodging taxes, host withholding taxes, and transactional taxes, net: add 23 / 974
9. Adjusted EBITDA: 4,041 / 3,653 (Adjusted EBITDA margin 36% / 37%, per the table)

Foot checks:
- FY2024: 2,648 + 683 + 40 − 818 + 65 + 1,407 − 7 + 23 = 4,041
- FY2023: 4,792 − 2,690 + 137 − 721 + 44 + 1,120 − 3 + 974 = 3,653

Stated reasons: The company says these items are excluded because they are non-cash in nature, or because their amount and timing are unpredictable and not driven by core results of operations. The company adds that this makes comparisons with prior periods and competitors less meaningful if they stayed in.

Item definitions (from the same section):
- Acquisition-related impacts are gains or losses from changes in the fair value of contingent consideration arrangements.
- The lodging tax line covers lodging taxes the company may be jointly and severally liable for with hosts, withholding taxes on payments to hosts and related settlements, and transactional taxes where it is significantly uncertain how the taxes apply to the platform.

Sign note: The income statement shows Other income (expense), net as (40) for 2024 and (137) for 2023, but the reconciliation adds back the expense as positive amounts.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. FY2024 Form 10-K (Item 7, Non-GAAP Financial Measures – Adjusted EBITDA reconciliation)"
        }
    ]
}