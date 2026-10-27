## Rollout `ctl4`
- outcome: submitted
- turns: 4; cost: $0.118; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Airbnb full year 2024 results gross booking value revenue") → 0 results: 
- edgar_search({"search_query": "Airbnb annual gross booking value revenue 2024 10-K", "ciks": ["0001559720"], "top_n_results": 5})
  result: {"total_matching_documents": 29, "page": 1, "results": [{"form": "8-K", "file_date": "2024-08-06", "period_ending": "2024-08-06", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-194849", "document": "d831385dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm"}, {"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-25-000010", "document": "abnb-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm"}, {"form": "8-K", "file_date": "2024-11-07", "period_ending": "2024-11-07", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-253103", "document": "d886752dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm"}, {"form": "10-Q", "file_date": "2024-05-08", "period_ending": "2024-03-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-24-000017", "document": "abnb-20240331.htm", "description": "10-Q", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000017/abnb-20240331.htm"}, {"form": "8-K", "file_date": "2025-02-13", "period_ending": "2025-02-13", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-25-026054", "document": "d915198dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm"}]}

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm>; Airbnb, Inc. - Form DEF 14A - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524102960/d636281ddef14a.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm>; Airbnb, Inc. - Form PRE 14A - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524080883/d636281dpre14a.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb10k. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb10k
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K, extract the exact figures in millions (or billions) for Revenue and Gross Booking Value for fiscal years 2024, 2023, and 2022 (as stated in the Key Business Metrics / Results of Operations tables). Quote the exact table values for each year. Text: {{abnb10k}}"})
  result: **Revenue and Gross Booking Value (GBV), in millions, as stated in the 10-K**
  
  | Fiscal Year | Revenue | Gross Booking Value |
  |---|---|---|
  | 2024 | $11,102 | $81,784 |
  | 2023 | $9,917 | $73,252 |
  | 2022 | $8,399 | Not disclosed in this filing |
  
  **Sources:**
  - **Revenue, 2024 and 2023:** Results of Operations table ("Revenue $9,917 100 % $11,102 100 %") and the Adjusted EBITDA reconciliation.
  - **Revenue, 2022:** Consolidated Statements of Operations ("Revenue $8,399 $9,917 $11,102"). The Results of Operations table covers only 2023 and 2024.
  - **GBV, 2024 and 2023:** Key Business Metrics table ("Gross Booking Value $73,252 $81,784 12 %").
  - **GBV, 2022:** The filing does not report it. Item 7 states that discussion of 2022 items "are not included in this Form 10-K" and refers readers to the FY2023 10-K.

### Turn 4  (stop_reason=tool_use)
- web_search(query="Airbnb 2022 full year gross booking value $62 billion revenue $8.4 billion") → 10 results: Airbnb, Inc. - Form 8-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000119312522210001/d353427dex991.htm>; Airbnb, Inc. - Form 10-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm>; Airbnb, Inc. - Form 8-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000119312522138654/d711122dex991.htm>; Airbnb, Inc. - Form 8-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000119312522274904/d408297dex991.htm>; Airbnb Revenue and Booking Statistics (2026) <https://backlinko.com/airbnb-stats>
- submit_final_result({"final_result": "Airbnb take rate (Revenue ÷ Gross Booking Value), FY2022–FY2024:\n\n- FY2022: 13.29% ($8,399M revenue ÷ $63.2B GBV)\n- FY2023: 13.54% ($9,917M ÷ $73,252M)\n- FY2024: 13.57% ($11,102M ÷ $81,784M)\n\nTrend comment: The take rate rose modestly from about 13.29% in 2022 to about 13.54% in 2023 and 13.57% in 2024, so it has been broadly stable with a slight upward drift that flattened in 2024.\n\nInputs and method:\n- Revenue: <cite index=\"20-1\">Revenue of $8.4 billion grew 40% year over year (46% ex-FX).</cite> The FY2024 10-K's consolidated statements show revenue of $8,399M (2022), $9,917M (2023), and $11,102M (2024). The 2024 revenue was <cite index=\"7-1\">$11.1 billion c
…[truncated 827 chars])

### Final answer
Airbnb take rate (Revenue ÷ Gross Booking Value), FY2022–FY2024:

- FY2022: 13.29% ($8,399M revenue ÷ $63.2B GBV)
- FY2023: 13.54% ($9,917M ÷ $73,252M)
- FY2024: 13.57% ($11,102M ÷ $81,784M)

Trend comment: The take rate rose modestly from about 13.29% in 2022 to about 13.54% in 2023 and 13.57% in 2024, so it has been broadly stable with a slight upward drift that flattened in 2024.

Inputs and method:
- Revenue: <cite index="20-1">Revenue of $8.4 billion grew 40% year over year (46% ex-FX).</cite> The FY2024 10-K's consolidated statements show revenue of $8,399M (2022), $9,917M (2023), and $11,102M (2024). The 2024 revenue was <cite index="7-1">$11.1 billion compared to 2023, primarily due to a 10% increase in Nights and Experiences Booked</cite>.
- GBV: For 2022, the FY2022 10-K states that <cite index="12-2">Gross Booking Value ("GBV") and revenue were $63.2 billion and $8.4 billion, respectively</cite>. The FY2024 10-K Key Business Metrics table gives GBV of $73,252M (2023) and $81,784M (2024), a 12% increase. The 2024 figure matches reporting that <cite index="8-10">gross bookings value was $81.8 billion for the full year, up 12%</cite>.
- Calculations: 8,399 / 63,200 = 13.29%; 9,917 / 73,252 = 13.54%; 11,102 / 81,784 = 13.57%. The 2022 figure uses the rounded $63.2B GBV, so it is accurate only to about ±0.02 percentage points.

Note: The 2022 GBV is only available rounded to $63.2 billion in the sources I found, so the 2022 take rate is an approximation.