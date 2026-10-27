## Rollout `ctl2`
- outcome: submitted
- turns: 5; cost: $0.019; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="Delta Air Lines fourth quarter 2024 earnings outlook guidance") → 0 results: 
- edgar_search({"search_query": "Delta Air Lines outlook first quarter 2025 operating margin pre-tax margin EPS guidance", "ciks": ["DAL"], "top_n_results": 5})
  result: {"total_matching_documents": 9, "page": 1, "results": [{"form": "8-K", "file_date": "2025-01-10", "period_ending": "2025-01-10", "company": "DELTA AIR LINES, INC.  (DAL)  (CIK 0000027904)", "ciks": ["0000027904"], "accession": "0001683168-25-000182", "document": "delta_ex9901.htm", "description": "PRESS RELEASE", "url": "https://www.sec.gov/Archives/edgar/data/27904/000168316825000182/delta_ex9901.htm"}, {"form": "10-K", "file_date": "2009-03-02", "period_ending": "2008-12-31", "company": "DELTA AIR LINES INC /DE/  (DAL)  (CIK 0000027904)", "ciks": ["0000027904"], "accession": "0001193125-09-042726", "document": "d10k.htm", "description": "FORM 10-K", "url": "https://www.sec.gov/Archives/edgar/data/27904/000119312509042726/d10k.htm"}, {"form": "10-K", "file_date": "2004-03-12", "period_ending": "2003-12-31", "company": "DELTA AIR LINES INC /DE/  (DAL)  (CIK 0000027904)", "ciks": ["0000027904"], "accession": "0000950144-04-002423", "document": "g87427e10vk.htm", "description": "DELTA AIR LINES, INC.", "url": "https://www.sec.gov/Archives/edgar/data/27904/000095014404002423/g87427e10vk.htm"}, {"form": "S-1/A", "file_date": "2005-02-10", "period_ending": null, "company": "DELTA AIR LINES INC /DE/  (DAL)  (CIK 0000027904)", "ciks": ["0000027904"], "accession": "0000950144-05-001180", "document": "g92354a1sv1za.htm", "description": "DELTA AIR LINES, INC.", "url": "https://www.sec.gov/Archives/edgar/data/27904/000095014405001180/g92354a1sv1za.htm"}, {"form": "S-1", "file_date": "2004-12-21", "period_ending": null, "company": "DELTA AIR LINES INC /DE/  (DAL)  (CIK 0000027904)", "ciks": ["0000027904"], "accession": "0000950144-04-012247", "document": "g92354sv1.htm", "description": "DELTA AIR LINES, INC.", "url": "https://www.sec.gov/Archives/edgar/data/27904/000095014404012247
  …[truncated 18 chars]

### Turn 2  (stop_reason=tool_use)
- web_search(query=null) → 9 results: DELTA AIR LINES, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/27904/000168316824002249/delta_ex9901.htm>; DELTA AIR LINES, INC. - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/27904/000168316824007033/delta_ex9901.htm>; SOUTHWEST AIRLINES CO - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/92380/000009238024000147/luv-20240930.htm>; SOUTHWEST AIRLINES CO - Form 10-Q - FY2024 <https://www.sec.gov/Archives/edgar/data/92380/000009238024000111/luv-20240630.htm>; Delta Air Lines (DAL) 3Q 2024 earnings <https://www.cnbc.com/2024/10/10/delta-air-lines-dal-3q-2024-earnings.html>
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/27904/000168316825000182/delta_ex9901.htm", "key": "dal_q4_2024"})
  result: SUCCESS: The result has been saved to the data storage under the key: dal_q4_2024. (52,998 characters)
  The data_storage currently contains the following keys:
  dal_q4_2024
  

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Delta Air Lines press release, list every financial metric/line item that Delta provides guidance or outlook for in the first quarter 2025 and full year 2025 outlook (e.g., total revenue growth, operating margin, pre-tax margin, EPS, free cash flow, fuel price, capacity, CASM-ex, tax rate, leverage, etc.), with the guided values. Also note if the release describes guidance as on a GAAP or non-GAAP (adjusted) basis. Context: {{dal_q4_2024}}"})
  result: ## Delta's 2025 Guidance (January 10, 2025 release)
  
  | Metric | Period | Guided value | Basis | Source in release |
  |---|---|---|---|---|
  | Earnings per share (EPS) | FY 2025 | Greater than $7.35 | Non-GAAP | Headline, CEO quote, "Financial Guidance" table |
  | EPS growth, YoY | FY 2025 | Greater than 10% (vs. normalized 2024 EPS excluding the 45¢ CrowdStrike impact); greater than 19% on a non-GAAP basis | Non-GAAP (the 19% figure is explicitly labeled) | Financial Guidance table and text |
  | Pre-tax income | FY 2025 | Greater than $6 billion | Not explicitly labeled; presumably non-GAAP | CEO quote only |
  | Free cash flow | FY 2025 | Greater than $4 billion | Non-GAAP (FCF is a non-GAAP measure) | Headline, table, CFO quote |
  | Gross leverage (adjusted debt to EBITDAR) | FY 2025 | 2x or less (footnote: adjusted debt to EBITDAR) | Non-GAAP | Table and CFO quote |
  | Non-fuel unit cost (CASM-Ex) growth | FY 2025 | "Low-single digits" growth (no number) | Non-GAAP | CFO quote |
  | Capacity growth | FY 2025 | "Slower capacity growth" (qualitative only, no number) | N/A | CFO quote |
  | Total revenue growth, YoY | 1Q 2025 | Up 7% to 9% | Adjusted (excludes third-party refinery sales), per text. The table just says "Total Revenue YoY" | Revenue Environment section; table |
  | Operating margin | 1Q 2025 | 6% to 8% | Non-GAAP (covered by footnote 1 on the forecast table) | 1Q25 Forecast table |
  | Earnings per share | 1Q 2025 | $0.70 to $1.00 | Non-GAAP (covered by footnote 1) | Headline, 1Q25 Forecast table |
  
  **Basis of guidance:** The release presents its guidance under the heading "Financial Guidance," with footnote 1 stating "Non-GAAP measures; Refer to Non-GAAP reconciliations for historical comparison figures." The Note A disclosure also says Delta cannot reconcile forward-lo
  …[truncated 1,215 chars]

### Turn 4  (stop_reason=end_turn)
Delta's quarterly earnings releases typically guide on a small set of forward-looking, mostly non-GAAP metrics. The most recent release before April 7, 2025 is the January 10, 2025 Q4 2024 release, which gives these.

**Metrics Delta guides on each quarter (based on the 2024 releases):**
- **Total revenue growth (year over year):** The forecast table lists this line. For Q4 2024, Delta guided to 
Total Revenue YoY Up 2% - 4%
.
- **Operating margin:** Also in the forecast table. For Q4 2024 it was 
11% - 13%
.
- **Earnings per share (adjusted):** For Q4 2024 it was 
$1.60 - $1.85
, and Delta said these are non-GAAP measures.
- **Full-year EPS and free cash flow:** Delta has reiterated annual targets alongside quarterly guidance. In April 2024 it reaffirmed 
2024 outlook for EPS of $6 to $7 and free cash flow of $3 to $4 billion
.

**Latest guidance (January 10, 2025 release, covering Q1 2025 and FY 2025):**
- **Q1 2025 total revenue growth:** Up 7% to 9% year over year, on an adjusted basis that excludes third-party refinery sales. 
The company expects to grow the top line by 7% to 9%, expand margins by 2 points, and nearly double earnings over last year.

- **Q1 2025 operating margin:** 6% to 8% (non-GAAP).
- **Q1 2025 EPS:** 
Adjusted earnings of 70 cents to $1 per share.

- **FY 2025 EPS:** Greater than $7.35 (non-GAAP). 
For the full year, the company expects earnings per share greater than $7.35, increasing more than 20% compared to 2024 as reported.

- **FY 2025 free cas
…[truncated 2,483 chars]

### Turn 5  (stop_reason=tool_use)
- submit_final_result({"final_result": "Delta Air Lines (NYSE: DAL) guides on a small, consistent set of forward-looking metrics in its quarterly earnings releases. The most recent release before April 7, 2025 is the January 10, 2025 Q4 2024 release, which covers Q1 2025 and full-year 2025.\n\n**Metrics guided each quarter (based on the 2024 releases):**\n- **Total revenue growth, year over year:** The forecast table includes this line. For Q4 2024, Delta projected revenue growth of 2% to 4% (Q3 2024 release).\n- **Operating margin:** Also in the forecast table. For Q4 2024, the projection was 11% to 13%, on a non-GAAP basis (Q3 2024 release).\n- **Adjusted earnings per share:** For Q4 2024, the projection was $1
…[truncated 3,121 chars])

### Final answer
Delta Air Lines (NYSE: DAL) guides on a small, consistent set of forward-looking metrics in its quarterly earnings releases. The most recent release before April 7, 2025 is the January 10, 2025 Q4 2024 release, which covers Q1 2025 and full-year 2025.

**Metrics guided each quarter (based on the 2024 releases):**
- **Total revenue growth, year over year:** The forecast table includes this line. For Q4 2024, Delta projected revenue growth of 2% to 4% (Q3 2024 release).
- **Operating margin:** Also in the forecast table. For Q4 2024, the projection was 11% to 13%, on a non-GAAP basis (Q3 2024 release).
- **Adjusted earnings per share:** For Q4 2024, the projection was $1.60 to $1.85, on a non-GAAP basis (Q3 2024 release).
- **Full-year EPS and free cash flow:** Delta has restated its annual targets alongside quarterly guidance. In April 2024 it reaffirmed 2024 EPS of $6 to $7 and free cash flow of $3 to $4 billion (Q1 2024 release).

**Latest guidance (January 10, 2025 release):**
- **Q1 2025 total revenue growth:** 7% to 9% year over year, on an adjusted basis that excludes third-party refinery sales. The CEO framed this as a top-line growth expectation alongside a two-point margin expansion and near-doubling of earnings versus the prior year (Motley Fool transcript).
- **Q1 2025 operating margin:** 6% to 8%, non-GAAP (release forecast table).
- **Q1 2025 adjusted EPS:** $0.70 to $1.00 (release; Zacks/Yahoo Finance coverage matches this range).
- **FY 2025 adjusted EPS:** Greater than $7.35, which Delta said would be more than 20% above 2024 reported EPS (release; CNBC coverage; Motley Fool transcript).
- **FY 2025 free cash flow:** Greater than $4 billion. Delta tied this to further debt reduction and a leverage ratio of 2x or less (CNBC coverage; Motley Fool transcript).
- **FY 2025 gross leverage:** 2x or less, defined as adjusted debt to EBITDAR (release).
- **FY 2025 pre-tax income:** Greater than $6 billion, mentioned by the CEO but not in the forecast table. This is my reading of the release and is not confirmed by the other sources I checked.
- **Qualitative 2025 items:** Non-fuel unit cost (CASM-Ex) growth in the "low-single digits" range and "slower capacity growth," with no numeric ranges (release).

**Basis and limits:**
- Delta's forward guidance is non-GAAP. The release says Delta cannot reconcile forward-looking non-GAAP measures to GAAP without unreasonable effort, so no GAAP reconciliation is given for guided figures.
- Delta does not give numeric guidance for fuel price per gallon, ASM capacity growth, tax rate, net income, capital expenditures, or full-year operating margin. Some of these appear in supplemental materials or are left qualitative.
- Delta's Q1 results have typically been released in mid-April. Q1 2025 results and updated guidance may therefore appear shortly after the April 7, 2025 reference date.

Sources:
- Delta Q4 2024 earnings press release (8-K Ex. 99.1, Jan. 10, 2025): https://www.sec.gov/Archives/edgar/data/27904/000168316825000182/delta_ex9901.htm
- Delta Q3 2024 earnings press release (8-K Ex. 99.1): https://www.sec.gov/Archives/edgar/data/27904/000168316824007033/delta_ex9901.htm
- Delta Q1 2024 earnings press release (8-K Ex. 99.1, Apr. 10, 2024): https://www.sec.gov/Archives/edgar/data/27904/000168316824002249/delta_ex9901.htm
- Delta Q4 2024 earnings call transcript (Motley Fool): https://www.fool.com/earnings/call-transcripts/2025/01/10/delta-air-lines-dal-q4-2024-earnings-call-transcri/
- CNBC, Delta Air Lines 4Q 2024 earnings: https://www.cnbc.com/2025/01/10/delta-air-lines-dal-4q-2024-earnings.html
- Yahoo Finance (Zacks), Delta Air Lines Earnings Surpass Estimates in Q4: https://finance.yahoo.com/news/delta-air-lines-earnings-surpass-174200268.html