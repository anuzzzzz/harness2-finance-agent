---
name: convertible_dilution_lookup
description: Find the maximum share dilution from a company's outstanding convertible notes at a balance-sheet date, and reconcile it to principal x conversion rate by series.
---
ANALYTIC MOVE: look up, then reconcile. Report the number of shares issuable on conversion of all outstanding convertible notes at the date asked, and check it against the debt footnote.

1. Controlling sources in the 10-K:
   - The net income (loss) per share note has a table of potentially dilutive securities excluded from diluted EPS. It usually has a line such as "Convertible Notes (if-converted)", in thousands of shares. This is the headline figure. Filings often state no separate "maximum" share count; the if-converted figure is the maximum potential dilution.
   - The debt note gives, for each series, the principal outstanding, the conversion rate per $1,000 of principal and the conversion price.
2. Reconcile. For each series, shares = principal / 1,000 x conversion rate. Sum the series and compare with the EPS-table line. Carry full precision and round only at the end. If the two differ, say why (for example a series repaid or converted during the year, or make-whole shares) and name which figure you use.
3. Keep these distinct and label them: shares on an if-converted basis, shares actually included in diluted EPS (zero when there is a net loss, because they are anti-dilutive), and any offset from capped calls or hedges. State whether the capped calls are netted into the figure. Do not net them unless the filing does.
4. Check the units (thousands of shares vs millions), the date (the period-end the question names, not the filing date), and that every series outstanding at that date is included. Take principal amounts from the debt note at that date, not from the original issue size.
5. Answer contract: the total shares with unit and date, the per-series table (principal, conversion rate, shares), the sum check against the disclosed total, the note that this is maximum potential dilution rather than diluted-EPS shares, and the sources.
6. List as sources only documents you opened and retrieved from.

Task lead (retrieved in two runs, re-confirm in the text): Snap Inc. FY2024 10-K (https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm). The Note 3 table at 12/31/2024 shows "Convertible Notes (if-converted)" of 85,945 thousand shares. The series are the 2025, 2026, 2027, 2028 and 2030 notes. Conversion rates per $1,000 were 46.1233, 43.8481, 11.2042, 17.7494 and 45.0846. Principal ($ thousands) was 36,240, 249,754, 1,150,000, 1,500,000 and 750,000. These imply about 1.67M, 10.95M, 12.89M, 26.62M and 33.81M shares, which sum to about 85.945M.
