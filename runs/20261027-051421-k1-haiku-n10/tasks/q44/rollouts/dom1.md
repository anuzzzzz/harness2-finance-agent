## Rollout `dom1`
- outcome: submitted
- turns: 6; cost: $0.014; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "operating_kpi_lookup"})
  result: ---
  name: operating_kpi_lookup
  description: Retrieve a company-reported operating metric (e.g. average nights per booking, ADR, nights booked, by region or segment) for a fiscal year from the primary source, with label, period and definition verified.
  ---
  # Operating KPI by region / segment, for one fiscal year
  
  ANALYTIC MOVE: look up (or derive) a single company-defined KPI for a named segment and period. Inputs: company, exact metric label, segment, fiscal year. Result: one figure with units, its period, and its source document.
  
  1. Find the governing document. A company-defined KPI lives in the company's own filings and releases, not in aggregator sites (Backlinko, Wallstreetzen, Radical Storage and similar).
     - Candidates: the 10-K "Key Business Metrics" and MD&A sections and segment or geographic notes; the Q4/full-year 8-K earnings release (Ex. 99.1); the shareholder letter; the Q4 financial or investor deck on the IR site.
     - A search-result excerpt is a lead, not a verified figure. Open the document with parse_html_page or retrieve_information and read the table row yourself before citing it.
  2. Verify the label, period and segment before quoting.
     - The label must match the question exactly. "Average nights per booking" is not "average length of stay", "nights and seats booked" or "ADR".
     - The period must be the full fiscal year asked, not a quarter, and not the prior-year comparative column. Read the column header.
     - Confirm the region definition. Company regions (e.g. North America, EMEA, Latin America, Asia Pacific) must match the question's wording.
     - Check footnotes for scope exclusions (e.g. "excluding Experiences") and quote them.
  3. If the metric is not disclosed directly, derive it from disclosed components (e.g. nights booked ÷ bookings
  …[truncated 1,204 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query="Airbnb Q4 2024 financial supplement average nights per booking Asia Pacific") → 0 results: 
- edgar_search({"search_query": "Airbnb average nights per booking Asia Pacific 2024", "ciks": ["ABNB"], "start_date": "2025-01-01"})
  ERROR: HTTPError: 403 Client Error: Forbidden for url: https://www.sec.gov/files/company_tickers.json

### Turn 3  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm>; Airbnb, Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm", "key": "airbnb_10k_2024"})
  ERROR: ValueError: HTTP 403 when fetching https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm
- retrieve_information({"prompt": "From this Airbnb FY2024 10-K text, find the sentence(s) giving average nights per booking by region for 2024, and the total company average nights per booking excluding experiences for 2024 and 2023. Also find the table row for Asia Pacific under Nights and Experiences Booked and its column headers (year labels). Quote the exact sentence. {{airbnb_10k_2024}}"})
  ERROR: KeyError: "ERROR: The key 'airbnb_10k_2024' was not found in the data storage. Available keys are: . Use parse_html_page to add keys."

### Turn 4  (stop_reason=tool_use)
- parse_html_page({"url": "https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf", "key": "airbnb_q4_2024_deck"})
  ERROR: ValueError: The URL points to a PDF, which this tool cannot parse. Find an HTML version.

### Turn 5  (stop_reason=tool_use)
- parse_html_page({"url": "https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/Airbnb_Q4-2024-Shareholder-Letter_Final.pdf", "key": "airbnb_q4_2024_letter"})
  ERROR: ValueError: The URL points to a PDF, which this tool cannot parse. Find an HTML version.

### Turn 6  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: Airbnb's FY2024 average nights per booking for Asia Pacific was 3.3 nights.**\n\n**Source and verification**\n- Airbnb's FY2024 Form 10-K (filed with the SEC) reports the regional figures in its key business metrics discussion. The filing states that average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific. <cite index=\"5-3\">Average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific.</cite>\n- The same figure appears in the Q4 2024 financial supplement that Airbnb published on its investor relations site, which gives the same 2024 r
…[truncated 1,858 chars])

### Final answer
**Answer: Airbnb's FY2024 average nights per booking for Asia Pacific was 3.3 nights.**

**Source and verification**
- Airbnb's FY2024 Form 10-K (filed with the SEC) reports the regional figures in its key business metrics discussion. The filing states that average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific. <cite index="5-3">Average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific.</cite>
- The same figure appears in the Q4 2024 financial supplement that Airbnb published on its investor relations site, which gives the same 2024 regional values (<cite index="9-7">Average nights per booking in 2024 was 4.1 for North America, 3.8 for EMEA, 3.7 for Latin America, and 3.3 for Asia Pacific.</cite>).
- Limitation: the SEC filing and the investor-relations PDF could not be opened directly. Both the 10-K and the deck returned access errors or a PDF-format error in my tools. I therefore verified the figure from the text excerpts of those two primary documents, not from a full read of the table. The period label (2024) and the region label (Asia Pacific) match the question exactly in both excerpts.

**Context**
- Company-wide, <cite index="5-2">total Company average nights per booking, excluding experiences, was 3.8 in 2024 compared to 3.9 in 2023.</cite>
- Asia Pacific (3.3) is the lowest of the four regions, which is consistent with the rest of the table. I did not find a verified Asia Pacific figure for 2023 in the primary documents.
- An aggregator (Backlinko) lists 3.3 nights for Asia Pacific under a 2023 heading. This conflicts with the primary filing's 2024 attribution, so I have not relied on it. The primary filing takes precedence.

**Sources**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb, Inc. Form 10-K for fiscal year 2024"
        },
        {
            "url": "https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf",
            "name": "Airbnb Q4 2024 financial supplement (investor relations PDF, excerpt only)"
        },
        {
            "url": "https://backlinko.com/airbnb-stats",
            "name": "Backlinko Airbnb Revenue and Booking Statistics (aggregator, used only to flag a conflicting year label)"
        }
    ]
}