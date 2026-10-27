## Rollout `ctl4`
- outcome: submitted
- turns: 2; cost: $0.012; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Rocket Companies to acquire Redfin per share equity value enterprise value") → 0 results: 
- edgar_search({"search_query": "Rocket Redfin merger agreement per share cash enterprise value", "start_date": "2025-03-01", "top_n_results": 5})
  result: {"total_matching_documents": 61, "page": 1, "results": [{"form": "425", "file_date": "2025-03-26", "period_ending": null, "company": "Redfin Corp  (RDFN)  (CIK 0001382821)", "ciks": ["0001382821"], "accession": "0001628280-25-014827", "document": "redfin-425faqsround2.htm", "description": "425", "url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm"}, {"form": "8-K", "file_date": "2025-03-10", "period_ending": "2025-03-09", "company": "Redfin Corp  (RDFN)  (CIK 0001382821)", "ciks": ["0001382821"], "accession": "0001628280-25-011457", "document": "rdfn-20250309.htm", "description": "8-K", "url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025011457/rdfn-20250309.htm"}, {"form": "425", "file_date": "2025-03-10", "period_ending": null, "company": "Redfin Corp  (RDFN)  (CIK 0001382821)", "ciks": ["0001382821"], "accession": "0001628280-25-011458", "document": "form8-kx31025.htm", "description": "425", "url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025011458/form8-kx31025.htm"}, {"form": "S-4", "file_date": "2025-04-07", "period_ending": null, "company": "Rocket Companies, Inc.  (RKT)  (CIK 0001805284)", "ciks": ["0001805284"], "accession": "0001104659-25-032694", "document": "tm2511408-1_s4.htm", "description": "S-4", "url": "https://www.sec.gov/Archives/edgar/data/1805284/000110465925032694/tm2511408-1_s4.htm"}, {"form": "8-K", "file_date": "2025-03-31", "period_ending": "2025-03-31", "company": "Mr. Cooper Group Inc.  (COOP)  (CIK 0000933136)", "ciks": ["0000933136"], "accession": "0001193125-25-067734", "document": "d941832dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/933136/000119312525067734/d941832dex991.htm"}]}

### Turn 2  (stop_reason=tool_use)
**Answer: Rocket Companies (RKT) agreed to acquire Redfin (RDFN) on March 10, 2025 for $12.50 per share, a $1.75 billion equity value and roughly $2.36–2.4 billion enterprise value.** The deal was announced as of March 10, 2025, so I've treated it as the completed agreement terms as of your April 7, 2025 date. It has not closed.

- **Price per share:** The deal was 
an all-stock transaction for a value of $12.50 per Redfin share, or $1.75 billion of equity value.
 Each Redfin share converts into a fixed ratio: 
0.7926 shares of Rocket Companies Class A common stock
, which the investor presentation equates to 
$12.50 in value per Redfin share.
 Because the ratio is fixed, the dollar value will move with Rocket's share price until closing. Redfin notes that 
this value may fluctuate between the signing of the merger agreement and the closing
.
- **Equity value:** 
$1.75B equity value, equivalent to 63% premium over 30-day volume weighted average price
.
- **Enterprise value:** Redfin's own FAQ says 
this equates to an enterprise value of $2.4 billion, which includes the assumption of Redfin's debt under its outstanding convertible notes.
 The investor presentation gives a slightly lower figure of 
$2.36B enterprise value
. The $2.4 billion figure appears in the merger filing, and the $2.36 billion figure appears in the deal presentation.

Summary: $12.50 per share; $1.75 billion equity value; about $2.36 billion (≈$2.4 billion) enterprise value.

{
    "sources": [
        {
 
…[truncated 1,141 chars]
- web_search(query=null) → 10 results: Rocket Companies to acquire Redfin <https://coverager.com/rocket-companies-to-acquire-redfin/>; Rocket Companies (RKT) to Acquire Redfin (RDFN) in All-Stock Deal, $1.75 Billion Equity Value <https://www.streetinsider.com/Corporate+News/Rocket+Companies+(RKT)+to+Acquire+Redfin+(RDFN)+in+All-Stock+Deal,+$1.75+Billion+Equity+Value/24474720.html>; Rocket Companies, Inc. - Form 8-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1805284/000095014225000696/eh250601250_ex9901.htm>; Redfin Corp - Form 425 - FY2025 <https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm>; March 10, 2025 Rocket Companies to acquire Redfin <https://s205.q4cdn.com/636124780/files/doc_downloads/2025/3/Rocket-Companies-Redfin-Transaction-Investor-Presentation.pdf>
- submit_final_result({"final_result": "Redfin (RDFN) was agreed to be acquired by Rocket Companies (RKT) on March 10, 2025 (merger agreement signed March 9, 2025) in an all-stock deal:\n\n- Price per share: $12.50 per Redfin share, implemented as a fixed exchange ratio of 0.7926 Rocket Class A shares per Redfin share. The dollar value fluctuates with RKT's share price until closing.\n- Equity value: $1.75 billion.\n- Enterprise value: approximately $2.36 billion per Rocket's investor presentation; $2.4 billion per Redfin's FAQ and the merger filing (includes assumed convertible notes debt).\n- Premium: 63% over the 30-day VWAP ending March 7, 2025.\n\nSources:\n{\"sources\": [\n{\"url\": \"https://ir.rocketcompa
…[truncated 950 chars])

### Final answer
Redfin (RDFN) was agreed to be acquired by Rocket Companies (RKT) on March 10, 2025 (merger agreement signed March 9, 2025) in an all-stock deal:

- Price per share: $12.50 per Redfin share, implemented as a fixed exchange ratio of 0.7926 Rocket Class A shares per Redfin share. The dollar value fluctuates with RKT's share price until closing.
- Equity value: $1.75 billion.
- Enterprise value: approximately $2.36 billion per Rocket's investor presentation; $2.4 billion per Redfin's FAQ and the merger filing (includes assumed convertible notes debt).
- Premium: 63% over the 30-day VWAP ending March 7, 2025.

Sources:
{"sources": [
{"url": "https://ir.rocketcompanies.com/news-and-events/press-releases/press-release-details/2025/Rocket-Companies-to-Acquire-Redfin-Accelerating-Purchase-Mortgage-Strategy/default.aspx", "name": "Rocket Companies press release, March 10, 2025"},
{"url": "https://www.sec.gov/Archives/edgar/data/1805284/000095014225000696/eh250601250_ex9901.htm", "name": "Rocket Companies Form 8-K Exhibit 99.1 (March 10, 2025)"},
{"url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm", "name": "Redfin Form 425 FAQs (March 25, 2025)"},
{"url": "https://s205.q4cdn.com/636124780/files/doc_downloads/2025/3/Rocket-Companies-Redfin-Transaction-Investor-Presentation.pdf", "name": "Rocket Companies investor presentation, March 10, 2025"},
{"url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025011458/form8-kx31025.htm", "name": "Redfin Form 425 (merger agreement excerpt, March 10, 2025)"}
]}