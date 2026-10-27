## Rollout `base1`
- outcome: submitted
- turns: 2; cost: $0.012; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Airbnb 2024 annual report average nights per booking by region Asia Pacific") → 0 results: 
- edgar_search({"search_query": "Airbnb average nights per booking Asia Pacific 2024", "ciks": ["ABNB"], "start_date": "2025-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 2, "page": 1, "results": [{"form": "8-K", "file_date": "2025-02-13", "period_ending": "2025-02-13", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-25-026054", "document": "d915198dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm"}, {"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-25-000010", "document": "abnb-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Airbnb Statistics - Airbnb Facts, Stats, Trends & Data (2026) <https://www.wallstreetzen.com/stocks/us/nasdaq/abnb/statistics>; Airbnb average nights per booking by region 2025| Statista <https://www.statista.com/statistics/1193597/airbnb-average-nights-per-booking-by-region-worldwide/>; Discover Latest Airbnb Statistics (2025) <https://analyzify.com/statsup/airbnb>; Airbnb, Inc. - Cloudfront.net <https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf>; Airbnb Statistics: Revenue and Users <https://radicalstorage.com/travel/airbnb-statistics/>
- submit_final_result({"final_result": "**Answer: Airbnb's Average Nights per Booking in the Asia Pacific region for 2024 was 3.3.**\n\n**Reasoning and support:**\n- Airbnb's Q4 2024 shareholder letter, published in February 2025, gives regional figures for 2024. It reports North America at 4.1, EMEA at 3.8, Latin America at 3.7, and Asia Pacific at 3.3 nights per booking. <cite index=\"4-7\">Average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific.</cite>\n- The same letter gives the company-wide figure. Excluding experiences, the blended average was 3.8 in 2024, down from 3.9 in 2023 (<cite index=\"4-6\">Our total Company average nights per book
…[truncated 1,247 chars])

### Final answer
**Answer: Airbnb's Average Nights per Booking in the Asia Pacific region for 2024 was 3.3.**

**Reasoning and support:**
- Airbnb's Q4 2024 shareholder letter, published in February 2025, gives regional figures for 2024. It reports North America at 4.1, EMEA at 3.8, Latin America at 3.7, and Asia Pacific at 3.3 nights per booking. <cite index="4-7">Average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific.</cite>
- The same letter gives the company-wide figure. Excluding experiences, the blended average was 3.8 in 2024, down from 3.9 in 2023 (<cite index="4-6">Our total Company average nights per booking, excluding experiences, was 3.8 in 2024 compared to 3.9 in 2023.</cite>).
- Third-party data is consistent with this. One compiled table lists Asia Pacific at 3.3 for 2024, and that same dataset shows the 2023 figure at 3.3 as well (<cite index="5-6">Asia Pacific | 2.8 | 2.8 | 2.7 | 3.2 | 3.3 | 3.3</cite>, covering 2019 through 2024).
- Asia Pacific had the shortest average stay among regions. <cite index="5-5">The average night stay varies by region, with North America being home to the longest average Airbnb night stay (4.14) compared to the shortest stay in Asia Pacific (3.33) in 2024.</cite> The 3.33 figure is unrounded, and the company-reported figure is 3.3.

I used only information available as of April 7, 2025. The company's own disclosure is the primary source for the answer.

{
    "sources": [
        {
            "url": "https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf",
            "name": "Airbnb, Inc. Q4 2024 Shareholder Letter"
        },
        {
            "url": "https://radicalstorage.com/travel/airbnb-statistics/",
            "name": "Radical Storage - Airbnb Statistics: Revenue and Users"
        }
    ]
}