---
name: peer_payout_ratio_compare
description: Compare a company's dividend payout ratio with its competitors' for a fiscal year and rank them, using the same definition and basis for every company and figures retrieved from each 10-K.
---
ANALYTIC MOVE: compute the same ratio for a named company and its peers, then rank.

1. Fix the peer set before searching. Name the competitors (from the company's 10-K competition section or the obvious direct listed peers), and say why each is in or out. A peer that pays no regular dividend cannot be ranked. List it as excluded rather than silently dropping it.
2. Fix the definition once and apply it to every company. Headline = dividends declared per common share / diluted EPS for the fiscal year (GAAP). Cross-check = total cash dividends paid / net income attributable to the company, from the cash-flow statement and income statement. Where companies report adjusted EPS, show an adjusted-basis ratio only as a labelled secondary column, and give the ranking on the headline basis first. If the two bases give a different order, say so.
3. Per company, open the FY 10-K (parse_html_page, one key per company) and retrieve with retrieve_information: dividends declared per share, diluted EPS, cash dividends paid, net income. Confirm period (fiscal year, which can end in a non-December week), unit and basis in the text. Do not use search snippets as inputs.
4. Compute with unrounded inputs and round only the final ratio (two decimals). If a company's per-share dividend is a sum of quarterly declarations, check it against the annual figure in the filing.
5. Answer: ranking highest to lowest with each ratio, the inputs with period, unit and source, the formula, the cross-check, the excluded peers, and the basis caveat. Cite only documents actually opened.

Leads from one earlier run (snippet-sourced and unverified; re-confirm in the 10-Ks): FY2024 Coca-Cola dividends $1.94/share, GAAP diluted EPS $2.46, comparable EPS $2.88. PepsiCo dividends declared $5.33/share, GAAP EPS $6.95, core EPS $8.16. Keurig Dr Pepper dividends $0.89/share, GAAP EPS $1.05, adjusted EPS $1.92. KO 10-K: https://www.sec.gov/Archives/edgar/data/21344/000002134425000011/ko-20241231.htm. KDP 10-K: https://www.sec.gov/Archives/edgar/data/1418135/000141813525000013/kdp-20241231.htm. Find the PepsiCo FY2024 10-K via edgar_search (the prior run did not open it).
