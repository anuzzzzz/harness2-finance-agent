## Rollout `inv1`
- outcome: submitted
- turns: 4; cost: $0.099; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Airbnb annual report 2024 stock-based compensation adjusted EBITDA", "ciks": ["ABNB"], "start_date": "2025-01-01", "end_date": "2025-04-07", "form_types": ["10-K"]})
  result: {"total_matching_documents": 1, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-25-000010", "document": "abnb-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm"}]}
- edgar_search({"search_query": "Airbnb Q4 2024 shareholder letter adjusted EBITDA reconciliation", "ciks": ["ABNB"], "start_date": "2025-02-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 1, "page": 1, "results": [{"form": "8-K", "file_date": "2025-02-13", "period_ending": "2025-02-13", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-25-026054", "document": "d915198dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm"}]}

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb_10k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_10k_2024. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb_10k_2024
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm", "key": "abnb_q4_2024_letter"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_q4_2024_letter. (54,854 characters)
  The data_storage currently contains the following keys:
  abnb_10k_2024
  abnb_q4_2024_letter
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K for fiscal 2024, find the stock-based compensation line in the consolidated statements of cash flows (year ended December 31, 2024), and the stock-based compensation figure in the Adjusted EBITDA reconciliation if present. Quote the row verbatim with its period, units (in millions), and label. Also give the 2023 and 2022 values. Document: {{abnb_10k_2024}}"})
  result: **Consolidated Statements of Cash Flows** (Item 8, "Adjustments to reconcile net income to cash provided by operating activities," in millions; columns are 2022, 2023, 2024):
  
  > Stock-based compensation expense930 1,120 1,407
  
  - **Year ended December 31, 2024:** $1,407 million
  - **Year ended December 31, 2023:** $1,120 million
  - **Year ended December 31, 2022:** $930 million
  
  **Adjusted EBITDA Reconciliation** (in the MD&A, in millions; columns are 2023, 2024):
  
  > Stock-based compensation expense1,120 1,407
  
  - **Year ended December 31, 2024:** $1,407 million
  - **Year ended December 31, 2023:** $1,120 million
  - **2022:** not presented in this reconciliation, which covers only 2023 and 2024.
  
  The two statements agree for 2023 and 2024.
- retrieve_information({"prompt": "From this Airbnb Q4 2024 shareholder letter, find the Adjusted EBITDA reconciliation table and the \"Stock-based compensation expense\" row. Quote the row verbatim with its column periods and units. Is there a full-year 2024 column? Document: {{abnb_q4_2024_letter}}"})
  result: **Stock-based compensation expense** row, quoted from the Adjusted EBITDA Reconciliation table:
  
  > Stock-based compensation expense 195 247 234 254 240 304 286 290 295 382 362 368
  
  **Column periods:** The table header reads "Three Months Ended," with twelve quarterly columns in this order: Mar 31, Jun 30, Sept 30, Dec 31 for 2022, then 2023, then 2024. Mapped to the columns, the values are:
  
  | Period | SBC ($M) |
  |---|---|
  | Q1–Q4 2022 | 195, 247, 234, 254 |
  | Q1–Q4 2023 | 240, 304, 286, 290 |
  | Q1–Q4 2024 | 295, 382, 362, 368 |
  
  **Units:** The table is labeled "(in millions, except percentages)," so the values are in $ millions.
  
  **Full-year 2024 column:** No. The reconciliation has only quarterly columns and no "Year Ended" column. The four 2024 quarters sum to $1,407M (295 + 382 + 362 + 368), which matches the full-year SBC figure in the letter's Statement of Operations footnote and the cash flow statement. That figure comes from those other tables, not from a column in the reconciliation.
  
  The text extraction of this table is jumbled, with row labels interleaved with numbers. I mapped the values to periods by column order and checked them against the Q4 2023 ($290M) and Q4 2024 ($368M) figures in the separate SBC footnote, which match.

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: Airbnb's stock-based compensation expense adjustment for fiscal 2024 was $1,407 million** (up from $1,120 million in 2023).\n\n**Supporting logic and sources**\n\n1. **FY2024 Form 10-K (primary, opened and checked).** In the consolidated statements of cash flows, the \"Stock-based compensation expense\" line under operating adjustments shows $930M (2022), $1,120M (2023) and $1,407M (2024), in millions. The Adjusted EBITDA reconciliation in the MD&A carries the same line: $1,120M for 2023 and $1,407M for 2024. The two statements agree. That reconciliation covers only 2023 and 2024, so there is no 2022 figure in it.\n\n2. **Q4 2024 shareholder letter (8-K Exhibit 99
…[truncated 1,038 chars])

### Final answer
**Answer: Airbnb's stock-based compensation expense adjustment for fiscal 2024 was $1,407 million** (up from $1,120 million in 2023).

**Supporting logic and sources**

1. **FY2024 Form 10-K (primary, opened and checked).** In the consolidated statements of cash flows, the "Stock-based compensation expense" line under operating adjustments shows $930M (2022), $1,120M (2023) and $1,407M (2024), in millions. The Adjusted EBITDA reconciliation in the MD&A carries the same line: $1,120M for 2023 and $1,407M for 2024. The two statements agree. That reconciliation covers only 2023 and 2024, so there is no 2022 figure in it.

2. **Q4 2024 shareholder letter (8-K Exhibit 99.1, cross-check).** The Adjusted EBITDA reconciliation is presented by quarter only, with no full-year column. The quarterly stock-based compensation figures for 2024 are $295M, $382M, $362M and $368M. These sum to $1,407M, matching the 10-K. The text extraction of this table was jumbled, so I mapped values to periods by column order and checked them against the separately disclosed Q4 2023 ($290M) and Q4 2024 ($368M) figures.

Unit: US$ millions. Period: fiscal year ended December 31, 2024.

**Sources:**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year ended December 31, 2024 (abnb-20241231.htm)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm",
            "name": "Airbnb, Inc. Q4 2024 Shareholder Letter, Form 8-K Exhibit 99.1 (d915198dex991.htm)"
        }
    ]
}