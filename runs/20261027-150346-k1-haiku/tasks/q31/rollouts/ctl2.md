## Rollout `ctl2`
- outcome: submitted
- turns: 2; cost: $0.013; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Dutch Bros 2024 full year results total revenue gross margin") → 0 results: 
- edgar_search({"search_query": "Dutch Bros 10-K 2024 cost of sales total revenue", "ciks": ["BROS"], "top_n_results": 5})
  result: {"total_matching_documents": 42, "page": 1, "results": [{"form": "ARS", "file_date": "2025-03-31", "period_ending": "2024-12-31", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-25-000104", "document": "p24788dutchbrothers2024ar-.pdf", "description": "ARS", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000104/p24788dutchbrothers2024ar-.pdf"}, {"form": "10-K", "file_date": "2025-02-13", "period_ending": "2024-12-31", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-25-000048", "document": "bros-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000048/bros-20241231.htm"}, {"form": "ARS", "file_date": "2024-04-01", "period_ending": "2023-12-31", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-24-000107", "document": "dutchbrosinc_10kx2024xbwxv4.pdf", "description": "ARS", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658124000107/dutchbrosinc_10kx2024xbwxv4.pdf"}, {"form": "10-K", "file_date": "2024-02-23", "period_ending": "2023-12-31", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-24-000038", "document": "bros-20231231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658124000038/bros-20231231.htm"}, {"form": "10-Q", "file_date": "2024-11-07", "period_ending": "2024-09-30", "company": "Dutch Bros Inc.  (BROS)  (CIK 0001866581)", "ciks": ["0001866581"], "accession": "0001866581-24-000306", "document": "bros-20240930.htm", "description": "10-Q", "url": "https://www.sec.gov/Archives/edgar/data/1866581/00018665812400
  …[truncated 26 chars]

### Turn 2  (stop_reason=tool_use)
**Answer: BROS 2026 gross profit is about $467 million.**

**Step 1: FY2024 baseline (year-end 2024)**
- Total revenues for 2024 were 
Total revenues · 342,786 · 254,123 · 1,281,015 · 965,776
 (in thousands), so $1,281.015 million for the full year.
- Cost of sales for 2024 was 
Cost of sales · 254,838 · 194,998 · 940,886 · 714,480
, or $940.886 million.
- Gross profit = $1,281.015M − $940.886M = $340.129M. This matches the 
Gross Profit 180.92M 251.3M 340.13M 423.95M 472.44M
 figures from Yahoo Finance.
- Gross margin = $340.129M / $1,281.015M = 26.55% (26.5518%).

Note: the company also reports a separate metric, company-operated shop gross margin (22.3% in 2024). The question refers to gross margin generally, so I used consolidated gross margin.

**Step 2: Revenue in 2026 at 30% CAGR**
- Two years of growth from 2024 to 2026: $1,281.015M × (1.30)² = $1,281.015M × 1.69 = $2,164.92M (about $2,164.916M).

**Step 3: Gross margin in 2026**
- A 500 bps compression from 26.5518% gives 21.5518%.

**Step 4: Gross profit in 2026**
- $2,164.916M × 21.5518% = $466.54M, which rounds to **$467 million**.

**Caveats**
- The 30% CAGR and 500 bps compression are the question's assumptions, not forecasts. Company guidance for 2025 revenue was 
between $1.555 billion and $1.575 billion
, which is well below the 30% growth path implied by the question's assumption.
- Gross profit is calculated as revenue minus cost of sales, consistent with the reported income statement.

**Sources:**
{
    "
…[truncated 846 chars]
- web_search(query=null) → 10 results: Dutch Bros Inc. Reports Fourth Quarter and Fiscal Year ... <https://www.sec.gov/Archives/edgar/data/1866581/000186658125000035/a2024-q4_ex991.htm>; Dutch Bros releases 2024 Q4 and full year results - Global Coffee Report <https://www.gcrmag.com/dutch-bros-releases-2024-q4-and-full-year-results>; Dutch Bros Full Year 2024 Earnings: Beats Expectations <https://finance.yahoo.com/news/dutch-bros-full-2024-earnings-110717401.html>; Dutch Bros (BROS) Financials & Income Statement <https://stockanalysis.com/stocks/bros/financials/>; Dutch Bros Revenue 2020-2026 <https://www.macrotrends.net/stocks/charts/BROS/dutch-bros/revenue>
- submit_final_result({"final_result": "**Answer: BROS 2026 gross profit is about $467 million.**\n\n**Step 1: FY2024 baseline.** Total revenues for 2024 were $1,281.015M (in thousands: 1,281,015). Cost of sales for 2024 was $940.886M. Gross profit = $1,281.015M − $940.886M = $340.129M. Gross margin = 340.129 / 1,281.015 = 26.5518%. Sources: Dutch Bros Q4/FY2024 earnings release (SEC EX-99.1); Yahoo Finance and StockAnalysis gross profit series (FY2024 gross profit 340.13M).\n\nNote: the company also reports company-operated shop gross margin (22.3% in 2024). I used consolidated gross margin because the question refers to gross margin generally.\n\n**Step 2: 2026 revenue at 30% CAGR.** Two years of growth: 1,281.
…[truncated 1,193 chars])

### Final answer
**Answer: BROS 2026 gross profit is about $467 million.**

**Step 1: FY2024 baseline.** Total revenues for 2024 were $1,281.015M (in thousands: 1,281,015). Cost of sales for 2024 was $940.886M. Gross profit = $1,281.015M − $940.886M = $340.129M. Gross margin = 340.129 / 1,281.015 = 26.5518%. Sources: Dutch Bros Q4/FY2024 earnings release (SEC EX-99.1); Yahoo Finance and StockAnalysis gross profit series (FY2024 gross profit 340.13M).

Note: the company also reports company-operated shop gross margin (22.3% in 2024). I used consolidated gross margin because the question refers to gross margin generally.

**Step 2: 2026 revenue at 30% CAGR.** Two years of growth: 1,281.015 × 1.30² = 1,281.015 × 1.69 = $2,164.916M.

**Step 3: 2026 gross margin.** 26.5518% − 5.00 pts = 21.5518%.

**Step 4: 2026 gross profit.** 2,164.916 × 21.5518% = $466.54M, which rounds to **$467 million**.

**Caveats.** The 30% CAGR and 500 bps compression are the question's assumptions, not forecasts. Company initial 2025 guidance was total revenues of $1.555–1.575 billion, well below the path implied by 30% growth.

{
    "sources": [
        {"url": "https://www.sec.gov/Archives/edgar/data/1866581/000186658125000035/a2024-q4_ex991.htm", "name": "Dutch Bros Inc. Q4 and Fiscal Year 2024 Earnings Release (SEC EX-99.1)"},
        {"url": "https://finance.yahoo.com/quote/BROS/financials/", "name": "Yahoo Finance – Dutch Bros (BROS) Income Statement"},
        {"url": "https://stockanalysis.com/stocks/bros/financials/", "name": "StockAnalysis – Dutch Bros (BROS) Financials"},
        {"url": "https://www.businesswire.com/news/home/20250212569291/en/Dutch-Bros-Inc.-Reports-Fourth-Quarter-and-Fiscal-Year-2024-Financial-Results", "name": "Business Wire – Dutch Bros Fourth Quarter and Fiscal Year 2024 Financial Results"}
    ]
}