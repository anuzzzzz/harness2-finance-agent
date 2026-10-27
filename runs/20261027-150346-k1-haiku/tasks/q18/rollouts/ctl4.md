## Rollout `ctl4`
- outcome: submitted
- turns: 2; cost: $0.013; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Workday 10-K subscription gross retention rate calculation") → 0 results: 
- edgar_search({"search_query": "Workday subscription gross retention rate definition", "ciks": ["WDAY"], "end_date": "2025-04-07", "top_n_results": 10})
  result: {"total_matching_documents": 28, "page": 1, "results": [{"form": "CORRESP", "file_date": "2024-09-04", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-24-000174", "document": "filename1.htm", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm"}, {"form": "UPLOAD", "file_date": "2024-08-20", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0000000000-24-009541", "document": "filename2.txt", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000000000024009541/filename2.txt"}, {"form": "UPLOAD", "file_date": "2024-08-20", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0000000000-24-009541", "document": "filename1.pdf", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000000000024009541/filename1.pdf"}, {"form": "10-K", "file_date": "2025-03-11", "period_ending": "2025-01-31", "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-25-000056", "document": "wday-20250131.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm"}, {"form": "10-Q", "file_date": "2024-12-05", "period_ending": "2024-10-31", "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-24-000242", "document": "wday-20241031.htm", "description": "10-Q", "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm"}, {"form": "ARS", "file_date": "2023-05-10", "period_ending": "2023-01-31", "compan
  …[truncated 1,637 chars]

### Turn 2  (stop_reason=tool_use)
**Short answer:** Yes, Workday reports a gross retention metric, but it has stopped reporting a net retention metric. As of April 7, 2025, the most recent annual report is the fiscal 2025 Form 10-K, filed March 11, 2025.

**Gross revenue retention rate (reported)**
- The FY2025 10-K gives the rate as approximately 98% as of January 31, 2025. 
Workday's gross revenue retention rate is approximately 98% as of January 31, 2025.

- Definition: the metric 
measures the percentage of recurring revenue retained from existing customers and is calculated by taking total annual recurring revenue ("ARR") of customers as of the corresponding prior period-end and comparing that to ARR from that same set of customers as of the current period-end.

- Treatment of churn and expansion: 
it takes into account recurring revenues lost to product or customer churn but does not account for additional revenue earned from add-ons or net expansions, which include volume and price adjustments.

- ARR basis: 
ARR represents the annualized value of active subscription contracts as of the end of each period.
 Each contract is annualized by dividing total contract value by the contract term in days and multiplying by 365. Contracts under one year that are distinct from the core product, such as tenants used for implementation and testing, are excluded. 
ARR is only adjusted if the customer churns
 during a renewal negotiation that follows expiration. ARR is calculated on a constant currency basis using ex
…[truncated 1,876 chars]
- web_search(query=null) → 9 results: Workday, Inc. - Form 10-K - FY2026 <https://www.sec.gov/Archives/edgar/data/1327811/000132781126000014/wday-20260131.htm>; Workday, Inc. - Form 10-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm>; Workday, Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1327811/000132781124000044/wday-20240131.htm>; Workday, Inc. <https://www.sec.gov/Archives/edgar/data/1327811/000132781124000192/filename1.htm>; September 9, 2024 Zane Rowe Chief Financial Officer Workday, Inc. <https://www.sec.gov/Archives/edgar/data/1327811/000000000024010149/filename1.pdf>
- submit_final_result({"final_result": "Yes. Workday (WDAY) reports a gross retention metric, the gross revenue retention rate, but it no longer reports a net retention rate.\n\nGross revenue retention rate: The FY2025 10-K (filed March 11, 2025) gives the rate as approximately 98% as of January 31, 2025. Definition: it measures the percentage of recurring revenue retained from existing customers. It is calculated by taking total ARR of customers at the prior period-end and comparing it to ARR from the same set of customers at the current period-end. It accounts for recurring revenue lost to product or customer churn but excludes add-ons and net expansion (volume and price adjustments). ARR is the annualized valu
…[truncated 1,237 chars])

### Final answer
Yes. Workday (WDAY) reports a gross retention metric, the gross revenue retention rate, but it no longer reports a net retention rate.

Gross revenue retention rate: The FY2025 10-K (filed March 11, 2025) gives the rate as approximately 98% as of January 31, 2025. Definition: it measures the percentage of recurring revenue retained from existing customers. It is calculated by taking total ARR of customers at the prior period-end and comparing it to ARR from the same set of customers at the current period-end. It accounts for recurring revenue lost to product or customer churn but excludes add-ons and net expansion (volume and price adjustments). ARR is the annualized value of active subscription contracts (contract value divided by term days, times 365), excludes certain short non-core contracts (e.g., implementation/testing tenants), is adjusted only on churn during renewal negotiations, and is calculated at constant currency using fiscal-year-start exchange rates.

Net retention rate: The FY2024 10-K disclosed gross and net retention rates of over 95% and over 100%. Following SEC staff comments, Workday said it no longer intends to disclose net revenue retention rates, since it is largely duplicative of the change in revenue from existing customers. It will instead disclose the percentage change in subscription revenue attributable to existing and new customers, and will disclose the actual then-current gross revenue retention rate.

Sources:
- https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm (FY2025 10-K)
- https://www.sec.gov/Archives/edgar/data/1327811/000132781124000044/wday-20240131.htm (FY2024 10-K)
- https://www.sec.gov/Archives/edgar/data/1327811/000132781124000192/filename1.htm (Workday SEC response letter)
- https://www.sec.gov/Archives/edgar/data/1327811/000000000024010149/filename1.pdf (SEC staff comment letter, Sept 9, 2024)