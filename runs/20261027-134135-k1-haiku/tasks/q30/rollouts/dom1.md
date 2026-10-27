## Rollout `dom1`
- outcome: submitted
- turns: 7; cost: $0.214; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "convertible_notes_dilution"})
  result: ---
  name: convertible_notes_dilution
  description: Share-count dilution from convertible senior notes (maximum or if-converted shares) at a balance-sheet date, built from the 10-K debt and EPS notes.
  ---
  
  # Convertible notes: dilutive share count
  
  ANALYTIC MOVE: calculate and reconcile. Inputs are the principal outstanding and the conversion rate for each note series at the stated date. Result is shares issuable per series and in total, reconciled to the figure the company reports.
  
  ## Where the figures live (10-K)
  - Net loss per share note (in this task, Note 3): the table of potentially dilutive securities excluded as anti-dilutive. It has a "Convertible Notes (if-converted)" line in thousands of shares at each year-end. This is the company's own aggregate share count.
  - Debt note (in this task, Note 7): per series, the principal outstanding, conversion rate per $1,000, conversion price, maturity, and make-whole or fundamental-change language. Item 7 liquidity repeats some of it.
  - Capped-call and hedge paragraphs: capped calls offset dilution economically but do not lower the gross shares issuable. Report gross and mention the capped calls separately.
  - Each series' indenture or its 8-K exhibit 4.x gives the "maximum conversion rate" that applies after a make-whole fundamental change. Treat it as a separate upper bound.
  
  ## Verified in this task (Snap FY2024 10-K, read through the retrieval tool, so re-confirm in the text)
  - The if-converted line was 85,945 thousand shares at 12/31/2024 (89,379 thousand at 12/31/2023 and 2022).
  - Principal x conversion rate by series at 12/31/2024 sums to about 85,945 thousand. Per series: 2025 notes $36.24M at 46.1233; 2026 notes $249.754M at 43.8481; 2027 notes $1,150M at 11.2042; 2028 notes $1,500M at 17.7494; 2030 notes $750M at 4
  …[truncated 1,579 chars]
- edgar_search({"search_query": "Snap Inc convertible senior notes if-converted shares dilutive", "start_date": "2025-01-01", "end_date": "2025-04-07", "form_types": ["10-K"]})
  result: {"total_matching_documents": 14, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-05", "period_ending": "2024-12-31", "company": "Snap Inc  (SNAP)  (CIK 0001564408)", "ciks": ["0001564408"], "accession": "0001564408-25-000019", "document": "snap-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm"}, {"form": "10-K", "file_date": "2025-03-28", "period_ending": "2024-12-31", "company": "Coeptis Therapeutics Holdings, Inc.  (COEP, COEPW)  (CIK 0001759186)", "ciks": ["0001759186"], "accession": "0001683168-25-001942", "document": "coeptis_i10k-123124.htm", "description": "FORM 10-K FOR DEC 2024", "url": "https://www.sec.gov/Archives/edgar/data/1759186/000168316825001942/coeptis_i10k-123124.htm"}, {"form": "10-K", "file_date": "2025-02-27", "period_ending": "2024-12-31", "company": "Match Group, Inc.  (MTCH)  (CIK 0000891103)", "ciks": ["0000891103"], "accession": "0000891103-25-000027", "document": "mtch-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/891103/000089110325000027/mtch-20241231.htm"}, {"form": "10-K", "file_date": "2025-03-20", "period_ending": "2024-12-31", "company": "Barinthus Biotherapeutics plc.  (BRNS)  (CIK 0001828185)", "ciks": ["0001828185"], "accession": "0001828185-25-000021", "document": "brns-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1828185/000182818525000021/brns-20241231.htm"}, {"form": "10-K", "file_date": "2025-03-24", "period_ending": "2024-12-31", "company": "AEON Biopharma, Inc.  (AEON)  (CIK 0001837607)", "ciks": ["0001837607"], "accession": "0001837607-25-000022", "document": "aeon-20241231x10k.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/da
  …[truncated 3,198 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm", "key": "snap10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: snap10k. (614,017 characters)
  The data_storage currently contains the following keys:
  snap10k
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Snap 10-K text: {{snap10k}}. (1) Find the anti-dilutive securities table in the net loss per share note, quoting the \"Convertible Notes\" if-converted line for 2024 and 2023 with units. (2) For each convertible senior notes series (2025, 2026, 2027, 2028, 2030 notes), give the principal outstanding at 12/31/2024 and the conversion rate per $1,000 principal and conversion price. (3) Quote any text on maximum conversion rate, make-whole fundamental change, or maximum number of shares issuable. Be exact and quote figures with units."})
  result: **(1) Anti-dilutive securities (Note 3, Net Loss per Share)**
  
  The table is headed "(in thousands)," so the share counts are in thousands of shares:
  
  - Convertible Notes (if-converted): **85,945** thousand shares for 2024; **89,379** thousand shares for 2023 (and 89,379 thousand for 2022).
  
  **(2) Convertible senior notes at December 31, 2024 (Note 7)**
  
  Principal amounts are from the Convertible Notes table, in thousands of USD:
  
  | Series | Principal at 12/31/2024 | Conversion rate (shares of Class A per $1,000 principal) | Conversion price |
  |---|---|---|---|
  | 2025 Notes | $36,240 thousand ($36.2 million) | 46.1233 | approx. $21.68 per share |
  | 2026 Notes | $249,754 thousand ($249.8 million) | 43.8481 | approx. $22.81 per share |
  | 2027 Notes | $1,150,000 thousand ($1.15 billion) | 11.2042 | approx. $89.25 per share |
  | 2028 Notes | $1,500,000 thousand ($1.50 billion) | 17.7494 | approx. $56.34 per share |
  | 2030 Notes | $750,000 thousand ($750.0 million) | 45.0846 (initial conversion rate) | approx. $22.18 per share |
  
  Total principal across the five series is $3,685,994 thousand. The 2028 and 2030 rates are described as "initial" conversion rates in the filing.
  
  **(3) Maximum conversion rate, make-whole, and maximum share language**
  
  - **Make-whole (2030 Notes, Note 7):** "Holders of the 2030 Notes who convert the 2030 Notes in connection with a make-whole fundamental change, as defined in the indenture governing the 2030 Notes, or in connection with a redemption are entitled to an increase in the conversion rate."
  - **Make-whole (Risk Factors):** "if a make-whole fundamental change as defined in each of the indentures governing the Convertible Notes, or the Indentures, occurs prior to the maturity date of the Convertible Notes, we will in some cases be required to
  …[truncated 938 chars]

### Turn 4  (stop_reason=tool_use)
- edgar_search({"search_query": "Snap 2030 Notes indenture maximum conversion rate 59.7371", "start_date": "2024-01-01", "end_date": "2025-04-07"})
  result: {"total_matching_documents": 2, "page": 1, "results": [{"form": "8-K", "file_date": "2024-05-13", "period_ending": "2024-05-08", "company": "Snap Inc  (SNAP)  (CIK 0001564408)", "ciks": ["0001564408"], "accession": "0001193125-24-137315", "document": "d821313d8k.htm", "description": "8-K", "url": "https://www.sec.gov/Archives/edgar/data/1564408/000119312524137315/d821313d8k.htm"}, {"form": "8-K", "file_date": "2024-05-13", "period_ending": "2024-05-08", "company": "Snap Inc  (SNAP)  (CIK 0001564408)", "ciks": ["0001564408"], "accession": "0001193125-24-137315", "document": "d821313dex41.htm", "description": "EX-4.1", "url": "https://www.sec.gov/Archives/edgar/data/1564408/000119312524137315/d821313dex41.htm"}]}

### Turn 5  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1564408/000119312524137315/d821313d8k.htm", "key": "8k2030"})
  result: SUCCESS: The result has been saved to the data storage under the key: 8k2030. (18,539 characters)
  The data_storage currently contains the following keys:
  snap10k
  8k2030
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1564408/000119312524137315/d821313dex41.htm", "key": "ex41"})
  result: SUCCESS: The result has been saved to the data storage under the key: ex41. (349,196 characters)
  The data_storage currently contains the following keys:
  snap10k
  8k2030
  ex41
  

### Turn 6  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this text: {{ex41}} and {{8k2030}}. Find the 2030 Notes \"maximum conversion rate\" (per $1,000 principal) and the initial conversion rate, and any statement of the maximum number of shares issuable. Also state whether any other series (2025, 2026, 2027, 2028 Notes) has a maximum conversion rate. Quote briefly."})
  result: **2030 Notes**
  
  - **Initial conversion rate:** Section 14.01(a) states the Notes are convertible "at an initial conversion rate of 45.0846 shares of Common Stock (subject to adjustment as provided in this Article 14, the 'Conversion Rate') per $1,000 principal amount of Notes."
  - **Maximum conversion rate:** Section 14.03(e) states: "Notwithstanding the foregoing, in no event shall the Conversion Rate per $1,000 principal amount of Notes exceed 59.7371 shares of Common Stock, subject to adjustment in the same manner as the Conversion Rate pursuant to Section 14.04."
  - **Maximum number of shares:** The indenture does not state a total share cap. The Form 8-K (Item 3.02) does: "Including the full exercise by the Initial Purchasers of the Notes Option, a maximum of 44,802,825 shares of our Class A common stock may be issued upon conversion of the Notes, based on the initial maximum conversion rate of 59.7371 shares of our Class A common stock per $1,000 principal amount of Notes." This matches $750,000,000 ÷ $1,000 × 59.7371.
  
  **Other series (2025, 2026, 2027, 2028 Notes)**
  
  The text does not state a maximum conversion rate for any other series. The document is the indenture for the 0.50% Convertible Senior Notes due 2030 and the related 8-K. The 8-K mentions the 0.25% Convertible Senior Notes due 2025 and the 0.75% Convertible Senior Notes due 2026 only in the context of repurchases. It gives no conversion rates for them, and it does not mention any 2027 or 2028 Notes at all.

### Turn 7  (stop_reason=tool_use)
- submit_final_result({"final_result": "\n**Answer: Snap's reported maximum dilution from its convertible notes at 12/31/2024 is 85,945 thousand shares (about 85.95 million Class A shares), on an if-converted basis. The filing does not state a single all-series maximum share count.**\n\n**Key figures and reconciliation (Snap FY2024 10-K, filed 2025-02-05)**\n- The anti-dilutive securities table (Net Loss per Share note, in thousands of shares) shows \"Convertible Notes (if-converted)\" of 85,945 thousand at 12/31/2024, versus 89,379 thousand at 12/31/2023.\n- I recomputed shares issuable as principal ÷ 1,000 × conversion rate for each series. Principal and rates are from the Convertible Notes note (Note 7):\n\n| 
…[truncated 2,252 chars])

### Final answer

**Answer: Snap's reported maximum dilution from its convertible notes at 12/31/2024 is 85,945 thousand shares (about 85.95 million Class A shares), on an if-converted basis. The filing does not state a single all-series maximum share count.**

**Key figures and reconciliation (Snap FY2024 10-K, filed 2025-02-05)**
- The anti-dilutive securities table (Net Loss per Share note, in thousands of shares) shows "Convertible Notes (if-converted)" of 85,945 thousand at 12/31/2024, versus 89,379 thousand at 12/31/2023.
- I recomputed shares issuable as principal ÷ 1,000 × conversion rate for each series. Principal and rates are from the Convertible Notes note (Note 7):

| Series | Principal 12/31/2024 ($000) | Conversion rate per $1,000 | Base shares (000) |
|---|---|---|---|
| 2025 Notes | 36,240 | 46.1233 | 1,671.51 |
| 2026 Notes | 249,754 | 43.8481 | 10,951.24 |
| 2027 Notes | 1,150,000 | 11.2042 | 12,884.83 |
| 2028 Notes | 1,500,000 | 17.7494 | 26,624.10 |
| 2030 Notes | 750,000 | 45.0846 | 33,813.45 |
| **Total** | 3,685,994 | | **85,945.13** |

The recomputed base total of 85,945.13 thousand reconciles to the reported 85,945 thousand.

**Make-whole maximum (2030 Notes only)**
- The 2030 Notes indenture caps the conversion rate at 59.7371 shares per $1,000 principal, which applies on a make-whole conversion.
- Applied to $750,000,000 principal, this gives 44,802,825 shares (the 8-K figure, which includes the initial purchasers' option), versus 33,813,450 at the base rate. The increase is about 10,989,375 shares.

**Why I do not report a combined maximum**
- I found a maximum conversion rate only for the 2030 Notes. The 2025, 2026, 2027 and 2028 Notes' maximum rates were not found in the retrieved documents, so I cannot build a total maximum across all series.
- Combining the 2030 Notes at maximum with the other series at base rates would give roughly 96,934 thousand shares. This is only an illustration, not a verified maximum, because the other series' maxima are unknown.
- Capped calls (cap prices of $32.12, $32.58, $121.02, $93.90 and $33.48 per share for the 2025, 2026, 2027, 2028 and 2030 transactions) offset economic dilution but do not reduce the gross share count.

**Sources**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm",
            "name": "Snap Inc. FY2024 Form 10-K (period ending 2024-12-31)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1564408/000119312524137315/d821313d8k.htm",
            "name": "Snap Inc. Form 8-K filed 2024-05-13 (2030 Notes issuance)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1564408/000119312524137315/d821313dex41.htm",
            "name": "Snap Inc. Form 8-K Exhibit 4.1 (2030 Notes indenture)"
        }
    ]
}
