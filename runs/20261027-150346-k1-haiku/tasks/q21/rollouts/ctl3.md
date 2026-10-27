## Rollout `ctl3`
- outcome: submitted
- turns: 2; cost: $0.012; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Shift4 Payments 10-K 2024 concentration risk vendors") → 0 results: 
- edgar_search({"search_query": "Shift4 vendor concentration risk", "start_date": "2025-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 86, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-19", "period_ending": "2024-12-31", "company": "Shift4 Payments, Inc.  (FOUR)  (CIK 0001794669)", "ciks": ["0001794669"], "accession": "0001794669-25-000011", "document": "four-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1794669/000179466925000011/four-20241231.htm"}, {"form": "NPORT-P", "file_date": "2025-03-31", "period_ending": "2025-01-31", "company": "Eaton Vance Mutual Funds Trust  (CIK 0000745463)", "ciks": ["0000745463"], "accession": "0001752724-25-075608", "document": "NPORT_FG7G_68214998_0125.htm", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/745463/000175272425075608/NPORT_FG7G_68214998_0125.htm"}, {"form": "NPORT-P", "file_date": "2025-03-28", "period_ending": "2025-01-31", "company": "ADVENT CONVERTIBLE & INCOME FUND  (AVK)  (CIK 0001219120)", "ciks": ["0001219120"], "accession": "0001752724-25-073695", "document": "gug88478nq.htm", "description": "ADVENT CONVERTIBLE AND INCOME FUND NQ", "url": "https://www.sec.gov/Archives/edgar/data/1219120/000175272425073695/gug88478nq.htm"}, {"form": "N-CSRS", "file_date": "2025-03-26", "period_ending": "2025-01-31", "company": "PRUDENTIAL INVESTMENT PORTFOLIOS 2  (CIK 0001099692)", "ciks": ["0001099692"], "accession": "0001193125-25-063651", "document": "d940387dncsrs.htm", "description": "PRUDENTIAL INVESTMENT PORTFOLIOS 2", "url": "https://www.sec.gov/Archives/edgar/data/1099692/000119312525063651/d940387dncsrs.htm"}, {"form": "N-CSR", "file_date": "2025-03-03", "period_ending": "2024-12-31", "company": "EMPOWER FUNDS, INC.  (CIK 0000356476)", "ciks": ["0000356476"], "accession": "0001145549-25-015759", "document": "8dd582dd1c96471.htm", "description": "N-CS
  …[truncated 5,679 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Shift4 Payments, Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1794669/000179466925000011/four-20241231.htm>; 20240229 shift4-payments-inc Item 1C. Cybersecurity - Board Cybersecurity <https://www.board-cybersecurity.com/annual-reports/tracker/20240229-shift4-payments-inc-cybersecurity-10k>; Shift4 Payments (FOUR) Risk Factors: 2025 10-K, What Changed <https://gloom.sh/stocks/four/risk-factors/2025>; Shift4 Payments, Inc. SEC 10-K Report — TradingView News <https://www.tradingview.com/news/tradingview:8a7cc90f01326:0-shift4-payments-inc-sec-10-k-report/>; four-20231231 <https://investors.shift4.com/sec-filings/all-sec-filings/content/0001794669-24-000007/four-20231231.htm>
- submit_final_result({"final_result": "**Answer: As of December 31, 2024, Shift4's vendor concentration risk is high. Its North American merchant processing depends on a single vendor.**\n\n**What the FY2024 10-K says (Concentration Risk note):**\n- Shift4 routes its North American merchant processing through one vendor. The company states that this vendor keeps backup systems and alternative arrangements to prevent major processing disruptions if an unforeseen event occurs. <cite index=\"1-1,1-2\">The Company's merchant processing activity in North America is facilitated by one vendor. The Company believes that this vendor maintains appropriate backup systems and alternative arrangements to avoid a significant 
…[truncated 2,577 chars])

### Final answer
**Answer: As of December 31, 2024, Shift4's vendor concentration risk is high. Its North American merchant processing depends on a single vendor.**

**What the FY2024 10-K says (Concentration Risk note):**
- Shift4 routes its North American merchant processing through one vendor. The company states that this vendor keeps backup systems and alternative arrangements to prevent major processing disruptions if an unforeseen event occurs. <cite index="1-1,1-2">The Company's merchant processing activity in North America is facilitated by one vendor. The Company believes that this vendor maintains appropriate backup systems and alternative arrangements to avoid a significant disruption of the processing in the event of an unforeseen event.</cite>
- This is a change from prior years. The FY2020 10-K described processing as <cite index="6-5">facilitated by two vendors</cite>, so the dependence has narrowed from two vendors to one.
- Revenue exposure: <cite index="1-3">A majority of the Company's revenue is derived from the processing of card transactions.</cite> A single processor therefore touches most of the revenue base.
- Sponsorship dependency (a related bank-level concentration): <cite index="1-4">Because the Company is not a "member bank" in North America, in order to process these bank card transactions, the Company has entered into a sponsorship agreement with a member bank.</cite> If that agreement is breached, <cite index="1-6">the bank sponsor may terminate the agreement and, under the terms of the agreement, the Company would have 180 days to identify an alternative bank sponsor.</cite>

**Related risk factor:** The 10-K's risk factors also state that <cite index="8-8">the company depends on third-party vendors for certain products and services, including components of its computer systems, software, data centers and telecommunications networks</cite>, and that failures by those vendors could adversely affect the business (see the risk factor on reliance on third-party vendors).

**Assessment:** Concentration is high. One processor handles North American card processing, which is most of revenue. Mitigants are the vendor's stated backup systems and the 180-day window to replace a sponsor bank. The 10-K does not quantify the share of volume or revenue tied to the vendor, so the exposure cannot be stated as a percentage from this source.

**Sources:** Shift4 Payments FY2024 Form 10-K (filed 2025-02-19); Shift4 FY2020 Form 10-K (filed 2021-03-08); Shift4 risk factor summaries.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1794669/000179466925000011/four-20241231.htm",
            "name": "Shift4 Payments, Inc. Form 10-K FY2024"
        },
        {
            "url": "https://content.edgar-online.com/ExternalLink/EDGAR/0001564590-21-011368.html?hash=b6ebf2d8395e5d019a29e11692e3b783baf613d4570e5e055b08d0150b3393e6&dest=four-ex42_573_htm",
            "name": "Shift4 Payments, Inc. Form 10-K (filed 03/08/2021)"
        },
        {
            "url": "https://www.tipranks.com/stocks/four/risk-factors",
            "name": "TipRanks - Shift4 Payments (FOUR) Risk Analysis"
        }
    ]
}