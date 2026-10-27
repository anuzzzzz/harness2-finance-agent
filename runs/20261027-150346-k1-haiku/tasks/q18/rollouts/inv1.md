## Rollout `inv1`
- outcome: submitted
- turns: 3; cost: $0.096; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm", "key": "10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: 10k. (369,273 characters)
  The data_storage currently contains the following keys:
  10k
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm", "key": "corr"})
  result: SUCCESS: The result has been saved to the data storage under the key: corr. (10,327 characters)
  The data_storage currently contains the following keys:
  10k
  corr
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm", "key": "10q"})
  result: SUCCESS: The result has been saved to the data storage under the key: 10q. (264,510 characters)
  The data_storage currently contains the following keys:
  10k
  corr
  10q
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this SEC correspondence, explain what Workday says about the retention metric: the earlier gross and net retention wording, the switch to gross revenue retention, and whether the net retention rate was dropped. Quote briefly. Text: {{corr}}"})
  result: **Short answer:** The letter doesn't quote the original 10-K retention wording, so it can't show exactly what changed. It also shows that net revenue retention was kept, not dropped.
  
  **The earlier wording.** The Staff's comment is the only description of the prior disclosure. It says, "We note your disclosure of both gross and net retention rate." The letter doesn't reproduce that earlier language or its definitions.
  
  **The switch to "revenue" retention.** The Staff used "gross and net retention rate," while Workday's response consistently uses "gross and net revenue retention rates." The response doesn't call this a change or explain it. It frames the new language as applying to future filings: "in future filings, beginning with our Quarterly Report on Form 10-Q for the quarter ended October 31, 2024, we will disclose information about gross and net revenue retention rates, including a description and definition of each and how they are calculated."
  
  The proposed definitions are:
  - **Gross:** "measure[s] the percentage of recurring revenue retained from existing customers. The metric takes into account only negative impacts such as recurring revenues lost to product or customer churn, and does not account for additional revenue earned from add-ons or net expansions."
  - **Net:** "measure[s] the net change in recurring revenue from existing customers. The metric includes both positive and negative impacts on revenue, such as add-ons, net expansions, and product and customer churn."
  
  Both are calculated from ARR, and the proposed text says the metrics are "based on ARR."
  
  **Was net retention dropped?** No. The proposed revised disclosure states that "our gross and net revenue retention rates exceeding XX% and XX%, respectively, as of October 31, 2024," and gives a separa
  …[truncated 614 chars]
- retrieve_information({"prompt": "In this 10-K, find the key business metrics section and any \"Gross Revenue Retention Rate\" or \"retention\" definition. Give the verbatim heading, the calculation, what is included and excluded, and the period it applies to. Also state whether any net retention rate is mentioned. Text: {{10k}}"})
  result: ## Key Business Metrics Section
  
  - **Verbatim heading:** "Financial Results Overview" (Item 7, MD&A)
  - **Introductory sentence:** "The following table provides an overview of our key metrics (in millions, except percentages, basis points, and headcount data):"
  - **Metrics in the table:** Total revenues, subscription services revenues, GAAP and non-GAAP operating income and margin, operating and free cash flows, total subscription revenue backlog, 12-month subscription revenue backlog, cash and marketable securities, and headcount.
  
  The gross revenue retention rate is not in this table. It appears separately in the MD&A.
  
  ## Gross Revenue Retention Rate
  
  **Verbatim heading:** "Gross Revenue Retention Rate"
  
  **Reported value:** "our gross revenue retention rate of approximately 98% as of January 31, 2025."
  
  **Calculation:** The rate "measures the percentage of recurring revenue retained from existing customers and is calculated by taking total annual recurring revenue ("ARR") of our customers as of the corresponding prior period-end and comparing that to ARR from that same set of customers as of the current period-end."
  
  **Included:**
  - ARR from the prior-period customer set, measured at the current period-end.
  - Recurring revenue lost to product or customer churn, which reduces the rate.
  
  **Excluded:**
  - Additional revenue from add-ons or net expansions, including volume and price adjustments. The filing states the metric "does not account for additional revenue earned from add-ons or net expansions."
  - Subscription contracts with terms under one year that are distinct from the core product offering, such as tenant contracts used for implementation and testing.
  - For renewals still being negotiated after expiration, ARR is adjusted only if the customer churns.
  
  **ARR def
  …[truncated 1,313 chars]
- retrieve_information({"prompt": "In this 10-Q, find any \"Gross Revenue Retention Rate\" or \"retention\" definition or \"net retention\" mention. Give the verbatim definition, calculation, inclusions/exclusions, and period. Text: {{10q}}"})
  result: ## Gross Revenue Retention Rate
  
  The 10-Q discloses one retention metric: the **gross revenue retention rate**, reported as **98% as of October 31, 2024**. It appears in Item 2 (MD&A), under "Results of Operations – Revenues."
  
  **Verbatim definition:**
  
  > "Our growth in subscription services revenues attributable to existing customers is further reflected by our gross revenue retention rate of 98% as of October 31, 2024. Our gross revenue retention rate measures the percentage of recurring revenue retained from existing customers and is calculated by taking total annual recurring revenue ("ARR") of our customers as of the corresponding prior period-end and comparing that to ARR from that same set of customers as of the current period-end. The metric takes into account recurring revenues lost to product or customer churn but does not account for additional revenue earned from add-ons or net expansions, which include volume and price adjustments. Our high gross revenue retention rate demonstrates our ability to maintain our existing customer base and drive strong overall customer satisfaction."
  
  **Calculation (as described):**
  - Take total ARR of the customer set as of the corresponding prior period-end.
  - Compare it to ARR from that same set of customers as of the current period-end.
  - The filing does not give an explicit formula, but the description implies: current-period ARR from the prior-period customer cohort ÷ prior-period ARR of that cohort.
  - Recurring revenue lost to product or customer churn reduces the rate.
  - Add-ons, net expansions, volume increases, and price adjustments are not counted toward the rate.
  
  **ARR definition (used in the calculation):**
  > "Our gross revenue retention rate is based on ARR, which represents the annualized value of active subscri
  …[truncated 2,324 chars]

### Turn 3  (stop_reason=tool_use)
**Answer: Workday reports a gross revenue retention rate only. Its FY2025 10-K and its Q3 FY2025 10-Q do not report a net retention rate.**

**Gross revenue retention rate (reported)**
- The FY2025 10-K gives the rate as approximately 98% as of January 31, 2025, under the heading "Gross Revenue Retention Rate" in MD&A. The 10-K's "Financial Results Overview" key metrics table does not include it.
- The 10-Q for the quarter ended October 31, 2024 reports the rate as 98% as of that date, in the Results of Operations section of MD&A.

**Definition (from the 10-Q, with the 10-K consistent with it)**
- Measure: the rate measures the percentage of recurring revenue retained from existing customers.
- Calculation: total ARR of the customer set at the corresponding prior period-end is compared with ARR from that same set of customers at the current period-end. The filings give no explicit formula, so the ratio (current ARR of the prior-period cohort ÷ prior-period ARR of that cohort) is my reading of that description.
- Included: recurring revenue lost to product or customer churn, which reduces the rate.
- Excluded: revenue from add-ons or net expansions, including volume and price adjustments. The 10-K also excludes distinct contracts under one year, such as tenant contracts used for implementation and testing.
- Renewals: while a customer is being renegotiated after expiration, ARR is adjusted only if the customer churns.
- ARR basis: ARR is annualized from active subscription con
…[truncated 2,300 chars]
- submit_final_result({"final_result": "Answer: Workday reports a gross revenue retention rate only. Its FY2025 10-K and its Q3 FY2025 10-Q do not report a net retention rate.\n\nGross revenue retention rate (reported): The FY2025 10-K gives the rate as approximately 98% as of January 31, 2025, under the heading \"Gross Revenue Retention Rate\" in MD&A. It is not in the \"Financial Results Overview\" key metrics table. The 10-Q for the quarter ended October 31, 2024 reports the rate as 98% as of that date, in the Results of Operations section of MD&A.\n\nDefinition (from the 10-Q, consistent with the 10-K): The rate measures the percentage of recurring revenue retained from existing customers. Total ARR of the cu
…[truncated 2,381 chars])

### Final answer
Answer: Workday reports a gross revenue retention rate only. Its FY2025 10-K and its Q3 FY2025 10-Q do not report a net retention rate.

Gross revenue retention rate (reported): The FY2025 10-K gives the rate as approximately 98% as of January 31, 2025, under the heading "Gross Revenue Retention Rate" in MD&A. It is not in the "Financial Results Overview" key metrics table. The 10-Q for the quarter ended October 31, 2024 reports the rate as 98% as of that date, in the Results of Operations section of MD&A.

Definition (from the 10-Q, consistent with the 10-K): The rate measures the percentage of recurring revenue retained from existing customers. Total ARR of the customer set at the corresponding prior period-end is compared with ARR from that same set of customers at the current period-end. No explicit formula is given; the ratio (current ARR of the prior-period cohort divided by prior-period ARR of that cohort) is my reading. Included: recurring revenue lost to product or customer churn, which reduces the rate. Excluded: add-on or net expansion revenue, including volume and price adjustments; the 10-K also excludes distinct contracts under one year (e.g., tenant contracts for implementation and testing). Renewals: while a customer is renegotiated after expiration, ARR is adjusted only if the customer churns. ARR basis: annualized active subscription contracts (contract value / days in term x 365), at constant currency using rates set at fiscal-year start; ARR is a non-GAAP measure. Period: the 10-Q does not state the exact prior-period date (presumably October 31, 2023); the 10-K does not label the window as trailing twelve months.

Net retention rate (not reported): Neither filing reports or defines a net revenue retention percentage. "Net expansions" appears only as an item the gross metric excludes.

SEC correspondence (September 4, 2024): The SEC staff noted Workday's disclosure of both gross and net retention rates. Workday's response said that beginning with the 10-Q for the quarter ended October 31, 2024 it would disclose gross and net revenue retention rates with definitions and calculations. The draft net definition covers net change in recurring revenue from existing customers, including add-ons, net expansions and churn. This contradicts the filings: the 10-Q, which the letter named as the first filing to include the new disclosure, and the 10-K report only gross revenue retention. I could not determine from the sources why the net rate was omitted. The letter also says Workday does not treat either metric as a KPI and that exact historical rates were redacted in the public version.

Sources:
- Workday FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm
- Workday Form 10-Q (quarter ended October 31, 2024): https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm
- Workday SEC correspondence letter (September 4, 2024): https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm