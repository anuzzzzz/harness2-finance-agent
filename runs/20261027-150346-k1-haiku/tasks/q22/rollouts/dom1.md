## Rollout `dom1`
- outcome: submitted
- turns: 5; cost: $0.220; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "kpi_ratio_from_reported_metrics"})
  result: ---
  name: kpi_ratio_from_reported_metrics
  description: Compute a per-unit ratio (for example gross booking value per night, ARPU, revenue per unit) across several fiscal years from a company's reported Key Business Metrics table.
  ---
  ANALYTIC MOVE: calculate. Take numerator / denominator for each fiscal year from the company's own published KPI table. Result: one value per year, in the format the question prescribes.
  
  1. Locate the table. Key operating metrics sit in the 10-K MD&A under "Key Business Metrics", in millions. Each 10-K shows only two or three years, so FY2022-FY2024 needs the FY2024 10-K (2023 and 2024) and the FY2023 10-K (2022 and 2023). Open each 10-K and retrieve the table from the opened text. Do not use search snippets for any figure.
  2. Which precision is the headline. Use the figures as printed in the Key Business Metrics table for both numerator and denominator. Compute the ratio with those printed figures at full precision, and round only the final number. The MD&A narrative sometimes gives a one-decimal count (for example 393.7M). Mention it as a labelled alternate only if it was retrieved verbatim from an opened filing. Never build a figure by adding a stated change to another year, such as 448.2 + 43.3, and present it as a reported figure. A rounded count changes the second decimal, so show both the headline and the alternate and say which is which.
  3. Check units and definitions. GBV is in $ millions and nights in millions, so the ratio is in dollars. Check that the same metric definition applies in each year. If a later 10-K restates an earlier year, say so and use the latest filing for that year.
  4. Answer contract:
     - one line per year in the exact layout asked;
     - beneath it, a table with numerator, denominator, source filing and peri
  …[truncated 1,073 chars]

### Turn 2  (stop_reason=tool_use)
- edgar_search({"search_query": "Airbnb annual report Key Business Metrics Nights and Experiences Booked", "ciks": ["1559720"], "form_types": ["10-K"]})
  result: {"total_matching_documents": 5, "page": 1, "results": [{"form": "10-K", "file_date": "2021-02-26", "period_ending": "2020-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-21-000010", "document": "airbnb-10k.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972021000010/airbnb-10k.htm"}, {"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-25-000010", "document": "abnb-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm"}, {"form": "10-K", "file_date": "2023-02-17", "period_ending": "2022-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-23-000003", "document": "abnb-20221231.htm", "description": "FORM 10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm"}, {"form": "10-K", "file_date": "2022-02-25", "period_ending": "2021-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-22-000006", "document": "abnb-20211231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972022000006/abnb-20211231.htm"}, {"form": "10-K", "file_date": "2024-02-16", "period_ending": "2023-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-24-000006", "document": "abnb-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm"}]}

### Turn 3  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "fy2024_10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2024_10k. (452,800 characters)
  The data_storage currently contains the following keys:
  fy2024_10k
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm", "key": "fy2023_10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2023_10k. (624,096 characters)
  The data_storage currently contains the following keys:
  fy2024_10k
  fy2023_10k
  

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K text, find the \"Key Business Metrics\" table. Report the exact printed values for \"Nights and Experiences Booked\" (in millions) and \"Gross Booking Value\" (in $ millions) for every year shown. Also report any narrative sentence giving the nights and experiences booked total with one decimal. Text: {{fy2024_10k}}"})
  result: **Key Business Metrics table** (Item 7, MD&A, in millions, except percentages):
  
  | Metric | 2023 | 2024 | % Change |
  |---|---|---|---|
  | Nights and Experiences Booked | 448 | 492 | 10% |
  | Gross Booking Value | $73,252 | $81,784 | 12% |
  
  **Narrative sentence with one decimal:** The Financial Highlights section says: "In 2024, revenue increased by 12% to $11.1 billion compared to 2023, primarily due to a 10% increase in Nights and Experiences Booked of 43.3 million..."
  
  The 43.3 million is the year-over-year increase, not the 2024 total. The filing gives no one-decimal total for Nights and Experiences Booked. The table's 492 million is the only total, and it is printed as a whole number.
- retrieve_information({"prompt": "From this Airbnb 10-K text, find the \"Key Business Metrics\" table. Report the exact printed values for \"Nights and Experiences Booked\" (in millions) and \"Gross Booking Value\" (in $ millions) for every year shown. Also report any narrative sentence giving the nights and experiences booked total with one decimal. Text: {{fy2023_10k}}"})
  result: **Key Business Metrics table** (Item 7, "Key Business Metrics"; the table header reads "in millions"):
  
  | Metric | 2022 | 2023 | % Change |
  |---|---|---|---|
  | Nights and Experiences Booked | 394 | 448 | 14% |
  | Gross Booking Value | $63,212 | $73,252 | 16% |
  
  The table covers two years, 2022 and 2023. The GBV row is printed in $ millions, so $63,212 and $73,252 are in millions.
  
  **Narrative sentence with the one-decimal total:**
  "In 2023, we had 448.2 million Nights and Experiences Booked, a 14% increase from 393.7 million in 2022."

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "FY 2022: $160.44\nFY 2023: $163.51\nFY 2024: $166.23\n\nHeadline calculation (Key Business Metrics tables, in millions, GBV in $ millions / Nights and Experiences Booked in millions):\n\n| Fiscal year | Gross Booking Value ($M) | Nights & Experiences Booked (M) | Source filing | Unrounded quotient |\n|---|---|---|---|---|\n| FY 2022 | 63,212 | 394 | FY2023 10-K (2022 column; also in FY2022 10-K) | 160.4366 |\n| FY 2023 | 73,252 | 448 | FY2023 10-K (also FY2024 10-K 2023 column) | 163.5089 |\n| FY 2024 | 81,784 | 492 | FY2024 10-K | 166.2276 |\n\nBoth filings were opened and the table values were confirmed. No restatement of the 2022 or 2023 figures appeared between the fili
…[truncated 1,029 chars])

### Final answer
FY 2022: $160.44
FY 2023: $163.51
FY 2024: $166.23

Headline calculation (Key Business Metrics tables, in millions, GBV in $ millions / Nights and Experiences Booked in millions):

| Fiscal year | Gross Booking Value ($M) | Nights & Experiences Booked (M) | Source filing | Unrounded quotient |
|---|---|---|---|---|
| FY 2022 | 63,212 | 394 | FY2023 10-K (2022 column; also in FY2022 10-K) | 160.4366 |
| FY 2023 | 73,252 | 448 | FY2023 10-K (also FY2024 10-K 2023 column) | 163.5089 |
| FY 2024 | 81,784 | 492 | FY2024 10-K | 166.2276 |

Both filings were opened and the table values were confirmed. No restatement of the 2022 or 2023 figures appeared between the filings.

Alternate (narrative one-decimal counts, labelled as alternate, not the headline): FY 2022 = 63,212 / 393.7 = $160.56; FY 2023 = 73,252 / 448.2 = $163.44. The FY2023 10-K narrative states "448.2 million Nights and Experiences Booked" for 2023 and "393.7 million" for 2022. The FY2024 10-K gives no one-decimal 2024 total (only a 43.3M year-over-year increase), so no alternate is provided for FY 2024.

Per-night value rose each year, consistent with GBV growing faster than or in line with nights (GBV +16% vs. nights +14% in 2023; GBV +12% vs. nights +10% in 2024).

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb FY2024 Form 10-K (abnb-20241231.htm)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm",
            "name": "Airbnb FY2023 Form 10-K (abnb-20231231.htm)"
        }
    ]
}