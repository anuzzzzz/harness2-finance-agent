---
name: ratio_from_10k_statements
description: Compute a turnover, margin, leverage or return ratio (inventory turnover, DIO, asset turnover, ROE) from a company's 10-K income statement and balance sheet, with the definition, the average-vs-ending choice and a labelled alternate.
---
ANALYTIC MOVE: calculate. Inputs are one flow figure (income statement or cash flow) and one stock figure (balance sheet), each for the right fiscal year. Result is the ratio, with the formula shown.

1. Source. Open the company's 10-K for the named fiscal year with parse_html_page. Retrieve the figures from the Consolidated Statements of Operations and the Consolidated Balance Sheets. One 10-K carries two balance-sheet dates (current and prior year-end), so it supplies both ends of a year's average. Earnings-release snippets are leads only. Confirm each figure, period and unit ($ millions vs thousands) in the retrieved text.
2. Definitions.
   - Inventory turnover = cost of goods sold (the "Cost of sales" line) / average inventory. Average inventory = (beginning-of-year + end-of-year inventory) / 2. Beginning is the prior year-end balance.
   - Also give days inventory outstanding = 365 / turnover, if it helps the reader.
   - Use net inventories as shown on the balance sheet (after LIFO reserves and write-downs). Do not add a LIFO reserve unless the question asks.
3. Average vs ending. State the primary basis explicitly. Default to the average-balance version, because it is the standard definition. Also show the ending-balance ratio as a clearly labelled alternate, with one line each. Never present two unlabelled headline numbers.
4. Cost-line caveat. Check whether "Cost of sales" excludes depreciation, depletion and amortization, which some industrial and steel issuers report on a separate line. If so, use the reported cost-of-sales line as the default and note the exclusion in one sentence. Do not add D&A unless the question asks.
5. Period alignment. The flow figure must be for the same 12-month fiscal year as the ending balance. Check the fiscal year-end date. Do not mix a calendar-year and a fiscal-year figure, and do not use a 10-Q's quarterly cost of sales.
6. Answer contract: the headline ratio at two decimals; the cost of sales, beginning inventory and ending inventory with period and unit; the average and the division at full precision, rounded only at the end; the labelled alternate; sources limited to documents actually opened.

Task facts (US Steel, FY2024; a prior run took these from earnings-release snippets without opening anything, so re-confirm in the opened 10-K). The FY2024 10-K is https://www.sec.gov/Archives/edgar/data/1163302/000116330225000018/x-20241231.htm. The leads: cost of sales 2024 = $14,060M, inventories $2,168M at 12/31/2024 and $2,128M at 12/31/2023. These give 14,060 / 2,148 = 6.5456 on average inventory and 14,060 / 2,168 = 6.4852 on ending inventory. U. S. Steel reports depreciation, depletion and amortization on a separate line, outside cost of sales.
