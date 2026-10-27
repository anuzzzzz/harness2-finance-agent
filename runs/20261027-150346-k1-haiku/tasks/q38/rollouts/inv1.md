## Rollout `inv1`
- outcome: submitted
- turns: 4; cost: $0.006; submitted: True

### Turn 1  (stop_reason=tool_use)
- edgar_search({"search_query": "Lyft fourth quarter 2024 results Adjusted EBITDA Gross Bookings", "ciks": ["1759509"], "start_date": "2025-02-01", "end_date": "2025-02-28"})
  result: {"total_matching_documents": 2, "page": 1, "results": [{"form": "8-K", "file_date": "2025-02-11", "period_ending": "2025-02-11", "company": "Lyft, Inc.  (LYFT)  (CIK 0001759509)", "ciks": ["0001759509"], "accession": "0001759509-25-000009", "document": "lyft-2024x12x31pressreleas.htm", "description": "EX-99.1", "url": "https://www.sec.gov/Archives/edgar/data/1759509/000175950925000009/lyft-2024x12x31pressreleas.htm"}, {"form": "10-K", "file_date": "2025-02-14", "period_ending": "2024-12-31", "company": "Lyft, Inc.  (LYFT)  (CIK 0001759509)", "ciks": ["0001759509"], "accession": "0001759509-25-000025", "document": "lyft-20241231.htm", "description": "10-K", "url": "https://www.sec.gov/Archives/edgar/data/1759509/000175950925000025/lyft-20241231.htm"}]}
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1759509/000175950924000121/lyft-20240930xpressrelease.htm", "key": "q3_release"})
  result: SUCCESS: The result has been saved to the data storage under the key: q3_release. (26,102 characters)
  The data_storage currently contains the following keys:
  q3_release
  

### Turn 2  (stop_reason=tool_use)
- parse_html_page({"url": "https://www.sec.gov/Archives/edgar/data/1759509/000175950925000009/lyft-2024x12x31pressreleas.htm", "key": "q4_release"})
  result: SUCCESS: The result has been saved to the data storage under the key: q4_release. (31,245 characters)
  The data_storage currently contains the following keys:
  q3_release
  q4_release
  
- retrieve_information({"prompt": "From this Lyft Q3 2024 earnings release, quote the Q4 2024 outlook: Gross Bookings range, Adjusted EBITDA range, and any Adjusted EBITDA margin guidance. Text: {{q3_release}}"})
  result: Here is the Q4 2024 outlook from the release, under "Fourth Quarter 2024 Outlook":
  
  - **Gross Bookings:** "approximately $4.28 billion to $4.35 billion, up 15% to 17% year-over-year"
  - **Adjusted EBITDA:** "$100 million to $105 million"
  - **Adjusted EBITDA margin:** "(calculated as a percentage of Gross Bookings) of approximately 2.3% to 2.4%"

### Turn 3  (stop_reason=tool_use)
- retrieve_information({"prompt": "From this Lyft Q4 2024 earnings release, give the exact figures for: fourth quarter 2024 Gross Bookings (in $ thousands or millions), fourth quarter 2024 Adjusted EBITDA, the stated Adjusted EBITDA margin for Q4 2024 as a percentage of Gross Bookings, and the full-year 2024 figures. Also state whether Adjusted EBITDA is a non-GAAP measure and how it is defined. Text: {{q4_release}}"})
  result: **Fourth quarter 2024 (three months ended December 31, 2024)**
  - **Gross Bookings:** $4,278.9 million (about $4.3 billion, or $4,278,900 thousand), up 15% year over year.
  - **Adjusted EBITDA:** $112.8 million, compared with $66.6 million in Q4 2023.
  - **Adjusted EBITDA margin (as a percentage of Gross Bookings):** 2.6%, compared with 1.8% in Q4 2023. The release's figure checks out: $112.8M ÷ $4,278.9M ≈ 2.64%.
  
  **Full year 2024 (year ended December 31, 2024)**
  - **Gross Bookings:** $16,099.4 million (about $16.1 billion), up 17% year over year.
  - **Adjusted EBITDA:** $382.4 million, compared with $222.4 million in 2023.
  - **Adjusted EBITDA margin (as a percentage of Gross Bookings):** 2.4%, compared with 1.6% in 2023. Checking: $382.4M ÷ $16,099.4M ≈ 2.38%.
  
  **Non-GAAP status and definition**
  Yes, Adjusted EBITDA is a non-GAAP financial measure. Lyft defines it as net income (loss) adjusted for:
  - interest expense
  - other income (expense), net
  - provision for (benefit from) income taxes
  - depreciation and amortization
  - stock-based compensation expense
  - payroll tax expense related to stock-based compensation
  - sublease income
  - gain from lease termination
  - restructuring charges and costs related to acquisitions and divestitures, if applicable
  
  Adjusted EBITDA margin is Adjusted EBITDA divided by Gross Bookings for the same period. The release presents it as a key metric, and it is also a non-GAAP measure.

### Turn 4  (stop_reason=tool_use)
- submit_final_result({"final_result": "Result: BEAT. Lyft's Q4'24 Adjusted EBITDA margin came in about 28.62 bps above the midpoint of the guidance it gave in Q3'24 (2.64% actual vs. 2.35% guided midpoint).\n\nGuidance (Q3'24 earnings release, 8-K EX-99.1, filed in Q3 2024): The \"Fourth Quarter 2024 Outlook\" gave Gross Bookings of approximately $4.28 billion to $4.35 billion, Adjusted EBITDA of $100 million to $105 million, and Adjusted EBITDA margin (as a percentage of Gross Bookings) of approximately 2.3% to 2.4%.\n- Stated margin range midpoint: (2.3% + 2.4%) / 2 = 2.35%.\n- Cross-check using dollar midpoints: $102.5M / $4,315M = 2.3754%.\n\nActual (Q4'24 earnings release, 8-K EX-99.1, filed 2025-02-11, ope
…[truncated 1,522 chars])

### Final answer
Result: BEAT. Lyft's Q4'24 Adjusted EBITDA margin came in about 28.62 bps above the midpoint of the guidance it gave in Q3'24 (2.64% actual vs. 2.35% guided midpoint).

Guidance (Q3'24 earnings release, 8-K EX-99.1, filed in Q3 2024): The "Fourth Quarter 2024 Outlook" gave Gross Bookings of approximately $4.28 billion to $4.35 billion, Adjusted EBITDA of $100 million to $105 million, and Adjusted EBITDA margin (as a percentage of Gross Bookings) of approximately 2.3% to 2.4%.
- Stated margin range midpoint: (2.3% + 2.4%) / 2 = 2.35%.
- Cross-check using dollar midpoints: $102.5M / $4,315M = 2.3754%.

Actual (Q4'24 earnings release, 8-K EX-99.1, filed 2025-02-11, opened and read directly):
- Q4'24 Gross Bookings: $4,278.9 million.
- Q4'24 Adjusted EBITDA: $112.8 million.
- Stated Q4'24 Adjusted EBITDA margin: 2.6%. Computed: $112.8M / $4,278.9M = 2.636193%.
- Both are non-GAAP measures on the same definition used in the guidance (Adjusted EBITDA divided by Gross Bookings for the same period).

Calculation (headline, vs. the stated 2.35% midpoint):
2.636193% - 2.35% = 0.286193 percentage points = +28.62 bps.

Alternate bases:
- Using dollar-midpoint guidance (2.3754%): 2.636193% - 2.375435% = +26.08 bps.
- Using the company's rounded 2.6% actual: 2.6% - 2.35% = +25 bps.

Conclusion: Q4'24 Adjusted EBITDA margin beat the Q3'24 guidance midpoint by about 28.62 bps on the headline basis (range of roughly 25 to 28.6 bps across bases). Both actuals were above the top of the guided 2.3%-2.4% range. Note the earlier-run figures from the FY2024 10-K minus 9M were not needed, since the Q4 release was opened directly and states the figures.

Sources:
{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1759509/000175950924000121/lyft-20240930xpressrelease.htm",
            "name": "Lyft Q3 2024 earnings release (8-K EX-99.1) - Q4 2024 outlook"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/1759509/000175950925000009/lyft-2024x12x31pressreleas.htm",
            "name": "Lyft Q4 and FY 2024 earnings release (8-K EX-99.1, filed 2025-02-11)"
        }
    ]
}