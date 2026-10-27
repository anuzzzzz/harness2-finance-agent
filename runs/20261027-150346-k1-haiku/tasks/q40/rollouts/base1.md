## Rollout `base1`
- outcome: submitted
- turns: 4; cost: $0.111; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Airbnb Q4 2024 results adjusted EBITDA reconciliation net income") → 0 results: 
- edgar_search({"search_query": "Airbnb adjusted EBITDA reconciliation net income", "ciks": ["ABNB"], "start_date": "2024-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 10, "page": 1, "results": [{"form": "8-K", "file_date": "2024-08-06", "period_ending": "2024-08-06", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-194849", "document": "d831385dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm"}, {"form": "8-K", "file_date": "2025-02-13", "period_ending": "2025-02-13", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-25-026054", "document": "d915198dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm"}, {"form": "8-K", "file_date": "2024-11-07", "period_ending": "2024-11-07", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-253103", "document": "d886752dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm"}, {"form": "8-K", "file_date": "2024-05-08", "period_ending": "2024-05-08", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-134183", "document": "d813800dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm"}, {"form": "8-K", "file_date": "2024-02-13", "period_ending": "2024-02-13", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-033706", "document": "d646462dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm"}, {"form": "10-Q", "file_date":
  …[truncated 1,676 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000017/abnb-20240331.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000032/abnb-20240930.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb_10k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_10k_2024. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb_10k_2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K, find the \"Adjusted EBITDA\" reconciliation table that starts from net income and lists the items adjusted to exclude (e.g., provision for income taxes, other income/expense, interest income, depreciation and amortization, stock-based compensation, acquisition-related impacts, lodging tax reserves, etc.). List every adjustment line item with its FY2024, FY2023 and FY2022 amounts (in millions), and the adjusted EBITDA totals, plus any footnotes explaining the items. Text: {{abnb_10k_2024}}"})
  result: The 10-K's Adjusted EBITDA reconciliation covers only **FY2024 and FY2023**. It does not include FY2022, so I can't give you a FY2022 Adjusted EBITDA total or FY2022 adjustment amounts from this filing. The FY2023 10-K would contain them.
  
  ## Adjusted EBITDA Reconciliation (in millions)
  
  | Line item | FY2024 | FY2023 |
  |---|---|---|
  | Revenue | $11,102 | $9,917 |
  | **Net income** | **$2,648** | **$4,792** |
  | Provision for (benefit from) income taxes | 683 | (2,690) |
  | Other expense, net | 40 | 137 |
  | Interest income | (818) | (721) |
  | Depreciation and amortization | 65 | 44 |
  | Stock-based compensation expense | 1,407 | 1,120 |
  | Acquisition-related impacts | (7) | (3) |
  | Lodging taxes, host withholding taxes, and transactional taxes, net | 23 | 974 |
  | **Adjusted EBITDA** | **$4,041** | **$3,653** |
  | Adjusted EBITDA Margin | 36% | 37% |
  
  Parentheses indicate negative amounts. The totals foot: for FY2023, $4,792 − 2,690 + 137 − 721 + 44 + 1,120 − 3 + 974 = $3,653; for FY2024, $2,648 + 683 + 40 − 818 + 65 + 1,407 − 7 + 23 = $4,041.
  
  ## Footnotes and Context from the Filing
  
  - **Definition:** Adjusted EBITDA is net income adjusted for the items above. Adjusted EBITDA Margin is Adjusted EBITDA divided by revenue.
  - **Rationale:** The company says these items are excluded because they are non-cash, or because their amount and timing are unpredictable and not driven by core results. It states this makes comparisons with prior periods and competitors less meaningful.
  - **Provision for (benefit from) income taxes:** FY2023 was a $2.7 billion benefit, driven mainly by the release of $2.9 billion of valuation allowance on U.S. federal and state deferred tax assets. FY2024 was a $683 million expense, reflecting current taxes and deferred tax expense from using some of those
  …[truncated 847 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Short answer:** Airbnb starts from GAAP net income and adds back or subtracts the following items to arrive at Adjusted EBITDA:\n\n1. **Provision for (benefit from) income taxes**\n2. **Other (income) expense, net**\n3. **Interest income** (deducted, since it is income)\n4. **Depreciation and amortization**\n5. **Stock-based compensation expense**\n6. **Acquisition-related impacts** (changes in the fair value of contingent consideration)\n7. **Lodging taxes, host withholding taxes, and transactional taxes, net** (also referred to in earlier periods as lodging tax reserves and reserves for host withholding taxes)\n\nThe company's stated rationale is that <cite index=\"5-2\
…[truncated 3,117 chars])

### Final answer
**Short answer:** Airbnb starts from GAAP net income and adds back or subtracts the following items to arrive at Adjusted EBITDA:

1. **Provision for (benefit from) income taxes**
2. **Other (income) expense, net**
3. **Interest income** (deducted, since it is income)
4. **Depreciation and amortization**
5. **Stock-based compensation expense**
6. **Acquisition-related impacts** (changes in the fair value of contingent consideration)
7. **Lodging taxes, host withholding taxes, and transactional taxes, net** (also referred to in earlier periods as lodging tax reserves and reserves for host withholding taxes)

The company's stated rationale is that <cite index="5-2">the above items are excluded from our Adjusted EBITDA measure because they are non-cash in nature, or because the amount and timing of these items are unpredictable, not driven by core results of operations, and renders comparisons with prior periods and competitors less meaningful.</cite>

Note that stock-based compensation is excluded, but Airbnb footnotes that it is <cite index="5-1">a significant recurring expense in our business and an important part of our compensation strategy.</cite>

**Full-year reconciliation (from the FY2024 Form 10-K, $ millions):**

| Line item | FY2024 | FY2023 |
|---|---|---|
| Net income | 2,648 | 4,792 |
| Provision for (benefit from) income taxes | 683 | (2,690) |
| Other expense, net | 40 | 137 |
| Interest income | (818) | (721) |
| Depreciation and amortization | 65 | 44 |
| Stock-based compensation expense | 1,407 | 1,120 |
| Acquisition-related impacts | (7) | (3) |
| Lodging taxes, host withholding taxes, and transactional taxes, net | 23 | 974 |
| **Adjusted EBITDA** | **4,041** | **3,653** |
| Adjusted EBITDA margin | 36% | 37% |

Arithmetic check: FY2024 = 2,648 + 683 + 40 − 818 + 65 + 1,407 − 7 + 23 = 4,041. FY2023 = 4,792 − 2,690 + 137 − 721 + 44 + 1,120 − 3 + 974 = 3,653. Both foot.

**Context on the larger items:**
- The FY2023 tax line was a benefit driven mainly by releasing a valuation allowance on U.S. deferred tax assets. FY2024 was an expense.
- FY2023's $974 million lodging/withholding tax adjustment was largely tied to the Italy withholding tax settlements.
- FY2024 "other expense, net" included a $45 million impairment on a private investment, partly offset by $77 million of FX gains.
- The Q4 2024 shareholder letter confirms the FY2024 result: <cite index="8-11">Adjusted EBITDA of $4.0 billion in 2024 increased 11% year-over-year and represented an Adjusted EBITDA Margin of 36%.</cite>

**Caveat:** The FY2024 table and the explanatory notes were extracted from the 10-K by an automated reading of the filing. The totals foot, but I did not visually verify each line against the original HTML. The adjustment categories above are also consistent with the 2024 10-Q reconciliations.

**Sources:**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb Form 10-K for fiscal year 2024 (filed 2025-02-13)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000032/abnb-20240930.htm",
            "name": "Airbnb Form 10-Q for quarter ended September 30, 2024"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000024/abnb-20240630.htm",
            "name": "Airbnb Form 10-Q for quarter ended June 30, 2024"
        },
        {
            "url": "https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/Airbnb_Q4-2024-Shareholder-Letter_Final.pdf",
            "name": "Airbnb Q4 2024 Shareholder Letter"
        }
    ]
}