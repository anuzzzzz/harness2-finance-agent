## Rollout `inv1`
- outcome: submitted
- turns: 3; cost: $0.006; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/27904/000168316825000182/delta_ex9901.htm", "key": "dal_q4_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: dal_q4_2024. (52,998 characters)
  The data_storage currently contains the following keys:
  dal_q4_2024
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Delta earnings release, find the outlook / guidance section. List every guided line item exactly as labelled in the outlook table (e.g., first quarter 2025 and full year 2025 items), with its period, unit and range. Also note any items labelled as non-GAAP or with footnotes. Quote labels exactly. Document: {{dal_q4_2024}}"})
  result: ## Outlook / Guidance Table
  
  The release has two guidance tables, both under the "Financial Guidance" heading. The "Financial Guidance" heading carries footnote marker 1.
  
  **FY 2025 Forecast** (footnote 2 is attached to this heading)
  
  | Label (exact) | Period | Unit | Range / Value |
  |---|---|---|---|
  | Earnings Per Share YoY | FY 2025 | Year-over-year % growth | Greater than 10% |
  | Free Cash Flow ($B) | FY 2025 | US$ billions | Greater than $4 |
  | Gross Leverage3 | FY 2025 | Multiple (x), per footnote 3 | 2x or less |
  
  **1Q25 Forecast** (no footnote marker on this heading)
  
  | Label (exact) | Period | Unit | Range / Value |
  |---|---|---|---|
  | Total Revenue YoY | 1Q25 (March 2025 quarter) | Year-over-year % growth | Up 7% - 9% |
  | Operating Margin | 1Q25 | % of revenue | 6% - 8% |
  | Earnings Per Share | 1Q25 | US$ per diluted share | $0.70 - $1.00 |
  
  **3-5 Year Targets** (a separate column, not 2025 guidance; footnote 4 is attached)
  
  | Label (exact) | Period | Unit | Range / Value |
  |---|---|---|---|
  | Earnings Per Share YoY | 3-5 years | Average YoY % growth | 10% average |
  | Free Cash Flow ($B) | 3-5 years | US$ billions | $3 - $5 |
  | Gross Leverage3 | Long-term | Multiple (x) | 1x |
  
  ## Non-GAAP Labelling and Footnotes
  
  - **Footnote 1** (attached to the "Financial Guidance" heading): "Non-GAAP measures; Refer to Non-GAAP reconciliations for historical comparison figures." The table labels themselves do not say "non-GAAP" or "adjusted." The footnote is the only indication that the guidance is on a non-GAAP basis.
  - **Footnote 2** (attached to "FY 2025 Forecast"): "Year-over-year EPS growth excludes the 45-cent impact of the CrowdStrike-caused outage in 2024."
  - **Footnote 3** (attached to "Gross Leverage"): "Adjusted debt to EBITDAR."
  - **Footnote 4** (attached to "3
  …[truncated 1,048 chars]

### Turn 3  (stop_reason=tool_use)
- submit_final_result({"final_result": "Delta Air Lines (NYSE: DAL) guides on a small set of metrics in its earnings release outlook. The most recent release I could open and verify is the December-quarter 2024 earnings release (8-K, January 2025). The March-quarter 2025 results come after the April 7, 2025 as-of date, so they are not used.\n\nQuarterly guidance (1Q25 Forecast table, March 2025 quarter):\n- Total Revenue YoY (year-over-year % growth): up 7% to 9%\n- Operating Margin (% of revenue): 6% to 8%\n- Earnings Per Share (US$ per diluted share): $0.70 to $1.00\n\nFull-year guidance (FY 2025 Forecast table):\n- Earnings Per Share YoY (year-over-year % growth): greater than 10%\n- Free Cash Flow ($B, US$ bi
…[truncated 1,631 chars])

### Final answer
Delta Air Lines (NYSE: DAL) guides on a small set of metrics in its earnings release outlook. The most recent release I could open and verify is the December-quarter 2024 earnings release (8-K, January 2025). The March-quarter 2025 results come after the April 7, 2025 as-of date, so they are not used.

Quarterly guidance (1Q25 Forecast table, March 2025 quarter):
- Total Revenue YoY (year-over-year % growth): up 7% to 9%
- Operating Margin (% of revenue): 6% to 8%
- Earnings Per Share (US$ per diluted share): $0.70 to $1.00

Full-year guidance (FY 2025 Forecast table):
- Earnings Per Share YoY (year-over-year % growth): greater than 10%
- Free Cash Flow ($B, US$ billions): greater than $4
- Gross Leverage (multiple, x): 2x or less

Narrative-only full-year figures, outside the table: FY 2025 EPS greater than $7.35 per share (more than 10% growth versus a normalized 2024 baseline, and greater than 19% on a non-GAAP basis); FY 2025 pre-tax income greater than $6 billion (CEO quote); and non-fuel unit cost (CASM-Ex) growth in the low-single digits (CFO quote).

Basis and caveats:
- The guidance is non-GAAP. The table labels do not say "non-GAAP" or "adjusted"; a footnote on the "Financial Guidance" heading says the measures are non-GAAP and refers to reconciliations for historical figures. The release also says forward-looking non-GAAP measures cannot be reconciled to GAAP without unreasonable effort.
- FY 2025 EPS growth excludes the 45-cent impact of the 2024 CrowdStrike-caused outage.
- Gross Leverage is adjusted debt to EBITDAR.
- The 3-5 year targets (EPS YoY 10% average, free cash flow $3 to $5 billion, long-term gross leverage 1x) were introduced at the November 2024 Investor Day. They are not 2025 guidance.
- The March-quarter revenue guidance is described as "adjusted revenue" in the narrative, but the table label is only "Total Revenue YoY."
- An earlier January 2024 supplemental deck exists, but I did not open it, so I have not relied on it for current guidance.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/27904/000168316825000182/delta_ex9901.htm",
            "name": "Delta Air Lines Q4 2024 earnings release (8-K Exhibit 99.1, January 2025)"
        }
    ]
}