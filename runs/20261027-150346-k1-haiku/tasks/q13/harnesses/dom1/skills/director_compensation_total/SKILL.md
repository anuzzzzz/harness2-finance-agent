---
name: director_compensation_total
description: Total the compensation paid to a company's non-employee directors for a fiscal year from the proxy statement's Director Compensation table, with the right proxy year and a cross-check.
---
ANALYTIC MOVE: retrieve and sum. Input: the Director Compensation table for the fiscal year asked. Result: the sum of the "Total" column across directors, with a per-director list.

1. Right proxy. The table for fiscal year N is in the DEF 14A filed AFTER year N ended (the "N+1 proxy"). The proxy filed during year N covers year N-1, so do not use it. A company that files its 10-K late can also file its proxy late, so check the table's own title ("Director Compensation for 2023") and the filing date. Find the proxy with edgar_search (form DEF 14A) and confirm the period in the retrieved text.
2. Retrieve each director's name, fees earned or paid in cash, stock awards, option awards, other compensation and total. Ask for the table's footnotes too, which cover grant counts, the grant-date fair value basis and the committee or chair fees.
3. Scope. The table covers non-employee directors only. An executive director such as the CEO is shown in the Summary Compensation Table instead. Say so, and do not add executive pay unless the question asks for it. Include every row in the table, including directors who left during the year. Note any such directors.
4. Cross-check. Add the Total column. Separately add the cash column and each other component column, and confirm that the parts equal the sum of the totals. Check that the units are dollars, not thousands. Keep every figure unrounded.
5. Answer contract: the total in dollars for the named fiscal year; the per-director table with components; the cash plus stock split; the exclusions (employee directors) stated; sources limited to the proxy documents actually opened, with no citation markup.

Task fact (3D Systems, FY2023; verified in an earlier run, so re-confirm in the text). The FY2023 table is in the 2024 proxy: https://www.sec.gov/Archives/edgar/data/910638/000119312524199863/d914592ddef14a.htm. It lists 9 non-employee directors, each with a $150,000 stock award (18,094 shares at $8.29). Cash fees total $913,113, and the Total column sums to $2,263,113. The CEO, Dr. Graves, is excluded as an employee. The proxy filed in 2023 (000119312523091651) covers FY2022 and is the wrong one.
