## Rollout `ctl2`
- outcome: submitted
- turns: 2; cost: $0.012; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Microsoft full-time employees June 30, 2024 United States international", "ciks": ["0000789019"], "start_date": "2024-07-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 0, "page": 1, "results": [], "hint": "No documents matched. Try fewer/shorter terms, drop the form filter, widen the dates, or check the company's CIK/ticker."}

### Turn 2  (stop_reason=tool_use)
- web_search(query="Microsoft 10-K fiscal 2024 employees full-time United States outside") → 10 results: MICROSOFT CORP - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm>; MICROSOFT CORP - Form 10-K - FY2024 (Annual Financial Statement Tables - full year 2024) <https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/Financial_Report.xlsx>; Microsoft Workforce 2026: 228,000 Employees and the First Hiring Plateau in a Decade <https://sqmagazine.co.uk/how-many-people-work-at-microsoft/>; Microsoft Corporation Annual Report 2026 Form 10-K (NASDAQ: ... <https://stocklight.com/stocks/us/nasdaq-msft/microsoft-corporation/annual-reports/nasdaq-msft-2026-10K-261217433.pdf>; Microsoft's total number of employees has... <https://www.chaincatcher.com/en/article/2298072>
- submit_final_result({"final_result": "**Answer: about 44.74% of Microsoft's full-time employees were located outside the United States as of June 30, 2024.**\n\n**Inputs (from Microsoft's FY2024 Form 10-K, fiscal year ended June 30, 2024):**\n- The Human Capital section of Microsoft's 2024 annual report reports a total of approximately 228,000 full-time employees, with 126,000 based in the U.S. and 102,000 international (<cite index=\"9-2\">As of June 30, 2024, we employed approximately 228,000 people on a full-time basis, 126,000 in the U.S. and 102,000 internationally.</cite>)\n- A secondary source (sqmagazine) also lists 126,000 U.S. employees for June 30, 2024, which matches the 10-K figure. Other sources c
…[truncated 936 chars])

### Final answer
**Answer: about 44.74% of Microsoft's full-time employees were located outside the United States as of June 30, 2024.**

**Inputs (from Microsoft's FY2024 Form 10-K, fiscal year ended June 30, 2024):**
- The Human Capital section of Microsoft's 2024 annual report reports a total of approximately 228,000 full-time employees, with 126,000 based in the U.S. and 102,000 international (<cite index="9-2">As of June 30, 2024, we employed approximately 228,000 people on a full-time basis, 126,000 in the U.S. and 102,000 internationally.</cite>)
- A secondary source (sqmagazine) also lists 126,000 U.S. employees for June 30, 2024, which matches the 10-K figure. Other sources cite 228,000 as the FY2024 total, consistent with the filing.

**Calculation:**
- International (non-U.S.) employees = 102,000
- Total full-time employees = 228,000 (check: 126,000 + 102,000 = 228,000)
- Share outside the U.S. = 102,000 / 228,000 = 0.447368... = **44.74%**
- For reference, the U.S. share is 126,000 / 228,000 = 55.26%.

**Note:** Microsoft reports these headcounts rounded to the nearest thousand, so the percentage is approximate.

**Sources:**
{
    "sources": [
        {
            "url": "https://www.microsoft.com/investor/reports/ar24/",
            "name": "Microsoft 2024 Annual Report (Form 10-K, FY2024 Human Capital Resources)"
        },
        {
            "url": "https://sqmagazine.co.uk/how-many-people-work-at-microsoft/",
            "name": "SQ Magazine – How many people work at Microsoft (cross-check of June 30, 2024 U.S. headcount)"
        }
    ]
}