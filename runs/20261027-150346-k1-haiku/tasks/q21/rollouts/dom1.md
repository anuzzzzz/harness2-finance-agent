## Rollout `dom1`
- outcome: submitted
- turns: 5; cost: $0.121; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "concentration_risk_disclosure"})
  result: ---
  name: concentration_risk_disclosure
  description: Answer "what is company X's vendor / supplier / customer / bank concentration risk as of FY Y" from a 10-K, with quotes, the scope of each dependency, and no imported or inferred names.
  ---
  
  # Concentration-risk questions (vendor, supplier, customer, sponsor bank, geography)
  
  ANALYTIC MOVE: classify and trace. Find every place the filing discloses a dependency, then say what is concentrated, on how many counterparties, and with what quantification.
  
  Where it lives in a 10-K (check each one, in this order):
  1. Financial-statement notes. Note 1 "Summary of Significant Accounting Policies" often has a "Concentration Risk" or "Concentration of Credit Risk" paragraph. A separate "Significant customers" or "Major suppliers" note may also exist. The note is the controlling source for the as-of year.
  2. Item 1A Risk Factors. Search for "single third-party", "sole source", "depend on", "sponsor bank", "limited number of vendors". These state the scope of the dependency, such as which services and which regions, and often go beyond the note.
  3. Item 1 Business (sponsorship, processing, supply relationships) and MD&A (percentage-of-revenue or volume statements, such as "no single customer exceeded X%").
  
  Answer contract, with each part labelled:
  - The dependency, quoted verbatim from the filing and tied to a section and page: who or what is concentrated, how many counterparties ("one vendor"), which regions and services.
  - Whether the counterparty is named. If the filing does not name it, say "not named in the filing". Never supply a name from memory, from inference, or from a different filing or year. If a name is unconfirmed, leave it out.
  - Quantification as of the as-of date, with units and period: % of revenue or volume, or
  …[truncated 2,206 chars]

### Turn 2  (stop_reason=tool_use)
- edgar_search({"search_query": "Shift4 single third-party processor merchant authorization settlement", "ciks": ["0001794669"], "start_date": "2025-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 2, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-19", "period_ending": "2024-12-31", "company": "Shift4 Payments, Inc.  (FOUR)  (CIK 0001794669)", "ciks": ["0001794669"], "accession": "0001794669-25-000011", "document": "four-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1794669/000179466925000011/four-20241231.htm"}, {"form": "SC TO-T", "file_date": "2025-03-21", "period_ending": null, "company": "Global Blue Group Holding AG  (GB, GBGWF)  (CIK 0001799983)", "ciks": ["0001799983", "0001794669"], "accession": "0001193125-25-059711", "document": "d916665dex99b2.htm", "description": "EX-99.(B)(2)", "url": "https://www.sec.gov/Archives/edgar/data/1799983/000119312525059711/d916665dex99b2.htm"}]}

### Turn 3  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1794669/000179466925000011/four-20241231.htm", "key": "shift4_10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: shift4_10k. (534,672 characters)
  The data_storage currently contains the following keys:
  shift4_10k
  

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this 10-K text, quote verbatim (full sentences) every passage about concentration risk, including: (1) the Note 1 \"Concentration Risk\" paragraph about the vendor handling merchant processing in North America, backup systems, and the sponsor bank/member bank agreement and 180-day terms; (2) the Item 1A risk factor sentence about depending on a single third-party processor in the U.S., EU and Canada for merchant authorization and settlement, including any termination notice period and backup language. Include the section heading and page number where visible. Do not paraphrase. State if not found. Text: {{shift4_10k}}"})
  result: ## (1) Note 1, "Concentration Risk" (Notes to Consolidated Financial Statements, Note 1, p. 85)
  
  > Concentration Risk
  >
  > The Company's merchant processing activity in North America is facilitated by one vendor. The Company believes that this vendor maintains appropriate backup systems and alternative arrangements to avoid a significant disruption of the processing in the event of an unforeseen event.
  >
  > A majority of the Company's revenue is derived from the processing of card transactions. Because the Company is not a "member bank" in North America, in order to process these bank card transactions, the Company has entered into a sponsorship agreement with a member bank. The agreement with the bank sponsor requires, among other things, that the Company abide by the by-laws and regulations of the credit card companies. If the Company breaches the sponsorship agreement, the bank sponsor may terminate the agreement and, under the terms of the agreement, the Company would have 180 days to identify an alternative bank sponsor.
  
  ## (2) Item 1A Risk Factor on the single third-party processor (Item 1A, "Business risks," p. 22)
  
  Heading: "Because we rely on third-party vendors to provide products and services, we could be adversely impacted if they fail to fulfill their obligations."
  
  > For example, in the U.S., EU, and Canada we are dependent on our relationship with a single third-party processor for services such as merchant authorization, processing, risk and chargeback monitoring accounting and clearing and settlement for the transactions we service. There can be no assurance that our backup systems and alternative arrangements would successfully avoid a significant disruption of processing in the event of an unforeseen event with this third-party. In the event our agreem
  …[truncated 1,951 chars]

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Shift4 Payments, Inc. – vendor concentration risk as of December 31, 2024 (FY2024 Form 10-K, filed 2025-02-19, accession 0001794669-25-000011)**\n\n**1. The dependency (Note 1, \"Concentration Risk,\" p. 85)**\n- The note states that the company's North American merchant processing is facilitated by one vendor, i.e., a single-counterparty dependency. Scope: North America merchant processing.\n- Item 1A (\"Business risks,\" p. 22, heading: \"Because we rely on third-party vendors to provide products and services, we could be adversely impacted if they fail to fulfill their obligations\") describes the dependency more broadly: in the U.S., EU and Canada the company depends 
…[truncated 2,915 chars])

### Final answer
**Shift4 Payments, Inc. – vendor concentration risk as of December 31, 2024 (FY2024 Form 10-K, filed 2025-02-19, accession 0001794669-25-000011)**

**1. The dependency (Note 1, "Concentration Risk," p. 85)**
- The note states that the company's North American merchant processing is facilitated by one vendor, i.e., a single-counterparty dependency. Scope: North America merchant processing.
- Item 1A ("Business risks," p. 22, heading: "Because we rely on third-party vendors to provide products and services, we could be adversely impacted if they fail to fulfill their obligations") describes the dependency more broadly: in the U.S., EU and Canada the company depends on a single third-party processor for merchant authorization, processing, risk and chargeback monitoring, accounting, and clearing and settlement. Note that the 10-K's Item 1A describes the EU as a region, which goes beyond the Note 1 North America wording.

**2. Counterparty name:** Not named in the filing. The vendor is referred to only as "one vendor" and "a single third-party processor."

**3. Quantification as of Dec 31, 2024:** None disclosed. The filing gives no percentage of revenue, volume, or balances for this vendor, and no 2023 comparison.

**4. Contractual exit terms and mitigants (quoted/cited as disclosed):**
- Note 1: the company "believes that this vendor maintains appropriate backup systems and alternative arrangements to avoid a significant disruption of the processing in the event of an unforeseen event."
- Item 1A: "There can be no assurance that our backup systems and alternative arrangements would successfully avoid a significant disruption of processing." It also says that if the agreement is terminated, or not renewed on favorable terms or at all, "it may be difficult for us to replace these services."
- Termination notice period: not stated in the risk factor or Note 1.

**5. Related sponsor-bank dependency (separate from the vendor):** Note 1 says the company is not a "member bank" in North America and relies on a sponsorship agreement with a member bank. If the company breaches it, the bank sponsor may terminate, and the company would have 180 days to identify an alternative bank sponsor. The bank is not named in the filing. Item 1A (p. 31) adds that the company relies on its sponsor bank for card-network sponsorship and treasury services in the U.S. and Canada.

**6. Offsetting concentrations (customer/reseller limits, reported separately):**
- No single merchant accounts for more than 3% of revenue in recent years (Item 1, p. 6).
- No single VAR accounts for more than 3% of volume for the year ended December 31, 2024 (Item 1, p. 8).
- No single customer accounted for more than 10% of revenue in 2024, 2023 or 2022 (Note 21, p. 110).

**Conclusion:** Shift4 has a single-point dependency for North American merchant processing, and its single third-party processor covers the U.S., EU and Canada. The filing gives no quantified share for this vendor and no notice period for termination. The company points to backup systems and alternative arrangements as mitigants, but the 10-K itself says those arrangements may not avoid disruption. The risk is therefore high in qualitative terms and unquantified in the filing.

**Sources:**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1794669/000179466925000011/four-20241231.htm",
            "name": "Shift4 Payments, Inc. Form 10-K for fiscal year ended December 31, 2024 (four-20241231.htm)"
        }
    ]
}