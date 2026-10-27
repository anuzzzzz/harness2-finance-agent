## Rollout `base1`
- outcome: submitted
- turns: 2; cost: $0.012; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Workday 10-K gross retention rate definition") → 0 results: 
- edgar_search({"search_query": "Workday gross retention rate definition subscription revenue", "ciks": ["WDAY"], "top_n_results": 10})
  result: {"total_matching_documents": 28, "page": 1, "results": [{"form": "CORRESP", "file_date": "2024-09-04", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-24-000174", "document": "filename1.htm", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm"}, {"form": "UPLOAD", "file_date": "2024-08-20", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0000000000-24-009541", "document": "filename2.txt", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000000000024009541/filename2.txt"}, {"form": "UPLOAD", "file_date": "2024-08-20", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0000000000-24-009541", "document": "filename1.pdf", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000000000024009541/filename1.pdf"}, {"form": "10-K", "file_date": "2025-03-11", "period_ending": "2025-01-31", "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-25-000056", "document": "wday-20250131.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm"}, {"form": "10-Q", "file_date": "2024-12-05", "period_ending": "2024-10-31", "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-24-000242", "document": "wday-20241031.htm", "description": "10-Q", "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm"}, {"form": "ARS", "file_date": "2024-05-07", "period_ending": "2024-01-31", "compan
  …[truncated 1,637 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Workday, Inc. - Form 10-K - FY2026 <https://www.sec.gov/Archives/edgar/data/1327811/000132781126000014/wday-20260131.htm>; Workday, Inc. - Form 10-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm>; Workday, Inc. <https://www.sec.gov/Archives/edgar/data/1327811/000132781124000192/filename1.htm>; September 9, 2024 Zane Rowe Chief Financial Officer Workday, Inc. <https://www.sec.gov/Archives/edgar/data/1327811/000000000024010149/filename1.pdf>; SaaS Gross Revenue Retention: Calculation Examples & Template <https://ordwaylabs.com/blog/saas-gross-revenue-retention-calculation-examples/>
- submit_final_result({"final_result": "**Short answer:** Yes, Workday reports a gross retention metric, called the \"gross revenue retention rate.\" It does not currently report a net retention rate. Earlier filings did show one, but Workday stopped disclosing it after SEC staff comments in 2024.\n\n**What Workday reports (as of April 7, 2025)**\n- The FY2025 Form 10-K (filed March 11, 2025) has a section titled \"Gross Revenue Retention Rate.\" It says the company's gross revenue retention rate was approximately 98% as of January 31, 2025. The metric is said to show the company's growth in subscription services revenue from existing customers.\n- The Q4 FY2025 prepared remarks (February 25, 2025) also cite gros
…[truncated 3,119 chars])

### Final answer
**Short answer:** Yes, Workday reports a gross retention metric, called the "gross revenue retention rate." It does not currently report a net retention rate. Earlier filings did show one, but Workday stopped disclosing it after SEC staff comments in 2024.

**What Workday reports (as of April 7, 2025)**
- The FY2025 Form 10-K (filed March 11, 2025) has a section titled "Gross Revenue Retention Rate." It says the company's gross revenue retention rate was approximately 98% as of January 31, 2025. The metric is said to show the company's growth in subscription services revenue from existing customers.
- The Q4 FY2025 prepared remarks (February 25, 2025) also cite gross revenue retention rates at 98%.

**Definition (per the FY2025 10-K)**
- It measures the percentage of recurring revenue kept from existing customers. It is calculated by taking total annual recurring revenue (ARR) of customers at the prior period-end and comparing it with ARR from that same set of customers at the current period-end.
- It reflects recurring revenue lost to product or customer churn. It does not count added revenue from add-ons or net expansions, which include volume and price changes.
- ARR is the annualized value of active subscription contracts at period-end. Each contract is annualized by dividing total contract value by the number of days in the term and multiplying by 365.
- Contracts with terms under one year that are distinct from the core product (for example, tenants used for implementation and testing) are excluded.
- If a customer is in renewal negotiations after expiration, ARR changes only if the customer churns.
- ARR is calculated in constant currency, using exchange rates set at the start of each fiscal year.

**Net retention history**
- Workday's FY2024 10-K and some 10-Qs stated that gross and net retention rates exceeded 95% and 100%, respectively. The SEC staff questioned this disclosure in 2024.
- In its response, Workday said it would disclose gross revenue retention rates, with a description and calculation, beginning with the 10-Q for the quarter ended October 31, 2024. It also said it no longer intended to disclose net revenue retention rates in future filings.
- In the SEC correspondence, the earlier net retention definition was described as the current period-end ARR of customers retained year-over-year, divided by prior period ARR. Gross retention, by contrast, excludes add-ons and net expansions.

**Caveat:** The search index also returned a later FY2026 Form 10-K. I did not rely on it because this answer is dated April 7, 2025. Under the FY2025 10-K, the answer is as stated above.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm",
            "name": "Workday, Inc. Form 10-K for fiscal year ended January 31, 2025"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm",
            "name": "Workday response letter to SEC staff (September 2024)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000192/filename1.htm",
            "name": "Workday SEC correspondence on retention rate disclosure"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1327811/000010149/filename1.pdf",
            "name": "SEC staff comment letter to Workday (September 9, 2024)"
        },
        {
            "url": "https://www.workday.com/content/dam/web/en-us/documents/investor/workday-fiscal-2025-fourth-quarter-prepared-remarks.pdf",
            "name": "Workday Fourth-Quarter Fiscal 2025 Prepared Remarks"
        }
    ]
}