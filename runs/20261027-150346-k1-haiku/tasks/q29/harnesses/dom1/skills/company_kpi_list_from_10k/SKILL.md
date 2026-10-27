---
name: company_kpi_list_from_10k
description: Answer "list the operating KPIs / operating statistics the company tracked in FY X, with the FY total" from a 10-K, completely and with units and bases.
---
ANALYTIC MOVE: classify and list. Inputs: the company's own operating-statistics table in the 10-K. Result: every KPI row the company reports, with the FY value, unit and basis.

1. Governing source: the 10-K, Item 7 MD&A. Look for "Operating Statistics", "Comparative Operating Statistics" or "Key Performance Indicators". Item 1 and the risk factors do not hold the KPI table. Use the company's own table, not a list you build from memory or from articles.
2. Completeness: retrieve the whole table in one dedicated retrieve_information call (ask for "every row of the table, in order, with units"). Then check the row count against the table. Ask again for the missing rows if the output is cut off. Do not drop rows because they look like inputs (aircraft count, departures, fuel gallons). They are KPIs if the company tabulates them.
3. Answer contract: a table with the KPI name exactly as printed, the FY value as printed, the unit (thousands, cents, $, hours, %), and the prior-year comparative if shown. Keep the period "twelve months ended December 31" and say it is unaudited if the filing says so.
4. Basis checks:
   - Mark non-GAAP rows (for airlines: Adjusted CASM, Adjusted CASM ex-fuel). Note that the 10-K reconciles them to CASM in the same Item.
   - Some KPIs are not additive totals, such as load factor, yield, CASM and average aircraft. Report them as the FY figure and say "FY value, not a sum".
   - Items in the MD&A text but not in the table (operating margin, liquidity) go in a separate "also discussed" line. Do not blend them into the KPI table.
   - Do not rename or recompute a value. If you derive anything, label it as derived.
5. Before submitting: confirm that the period is FY2024 (not Q4, not FY2023) and that the units match the table's header. List only the filing(s) actually opened as sources.

Task fact (Spirit Airlines FY2024, labelled; the base run retrieved these rows from the 10-K table and they should be re-confirmed in the text): average aircraft 209.9; aircraft at end of period 213 (includes 21 held for sale); average daily utilization 9.9 hours; departures 288,180; passenger flight segments 44,180 thousand; RPMs 43,671,009 thousand; ASMs 53,017,948 thousand; load factor 82.4%; total revenue per PFS $111.21; average yield 11.25 cents; TRASM 9.27 cents; CASM 11.35 cents; Adjusted CASM 10.76 cents; Adjusted CASM ex-fuel 7.97 cents; fuel gallons 551,819 thousand; average fuel cost per gallon $2.68. Check whether the table has any row not in this list (for example stage length) before submitting.
