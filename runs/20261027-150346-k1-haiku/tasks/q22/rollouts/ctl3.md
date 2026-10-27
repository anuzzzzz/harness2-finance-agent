## Rollout `ctl3`
- outcome: submitted
- turns: 6; cost: $0.655; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Airbnb gross booking value nights and experiences booked annual report", "ciks": ["0001559720"], "form_types": ["10-K"], "start_date": "2023-01-01"})
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
- retrieve_information({"prompt": "From this Airbnb 10-K, find the key business metrics: Gross Booking Value (in millions) and Nights and Experiences Booked (in millions) for the fiscal years covered in the table (current and prior years). Give exact figures as stated. Document: {{fy2024}}"})
  result: From the Key Business Metrics table in Item 7 (MD&A), in millions except percentages:
  
  | Metric | 2023 | 2024 | % Change |
  |---|---|---|---|
  | Gross Booking Value | $73,252 | $81,784 | 12% |
  | Nights and Experiences Booked | 448 | 492 | 10% |
  
  The filing presents only 2023 and 2024 in this table. It does not report these metrics for 2022 in this document.
- retrieve_information({"prompt": "From this Airbnb 10-K, find the key business metrics: Gross Booking Value (in millions) and Nights and Experiences Booked (in millions) for the fiscal years covered in the table (current and prior years). Give exact figures as stated. Document: {{fy2023}}"})
  result: From the Key Business Metrics table in Item 7 (MD&A) of Airbnb's 10-K for fiscal year 2023:
  
  | Metric | 2022 | 2023 | % Change |
  |---|---|---|---|
  | Nights and Experiences Booked (in millions) | 394 | 448 | 14% |
  | Gross Booking Value (in millions) | $63,212 | $73,252 | 16% |
  
  The narrative text gives the more precise Nights and Experiences Booked figures of 393.7 million (2022) and 448.2 million (2023).
- retrieve_information({"prompt": "From this Airbnb 10-K, find the key business metrics: Gross Booking Value (in millions) and Nights and Experiences Booked (in millions) for the fiscal years covered in the table (current and prior years). Give exact figures as stated. Document: {{fy2022}}"})
  result: Here are the key business metrics from the Key Business Metrics table in Item 7 (MD&A) of the Airbnb FY2022 10-K:
  
  | Metric (in millions) | 2021 | 2022 |
  |---|---|---|
  | Nights and Experiences Booked | 301 | 394 |
  | Gross Booking Value | $46,877 | $63,212 |
  
  The filing's narrative also states these figures as 393.7 million Nights and Experiences Booked in 2022 (up from 300.6 million in 2021) and GBV of $63.2 billion in 2022 (up from $46.9 billion in 2021), a 35% increase.

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "Find the exact (unrounded) figures for Nights and Experiences Booked in millions for 2022, 2023, and 2024 and Gross Booking Value in thousands/millions as stated in the narrative or footnotes (e.g., '491.8 million nights'). Document: {{fy2024}} Also check: {{fy2023}}"})
  result: Here are the figures for Nights and Experiences Booked and Gross Booking Value, as stated in the Airbnb 10-K documents provided.
  
  **Nights and Experiences Booked (millions)**
  
  | Year | Figure (as stated) | Source |
  |---|---|---|
  | 2022 | 393.7 million | FY2023 10-K, MD&A: "a 14% increase from 393.7 million in 2022" (table shows 394, rounded) |
  | 2023 | 448.2 million | FY2023 10-K, MD&A: "In 2023, we had 448.2 million Nights and Experiences Booked" (table shows 448) |
  | 2024 | 491.8 million (implied) | FY2024 10-K does not state the exact figure in narrative; the table shows 492. The FY2024 narrative says the 10% increase was "of 43.3 million," which implies 448.2 + 43.3 = 491.5 million. |
  
  Note on 2024: the FY2024 10-K only presents the rounded figure (492) in the key metrics table. The 43.3 million increase in the narrative, applied to the 2023 figure of 448.2 million, implies approximately 491.5 million. The exact unrounded 2024 figure is not stated in the document provided. The example you gave, "491.8 million nights," does not appear in these filings, so I cannot confirm it from them.
  
  **Gross Booking Value (in millions of USD)**
  
  | Year | Figure (as stated) | Source |
  |---|---|---|
  | 2022 | $63.2 billion (table: $63,212 million) | FY2023 10-K, MD&A: "a 16% increase from $63.2 billion in 2022" |
  | 2023 | $73.3 billion (table: $73,252 million) | FY2023 10-K, MD&A: "our GBV was $73.3 billion" |
  | 2024 | $81,784 million (table) / "$8.5 billion" increase | FY2024 10-K table shows $81,784 million; the narrative describes a 12% increase "of $8.5 billion" (which implies roughly $81.8 billion from $73.25 billion) |
  
  The FY2024 10-K gives the exact figure in the table as $81,784 million, which is the most precise value stated for 2024. The FY2023 10-K gives $63,212 million f
  …[truncated 83 chars]

### Turn 5  (stop_reason=tool_use)
- retrieve_information({"prompt": "Quote exactly every sentence in this Airbnb FY2024 10-K that mentions the number of Nights and Experiences Booked in 2024 (with decimal figures, e.g., 'million'). Document: {{fy2024}}"})
  result: Only one sentence in the document states a decimal figure for the number of Nights and Experiences Booked in 2024:
  
  "In 2024, revenue increased by 12% to $11.1 billion compared to 2023, primarily due to a 10% increase in Nights and Experiences Booked of 43.3 million combined with higher Average Daily Rate (“ADR”) driving a 12% increase in Gross Booking Value of $8.5 billion."
  
  The key business metrics table also reports 2024 Nights and Experiences Booked (492 million), but those figures are whole numbers, so I excluded them. The sentence "Our total Company average nights per booking, excluding experiences, was 3.8 in 2024" has a decimal, but it refers to nights per booking, not the total number of Nights and Experiences Booked, so I excluded it too.

### Turn 6  (stop_reason=tool_use)
- submit_final_result({"final_result": "FY 2022: $160.44\nFY 2023: $163.51\nFY 2024: $166.23\n\nMethod: Gross booking value (GBV) divided by Nights and Experiences Booked, using the Key Business Metrics table figures in Airbnb's 10-K filings (both in millions, so the units cancel to $ per night/experience):\n- FY2022: GBV $63,212M ÷ 394M nights and experiences = $160.44. The FY2023 10-K shows 2022 GBV of $63,212M and 394M nights (the FY2022 10-K shows the same 2022 values).\n- FY2023: GBV $73,252M ÷ 448M = $163.51. Both the FY2023 and FY2024 10-Ks show these 2023 figures.\n- FY2024: GBV $81,784M ÷ 492M = $166.23. The FY2024 10-K shows these figures.\n\nCaveat: the 10-K tables round nights to whole millions. The n
…[truncated 1,004 chars])

### Final answer
FY 2022: $160.44
FY 2023: $163.51
FY 2024: $166.23

Method: Gross booking value (GBV) divided by Nights and Experiences Booked, using the Key Business Metrics table figures in Airbnb's 10-K filings (both in millions, so the units cancel to $ per night/experience):
- FY2022: GBV $63,212M ÷ 394M nights and experiences = $160.44. The FY2023 10-K shows 2022 GBV of $63,212M and 394M nights (the FY2022 10-K shows the same 2022 values).
- FY2023: GBV $73,252M ÷ 448M = $163.51. Both the FY2023 and FY2024 10-Ks show these 2023 figures.
- FY2024: GBV $81,784M ÷ 492M = $166.23. The FY2024 10-K shows these figures.

Caveat: the 10-K tables round nights to whole millions. The narrative gives more precise counts: 393.7M (2022) and 448.2M (2023). The FY2024 narrative implies about 491.5M for 2024 (448.2 + 43.3). Using those unrounded counts gives roughly $160.56 (FY2022), $163.44 (FY2023), and $166.40 (FY2024). The answer above uses the table figures as reported.

Sources: Airbnb 10-K filings for FY2024 (filed 2025-02-13), FY2023 (filed 2024-02-16), and FY2022 (filed 2023-02-17).

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb FY2024 Form 10-K"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm",
            "name": "Airbnb FY2023 Form 10-K"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm",
            "name": "Airbnb FY2022 Form 10-K"
        }
    ]
}