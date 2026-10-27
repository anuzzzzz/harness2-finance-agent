## Rollout `dom1`
- outcome: submitted
- turns: 5; cost: $0.011; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "guidance_metrics_inventory"})
  result: ---
  name: guidance_metrics_inventory
  description: Answer "what metrics does company X guide on in its earnings reports" by reading the outlook section of the latest earnings release and supplemental deck, then listing each guided metric with its period, basis and latest range.
  ---
  ANALYTIC MOVE: classify and list. Input: the company's most recent earnings release and any supplemental or investor deck filed as of the question's date. Result: the complete list of metrics the company gives forward ranges or targets for, each with its period, basis and unit.
  
  1. Find the controlling documents.
     - Open the latest earnings release (8-K EX-99.1) for the most recent completed quarter before the as-of date. Open the supplemental or investor-update exhibit (often EX-99.2) if the filing has one.
     - Ignore filings dated after the as-of date. Search results often surface later quarters.
     - Guidance is usually in an "Outlook" or "Guidance" section, a table at the end of the release or deck, or the CFO prepared remarks. Do not infer the list from news snippets or the earnings-call Q&A, since journalists report only the headline items (usually EPS).
  2. Build the list by asking retrieve_information for every guided line: "list every forward-looking metric in the outlook or guidance section, with its period (next quarter or full year), range, and whether it is GAAP or adjusted". Ask a second time for items the first answer may have missed. Common categories are revenue or revenue growth, capacity or volume, unit costs, margin, fuel or other key input prices, EPS, non-operating items, tax rate, capital expenditure, free cash flow, and leverage or debt targets.
  3. Separate the metrics into three groups.
     - Next-quarter guidance (the quarterly outlook table).
     - Full-year guidance
  …[truncated 2,586 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/27904/000168316825000182/delta_ex9901.htm", "key": "dal_q4_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: dal_q4_2024. (52,998 characters)
  The data_storage currently contains the following keys:
  dal_q4_2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "List every forward-looking metric in the outlook or guidance section of this earnings release, with its period (first quarter 2025 or full year 2025), range, unit, and whether it is GAAP or adjusted. Also list any other guidance items (e.g., capex, free cash flow, leverage, tax rate, non-operating expense, capacity, fuel price, non-fuel unit cost). Quote the section headings used. {{dal_q4_2024}}"})
  result: ## Forward-looking metrics in the outlook/guidance section
  
  The release does not label each guidance line as GAAP or adjusted. Footnote 1 on the "Financial Guidance" heading says the guidance uses "Non-GAAP measures," and the text confirms that for EPS and revenue. The "Basis" column below reflects that footnote and the text, so the adjusted classifications for operating margin and EPS are inferred from the footnote rather than stated line by line.
  
  | Metric | Period | Range / Value | Unit | GAAP or Adjusted | Source heading |
  |---|---|---|---|---|---|
  | Earnings per share | FY 2025 | Greater than $7.35 | $ per diluted share | Adjusted (non-GAAP per footnote 1; text says "On a non-GAAP basis" growth is >19%) | "FY 2025 Forecast"; "Financial Guidance" |
  | Earnings per share growth YoY | FY 2025 | Greater than 10% (vs. normalized 2024 baseline excluding the 45¢ CrowdStrike impact) | % YoY | Adjusted (non-GAAP per footnote 1) | "FY 2025 Forecast"; "Financial Guidance" |
  | Free cash flow | FY 2025 | Greater than $4 billion | $ billions | Adjusted/non-GAAP (FCF is defined only in Note A) | "FY 2025 Forecast" |
  | Gross leverage (adjusted debt to EBITDAR) | FY 2025 | 2x or less | multiple (x) | Adjusted/non-GAAP (footnote 3; defined in Note A) | "FY 2025 Forecast" |
  | Total revenue growth YoY | 1Q 2025 | Up 7% to 9% | % YoY | Adjusted (text: "March quarter adjusted revenue to be 7 to 9 percent higher") | "1Q25 Forecast"; "Revenue Environment and Outlook" |
  | Operating margin | 1Q 2025 | 6% to 8% | % | Adjusted (non-GAAP per footnote 1; not labeled line by line) | "1Q25 Forecast" |
  | Earnings per share | 1Q 2025 | $0.70 to $1.00 | $ per diluted share | Adjusted (non-GAAP per footnote 1) | "1Q25 Forecast" |
  
  **Other forward-looking items in the release:**
  
  - **Pre-tax income, FY
  …[truncated 928 chars]

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this release: (1) Which guidance items are NOT provided (e.g., full-year capacity, full-year revenue growth, fuel price per gallon, non-operating expense, tax rate, capex)? (2) Quote the exact outlook table rows for 1Q25 and FY 2025, including any capacity (ASM) or fuel rows, and any footnote 1 text on non-GAAP. {{dal_q4_2024}}"})
  result: **(1) Guidance not provided in this release**
  
  The release gives no numeric guidance for any of these:
  
  - **Full-year 2025 capacity (ASM) growth:** Not given. Management only says 2025 will see "slower capacity growth," with no figure.
  - **Full-year 2025 revenue growth:** Not given. Only the 1Q25 total revenue growth range is provided.
  - **Fuel price per gallon:** Not given for 1Q25 or FY 2025.
  - **Non-operating expense:** Not given.
  - **Tax rate:** Not given.
  - **Capital expenditures:** Not given. Only free cash flow is guided.
  
  The release also omits 1Q25 capacity and fuel guidance. Some items are only qualitative: non-fuel unit cost growth is expected to be "in the low-single digits" for FY 2025, and the CEO cites pre-tax income "greater than $6 billion" in a quote rather than in the outlook table.
  
  **(2) Outlook table rows and footnote 1**
  
  The outlook section is titled "Financial Guidance1" and the table reads:
  
  *FY 2025 Forecast2 / 3-5 Year Targets4*
  - Earnings Per Share YoY: Greater than 10% / 10% average
  - Free Cash Flow ($B): Greater than $4 / $3 - $5
  - Gross Leverage3: 2x or less / 1x
  
  *1Q25 Forecast*
  - Total Revenue YoY: Up 7% - 9%
  - Operating Margin: 6% - 8%
  - Earnings Per Share: $0.70 - $1.00
  
  No ASM or fuel rows appear in the table.
  
  Footnote 1 text: "Non-GAAP measures; Refer to Non-GAAP reconciliations for historical comparison figures"
  
  The release also has footnotes 2–4: (2) "Year-over-year EPS growth excludes the 45-cent impact of the CrowdStrike-caused outage in 2024"; (3) "Adjusted debt to EBITDAR"; (4) "Introduced at November 2024 Investor Day."

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "Headline: In its most recent earnings release before April 7, 2025 (the December-quarter 2024 results, released January 2025), Delta Air Lines guides on a short list of non-GAAP metrics: EPS, total revenue growth, operating margin, free cash flow and gross leverage, with qualitative comments on non-fuel unit cost. It gives no numeric guidance on capacity, fuel price, non-operating expense, tax rate or capex in that release.\n\nSource document: Delta's Q4 2024 earnings release (Form 8-K, Exhibit 99.1), dated January 2025. I did not find a separate EX-99.2 investor deck in the materials I opened, so this list is based on the release only.\n\nGuidance table, grouped by period 
…[truncated 1,838 chars])

### Final answer
Headline: In its most recent earnings release before April 7, 2025 (the December-quarter 2024 results, released January 2025), Delta Air Lines guides on a short list of non-GAAP metrics: EPS, total revenue growth, operating margin, free cash flow and gross leverage, with qualitative comments on non-fuel unit cost. It gives no numeric guidance on capacity, fuel price, non-operating expense, tax rate or capex in that release.

Source document: Delta's Q4 2024 earnings release (Form 8-K, Exhibit 99.1), dated January 2025. I did not find a separate EX-99.2 investor deck in the materials I opened, so this list is based on the release only.

Guidance table, grouped by period (all items footnoted as non-GAAP):

Next quarter (1Q 2025 forecast):
- Total revenue growth, year over year: up 7% to 9% (the release text describes this as adjusted revenue growth)
- Operating margin: 6% to 8% (non-GAAP per footnote 1; not labeled line by line)
- Earnings per share: $0.70 to $1.00 per diluted share

Full year (FY 2025 forecast):
- Earnings per share growth, year over year: greater than 10%, measured against a 2024 baseline that excludes the 45-cent CrowdStrike-related impact (footnote 2)
- Earnings per share level: one extraction reported "greater than $7.35" under the FY 2025 forecast heading, but the table extraction did not show that figure, so I treat it as unconfirmed
- Free cash flow: greater than $4 billion
- Gross leverage (adjusted debt to EBITDAR): 2x or less (footnote 3)
- Non-fuel unit cost (CASM-Ex): qualitative, expected to rise in the low-single digits year over year
- Pre-tax income: the CEO's quote says "greater than $6 billion." This is outside the guidance table and its GAAP or non-GAAP basis is not stated.

Longer-term targets (3 to 5 year, introduced at the November 2024 Investor Day, footnote 4):
- Earnings per share: 10% average annual growth
- Free cash flow: $3 billion to $5 billion
- Gross leverage: 1x

Not provided in this release: full-year 2025 capacity (ASM) growth (only described as "slower capacity growth"), full-year 2025 revenue growth, first-quarter capacity and fuel guidance, fuel price per gallon, non-operating expense, tax rate and capital expenditures.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/27904/000168316825000182/delta_ex9901.htm",
            "name": "Delta Air Lines Q4 2024 earnings release (8-K Exhibit 99.1), January 2025"
        }
    ]
}