## Rollout `ctl3`
- outcome: submitted
- turns: 6; cost: $0.039; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Airbnb adjusted EBITDA definition net income adjustments depreciation stock-based compensation") → 0 results: 
- edgar_search({"search_query": "Airbnb reconciliation net income to adjusted EBITDA", "ciks": ["ABNB"], "start_date": "2024-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 10, "page": 1, "results": [{"form": "8-K", "file_date": "2024-08-06", "period_ending": "2024-08-06", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-194849", "document": "d831385dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm"}, {"form": "8-K", "file_date": "2025-02-13", "period_ending": "2025-02-13", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-25-026054", "document": "d915198dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm"}, {"form": "8-K", "file_date": "2024-11-07", "period_ending": "2024-11-07", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-253103", "document": "d886752dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm"}, {"form": "8-K", "file_date": "2024-05-08", "period_ending": "2024-05-08", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-134183", "document": "d813800dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524134183/d813800dex991.htm"}, {"form": "8-K", "file_date": "2024-02-13", "period_ending": "2024-02-13", "company": "Airbnb, Inc.  (ABNB)  (CIK 0001559720)", "ciks": ["0001559720"], "accession": "0001193125-24-033706", "document": "d646462dex991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm"}, {"form": "10-Q", "file_date":
  …[truncated 1,676 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 10 results: Airbnb, Inc. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000155972022000009/abnb-20220331.htm>; Airbnb, Inc. - Form 10-Q - FY2023 <https://www.sec.gov/Archives/edgar/data/1559720/000155972023000020/abnb-20230930.htm>; Airbnb, Inc. - Form S-1 - FY2020 <https://www.sec.gov/Archives/edgar/data/1559720/000119312520294801/d81668ds1.htm>; Airbnb, Inc. - Form 10-Q - FY2021 <https://www.sec.gov/Archives/edgar/data/1559720/000162828021016979/abnb-20210630.htm>; Airbnb, Inc. - Form 10-Q - FY2022 <https://www.sec.gov/Archives/edgar/data/1559720/000155972022000012/abnb-20220630.htm>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm", "key": "abnb_q4_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: abnb_q4_2024. (54,854 characters)
  The data_storage currently contains the following keys:
  abnb_q4_2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb earnings release, list the definition of Adjusted EBITDA and every line item in the reconciliation from Net Income (loss) to Adjusted EBITDA for the full year 2024 and 2023 (with amounts). Also note the definition text about what is adjusted. Document: {{abnb_q4_2024}}"})
  result: 

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Airbnb earnings release, list the definition of Adjusted EBITDA and every line item in the reconciliation from Net Income (loss) to Adjusted EBITDA for the full year 2024 and 2023 (with amounts). Document: {{abnb_q4_2024}}"})
  result: 

### Turn 5  (stop_reason=tool_use)
- retrieve_information({"prompt": "Find the text describing Adjusted EBITDA and the reconciliation table of net income to Adjusted EBITDA in this document and summarize the adjustment line items: {{abnb_q4_2024}}"})
  result: 

### Turn 6  (stop_reason=tool_use)
- web_search(query="Airbnb fourth quarter 2024 results Adjusted EBITDA reconciliation net income provision for income taxes restructuring") → 9 results: Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524194849/d831385dex991.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524033706/d646462dex991.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000032/abnb-20240930.htm>; Airbnb, Inc. - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000155972024000024/abnb-20240630.htm>; Airbnb, Inc. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/1559720/000119312524253103/d886752dex991.htm>
- submit_final_result({"final_result": "**Short answer:** Airbnb starts from GAAP net income and adds back or removes the items below. The most recent full reconciliation I could verify is in its Q3 2024 10-Q (nine months ended Sept. 30, 2024). Airbnb's 10-K definition text (2021–2023 filings) also lists restructuring charges, which do not appear as a line in the 2024 tables I reviewed.\n\n**Adjustments (from the Q3 2024 10-Q reconciliation, $ millions)**\n\n1. **Provision for income taxes**: the 9M 2024 figure is +522. Airbnb's definition covers the provision for (or benefit from) income taxes. <cite index=\"13-1\">Provision for (benefit from) income taxes | (2,695) | 367 | (2,656) | 522</cite>\n2. **Other (inco
…[truncated 3,640 chars])

### Final answer
**Short answer:** Airbnb starts from GAAP net income and adds back or removes the items below. The most recent full reconciliation I could verify is in its Q3 2024 10-Q (nine months ended Sept. 30, 2024). Airbnb's 10-K definition text (2021–2023 filings) also lists restructuring charges, which do not appear as a line in the 2024 tables I reviewed.

**Adjustments (from the Q3 2024 10-Q reconciliation, $ millions)**

1. **Provision for income taxes**: the 9M 2024 figure is +522. Airbnb's definition covers the provision for (or benefit from) income taxes. <cite index="13-1">Provision for (benefit from) income taxes | (2,695) | 367 | (2,656) | 522</cite>
2. **Other (income) expense, net**: 9M 2024 is +49. The definition covers <cite index="2-1">other income (expense), net, interest expense, and interest income</cite>.
3. **Interest income**: 9M 2024 is (635), which is deducted. <cite index="13-1">Interest income | (192) | (207) | (529) | (635)</cite>
4. **Depreciation and amortization**: 9M 2024 is +43. Airbnb excludes <cite index="3-1">depreciation of property and equipment and amortization of intangible assets</cite>, which it describes as non-cash charges.
5. **Stock-based compensation expense**: 9M 2024 is +1,039. Airbnb notes that <cite index="13-1">stock-based compensation expense, which has been, and will continue to be for the foreseeable future, a significant recurring expense in our business</cite>, yet still excludes it.
6. **Acquisition-related impacts**: 9M 2024 is +5. The definition covers <cite index="1-1">gains (losses) recognized on changes in the fair value of contingent consideration arrangements</cite>.
7. **Lodging taxes, host withholding taxes, and transactional taxes, net**: 9M 2024 is +66. The definition describes <cite index="1-1">net changes to the reserves for lodging taxes for which management believes it is probable that we may be held jointly liable with Hosts for collecting and remitting such taxes</cite>. The 2024 label is broader than the older "lodging tax reserves" wording.
8. **Restructuring charges**: the 2021–2023 definitions list <cite index="1-1">restructuring charges</cite> as an adjustment, but I did not see a restructuring line in the 2024 reconciliation tables.

**Check of the 9M 2024 figures:** Net income of 2,187 + taxes 522 + other expense 49 − interest income 635 + D&A 43 + SBC 1,039 + acquisition impacts 5 + lodging/withholding/transactional taxes 66 = 3,276. This matches the reported Adjusted EBITDA of $3,276 million. The Q3 2024 three-month figures also tie: 1,368 + 367 − 3 − 207 + 15 + 362 − 2 + 58 = 1,958.

**Caveats:** I could not open the FY2024 10-K (filed Feb. 13, 2025) or the Q4 2024 release to confirm the full-year 2024 line items, so the list reflects the Q3 2024 10-Q plus the definition text in earlier filings. Airbnb's stated rationale is that <cite index="1-2">the above items are excluded from our Adjusted EBITDA measure because these items are non-cash in nature, or because the amount and timing of these items is unpredictable</cite>.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000032/abnb-20240930.htm",
            "name": "Airbnb Form 10-Q for quarter ended September 30, 2024 (Adjusted EBITDA Reconciliation)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000017/abnb-20240331.htm",
            "name": "Airbnb Form 10-Q for quarter ended March 31, 2024 (Adjusted EBITDA Reconciliation)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972022000006/abnb-20211231.htm",
            "name": "Airbnb Form 10-K for FY2021 (Adjusted EBITDA definition)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000024/abnb-20240630.htm",
            "name": "Airbnb Form 10-Q for quarter ended June 30, 2024 (Adjusted EBITDA Reconciliation)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm",
            "name": "Airbnb Form 10-K for FY2024 (not successfully parsed; referenced for latest filing)"
        }
    ]
}