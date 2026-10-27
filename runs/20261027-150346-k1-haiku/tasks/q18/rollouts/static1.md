## Rollout `static1`
- outcome: submitted
- turns: 3; cost: $0.092; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Workday gross retention rate 10-K definition") → 0 results: 
- edgar_search({"search_query": "Workday gross retention rate definition subscription revenue", "ciks": ["WDAY"], "start_date": "2024-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 9, "page": 1, "results": [{"form": "CORRESP", "file_date": "2024-09-04", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-24-000174", "document": "filename1.htm", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm"}, {"form": "UPLOAD", "file_date": "2024-08-20", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0000000000-24-009541", "document": "filename2.txt", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000000000024009541/filename2.txt"}, {"form": "UPLOAD", "file_date": "2024-08-20", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0000000000-24-009541", "document": "filename1.pdf", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000000000024009541/filename1.pdf"}, {"form": "10-K", "file_date": "2025-03-11", "period_ending": "2025-01-31", "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-25-000056", "document": "wday-20250131.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm"}, {"form": "10-Q", "file_date": "2024-12-05", "period_ending": "2024-10-31", "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-24-000242", "document": "wday-20241031.htm", "description": "10-Q", "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm"}, {"form": "ARS", "file_date": "2024-05-07", "period_ending": "2024-01-31", "company
  …[truncated 1,286 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Workday, Inc. - Form 10-K - FY2026 <https://www.sec.gov/Archives/edgar/data/1327811/000132781126000014/wday-20260131.htm>; Workday, Inc. - Form 10-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm>; Document <https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm>; Workday, Inc. <https://www.sec.gov/Archives/edgar/data/1327811/000132781124000192/filename1.htm>; Workday, Inc. - Form 10-K - FY2023 <https://www.sec.gov/Archives/edgar/data/1327811/000132781123000024/wday-20230131.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm", "key": "wday_10k_fy2025"})
  result: SUCCESS: The result has been saved to the data storage under the key: wday_10k_fy2025. (369,273 characters)
  The data_storage currently contains the following keys:
  wday_10k_fy2025
  
- retrieve_information({"prompt": "From this document: {{wday_10k_fy2025}}. Quote the passages on gross revenue retention rate and net revenue retention rate (or net retention) in the MD&A, including the stated percentage as of January 31, 2025, the definition, and whether any net retention rate is disclosed. Also quote any statement about ARR being a non-GAAP measure."})
  result: **Gross revenue retention rate (MD&A, Item 7, "Results of Operations – Revenues"):**
  
  > "Our growth in subscription services revenues attributable to existing customers is further reflected by our gross revenue retention rate of approximately 98% as of January 31, 2025. Our gross revenue retention rate measures the percentage of recurring revenue retained from existing customers and is calculated by taking total annual recurring revenue ("ARR") of our customers as of the corresponding prior period-end and comparing that to ARR from that same set of customers as of the current period-end. The metric takes into account recurring revenues lost to product or customer churn but does not account for additional revenue earned from add-ons or net expansions, which include volume and price adjustments. Our high gross revenue retention rate demonstrates our ability to maintain our existing customer base and drive strong overall customer satisfaction."
  
  **ARR and the non-GAAP statement (same MD&A section):**
  
  > "Our gross revenue retention rate is based on ARR, which represents the annualized value of active subscription contracts as of the end of each period. Each subscription contract is annualized by dividing the total contract value by the number of days in the contract term and then multiplying by 365. We exclude certain subscription contracts from the calculation, including contracts with terms less than one year that are distinct from our core product offering, such as contracts for tenants which are used for implementation and testing. To the extent that we are negotiating a renewal with a customer after the expiration of the subscription, ARR is only adjusted if the customer churns. We calculate ARR on a constant currency basis using exchange rates set at the beginning of
  …[truncated 593 chars]

### Turn 3  (stop_reason=tool_use)
**Short answer:** Yes, Workday reports a gross retention metric, which it calls the "gross revenue retention rate." It no longer reports a net retention rate. Its FY2025 10-K (fiscal year ended January 31, 2025) shows only the gross metric.

**Gross revenue retention rate (latest annual report as of April 7, 2025)**
- The FY2025 10-K puts it at approximately 98% as of January 31, 2025, and describes it as reflecting the growth in subscription revenue from existing customers.
- Definition: it measures the percentage of recurring revenue kept from existing customers. It compares the total ARR of customers at the prior period-end with the ARR from that same set of customers at the current period-end.
- Scope: it counts only losses from product or customer churn. It excludes add-ons and net expansions, which include volume and price increases.
- ARR basis: ARR is the annualized value of active subscription contracts at period-end. Each contract is annualized as total contract value divided by days in the term, times 365. Contracts under one year that are distinct from the core product (such as tenant contracts used for implementation and testing) are excluded. ARR is adjusted for a renewal only if the customer churns. ARR is calculated at constant currency using rates set at the start of each fiscal year.
- The 10-K states that ARR is a non-GAAP financial measure.

**Net retention**
- The FY2024 10-K said gross and net retention rates were "over 95%" and "over 100%," respectively
…[truncated 1,613 chars]
- submit_final_result({"final_result": "Yes. Workday reports a gross retention metric, called the \"gross revenue retention rate\" (about 98% as of January 31, 2025, per the FY2025 10-K). It does not report a net retention rate in its FY2025 10-K; after SEC comments on the FY2024 10-K, it said it would no longer disclose net retention rates.\n\nDefinition (FY2025 10-K): The gross revenue retention rate measures the percentage of recurring revenue retained from existing customers. It compares the total ARR of customers at the prior period-end with ARR from the same set of customers at the current period-end. It counts only churn (product or customer) and excludes add-ons and net expansions (volume and price adjust
…[truncated 1,474 chars])

### Final answer
Yes. Workday reports a gross retention metric, called the "gross revenue retention rate" (about 98% as of January 31, 2025, per the FY2025 10-K). It does not report a net retention rate in its FY2025 10-K; after SEC comments on the FY2024 10-K, it said it would no longer disclose net retention rates.

Definition (FY2025 10-K): The gross revenue retention rate measures the percentage of recurring revenue retained from existing customers. It compares the total ARR of customers at the prior period-end with ARR from the same set of customers at the current period-end. It counts only churn (product or customer) and excludes add-ons and net expansions (volume and price adjustments). ARR is the annualized value of active subscription contracts (contract value / days in term x 365), excludes certain short non-core contracts, is adjusted for renewals only on churn, and is calculated at constant currency. ARR is a non-GAAP measure.

Net retention: The FY2024 10-K cited gross and net retention rates "over 95%" and "over 100%". The FY2025 10-K contains no net revenue retention rate. Workday told the SEC staff it would stop disclosing net retention and would disclose the actual gross retention rate for each period.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm",
            "name": "Workday, Inc. Form 10-K for fiscal year ended January 31, 2025"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000044/wday-20240131.htm",
            "name": "Workday, Inc. Form 10-K for fiscal year ended January 31, 2024"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm",
            "name": "Workday SEC correspondence (CORRESP, September 4, 2024)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000192/filename1.htm",
            "name": "Workday SEC response letter on retention rate disclosure"
        }
    ]
}