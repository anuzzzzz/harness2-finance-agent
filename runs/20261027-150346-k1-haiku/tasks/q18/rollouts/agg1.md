## Rollout `agg1`
- outcome: submitted
- turns: 5; cost: $0.098; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm", "key": "wday10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: wday10k. (369,273 characters)
  The data_storage currently contains the following keys:
  wday10k
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm", "key": "corr1"})
  result: SUCCESS: The result has been saved to the data storage under the key: corr1. (10,327 characters)
  The data_storage currently contains the following keys:
  wday10k
  corr1
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000192/filename1.htm", "key": "corr2"})
  result: SUCCESS: The result has been saved to the data storage under the key: corr2. (6,605 characters)
  The data_storage currently contains the following keys:
  wday10k
  corr1
  corr2
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Workday 10-K text, quote verbatim the \"Gross Revenue Retention Rate\" subsection: its heading, how it is calculated, what it includes and excludes, the period it applies to, and whether any net retention rate is reported. Also state whether any \"net revenue retention\" or \"net retention\" metric appears anywhere. {{wday10k}}"})
  result: **Gross Revenue Retention Rate** (Item 7, MD&A, "Results of Operations – Revenues")
  
  The heading reads: "Gross Revenue Retention Rate"
  
  The subsection text reads, verbatim:
  
  > "Our growth in subscription services revenues attributable to existing customers is further reflected by our gross revenue retention rate of approximately 98% as of January 31, 2025. Our gross revenue retention rate measures the percentage of recurring revenue retained from existing customers and is calculated by taking total annual recurring revenue ("ARR") of our customers as of the corresponding prior period-end and comparing that to ARR from that same set of customers as of the current period-end. The metric takes into account recurring revenues lost to product or customer churn but does not account for additional revenue earned from add-ons or net expansions, which include volume and price adjustments. Our high gross revenue retention rate demonstrates our ability to maintain our existing customer base and drive strong overall customer satisfaction.
  >
  > Our gross revenue retention rate is based on ARR, which represents the annualized value of active subscription contracts as of the end of each period. Each subscription contract is annualized by dividing the total contract value by the number of days in the contract term and then multiplying by 365. We exclude certain subscription contracts from the calculation, including contracts with terms less than one year that are distinct from our core product offering, such as contracts for tenants which are used for implementation and testing. To the extent that we are negotiating a renewal with a customer after the expiration of the subscription, ARR is only adjusted if the customer churns. We calculate ARR on a constant currency basis using exchange
  …[truncated 1,627 chars]
- retrieve_information({"prompt": "This is SEC correspondence from Workday. Quote verbatim what it says about the company's retention rate metrics (gross and net), including any commitment to disclose or stop disclosing a metric, and the date. {{corr1}}"})
  result: **Date:** The letter is dated **September 4, 2024**. It responds to the Staff's letter dated August 20, 2024.
  
  **1. Commitment to add a description, definition, and calculation method (future filings, beginning with the 10-Q for the quarter ended October 31, 2024)**
  
  > "We advise the Staff that in future filings, beginning with our Quarterly Report on Form 10-Q for the quarter ended October 31, 2024, we will disclose information about gross and net revenue retention rates, including a description and definition of each and how they are calculated."
  
  **2. Proposed disclosure of the rates and their definitions**
  
  > "Our growth with existing customers is further reflected by our gross and net revenue retention rates exceeding XX% and XX%, respectively, as of October 31, 2024. Gross revenue retention rates measure the percentage of recurring revenue retained from existing customers. ... Gross revenue retention rates are calculated by taking the current period-end annual recurring revenue ("ARR") of our customers that we retained year-over-year, excluding add-ons and net expansions, divided by the total ARR at the end of the corresponding prior period. ... Net revenue retention rates measure the net change in recurring revenue from existing customers. ... Net revenue retention rates are calculated by taking the current period-end ARR of our customers that we retained year-over-year, including add-ons and net expansion, divided by the total ARR at the end of the corresponding prior period."
  
  The proposed text is longer, and the ellipses above omit the descriptive sentences about revenue impacts, the ARR methodology, and the exclusions.
  
  **3. Whether the metrics are key performance indicators, and whether exact figures are disclosed**
  
  > "We respectfully advise the staff that 
  …[truncated 1,727 chars]
- retrieve_information({"prompt": "This is SEC correspondence from Workday. Quote verbatim what it says about the company's retention rate metrics (gross and net), including any commitment or final position on net retention, and the date. {{corr2}}"})
  result: **Date:** September 19, 2024 (the response letter, signed by CFO Zane Rowe)
  
  **Staff comment (quoted in the letter):**
  > "We note you currently disclose that gross and net retention rates exceeded 95% and 100%, respectively, for the periods presented in your recent Form 10-K and Form 10-Q filings. To the extent you intend to provide similar disclosures in future filings, revise to ensure that the amounts provided appropriately reflect your current net retention rates."
  
  **Company response on net retention (final position):**
  > "We respectfully acknowledge the Staff's comment and advise the Staff that upon further consideration and in light of our planned quantification of factors contributing to changes in subscription services revenues, we no longer intend to include disclosure related to net revenue retention rates in our SEC filings. ... We believe that the net revenue retention rate is largely duplicative of the change in revenue from existing customers as a measure of our business performance."
  
  And in the second comment response:
  > "As discussed in our response to comment 1 above, we no longer intend to disclose net revenue retention rates in our future filings."
  
  **Gross retention commitment:**
  > "As gross revenue retention provides insight into the recurring revenue retained from our existing customers, we currently intend to continue disclosing our gross revenue retention rate in future filings. Furthermore, upon further consideration and in light of your comments, we plan to disclose the actual, then-current gross revenue retention rate for each period in future filings."
  
  **Calculation clarification:**
  > "[T]he net and gross revenue retention rates are calculated using ARR attributable to existing customers from the corresponding period and comparing that to 
  …[truncated 405 chars]

### Turn 3  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm", "key": "wday10q"})
  result: SUCCESS: The result has been saved to the data storage under the key: wday10q. (264,510 characters)
  The data_storage currently contains the following keys:
  wday10k
  corr1
  corr2
  wday10q
  

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Workday 10-Q for the quarter ended October 31, 2024, state whether it reports a gross revenue retention rate and/or a net revenue retention rate. If gross is reported, quote its definition/calculation verbatim. State whether any net retention rate is reported. {{wday10q}}"})
  result: **Gross revenue retention rate: reported. Net revenue retention rate: not reported.**
  
  The 10-Q reports a gross revenue retention rate of 98% as of October 31, 2024, in Item 2 (MD&A), under "Results of Operations – Revenues." The filing's definition reads:
  
  > "Our growth in subscription services revenues attributable to existing customers is further reflected by our gross revenue retention rate of 98% as of October 31, 2024. Our gross revenue retention rate measures the percentage of recurring revenue retained from existing customers and is calculated by taking total annual recurring revenue ("ARR") of our customers as of the corresponding prior period-end and comparing that to ARR from that same set of customers as of the current period-end. The metric takes into account recurring revenues lost to product or customer churn but does not account for additional revenue earned from add-ons or net expansions, which include volume and price adjustments. Our high gross revenue retention rate demonstrates our ability to maintain our existing customer base and drive strong overall customer satisfaction."
  
  The filing also defines the ARR underlying the metric:
  
  > "Our gross revenue retention rate is based on ARR, which represents the annualized value of active subscription contracts as of the end of each period. Each subscription contract is annualized by dividing the total contract value by the number of days in the contract term and then multiplying by 365. We exclude certain subscription contracts from the calculation, including contracts with terms less than one year that are distinct from our core product offering, such as contracts for tenants which are used for implementation and testing. To the extent that we are negotiating a renewal with a customer after the expiration
  …[truncated 831 chars]

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "Short answer: Yes, Workday reports a gross revenue retention rate (GRR) in its annual and quarterly reports. It does not report a net revenue retention rate in either.\n\n1. Annual report (FY2025 10-K, period ended January 31, 2025)\nThe 10-K reports a gross revenue retention rate of approximately 98% as of January 31, 2025, in MD&A under Results of Operations – Revenues. The company says this rate measures the share of recurring revenue kept from existing customers. It is calculated by taking the total annual recurring revenue (ARR) of customers at the prior period-end and comparing it with the ARR from that same set of customers at the current period-end. (Source: FY2025 
…[truncated 3,492 chars])

### Final answer
Short answer: Yes, Workday reports a gross revenue retention rate (GRR) in its annual and quarterly reports. It does not report a net revenue retention rate in either.

1. Annual report (FY2025 10-K, period ended January 31, 2025)
The 10-K reports a gross revenue retention rate of approximately 98% as of January 31, 2025, in MD&A under Results of Operations – Revenues. The company says this rate measures the share of recurring revenue kept from existing customers. It is calculated by taking the total annual recurring revenue (ARR) of customers at the prior period-end and comparing it with the ARR from that same set of customers at the current period-end. (Source: FY2025 10-K.)
- Includes: revenue lost to product or customer churn.
- Excludes: add-ons and net expansions, meaning volume and price increases. The metric does not count that extra revenue.
- ARR basis: ARR is the annualized value of active subscription contracts. Each contract is annualized by dividing total contract value by its term in days and multiplying by 365. Contracts with terms under one year that are distinct from the core product (for example, implementation and testing tenants) are excluded. For renewals still under negotiation after expiration, ARR changes only if the customer churns. ARR is calculated at constant currency using exchange rates set at the start of each fiscal year. ARR is a non-GAAP measure.
- The 10-K does not report any net retention rate. It mentions net expansion only to say the GRR excludes it.

2. Quarterly report (10-Q for the quarter ended October 31, 2024)
The 10-Q reports a gross revenue retention rate of 98% as of October 31, 2024, using the same definition and ARR methodology as the 10-K. It does not report a net revenue retention rate. It does say that about 60% of the year-over-year increase in subscription services revenue came from expansion within existing customers. That is a revenue attribution, not a retention percentage. (Source: Q3 FY2025 10-Q.)

3. Why net retention is absent (SEC correspondence)
- In a September 4, 2024 response letter, Workday said it would disclose gross and net revenue retention rates with definitions beginning with the October 31, 2024 10-Q. It also said it does not treat these metrics as key performance indicators and would not disclose exact figures. (Source: SEC letter dated 2024-09-04.)
- In a September 19, 2024 response, after an SEC staff comment on net retention, Workday said it no longer intended to include net revenue retention rates in its SEC filings. It cited its planned quantification of factors driving subscription services revenue changes and said the net rate largely duplicates the change in revenue from existing customers. It said it would continue to disclose gross revenue retention and would report the actual rate for each period. (Source: SEC letter dated 2024-09-19.)
- The 10-Q and 10-K are consistent with that final position: only gross retention is reported.

Conclusion: Workday's annual and quarterly filings report only a gross revenue retention rate (about 98% in both the FY2025 10-K and the Q3 FY2025 10-Q). Net revenue retention was proposed in 2024 correspondence but later dropped and does not appear in those filings.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm",
            "name": "Workday FY2025 Form 10-K (period ended January 31, 2025)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm",
            "name": "Workday Form 10-Q for the quarter ended October 31, 2024"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm",
            "name": "Workday SEC correspondence response dated September 4, 2024"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000192/filename1.htm",
            "name": "Workday SEC correspondence response dated September 19, 2024"
        }
    ]
}