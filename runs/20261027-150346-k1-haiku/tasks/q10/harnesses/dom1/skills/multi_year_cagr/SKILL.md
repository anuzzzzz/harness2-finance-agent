---
name: multi_year_cagr
description: Compute a compound annual growth rate (revenue or another line) between two fiscal years from filed statements, with period count, units and sources checked.
---
ANALYTIC MOVE: calculate. Inputs are the start-year and end-year values of the same line, taken from filed statements. The result is CAGR = (End / Start)^(1 / n) - 1.

1. Period count. n = end fiscal year minus start fiscal year ("2022 to 2024" means n = 2, not 3). Confirm the company's fiscal year end, because a non-calendar fiscal year changes which statement holds each year.
2. Source of each value. Open the latest 10-K, which has three years of income-statement columns. Retrieve the start-year and end-year values from that one statement, so both use the same definitions. If the start year is outside that filing, open the earlier 10-K. If it was restated or recast, prefer the later filing's comparative figure and say so. Use total revenue from the consolidated statements of operations, not a segment or non-GAAP number, unless the question asks for one.
3. Units. Statements are usually in thousands. Keep both values in the same unit. State the unit in the answer.
4. Calculation, with no intermediate rounding. Show the ratio End / Start, the root and the result. Round only the final percentage to two decimals. Also give the total growth over the window (End / Start - 1) as a cross-check. CAGR must lie between 0 and the simple total growth. Taking the square root of the ratio when n = 2 should give the same answer as the formula.
5. Answer contract: the CAGR to two decimals; both values with fiscal year, unit and source document; n; the formula and arithmetic. Sources are limited to documents actually opened.

Task facts (Palantir Technologies, calendar fiscal year; re-confirm in the opened text). FY2023 10-K, https://www.sec.gov/Archives/edgar/data/1321655/000132165524000022/pltr-20231231.htm. Its statement of operations, in thousands, shows revenue of 2,225,012 (2023), 1,905,871 (2022) and 1,541,889 (2021); this was retrieved in an earlier run. FY2024 10-K, https://www.sec.gov/Archives/edgar/data/1321655/000132165525000022/pltr-20241231.htm. The earlier run did NOT open it and used 2,865,507 for FY2024 from outside the filing, so retrieve the FY2024 revenue from this filing's statement of operations (it also carries the 2022 comparative) before using it. If the retrieved values are 2,865,507 and 1,905,871, then CAGR = sqrt(2,865,507 / 1,905,871) - 1 = about 22.62%.
