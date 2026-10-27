---
name: convertible_dilution_lookup
description: Find the maximum number of shares issuable on conversion of a company's outstanding convertible notes at a balance-sheet date, and reconcile it to the per-series figures.
---

# Convertible-note dilution ("maximum shares from the converts as of date X")

**Analytic move:** retrieve and reconcile. Several look-alike figures exist, and the question picks one.

**Where the figures live (10-K for the fiscal year ending on the date asked)**
- Net loss / earnings per share note: the table of securities excluded from diluted EPS as anti-dilutive. It has a "Convertible Notes (if-converted)" line, in thousands of shares, for the year-end date and prior years. This is the aggregate across all series and is the usual answer to "maximum dilutive impact".
- Debt / convertible senior notes note: per-series principal outstanding, conversion rate per $1,000 and conversion price. Some filings state a maximum share count for a series, including any make-whole increase. This can be higher than the EPS-table figure.
- An 8-K for a note issuance gives a maximum for that one series at issuance. It is not a year-end aggregate.

**Procedure**
1. Fix the balance-sheet date and the filing. Use the 10-K for that fiscal year, not an older 10-K or a 10-Q.
2. Get the aggregate if-converted line from the EPS note, using the current-year column. Note its units.
3. Cross-check against the debt note. For each series still outstanding at the date, compute principal outstanding ÷ 1,000 × conversion rate (or principal ÷ conversion price). Use principal outstanding at the date, not the original issue size. Exclude series repaid, converted or matured before the date. Sum the series. A later 10-Q's comparative column or the financial-statement tables can supply year-end principal if the 10-K text is not reachable.
4. If the sum matches the EPS line, report it. If the debt note states a make-whole maximum that differs, report both and say which one answers "maximum". If the series do not reconcile, say by how much and which figure you headline.
5. Do not use one series' ceiling (for example one issue's maximum including the initial purchasers' option) as the total. Do not add issuance-level maxima to the table total. Do not use diluted weighted-average shares or RSU/option counts.
6. Answer contract: the share count with units, the table and section, the period, the series covered with per-series shares, the cross-check result, and the prior-year comparative as brief context. Say plainly whether each figure came from an opened filing or a search excerpt.
