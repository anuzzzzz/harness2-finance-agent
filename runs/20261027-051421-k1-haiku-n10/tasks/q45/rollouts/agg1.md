## Rollout `agg1`
- outcome: submitted
- turns: 3; cost: $0.090; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "non_gaap_adjustment_lookup"})
  result: ---
  name: non_gaap_adjustment_lookup
  description: Retrieve a specific adjustment line (e.g. stock-based compensation) from a company's Adjusted EBITDA / non-GAAP reconciliation for a fiscal year.
  ---
  
  # Non-GAAP adjustment lookup ("what was the adjustment for X in year Y")
  
  **Analytic move:** retrieve and reconcile. The answer is one line of the company's own reconciliation table for the stated fiscal year, with its units and a check that the table foots.
  
  **Where the figure lives**
  - Q4/full-year earnings release or shareholder letter (8-K Exhibit 99.1): the "Reconciliation of Net Income to Adjusted EBITDA" table, with quarterly and full-year columns. Use the full-year column for an "in 2024" question, not the Q4 column.
  - 10-K, MD&A, "Adjusted EBITDA" or "Non-GAAP Financial Measures" section: the same table for the fiscal year, with the prior year beside it.
  - The cash flow statement and the stock-based compensation footnote also report a stock-based compensation figure. It can differ from the add-back. For an "adjustment" question the reconciliation line is the controlling figure. Mention the cash-flow figure only if it differs, and label it.
  
  **Procedure**
  1. Fix the fiscal year the question names and the measure (Adjusted EBITDA vs free cash flow vs non-GAAP net income). Each has its own reconciliation.
  2. Read the line from the reconciliation table (opened document or a search excerpt quoting it), not from memory. Record the unit in the table header.
  3. Foot the table where the excerpt allows: net income plus every listed adjustment, with signs, must equal Adjusted EBITDA. If it does not, you misread a line, column or year.
  4. Give the prior-year comparative and the year-over-year change only as brief context. Do not add figures the question did not ask for.
  5. An
  …[truncated 312 chars]

### Turn 2  (stop_reason=end_turn)
**Answer: Airbnb's 2024 stock-based compensation adjustment was $1,407 million.**

**Source and units:** The figure comes from the "Adjusted EBITDA Reconciliation" table in Airbnb's FY2024 annual report (10-K), where the reconciliation runs from net income to Adjusted EBITDA for the year ended December 31, 2024, in millions. I saw this table in a search excerpt, not in an opened filing, so I am not calling it verified. The same figure appears as the $1,407 million stock-based compensation expense in the cash flow statement in the Q4 2024 shareholder letter excerpt, which is consistent with the add-back.

**Footing check (2024, $ millions), from the excerpt:**
- Net income: 2,648
- Provision for income taxes: 683
- Other expense, net: 40
- Interest income: (818)
- Depreciation and amortization: 65
- Stock-based compensation expense: 1,407
- Acquisition-related impacts: (7)
- Lodging taxes, host withholding taxes, and transactional taxes, net: 23
- Sum: 2,648 + 683 + 40 − 818 + 65 + 1,407 − 7 + 23 = 4,041, which matches the reported Adjusted EBITDA of $4,041 million.

**Context:** The 2023 comparative was $1,120 million, so the 2024 figure was about 25.63% higher ((1,407 − 1,120) / 1,120). Airbnb's Q4 2024 letter also reports full-year 2024 net income of $2.6 billion and Adjusted EBITDA of $4.0 billion, which agrees with the table.

{
    "sources": [
        {
            "url": "https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.
…[truncated 351 chars]
- web_search(query="Airbnb full year 2024 Adjusted EBITDA reconciliation stock-based compensation expense") → 10 results: Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000032/abnb-20240930.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000017/abnb-20240331.htm>
- web_search(query="Airbnb fourth quarter 2024 shareholder letter exhibit 99.1 reconciliation") → 10 results: Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462d8k.htm>
- web_search(query="Airbnb 2024 full year stock-based compensation expense adjusted EBITDA $3.5 billion reconciliation table") → 10 results: Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000032/abnb-20240930.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000024/abnb-20240630.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm>
- web_search(query="Airbnb Q4 2024 shareholder letter exhibit 99.1 February 2025") → 10 results: Airbnb, Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm>; Airbnb, Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1559720/000119312525109934/d40594dex991.htm>
- web_search(query="Airbnb 10-K 2024 Adjusted EBITDA reconciliation year ended December 31, 2024 stock-based compensation expense net income $2,646") → 9 results: Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000032/abnb-20240930.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000024/abnb-20240630.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000017/abnb-20240331.htm>; Airbnb, Inc. - Form 10-K - FY2021 <https://www.sec.gov/Archives/edgar/data/1559720/000155972022000006/abnb-20211231.htm>; Airbnb, Inc. (Form: 10-K, Received: 02/16/2024 16:03:41) <https://content.edgar-online.com/ExternalLink/EDGAR/0001559720-24-000006.html?hash=8fb59a79794331d61fbddd144f54c3e63f372875378160b08c84a6274e949294&dest=exh1011sfo_888brannanxgrou_htm>

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "Airbnb's 2024 stock-based compensation adjustment in its Adjusted EBITDA reconciliation was $1,407 million (in millions of USD, year ended December 31, 2024).\n\nSource and units: The figure comes from the \"Adjusted EBITDA Reconciliation\" table in Airbnb's FY2024 annual report (10-K), which reconciles net income to Adjusted EBITDA in millions. I saw this table in a search excerpt, not in an opened filing, so it is not described as verified. The same $1,407 million appears as stock-based compensation expense in the cash flow statement excerpt from the Q4 2024 shareholder letter, which is consistent with the add-back.\n\nFooting check (2024, $ millions): Net income 2,648 + 
…[truncated 974 chars])

### Final answer
Airbnb's 2024 stock-based compensation adjustment in its Adjusted EBITDA reconciliation was $1,407 million (in millions of USD, year ended December 31, 2024).

Source and units: The figure comes from the "Adjusted EBITDA Reconciliation" table in Airbnb's FY2024 annual report (10-K), which reconciles net income to Adjusted EBITDA in millions. I saw this table in a search excerpt, not in an opened filing, so it is not described as verified. The same $1,407 million appears as stock-based compensation expense in the cash flow statement excerpt from the Q4 2024 shareholder letter, which is consistent with the add-back.

Footing check (2024, $ millions): Net income 2,648 + provision for income taxes 683 + other expense, net 40 + interest income (818) + depreciation and amortization 65 + stock-based compensation 1,407 + acquisition-related impacts (7) + lodging taxes, host withholding taxes and transactional taxes, net 23 = 4,041, matching reported Adjusted EBITDA of $4,041 million.

Context: The 2023 comparative was $1,120 million, so the 2024 figure rose about 25.63% ((1,407 − 1,120) / 1,120 = 25.625%).

{
    "sources": [
        {
            "url": "https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf",
            "name": "Airbnb FY2024 Form 10-K (annual report PDF), Adjusted EBITDA Reconciliation"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm",
            "name": "Airbnb Q4 2024 Shareholder Letter (Exhibit 99.1 to Form 8-K, February 13, 2025)"
        }
    ]
}