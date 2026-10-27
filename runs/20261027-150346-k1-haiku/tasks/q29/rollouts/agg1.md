## Rollout `agg1`
- outcome: submitted
- turns: 4; cost: $0.280; submitted: True

### Turn 1  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm", "key": "save10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: save10k. (635,378 characters)
  The data_storage currently contains the following keys:
  save10k
  

### Turn 2  (stop_reason=tool_use)
- retrieve_information({"prompt": "From {{save10k}}, find the table titled \"Comparative Operating Statistics\" (or similar operating statistics / KPI table) in Item 7 MD&A for the twelve months ended December 31, 2024 vs 2023. List every row in the table in order, with the unit, the 2024 value, and the 2023 value. Also state whether any rows are non-GAAP, and note whether rows are averages/rates/unit costs (full-year figures). Include the full table row count."})
  result: The table is titled **"Operating Statistics (unaudited)"** and appears under "Comparative Operating Statistics" in Item 7 (MD&A). It has **16 data rows**, not counting the header.
  
  | # | Metric | Unit | 2024 | 2023 | Type |
  |---|---|---|---|---|---|
  | 1 | Average aircraft | Count (daily average) | 209.9 | 199.5 | Average |
  | 2 | Aircraft at end of period (B) | Count | 213 | 205 | Point-in-time |
  | 3 | Average daily aircraft utilization | Hours per day | 9.9 | 11.1 | Average/rate |
  | 4 | Departures | Count | 288,180 | 297,900 | Full-year total |
  | 5 | Passenger flight segments (PFSs) | Thousands | 44,180 | 44,105 | Full-year total |
  | 6 | Revenue passenger miles (RPMs) | Thousands | 43,671,009 | 45,243,787 | Full-year total |
  | 7 | Available seat miles (ASMs) | Thousands | 53,017,948 | 55,665,561 | Full-year total |
  | 8 | Load factor | % | 82.4% | 81.3% | Rate |
  | 9 | Total revenue per passenger flight segment | $ | 111.21 | 121.58 | Average per unit |
  | 10 | Average yield | Cents per RPM | 11.25 | 11.85 | Average/rate |
  | 11 | TRASM (total operating revenue per ASM) | Cents per ASM | 9.27 | 9.63 | Unit revenue |
  | 12 | CASM (operating expenses per ASM) | Cents per ASM | 11.35 | 10.52 | Unit cost |
  | 13 | Adjusted CASM | Cents per ASM | 10.76 | 10.33 | Unit cost (non-GAAP) |
  | 14 | Adjusted CASM ex-fuel | Cents per ASM | 7.97 | 7.06 | Unit cost (non-GAAP) |
  | 15 | Fuel gallons consumed | Thousands of gallons | 551,819 | 591,796 | Full-year total |
  | 16 | Average fuel cost per gallon | $ per gallon | 2.68 | 3.08 | Average/rate |
  
  The table also shows a percent change column. Those values are: 5.2%, 3.9%, (10.8)%, (3.3)%, 0.2%, (3.5)%, (4.8)%, 1.1 pts, (8.5)%, (5.1)%, (3.7)%, 7.9%, 4.2%, 12.9%, (6.8)%, and (13.0)%.
  
  **Non-GAAP rows:** Only rows 13 and 14 (Adjusted CASM and
  …[truncated 864 chars]

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "Quote verbatim the \"Comparative Operating Statistics\" / \"Operating Statistics (unaudited)\" table from {{save10k}} exactly as it appears, including the column headers and all rows (aircraft, departures, PFSs, RPMs, ASMs, load factor, yield, TRASM, CASM, adjusted CASM, fuel gallons, fuel cost per gallon), and the footnote text under it."})
  result: The table as it appears in the filing text (the source extraction flattens the table layout, so I've kept the text as it appears):
  
  > Twelve Months Ended December 31, Percent Change 20242023Operating Statistics (unaudited) (A):Average aircraft209.9 199.5 5.2 %Aircraft at end of period (B)213 205 3.9 %Average daily aircraft utilization (hours)9.9 11.1 (10.8)%Departures288,180 297,900 (3.3)%Passenger flight segments (PFSs) (thousands)44,180 44,105 0.2 %Revenue passenger miles (RPMs) (thousands)43,671,009 45,243,787 (3.5)%Available seat miles (ASMs) (thousands)53,017,948 55,665,561 (4.8)%Load factor (%)82.4 %81.3 %1.1 ptsTotal revenue per passenger flight segment ($)111.21 121.58 (8.5)%Average yield (cents)11.25 11.85 (5.1)%TRASM (cents)9.27 9.63 (3.7)%CASM (cents)11.35 10.52 7.9 %Adjusted CASM (cents)10.76 10.33 4.2 %Adjusted CASM ex-fuel (cents)7.97 7.06 12.9 %Fuel gallons consumed (thousands)551,819 591,796 (6.8)%Average fuel cost per gallon ($)2.68 3.08 (13.0)%    (A) See "Glossary of Airline Terms" elsewhere in this annual report for definitions used in this table.(B) Includes 21 aircraft recorded as assets held for sale on our consolidated balance sheets as of December 31, 2024. Refer to "Notes to Consolidated Financial Statements—1. Summary of Significant Accounting Policies" for additional information on the aircraft recorded as assets held for sale.

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "Spirit Airlines (NYSE: SAVE) reported its operating statistics in the \"Comparative Operating Statistics\" table in Item 7 (MD&A) of its FY2024 Form 10-K. The table is labelled unaudited and covers the twelve months ended December 31, 2024, compared with 2023. I checked the table text directly in the filing and the figures below match it.\n\nFY2024 operating KPIs (twelve months ended Dec 31, 2024; 2023 comparative in parentheses):\n\n1. Average aircraft: 209.9 (199.5) - daily average count\n2. Aircraft at end of period: 213 (205) - point-in-time count at Dec 31; includes 21 aircraft held for sale\n3. Average daily aircraft utilization: 9.9 hours per day (11.1)\n4. Departure
…[truncated 1,642 chars])

### Final answer
Spirit Airlines (NYSE: SAVE) reported its operating statistics in the "Comparative Operating Statistics" table in Item 7 (MD&A) of its FY2024 Form 10-K. The table is labelled unaudited and covers the twelve months ended December 31, 2024, compared with 2023. I checked the table text directly in the filing and the figures below match it.

FY2024 operating KPIs (twelve months ended Dec 31, 2024; 2023 comparative in parentheses):

1. Average aircraft: 209.9 (199.5) - daily average count
2. Aircraft at end of period: 213 (205) - point-in-time count at Dec 31; includes 21 aircraft held for sale
3. Average daily aircraft utilization: 9.9 hours per day (11.1)
4. Departures: 288,180 (297,900)
5. Passenger flight segments (PFSs): 44,180 thousand (44,105 thousand)
6. Revenue passenger miles (RPMs): 43,671,009 thousand (45,243,787 thousand)
7. Available seat miles (ASMs): 53,017,948 thousand (55,665,561 thousand)
8. Load factor: 82.4% (81.3%)
9. Total revenue per passenger flight segment: $111.21 ($121.58)
10. Average yield: 11.25 cents per RPM (11.85)
11. TRASM (total operating revenue per ASM): 9.27 cents (9.63)
12. CASM (operating expenses per ASM): 11.35 cents (10.52)
13. Adjusted CASM (non-GAAP): 10.76 cents (10.33)
14. Adjusted CASM ex-fuel (non-GAAP): 7.97 cents (7.06)
15. Fuel gallons consumed: 551,819 thousand gallons (591,796 thousand)
16. Average fuel cost per gallon: $2.68 ($3.08)

Notes:
- Rows 1, 3, 8 to 14 and 16 are averages, rates or per-unit figures, which are full-year values rather than sums. Row 2 is a point-in-time count.
- Rows 4 to 7 and 15 are full-year totals.
- Adjusted CASM and Adjusted CASM ex-fuel are the only rows the filing identifies as non-GAAP. CASM and TRASM are calculated from GAAP figures but are not labelled non-GAAP.
- The table also shows year-over-year percent changes (for example, CASM up 7.9% and fuel cost per gallon down 13.0%).

Source: Spirit Airlines, Form 10-K for fiscal year 2024 (filed 2025), Item 7 MD&A, "Comparative Operating Statistics."

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1498710/000149871025000008/save-20241231.htm",
            "name": "Spirit Airlines FY2024 Form 10-K (Comparative Operating Statistics, Item 7 MD&A)"
        }
    ]
}