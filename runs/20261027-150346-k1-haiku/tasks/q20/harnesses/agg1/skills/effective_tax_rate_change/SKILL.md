---
name: effective_tax_rate_change
description: Report a company's effective tax rate for a fiscal year, the prior-year rate, and the change in bps, using the company-stated GAAP rates with an unrounded cross-check.
---
ANALYTIC MOVE: look up, then compare. Inputs are the provision for income taxes and income before income taxes for the two fiscal years. The result is each year's effective tax rate and the change in basis points.

1. Controlling source: the FY 10-K. Look in MD&A "Provision for Income Taxes", which has a line "Effective tax rate x% y%", and in the income-taxes note (rate reconciliation). The earnings release (8-K EX-99.1) only confirms. Take both years from the same 10-K's comparative columns, which keeps the basis consistent.
2. Headline = the effective tax rates the company states, at its published precision. Compute the change in bps as (current stated rate - prior stated rate) x 100. Show it in the form the question prescribes, e.g. "Delta: 410bps".
3. Cross-check on a separate labelled line: provision / pre-tax income for each year, unrounded, and the bps change from those. Say that this differs from the headline only because the company rounds its rates to one decimal. Do not present the two as equal answers. Name which one is the headline.
4. Distractors:
   - Non-GAAP or "adjusted" effective rates in the earnings-release reconciliation footnotes are not the GAAP rate asked for. Mention them only as a labelled aside, if at all.
   - Check the fiscal year-end against the question (a 5/31 year-end is not a calendar year).
   - A rate change is in percentage points, not percent. 1 percentage point = 100bps.
5. Give the drivers of the change as the MD&A states them (quote or closely paraphrase retrieved text). Do not invent drivers.
6. Answer contract: both rates with fiscal-year labels, the provision and pre-tax income for each year in $ millions, the calculation, the bps delta in the requested format, the direction (increase or decrease), the drivers, and sources limited to documents actually opened.

Task facts (Oracle, FY ended 5/31; retrieved in a prior run from the FY2024 10-K MD&A and Note 13, so re-confirm in the text), $ millions:
- FY2024 pre-tax income 11,741, provision 1,274, stated rate 10.9%.
- FY2023 pre-tax income 9,126, provision 623, stated rate 6.8%.
- The stated-rate change is 410bps. The unrounded change is about 402bps (10.8509% vs 6.8266%).
- Oracle's non-GAAP adjusted rates (19.2% and 16.3%) are a distractor.
- FY2024 10-K: https://www.sec.gov/Archives/edgar/data/1341439/000095017024075605/orcl-20240531.htm
