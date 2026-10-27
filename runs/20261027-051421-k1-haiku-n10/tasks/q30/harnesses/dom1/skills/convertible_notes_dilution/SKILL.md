---
name: convertible_notes_dilution
description: Answer "maximum dilutive impact / shares issuable on conversion" of a company's convertible notes at a fiscal year-end, with reconciliation across note series.
---

# Convertible notes: share dilution at a balance-sheet date

**Analytic move:** retrieve and reconcile. Get the aggregate number of Class A (or common) shares that all outstanding convertible notes could convert into at the date named, then check it against the per-series conversion terms.

**Where the figures live (10-K for the fiscal year named)**
- EPS note ("Net Loss / Income per Share"): the table of potentially dilutive securities excluded from diluted EPS as anti-dilutive. It has a line such as "Convertible Notes (if-converted)", in thousands of shares, for the current year and the two prior years. This is the aggregate figure and the usual answer to "maximum dilutive impact".
- Debt / Convertible Notes note: for each series (by year of maturity) the principal still outstanding, the initial conversion rate (shares per $1,000) or conversion price, and any maximum conversion rate that applies after a make-whole fundamental change. A text sentence in the note or in Liquidity may also state a "maximum" share count. If one is stated, report it and say which it is.
- The 8-K for a note issuance states a maximum share count for that series only (including the initial purchasers' option). That is a single series at issuance, not the year-end aggregate.

**Procedure**
1. Fix the date (fiscal year-end) and which series were outstanding then. Exclude series repurchased, converted or matured before the date, and include series issued before it. Use principal outstanding at the date, not the original issue amount.
2. Read the aggregate from the EPS anti-dilutive table (current-year column, not the prior year). Note the unit (thousands of shares).
3. Reconcile: for each series, principal outstanding / 1,000 x conversion rate (or principal / conversion price) gives shares. The series should sum to about the aggregate. Do not add series maxima from issuance 8-Ks to the table total. If a make-whole maximum rate exists and differs from the if-converted figure, report the if-converted figure as the headline and the make-whole as labelled context.
4. If the series do not reconcile to the aggregate, say which differs and by how much, and name the figure you headline and why.
5. Do not use diluted weighted-average shares, share counts for RSUs/options, or a dollar amount as the answer. The question asks for shares from the notes only.

**Answer contract:** the share count with units (shares or thousands), the fiscal year-end, the table and filing it came from, a per-series breakdown if available, the prior-year comparative as brief context, and the URL. Say plainly whether the figure came from an opened filing or a search excerpt.

**Task fact (this research desk, Snap Inc, FY2024 10-K; seen only in a search excerpt, not in an opened filing):** the anti-dilutive table showed Convertible Notes (if-converted) of 85,945 thousand shares at 12/31/2024 (89,379 thousand in 2023 and 2022). Series outstanding: 2025, 2026, 2027, 2028 and 2030 notes. Re-check against the filing text and the per-series conversion terms before relying on it. The 2030 series alone is up to 44,802,825 shares per its May 2024 8-K.
