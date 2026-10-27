## Rollout `inv1`
- outcome: submitted
- turns: 3; cost: $0.098; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "abnb_10k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_10k_2024. (452,800 characters)
  The data_storage currently contains the following keys:
  abnb_10k_2024
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm", "key": "abnb_8k_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_8k_2024. (54,854 characters)
  The data_storage currently contains the following keys:
  abnb_10k_2024
  abnb_8k_2024
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this document, find the \"Average Nights per Booking\" table by region (North America, EMEA, Latin America, Asia Pacific, Total) with the years 2024 and 2023 columns. Report the exact figure for Asia Pacific for 2024, the number of decimals shown, and whether the figure excludes Experiences. Document: {{abnb_10k_2024}}"})
  result: The document doesn't contain an "Average Nights per Booking" table. Its Geographic Mix section has tables for Nights and Experiences Booked, Gross Booking Value, and Revenue by region, but none for nights per booking. The only nights-per-booking figures are in a sentence after those tables:
  
  > "Our total Company average nights per booking, excluding experiences, was 3.8 in 2024 compared to 3.9 in 2023. Average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific."
  
  So:
  
  - **Asia Pacific, 2024:** 3.3 nights per booking, shown to one decimal place.
  - **Excludes experiences?** The explicit "excluding experiences" qualifier is attached only to the total company figure (3.8 in 2024). The regional sentence doesn't state it, though it appears in the same paragraph and likely uses the same definition. The document doesn't confirm this for Asia Pacific.
  - **2023 regional figure:** Not provided. Only the 2023 total (3.9) appears.
- retrieve_information({"prompt": "From this document, find any \"Average Nights per Booking\" figures by region (North America, EMEA, Latin America, Asia Pacific) for 2024 and 2023. Report the exact Asia Pacific figure for 2024 and its decimal precision. Document: {{abnb_8k_2024}}"})
  result: The document doesn't contain any "Average Nights per Booking" figures, for any region or year, so I can't report an Asia Pacific figure or its decimal precision.
  
  The closest regional data is Q4 2024 growth in Nights and Experiences Booked, which is qualitative:
  
  - **North America:** mid-single-digit growth
  - **EMEA:** low-double-digit growth
  - **Latin America:** low-20s growth
  - **Asia Pacific:** low-20s growth
  
  These are year-over-year growth rates, not average nights per booking, and the document gives no 2023 regional figures.
  
  The only per-night figure is Gross Booking Value per Night and Experience Booked (also labeled ADR), which is $158.13 for Q4 2024 globally. It is not broken out by region and is not a nights-per-booking measure.

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: 3.3 nights per booking for Asia Pacific in 2024** (as reported by Airbnb, one decimal place).\n\n**How I verified it**\n1. I opened Airbnb's FY2024 Form 10-K (https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm) and searched its Geographic Mix section. The regional tables cover nights and experiences booked, gross booking value and revenue. Nights per booking appears only in a sentence after those tables. That sentence says the total company average nights per booking, excluding experiences, was 3.8 in 2024 (3.9 in 2023). It then gives 2024 regional averages: 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America and 3.3 for As
…[truncated 1,887 chars])

### Final answer
**Answer: 3.3 nights per booking for Asia Pacific in 2024** (as reported by Airbnb, one decimal place).

**How I verified it**
1. I opened Airbnb's FY2024 Form 10-K (https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm) and searched its Geographic Mix section. The regional tables cover nights and experiences booked, gross booking value and revenue. Nights per booking appears only in a sentence after those tables. That sentence says the total company average nights per booking, excluding experiences, was 3.8 in 2024 (3.9 in 2023). It then gives 2024 regional averages: 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America and 3.3 for Asia Pacific.
2. I also opened the Q4 2024 earnings 8-K exhibit 99.1 (https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm). The extraction found no nights-per-booking figures in it, so it did not confirm the number. The 8-K does not contradict the 10-K.
3. The figures from the earlier search leads (Q4 2024 shareholder letter, and a third-party 3.33 for Asia Pacific) match the 10-K at one decimal. The 10-K reports 3.3, so I give that as the company figure. The third-party 3.33 is a more precise figure from a secondary source and is not a company-reported number.

**Caveats**
- The 10-K sentence explicitly says "excluding experiences" only for the company-wide 3.8 figure. The regional sentence does not state it, though it sits in the same paragraph and likely uses the same basis.
- The 2023 regional figure for Asia Pacific was not found in the documents I opened, so I cannot give a year-over-year comparison.
- I did not open the shareholder letter PDF directly. The 10-K text is the primary source used for the answer.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year 2024 (primary source, Geographic Mix section)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm",
            "name": "Airbnb, Inc. Form 8-K Exhibit 99.1, Q4 2024 results (checked; no nights-per-booking figures found)"
        },
        {
            "url": "https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf",
            "name": "Airbnb Q4 2024 shareholder letter (search excerpt only; not opened, consistent with the 10-K)"
        }
    ]
}