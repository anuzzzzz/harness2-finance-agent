## Rollout `agg1`
- outcome: submitted
- turns: 5; cost: $0.187; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Airbnb adjusted EBITDA reconciliation stock-based compensation expense 2024", "ciks": ["ABNB"], "start_date": "2025-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 0, "page": 1, "results": [], "hint": "No documents matched. Try fewer/shorter terms, drop the form filter, widen the dates, or check the company's CIK/ticker."}
- edgar_search({"search_query": "Airbnb 10-K 2024 annual report stock-based compensation", "ciks": ["ABNB"], "form_types": ["10-K"]})
  result: {"total_matching_documents": 5, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-25-000010", "document": "abnb-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm"}, {"form": "10-K", "file_date": "2024-02-16", "period_ending": "2023-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-24-000006", "document": "abnb-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm"}, {"form": "10-K", "file_date": "2023-02-17", "period_ending": "2022-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-23-000003", "document": "abnb-20221231.htm", "description": "FORM 10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm"}, {"form": "10-K", "file_date": "2021-02-26", "period_ending": "2020-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-21-000010", "document": "airbnb-10k.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972021000010/airbnb-10k.htm"}, {"form": "10-K", "file_date": "2022-02-25", "period_ending": "2021-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-22-000006", "document": "abnb-20211231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972022000006/abnb-20211231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb_10k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_10k_2024. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb_10k_2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K for fiscal 2024, find the Adjusted EBITDA reconciliation table. Quote verbatim the row label and the 2024 amount (in millions) for \"Stock-based compensation expense\" in the reconciliation of Net income to Adjusted EBITDA, along with the 2023 and 2022 amounts and the units. Also quote the 2024 Adjusted EBITDA total. Document: {{abnb_10k_2024}}"})
  result: **Adjusted EBITDA reconciliation (Item 7, "Adjusted EBITDA Reconciliation")**
  
  - **Row label:** "Stock-based compensation expense"
  - **2024 amount:** 1,407
  - **2023 amount:** 1,120
  - **Units:** millions of U.S. dollars (the table header reads "in millions, except percentages")
  
  The reconciliation table has columns only for 2023 and 2024, so it does not include a 2022 figure. The 2022 stock-based compensation expense appears elsewhere in the filing: $930 million in the Consolidated Statements of Cash Flows and in the segment expense table (Note 16), and the Note 12 text gives "$930 million" for 2022.
  
  - **2024 Adjusted EBITDA total:** "$4,041" (in millions), which is $4.0 billion.

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K for fiscal 2024, quote verbatim the 2024 amount (in millions) for the \"Stock-based compensation\" line in the Consolidated Statements of Cash Flows operating activities, and the Adjusted EBITDA reconciliation row \"Stock-based compensation expense\" 2024 value. Document: {{abnb_10k_2024}}"})
  result: **Cash flow statement (operating activities), "Stock-based compensation expense," 2024: 1,407**
  
  **Adjusted EBITDA reconciliation, "Stock-based compensation expense," 2024: 1,407**
  
  Both figures are $1,407 million.

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "Airbnb's 2024 adjustment for stock-based compensation expense was $1,407 million (about $1.41 billion).\n\nHow I got it:\n- I opened Airbnb's Form 10-K for fiscal year 2024 (period ending December 31, 2024, filed February 13, 2025) from SEC EDGAR.\n- In the Item 7 \"Adjusted EBITDA Reconciliation\" table (stated in millions of U.S. dollars), the \"Stock-based compensation expense\" line shows 1,407 for 2024 and 1,120 for 2023.\n- A second pass through the same filing confirmed the same $1,407 million figure in the Consolidated Statements of Cash Flows (operating activities), so the reconciliation and cash flow statement agree.\n- For context, the same reconciliation gives 2
…[truncated 586 chars])

### Final answer
Airbnb's 2024 adjustment for stock-based compensation expense was $1,407 million (about $1.41 billion).

How I got it:
- I opened Airbnb's Form 10-K for fiscal year 2024 (period ending December 31, 2024, filed February 13, 2025) from SEC EDGAR.
- In the Item 7 "Adjusted EBITDA Reconciliation" table (stated in millions of U.S. dollars), the "Stock-based compensation expense" line shows 1,407 for 2024 and 1,120 for 2023.
- A second pass through the same filing confirmed the same $1,407 million figure in the Consolidated Statements of Cash Flows (operating activities), so the reconciliation and cash flow statement agree.
- For context, the same reconciliation gives 2024 Adjusted EBITDA of $4,041 million. The 2024 adjustment is the largest add-back in that reconciliation and is the figure the question asks for.

Note: the reconciliation table only covers 2023 and 2024. The 2022 stock-based compensation figure ($930 million) appears elsewhere in the filing, not in that table.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year 2024 (filed 2025-02-13)"
        }
    ]
}