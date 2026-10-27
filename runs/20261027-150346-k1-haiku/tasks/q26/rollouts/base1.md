## Rollout `base1`
- outcome: submitted
- turns: 2; cost: $0.012; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Microsoft 10-K fiscal 2024 employees located outside United States percent") → 0 results: 
- edgar_search({"search_query": "Microsoft full-time employees June 30, 2024 United States outside United States", "ciks": ["0000789019"], "start_date": "2024-07-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 6, "page": 1, "results": [{"form": "DEF 14A", "file_date": "2024-10-24", "period_ending": "2024-12-10", "company": "MICROSOFT CORP  (MSFT)  (CIK 0000789019)", "ciks": ["0000789019"], "accession": "0001193125-24-242883", "document": "d858775ddef14a.htm", "description": "DEF 14A", "url": "https://www.sec.gov/Archives/edgar/data/789019/000119312524242883/d858775ddef14a.htm"}, {"form": "DEF 14A", "file_date": "2024-10-24", "period_ending": "2024-12-10", "company": "MICROSOFT CORP  (MSFT)  (CIK 0000789019)", "ciks": ["0000789019"], "accession": "0001193125-24-242883", "document": "d858775ddef14a1.pdf", "description": "DEF 14A", "url": "https://www.sec.gov/Archives/edgar/data/789019/000119312524242883/d858775ddef14a1.pdf"}, {"form": "ARS", "file_date": "2024-10-24", "period_ending": "2024-06-30", "company": "MICROSOFT CORP  (MSFT)  (CIK 0000789019)", "ciks": ["0000789019"], "accession": "0001193125-24-242888", "document": "d815777dars.pdf", "description": "ARS", "url": "https://www.sec.gov/Archives/edgar/data/789019/000119312524242888/d815777dars.pdf"}, {"form": "8-K", "file_date": "2024-12-03", "period_ending": "2024-12-03", "company": "MICROSOFT CORP  (MSFT)  (CIK 0000789019)", "ciks": ["0000789019"], "accession": "0000950170-24-132722", "document": "msft-ex99_1.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/789019/000095017024132722/msft-ex99_1.htm"}, {"form": "10-K", "file_date": "2024-07-30", "period_ending": "2024-06-30", "company": "MICROSOFT CORP  (MSFT)  (CIK 0000789019)", "ciks": ["0000789019"], "accession": "0000950170-24-087843", "document": "msft-20240630.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm"}, {"form": "10-K", "file_da
  …[truncated 316 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: MICROSOFT CORP - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm>; MICROSOFT CORP - Form 10-K - FY2024 (Annual Financial Statement Tables - full year 2024) <https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/Financial_Report.xlsx>; Microsoft Corporation: employees by location 2026 <https://www.statista.com/statistics/1032154/microsoft-employees-by-location/>; Microsoft Corporation: number of employees 2026 <https://www.statista.com/statistics/273475/number-of-employees-at-the-microsoft-corporation-since-2005/>; UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549 <https://microsoft.gcs-web.com/static-files/1c864583-06f7-40cc-a94d-d11400c83cc8>
- submit_final_result({"final_result": "**Answer: about 44.74% of Microsoft's full-time employees were located outside the United States as of June 30, 2024.**\n\n**Inputs (from the FY2024 Form 10-K, fiscal year ended June 30, 2024):**\n- Total full-time employees: 228,000\n- U.S. full-time employees: 126,000\n- International (non-U.S.) full-time employees: 102,000\n\nThe 10-K's headcount disclosure, as quoted in a reproduction of the filing, states that Microsoft had about 228,000 full-time staff at that date, split into 126,000 in the U.S. and 102,000 abroad (<cite index=\"7-3\">As of June 30, 2024, we employed approximately 228,000 people on a full-time basis, 126,000 in the U.S. and 102,000 internationally.</
…[truncated 1,382 chars])

### Final answer
**Answer: about 44.74% of Microsoft's full-time employees were located outside the United States as of June 30, 2024.**

**Inputs (from the FY2024 Form 10-K, fiscal year ended June 30, 2024):**
- Total full-time employees: 228,000
- U.S. full-time employees: 126,000
- International (non-U.S.) full-time employees: 102,000

The 10-K's headcount disclosure, as quoted in a reproduction of the filing, states that Microsoft had about 228,000 full-time staff at that date, split into 126,000 in the U.S. and 102,000 abroad (<cite index="7-3">As of June 30, 2024, we employed approximately 228,000 people on a full-time basis, 126,000 in the U.S. and 102,000 internationally.</cite>). A secondary data site reports the same split, showing a 55.3% U.S. / 44.7% international mix for FY2024 (<cite index="6-1,6-2">United States: 55.3%. International: 44.7%.</cite>).

**Calculation:**
- Outside-U.S. share = 102,000 ÷ 228,000 = 0.447368... ≈ **44.74%**
- Cross-check: 126,000 ÷ 228,000 = 55.26% U.S.; 55.26% + 44.74% = 100%.

**Note:** The 10-K uses the term "internationally" rather than "outside the United States," which I've treated as the same population. The figures are rounded to the nearest thousand in the filing, so the percentage is approximate.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm",
            "name": "Microsoft Form 10-K for fiscal year ended June 30, 2024 (SEC EDGAR)"
        },
        {
            "url": "https://stocklight.com/stocks/us/nasdaq-msft/microsoft-corporation/annual-reports/nasdaq-msft-2024-10K-241157360.pdf",
            "name": "Stocklight – Microsoft Annual Report 2024 Form 10-K (reproduction)"
        },
        {
            "url": "https://stockdividendscreener.com/technology/software/microsoft/microsoft-employees-distribution-by-region-and-by-role/",
            "name": "Stock Dividend Screener – Microsoft Employees Distribution by Region"
        }
    ]
}