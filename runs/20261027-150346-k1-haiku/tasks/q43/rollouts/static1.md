## Rollout `static1`
- outcome: submitted
- turns: 4; cost: $0.143; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Uber 2024 annual report gross bookings revenue take rate", "ciks": ["0001543151"], "form_types": ["10-K"], "start_date": "2025-01-01"})
  result: {"total_matching_documents": 1, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-14", "period_ending": "2024-12-31", "company": "Uber Technologies, Inc  (UBER)  (CIK 0001543151)", "ciks": ["0001543151"], "accession": "0001543151-25-000008", "document": "uber-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315125000008/uber-20241231.htm"}]}

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315125000008/uber-20241231.htm", "key": "uber10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: uber10k. (649,943 characters)
  The data_storage currently contains the following keys:
  uber10k
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Uber 10-K, extract: total revenue for 2024, 2023, 2022 (in millions); Gross Bookings for 2024, 2023 (total and by Mobility, Delivery, Freight); and the take rate figures reported (Revenue as % of Gross Bookings) for 2024 and 2023. Also any MD&A text explaining revenue growth drivers (volume vs. pricing/take rate, FX impact). Quote the exact table values. {{uber10k}}"})
  result: # Uber Technologies FY2024 10-K: Revenue, Gross Bookings, Take Rate, and MD&A Drivers
  
  ## 1. Total Revenue (in millions)
  
  From the Consolidated Statements of Operations:
  
  | | 2022 | 2023 | 2024 |
  |---|---|---|---|
  | **Revenue** | $31,877 | $37,281 | $43,978 |
  
  Segment revenue (Note 2 and MD&A Segment Results):
  
  | Segment | 2022 | 2023 | 2024 | 2023→2024 % Change |
  |---|---|---|---|---|
  | Mobility | $14,029 | $19,832 | $25,087 | 26% |
  | Delivery | $10,901 | $12,204 | $13,750 | 13% |
  | Freight | $6,947 | $5,245 | $5,141 | (2)% |
  | **Total** | **$31,877** | **$37,281** | **$43,978** | **18%** |
  
  ## 2. Gross Bookings (in millions)
  
  **Total Gross Bookings** (Financial and Operational Highlights table):
  
  | | 2023 | 2024 | % Change | % Change (Constant Currency) |
  |---|---|---|---|---|
  | **Gross Bookings** | $137,865 | $162,773 | 18% | 21% |
  
  **The 10-K does not report annual Gross Bookings by segment in a table.** It appears only as quarterly data in the "Certain Key Metrics" section. The annual segment figures below are my sums of those quarterly values. They reconcile exactly to the reported totals.
  
  Quarterly values as reported:
  
  | (In millions) | Q1 2023 | Q2 2023 | Q3 2023 | Q4 2023 | Q1 2024 | Q2 2024 | Q3 2024 | Q4 2024 |
  |---|---|---|---|---|---|---|---|---|
  | Mobility | $14,981 | $16,728 | $17,903 | $19,285 | $18,670 | $20,554 | $21,002 | $22,798 |
  | Delivery | 15,026 | 15,595 | 16,094 | 17,011 | 17,699 | 18,126 | 18,663 | 20,126 |
  | Freight | 1,401 | 1,278 | 1,284 | 1,279 | 1,282 | 1,272 | 1,308 | 1,273 |
  
  Derived annual totals:
  
  | Segment | 2023 (derived) | 2024 (derived) | Implied % Change |
  |---|---|---|---|
  | Mobility | $68,897 | $83,024 | ~20.5% |
  | Delivery | $63,726 | $74,614 | ~17.1% |
  | Freight | $5,242 | $5,135 | ~(2.0)% |
  | **Total** | **$137,865** | **$1
  …[truncated 1,978 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: Essentially all of Uber's 2024 revenue growth came from volume (Gross Bookings growth). Take rate was flat to slightly negative, so its contribution was roughly -0.6% of the growth, not a positive share.**\n\n**Inputs (Uber FY2024 10-K, filed 2025-02-14; $ millions)**\n- Revenue: 2023 = 37,281; 2024 = 43,978. Change = 6,697 (+17.96%).\n- Gross Bookings (GB): 2023 = 137,865; 2024 = 162,773. Change = 24,908 (+18.07%).\n- Take rate (Revenue ÷ GB), not reported as a figure in the 10-K, so calculated:\n  - 2023: 37,281 ÷ 137,865 = 27.0417%\n  - 2024: 43,978 ÷ 162,773 = 27.0180%\n  - Change = -0.0237 percentage points\n\n**Decomposition (volume at prior-year take rate; 
…[truncated 1,869 chars])

### Final answer
**Answer: Essentially all of Uber's 2024 revenue growth came from volume (Gross Bookings growth). Take rate was flat to slightly negative, so its contribution was roughly -0.6% of the growth, not a positive share.**

**Inputs (Uber FY2024 10-K, filed 2025-02-14; $ millions)**
- Revenue: 2023 = 37,281; 2024 = 43,978. Change = 6,697 (+17.96%).
- Gross Bookings (GB): 2023 = 137,865; 2024 = 162,773. Change = 24,908 (+18.07%).
- Take rate (Revenue ÷ GB), not reported as a figure in the 10-K, so calculated:
  - 2023: 37,281 ÷ 137,865 = 27.0417%
  - 2024: 43,978 ÷ 162,773 = 27.0180%
  - Change = -0.0237 percentage points

**Decomposition (volume at prior-year take rate; rate change at current-year GB)**
- Volume effect = ΔGB × TR2023 = 24,908 × 0.270417 ≈ +6,736.0
- Take-rate effect = ΔTR × GB2024 = (-0.000237) × 162,773 ≈ -38.6
- Total = 6,736.0 - 38.6 ≈ 6,697.4, which reconciles to the reported 6,697 change.

**Shares of 2024 revenue growth**
- Volume: 6,736.0 ÷ 6,697 ≈ 100.6%
- Take rate: -38.6 ÷ 6,697 ≈ -0.58%

**Context and caveats**
- The 10-K attributes revenue growth primarily to the 18% increase in Gross Bookings, which was driven by Mobility and Delivery trip volume growth. It also says business-model changes that classified certain sales and marketing costs as contra-revenue reduced revenue by $863 million (Mobility) and $713 million (Delivery), or $1,576 million in total. That drag is the main reason the consolidated take rate did not rise.
- Segment take rates moved in opposite directions. Mobility rose from about 28.8% to 30.2%, while Delivery fell from about 19.2% to 18.4%. Segment GB figures were derived by summing the quarterly values in the 10-K's key metrics section, so they are approximations.
- Using constant-currency GB growth (21%) instead of reported growth (18%) would not change the conclusion that volume drove the growth.
- If the $1,576 million contra-revenue reclassification is excluded, underlying take rate would be about 27.99% in 2024 (45,554 ÷ 162,773). That would make take-rate expansion a meaningful contributor (roughly 1,576 of the growth, or about 24%). This is an analytical adjustment, not a reported figure. It assumes the 2023 base is comparable, which the filing does not confirm.

**Sources**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1543151/000154315125000008/uber-20241231.htm",
            "name": "Uber Technologies, Inc. Form 10-K for fiscal year 2024 (SEC EDGAR)"
        }
    ]
}