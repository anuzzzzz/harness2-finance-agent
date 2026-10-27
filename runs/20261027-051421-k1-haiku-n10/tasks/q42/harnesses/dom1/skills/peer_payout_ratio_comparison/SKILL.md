---
name: peer_payout_ratio_comparison
description: Compare a company's dividend payout ratio with its competitors for a fiscal year and rank them, with a defined peer set and a stated ratio definition.
---

# Peer dividend payout ratio comparison and ranking

**Analytic move:** retrieve, calculate, then rank. For each company, take dividends and earnings for the same fiscal year, compute the ratio, and sort the results.

**Definition (state it in the answer)**
- Headline ratio = dividends ÷ GAAP net income attributable to the company. The per-share equivalent is dividends per share ÷ GAAP diluted EPS. Use one definition for every company.
- Dividends: use cash dividends paid from the cash-flow statement, or dividends declared per share from the equity statement or dividend note. Do not mix paid and declared across companies. Declared and paid can differ because of timing.
- Earnings: use net income attributable to common shareholders (continuing operations if the filing separates it). It comes from the 10-K or the Q4 8-K Exhibit 99.1. Do not substitute adjusted, comparable or core EPS in the headline.
- Also show a secondary adjusted-basis ratio (dividends ÷ company non-GAAP EPS), labelled as such. Do this especially when GAAP earnings carry large one-offs such as impairments, restructuring or settlements. A one-off can push a payout ratio up or down enough to change the ranking. If the ranking differs between GAAP and adjusted, say so in one sentence and keep the GAAP ranking as the headline unless the question specifies otherwise.

**Peer set**
- Choose peers from the target's own 10-K competition discussion and from standard industry peers. For Coca-Cola, the core non-alcoholic beverage peers are PepsiCo, Keurig Dr Pepper and Monster Beverage. Add other listed beverage companies only if they are clearly relevant and you can source their figures. List the set and the reason for it.
- Include a peer that pays no dividend as 0.00%. Quote the filing language saying so. Rank it last, and say it is a non-payer rather than a computed ratio.
- Do not include companies whose fiscal year does not end near the target's without saying so. Match fiscal-year labels (FY2024), and note any non-calendar year-end.

**Checks before submitting**
1. Every figure is for the same fiscal year (FY2024 = the 10-K or Q4 release filed in early 2025, as of April 2025). Each figure was seen in tool output. Do not use a third-party data site's precomputed ratio as a substitute. Use it only as a cross-check and name it as such.
2. Units are consistent (per-share vs total dollars, thousands vs millions). A per-share and a total-dollar ratio for the same company should roughly agree (within about a percentage point, after buybacks and share-count effects). If they don't, explain why.
3. Recompute each ratio from unrounded inputs and round only at the end, to two decimals.
4. The ranking order matches the numbers, with ties and non-payers handled explicitly.

**Answer contract:** a ranked list from highest to lowest, each with the ratio to two decimals, its dividends and earnings inputs with units and fiscal period, the target company's position in the ranking, the definition used, the GAAP and adjusted comparison, and the source of each figure. Say whether a figure came from an opened filing or from a search excerpt. Write plain text with no raw citation tags, and end with the sources dictionary.
