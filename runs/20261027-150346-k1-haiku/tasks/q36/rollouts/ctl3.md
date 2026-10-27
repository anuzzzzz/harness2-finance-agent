## Rollout `ctl3`
- outcome: submitted
- turns: 3; cost: $0.014; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Rocket Companies to acquire Redfin per share enterprise value") → 0 results: 
- edgar_search({"search_query": "Rocket Redfin merger agreement per share consideration", "start_date": "2025-03-01", "top_n_results": 5})
  result: {"total_matching_documents": 41, "page": 1, "results": [{"form": "S-4", "file_date": "2025-04-07", "period_ending": null, "company": "Rocket Companies, Inc.  (RKT)  (CIK 0001805284)", "ciks": ["0001805284"], "accession": "0001104659-25-032694", "document": "tm2511408-1_s4.htm", "description": "S-4", "url": "https://www.sec.gov/Archives/edgar/data/1805284/000110465925032694/tm2511408-1_s4.htm"}, {"form": "425", "file_date": "2025-03-10", "period_ending": null, "company": "Redfin Corp  (RDFN)  (CIK 0001382821)", "ciks": ["0001382821", "0001805284"], "accession": "0000950142-25-000697", "document": "eh250601348_425.htm", "description": "FORM 425", "url": "https://www.sec.gov/Archives/edgar/data/1382821/000095014225000697/eh250601348_425.htm"}, {"form": "8-K", "file_date": "2025-03-10", "period_ending": "2025-03-09", "company": "Rocket Companies, Inc.  (RKT)  (CIK 0001805284)", "ciks": ["0001805284"], "accession": "0000950142-25-000696", "document": "eh250601250_8k.htm", "description": "FORM 8-K", "url": "https://www.sec.gov/Archives/edgar/data/1805284/000095014225000696/eh250601250_8k.htm"}, {"form": "8-K", "file_date": "2025-03-10", "period_ending": "2025-03-09", "company": "Redfin Corp  (RDFN)  (CIK 0001382821)", "ciks": ["0001382821"], "accession": "0001628280-25-011457", "document": "rdfn-20250309.htm", "description": "8-K", "url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025011457/rdfn-20250309.htm"}, {"form": "425", "file_date": "2025-03-26", "period_ending": null, "company": "Redfin Corp  (RDFN)  (CIK 0001382821)", "ciks": ["0001382821"], "accession": "0001628280-25-014827", "document": "redfin-425faqsround2.htm", "description": "425", "url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm"}]}

### Turn 2  (stop_reason=end_turn)
**Answer: Rocket Companies (NYSE: RKT) agreed to acquire Redfin (NASDAQ: RDFN) for $12.50 per share, $1.75 billion in equity value, and about $2.36 billion in enterprise value.** The deal was announced March 10, 2025, and had not closed as of April 7, 2025.

- **Price per share: $12.50.** The deal is all-stock. 
Each share of Redfin common stock will be exchanged for a fixed ratio of 0.7926 shares of Rocket Companies Class A common stock
, which the companies valued at $12.50 per Redfin share. The premium is 
63% over the volume weighted average price (VWAP) of Redfin's common stock for the 30 days ending March 7, 2025.

- **Equity value: $1.75 billion.** 
Rocket Companies announced it would purchase Redfin in an all-stock transaction for a value of $12.50 per Redfin share, or $1.75 billion of equity value.

- **Enterprise value: about $2.36 billion.** Rocket's investor presentation lists a 
$1.75B equity value, equivalent to 63% premium over 30-day volume weighted average price
 and a 
$2.36B enterprise value
. Redfin's own FAQ rounds this to 
an enterprise value of $2.4 billion, which includes the assumption of Redfin's debt under its outstanding convertible notes.
 The roughly $0.61 billion gap between the two figures is consistent with net debt, including those convertible notes.

**Caveat on the per-share value:** The $12.50 is an implied value at signing, not a fixed cash price. Redfin's FAQ notes that 
the value of the consideration to be received by Redfin stockholder
…[truncated 1,845 chars]
- web_search(query=null) → 10 results: March 10, 2025 Rocket Companies to acquire Redfin <https://s205.q4cdn.com/636124780/files/doc_downloads/2025/3/Rocket-Companies-Redfin-Transaction-Investor-Presentation.pdf>; Rocket Companies to acquire Redfin for $1.75B <https://techcrunch.com/2025/03/10/rocket-companies-to-acquire-redfin-for-1-75b/>; Rocket Companies, Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1805284/000095014225000696/eh250601250_ex9901.htm>; Rocket Companies to Acquire Redfin <https://www.paulweiss.com/insights/client-news/rocket-companies-to-acquire-redfin>; Redfin Corp - Form 425 - FY2025 <https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm>

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: Rocket Companies (NYSE: RKT) agreed to acquire Redfin (NASDAQ: RDFN) for $12.50 per share, $1.75 billion in equity value, and about $2.36 billion in enterprise value.** The deal was announced March 10, 2025, and had not closed as of April 7, 2025.\n\n- **Price per share: $12.50.** The deal is all-stock. Redfin holders receive a fixed 0.7926 Rocket Class A shares for each Redfin share, which the companies valued at $12.50 per Redfin share at signing. The implied premium is 63% over the 30-day volume weighted average price ending March 7, 2025 (Rocket press release and Form 425 Exhibit 99.1).\n- **Equity value: $1.75 billion.** Rocket's announcement described the al
…[truncated 3,049 chars])

### Final answer
**Answer: Rocket Companies (NYSE: RKT) agreed to acquire Redfin (NASDAQ: RDFN) for $12.50 per share, $1.75 billion in equity value, and about $2.36 billion in enterprise value.** The deal was announced March 10, 2025, and had not closed as of April 7, 2025.

- **Price per share: $12.50.** The deal is all-stock. Redfin holders receive a fixed 0.7926 Rocket Class A shares for each Redfin share, which the companies valued at $12.50 per Redfin share at signing. The implied premium is 63% over the 30-day volume weighted average price ending March 7, 2025 (Rocket press release and Form 425 Exhibit 99.1).
- **Equity value: $1.75 billion.** Rocket's announcement described the all-stock transaction as a $12.50 per share value, or $1.75 billion of equity value.
- **Enterprise value: about $2.36 billion.** Rocket's investor presentation lists $1.75B equity value and $2.36B enterprise value, with enterprise value to 2026E revenue of 2.0x. Redfin's own FAQ rounds this to $2.4 billion and states the figure includes assumption of Redfin's convertible note debt. The roughly $0.61 billion gap between equity value and enterprise value reflects net debt, including those convertible notes.

**Caveat on the per-share value:** The $12.50 is an implied value at signing, not a fixed cash price. Under the exchange ratio, the value Redfin holders receive depends on Rocket's Class A share price at closing, so it could be higher or lower than $12.50.

**Sources:**
- Rocket Companies investor presentation (March 10, 2025): https://s205.q4cdn.com/636124780/files/doc_downloads/2025/3/Rocket-Companies-Redfin-Transaction-Investor-Presentation.pdf
- Rocket Companies press release (March 10, 2025): https://ir.rocketcompanies.com/news-and-events/press-releases/press-release-details/2025/Rocket-Companies-to-Acquire-Redfin-Accelerating-Purchase-Mortgage-Strategy/default.aspx
- Redfin Form 425, Exhibit 99.1 (Rocket press release): https://www.sec.gov/Archives/edgar/data/1382821/000095014225000697/eh250601348_ex9901.htm
- Redfin Form 425 FAQ (March 25, 2025): https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm
- Redfin Form 425 employee FAQ: https://www.sec.gov/Archives/edgar/data/1382821/000162828025011642/redfin425formofemls.htm
- TechCrunch (March 10, 2025): https://techcrunch.com/2025/03/10/rocket-companies-to-acquire-redfin-for-1-75b/
- Paul, Weiss deal summary: https://www.paulweiss.com/insights/client-news/rocket-companies-to-acquire-redfin

{"sources": [{"url": "https://s205.q4cdn.com/636124780/files/doc_downloads/2025/3/Rocket-Companies-Redfin-Transaction-Investor-Presentation.pdf", "name": "Rocket Companies investor presentation (March 10, 2025)"}, {"url": "https://ir.rocketcompanies.com/news-and-events/press-releases/press-release-details/2025/Rocket-Companies-to-Acquire-Redfin-Accelerating-Purchase-Mortgage-Strategy/default.aspx", "name": "Rocket Companies press release (March 10, 2025)"}, {"url": "https://www.sec.gov/Archives/edgar/data/1382821/000095014225000697/eh250601348_ex9901.htm", "name": "Redfin Form 425, Exhibit 99.1"}, {"url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm", "name": "Redfin Form 425 FAQ (March 25, 2025)"}, {"url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025011642/redfin425formofemls.htm", "name": "Redfin Form 425 employee FAQ"}, {"url": "https://techcrunch.com/2025/03/10/rocket-companies-to-acquire-redfin-for-1-75b/", "name": "TechCrunch (March 10, 2025)"}, {"url": "https://www.paulweiss.com/insights/client-news/rocket-companies-to-acquire-redfin", "name": "Paul, Weiss deal summary"}]}