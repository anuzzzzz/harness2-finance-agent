## Rollout `ctl3`
- outcome: submitted
- turns: 3; cost: $0.014; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Workday subscription gross retention rate definition 10-K") → 0 results: 
- edgar_search({"search_query": "Workday gross retention rate definition subscription", "ciks": ["WDAY"], "start_date": "2024-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 9, "page": 1, "results": [{"form": "CORRESP", "file_date": "2024-09-04", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-24-000174", "document": "filename1.htm", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm"}, {"form": "UPLOAD", "file_date": "2024-08-20", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0000000000-24-009541", "document": "filename2.txt", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000000000024009541/filename2.txt"}, {"form": "UPLOAD", "file_date": "2024-08-20", "period_ending": null, "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0000000000-24-009541", "document": "filename1.pdf", "description": null, "url": "https://www.sec.gov/Archives/edgar/data/1327811/000000000024009541/filename1.pdf"}, {"form": "10-K", "file_date": "2025-03-11", "period_ending": "2025-01-31", "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-25-000056", "document": "wday-20250131.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm"}, {"form": "10-Q", "file_date": "2024-12-05", "period_ending": "2024-10-31", "company": "Workday, Inc.  (WDAY)  (CIK 0001327811)", "ciks": ["0001327811"], "accession": "0001327811-24-000242", "document": "wday-20241031.htm", "description": "10-Q", "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm"}, {"form": "ARS", "file_date": "2024-05-07", "period_ending": "2024-01-31", "company
  …[truncated 1,286 chars]

### Turn 2  (stop_reason=end_turn)
**Yes. Workday reports a gross retention metric, now called the gross revenue retention rate. It does not currently report a net retention rate.**

**Current figure (FY2025 10-K, as of April 7, 2025).** The most recent annual report I could find is the 10-K for the fiscal year ended January 31, 2025. It states that 
its gross revenue retention rate was approximately 98% as of January 31, 2025.


**Definition (per the FY2025 10-K):**
- 
The rate measures the percentage of recurring revenue retained from existing customers. It is calculated by taking total annual recurring revenue ("ARR") of customers as of the prior period-end and comparing that to ARR from that same set of customers as of the current period-end.

- 
It accounts for recurring revenues lost to product or customer churn, but it does not credit additional revenue from add-ons or net expansions, which include volume and price adjustments.

- ARR is 
the annualized value of active subscription contracts as of the end of each period.
 
Each subscription contract is annualized by dividing the total contract value by the number of days in the contract term and then multiplying by 365.

- 
Certain subscription contracts are excluded, including contracts with terms under one year that are distinct from the core product, such as tenant contracts used for implementation and testing.

- 
If a customer is negotiating a renewal after its subscription expires, ARR is adjusted only if the customer churns.


**Earlier net reten
…[truncated 1,564 chars]
- web_search(query=null) → 9 results: Workday, Inc. - Form 10-K - FY2026 <https://www.sec.gov/Archives/edgar/data/1327811/000132781126000014/wday-20260131.htm>; Workday, Inc. - Form 10-K - FY2025 <https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm>; Document <https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm>; Workday, Inc. - Form 10-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1327811/000132781124000044/wday-20240131.htm>; Workday, Inc. <https://www.sec.gov/Archives/edgar/data/1327811/000132781124000192/filename1.htm>

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "Yes. Workday (NASDAQ: WDAY) reports a gross retention metric, now called the gross revenue retention rate. As of April 7, 2025, it does not report a net retention rate.\n\n1. Current figure (FY2025 Form 10-K, fiscal year ended January 31, 2025): Workday states that its gross revenue retention rate was about 98% as of January 31, 2025.\n\n2. Definition (per the FY2025 10-K):\n- The rate shows the share of recurring revenue kept from existing customers. It compares the total annual recurring revenue (ARR) of customers at the prior period-end with the ARR from that same group of customers at the current period-end.\n- It counts recurring revenue lost to product or customer chu
…[truncated 2,006 chars])

### Final answer
Yes. Workday (NASDAQ: WDAY) reports a gross retention metric, now called the gross revenue retention rate. As of April 7, 2025, it does not report a net retention rate.

1. Current figure (FY2025 Form 10-K, fiscal year ended January 31, 2025): Workday states that its gross revenue retention rate was about 98% as of January 31, 2025.

2. Definition (per the FY2025 10-K):
- The rate shows the share of recurring revenue kept from existing customers. It compares the total annual recurring revenue (ARR) of customers at the prior period-end with the ARR from that same group of customers at the current period-end.
- It counts recurring revenue lost to product or customer churn. It does not credit add-ons or net expansion (volume and price increases).
- ARR is the annualized value of active subscription contracts at period-end. Each contract is annualized by dividing total contract value by the number of days in the term and multiplying by 365.
- Certain contracts are excluded from the calculation, including terms under one year that are separate from the core product (for example, tenant contracts used for implementation and testing).
- When a subscription is in renewal negotiations after expiry, ARR changes only if the customer churns.

3. Net retention history: The FY2024 10-K described gross and net retention rates of over 95% and over 100%, respectively, without a formal definition. Following SEC staff comments, Workday agreed to define both metrics starting with its 10-Q for the quarter ended October 31, 2024. A later SEC response letter (undated in the materials reviewed) said Workday no longer intends to disclose net revenue retention rates in future filings. Gross retention is the only retention metric it currently discloses.

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
            "name": "Workday SEC correspondence (CORRESP), September 4, 2024"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000192/filename1.htm",
            "name": "Workday SEC correspondence response letter (undated)"
        }
    ]
}