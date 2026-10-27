---
name: convertible_notes_dilution
description: Share-count dilution from convertible senior notes (maximum or if-converted shares) at a balance-sheet date, built from the 10-K debt and EPS notes.
---

# Convertible notes: dilutive share count

ANALYTIC MOVE: calculate and reconcile. Inputs are the principal outstanding and the conversion rate for each note series at the stated date. Result is shares issuable per series and in total, reconciled to the figure the company reports.

## Where the figures live (10-K)
- Net loss per share note (in this task, Note 3): the table of potentially dilutive securities excluded as anti-dilutive. It has a "Convertible Notes (if-converted)" line in thousands of shares at each year-end. This is the company's own aggregate share count.
- Debt note (in this task, Note 7): per series, the principal outstanding, conversion rate per $1,000, conversion price, maturity, and make-whole or fundamental-change language. Item 7 liquidity repeats some of it.
- Capped-call and hedge paragraphs: capped calls offset dilution economically but do not lower the gross shares issuable. Report gross and mention the capped calls separately.
- Each series' indenture or its 8-K exhibit 4.x gives the "maximum conversion rate" that applies after a make-whole fundamental change. Treat it as a separate upper bound.

## Verified in this task (Snap FY2024 10-K, read through the retrieval tool, so re-confirm in the text)
- The if-converted line was 85,945 thousand shares at 12/31/2024 (89,379 thousand at 12/31/2023 and 2022).
- Principal x conversion rate by series at 12/31/2024 sums to about 85,945 thousand. Per series: 2025 notes $36.24M at 46.1233; 2026 notes $249.754M at 43.8481; 2027 notes $1,150M at 11.2042; 2028 notes $1,500M at 17.7494; 2030 notes $750M at 45.0846.
- The 2030 notes' maximum conversion rate, from the May 2024 8-K indenture, is 59.7371 per $1,000. The base run found no maxima for the other series.

## Procedure
1. Retrieve the dilutive-securities table row and the per-series principal and rate from the 10-K text, quoted with period and unit. Check that the date is the one the question names.
2. Compute principal / 1,000 x rate for each series. Sum them and reconcile to the reported if-converted line. Explain any gap, such as a repaid or repurchased series or a change in principal.
3. Search the 10-K text for "maximum", "make-whole" and "fundamental change". If the 10-K states a maximum number of shares issuable, quote it and use it as the answer.
4. If the question says "maximum", check whether each series has a maximum conversion rate, found in the 10-K or the 8-K exhibit for that series. Compute a maximum only when it is applied to EVERY series with a retrieved maximum rate. Do not combine one series at its maximum rate with the others at base rates and present that total as the maximum. If only some maxima are found, say so and lead with the reported if-converted figure.
5. State the answer as a lead number in shares (and in millions), with the per-series table, the date, and the basis (if-converted at base rates vs make-whole maximum). Keep the basis explicit and give the base-rate total and the make-whole total as separate labelled lines.
6. Before submitting, confirm that the principal amounts are as of the question's date. Also confirm that units are thousands of shares, not dollars.
