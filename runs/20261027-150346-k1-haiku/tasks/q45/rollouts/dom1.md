## Rollout `dom1`
- outcome: submitted
- turns: 4; cost: $0.109; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "nongaap_addback_lookup"})
  result: ---
  name: nongaap_addback_lookup
  description: Retrieve a full-year add-back or adjustment (stock-based compensation, D&A, restructuring, etc.) from a company's Adjusted EBITDA / non-GAAP reconciliation and report it with period, units and source.
  ---
  ANALYTIC MOVE: look up one line of a non-GAAP reconciliation for a fiscal year. Sum quarters only if no annual column exists, and cross-check against the GAAP footnote.
  
  1. Pick the controlling documents. The annual add-back is in the 10-K MD&A non-GAAP section (Adjusted EBITDA reconciliation) and in the stock-compensation footnote or cash-flow statement. The Q4 8-K EX-99.1 (shareholder letter) often shows only quarterly columns. Find the 10-K or the EX-99.1 through edgar_search with company and date filters.
  2. Parse the document yourself and retrieve the line from that text. Ask for the exact label, the amount for the requested year, the prior-year comparative, and the units (millions or thousands). If only quarters are shown, sum the four quarters of the requested fiscal year. Then confirm against a second statement in the same filing, such as the SBC footnote or the cash-flow "stock-based compensation" line. Say which basis each number came from.
  3. Match the period. Use the fiscal year the question names, and check that the fiscal year-end is December 31 or otherwise. Do not use a trailing, quarterly or prior-year figure.
  4. Keep the add-back (the pre-tax expense added to net income to reach Adjusted EBITDA) separate from other SBC measures such as the amount capitalized, tax effects, or unrecognized compensation cost.
  5. Cite only documents you opened and retrieved from in this run. Do not list 10-Qs or the 10-K as sources, and do not attribute a quarterly figure to a filing you did not read. If the 10-K was not opene
  …[truncated 733 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm", "key": "abnb_q4_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_q4_2024. (54,854 characters)
  The data_storage currently contains the following keys:
  abnb_q4_2024
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb_10k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_10k_2024. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb_q4_2024
  abnb_10k_2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb document, find the Adjusted EBITDA reconciliation line for \"Stock-based compensation expense\". Give the exact label, the quarterly amounts (Q1-Q4 2024) and full-year 2024 and 2023 amounts, and the units (millions or thousands). Also find the full-year 2024 stock-based compensation expense in the cash flow statement or stock-based compensation footnote. Text: {{abnb_q4_2024}} {{abnb_10k_2024}}"})
  result: **Line item:** "Stock-based compensation expense" (in the Adjusted EBITDA Reconciliation, Q4 2024 Shareholder Letter, p. 28)
  
  **Units:** Millions of US dollars ($M)
  
  | Period | Amount ($M) |
  |---|---|
  | Q1 2024 | 295 |
  | Q2 2024 | 382 |
  | Q3 2024 | 362 |
  | Q4 2024 | 368 |
  | **FY 2024** | **1,407** (sum of quarters) |
  | **FY 2023** | **1,120** (sum of Q1–Q4 2023: 240 + 304 + 286 + 290) |
  
  The quarterly figures sum to the full-year totals in the 10-K. The 2023 quarters are 240, 304, 286 and 290.
  
  **Full-year 2024 SBC in the cash flow statement and footnotes:** $1,407 million.
  
  - Cash flow statement: "Stock-based compensation expense" of 1,407 (Year Ended December 31, 2024).
  - Note 12 (Stock-Based Compensation) and the Statements of Operations footnote both report $1,407M ($1.4 billion in the narrative text).
  
  The Statement of Stockholders' Equity shows a "Stock-based compensation" equity credit of $1,424M for 2024. That figure differs from the $1,407M expense and is not the expense amount.

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: Airbnb's 2024 stock-based compensation expense add-back in its Adjusted EBITDA reconciliation was $1,407 million (about $1.41 billion).**\n\n**Basis and steps**\n1. **Reconciliation line:** \"Stock-based compensation expense\" in the Adjusted EBITDA reconciliation, in the Q4 2024 shareholder letter (EX-99.1). Units are millions of US dollars. The letter shows quarterly columns only.\n2. **Quarterly components (2024):** Q1 $295M + Q2 $382M + Q3 $362M + Q4 $368M = **$1,407M** (295 + 382 + 362 + 368 = 1,407).\n3. **Prior-year comparative (2023):** Q1 $240M + Q2 $304M + Q3 $286M + Q4 $290M = $1,120M. This is shown for context only and is not the answer.\n4. **Cross-ch
…[truncated 1,085 chars])

### Final answer
**Answer: Airbnb's 2024 stock-based compensation expense add-back in its Adjusted EBITDA reconciliation was $1,407 million (about $1.41 billion).**

**Basis and steps**
1. **Reconciliation line:** "Stock-based compensation expense" in the Adjusted EBITDA reconciliation, in the Q4 2024 shareholder letter (EX-99.1). Units are millions of US dollars. The letter shows quarterly columns only.
2. **Quarterly components (2024):** Q1 $295M + Q2 $382M + Q3 $362M + Q4 $368M = **$1,407M** (295 + 382 + 362 + 368 = 1,407).
3. **Prior-year comparative (2023):** Q1 $240M + Q2 $304M + Q3 $286M + Q4 $290M = $1,120M. This is shown for context only and is not the answer.
4. **Cross-check:** The 2024 full-year stock-based compensation expense in the cash flow statement is $1,407M, and the stock-based compensation footnote reports the same amount. This matches the summed quarters.
5. **Excluded figure:** The statement of stockholders' equity shows a "Stock-based compensation" equity credit of $1,424M for 2024. That is a different measure from the expense add-back, so I did not use it.

I summed the quarters because the letter has no annual column for this line. The quarterly figures and the cash-flow amount agree, so the full-year figure is consistent across both sources.

**Sources**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm",
            "name": "Airbnb Q4 2024 Shareholder Letter (Form 8-K EX-99.1)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb Form 10-K for fiscal year ended December 31, 2024"
        }
    ]
}