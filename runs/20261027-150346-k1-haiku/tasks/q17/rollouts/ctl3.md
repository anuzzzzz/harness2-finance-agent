## Rollout `ctl3`
- outcome: submitted
- turns: 2; cost: $0.024; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Airbnb full year 2024 results revenue gross booking value") → 0 results: 
- edgar_search({"search_query": "Airbnb gross booking value annual revenue full year 2024 shareholder letter", "ciks": ["0001559720"], "start_date": "2023-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 11, "page": 1, "results": [{"form": "8-K", "file_date": "2024-08-06", "period_ending": "2024-08-06", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-194849", "document": "d831385dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm"}, {"form": "8-K", "file_date": "2025-02-13", "period_ending": "2025-02-13", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-25-026054", "document": "d915198dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm"}, {"form": "8-K", "file_date": "2024-11-07", "period_ending": "2024-11-07", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-253103", "document": "d886752dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm"}, {"form": "8-K", "file_date": "2024-05-08", "period_ending": "2024-05-08", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-134183", "document": "d813800dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm"}, {"form": "8-K", "file_date": "2024-02-13", "period_ending": "2024-02-13", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-033706", "document": "d646462dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm"}, {"form": "8-K", "file_date": 
  …[truncated 2,042 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm>; Airbnb, Inc. - Form DEF 14A - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524102960/d636281ddef14a.htm>; Airbnb, Inc. - Form PRE 14A - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524080883/d636281dpre14a.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm>
- web_search(query="Airbnb full year 2022 revenue $8.4 billion gross booking value 2022") → 10 results: Airbnb, Inc. - Form 8-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000119312522138654/d711122dex991.htm>; Airbnb, Inc. - Form 10-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm>; Airbnb, Inc. - Form 8-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000119312522210001/d353427dex991.htm>; Airbnb, Inc. - Form 8-K - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000119312522274904/d408297dex991.htm>; Airbnb Revenue and Booking Statistics (2026) <https://backlinko.com/airbnb-stats>
- submit_final_result({"final_result": "Airbnb's annual take rate (revenue ÷ gross booking value) rose slightly from FY2022 to FY2024, from about 13.29% to about 13.57%.\n\nInputs and calculations (unrounded ratios; figures are rounded in the sources):\n- FY2022: Revenue of about $8.4B (the 10-K says revenue grew to <cite index=\"12-1\">$8.4 billion</cite>) and GBV of about $63.2B (<cite index=\"16-6\">Gross Booking Value ('GBV') increased 35% YoY to $63.2 billion in 2022.</cite>). Take rate = 8.4 / 63.2 = 13.29%. This matches the third-party figure that <cite index=\"16-10\">the implied take rate (revenue divided by GBV) was 13.3%, which was up slightly from 12.8% during 2021.</cite>\n- FY2023: Revenue of about 
…[truncated 2,283 chars])

### Final answer
Airbnb's annual take rate (revenue ÷ gross booking value) rose slightly from FY2022 to FY2024, from about 13.29% to about 13.57%.

Inputs and calculations (unrounded ratios; figures are rounded in the sources):
- FY2022: Revenue of about $8.4B (the 10-K says revenue grew to <cite index="12-1">$8.4 billion</cite>) and GBV of about $63.2B (<cite index="16-6">Gross Booking Value ('GBV') increased 35% YoY to $63.2 billion in 2022.</cite>). Take rate = 8.4 / 63.2 = 13.29%. This matches the third-party figure that <cite index="16-10">the implied take rate (revenue divided by GBV) was 13.3%, which was up slightly from 12.8% during 2021.</cite>
- FY2023: Revenue of about $9.92B (<cite index="15-12">Airbnb generated $9.92 billion in revenue in 2023</cite>) and GBV of about $73.25B (<cite index="15-9">Airbnb processed $73.25 billion in gross booking value in 2023</cite>). Take rate = 9.92 / 73.25 = 13.54%.
- FY2024: Revenue of about $11.1B (<cite index="7-1">In 2024, revenue increased by 12% to $11.1 billion compared to 2023</cite>) and GBV of about $81.8B (<cite index="8-10">Gross bookings value was $81.8 billion for the full year, up 12%</cite>). Take rate = 11.1 / 81.8 = 13.57%. Using the more precise $81.78B GBV gives 13.57% as well.

Take rate by fiscal year:
- FY2022: 13.29%
- FY2023: 13.54%
- FY2024: 13.57%

Trend comment: The take rate edged up each year, with most of the gain coming in 2023 and only a marginal increase in 2024, suggesting it is stabilizing near 13.5% as revenue and GBV grow at similar rates.

Note: The FY2022 and FY2023 GBV values are rounded in the sources (the FY2023 figure is $73.3B in Airbnb's Q4 2023 letter), so the ratios are approximate to about ±0.02 percentage points.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm",
            "name": "Airbnb, Inc. Form 10-K for FY2022"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K for FY2024"
        },
        {
            "url": "https://www.thewolfofharcourtstreet.com/p/airbnb-headcount-down-5-revenue-up",
            "name": "The Wolf of Harcourt Street - Airbnb Full Year 2022 Earnings Analysis"
        },
        {
            "url": "https://backlinko.com/airbnb-stats",
            "name": "Backlinko - Airbnb Revenue and Booking Statistics"
        },
        {
            "url": "https://www.phocuswire.com/airbnb-earnings-q4-2024",
            "name": "PhocusWire - Airbnb to spend up to $250M on new businesses in 2025"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm",
            "name": "Airbnb Q4 2023 Shareholder Letter (Form 8-K)"
        }
    ]
}