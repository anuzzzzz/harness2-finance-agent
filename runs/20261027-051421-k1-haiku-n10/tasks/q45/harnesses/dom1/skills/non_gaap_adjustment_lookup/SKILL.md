---
name: non_gaap_adjustment_lookup
description: Retrieve a specific adjustment line (e.g. stock-based compensation) from a company's Adjusted EBITDA / non-GAAP reconciliation for a fiscal year.
---

# Non-GAAP adjustment lookup ("what was the adjustment for X in year Y")

**Analytic move:** retrieve and reconcile. The answer is one line of the company's own reconciliation table for the stated fiscal year, with its units and a check that the table foots.

**Where the figure lives**
- Q4/full-year earnings release (8-K Exhibit 99.1): the "Reconciliation of Net Income to Adjusted EBITDA" table, with quarterly and full-year columns. Use the full-year column for a "in 2024" question, not the Q4 column.
- 10-K, MD&A, "Adjusted EBITDA" or "Non-GAAP Financial Measures" section: the same table for the fiscal year, with the prior year beside it.
- The cash flow statement and the stock-based compensation footnote also report a stock-based compensation figure. It can differ from the add-back because of capitalized amounts, restructuring-related items, or items shown on other lines. For an "adjustment" question the reconciliation line is the controlling figure. Mention the cash-flow figure only if it differs, and label it.

**Procedure**
1. Fix the fiscal year the question names and the measure (Adjusted EBITDA vs free cash flow vs non-GAAP net income). Each has its own reconciliation and can list the same item separately.
2. Read the line from the opened document (the reconciliation table in the 10-K or release), not from memory. Record the unit in the table header (millions or thousands).
3. Foot the table: net income plus every listed adjustment must equal Adjusted EBITDA, with the correct signs. If the sum does not match, you misread a line, a column or a year.
4. Give the prior-year comparative from the same table, and the year-over-year change, only if useful for context. Do not add figures the question did not ask for.
5. Answer contract: the adjustment amount with year and units, the table it came from (document, section), Adjusted EBITDA and net income for the same year as the footing evidence, and the URL. If the figure came from a search excerpt rather than an opened filing, say so.

**This task's sources (Airbnb, FY2024):** the FY2024 10-K is at https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm. The Q4 2024 shareholder letter is at https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf. In the earlier run the stock-based compensation add-back (about $1,407M) was reported without the table having been opened and footed, so treat it as unconfirmed until the table is read and foots.
