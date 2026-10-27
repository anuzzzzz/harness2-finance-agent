## Rollout `ctl4`
- outcome: submitted
- turns: 2; cost: $0.013; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Dutch Bros full year 2024 results total revenue gross profit") → 0 results: 
- edgar_search({"search_query": "Dutch Bros 10-K 2024 total revenue gross profit", "ciks": ["BROS"], "top_n_results": 5})
  result: {"total_matching_documents": 38, "page": 1, "results": [{"form": "8-K", "file_date": "2024-11-06", "period_ending": "2024-11-01", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-24-000304", "document": "a2024-q3_ex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658124000304/a2024-q3_ex991.htm"}, {"form": "8-K", "file_date": "2024-08-07", "period_ending": "2024-08-07", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-24-000212", "document": "a2024-q2_ex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658124000212/a2024-q2_ex991.htm"}, {"form": "8-K", "file_date": "2024-05-07", "period_ending": "2024-05-07", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-24-000132", "document": "a2024-q1_ex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658124000132/a2024-q1_ex991.htm"}, {"form": "8-K", "file_date": "2025-02-12", "period_ending": "2025-02-12", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-25-000035", "document": "a2024-q4_ex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000035/a2024-q4_ex991.htm"}, {"form": "8-K", "file_date": "2024-02-21", "period_ending": "2024-02-20", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-24-000032", "document": "a2023-q4_ex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658124000032/a2023-q4_ex991.htm"}]}

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Dutch Bros Inc. - Form ARS - FY2024 <https://www.sec.gov/Archives/edgar/data/1866581/000186658125000104/p24788dutchbrothers2024ar-.pdf>; Dutch Bros Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1866581/000186658124000212/a2024-q2_ex991.htm>; Dutch Bros Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1866581/000186658124000032/a2023-q4_ex991.htm>; Dutch Bros Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1866581/000186658124000132/a2024-q1_ex991.htm>; Dutch Bros Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1866581/000186658125000048/bros-20241231.htm>
- submit_final_result({"final_result": "**Answer: BROS 2026 gross profit ≈ $467 million** (about $466.58M before rounding)\n\n**Step 1: FY2024 baseline (consolidated)**\n- Total revenue for FY2024 was <cite index=\"10-3\">1,281.02</cite> million (the investing.com table shows 1,281.02 for 2024). Cross-check: <cite index=\"6-9\">Dutch Bros total revenues for 2024 grew 32.6 per cent to $1.28 billion as compared to $965.8 million in 2023.</cite>\n- FY2024 gross profit was $340.13 million, with cost of revenue of $940.89 million (Yahoo Finance: <cite index=\"9-5\">2024 gross profit 340.13M; cost of revenue 940.89M</cite>). Check: 340.13 + 940.89 = 1,281.02, which ties to revenue.\n- YE 2024 gross margin = 340.13 / 1,
…[truncated 1,872 chars])

### Final answer
**Answer: BROS 2026 gross profit ≈ $467 million** (about $466.58M before rounding)

**Step 1: FY2024 baseline (consolidated)**
- Total revenue for FY2024 was <cite index="10-3">1,281.02</cite> million (the investing.com table shows 1,281.02 for 2024). Cross-check: <cite index="6-9">Dutch Bros total revenues for 2024 grew 32.6 per cent to $1.28 billion as compared to $965.8 million in 2023.</cite>
- FY2024 gross profit was $340.13 million, with cost of revenue of $940.89 million (Yahoo Finance: <cite index="9-5">2024 gross profit 340.13M; cost of revenue 940.89M</cite>). Check: 340.13 + 940.89 = 1,281.02, which ties to revenue.
- YE 2024 gross margin = 340.13 / 1,281.02 = 26.5516%.

**Step 2: Apply the scenario**
- Gross margin compressed by 500 bps (5.00 percentage points): 26.5516% − 5.00% = 21.5516%.
- Revenue grows at 30% CAGR for two years (2025 and 2026): 1,281.02 × 1.30² = 1,281.02 × 1.69 = 2,164.92 million.

**Step 3: 2026 gross profit**
- 2,164.9238 × 21.5516% = 466.58 million, which rounds to **$467 million**.

**Caveats**
- I used consolidated gross profit (revenue minus cost of revenue), which is the figure the data aggregators report. The company's own headline metric is company-operated shop gross margin (22.3% in 2024), which is a different base. Applying the same 500 bps compression to a 22.3% base would give a different result.
- The 2024 figures come from third-party aggregators. The 10-K and Q4 2024 earnings release (Business Wire) are the primary sources; they confirm the 2024 revenue of $1.28 billion and the company-operated gross profit figures.

**Sources:**
{
    "sources": [
        {
            "url": "https://finance.yahoo.com/quote/BROS/financials/",
            "name": "Yahoo Finance - Dutch Bros (BROS) Income Statement"
        },
        {
            "url": "https://www.investing.com/equities/dutch-bros-income-statement",
            "name": "Investing.com - Dutch Bros Income Statement"
        },
        {
            "url": "https://www.gcrmag.com/dutch-bros-releases-2024-q4-and-full-year-results",
            "name": "Global Coffee Report - Dutch Bros releases 2024 Q4 and full year results"
        },
        {
            "url": "https://www.businesswire.com/news/home/20250212569291/en/Dutch-Bros-Inc.-Reports-Fourth-Quarter-and-Fiscal-Year-2024-Financial-Results",
            "name": "Business Wire - Dutch Bros Inc. Reports Fourth Quarter and Fiscal Year 2024 Financial Results"
        }
    ]
}