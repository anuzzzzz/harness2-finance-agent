## Rollout `ctl2`
- outcome: submitted
- turns: 3; cost: $0.025; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Workday gross retention rate definition 10-K") → 0 results: 
- edgar_search({"search_query": "Workday gross retention rate definition subscription revenue", "ciks": ["WDAY"], "top_n_results": 10})
  result: {"total_matching_documents": 28, "page": 1, "results": [{"form": "CORRESP", "file_date": "2024-09-04", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-24-000174", "document": "filename1.htm", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm"}, {"form": "UPLOAD", "file_date": "2024-08-20", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0000000000-24-009541", "document": "filename2.txt", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000000000024009541/filename2.txt"}, {"form": "UPLOAD", "file_date": "2024-08-20", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0000000000-24-009541", "document": "filename1.pdf", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000000000024009541/filename1.pdf"}, {"form": "10-K", "file_date": "2025-03-11", "period_ending": "2025-01-31", "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-25-000056", "document": "wday-20250131.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm"}, {"form": "10-Q", "file_date": "2024-12-05", "period_ending": "2024-10-31", "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-24-000242", "document": "wday-20241031.htm", "description": "10-Q", "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm"}, {"form": "ARS", "file_date": "2024-05-07", "period_ending": "2024-01-31", "compan
  …[truncated 1,637 chars]

### Turn 2  (stop_reason=end_turn)
**Short answer:** Yes, but only a gross metric. Workday reports a **gross revenue retention rate** (GRR) in its 10-K and 10-Q filings. It stopped disclosing a net retention rate after an SEC comment process in 2024.

**Gross revenue retention rate (current disclosure)**
- In its fiscal 2025 10-K (for the year ended January 31, 2025), Workday said its gross revenue retention rate was 
approximately 98% as of January 31, 2025.

- Its 10-Q for the quarter ended October 31, 2024 reported the same metric at 
98% as of October 31, 2024.

- Definition from the 10-K: the metric 
measures the percentage of recurring revenue retained from existing customers and is calculated by taking total annual recurring revenue ("ARR") of our customers as of the corresponding prior period-end and comparing that to ARR from that same set of customers as of the current period-end.

- It 
takes into account recurring revenues lost to product or customer churn but does not account for additional revenue earned from add-ons or net expansions, which include volume and price adjustments.

- ARR is 
the annualized value of active subscription contracts as of the end of each period.
 Each contract is annualized by 
dividing the total contract value by the number of days in the contract term and then multiplying by 365.
 Contracts under one year that are distinct from the core product, such as tenant contracts used for implementation and testing, are excluded.

**Net retention (historical, no longer reported
…[truncated 1,766 chars]
- web_search(query=null) → 10 results: Workday, Inc. - Form 10-K - FY2026 <https://www.sec.gov/Archives/edgar/data/1327811/000132781126000014/wday-20260131.htm>; Workday, Inc. - Form 10-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm>; Document <https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm>; Workday, Inc. - Form 10-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1327811/000132781123000024/wday-20230131.htm>; September 9, 2024 Zane Rowe Chief Financial Officer Workday, Inc. <https://www.sec.gov/Archives/edgar/data/1327811/000000000024010149/filename1.pdf>
- web_search(query="Workday net revenue retention rate definition 10-Q October 31, 2024") → 9 results: Workday, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm>; Workday, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1327811/000132781124000165/wday-20240731.htm>; Workday, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1327811/000132781124000093/wday-20240430.htm>; Workday, Inc. - Form 10-Q - FY2024 (Quarterly Earnings Tables - quarter ended Oct 2024) <https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/Financial_Report.xlsx>; Document <https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm>

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer:** Yes, Workday reports a gross retention metric, the **gross revenue retention rate (GRR)**, in both its annual and quarterly filings. It does not currently report a net retention rate. It did report one in 2024, then withdrew it after SEC staff comments.\n\n**1. Current gross revenue retention rate**\n- Fiscal 2025 Form 10-K (year ended January 31, 2025): GRR was about 98% at that date.\n- Form 10-Q for the quarter ended October 31, 2024: GRR was 98% at that date.\n\n**2. How Workday defines GRR (per the 10-K)**\n- It measures how much recurring revenue is kept from existing customers. Total ARR for customers at the prior period-end is compared with ARR from that
…[truncated 2,278 chars])

### Final answer
**Answer:** Yes, Workday reports a gross retention metric, the **gross revenue retention rate (GRR)**, in both its annual and quarterly filings. It does not currently report a net retention rate. It did report one in 2024, then withdrew it after SEC staff comments.

**1. Current gross revenue retention rate**
- Fiscal 2025 Form 10-K (year ended January 31, 2025): GRR was about 98% at that date.
- Form 10-Q for the quarter ended October 31, 2024: GRR was 98% at that date.

**2. How Workday defines GRR (per the 10-K)**
- It measures how much recurring revenue is kept from existing customers. Total ARR for customers at the prior period-end is compared with ARR from that same customer group at the current period-end.
- Churn from lost products or customers reduces the rate. Add-ons and net expansion (volume and price increases) are excluded, so they do not raise it.
- ARR is the annualized value of active subscription contracts at period-end. Each contract's total value is divided by its term in days and multiplied by 365.
- Contracts under one year that are separate from the core product, such as short tenant contracts used for implementation and testing, are left out. ARR changes during an unresolved renewal only if the customer churns.

**3. Net retention history**
- The fiscal 2024 10-K and 2024 10-Qs stated gross and net retention rates of over 95% and over 100%, respectively.
- The SEC staff questioned the net figure, in particular whether it was computed on the same customer set year over year. Workday first agreed to add a net revenue retention definition starting with the October 31, 2024 10-Q.
- In a later response, Workday said it would no longer include net revenue retention disclosure in its SEC filings. It said that metric largely duplicates the change in revenue from existing customers, which it would disclose instead, along with growth from new customers.

**Caveat:** Search results also included a later fiscal 2026 10-K. I excluded it because it postdates the April 7, 2025 reference date.

{"sources": [{"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm", "name": "Workday Form 10-K for fiscal year ended January 31, 2025"}, {"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm", "name": "Workday Form 10-Q for quarter ended October 31, 2024"}, {"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000044/wday-20240131.htm", "name": "Workday Form 10-K for fiscal year ended January 31, 2024"}, {"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm", "name": "Workday SEC correspondence (response to Form 10-K FY2024 comments)"}, {"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000192/filename1.htm", "name": "Workday SEC correspondence (later response on net revenue retention disclosure)"}]}