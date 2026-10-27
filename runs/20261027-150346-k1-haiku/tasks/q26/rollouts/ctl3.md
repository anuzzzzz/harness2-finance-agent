## Rollout `ctl3`
- outcome: submitted
- turns: 2; cost: $0.012; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Microsoft 10-K fiscal 2024 employees full-time U.S. and international") → 0 results: 
- edgar_search({"search_query": "Microsoft full-time employees June 30, 2024 United States international", "ciks": ["0000789019"], "start_date": "2024-07-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 0, "page": 1, "results": [], "hint": "No documents matched. Try fewer/shorter terms, drop the form filter, widen the dates, or check the company's CIK/ticker."}

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: MICROSOFT CORP - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm>; MICROSOFT CORP - Form 10-K - FY2024 (Annual Financial Statement Tables - full year 2024) <https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/Financial_Report.xlsx>; Microsoft Employees by Year: 223,000 in 2026 (10-K) <https://fourweekmba.com/microsoft-employees-number/>; UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549 <https://microsoft.gcs-web.com/static-files/8a9beeed-0e9e-48e6-b4fb-593d558e2693>; Microsoft is stuck at 228,000 employees and that's by design <https://sqmagazine.co.uk/how-many-people-work-at-microsoft/>
- submit_final_result({"final_result": "**Answer: about 44.74% of Microsoft's full-time employees were located outside the United States as of June 30, 2024.**\n\n**Inputs (from the FY2024 Form 10-K, human capital section):** <cite index=\"6-3\">As of June 30, 2024, Microsoft employed approximately 228,000 people on a full-time basis, 126,000 in the U.S. and 102,000 internationally.</cite>\n\n**Calculation:**\n- Total full-time employees: 228,000\n- Employees outside the U.S. (international): 102,000\n- Check: 126,000 (U.S.) + 102,000 (international) = 228,000, which matches the reported total.\n- Percentage outside the U.S. = 102,000 / 228,000 × 100 = 44.736...% ≈ **44.74%**\n\n(For reference, the U.S. share is 
…[truncated 1,433 chars])

### Final answer
**Answer: about 44.74% of Microsoft's full-time employees were located outside the United States as of June 30, 2024.**

**Inputs (from the FY2024 Form 10-K, human capital section):** <cite index="6-3">As of June 30, 2024, Microsoft employed approximately 228,000 people on a full-time basis, 126,000 in the U.S. and 102,000 internationally.</cite>

**Calculation:**
- Total full-time employees: 228,000
- Employees outside the U.S. (international): 102,000
- Check: 126,000 (U.S.) + 102,000 (international) = 228,000, which matches the reported total.
- Percentage outside the U.S. = 102,000 / 228,000 × 100 = 44.736...% ≈ **44.74%**

(For reference, the U.S. share is 126,000 / 228,000 = 55.26%.)

**Note on sources:** A secondary summary (sqmagazine) lists the June 30, 2024 U.S. count as 126,000 and the international count as 102,000, consistent with the 10-K. The FY2025 10-K reports the same 228,000 total for June 30, 2025 but splits it as 125,000 U.S. and 103,000 international, which does not apply to the June 30, 2024 date asked about. I used the FY2024 10-K figures because they are the figures as of the requested date.

{
    "sources": [
        {
            "url": "https://stocklight.com/stocks/us/nasdaq-msft/microsoft-corporation/annual-reports/nasdaq-msft-2024-10K-241157360.pdf",
            "name": "Microsoft Corporation Annual Report 2024 Form 10-K (FY ended June 30, 2024), via StockLight"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm",
            "name": "Microsoft Form 10-K FY2024 (SEC EDGAR)"
        },
        {
            "url": "https://stocklight.com/stocks/us/nasdaq-msft/microsoft-corporation/annual-reports/nasdaq-msft-2025-10K-251167157.pdf",
            "name": "Microsoft Corporation Annual Report 2025 Form 10-K, via StockLight"
        },
        {
            "url": "https://sqmagazine.co.uk/how-many-people-work-at-microsoft/",
            "name": "SQ Magazine – How many people work at Microsoft"
        }
    ]
}