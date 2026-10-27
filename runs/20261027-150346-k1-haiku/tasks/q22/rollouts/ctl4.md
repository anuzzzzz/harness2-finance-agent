## Rollout `ctl4`
- outcome: submitted
- turns: 5; cost: $0.564; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Airbnb gross booking value nights and experiences booked annual report", "ciks": ["ABNB"], "form_types": ["10-K"], "start_date": "2023-01-01"})
  result: {"total_matching_documents": 3, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-25-000010", "document": "abnb-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm"}, {"form": "10-K", "file_date": "2023-02-17", "period_ending": "2022-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-23-000003", "document": "abnb-20221231.htm", "description": "FORM 10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm"}, {"form": "10-K", "file_date": "2024-02-16", "period_ending": "2023-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-24-000006", "document": "abnb-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "fy2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2024. (452,800 characters)
  The data_storage currently contains the following keys:
  fy2024
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm", "key": "fy2023"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2023. (624,096 characters)
  The data_storage currently contains the following keys:
  fy2024
  fy2023
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm", "key": "fy2022"})
  result: SUCCESS: The result has been saved to the data storage under the key: fy2022. (637,988 characters)
  The data_storage currently contains the following keys:
  fy2024
  fy2023
  fy2022
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K text, find the full-year Gross Booking Value (in $ billions or millions) and Nights and Experiences Booked (in millions) for the fiscal year covered by the filing, for the current year and prior year. Quote the exact figures from the key metrics table. Document: {{fy2024}}"})
  result: The key business metrics table in Item 7 (MD&A) reports the following for the fiscal year ended December 31, 2024 (in millions, except percentages):
  
  | Metric | 2023 (prior year) | 2024 (current year) | % Change |
  |---|---|---|---|
  | Nights and Experiences Booked | 448 | 492 | 10% |
  | Gross Booking Value | $73,252 | $81,784 | 12% |
  
  So for fiscal 2024:
  - **Gross Booking Value:** $81,784 million (about $81.8 billion), up from $73,252 million (about $73.3 billion) in 2023.
  - **Nights and Experiences Booked:** 492 million, up from 448 million in 2023.
- retrieve_information({"prompt": "From this Airbnb 10-K text, find the full-year Gross Booking Value (in $ billions or millions) and Nights and Experiences Booked (in millions) for the fiscal year covered by the filing, for the current year and prior year. Quote the exact figures from the key metrics table. Document: {{fy2023}}"})
  result: Here are the full-year figures from the Key Business Metrics table in the MD&A (Item 7) of Airbnb's 10-K for the fiscal year ended December 31, 2023:
  
  **Key business metrics table (in millions):**
  
  | Metric | 2022 | 2023 | % Change |
  |---|---|---|---|
  | Nights and Experiences Booked | 394 | 448 | 14% |
  | Gross Booking Value | $63,212 | $73,252 | 16% |
  
  **Summary:**
  
  - **Gross Booking Value:** $63,212 million (about $63.2 billion) for 2022 and $73,252 million (about $73.3 billion) for 2023.
  - **Nights and Experiences Booked:** 394 million for 2022 and 448 million for 2023.
  
  The text also states these figures in narrative form: "In 2023, we had 448.2 million Nights and Experiences Booked, a 14% increase from 393.7 million in 2022," and "In 2023, our GBV was $73.3 billion, a 16% increase from $63.2 billion in 2022."
- retrieve_information({"prompt": "From this Airbnb 10-K text, find the full-year Gross Booking Value (in $ billions or millions) and Nights and Experiences Booked (in millions) for the fiscal year covered by the filing, for the current year and prior year. Quote the exact figures from the key metrics table. Document: {{fy2022}}"})
  result: Here are the figures from the key business metrics table in Item 7 (MD&A, "Key Business Metrics"), for the fiscal year ended December 31, 2022 (current year) and December 31, 2021 (prior year):
  
  | Metric (in millions) | 2021 (prior year) | 2022 (current year) |
  |---|---|---|
  | Nights and Experiences Booked | 301 | 394 |
  | Gross Booking Value | $46,877 | $63,212 |
  
  Exact quoted figures from the table: "Nights and Experiences Booked 301 394" and "Gross Booking Value $46,877 $63,212" (in millions).
  
  Related figures from the same filing, for context:
  - The text describes 2022 Nights and Experiences Booked as 393.7 million (up 31% from 300.6 million in 2021).
  - GBV is described as $63.2 billion in 2022, a 35% increase from $46.9 billion in 2021.

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb 10-K text, quote the exact narrative sentences giving the precise number of Nights and Experiences Booked (with decimals, in millions) and Gross Booking Value for 2024 and 2023. Document: {{fy2024}}"})
  result: The filing doesn't state Nights and Experiences Booked or Gross Booking Value to one decimal place in millions. The only decimal figure is the 43.3 million increase in Nights and Experiences Booked. The levels appear as whole numbers in the key business metrics table.
  
  **Narrative (Item 7, 2024 Financial Highlights):**
  > "In 2024, revenue increased by 12% to $11.1 billion compared to 2023, primarily due to a 10% increase in Nights and Experiences Booked of 43.3 million combined with higher Average Daily Rate ("ADR") driving a 12% increase in Gross Booking Value of $8.5 billion."
  
  **Key business metrics table (Item 7, "Key Business Metrics"), introduced by:**
  > "The following table summarizes our key business metrics, for each period presented below (in millions, except percentages):"
  
  | Metric | 2023 | 2024 | % Change |
  |---|---|---|---|
  | Nights and Experiences Booked | 448 | 492 | 10% |
  | Gross Booking Value | $73,252 | $81,784 | 12% |
  
  So the 2023 and 2024 figures are 448 million and 492 million Nights and Experiences Booked, and $73,252 million and $81,784 million in GBV, respectively.
- retrieve_information({"prompt": "From this Airbnb 10-K text, quote the exact narrative sentences giving the precise number of Nights and Experiences Booked (with decimals, in millions) and Gross Booking Value for 2023 and 2022. Document: {{fy2023}}"})
  result: **Nights and Experiences Booked** (Item 7, Key Business Metrics):
  
  > "In 2023, we had 448.2 million Nights and Experiences Booked, a 14% increase from 393.7 million in 2022."
  
  **Gross Booking Value** (Item 7, Key Business Metrics):
  
  > "In 2023, our GBV was $73.3 billion, a 16% increase from $63.2 billion in 2022."
  
  The GBV narrative is rounded to one decimal place in billions. The key metrics table in the same section gives the unrounded figures in millions: $73,252 million for 2023 and $63,212 million for 2022.

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "Gross booking per room night = Gross Booking Value (GBV) ÷ Nights and Experiences Booked, using Airbnb's 10-K filings. I used the unrounded narrative figures where the filings give them, and the rounded key-metrics table otherwise.\n\nFY 2022: $160.56\nFY 2023: $163.44\nFY 2024: $166.40\n\nCalculations:\n- FY 2022: GBV $63,212M ÷ 393.7M nights = $160.56. The 10-K states <cite index=\"2-1\">the 2022 Nights and Experiences Booked as 393.7 million</cite> (the table rounds this to 394). GBV is $63,212M per the key metrics table.\n- FY 2023: GBV $73,252M ÷ 448.2M nights = $163.44. The 2023 10-K says <cite index=\"2-1\">\"In 2023, we had 448.2 million Nights and Experiences Booke
…[truncated 543 chars])

### Final answer
Gross booking per room night = Gross Booking Value (GBV) ÷ Nights and Experiences Booked, using Airbnb's 10-K filings. I used the unrounded narrative figures where the filings give them, and the rounded key-metrics table otherwise.

FY 2022: $160.56
FY 2023: $163.44
FY 2024: $166.40

Calculations:
- FY 2022: GBV $63,212M ÷ 393.7M nights = $160.56. The 10-K states <cite index="2-1">the 2022 Nights and Experiences Booked as 393.7 million</cite> (the table rounds this to 394). GBV is $63,212M per the key metrics table.
- FY 2023: GBV $73,252M ÷ 448.2M nights = $163.44. The 2023 10-K says <cite index="2-1">"In 2023, we had 448.2 million Nights and Experiences Booked, a 14% increase from 393.7 million in 2022."</cite>
- FY 2024: The 2024 10-K gives no decimal figure for nights. Its table shows 448 million (2023) and 492 million (2024) nights, and GBV of $81,784M. The filing also notes a <cite index="0-1">10% increase in Nights and Experiences Booked of 43.3 million</cite>, which implies 448.2M + 43.3M = 491.5M nights. Using 491.5M: $81,784M ÷ 491.5M = $166.40. Using the rounded table figure of 492M instead gives $166.23.

Sources: Airbnb Form 10-K for FY2024, FY2023, and FY2022 (SEC EDGAR).