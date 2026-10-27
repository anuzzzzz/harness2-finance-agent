## Rollout `static1`
- outcome: submitted
- turns: 5; cost: $0.443; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Airbnb 10-K gross booking value nights and experiences booked", "ciks": ["ABNB"], "form_types": ["10-K"], "start_date": "2023-01-01", "end_date": "2025-04-07"})
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
- retrieve_information({"prompt": "From this Airbnb 10-K, find the key metrics: Gross Booking Value (in billions, for the fiscal year) and Nights and Experiences Booked (in millions) for the fiscal year ended December 31. Give exact figures as stated in the document, including units, and the exact sentence or table row where they appear. Document: {{fy2024}}"})
  result: ## Key Metrics for Fiscal Year 2024 (Ended December 31, 2024)
  
  | Metric | FY2024 Value | Units in Document |
  |---|---|---|
  | Gross Booking Value (GBV) | **$81,784** | Millions of USD (≈ **$81.8 billion**) |
  | Nights and Experiences Booked | **492** | Millions |
  
  ### Source Table Rows
  
  The Key Business Metrics table in Item 7 (MD&A) reads, in millions except percentages:
  
  > Nights and Experiences Booked 448 492 10 %
  > Gross Booking Value $73,252 $81,784 12 %
  
  ### Supporting Sentence
  
  The 2024 Financial Highlights section states:
  
  > "In 2024, revenue increased by 12% to $11.1 billion compared to 2023, primarily due to a 10% increase in Nights and Experiences Booked of 43.3 million combined with higher Average Daily Rate ("ADR") driving a 12% increase in Gross Booking Value of $8.5 billion."
  
  ### Notes on Interpretation
  
  - **GBV:** The document reports the total in millions ($81,784 million). The $8.5 billion figure in the highlights is the *year-over-year increase* (from $73,252 million), not the full-year total.
  - **Nights and Experiences Booked:** The 492 million figure is the total for 2024. The "43.3 million" in the highlights is the year-over-year increase, not the total.
- retrieve_information({"prompt": "From this Airbnb 10-K, find the key metrics: Gross Booking Value (in billions, for the fiscal year) and Nights and Experiences Booked (in millions) for the fiscal year ended December 31. Give exact figures as stated in the document, including units, and the exact sentence or table row where they appear. Document: {{fy2023}}"})
  result: **Fiscal year ended December 31, 2023**
  
  | Metric | FY2023 Value (as stated) | Source location |
  |---|---|---|
  | **Gross Booking Value (GBV)** | **$73.3 billion** | Item 7, Key Business Metrics: "In 2023, our GBV was $73.3 billion, a 16% increase from $63.2 billion in 2022." |
  | **Nights and Experiences Booked** | **448.2 million** | Item 7, Key Business Metrics: "In 2023, we had 448.2 million Nights and Experiences Booked, a 14% increase from 393.7 million in 2022." |
  
  **Supporting table rows**
  
  - Key business metrics table (in millions): "Nights and Experiences Booked: 394 | 448 | 14 %" and "Gross Booking Value: $63,212 | $73,252 | 16 %". The table gives GBV in millions, so the FY2023 figure is $73,252 million, which rounds to $73.3 billion.
  - Geographic Mix table: GBV total is $73,252 million (51% North America in 2022 vs. 48% in 2023, etc.), and Nights and Experiences Booked total is 448 million.
  
  **Note on the 2023 Financial Highlights section:** It says "a 14% increase in Nights and Experiences Booked of 54.5 million combined with higher average daily rates driving a 16% increase in Gross Booking Value of $10.0 billion." The $10.0 billion there is the year-over-year increase in GBV, not the total for 2023. The total is $73.3 billion.
- retrieve_information({"prompt": "From this Airbnb 10-K, find the key metrics: Gross Booking Value (in billions, for the fiscal year) and Nights and Experiences Booked (in millions) for the fiscal year ended December 31. Give exact figures as stated in the document, including units, and the exact sentence or table row where they appear. Document: {{fy2022}}"})
  result: **Fiscal year ended December 31, 2022**
  
  **Gross Booking Value: $63.2 billion**
  - Key Business Metrics table (Item 7, in millions): "Gross Booking Value $46,877 $63,212"
  - Key Business Metrics narrative: "In 2022, our GBV was $63.2 billion, a 35% increase from $46.9 billion in 2021."
  
  **Nights and Experiences Booked: 393.7 million**
  - Key Business Metrics table (Item 7, in millions): "Nights and Experiences Booked 301 394"
  - Key Business Metrics narrative: "In 2022, we had 393.7 million Nights and Experiences Booked, a 31% increase from 300.6 million in 2021."
  
  The table rounds Nights and Experiences Booked to 394 million, while the narrative gives 393.7 million. The table's GBV figure is $63,212 million, which matches the $63.2 billion stated in the text.

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "Quote the exact narrative sentence in this Airbnb FY2024 10-K giving the number of Nights and Experiences Booked in 2024 with decimal precision (e.g., 'In 2024, we had X million Nights and Experiences Booked'). Also quote the exact GBV narrative sentence. Document: {{fy2024}}"})
  result: The document has no sentence stating the total 2024 Nights and Experiences Booked in the form you describe ("In 2024, we had X million..."). The closest narrative sentence gives the year-over-year increase, not the total:
  
  > "In 2024, revenue increased by 12% to $11.1 billion compared to 2023, primarily due to a 10% increase in Nights and Experiences Booked of 43.3 million combined with higher Average Daily Rate ("ADR") driving a 12% increase in Gross Booking Value of $8.5 billion."
  
  The total appears only in the key business metrics table, in whole millions with no decimals: Nights and Experiences Booked was 448 million in 2023 and 492 million in 2024.
  
  For GBV, the document has no narrative sentence stating the 2024 total. The only narrative figure is the increase quoted above ($8.5 billion, a 12% increase). The total is in the same table: Gross Booking Value was $73,252 million in 2023 and $81,784 million in 2024.

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "Method: gross booking value (GBV) ÷ Nights and Experiences Booked, using the Key Business Metrics in Airbnb's 10-K filings (GBV in $ millions; nights in millions, so the units cancel to $ per night).\n\nFY 2022: $160.56\n- GBV: $63,212 million (the FY2022 10-K states \"$63.2 billion\"); Nights and Experiences Booked: 393.7 million (narrative). 63,212 ÷ 393.7 = 160.56\n\nFY 2023: $163.44\n- GBV: $73,252 million (\"$73.3 billion\"); Nights and Experiences Booked: 448.2 million (FY2023 10-K narrative). 73,252 ÷ 448.2 = 163.44\n\nFY 2024: $166.23\n- GBV: $81,784 million; Nights and Experiences Booked: 492 million (the FY2024 10-K gives only the whole-million table figure). 81,7
…[truncated 1,022 chars])

### Final answer
Method: gross booking value (GBV) ÷ Nights and Experiences Booked, using the Key Business Metrics in Airbnb's 10-K filings (GBV in $ millions; nights in millions, so the units cancel to $ per night).

FY 2022: $160.56
- GBV: $63,212 million (the FY2022 10-K states "$63.2 billion"); Nights and Experiences Booked: 393.7 million (narrative). 63,212 ÷ 393.7 = 160.56

FY 2023: $163.44
- GBV: $73,252 million ("$73.3 billion"); Nights and Experiences Booked: 448.2 million (FY2023 10-K narrative). 73,252 ÷ 448.2 = 163.44

FY 2024: $166.23
- GBV: $81,784 million; Nights and Experiences Booked: 492 million (the FY2024 10-K gives only the whole-million table figure). 81,784 ÷ 492 = 166.23

Formatted answer:
FY 2022: $160.56
FY 2023: $163.44
FY 2024: $166.23

Caveat: the FY2024 10-K reports nights only in whole millions (492), and it states a year-over-year increase of 43.3 million from 2023. Using 448.2 + 43.3 = 491.5 million instead would give about $166.40 for FY2024.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year ended December 31, 2024"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year ended December 31, 2023"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year ended December 31, 2022"
        }
    ]
}