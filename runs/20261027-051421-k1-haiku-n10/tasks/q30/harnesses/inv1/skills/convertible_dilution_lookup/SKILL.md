---
name: convertible_dilution_lookup
description: Find the maximum number of shares issuable on conversion of a company's outstanding convertible notes at a balance-sheet date, and reconcile it to the per-series figures.
---

# Convertible-note dilution ("maximum shares from the converts as of date X")

**Analytic move:** retrieve and reconcile. Two look-alike figures exist, and the question picks one.

**Where the figures live (10-K for the fiscal year ending on the date asked)**
- Net loss / earnings per share note: the table of securities excluded from diluted EPS as anti-dilutive. It has a "Convertible Notes (if-converted)" line, in thousands of shares, for the year-end date and prior years. This is the aggregate across all series.
- Debt / convertible senior notes note: per-series principal, conversion rate per $1,000 and conversion price. Some filings state a maximum share count for a series, including any make-whole increase. This can be higher than the EPS-table figure.

**Procedure**
1. Fix the balance-sheet date and the filing. Use the 10-K for that fiscal year, not an older 10-K or a 10-Q.
2. Get the aggregate if-converted line from the EPS note. Note its units.
3. Cross-check against the debt note: for each series still outstanding at the date, principal ÷ 1,000 × conversion rate, summed. Exclude series already repaid or converted. If the sum matches the EPS line, report it. If the debt note states a maximum including make-whole, report both and say which one answers "maximum".
4. Do not use a single series' ceiling (for example one issue's maximum with the initial purchasers' option) as the total.
5. Answer contract: the share count with units, the table and section, the period, the series covered, and the cross-check result. Say plainly whether it came from an opened filing or a search excerpt.

**Task fact (labelled, unconfirmed):** in this task (Snap Inc, 12/31/2024), a search excerpt of the FY2024 10-K showed "Convertible Notes (if-converted) 85,945" thousand shares (89,379 in 2023 and 2022) in the anti-dilutive securities table. The filing itself was not opened (403), and no per-series cross-check was made. Re-verify it.
