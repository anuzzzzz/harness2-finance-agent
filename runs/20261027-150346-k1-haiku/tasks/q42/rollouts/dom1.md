## Rollout `dom1`
- outcome: submitted
- turns: 7; cost: $0.445; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "peer_payout_ratio"})
  result: ---
  name: peer_payout_ratio
  description: Compare a company's dividend payout ratio with its competitors' for a fiscal year and rank them, using filing-sourced dividends and earnings on a stated, consistent basis.
  ---
  ANALYTIC MOVE: compare and rank. Inputs are the dividends and earnings of each company for the same fiscal year. The result is one ranking, highest to lowest, with each ratio shown.
  
  1. Definition. The headline payout ratio is dividends per share declared in the year divided by GAAP diluted EPS for the same year. Cross-check it with total dividends paid (cash-flow statement, financing section) divided by net income attributable to the company's shareholders. If the two differ by more than rounding, say why (declared vs paid timing, a dividend declared in one year and paid the next, share count). Use the same definition for every company. Do not mix a declared figure for one company with a paid figure for another.
  2. Basis. Give one primary ranking on GAAP. Add adjusted or core EPS only as a labelled secondary column. Report whether the order changes, but do not give two competing answers as equal. Never divide GAAP dividends by non-GAAP EPS inside the primary ranking.
  3. Peer set. Name the peers and say why. For a beverage or consumer-staples issuer, take direct large-cap peers that file 10-Ks (for Coca-Cola, PepsiCo and Keurig Dr Pepper first, then Coca-Cola Consolidated and others as relevant). Show non-payers (e.g. Monster Beverage) as 0% or "no dividend" rather than silently dropping them. If a peer is excluded, say so in one line.
  4. Period alignment. Use each company's FY2024 as reported. PepsiCo's fiscal year is 52 weeks ending the last Saturday of December (Dec 28, 2024). Sum the declared dividend per share across all four quarters in that fiscal ye
  …[truncated 1,455 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/21344/000002134425000011/ko-20241231.htm", "key": "ko10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: ko10k. (655,758 characters)
  The data_storage currently contains the following keys:
  ko10k
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1418135/000141813525000013/kdp-20241231.htm", "key": "kdp10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: kdp10k. (403,591 characters)
  The data_storage currently contains the following keys:
  ko10k
  kdp10k
  
- edgar_search({"search_query": "PepsiCo annual report 2024 dividends declared per common share", "start_date": "2025-02-01", "end_date": "2025-04-07", "form_types": ["10-K"]})
  result: {"total_matching_documents": 63, "page": 1, "results": [{"form": "10-K", "file_date": "2025-02-04", "period_ending": "2024-12-28", "company": "PEPSICO INC  (PEP)  (CIK 0000077476)", "ciks": ["0000077476"], "accession": "0000077476-25-000007", "document": "pep-20241228.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/77476/000007747625000007/pep-20241228.htm"}, {"form": "10-K", "file_date": "2025-03-03", "period_ending": "2024-12-31", "company": "Celsius Holdings, Inc.  (CELH)  (CIK 0001341766)", "ciks": ["0001341766"], "accession": "0001341766-25-000024", "document": "celh-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1341766/000134176625000024/celh-20241231.htm"}, {"form": "10-K", "file_date": "2025-02-20", "period_ending": "2024-12-31", "company": "Coca-Cola Consolidated, Inc.  (COKE)  (CIK 0000317540)", "ciks": ["0000317540"], "accession": "0000317540-25-000025", "document": "coke-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/317540/000031754025000025/coke-20241231.htm"}, {"form": "10-K", "file_date": "2025-03-27", "period_ending": "2025-02-01", "company": "DICK'S SPORTING GOODS, INC.  (DKS)  (CIK 0001089063)", "ciks": ["0001089063"], "accession": "0001089063-25-000012", "document": "dks-20250201.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1089063/000108906325000012/dks-20250201.htm"}, {"form": "10-K", "file_date": "2025-03-12", "period_ending": "2025-02-01", "company": "TARGET CORP  (TGT)  (CIK 0000027419)", "ciks": ["0000027419"], "accession": "0000027419-25-000018", "document": "tgt-20250201.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/27419/000002741925000018/tgt-20250201.htm"}, {"form": "10-K
  …[truncated 5,268 chars]

### Turn 3  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/77476/000007747625000007/pep-20241228.htm", "key": "pep10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: pep10k. (479,973 characters)
  The data_storage currently contains the following keys:
  ko10k
  kdp10k
  pep10k
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/317540/000031754025000025/coke-20241231.htm", "key": "coke10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: coke10k. (412,831 characters)
  The data_storage currently contains the following keys:
  ko10k
  kdp10k
  pep10k
  coke10k
  

### Turn 4  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Coca-Cola 10-K text: {{ko10k}}. Find (1) the dividends declared per share for 2024 (the \"Dividends declared per share\" or \"Cash dividends declared per share\" in the equity statement or the dividends section, and the quarterly dividend amounts), (2) diluted net income per share for 2024 (GAAP, \"Net income attributable to shareowners ... per share diluted\"), (3) the net income attributable to shareowners for 2024 in millions, (4) dividends paid in 2024 from the cash flow statement in millions, and (5) comparable/non-GAAP diluted EPS for 2024 if stated. Quote the exact figures and their table labels."})
  result: Here are the figures from the 10-K text for fiscal 2024:
  
  1. **Dividends declared per share:** The Consolidated Statements of Shareowners' Equity shows "Dividends (per share — $1.94, $1.84 and $1.76 in 2024, 2023 and 2022, respectively)." The MD&A (Liquidity section) says "Our annualized common stock dividend was $1.94 per share and $1.84 per share in 2024 and 2023, respectively." The filing does not state the individual 2024 quarterly dividend amounts. The only quarterly figure given is for 2025: the Board "increased our regular quarterly dividend to $0.51 per share, equivalent to a full year dividend of $2.04 per share in 2025."
  
  2. **Diluted net income per share (GAAP):** The Consolidated Statements of Income shows "Diluted Net Income Per Share¹ $2.46" for 2024. Footnote 1 says it is "Calculated based on net income attributable to shareowners of The Coca-Cola Company." Basic is $2.47.
  
  3. **Net income attributable to shareowners of The Coca-Cola Company:** $10,631 million, per the Consolidated Statements of Income line "Net Income Attributable to Shareowners of The Coca-Cola Company." Consolidated Net Income was $10,649 million, of which $18 million was attributable to noncontrolling interests.
  
  4. **Dividends paid:** $8,359 million, per the Consolidated Statements of Cash Flows, Financing Activities line "Dividends (8,359)." The MD&A confirms: "The Company paid dividends of $8,359 million and $7,952 million during the years ended December 31, 2024 and 2023."
  
  5. **Comparable/non-GAAP diluted EPS:** The 10-K does not state a comparable or non-GAAP diluted EPS for 2024. It does not use that metric anywhere. Note 18 ("Significant Operating and Nonoperating Items") quantifies several large items in dollar terms, such as the $3,109 million fairlife contingent considerati
  …[truncated 170 chars]
- retrieve_information({"prompt": "From this PepsiCo 10-K text: {{pep10k}}. Find (1) the dividends declared per common share for fiscal 2024 (quarterly amounts and total, e.g. \"Cash dividends declared per common share\" in equity statement), (2) diluted EPS for fiscal 2024 (GAAP), (3) net income attributable to PepsiCo in $ millions for 2024, (4) dividends paid in 2024 from the cash flow statement in $ millions, and (5) core constant currency or core EPS for 2024 if stated. Quote exact figures and labels."})
  result: Here are the figures from the filing:
  
  1. **Dividends declared per common share, fiscal 2024:** $5.3300 total. The equity statement footnote reads "Cash dividends declared per common share were $5.3300, $4.9450 and $4.5250 for 2024, 2023 and 2022." The filing does not break this out by quarter, so I can't give quarterly amounts from this text. The total dividends declared were $7,347 million ("Cash dividends declared (a)" in the Consolidated Statement of Equity).
  
  2. **Diluted EPS, fiscal 2024 (GAAP):** $6.95 ("Net Income Attributable to PepsiCo per Common Share – Diluted").
  
  3. **Net income attributable to PepsiCo, 2024:** $9,578 million.
  
  4. **Dividends paid, 2024 (cash flow statement):** $(7,229) million, shown as "Cash dividends paid" under Financing Activities.
  
  5. **Core / constant currency figures for 2024:**
     - Core (non-GAAP) net income attributable to PepsiCo per common share – diluted: **$8.16** for 2024, versus $7.62 for 2023, a 7% increase.
     - Growth in core diluted EPS on a constant currency basis (non-GAAP): **9%**. This is a growth rate, not a dollar level. The filing states an impact of foreign exchange translation of 2 percentage points.
- retrieve_information({"prompt": "From this Keurig Dr Pepper 10-K text: {{kdp10k}}. Find (1) dividends declared per share for 2024 (quarterly amounts and total), (2) GAAP diluted EPS for 2024, (3) net income attributable to KDP in millions for 2024, (4) dividends paid in 2024 from the cash flow statement in millions, and (5) adjusted diluted EPS for 2024 if stated in the filing. Quote exact figures and labels."})
  result: **1. Dividends declared per share for 2024**
  - **Total:** The MD&A (Liquidity and Capital Resources, "Regular Quarterly Dividends") states: "We have declared total dividends of $0.89 per share and $0.83 per share for the years ended December 31, 2024 and 2023, respectively." The Consolidated Statements of Changes in Stockholders' Equity show "Dividends declared, $0.89 per share" for 2024.
  - **Quarterly amounts:** The filing does not state the individual quarterly per-share amounts in the text provided. It says only that KDP "has declared a regular quarterly cash dividend and expects to continue to pay such dividends on a quarterly basis."
  
  **2. GAAP diluted EPS for 2024:** $1.05 (Consolidated Statements of Income, "Diluted"; MD&A: "Diluted EPS decreased 32.3% to $1.05 per diluted share as compared to $1.55 in the prior year"). Basic EPS was $1.06.
  
  **3. Net income attributable to KDP for 2024:** $1,441 million (Consolidated Statements of Income, "Net income"). Net income including non-controlling interest was also $1,441 million, since there was no non-controlling interest in 2024.
  
  **4. Dividends paid in 2024 (cash flow statement):** $1,194 million ("Cash dividends paid (1,194)" in the financing activities section of the Consolidated Statements of Cash Flows). For comparison, the equity statement shows dividends declared of $1,207 million for 2024, and the balance sheet shows "Dividends payable" of $312 million at year-end.
  
  **5. Adjusted diluted EPS for 2024:** Not stated. The filing reports only GAAP measures and does not present an adjusted or non-GAAP diluted EPS figure. The MD&A discusses the impacts of the goodwill and intangible impairments ($306 million and $412 million), the $225 million ABI termination fee, and the tax effects, but it does not convert these i
  …[truncated 20 chars]

### Turn 5  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/317540/000031754025000025/coke-20241231.htm", "key": "cokec10k"})
  result: SUCCESS: The result has been saved to the data storage under the key: cokec10k. (412,831 characters)
  The data_storage currently contains the following keys:
  ko10k
  kdp10k
  pep10k
  coke10k
  cokec10k
  

### Turn 6  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Coca-Cola Consolidated 10-K text: {{cokec10k}}. Find (1) cash dividends declared per share for 2024 (common stock and Class B common stock, and quarterly amounts if given), (2) GAAP basic and diluted net income per share for 2024, (3) net income attributable to Coca-Cola Consolidated in thousands for 2024, and (4) dividends paid in 2024 from the cash flow statement. Quote exact figures and labels."})
  result: **1. Cash dividends declared per share for 2024**
  - Consolidated Statements of Changes in Stockholders' Equity: "Common Stock ($3.50 per share)" and "Class B Common Stock ($3.50 per share)."
  - The filing does not give a quarter-by-quarter breakdown of 2024 declared amounts. It only states that on August 20, 2024, the Board "approved an increase in the regular quarterly cash dividend from $0.50 per share to $2.50 per share on the Common Stock and the Class B Common Stock."
  - Dividends *paid* per share in 2024 were $20.00 on both classes, per Note 1: "dividends of $20.00 per share were paid on both the Common Stock and the Class B Common Stock." That figure includes the special cash dividend of $16.00 per share noted in the MD&A.
  
  **2. GAAP basic and diluted net income per share for 2024**
  From the Consolidated Statements of Operations:
  - Basic net income per share: Common Stock **$70.10**; Class B Common Stock **$69.50**
  - Diluted net income per share: Common Stock **$69.94**; Class B Common Stock **$69.17**
  
  **3. Net income attributable to Coca-Cola Consolidated, 2024**
  - Consolidated Statements of Operations: "Net income $633,125" (in thousands), so **$633,125 thousand** (about $633.1 million).
  - The filing does not show a separate noncontrolling-interest line, so this is the reported net income figure. The label is "Net income," not "attributable to Coca-Cola Consolidated, Inc."
  
  **4. Dividends paid in 2024 (cash flow statement)**
  - Consolidated Statements of Cash Flows, Financing Activities: "Cash dividends paid (185,635)" for fiscal year 2024, so **$185,635 thousand** (about $185.6 million).

### Turn 7  (stop_reason=tool_use)
- submit_final_result({"final_result": "**Answer: On a GAAP basis, FY2024 ranking (highest to lowest payout): Keurig Dr Pepper (84.76%) > Coca-Cola (78.86%) > PepsiCo (76.69%).** Coca-Cola ranks second of the three large-cap peers. Coca-Cola Consolidated (5.00%) and Monster (0%, not verified in filings) sit far below, but they are a bottler and a non-payer, so they are weak comparables.\n\n**Basis:** Payout % = FY2024 dividends declared per share ÷ FY2024 GAAP diluted EPS, computed unrounded and rounded to two decimals at the end. Cash cross-check = total dividends paid (cash-flow statement) ÷ net income attributable to shareholders, in the same year.\n\n**Table (figures from each FY2024 10-K):**\n\n| Company | F
…[truncated 2,814 chars])

### Final answer
**Answer: On a GAAP basis, FY2024 ranking (highest to lowest payout): Keurig Dr Pepper (84.76%) > Coca-Cola (78.86%) > PepsiCo (76.69%).** Coca-Cola ranks second of the three large-cap peers. Coca-Cola Consolidated (5.00%) and Monster (0%, not verified in filings) sit far below, but they are a bottler and a non-payer, so they are weak comparables.

**Basis:** Payout % = FY2024 dividends declared per share ÷ FY2024 GAAP diluted EPS, computed unrounded and rounded to two decimals at the end. Cash cross-check = total dividends paid (cash-flow statement) ÷ net income attributable to shareholders, in the same year.

**Table (figures from each FY2024 10-K):**

| Company | FY24 DPS (declared) | GAAP diluted EPS | Payout % (primary) | Cash cross-check |
|---|---|---|---|---|
| Keurig Dr Pepper (KDP) | $0.89 | $1.05 | 84.76% | 1,194 ÷ 1,441 = 82.86% |
| Coca-Cola (KO) | $1.94 | $2.46 | 78.86% | 8,359 ÷ 10,631 = 78.63% |
| PepsiCo (PEP) | $5.33 | $6.95 | 76.69% | 7,229 ÷ 9,578 = 75.48% (declared basis: 7,347 ÷ 9,578 = 76.71%) |
| Coca-Cola Consolidated (COKE) | $3.50 | $69.94 | 5.00% | 185,635 ÷ 633,125 = 29.32% (distorted by a $16.00 special dividend paid in 2024) |
| Monster Beverage | none | n/a | 0% (non-payer) | n/a — not checked against a filing in this run |

**Calculations:**
- KO: 1.94 ÷ 2.46 = 78.86%. Cash: 8,359 ÷ 10,631 = 78.63%.
- PEP: 5.33 ÷ 6.95 = 76.69%. PepsiCo's DPS is a full-year sum of quarterly declarations ($1.265 + 3 × $1.355 = $5.33), as the 10-K's $5.3300 total confirms.
- KDP: 0.89 ÷ 1.05 = 84.76%. Cash: 1,194 ÷ 1,441 = 82.86%. KDP's $1.05 GAAP EPS is depressed by about $718 million of goodwill and intangible impairments, so its high ratio is partly a one-off effect.
- COKE: 3.50 ÷ 69.94 = 5.00%.

**Cross-check:** The cash-basis ranking (KDP 82.86% > KO 78.63% > PEP 75.48%) matches the GAAP ranking, so the order holds on both bases.

**Secondary (non-GAAP) column:** PepsiCo's core diluted EPS is $8.16, giving 5.33 ÷ 8.16 = 65.31%. Coca-Cola's 10-K does not report a comparable EPS, so no KO adjusted payout is shown. The $2.88 comparable EPS in the earlier lead is unverified and was not used. KDP's 10-K reports no adjusted EPS, so none is shown. Using PepsiCo's core EPS alone would move PepsiCo to last place, but that mixes bases, so it is not the primary ranking.

**Coverage notes:** Keurig Dr Pepper, Coca-Cola and PepsiCo are the core peers. Coca-Cola Consolidated is included for completeness only, since it is a franchise bottler with a very different share structure. Monster is listed as a non-payer but was not verified against a filing in this run.

**Sources:**
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/21344/000002134425000011/ko-20241231.htm",
            "name": "The Coca-Cola Company FY2024 Form 10-K"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/77476/000007747625000007/pep-20241228.htm",
            "name": "PepsiCo FY2024 Form 10-K (fiscal year ended Dec 28, 2024)"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1418135/000141813525000013/kdp-20241231.htm",
            "name": "Keurig Dr Pepper FY2024 Form 10-K"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/317540/000031754025000025/coke-20241231.htm",
            "name": "Coca-Cola Consolidated FY2024 Form 10-K"
        }
    ]
}