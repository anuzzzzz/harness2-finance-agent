## Rollout `ctl3`
- outcome: submitted
- turns: 2; cost: $0.012; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Airbnb 2024 annual report average nights per booking by region Asia Pacific") → 0 results: 
- edgar_search({"search_query": "Airbnb average nights per booking Asia Pacific 2024", "ciks": ["ABNB"], "start_date": "2025-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 2, "page": 1, "results": [{"form": "8-K", "file_date": "2025-02-13", "period_ending": "2025-02-13", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-25-026054", "document": "d915198dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm"}, {"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001559720-25-000010", "document": "abnb-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm"}]}

### Turn 2  (stop_reason=tool_use)
In 2024, Airbnb's average nights per booking in the Asia Pacific region was **3.3**.

Airbnb's Q4 2024 shareholder letter reports that 
average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific.
 The same letter says the 
total Company average nights per booking, excluding experiences, was 3.8 in 2024 compared to 3.9 in 2023.


A secondary source is consistent with this. Radical Storage reports the Asia Pacific figure as 
the shortest stay in Asia Pacific (3.33)
 in 2024, which rounds to 3.3. I did not check the figure against the 10-K filing itself, but the shareholder letter is Airbnb's own disclosure.

For context, Asia Pacific had the shortest average stay of any region in 2024, and the figure was flat relative to 2023. Airbnb's 2025 results, which are outside the 2024 question, show Asia Pacific at 3.3 again.
- web_search(query=null) → 10 results: Airbnb Statistics - Airbnb Facts, Stats, Trends & Data (2026) <https://www.wallstreetzen.com/stocks/us/nasdaq/abnb/statistics>; Airbnb, Inc. - Cloudfront.net <https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf>; Airbnb average nights per booking by region 2025| Statista <https://www.statista.com/statistics/1193597/airbnb-average-nights-per-booking-by-region-worldwide/>; Discover Latest Airbnb Statistics (2025) <https://analyzify.com/statsup/airbnb>; Airbnb Statistics: Revenue and Users <https://radicalstorage.com/travel/airbnb-statistics/>
- submit_final_result({"final_result": "Answer: Airbnb's average nights per booking in the Asia Pacific region in 2024 was 3.3 nights.\n\nReasoning and support:\n- Airbnb's Q4 2024 shareholder letter states that average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific (source: Airbnb Q4 2024 shareholder letter, https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf). The same letter gives the total company average of 3.8 in 2024 (excluding experiences), versus 3.9 in 2023.\n- A secondary source (Radical Storage) reports the Asia Pacific 2024 average as 3.33, which rounds to 3.3, and identifies Asia Pa
…[truncated 652 chars])

### Final answer
Answer: Airbnb's average nights per booking in the Asia Pacific region in 2024 was 3.3 nights.

Reasoning and support:
- Airbnb's Q4 2024 shareholder letter states that average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific (source: Airbnb Q4 2024 shareholder letter, https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf). The same letter gives the total company average of 3.8 in 2024 (excluding experiences), versus 3.9 in 2023.
- A secondary source (Radical Storage) reports the Asia Pacific 2024 average as 3.33, which rounds to 3.3, and identifies Asia Pacific as the region with the shortest average stay (https://radicalstorage.com/travel/airbnb-statistics/).
- I did not independently verify the figure in the FY2024 Form 10-K; the shareholder letter is Airbnb's own disclosure.

Sources:
{
    "sources": [
        {
            "url": "https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf",
            "name": "Airbnb Q4 2024 Shareholder Letter"
        },
        {
            "url": "https://radicalstorage.com/travel/airbnb-statistics/",
            "name": "Radical Storage - Airbnb Statistics"
        }
    ]
}