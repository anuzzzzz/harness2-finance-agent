## Rollout `ctl4`
- outcome: submitted
- turns: 6; cost: $0.283; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Spirit Airlines operating statistics available seat miles load factor 2024 annual report", "ciks": ["SAVE"], "start_date": "2025-01-01", "end_date": "2025-04-07"})
  ERROR: ValueError: Unknown ticker 'SAVE'. Provide a numeric CIK instead.

### Turn 2  (stop_reason=tool_use)
- edgar_search({"search_query": "Spirit Airlines 10-K 2024 operating statistics available seat miles load factor", "start_date": "2025-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 17, "page": 1, "results": [{"form": "8-K", "file_date": "2025-01-28", "period_ending": "2025-01-28", "company": "JETBLUE AIRWAYS CORP  (JBLU)  (CIK 0001158463)", "ciks": ["0001158463"], "accession": "0001158463-25-000001", "document": "ex991-earningsreleaseq42024.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1158463/000115846325000001/ex991-earningsreleaseq42024.htm"}, {"form": "8-K", "file_date": "2025-02-07", "period_ending": "2025-02-07", "company": "Frontier Group Holdings, Inc.  (ULCC)  (CIK 0001670076)", "ciks": ["0001670076"], "accession": "0001670076-25-000009", "document": "frontier_earningsreleasexq.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1670076/000167007625000009/frontier_earningsreleasexq.htm"}, {"form": "ARS", "file_date": "2025-04-03", "period_ending": "2024-12-31", "company": "Frontier Group Holdings, Inc.  (ULCC)  (CIK 0001670076)", "ciks": ["0001670076"], "accession": "0001670076-25-000083", "document": "ars.pdf", "description": "ARS", "url": "https://www.sec.gov/Archives/edgar/data/1670076/000167007625000083/ars.pdf"}, {"form": "10-K", "file_date": "2025-02-18", "period_ending": "2024-12-31", "company": "Frontier Group Holdings, Inc.  (ULCC)  (CIK 0001670076)", "ciks": ["0001670076"], "accession": "0001670076-25-000041", "document": "fron-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1670076/000167007625000041/fron-20241231.htm"}, {"form": "10-K", "file_date": "2025-03-03", "period_ending": "2024-12-31", "company": "Allegiant Travel CO  (ALGT)  (CIK 0001362468)", "ciks": ["0001362468"], "accession": "0001362468-25-000008", "document": "algt-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archi
  …[truncated 4,376 chars]

### Turn 3  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm", "key": "spirit10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: spirit10k. (635,378 characters)
  The data_storage currently contains the following keys:
  spirit10k
  

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Spirit Airlines 10-K, list every operating KPI / operating statistic the company tracks and reports (e.g., Available Seat Miles, Revenue Passenger Miles, Load Factor, Average Fare, Yield, PRASM, TRASM, CASM, CASM-ex fuel, Average stage length, Aircraft utilization, Fuel gallons, Average fuel price, Departures, Block hours, Passengers flown, Average daily aircraft utilization, On-time performance, Full-time equivalent employees, etc.). For each, give the FY 2024 total/value as stated in the filing, and the exact table or section where it appears. Quote the table headings exactly. Text: {{spirit10k}}"})
  result: # Spirit Airlines FY2024 Form 10-K: Operating KPIs and Statistics
  
  Most of the operating statistics appear in one table in Item 7 (MD&A). Other KPIs appear in the Operating Revenues and Operating Expenses subsections, the fuel discussion, Items 1, 1A and 2, and the glossary.
  
  ## 1. Core Operating Statistics
  
  **Source:** Item 7, MD&A, "Comparative Operating Statistics." The table is headed "Twelve Months Ended December 31, Percent Change 20242023" and the first row is "Operating Statistics (unaudited) (A):". Footnote (A) refers to the "Glossary of Airline Terms" and footnote (B) covers the 21 aircraft held for sale.
  
  | KPI (row label as filed) | FY2024 | FY2023 | % Change |
  |---|---|---|---|
  | Average aircraft | 209.9 | 199.5 | 5.2% |
  | Aircraft at end of period (B) | 213 | 205 | 3.9% |
  | Average daily aircraft utilization (hours) | 9.9 | 11.1 | (10.8)% |
  | Departures | 288,180 | 297,900 | (3.3)% |
  | Passenger flight segments (PFSs) (thousands) | 44,180 | 44,105 | 0.2% |
  | Revenue passenger miles (RPMs) (thousands) | 43,671,009 | 45,243,787 | (3.5)% |
  | Available seat miles (ASMs) (thousands) | 53,017,948 | 55,665,561 | (4.8)% |
  | Load factor (%) | 82.4% | 81.3% | 1.1 pts |
  | Total revenue per passenger flight segment ($) | 111.21 | 121.58 | (8.5)% |
  | Average yield (cents) | 11.25 | 11.85 | (5.1)% |
  | TRASM (cents) | 9.27 | 9.63 | (3.7)% |
  | CASM (cents) | 11.35 | 10.52 | 7.9% |
  | Adjusted CASM (cents) | 10.76 | 10.33 | 4.2% |
  | Adjusted CASM ex-fuel (cents) | 7.97 | 7.06 | 12.9% |
  | Fuel gallons consumed (thousands) | 551,819 | 591,796 | (6.8)% |
  | Average fuel cost per gallon ($) | 2.

### Turn 5  (stop_reason=tool_use)
- retrieve_information({"prompt": "In this Spirit Airlines 10-K, find the \"Comparative Operating Statistics\" table in Item 7 MD&A. Give the complete list of every row label after \"Fuel gallons consumed (thousands)\" with their FY2024 and FY2023 values exactly as printed (including Average fuel cost per gallon, Full-time equivalent employees, and any others such as PRASM, CASM-ex, block hours, average stage length, on-time performance, etc.). Text: {{spirit10k}}"})
  result: Only one row follows "Fuel gallons consumed (thousands)" in the Comparative Operating Statistics table:
  
  | Row label | FY2024 | FY2023 | Percent Change |
  |---|---|---|---|
  | Average fuel cost per gallon ($) | 2.68 | 3.08 | (13.0)% |
  
  The other items you listed are not in this table. "Full-time equivalent employees," PRASM, CASM-ex, block hours, average stage length, and on-time performance do not appear in it. The table ends with the footnotes "(A) See 'Glossary of Airline Terms'" and "(B) Includes 21 aircraft recorded as assets held for sale."

### Turn 6  (stop_reason=tool_use)
- submit_final_result({"final_result": "Spirit Airlines' FY2024 operating statistics are in the \"Comparative Operating Statistics\" table in Item 7 (MD&A) of its Form 10-K for the year ended December 31, 2024, filed March 3, 2025. The table is labeled \"Operating Statistics (unaudited)\" and compares FY2024 with FY2023. Spirit's stock was trading under the ticker SAVEQ, reflecting its Chapter 11 status, when this filing was made.\n\nFY2024 operating KPIs and totals (FY2023 shown for reference):\n\n| KPI | FY2024 Total | FY2023 |\n|---|---|---|\n| Average aircraft | 209.9 | 199.5 |\n| Aircraft at end of period (includes 21 aircraft held for sale) | 213 | 205 |\n| Average daily aircraft utilization (hours) | 9.9 |
…[truncated 1,337 chars])

### Final answer
Spirit Airlines' FY2024 operating statistics are in the "Comparative Operating Statistics" table in Item 7 (MD&A) of its Form 10-K for the year ended December 31, 2024, filed March 3, 2025. The table is labeled "Operating Statistics (unaudited)" and compares FY2024 with FY2023. Spirit's stock was trading under the ticker SAVEQ, reflecting its Chapter 11 status, when this filing was made.

FY2024 operating KPIs and totals (FY2023 shown for reference):

| KPI | FY2024 Total | FY2023 |
|---|---|---|
| Average aircraft | 209.9 | 199.5 |
| Aircraft at end of period (includes 21 aircraft held for sale) | 213 | 205 |
| Average daily aircraft utilization (hours) | 9.9 | 11.1 |
| Departures | 288,180 | 297,900 |
| Passenger flight segments (thousands) | 44,180 | 44,105 |
| Revenue passenger miles (thousands) | 43,671,009 | 45,243,787 |
| Available seat miles (thousands) | 53,017,948 | 55,665,561 |
| Load factor (%) | 82.4% | 81.3% |
| Total revenue per passenger flight segment ($) | 111.21 | 121.58 |
| Average yield (cents) | 11.25 | 11.85 |
| TRASM (cents) | 9.27 | 9.63 |
| CASM (cents) | 11.35 | 10.52 |
| Adjusted CASM (cents) | 10.76 | 10.33 |
| Adjusted CASM ex-fuel (cents) | 7.97 | 7.06 |
| Fuel gallons consumed (thousands) | 551,819 | 591,796 |
| Average fuel cost per gallon ($) | 2.68 | 3.08 |

Notes: The table does not include full-time equivalent employees, PRASM, block hours, average stage length, or on-time performance. The "Operating Statistics" section is the only one I found that gives FY2024 totals in this format. I read the table from the filing text through an automated extraction, so the figures should be checked against the original document before use.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm",
            "name": "Spirit Airlines, Inc. Form 10-K for fiscal year ended December 31, 2024 (filed 2025-03-03)"
        }
    ]
}