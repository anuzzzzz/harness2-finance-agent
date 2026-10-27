---
name: dividend_payout_peer_compare
description: Compare dividend payout ratios across a company and its competitors for a fiscal year and rank them, on one consistent basis from each company's 10-K.
---

# Dividend payout ratio: peer comparison and ranking

**Analytic move:** compare. Inputs are, for each company, FY dividends and FY earnings. The result is a ranked list on one basis.

## Definition (state it in the answer)
Payout ratio = common dividends ÷ net income attributable to common shareholders, for the same fiscal year.
- Primary basis: aggregate cash dividends paid (cash flow statement, financing section, "dividends paid" or "cash dividends paid") ÷ GAAP net income attributable to the company (income statement).
- Use the same basis for every company. Do not divide dollars by dollars for one company and per-share by per-share for another.
- Per-share declared dividends ÷ diluted GAAP EPS is an acceptable cross-check, and it is the fallback only if the aggregate paid figure cannot be retrieved. If you fall back, say so and apply it to every company.
- Dividends declared and dividends paid differ by timing (a Q4 dividend declared in December may be paid in January). Say which one you used.
- GAAP and adjusted/non-GAAP payout differ materially when there are impairments or one-offs. Rank on GAAP. Add one line showing the adjusted figure only if the company's own release reconciles it.

## Peer set
- Competitors means direct peers in the same line of business that file with the SEC and have FY2024 data. For Coca-Cola, start from PepsiCo, Keurig Dr Pepper and Monster Beverage. Add other listed bottlers or beverage peers only if you can open their filings (for example Coca-Cola Consolidated).
- State the peer set in the answer. A company that pays no dividend has a payout ratio of 0% and goes last. Show it rather than omitting it.
- Fiscal year ends differ (for example PepsiCo's FY2024 ends in late December and KDP's on Dec 31). Use each company's fiscal 2024 and state the period end.

## Where the figures live
- 10-K Item 8: the consolidated statements of cash flows (dividends paid), and the income statement (net income attributable to shareowners, diluted EPS).
- Equity statement or notes: dividends declared per share.
- Do not use aggregator pages (payout ratio TTM on MarketBeat, GuruFocus and similar) as the figure. They use different periods and bases. Only filings dated on or before April 07, 2025 count.

## Task facts to re-verify (found in a prior run, not yet confirmed from opened documents)
- In this task, Coca-Cola's 10-K reportedly shows dividends paid of $8,359M in 2024 and net income attributable to shareowners of $10,631M, a ratio of about 78.63%. Confirm both from the opened 10-K (cash flow statement and income statement).
- The earlier run did not retrieve PepsiCo's or KDP's aggregate dividends paid, and it mixed bases. Retrieve each company's cash-flow dividends and net income from its own FY2024 10-K.

## Answer contract
1. A ranked list from highest to lowest payout ratio, with Coca-Cola's rank clearly marked.
2. A table per company with: fiscal year end, dividends ($M), net income attributable to the company ($M), ratio to two decimals, and the source document.
3. The arithmetic shown, unrounded until the end.
4. The basis stated (paid vs declared, GAAP) and the peer set stated.
5. Before submitting, confirm every figure comes from an opened primary document (not from memory or search snippets), and that the period, units (millions) and share count basis match across companies.
