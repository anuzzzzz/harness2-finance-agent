## Rollout `dom1`
- outcome: submitted
- turns: 4; cost: $0.095; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "non_gaap_adjustment_lookup"})
  result: ---
  name: non_gaap_adjustment_lookup
  description: Retrieve a company's full-year non-GAAP reconciling adjustment (e.g. stock-based compensation in Adjusted EBITDA) from the 10-K and cross-check it.
  ---
  
  # Non-GAAP adjustment for a fiscal year
  
  ANALYTIC MOVE: read one line item of the company's non-GAAP reconciliation (Adjusted EBITDA, adjusted net income, free cash flow) for the full fiscal year the question names.
  
  WHERE THE FULL-YEAR FIGURE LIVES
  1. Governing source: the 10-K for that fiscal year. The reconciliation is in MD&A under "Non-GAAP Financial Measures" or "Key Business Metrics and Non-GAAP", with an annual column. Use `edgar_search` with form 10-K and the ticker to get the URL.
  2. Cross-checks, all from the same 10-K:
     - Cash flow statement (operating section) shows the stock-based compensation add-back.
     - The equity note or the income statement footnote gives SBC by function.
     - The MD&A line item should equal these, unless the reconciliation excludes some items. If they differ, report the reconciliation line as the answer, say why they differ, and give both.
  3. The Q4 8-K Exhibit 99.1 shareholder letter often shows only quarterly columns. Do not build a full-year figure by adding four quarters when one quarter has not been read from the table. A derived sum is a fallback only. If you use it, label it as derived and read every quarter from a document.
  
  ANSWER CONTRACT
  - The figure with fiscal year, units (millions or thousands) and the exact row label from the reconciliation.
  - The prior-year comparative from the same table.
  - The document and table it came from, and the cross-check result.
  - If asked for the "adjustment", state the sign. An add-back is positive in the reconciliation.
  
  CHECKS BEFORE SUBMIT
  - The column is the full fiscal year, not a 
  …[truncated 1,143 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb_10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_10k. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb_10k
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K, find the Adjusted EBITDA reconciliation table in the Non-GAAP Financial Measures section. Quote the exact row label and the full-year 2024 and 2023 values for \"Stock-based compensation expense\" (in millions). Also find the stock-based compensation add-back in the cash flow statement operating activities for 2024 and 2023, and the total stock-based compensation expense in the equity note for 2024. Report units from table headers. Document: {{abnb_10k}}"})
  result: **Adjusted EBITDA Reconciliation** (Item 7, Non-GAAP Financial Measures; header: "in millions, except percentages")
  
  - **Row label:** "Stock-based compensation expense"
  - **2023:** $1,120 million
  - **2024:** $1,407 million
  
  **Cash flow statement, operating activities** (Consolidated Statements of Cash Flows; header: "in millions")
  
  - **Row label:** "Stock-based compensation expense"
  - **2023:** $1,120 million
  - **2024:** $1,407 million
  
  **Equity note** (Note 12, Stock-Based Compensation and Employee Benefit Plan)
  
  - **2024:** The note states "$1.4 billion" in the text, which is the rounded form of the $1,407 million shown in the reconciliation and cash flow statement. The note text uses billions rather than the millions header used in the tables.

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: Airbnb's 2024 stock-based compensation adjustment was $1,407 million (an add-back of +$1,407 million, reported in millions).**\n\n**Step-by-step:**\n1. The earlier quarterly sum (295 + 382 + 362 + an unconfirmed Q4 of 368 = 1,407) was treated only as a lead, not as the answer. I did not rely on it.\n2. I pulled Airbnb's FY2024 Form 10-K (accession 0001559720-25-000010) and extracted the relevant tables.\n3. **Adjusted EBITDA reconciliation** (Item 7, Non-GAAP Financial Measures; header \"in millions, except percentages\"): row \"Stock-based compensation expense\" = $1,407 million for 2024 and $1,120 million for 2023. Sign: positive add-back.\n4. **Cross-check, cas
…[truncated 1,347 chars])

### Final answer
**Answer: Airbnb's 2024 stock-based compensation adjustment was $1,407 million (an add-back of +$1,407 million, reported in millions).**

**Step-by-step:**
1. The earlier quarterly sum (295 + 382 + 362 + an unconfirmed Q4 of 368 = 1,407) was treated only as a lead, not as the answer. I did not rely on it.
2. I pulled Airbnb's FY2024 Form 10-K (accession 0001559720-25-000010) and extracted the relevant tables.
3. **Adjusted EBITDA reconciliation** (Item 7, Non-GAAP Financial Measures; header "in millions, except percentages"): row "Stock-based compensation expense" = $1,407 million for 2024 and $1,120 million for 2023. Sign: positive add-back.
4. **Cross-check, cash flow statement** (operating activities; header "in millions"): row "Stock-based compensation expense" = $1,407 million for 2024 and $1,120 million for 2023. This matches the reconciliation.
5. **Cross-check, equity note** (Note 12, Stock-Based Compensation and Employee Benefit Plan): the text cites "$1.4 billion" for 2024, which is the rounded form of $1,407 million. This is consistent.

**Conclusion:** The reconciliation, cash flow statement, and equity note all agree. The 2024 figure is $1,407 million, up from $1,120 million in 2023.

**Caveat:** The 10-K tables were extracted by an automated parse, and I verified the figures through that extraction rather than by reading the raw table cells. The 2024 value agrees across three locations in the filing, which supports it.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year 2024 (Adjusted EBITDA reconciliation, cash flow statement, Note 12)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm",
            "name": "Airbnb Q4 2024 shareholder letter (Exhibit 99.1), referenced as the quarterly source"
        }
    ]
}