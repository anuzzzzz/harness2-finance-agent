## Rollout `dom1`
- outcome: submitted
- turns: 7; cost: $0.019; submitted: True

### Turn 1  (stop_reason=tool_use)
- load_skill({"name": "guidance_implied_gross_profit"})
  result: ---
  name: guidance_implied_gross_profit
  description: Compare reported gross profit (non-GAAP or GAAP) with the dollar gross profit implied by prior-quarter guidance (revenue midpoint x guided gross margin), for several quarters, with an average.
  ---
  ANALYTIC MOVE: compare, repeated per quarter, then average. Inputs per quarter: (a) revenue guidance and gross margin guidance for quarter N, from the earnings release for quarter N-1 (its "Current Outlook" section); (b) the actual non-GAAP gross profit for quarter N, from the reconciliation table in the release for quarter N. Result: implied guide $, actual $, difference $, difference %, BEAT or MISS.
  
  1. Window. Take "the last 4 quarters" as the four most recent quarters reported on or before the as-of date (April 07, 2025). Check the date of the latest results release you can open. A quarter reported after the as-of date is excluded; say so. In this task (AMD) the window should be the four quarters of fiscal 2024. The Q4 2024 results release is dated about Feb 4, 2025. The Q1 2025 release falls after the as-of date.
  2. Guidance document. Quarter N's guide is in the release that reported quarter N-1, so the Q1 2024 guide is in the Q4 2023 release. Open each guidance release and retrieve three items: the revenue midpoint (for example "approximately $X B, plus or minus $300M"), the non-GAAP gross margin percentage and the basis (non-GAAP, not GAAP). Quote the margin exactly as printed. AMD guides in half-point steps (for example 53.5%), so never round it to a whole percent or reuse the previous quarter's margin. Write down the exact sentence retrieved for each quarter.
  3. Actual document. Open the release for quarter N. Retrieve the non-GAAP gross profit in dollars (millions) from the "Reconciliation of GAAP to Non-GAAP Fina
  …[truncated 2,834 chars]

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/2488/000000248824000009/q42023991final.htm", "key": "q4_2023"})
  result: SUCCESS: The result has been saved to the data storage under the key: q4_2023. (30,655 characters)
  The data_storage currently contains the following keys:
  q4_2023
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/2488/000000248824000054/q12024991.htm", "key": "q1_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: q1_2024. (27,089 characters)
  The data_storage currently contains the following keys:
  q4_2023
  q1_2024
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/q22024991.htm", "key": "q2_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: q2_2024. (28,510 characters)
  The data_storage currently contains the following keys:
  q4_2023
  q1_2024
  q2_2024
  
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/2488/000000248824000161/q32024991.htm", "key": "q3_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: q3_2024. (28,911 characters)
  The data_storage currently contains the following keys:
  q4_2023
  q1_2024
  q2_2024
  q3_2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this AMD release, quote the 'Current Outlook' section exactly: the revenue guidance for the next quarter (approximately $X billion plus or minus $Y) and the non-GAAP gross margin guidance percentage (quote exactly as printed, and state the basis). Document: {{q4_2023}}"})
  result: **Revenue guidance (first quarter 2024):** "For the first quarter of 2024, AMD expects revenue to be approximately $5.4 billion, plus or minus $300 million."
  
  **Non-GAAP gross margin guidance:** "Non-GAAP gross margin is expected to be approximately 52%."
  
  **Basis:** The 52% figure is a non-GAAP outlook, so it excludes certain items from GAAP gross margin. The release says adjustments to arrive at the GAAP gross margin outlook "typically include stock-based compensation, amortization of acquired intangible assets and acquisition-related and other costs." It also states that AMD cannot reconcile this outlook to a GAAP equivalent because the timing and impact of those adjustments are uncertain, so a reconciliation "is not practicable at this time." The guidance is based on expectations as of January 30, 2024.
- retrieve_information({"prompt": "From this AMD release, quote the 'Current Outlook' section exactly: the revenue guidance for the next quarter (approximately $X billion plus or minus $Y) and the non-GAAP gross margin guidance percentage (quote exactly as printed, and state the basis). Document: {{q1_2024}}"})
  result: **Current Outlook (quoted exactly):**
  
  > "For the second quarter of 2024, AMD expects revenue to be approximately $5.7 billion, plus or minus $300 million. At the mid-point of the revenue range, this represents year-over-year growth of approximately 6% and sequential growth of approximately 4%. Non-GAAP gross margin is expected to be approximately 53%."
  
  - **Revenue guidance:** approximately $5.7 billion, plus or minus $300 million (X = 5.7, Y = 0.3 billion), for Q2 2024.
  - **Non-GAAP gross margin guidance:** approximately 53%.
  
  **Basis of the gross margin figure:** It is a forward-looking non-GAAP measure based on expectations as of April 30, 2024. The release says the GAAP adjustments would typically include stock-based compensation, amortization of acquired intangibles, and acquisition-related costs. Because the timing and amounts of these items are uncertain, AMD states that a reconciliation to GAAP gross margin guidance is not practicable.
- retrieve_information({"prompt": "From this AMD release, quote the 'Current Outlook' section exactly: the revenue guidance for the next quarter (approximately $X billion plus or minus $Y) and the non-GAAP gross margin guidance percentage (quote exactly as printed, and state the basis). Document: {{q2_2024}}"})
  result: **Current Outlook (quoted exactly from the release):**
  
  "For the third quarter of 2024, AMD expects revenue to be approximately $6.7 billion, plus or minus $300 million. At the mid-point of the revenue range, this represents year-over-year growth of approximately 16% and sequential growth of approximately 15%. Non-GAAP gross margin is expected to be approximately 53.5%."
  
  - **Revenue guidance:** approximately $6.7 billion, plus or minus $300 million (X = 6.7, Y = 0.3).
  - **Non-GAAP gross margin guidance:** "approximately 53.5%," printed as shown.
  
  **Basis:** The margin sentence has no separate period label. It follows the third-quarter 2024 revenue sentence in the same paragraph, so it is presented as Q3 2024 guidance. The release's cautionary language also says the forward-looking non-GAAP gross margin is based on AMD's expectations as of July 30, 2024. Because the timing and amounts of the GAAP adjustments depend on future events, the release says a reconciliation to the equivalent GAAP measure is not practicable. The release notes that these adjustments typically include stock-based compensation, amortization of acquired intangibles, and acquisition-related costs.
- retrieve_information({"prompt": "From this AMD release, quote the 'Current Outlook' section exactly: the revenue guidance for the next quarter (approximately $X billion plus or minus $Y) and the non-GAAP gross margin guidance percentage (quote exactly as printed, and state the basis). Document: {{q3_2024}}"})
  result: **Revenue guidance (Q4 2024):**
  > "For the fourth quarter of 2024, AMD expects revenue to be approximately $7.5 billion, plus or minus $300 million."
  
  So the guidance is approximately $7.5 billion, plus or minus $300 million.
  
  **Non-GAAP gross margin guidance:**
  > "Non-GAAP gross margin is expected to be approximately 54%."
  
  **Basis:** The 54% is for the fourth quarter of 2024, the same period as the revenue guidance. It is a non-GAAP figure, so it excludes items AMD adjusts for in its non-GAAP presentation. The release says adjustments to arrive at GAAP gross margin "typically include stock-based compensation, amortization of acquired intangible assets and acquisition-related and other costs," and that a reconciliation to the equivalent GAAP measure is not practicable at this time. The outlook is based on expectations as of October 29, 2024.

### Turn 4  (stop_reason=tool_use)
- edgar_search({"search_query": "AMD fourth quarter 2024 financial results non-GAAP gross profit", "ciks": ["0000002488"], "start_date": "2025-01-28", "end_date": "2025-02-15", "form_types": ["8-K"]})
  result: {"total_matching_documents": 2, "page": 1, "results": [{"form": "8-K", "file_date": "2025-02-04", "period_ending": "2025-02-04", "company": "ADVANCED MICRO DEVICES INC  (AMD)  (CIK 0000002488)", "ciks": ["0000002488"], "accession": "0000002488-25-000009", "document": "q42024991.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/2488/000000248825000009/q42024991.htm"}, {"form": "8-K", "file_date": "2025-02-04", "period_ending": "2025-02-04", "company": "ADVANCED MICRO DEVICES INC  (AMD)  (CIK 0000002488)", "ciks": ["0000002488"], "accession": "0000002488-25-000009", "document": "amdq424earningsslidesfin.htm", "description": "EX-99.2", "url": "https://www.sec.gov/Archives/edgar/data/2488/000000248825000009/amdq424earningsslidesfin.htm"}]}
- retrieve_information({"prompt": "From the reconciliation table 'Reconciliation of GAAP to Non-GAAP Financial Measures' in this AMD release, give the current-quarter (first quarter 2024, three months ended March 30, 2024) GAAP gross profit, non-GAAP adjustments to gross profit, and non-GAAP gross profit in $ millions, and total net revenue and non-GAAP gross margin percentage for the quarter. Document: {{q1_2024}}"})
  result: For the first quarter of 2024 (three months ended March 30, 2024), AMD reported:
  
  | Item | Amount ($ millions) |
  |---|---|
  | GAAP gross profit | $2,560 |
  | Stock-based compensation | 6 |
  | Amortization of acquisition-related intangibles | 230 |
  | Acquisition-related and other costs | — |
  | Inventory loss at contract manufacturer | 65 |
  | **Total non-GAAP adjustments** | **$301** |
  | Non-GAAP gross profit | $2,861 |
  
  - **Total net revenue:** $5,473 million
  - **Non-GAAP gross margin:** 52%
- retrieve_information({"prompt": "From the reconciliation table 'Reconciliation of GAAP to Non-GAAP Financial Measures' in this AMD release, give the current-quarter (second quarter 2024, three months ended June 29, 2024) GAAP gross profit, non-GAAP adjustments to gross profit, and non-GAAP gross profit in $ millions, and total net revenue and non-GAAP gross margin percentage for the quarter. Document: {{q2_2024}}"})
  result: **Second quarter 2024 (three months ended June 29, 2024), in $ millions:**
  
  - **GAAP gross profit:** $2,864
  - **Non-GAAP adjustments to gross profit:** $237 total
    - Stock-based compensation: $5
    - Amortization of acquisition-related intangibles: $231
    - Acquisition-related and other costs: $1
    - Inventory loss at contract manufacturer: $0 (shown as "—")
  - **Non-GAAP gross profit:** $3,101
  - **Total net revenue:** $5,835
  - **Non-GAAP gross margin:** 53%
  
  The adjustments reconcile: $2,864 + $237 = $3,101. The 53% margin matches $3,101 ÷ $5,835 ≈ 53.1%.
- retrieve_information({"prompt": "From the reconciliation table 'Reconciliation of GAAP to Non-GAAP Financial Measures' in this AMD release, give the current-quarter (third quarter 2024, three months ended September 28, 2024) GAAP gross profit, non-GAAP adjustments to gross profit, and non-GAAP gross profit in $ millions, and total net revenue and non-GAAP gross margin percentage for the quarter. Document: {{q3_2024}}"})
  result: **Third quarter 2024 (three months ended September 28, 2024), in $ millions:**
  
  - **GAAP gross profit:** $3,419
  - **Non-GAAP adjustments to gross profit:** $238 total
    - Stock-based compensation: $5
    - Amortization of acquisition-related intangibles: $233
    - Acquisition-related and other costs: $0 (shown as "—")
  - **Non-GAAP gross profit:** $3,657
  - **Total net revenue:** $6,819
  - **Non-GAAP gross margin:** 54%
  
  The adjustments reconcile: $3,419 + $5 + $233 = $3,657. The 54% margin is $3,657 ÷ $6,819 ≈ 53.6%, which the release rounds to 54%.

### Turn 5  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/2488/000000248825000009/q42024991.htm", "key": "q4_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: q4_2024. (32,083 characters)
  The data_storage currently contains the following keys:
  q4_2023
  q1_2024
  q2_2024
  q3_2024
  q4_2024
  

### Turn 6  (stop_reason=tool_use)
- retrieve_information({"prompt": "From the reconciliation table 'Reconciliation of GAAP to Non-GAAP Financial Measures' in this AMD release, give the current-quarter (fourth quarter 2024, three months ended December 28, 2024) GAAP gross profit, non-GAAP adjustments to gross profit, and non-GAAP gross profit in $ millions, and total net revenue and non-GAAP gross margin percentage for the quarter. Document: {{q4_2024}}"})
  result: **Q4 2024 (three months ended December 28, 2024), in $ millions:**
  
  - **GAAP gross profit:** $3,882
  - **Non-GAAP adjustments to gross profit:** $258 total
    - Stock-based compensation: $6
    - Amortization of acquisition-related intangibles: $252
    - Acquisition-related and other costs: $0 (shown as "—")
  - **Non-GAAP gross profit:** $4,140
  - **Total net revenue:** $7,658
  - **Non-GAAP gross margin:** 54%
  
  The adjustments reconcile: $3,882 + $258 = $4,140. Non-GAAP gross margin checks out as $4,140 / $7,658 ≈ 54.1%.

### Turn 7  (stop_reason=tool_use)
- submit_final_result({"final_result": "AMD non-GAAP gross profit vs. guidance-implied gross profit, fiscal 2024 (last four quarters reported before April 7, 2025)\n\nQ1 - $53 million (1.9 % BEAT)\nQ2 - $80 million (2.6 % BEAT)\nQ3 - $73 million (2.0 % BEAT)\nQ4 - $90 million (2.2 % BEAT)\nAverage - 2.2 % BEAT\n\nWorking (unrounded, $ millions):\n\nQ1 2024 (guide in Q4 2023 release, dated ~Jan 30, 2024)\n- Guidance text: revenue \"approximately $5.4 billion, plus or minus $300 million\"; \"Non-GAAP gross margin is expected to be approximately 52%.\"\n- Implied GP = 5,400 x 52% = 2,808.0\n- Actual non-GAAP GP (Q1 2024 release, reconciliation, current quarter) = 2,861 (GAAP GP 2,560 + adjustments 301); revenue 5,47
…[truncated 3,057 chars])

### Final answer
AMD non-GAAP gross profit vs. guidance-implied gross profit, fiscal 2024 (last four quarters reported before April 7, 2025)

Q1 - $53 million (1.9 % BEAT)
Q2 - $80 million (2.6 % BEAT)
Q3 - $73 million (2.0 % BEAT)
Q4 - $90 million (2.2 % BEAT)
Average - 2.2 % BEAT

Working (unrounded, $ millions):

Q1 2024 (guide in Q4 2023 release, dated ~Jan 30, 2024)
- Guidance text: revenue "approximately $5.4 billion, plus or minus $300 million"; "Non-GAAP gross margin is expected to be approximately 52%."
- Implied GP = 5,400 x 52% = 2,808.0
- Actual non-GAAP GP (Q1 2024 release, reconciliation, current quarter) = 2,861 (GAAP GP 2,560 + adjustments 301); revenue 5,473; margin 52%
- Difference = 53.0; % = 53 / 2,808 = 1.8875% BEAT

Q2 2024 (guide in Q1 2024 release, dated ~Apr 30, 2024)
- Guidance text: "approximately $5.7 billion, plus or minus $300 million" and "Non-GAAP gross margin is expected to be approximately 53%."
- Implied GP = 5,700 x 53% = 3,021.0
- Actual non-GAAP GP (Q2 2024 release) = 3,101 (GAAP GP 2,864 + adjustments 237); revenue 5,835; margin 53%
- Difference = 80.0; % = 80 / 3,021 = 2.6481% BEAT

Q3 2024 (guide in Q2 2024 release, dated ~Jul 30, 2024)
- Guidance text: "approximately $6.7 billion, plus or minus $300 million" and "Non-GAAP gross margin is expected to be approximately 53.5%."
- Implied GP = 6,700 x 53.5% = 3,584.5
- Actual non-GAAP GP (Q3 2024 release) = 3,657 (GAAP GP 3,419 + adjustments 238); revenue 6,819; margin 54%
- Difference = 72.5; % = 72.5 / 3,584.5 = 2.0228% BEAT

Q4 2024 (guide in Q3 2024 release, dated ~Oct 29, 2024)
- Guidance text: "approximately $7.5 billion, plus or minus $300 million" and "Non-GAAP gross margin is expected to be approximately 54%."
- Implied GP = 7,500 x 54% = 4,050.0
- Actual non-GAAP GP (Q4 2024 release, dated Feb 4, 2025) = 4,140 (GAAP GP 3,882 + adjustments 258); revenue 7,658; margin 54%
- Difference = 90.0; % = 90 / 4,050 = 2.2222% BEAT

Average of the four percentages = (1.8875 + 2.6481 + 2.0228 + 2.2222) / 4 = 2.1951% BEAT (about 2.2%). Average dollar beat = 295.5 / 4 = $73.9 million.

Notes: The Q1 2025 quarter was reported in May 2025, after the as-of date, so it is excluded. Guided margins were read from the text of the prior-quarter releases, not assumed. All actuals are non-GAAP gross profit from the current-quarter column of each release's reconciliation table; the GAAP-to-non-GAAP adjustments reconcile to the printed totals.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/2488/000000248824000009/q42023991final.htm",
            "name": "AMD Q4 2023 results release (8-K EX-99.1), source of Q1 2024 guidance"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/2488/000000248824000054/q12024991.htm",
            "name": "AMD Q1 2024 results release (8-K EX-99.1), source of Q2 2024 guidance and Q1 2024 actuals"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/q22024991.htm",
            "name": "AMD Q2 2024 results release (8-K EX-99.1), source of Q3 2024 guidance and Q2 2024 actuals"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/2488/000000248824000161/q32024991.htm",
            "name": "AMD Q3 2024 results release (8-K EX-99.1), source of Q4 2024 guidance and Q3 2024 actuals"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/2488/000000248825000009/q42024991.htm",
            "name": "AMD Q4 2024 results release (8-K EX-99.1, Feb 4, 2025), source of Q4 2024 actuals"
        }
    ]
}