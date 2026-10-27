---
name: interest_rate_sensitivity_net_income
description: Estimate the dollar and percent effect on net income (or net loss) if a company's debt were refinanced at a higher or lower interest rate, using the debt note, income statement and tax line from the 10-K.
---
ANALYTIC MOVE: calculate, then compare. Inputs are (a) total debt at fiscal year-end, (b) the rate shift in percentage points, (c) the tax treatment and (d) the reported net income or loss. Result: the incremental annual interest in dollars, the new net income, and the % change.

1. The shift is additive, so the current rate is NOT needed. Incremental pre-tax interest = total debt x shift (3 points = 0.03). Do not pull a third-party "weighted-average rate" (WACC pages, stock-analysis sites); it is not a filing figure and does not change the increment. If you show an implied current rate for context, label it as derived (interest and debt expense / debt).
2. Debt base. Open the 10-K debt note and the MD&A liquidity section and retrieve total debt at year-end including the short-term portion. Check whether the note total and any capital-resources table (principal or contractual view) differ. Use the balance-sheet-tied carrying-value total as the base, and show the other figure as a one-line sensitivity if it differs. State the year-end date.
3. Net income base. Retrieve from the income statement: net income or loss, net income attributable to the parent, income tax expense or benefit, and pre-tax result. Use "attributable to [company] shareholders" as the headline and name the choice; give the total-net-loss percentage if it is a one-line addition. Units are usually $ millions.
4. Tax. Lead with the simplest reading (debt x shift against reported net income), then give the after-tax figure as a clearly labelled second: after-tax = pre-tax x (1 - tax rate). Take the effective rate from the opened 10-K; give the statutory 21% as an alternate if the effective rate is distorted (a loss, a valuation allowance, a tiny benefit). Never take a tax rate from an unopened or third-party page.
5. Sign handling. If the company reported a net LOSS, the extra interest makes the loss larger. New result = reported - impact. Percent = impact / |reported| x 100, stated as "the loss grows by X%". Never give a bare negative percent without saying what it means.
6. Caveats, one line each: the full-year effect assumes all debt reprices on day one; fixed-rate debt reprices only at maturity; capitalized interest and interest income are ignored.
7. Answer contract: debt base with date and source; shift; dollar impact (pre-tax, and after-tax if shown); reported net income or loss; new net income or loss; % change with its sign convention; arithmetic unrounded until the end; sources limited to documents actually opened and retrieved from. Plain text, no citation markup.

Task facts (Boeing FY2024 10-K, retrieved in earlier runs; re-confirm in the text): https://www.sec.gov/Archives/edgar/data/12927/000001292725000015/ba-20241231.htm (about 477K characters; use targeted retrievals).
- Total debt at Dec 31, 2024 is $53,864M (Note 16; $1,278M short-term plus $52,586M long-term; MD&A says $53.9B). The Capital Resources table shows $54,369M for long-term debt including the current portion, which is a different, contractual view.
- Net loss attributable to Boeing shareholders $(11,817)M; total net loss $(11,829)M; loss before income taxes $(12,210)M; income tax benefit $381M (about 3.1%, distorted by a valuation allowance); interest and debt expense $2,725M.
- The 10-K gives no weighted-average rate, only coupon ranges by category.
- Pre-tax increment: 53,864 x 3% = $1,615.92M, which is 13.67% of 11,817.
