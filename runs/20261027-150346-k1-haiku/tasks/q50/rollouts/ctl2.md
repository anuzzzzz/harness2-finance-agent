## Rollout `ctl2`
- outcome: submitted
- turns: 1; cost: $0.046; submitted: True

### Turn 1  (stop_reason=tool_use)
- web_search(query="AMD fourth quarter 2024 financial results outlook non-GAAP gross margin") → 9 results: ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000161/q32024991.htm>; ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000009/q42023991final.htm>; ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/q22024991.htm>; ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000054/q12024991.htm>; AMD Reports Record Fourth Quarter and Full Year 2024 Financial Results <https://www.nasdaq.com/articles/amd-reports-record-fourth-quarter-and-full-year-2024-financial-results>
- web_search(query="AMD third quarter 2024 financial results non-GAAP gross margin outlook") → 9 results: ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000161/q32024991.htm>; ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/q22024991.htm>; ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000009/q42023991final.htm>; ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/amdq224earningsslides.htm>; AMD Reports Third Quarter 2024 Financial Results :: Advanced Micro Devices, Inc. (AMD) <https://ir.amd.com/news-events/press-releases/detail/1224/amd-reports-third-quarter-2024-financial-results>
- web_search(query="AMD second quarter 2024 financial results non-GAAP gross margin outlook") → 10 results: ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000054/q12024991.htm>; ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/q22024991.htm>; ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/amdq224earningsslides.htm>; ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000054/amdq124earningsslides.htm>; ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000161/q32024991.htm>
- web_search(query="AMD first quarter 2024 financial results non-GAAP gross margin outlook") → 10 results: ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000009/q42023991final.htm>; ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000054/q12024991.htm>; ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000054/amdq124earningsslides.htm>; ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000161/q32024991.htm>; ADVANCED MICRO DEVICES INC - Form 8-K - FY2024 <https://www.sec.gov/Archives/edgar/data/2488/000000248824000009/amdq423earningsslides.htm>
- submit_final_result({"final_result": "Method: For each quarter, I used the revenue guidance midpoint and the non-GAAP gross margin guidance from the prior quarter's earnings release to compute implied non-GAAP gross profit (midpoint × margin). I then compared that to the actual non-GAAP gross profit reported for the quarter.\n\nGuidance and actuals by quarter:\n\n- Q1 2024: Guidance (from the Q4 2023 release) was <cite index=\"29-3\">revenue to be approximately $5.4 billion, plus or minus $300 million</cite> and <cite index=\"29-6\">non-GAAP gross margin is expected to be approximately 52%.</cite> Implied gross profit = $5,400M × 52% = $2,808M. Actual non-GAAP gross profit was <cite index=\"34-3\">$2,861</cite>
…[truncated 3,940 chars])

### Final answer
Method: For each quarter, I used the revenue guidance midpoint and the non-GAAP gross margin guidance from the prior quarter's earnings release to compute implied non-GAAP gross profit (midpoint × margin). I then compared that to the actual non-GAAP gross profit reported for the quarter.

Guidance and actuals by quarter:

- Q1 2024: Guidance (from the Q4 2023 release) was <cite index="29-3">revenue to be approximately $5.4 billion, plus or minus $300 million</cite> and <cite index="29-6">non-GAAP gross margin is expected to be approximately 52%.</cite> Implied gross profit = $5,400M × 52% = $2,808M. Actual non-GAAP gross profit was <cite index="34-3">$2,861</cite> million (52% margin). Beat = $53M, or 1.89% (53 / 2,808).

- Q2 2024: Guidance (from the Q1 2024 release) was <cite index="30-3">revenue to be approximately $5.7 billion, plus or minus $300 million</cite> and <cite index="30-5">non-GAAP gross margin is expected to be approximately 53%.</cite> Implied gross profit = $5,700M × 53% = $3,021M. Actual non-GAAP gross profit was <cite index="24-4">$3,101</cite> million (53% margin). Beat = $80M, or 2.65% (80 / 3,021).

- Q3 2024: Guidance (from the Q2 2024 release) was <cite index="3-3">revenue to be approximately $6.7 billion, plus or minus $300 million</cite> and <cite index="3-5">non-GAAP gross margin is expected to be approximately 53.5%.</cite> Implied gross profit = $6,700M × 53.5% = $3,584.5M. Actual non-GAAP gross profit was <cite index="14-3">$3,657</cite> million (54% margin). Beat = $72.5M, or 2.02% (72.5 / 3,584.5).

- Q4 2024: Guidance (from the Q3 2024 release) was <cite index="10-3">revenue to be approximately $7.5 billion, plus or minus $300 million</cite> and <cite index="10-5">non-GAAP gross margin is expected to be approximately 54%.</cite> Implied gross profit = $7,500M × 54% = $4,050M. Actual non-GAAP gross profit was <cite index="7-4">$4,140</cite> million (54% margin). Beat = $90M, or 2.22% (90 / 4,050).

Results (formatted as requested; percentages shown to one decimal as specified, with two-decimal values in the notes):

Q1 - $53 million (1.9 % BEAT)
Q2 - $80 million (2.6 % BEAT)
Q3 - $72.5 million (2.0 % BEAT)
Q4 - $90 million (2.2 % BEAT)

Average beat (simple average of the four percentage beats): (1.89% + 2.65% + 2.02% + 2.22%) / 4 = 2.20% BEAT. Using the one-decimal figures instead gives (1.9 + 2.6 + 2.0 + 2.2) / 4 = 2.18%.

Notes: All four quarters were beats. Every guide was a revenue midpoint with a ±$300M range, and the margin guide was a single point estimate, so the implied gross profit is an approximation. The beats were driven by actual gross margin meeting or exceeding the guided figure combined with revenue above the midpoint. The Q1 2024 figure was reported as 52% non-GAAP gross margin, which matched the guide. Q2 was reported at 53%, matching the guide. Q3 was reported at 54% versus a 53.5% guide. Q4 was reported at 54%, matching the guide.

{
    "sources": [
        {
            "url": "https://www.sec.gov/Archives/edgar/data/2488/000000248824000009/q42023991final.htm",
            "name": "AMD Q4 2023 earnings release (8-K) - Q1 2024 outlook"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/2488/000000248824000054/q12024991.htm",
            "name": "AMD Q1 2024 earnings release (8-K) - Q2 2024 outlook"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/q22024991.htm",
            "name": "AMD Q2 2024 earnings release (8-K) - Q3 2024 outlook"
        },
        {
            "url": "https://www.sec.gov/Archives/edgar/data/2488/000000248824000161/q32024991.htm",
            "name": "AMD Q3 2024 earnings release (8-K) - Q4 2024 outlook and Q3 non-GAAP gross profit"
        },
        {
            "url": "https://www.amd.com/en/newsroom/press-releases/2024-4-30-amd-reports-first-quarter-2024-financial-results.html",
            "name": "AMD Reports First Quarter 2024 Financial Results"
        },
        {
            "url": "https://www.amd.com/en/newsroom/press-releases/2024-7-30-amd-reports-second-quarter-2024-financial-results.html",
            "name": "AMD Reports Second Quarter 2024 Financial Results"
        },
        {
            "url": "https://ir.amd.com/financial-information/sec-filings/content/0000002488-25-000009/0000002488-25-000009.pdf",
            "name": "AMD Reports Fourth Quarter and Full Year 2024 Financial Results (Feb 4, 2025)"
        }
    ]
}