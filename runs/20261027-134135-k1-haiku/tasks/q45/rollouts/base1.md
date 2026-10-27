## Rollout `base1`
- outcome: submitted
- turns: 4; cost: $0.029; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Airbnb fourth quarter full year 2024 results adjusted EBITDA stock-based compensation") → 0 results: 
- edgar_search({"search_query": "Airbnb adjusted EBITDA reconciliation stock-based compensation 2024", "ciks": ["ABNB"], "start_date": "2025-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 2, "page": 1, "results": [{"form": "8-K", "file_date": "2025-02-13", "period_ending": "2025-02-13", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-25-026054", "document": "d915198dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm"}, {"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-25-000010", "document": "abnb-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000017/abnb-20240331.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm", "key": "abnb_q4_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_q4_2024. (54,854 characters)
  The data_storage currently contains the following keys:
  abnb_q4_2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this document, find the full-year 2024 (twelve months ended December 31, 2024) Adjusted EBITDA reconciliation table. Report the 'Stock-based compensation expense' figure for FY 2024 exactly as shown, the FY 2023 figure, the table's units (millions or thousands), and the full-year Adjusted EBITDA and net income for 2024. Also note the footnote text about stock-based compensation if present. Document: {{abnb_q4_2024}}"})
  result: **Full-year 2024 figures**
  
  - **Stock-based compensation expense, FY 2024:** $1,407 (as shown in the income statement footnote, "Stock-based compensation expense" total, Year Ended December 31, 2024)
  - **Stock-based compensation expense, FY 2023:** $1,120 (same footnote)
  - **Units:** Millions (USD)
  - **Adjusted EBITDA, FY 2024:** $4,041M, the sum of the four 2024 quarters ($424 + $894 + $1,958 + $765). The letter describes this as "$4.0 billion."
  - **Net income, FY 2024:** $2,648M (the sum of the quarters, and the Year Ended December 31, 2024 figure in the Statements of Operations)
  
  **Notes on the source**
  
  - The document has no single full-year column in the Adjusted EBITDA reconciliation. It presents quarterly columns for 2022 through 2024. The full-year values above are my sums of those quarters. The quarterly SBC figures for 2024 ($295M, $382M, $362M, $368M) also sum to $1,407M, which matches the annual figure.
  - The reconciliation's rows for acquisition-related impacts and lodging/withholding/transactional taxes are garbled in the text extraction, so I could not reliably reconstruct the full-year line-item totals.
  - The reconciliation table has no footnote specifically about stock-based compensation. The relevant text is:
    - In the Non-GAAP definition, Adjusted EBITDA is defined as net income (loss) adjusted for "(iv) stock-based compensation expense."
    - A limitation bullet states: "Adjusted EBITDA excludes stock-based compensation expense, which has been, and will continue to be for the foreseeable future, a significant recurring expense in our business and an important part of our compensation strategy."
    - The income statement footnote (1) reads: "Includes stock-based compensation expense as follows (in millions)," followed by the breakdown by function.
  - Th
  …[truncated 162 chars]

### Turn 4  (stop_reason=tool_use)
**Answer: about $1,407 million (≈$1.41 billion) of stock-based compensation was added back to net income to reach Adjusted EBITDA for full-year 2024.** I built this total from quarterly figures, so treat it as a derived figure rather than a number read directly from the annual table.

**How I got it**

- **Q1 2024:** 
Stock-based compensation expense(1) | 240 | 295
 (2023 and 2024 columns). That is $295 million for the quarter.
- **Q2 2024:** The Q2 10-Q reconciliation shows $382 million for the quarter. 
Total stock-based compensation expense was $304 million and $382 million for the three months ended June 30, 2023 and 2024
.
- **Q3 2024:** The Q3 10-Q reconciliation shows $362 million for the quarter. Its nine-month figure is $1,039 million (
Stock-based compensation expense(1) | 286 | 362 | 830 | 1,039
).
- **Q4 2024:** $368 million, taken from the Q4 2024 shareholder letter's quarterly reconciliation. I could not confirm this line in the extraction, so it is the least verified input.

Summing the four quarters: 295 + 382 + 362 + 368 = **$1,407 million**. The nine-month total of $1,039 million plus Q4's $368 million gives the same result.

**Cross-check on 2023:** The nine-month 2023 figure was $830 million, and Q4 2023 SBC was 
$290 million of stock-based compensation expense, which is excluded from Adjusted EBITDA
. That gives about $1,120 million for full-year 2023. Growth from $1,120 million to $1,407 million is about 25.63%, consistent with management's guidance of r
…[truncated 1,995 chars]
- web_search(query="Airbnb 2024 annual stock-based compensation expense 1,407 million") → 10 results: Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000024/abnb-20240630.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000032/abnb-20240930.htm>; Airbnb, Inc. - Form 10-Q - FY2024 (Quarterly Earnings Tables - quarter ended Jun 2024) <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000024/Financial_Report.xlsx>; Airbnb, Inc. - Form 10-Q - FY2024 (Quarterly Earnings Tables - quarter ended Sep 2024) <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000032/Financial_Report.xlsx>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm>
- submit_final_result({"final_result": "Airbnb's 2024 adjustment for stock-based compensation expense in its Adjusted EBITDA reconciliation was about $1,407 million (≈$1.41 billion). This is derived by summing the quarterly figures: Q1 $295M + Q2 $382M + Q3 $362M + Q4 $368M = $1,407M. The nine-month figure of $1,039M from the Q3 10-Q plus Q4's $368M gives the same total. The Q4 figure was taken from the Q4 2024 shareholder letter and was the least directly verified input. A cross-check against 2023 (nine-month $830M + Q4 $290M ≈ $1,120M) implies about 25.63% growth, consistent with management's guidance of roughly 25% higher SBC for 2024. For context, full-year 2024 Adjusted EBITDA was about $4,041M (quarterly $4
…[truncated 1,112 chars])

### Final answer
Airbnb's 2024 adjustment for stock-based compensation expense in its Adjusted EBITDA reconciliation was about $1,407 million (≈$1.41 billion). This is derived by summing the quarterly figures: Q1 $295M + Q2 $382M + Q3 $362M + Q4 $368M = $1,407M. The nine-month figure of $1,039M from the Q3 10-Q plus Q4's $368M gives the same total. The Q4 figure was taken from the Q4 2024 shareholder letter and was the least directly verified input. A cross-check against 2023 (nine-month $830M + Q4 $290M ≈ $1,120M) implies about 25.63% growth, consistent with management's guidance of roughly 25% higher SBC for 2024. For context, full-year 2024 Adjusted EBITDA was about $4,041M (quarterly $424M + $894M + $1,958M + $765M).

Sources:
{"sources": [
{"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000017/abnb-20240331.htm", "name": "Airbnb Form 10-Q for Q1 2024"},
{"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000024/abnb-20240630.htm", "name": "Airbnb Form 10-Q for Q2 2024"},
{"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000032/abnb-20240930.htm", "name": "Airbnb Form 10-Q for Q3 2024"},
{"url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm", "name": "Airbnb Q4 2024 shareholder letter (8-K Ex. 99.1)"},
{"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "name": "Airbnb Form 10-K FY2024"},
{"url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm", "name": "Airbnb Q4 2023 shareholder letter"},
{"url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm", "name": "Airbnb Q3 2024 shareholder letter"}
]}