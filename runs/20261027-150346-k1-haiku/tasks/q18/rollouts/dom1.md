## Rollout `dom1`
- outcome: submitted
- turns: 7; cost: $0.184; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "company_kpi_definition_lookup"})
  result: ---
  name: company_kpi_definition_lookup
  description: Answer "does the company report metric X (retention, churn, ARR, backlog, etc.) and how does it define it" from the 10-K/10-Q, including how the disclosure changed over time.
  ---
  ANALYTIC MOVE: classify and trace. Decide whether the company reports the metric, in which documents, with what exact definition and latest value, and whether the disclosure changed.
  
  1. Controlling source: the latest 10-K before the as-of date, in Item 7 MD&A "Key Business Metrics" or a section named for the metric. Check the latest 10-Q too. Earnings releases and prepared remarks only repeat the value. Retrieve the heading, the definition, the value and its as-of date, all from the opened text.
  2. Check the gross and the net variant separately. Report each as reported, or state "not reported" only after retrieving from the relevant section of the opened filing. Do not infer absence from one failed retrieval. Re-ask with different wording.
  3. Definition contract. Give the company's own wording on: the numerator and denominator (or what is compared); what is included and excluded (expansion, price, churn, contract terms under one year); the measurement basis (ARR, constant currency, annualisation method); and the measurement date. Give the latest value with its date and unit.
  4. Disclosure history. Metrics are sometimes changed after SEC staff comment letters. Check the prior-year 10-K and the CORRESP/UPLOAD letters in edgar_search results. Open them before saying a metric was dropped or added, and give the period of the change. Open the letters if you cite them.
  5. Answer: yes/no per metric, then the definition, the value with its date, and the history. State plainly anything you did not verify.
  
  Task facts (Workday, WDAY; from search result
  …[truncated 942 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm", "key": "wday10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: wday10k. (369,273 characters)
  The data_storage currently contains the following keys:
  wday10k
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm", "key": "wday10q"})
  result: SUCCESS: The result has been saved to the data storage under the key: wday10q. (264,510 characters)
  The data_storage currently contains the following keys:
  wday10k
  wday10q
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Workday 10-K text: {{wday10k}} — Find the \"Key Business Metrics\" section or any section on Gross Revenue Retention Rate / Subscription Revenue Retention / net retention. Quote the heading, the full definition (numerator, denominator, what is included/excluded, measurement basis, measurement date), the reported value and its as-of date, and any statement about net retention rate being discontinued or changed. Also state whether a net retention rate is reported."})
  result: The filing has no section titled "Key Business Metrics." The closest match is **"Gross Revenue Retention Rate,"** a subsection of Item 7 (MD&A), under "Results of Operations" > "Revenues," immediately after the revenue table. It is not in the "Financial Results Overview" key metrics table.
  
  **Heading:** "Gross Revenue Retention Rate"
  
  **Reported value and as-of date:** "our gross revenue retention rate of approximately 98% as of January 31, 2025."
  
  **Definition, as stated in the filing:**
  
  - **What it measures:** "the percentage of recurring revenue retained from existing customers."
  - **Calculation:** "calculated by taking total annual recurring revenue ('ARR') of our customers as of the corresponding prior period-end and comparing that to ARR from that same set of customers as of the current period-end."
  - **Numerator and denominator:** The filing describes the comparison (current-period ARR from the prior-period customer set against prior-period ARR) but does not state a formula in those terms.
  - **Included/excluded:** "The metric takes into account recurring revenues lost to product or customer churn but does not account for additional revenue earned from add-ons or net expansions, which include volume and price adjustments."
  - **Measurement basis:** ARR, which "represents the annualized value of active subscription contracts as of the end of each period." Each contract is "annualized by dividing the total contract value by the number of days in the contract term and then multiplying by 365."
  - **Exclusions from ARR:** "contracts with terms less than one year that are distinct from our core product offering, such as contracts for tenants which are used for implementation and testing."
  - **Renewals:** "To the extent that we are negotiating a renewal with a customer a
  …[truncated 1,030 chars]
- retrieve_information({"prompt": "From this Workday 10-Q text: {{wday10q}} — Find any \"Key Business Metrics\" section, gross retention rate, or net retention rate disclosure. Quote the heading, definition, value and as-of date, and any statement about discontinuing net retention disclosure."})
  result: The filing has no section titled "Key Business Metrics." The retention disclosure appears under a different heading.
  
  **Heading:** "Gross Revenue Retention Rate," in Item 2, MD&A, under "Results of Operations" > "Revenues."
  
  **Value and as-of date:** 98% as of October 31, 2024.
  
  **Quoted text:** "Our growth in subscription services revenues attributable to existing customers is further reflected by our gross revenue retention rate of 98% as of October 31, 2024. Our gross revenue retention rate measures the percentage of recurring revenue retained from existing customers and is calculated by taking total annual recurring revenue ("ARR") of our customers as of the corresponding prior period-end and comparing that to ARR from that same set of customers as of the current period-end. The metric takes into account recurring revenues lost to product or customer churn but does not account for additional revenue earned from add-ons or net expansions, which include volume and price adjustments."
  
  The filing also states that ARR is calculated per subscription contract (total contract value divided by contract-term days, times 365), excludes certain short-term or non-core contracts, is measured on a constant-currency basis using exchange rates set at the beginning of each fiscal year, and is a non-GAAP measure.
  
  **Net retention rate:** The filing does not disclose a net retention rate. It does not use that term.
  
  **Discontinuation statement:** None. The filing does not say that Workday is discontinuing any retention disclosure.
  
  The "Financial Results Overview" table in MD&A lists the other operating metrics (subscription revenue backlog, 12-month backlog, cash and marketable securities, and headcount), but it does not include a retention rate.

### Turn 4  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm", "key": "corresp"})
  result: SUCCESS: The result has been saved to the data storage under the key: corresp. (10,327 characters)
  The data_storage currently contains the following keys:
  wday10k
  wday10q
  corresp
  
- retrieve_information({"prompt": "From this Workday 10-K text: {{wday10k}} — Does the filing mention \"net retention\" or \"subscription revenue retention\" or a prior-year net retention rate? Quote any sentence describing a change in how retention is disclosed."})
  result: **No.** The filing does not mention "net retention," "net revenue retention," or "subscription revenue retention." It discloses only a **gross revenue retention rate**, and it gives no prior-year figure for that metric.
  
  The only retention disclosure is in MD&A, under "Gross Revenue Retention Rate":
  
  > "Our growth in subscription services revenues attributable to existing customers is further reflected by our gross revenue retention rate of approximately 98% as of January 31, 2025."
  
  The filing also defines the metric and says what it excludes:
  
  > "The metric takes into account recurring revenues lost to product or customer churn but does not account for additional revenue earned from add-ons or net expansions, which include volume and price adjustments."
  
  The filing does not describe any change in how retention is calculated or disclosed. The "Change in Non-GAAP Financial Measures" section refers to changes in excluded items for operating income (acquisition-related and restructuring costs), not to retention metrics.

### Turn 5  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this SEC correspondence letter: {{corresp}} — Quote what Workday says about net retention rate disclosure, including whether it will stop disclosing it, the period it applies from, and what it will disclose instead. Quote the sentences."})
  result: Workday does not say it will stop disclosing net revenue retention. It says it will expand the disclosure, starting with the Form 10-Q for the quarter ended October 31, 2024, and will report the rate as a threshold rather than an exact figure. The relevant sentences are:
  
  **Period and scope of the change:**
  > "We advise the Staff that in future filings, beginning with our Quarterly Report on Form 10-Q for the quarter ended October 31, 2024, we will disclose information about gross and net revenue retention rates, including a description and definition of each and how they are calculated."
  
  **Proposed disclosure:**
  > "Our growth with existing customers is further reflected by our gross and net revenue retention rates exceeding XX% and XX%, respectively, as of October 31, 2024."
  
  **Definition of net revenue retention:**
  > "Net revenue retention rates measure the net change in recurring revenue from existing customers. The metric includes both positive and negative impacts on revenue, such as add-ons, net expansions, and product and customer churn. Net revenue retention rates are calculated by taking the current period-end ARR of our customers that we retained year-over-year, including add-ons and net expansion, divided by the total ARR at the end of the corresponding prior period."
  
  **Why exact figures are not disclosed:**
  > "Since we do not consider these metrics to be key performance indicators, we do not disclose the exact figures. Providing these amounts with greater precision may suggest that small fluctuations are indicative of fundamental changes in our retention patterns, which we believe is unfounded and potentially misleading for readers."
  
  **Future treatment of changes:**
  > "In future filings, to the extent any changes in our revenue retention rates are materia
  …[truncated 517 chars]

### Turn 6  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Workday 10-Q text: {{wday10q}} — Search for the phrases \"net revenue retention\", \"net retention\", \"net expansion\", and \"exceeding\". Quote every sentence containing them, or state that none appear."})
  result: Only one of the four phrases appears. "Net expansion" (in the plural form "net expansions") occurs in one sentence, in the Gross Revenue Retention Rate discussion in Item 2:
  
  "The metric takes into account recurring revenues lost to product or customer churn but does not account for additional revenue earned from add-ons or net expansions, which include volume and price adjustments."
  
  "Net revenue retention," "net retention," and "exceeding" do not appear in the text.

### Turn 7  (stop_reason=tool_use)
- submit_final_result({"final_result": "Short answer: Yes, Workday reports a gross revenue retention rate in its annual and quarterly filings. As of the latest filing I reviewed (FY2025 10-K, as of the April 7, 2025 as-of date), it does not report a net retention rate in those filings, although it told the SEC it would add net retention disclosure starting with the Oct 31, 2024 10-Q. It did not do so in that 10-Q.\n\n1. Gross revenue retention rate (reported)\n- FY2025 10-K (fiscal year ended January 31, 2025), MD&A, \"Gross Revenue Retention Rate\" subsection under Results of Operations > Revenues: the company reports a gross revenue retention rate of approximately 98% as of January 31, 2025. The filing says the
…[truncated 3,431 chars])

### Final answer
Short answer: Yes, Workday reports a gross revenue retention rate in its annual and quarterly filings. As of the latest filing I reviewed (FY2025 10-K, as of the April 7, 2025 as-of date), it does not report a net retention rate in those filings, although it told the SEC it would add net retention disclosure starting with the Oct 31, 2024 10-Q. It did not do so in that 10-Q.

1. Gross revenue retention rate (reported)
- FY2025 10-K (fiscal year ended January 31, 2025), MD&A, "Gross Revenue Retention Rate" subsection under Results of Operations > Revenues: the company reports a gross revenue retention rate of approximately 98% as of January 31, 2025. The filing says the metric "measures the percentage of recurring revenue retained from existing customers" and is calculated by taking total ARR of customers as of the corresponding prior period-end and comparing that to ARR from that same set of customers as of the current period-end.
- Inclusions/exclusions: the metric "takes into account recurring revenues lost to product or customer churn but does not account for additional revenue earned from add-ons or net expansions, which include volume and price adjustments." No prior-year rate is given in the 10-K.
- ARR basis (per the 10-K): ARR "represents the annualized value of active subscription contracts as of the end of each period," annualized by dividing total contract value by contract-term days and multiplying by 365. Contracts under one year that are distinct from the core product (e.g., tenants used for implementation and testing) are excluded. ARR is calculated on a constant currency basis using exchange rates set at the beginning of each fiscal year. ARR is a non-GAAP measure.
- Renewals: ARR is adjusted for a customer in renewal negotiations only if the customer churns.
- 10-Q (quarter ended October 31, 2024): the same metric and definition were disclosed, with a gross revenue retention rate of 98% as of October 31, 2024.

2. Net retention rate
- Neither the FY2025 10-K nor the Q3 FY2025 10-Q (October 31, 2024) reports a net revenue retention rate. Searches of both filings found no "net revenue retention" or "net retention" wording; "net expansions" appears only in the gross-metric definition as an exclusion.
- SEC correspondence (CORRESP filed 2024-09-04, responding to staff comments): Workday said that "in future filings, beginning with our Quarterly Report on Form 10-Q for the quarter ended October 31, 2024, we will disclose information about gross and net revenue retention rates, including a description and definition of each and how they are calculated." The proposed net definition was: "Net revenue retention rates are calculated by taking the current period-end ARR of our customers that we retained year-over-year, including add-ons and net expansion, divided by the total ARR at the end of the corresponding prior period." Workday also said it would show rates as thresholds (e.g., "exceeding XX%") rather than exact figures, because it does not consider these metrics to be key performance indicators.
- Discrepancy: the letter's commitment to disclose net retention from the October 2024 10-Q does not appear in the 10-Q text I opened, and the 10-K also omits it. I did not find a later filing or letter explaining this. I did not verify whether an amendment or other filing added net retention disclosure.

Not verified: I did not check the earnings releases, and I did not review the UPLOAD staff letter dated 2024-08-20. The FY2026 10-K postdates the as-of date and was not used.

{"sources": [{"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm", "name": "Workday FY2025 Form 10-K (fiscal year ended January 31, 2025)"}, {"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000242/wday-20241031.htm", "name": "Workday Form 10-Q for quarter ended October 31, 2024"}, {"url": "https://www.sec.gov/Archives/edgar/data/1327811/000132781124000174/filename1.htm", "name": "Workday SEC correspondence (CORRESP) filed 2024-09-04"}]}