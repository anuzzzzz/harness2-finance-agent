## Rollout `static1`
- outcome: submitted
- turns: 3; cost: $0.014; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Rocket Redfin acquisition $10.00 per share equity value enterprise value") → 0 results: 
- edgar_search({"search_query": "Rocket Companies Redfin merger agreement per share enterprise value", "start_date": "2025-03-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 61, "page": 1, "results": [{"form": "425", "file_date": "2025-03-26", "period_ending": null, "company": "Redfin Corp  (RDFN)  (CIK 0001382821)", "ciks": ["0001382821"], "accession": "0001628280-25-014827", "document": "redfin-425faqsround2.htm", "description": "425", "url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm"}, {"form": "8-K", "file_date": "2025-03-10", "period_ending": "2025-03-09", "company": "Redfin Corp  (RDFN)  (CIK 0001382821)", "ciks": ["0001382821"], "accession": "0001628280-25-011457", "document": "rdfn-20250309.htm", "description": "8-K", "url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025011457/rdfn-20250309.htm"}, {"form": "425", "file_date": "2025-03-10", "period_ending": null, "company": "Redfin Corp  (RDFN)  (CIK 0001382821)", "ciks": ["0001382821"], "accession": "0001628280-25-011458", "document": "form8-kx31025.htm", "description": "425", "url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025011458/form8-kx31025.htm"}, {"form": "S-4", "file_date": "2025-04-07", "period_ending": null, "company": "Rocket Companies, Inc.  (RKT)  (CIK 0001805284)", "ciks": ["0001805284"], "accession": "0001104659-25-032694", "document": "tm2511408-1_s4.htm", "description": "S-4", "url": "https://www.sec.gov/Archives/edgar/data/1805284/000110465925032694/tm2511408-1_s4.htm"}, {"form": "425", "file_date": "2025-03-31", "period_ending": null, "company": "Mr. Cooper Group Inc.  (COOP)  (CIK 0000933136)", "ciks": ["0000933136"], "accession": "0001193125-25-067735", "document": "d941832d425.htm", "description": "425", "url": "https://www.sec.gov/Archives/edgar/data/933136/000119312525067735/d941832d425.htm"}, {"form": "8-K", "file_date": "2025-03-31", "period_endi
  …[truncated 5,304 chars]

### Turn 2  (stop_reason=end_turn)
The deal was announced on March 10, 2025 and is still pending as of April 7, 2025, so the figures below are deal terms, not a completed purchase price.

**Price per share: $12.50 (implied, not fixed).** Rocket Companies agreed to buy Redfin 
in an all-stock transaction for a value of $12.50 per Redfin share, or $1.75 billion of equity value.
 The mechanics are a fixed exchange ratio: 
each share of Redfin common stock will be exchanged for a fixed ratio of 0.7926 shares of Rocket Class A common stock.
 The $12.50 is therefore an effective valuation, not a guaranteed cash amount. Redfin's own FAQ notes that 
this value may fluctuate between the signing of the merger agreement and the closing of the proposed transaction, or after closing, and could be more or less than an effective valuation of $12.50 per share
.

**Equity value: $1.75 billion.** This is the figure in Rocket's announcement and the Redfin filing, and it was confirmed by the investor presentation, which lists a 
$1.75B equity value, equivalent to 63% premium over 30-day volume weighted average price
.

**Enterprise value: $2.36 billion (Rocket's figure).** Rocket's investor presentation states a 
$2.36B enterprise value
. Redfin's FAQ rounds this to 
an enterprise value of $2.4 billion, which includes the assumption of Redfin's debt under its outstanding convertible notes.
 Press coverage also cites 
total enterprise value of the acquisition, including Redfin's debt and other financial obligations, is $2.4 billio
…[truncated 1,575 chars]
- web_search(query=null) → 10 results: March 10, 2025 Rocket Companies to acquire Redfin <https://s205.q4cdn.com/636124780/files/doc_downloads/2025/3/Rocket-Companies-Redfin-Transaction-Investor-Presentation.pdf>; Redfin Corp - Form 425 - FY2025 <https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm>; Rocket Companies to acquire Redfin for $1.75B <https://techcrunch.com/2025/03/10/rocket-companies-to-acquire-redfin-for-1-75b/>; Rocket Companies, Inc. - Rocket Companies to Acquire Redfin, Accelerating Purchase Mortgage Strategy <https://ir.rocketcompanies.com/news-and-events/press-releases/press-release-details/2025/Rocket-Companies-to-Acquire-Redfin-Accelerating-Purchase-Mortgage-Strategy/default.aspx>; Rocket Companies to Acquire Redfin <https://www.paulweiss.com/insights/client-news/rocket-companies-to-acquire-redfin>

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "Redfin (RDFN) agreed to be acquired by Rocket Companies (RKT) on March 10, 2025. The deal is still pending as of April 7, 2025, so these are announced deal terms, not a completed purchase price.\n\n**Price per share: $12.50 (implied, not fixed).** The deal is all-stock and uses a fixed exchange ratio of 0.7926 Rocket Class A shares for each Redfin share. The $12.50 figure is the value implied by that ratio at signing. Because Rocket's share price moves until closing, the actual value received by Redfin holders can be higher or lower than $12.50.\n\n**Equity value: $1.75 billion.** Rocket's announcement and the investor presentation both state $1.75 billion of equity value.\
…[truncated 1,864 chars])

### Final answer
Redfin (RDFN) agreed to be acquired by Rocket Companies (RKT) on March 10, 2025. The deal is still pending as of April 7, 2025, so these are announced deal terms, not a completed purchase price.

**Price per share: $12.50 (implied, not fixed).** The deal is all-stock and uses a fixed exchange ratio of 0.7926 Rocket Class A shares for each Redfin share. The $12.50 figure is the value implied by that ratio at signing. Because Rocket's share price moves until closing, the actual value received by Redfin holders can be higher or lower than $12.50.

**Equity value: $1.75 billion.** Rocket's announcement and the investor presentation both state $1.75 billion of equity value.

**Enterprise value: $2.36 billion.** Rocket's investor presentation gives $2.36 billion. Redfin's shareholder FAQ and press coverage round this to about $2.4 billion. The enterprise value includes the assumed debt under Redfin's outstanding convertible notes and other obligations.

**Cross-checks and context:**
- Implied share count: $1.75B ÷ $12.50 ≈ 140 million Redfin shares.
- Implied debt and other obligations: $2.36B − $1.75B = $0.61B.
- The $12.50 price represents a 63% premium to Redfin's 30-day volume weighted average price ending March 7, 2025.
- Closing is expected in Q2 or Q3 2025, subject to Redfin shareholder approval and regulatory approvals.

**Summary:** $12.50 per share (paid as 0.7926 Rocket Class A shares per Redfin share), $1.75 billion equity value, and $2.36 billion enterprise value (about $2.4 billion when rounded).

{
    "sources": [
        {
            "url": "https://s205.q4cdn.com/636124780/files/doc_downloads/2025/3/Rocket-Companies-Redfin-Transaction-Investor-Presentation.pdf",
            "name": "Rocket Companies to acquire Redfin – Investor Presentation (March 10, 2025)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025011458/exhibit991-8xk31025.htm",
            "name": "Redfin Corp Form 425 – Exhibit 99.1 press release (March 10, 2025)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm",
            "name": "Redfin Corp Form 425 – Shareholder FAQ (March 25, 2025)"
        },
        {
            "url": "https://www.geekwire.com/2025/redfin-to-be-acquired-by-rocket-companies-in-1-75b-deal/",
            "name": "GeekWire – Redfin to be acquired by Rocket Companies in $1.75B deal"
        }
    ]
}