## Rollout `inv1`
- outcome: submitted
- turns: 4; cost: $0.010; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm", "key": "q3guidance"})
  result: SUCCESS: The result has been saved to the data storage under the key: q3guidance. (45,843 characters)
  The data_storage currently contains the following keys:
  q3guidance
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142125000021/lmndshareholderletterq42.htm", "key": "q4results"})
  result: SUCCESS: The result has been saved to the data storage under the key: q4results. (53,419 characters)
  The data_storage currently contains the following keys:
  q3guidance
  q4results
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Lemonade Q3 2024 shareholder letter, find the full-year 2024 guidance table/column. List for FY2024 the low and high guidance for: In-force premium (IFP), Gross earned premium (GEP), Revenue, Adjusted EBITDA loss. State units ($ millions) and whether guidance is stated as a range. Quote the exact table rows. {{q3guidance}}"})
  result: **FY2024 guidance (Full Year 2024 columns, in $ millions)**
  
  The guidance table has two column groups, Q4 2024 and Full Year 2024, each with Low and High values. The four rows you asked for are:
  
  | Metric | FY2024 Low | FY2024 High | Units | Range? |
  |---|---|---|---|---|
  | In Force Premium (IFP) | $940 | $944 | $ millions | Yes |
  | Gross Earned Premium (GEP) | $823 | $826 | $ millions | Yes |
  | Revenue | $522 | $524 | $ millions | Yes |
  | Adjusted EBITDA Loss | ($155) | ($151) | $ millions | Yes |
  
  **Exact table rows as quoted from the letter** (column order: Q4 Low, Q4 High, FY Low, FY High):
  
  - "In Force Premium (IFP) $940 $944 $940 $944"
  - "Gross Earned Premium (GEP) $222 $225 $823 $826"
  - "Revenue $144 $146 $522 $524"
  - "Adjusted EBITDA Loss ($29) ($25) ($155) ($151)"
  
  Each metric is stated as a low-to-high range. The Adjusted EBITDA loss is shown in parentheses, so the low end ($155) is the larger loss and the high end ($151) is the smaller loss. The letter says the company is "increasing full year guidance for gross earned premium and revenue, and reaffirming guidance for FY 2024 for all other metrics." The FY IFP figure matches the Q4 figure because IFP is an end-of-period metric.
- retrieve_information({"prompt": "From this Lemonade Q4 2024 shareholder letter, find full-year 2024 results: In-force premium (IFP), Gross earned premium (GEP) full year 2024, Revenue full year 2024, Adjusted EBITDA loss full year 2024. State exact figures, units ($ millions), and whether they are full-year figures and GAAP/non-GAAP. Quote the exact table rows. {{q4results}}"})
  result: ## Full-Year 2024 Results (Lemonade Q4 2024 Shareholder Letter)
  
  | Metric | FY 2024 value | Units | Period type | GAAP / non-GAAP |
  |---|---|---|---|---|
  | In-force premium (IFP) | $943.7M | $ millions | Point-in-time, as of Dec 31, 2024 (not a full-year flow) | Operating KPI (not a GAAP line item; not labeled non-GAAP in the letter) |
  | Gross earned premium (GEP) | $827.3M | $ millions | Full year (Jan 1 to Dec 31, 2024) | Operating KPI (the letter lists it among KPIs, not non-GAAP measures) |
  | Total revenue | $526.5M | $ millions | Full year | GAAP |
  | Adjusted EBITDA | ($149.7)M loss | $ millions | Full year | Non-GAAP |
  
  ## Exact Table Rows
  
  **Key Operating and Financial Metrics** (columns: Three Months Q4 2024, Q4 2023, Year Ended 2024, 2023):
  - "In force premium (end of period) $ 943.7 $ 747.3 $ 943.7 $ 747.3"
  - "Gross earned premium $ 226.4 $ 181.0 $ 827.3 $ 672.3"
  - "Total revenue $ 148.8 $ 115.5 $ 526.5 $ 429.8"
  - "Adjusted EBITDA $ (23.8) $ (28.9) $ (149.7) $ (172.6)"
  
  **Condensed Consolidated Statements of Operations** (GAAP):
  - "Total revenue 148.8 115.5 526.5 429.8"
  
  **Adjusted EBITDA reconciliation** (non-GAAP):
  - "Adjusted EBITDA $ (23.8) $ (28.9) $ (149.7) $ (172.6)"
  
  ## Notes
  - **IFP** is an end-of-period figure, so the $943.7M is the annualized premium in force at December 31, 2024, not a sum of the year's premium. The letter's "full year" IFP figure is the same as the Q4 end-of-period value.
  - **GEP of $827.3M** is the full-year figure. The $226.4M in the table is the Q4-only figure and should not be used as the full-year number.
  - **Adjusted EBITDA** is a loss, so it appears as a negative number. The letter's text rounds it to "($150) million."
  - The guidance table (for Q1 and FY 2025) is forward-looking and not part of these results.

### Turn 3  (stop_reason=end_turn)
**Answer:** Lemonade's FY2024 results beat the top end of the full-year guidance in its Q3 2024 letter on gross earned premium, revenue and Adjusted EBITDA. In-force premium landed inside the range, and it was the only metric that did not beat the high end.

**Guidance (Q3 2024 shareholder letter, FY2024 column, $ millions)**
- In-force premium (IFP): $940 to $944 (midpoint $942)
- Gross earned premium (GEP): $823 to $826 (midpoint $824.5)
- Revenue: $522 to $524 (midpoint $523)
- Adjusted EBITDA: ($155) to ($151) (midpoint ($153))

The letter said Lemonade was increasing full-year guidance for GEP and revenue and reaffirming the other metrics.

**Actuals (Q4 2024 shareholder letter, year ended 2024, $ millions)**
- IFP, end of period at Dec 31, 2024: $943.7
- GEP, full year: $827.3 (the $226.4 in the table is the Q4-only figure, so I did not use it)
- Total revenue, full year (GAAP): $526.5
- Adjusted EBITDA, full year (non-GAAP): ($149.7)

**Comparison**
- **IFP:** $943.7 is within the range, $0.7 below the high end and $1.7 above the midpoint (+0.18% vs. midpoint). Because IFP is a point-in-time metric, the full-year guidance figure and the year-end figure are directly comparable.
- **GEP:** $827.3 is above the range by $1.3 (+0.16% vs. the $826 high end). It is $2.8 above the midpoint (+0.34%).
- **Revenue:** $526.5 is above the range by $2.5 (+0.48% vs. the $524 high end). It is $3.5 above the midpoint (+0.67%).
- **Adjusted EBITDA:** The loss of ($149.7) is smaller than
…[truncated 1,186 chars]

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "Lemonade FY2024 results versus the full-year 2024 guidance given in the Q3 2024 shareholder letter.\n\nOverall: Gross earned premium, revenue and Adjusted EBITDA beat the top end of the guidance range. In-force premium landed inside the range, slightly above the midpoint.\n\nGuidance (Q3 2024 shareholder letter, 8-K EX-99.1 dated Oct 30, 2024; FY2024 column; $ millions):\n- In-force premium (IFP): 940 to 944 (midpoint 942)\n- Gross earned premium (GEP): 823 to 826 (midpoint 824.5)\n- Revenue: 522 to 524 (midpoint 523)\n- Adjusted EBITDA: (155) to (151) (midpoint (153))\nThe letter said Lemonade was increasing full-year guidance for GEP and revenue and reaffirming guidance f
…[truncated 1,803 chars])

### Final answer
Lemonade FY2024 results versus the full-year 2024 guidance given in the Q3 2024 shareholder letter.

Overall: Gross earned premium, revenue and Adjusted EBITDA beat the top end of the guidance range. In-force premium landed inside the range, slightly above the midpoint.

Guidance (Q3 2024 shareholder letter, 8-K EX-99.1 dated Oct 30, 2024; FY2024 column; $ millions):
- In-force premium (IFP): 940 to 944 (midpoint 942)
- Gross earned premium (GEP): 823 to 826 (midpoint 824.5)
- Revenue: 522 to 524 (midpoint 523)
- Adjusted EBITDA: (155) to (151) (midpoint (153))
The letter said Lemonade was increasing full-year guidance for GEP and revenue and reaffirming guidance for the other metrics.

Actuals (Q4 2024 shareholder letter, 8-K EX-99.1; year ended 2024 unless noted; $ millions):
- IFP, end of period at Dec 31, 2024: 943.7 (point-in-time metric)
- GEP, full year: 827.3 (the 226.4 shown in the table is the Q4-only figure and was not used)
- Total revenue, full year (GAAP): 526.5
- Adjusted EBITDA, full year (non-GAAP): (149.7)

Comparison:
- IFP: 943.7 is within the range. It is 0.3 below the high end and 1.7 above the midpoint (+0.18% vs. midpoint).
- GEP: 827.3 is above the range by 1.3 (+0.16% vs. the 826 high end). It is 2.8 above the midpoint (+0.34%).
- Revenue: 526.5 is above the range by 2.5 (+0.48% vs. the 524 high end). It is 3.5 above the midpoint (+0.67%).
- Adjusted EBITDA: the loss of (149.7) is smaller than guided. It beats the high end (151) by 1.3 (0.86% smaller loss) and the midpoint (153) by 3.3 (2.16% smaller loss).

Conclusion: Against the prior quarter's full-year guidance, FY2024 results were above the range for GEP, revenue and Adjusted EBITDA (a smaller loss than guided), and within the range but above the midpoint for IFP.

Sources:
- Lemonade Q3 2024 shareholder letter (8-K EX-99.1): https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm
- Lemonade Q4 2024 shareholder letter (8-K EX-99.1): https://www.sec.gov/Archives/edgar/data/1691421/000169142125000021/lmndshareholderletterq42.htm

{"sources": [{"url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm", "name": "Lemonade Q3 2024 Shareholder Letter (8-K EX-99.1)"}, {"url": "https://www.sec.gov/Archives/edgar/data/1691421/000169142125000021/lmndshareholderletterq42.htm", "name": "Lemonade Q4 2024 Shareholder Letter (8-K EX-99.1)"}]}