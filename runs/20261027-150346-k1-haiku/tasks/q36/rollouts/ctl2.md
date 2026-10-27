## Rollout `ctl2`
- outcome: submitted
- turns: 2; cost: $0.013; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Rocket Companies to acquire Redfin per share equity value enterprise value") → 0 results: 
- edgar_search({"search_query": "Rocket Redfin merger agreement per share cash enterprise value", "start_date": "2025-03-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 61, "page": 1, "results": [{"form": "425", "file_date": "2025-03-26", "period_ending": null, "company": "Redfin Corp  (RDFN)  (CIK 0001382821)", "ciks": ["0001382821"], "accession": "0001628280-25-014827", "document": "redfin-425faqsround2.htm", "description": "425", "url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm"}, {"form": "8-K", "file_date": "2025-03-10", "period_ending": "2025-03-09", "company": "Redfin Corp  (RDFN)  (CIK 0001382821)", "ciks": ["0001382821"], "accession": "0001628280-25-011457", "document": "rdfn-20250309.htm", "description": "8-K", "url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025011457/rdfn-20250309.htm"}, {"form": "425", "file_date": "2025-03-10", "period_ending": null, "company": "Redfin Corp  (RDFN)  (CIK 0001382821)", "ciks": ["0001382821"], "accession": "0001628280-25-011458", "document": "form8-kx31025.htm", "description": "425", "url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025011458/form8-kx31025.htm"}, {"form": "S-4", "file_date": "2025-04-07", "period_ending": null, "company": "Rocket Companies, Inc.  (RKT)  (CIK 0001805284)", "ciks": ["0001805284"], "accession": "0001104659-25-032694", "document": "tm2511408-1_s4.htm", "description": "S-4", "url": "https://www.sec.gov/Archives/edgar/data/1805284/000110465925032694/tm2511408-1_s4.htm"}, {"form": "8-K", "file_date": "2025-03-31", "period_ending": "2025-03-31", "company": "Mr. Cooper Group Inc.  (COOP)  (CIK 0000933136)", "ciks": ["0000933136"], "accession": "0001193125-25-067734", "document": "d941832dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/933136/000119312525067734/d941832dex991.htm"}, {"form": "425", "file_date": "2025-03-3
  …[truncated 5,304 chars]

### Turn 2  (stop_reason=tool_use)
The acquirer was Rocket Companies (NYSE: RKT), which agreed on March 9–10, 2025 to buy Redfin in an all-stock deal. As of April 7, 2025, the deal had not closed.

**Price per share:** Rocket valued each Redfin share at 
$12.50 per Redfin share
. The consideration is a fixed exchange ratio of 
0.7926 shares of Rocket Class A common stock for each share of Redfin common stock
. Because the ratio is fixed, the dollar value moves with Rocket's stock price until closing. The filing notes that the value 
could be more or less than an effective valuation of $12.50 per share
. The $12.50 figure implies a Rocket share price of about $15.77 at signing (12.50 / 0.7926).

**Equity value:** 
$1.75 billion of equity value
. The premium was 
63% over the volume weighted average price (VWAP) of Redfin's common stock for the 30 days ending March 7, 2025
.

**Enterprise value:** Sources differ slightly on rounding. The investor presentation lists 
$2.36B enterprise value
, and that figure is also used in press coverage such as 
$2.36 billion in total enterprise value
. Redfin's own FAQ and the merger filing describe it as 
an enterprise value of $2.4 billion, which includes the assumption of Redfin's debt under its outstanding convertible notes
. The precise figure is about $2.36 billion; $2.4 billion is the rounded version.

**Summary:**
- Price per share: $12.50 (at signing, paid as 0.7926 Rocket Class A shares)
- Equity value: $1.75 billion
- Enterprise value: approximately $2.36 billion (r
…[truncated 1,474 chars]
- web_search(query=null) → 10 results: Rocket Companies (RKT) to Acquire Redfin (RDFN) in All-Stock Deal, $1.75 Billion Equity Value <https://www.streetinsider.com/Corporate+News/Rocket+Companies+(RKT)+to+Acquire+Redfin+(RDFN)+in+All-Stock+Deal,+$1.75+Billion+Equity+Value/24474720.html>; Redfin Corp - Form 425 - FY2025 <https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm>; Rocket Companies, Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1805284/000095014225000696/eh250601250_ex9901.htm>; March 10, 2025 Rocket Companies to acquire Redfin <https://s205.q4cdn.com/636124780/files/doc_downloads/2025/3/Rocket-Companies-Redfin-Transaction-Investor-Presentation.pdf>; Rocket Companies to Acquire Redfin <https://www.paulweiss.com/insights/client-news/rocket-companies-to-acquire-redfin>
- submit_final_result({"final_result": "Redfin (RDFN) was agreed to be acquired by Rocket Companies (NYSE: RKT) on March 9–10, 2025, in an all-stock deal. As of April 7, 2025, the deal had not closed.\n\nPrice per share: $12.50 per Redfin share at signing, paid as a fixed exchange ratio of 0.7926 Rocket Class A shares per Redfin share. Because the ratio is fixed, the dollar value floats with Rocket's share price until closing. The $12.50 figure implies a Rocket share price of about $15.77 (12.50 / 0.7926).\n\nEquity value: $1.75 billion, a 63% premium to Redfin's 30-day VWAP ending March 7, 2025.\n\nEnterprise value: about $2.36 billion per the investor presentation and press coverage; Redfin's FAQ and merger fil
…[truncated 1,368 chars])

### Final answer
Redfin (RDFN) was agreed to be acquired by Rocket Companies (NYSE: RKT) on March 9–10, 2025, in an all-stock deal. As of April 7, 2025, the deal had not closed.

Price per share: $12.50 per Redfin share at signing, paid as a fixed exchange ratio of 0.7926 Rocket Class A shares per Redfin share. Because the ratio is fixed, the dollar value floats with Rocket's share price until closing. The $12.50 figure implies a Rocket share price of about $15.77 (12.50 / 0.7926).

Equity value: $1.75 billion, a 63% premium to Redfin's 30-day VWAP ending March 7, 2025.

Enterprise value: about $2.36 billion per the investor presentation and press coverage; Redfin's FAQ and merger filing round this to $2.4 billion (including assumed convertible notes debt).

Sources:
{
    "sources": [
        {"url": "https://ir.rocketcompanies.com/news-and-events/press-releases/press-release-details/2025/Rocket-Companies-to-Acquire-Redfin-Accelerating-Purchase-Mortgage-Strategy/default.aspx", "name": "Rocket Companies press release, March 10, 2025"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1805284/000095014225000696/eh250601250_ex9901.htm", "name": "Rocket Companies Form 8-K Exhibit 99.1, March 10, 2025"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm", "name": "Redfin Form 425 FAQs, March 25, 2025"},
        {"url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025011458/form8-kx31025.htm", "name": "Redfin Form 425 filing (merger consideration), March 10, 2025"},
        {"url": "https://s205.q4cdn.com/636124780/files/doc_downloads/2025/3/Rocket-Companies-Redfin-Transaction-Investor-Presentation.pdf", "name": "Rocket Companies investor presentation, March 10, 2025"},
        {"url": "https://seekingalpha.com/article/4766448-rocket-companies-acquires-redfin-not-a-silver-bullet-but-longer-lifeline-to-resurrect-real-estate-business", "name": "Seeking Alpha: Rocket Acquires Redfin"}
    ]
}