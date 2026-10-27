## Rollout `dom1`
- outcome: submitted
- turns: 4; cost: $0.009; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "guidance_vs_actual_range"})
  result: ---
  name: guidance_vs_actual_range
  description: Compare a company's reported period results (quarter or full year) with the guidance range it issued in an earlier release, metric by metric, against both the range and the midpoint.
  ---
  ANALYTIC MOVE: compare. Inputs: (a) the guidance table for the target period from the release that issued it (for "prior quarter's full-year guidance", the quarterly release immediately before the period-end release; for guidance given in a named period, that period's release); (b) the actuals from the release or filing reporting the target period. Result: per metric, BEAT / IN RANGE / MISS, with the variance.
  
  1. Guidance source. Open the prior release (8-K EX-99.1 or shareholder letter, HTML) and retrieve the outlook table with every metric, low and high, for the right column (full-year vs next-quarter columns sit side by side in the same table; pick the one for the period asked). Note whether the release says guidance was raised, lowered or reaffirmed versus earlier. Releases often revise guidance each quarter, so the "prior quarter" guidance is not the initial guidance. Mention the initial guidance only as context.
  2. Actual source. Open the period-end release (the Q4 / full-year letter or release) and retrieve the full-year actuals. Prefer a stated full-year figure over summing quarters. Match each metric's definition exactly (e.g. in-force premium is an end-of-period figure, gross earned premium and revenue are period sums, Adjusted EBITDA is non-GAAP and a loss is negative). Check units ($M vs $K) and the sign convention for losses.
  3. Calculation, unrounded until the end, for each metric: midpoint = (low + high)/2; variance $ = actual - midpoint; variance % = variance / |midpoint| x 100. Position: above the high end, within the ran
  …[truncated 1,833 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm", "key": "q3letter"})
  result: SUCCESS: The result has been saved to the data storage under the key: q3letter. (45,843 characters)
  The data_storage currently contains the following keys:
  q3letter
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142125000021/lmndshareholderletterq42.htm", "key": "q4letter"})
  result: SUCCESS: The result has been saved to the data storage under the key: q4letter. (53,419 characters)
  The data_storage currently contains the following keys:
  q3letter
  q4letter
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Q3 2024 letter, find the outlook/guidance table. List every metric with Q4 2024 and FY2024 guidance low and high values, and state whether each was raised, lowered or reaffirmed. Also list the exact wording on which metrics were raised. Document: {{q3letter}}"})
  result: ## FY2024 and Q4 2024 Guidance (Q3 2024 Shareholder Letter)
  
  | Metric | Q4 2024 Low | Q4 2024 High | FY2024 Low | FY2024 High | Status (FY2024) |
  |---|---|---|---|---|---|
  | In Force Premium (IFP) | $940M | $944M | $940M | $944M | Reaffirmed |
  | Gross Earned Premium (GEP) | $222M | $225M | $823M | $826M | **Raised** |
  | Revenue | $144M | $146M | $522M | $524M | **Raised** |
  | Adjusted EBITDA Loss | ($29M) | ($25M) | ($155M) | ($151M) | Reaffirmed |
  | Stock-based compensation expense | $16M | n/a (single value) | $64M | n/a (single value) | Reaffirmed |
  | Capital expenditures | $3M | n/a (single value) | $10M | n/a (single value) | Reaffirmed |
  | Weighted common shares | 72M | n/a (single value) | 71M | n/a (single value) | Reaffirmed |
  
  The table in the document is garbled, so the stock-based compensation, capex, and weighted share figures appear as single values. I've read them as point estimates.
  
  **Exact wording on the raised metrics:**
  
  > "We are increasing full year guidance for gross earned premium and revenue, and reaffirming guidance for FY 2024 for all other metrics."
  
  So the raises are gross earned premium (FY2024 $823M–$826M) and revenue (FY2024 $522M–$524M). The letter does not give the prior ranges, so the size of each increase cannot be determined from this document. The letter also does not explicitly label the Q4 2024 ranges as raised or reaffirmed. The raise language refers to full-year guidance.
- retrieve_information({"prompt": "From this Q4 2024 shareholder letter, find full-year 2024 actuals for: in-force premium (end of period), gross earned premium (full year), revenue (full year), Adjusted EBITDA (full year), gross profit, net loss, free cash flow. Give exact figures, units and periods, and any full-year outlook for 2025 is not needed. Document: {{q4letter}}"})
  result: Figures are for fiscal year 2024 (year ended December 31, 2024) unless noted. All dollar amounts are in US$ millions, except per-share data.
  
  | Metric | FY 2024 Actual | Period / Basis | Source in letter |
  |---|---|---|---|
  | In-force premium (IFP), end of period | **$943.7 million** | As of Dec 31, 2024 (point in time) | Key Operating and Financial Metrics table |
  | Gross earned premium (GEP) | **$827.3 million** | Year ended Dec 31, 2024 | Key Operating and Financial Metrics table |
  | Total revenue | **$526.5 million** | Year ended Dec 31, 2024 | Condensed Consolidated Statements of Operations |
  | Adjusted EBITDA | **($149.7) million** (loss) | Year ended Dec 31, 2024 | Adjusted EBITDA reconciliation (non-GAAP) |
  | Gross profit | **$166.9 million** | Year ended Dec 31, 2024 (GAAP; 32% margin on total revenue) | Key Operating and Financial Metrics table |
  | Net loss | **($202.2) million** | Year ended Dec 31, 2024 (($2.85) per share, basic and diluted) | Statements of Operations |
  | Free cash flow (FCF) | **($20.8) million** | Year ended Dec 31, 2024 (operating cash flow of ($11.4)M less capex of $9.4M) | Adjusted Free Cash Flow reconciliation (non-GAAP) |
  
  Notes:
  - The letter rounds several of these figures in its narrative: Adjusted EBITDA to "($150) million", gross profit to "$167 million", and IFP to "$944 million".
  - The letter's headline "Adjusted Free Cash Flow" is a different non-GAAP measure. For FY 2024 it was **$47.6 million** (adds $68.4M of net borrowings under the financing agreement to FCF). The letter's "$48 million" headline uses this figure.

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "\nOverall verdict: Lemonade beat its prior full-year 2024 guidance on every metric with a range. Gross earned premium, revenue and Adjusted EBITDA finished above the top of their ranges, and in-force premium landed inside its range, in the upper half.\n\nGuidance source: the Q3 2024 shareholder letter (8-K dated 2024-10-30). Its FY2024 outlook raised gross earned premium and revenue, and reaffirmed in-force premium (IFP), Adjusted EBITDA and the other metrics. The letter does not give the prior ranges, so the size of the raises cannot be measured from it. The Q3 letter's outlook table was garbled in parsing; the FY2024 ranges used below were read from it and match the range
…[truncated 2,000 chars])

### Final answer

Overall verdict: Lemonade beat its prior full-year 2024 guidance on every metric with a range. Gross earned premium, revenue and Adjusted EBITDA finished above the top of their ranges, and in-force premium landed inside its range, in the upper half.

Guidance source: the Q3 2024 shareholder letter (8-K dated 2024-10-30). Its FY2024 outlook raised gross earned premium and revenue, and reaffirmed in-force premium (IFP), Adjusted EBITDA and the other metrics. The letter does not give the prior ranges, so the size of the raises cannot be measured from it. The Q3 letter's outlook table was garbled in parsing; the FY2024 ranges used below were read from it and match the ranges supplied in the task brief.

Actuals source: the Q4 2024 shareholder letter (8-K filed February 2025). Figures are for the year ended December 31, 2024, except IFP, which is an end-of-period figure.

Results table (midpoint = (low + high) / 2; variance = actual - midpoint; variance % = variance / |midpoint|):

1. In-force premium (end of period): guidance $940M–$944M (midpoint $942M). Actual $943.7M. Variance +$1.70M (+0.18%). Position: within the range, in the upper part.

2. Gross earned premium: guidance $823M–$826M (midpoint $824.5M), raised in Q3. Actual $827.3M. Variance +$2.80M (+0.34%). Position: above the high end.

3. Total revenue: guidance $522M–$524M (midpoint $523M), raised in Q3. Actual $526.5M. Variance +$3.50M (+0.67%). Position: above the high end.

4. Adjusted EBITDA (non-GAAP, loss shown as negative): guidance ($155M) to ($151M) (midpoint ($153M)). Actual ($149.7M). Variance +$3.30M (+2.16% of the guided loss magnitude). Position: above the high end. The loss was smaller than guided, which is better for the company.

Context: the letter itself rounds Adjusted EBITDA to about ($150M), and IFP to about $944M. Gross profit ($166.9M), net loss ($202.2M, or ($2.85) per share) and free cash flow (($20.8M)) were reported but had no guidance in the Q3 table. The company's headline "Adjusted Free Cash Flow" of $47.6M is a different non-GAAP measure and was not compared. The variance percentages above are derived by me from the stated figures.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm",
            "name": "Lemonade Q3 2024 Shareholder Letter (8-K, 2024-10-30)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142125000021/lmndshareholderletterq42.htm",
            "name": "Lemonade Q4 2024 Shareholder Letter (8-K, February 2025)"
        }
    ]
}
