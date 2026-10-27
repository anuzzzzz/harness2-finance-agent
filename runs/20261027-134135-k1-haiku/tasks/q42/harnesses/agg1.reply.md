<file path="tool_guidance.md">
# Tool guidance

Before searching, decide which documents and periods the question needs: each company, form type (10-K, 10-Q, 8-K exhibit 99.1) and fiscal period. Then search with those filters, not the question's wording. Use only documents dated on or before April 07, 2025.

- `edgar_search`: pass the ticker or CIK, a date range, and the form type. If it returns 0 results, change the filters once. If it still returns nothing, use `web_search` for the primary document. Do not repeat an empty `web_search`.
- `web_search`: use it to find primary documents. A snippet or third-party page (dividend history sites, aggregators, TTM ratio pages) is a lead, not evidence.
- `parse_html_page`: store each primary document under a clear key (for example `ko_10k_2024`). When the question involves several companies, open every company's 10-K in the same turn, including the company the question is centred on. Do not rely on a figure remembered from an earlier run or stated in a prompt without re-reading it from the filing.
- `retrieve_information`: ask one targeted question per document, and ask for several related figures at once (for example dividends paid, net income attributable, diluted EPS, declared dividends per share). On long filings, use `input_character_ranges`. Ask for exact figures with period, unit and row label, quoted verbatim. If a row is unclear, check it in a second table (for example the cash flow statement versus the income statement).

Enough evidence means each figure that enters a calculation was read from a period-matching column of a primary document that was actually opened and retrieved. Do not write that a figure was "read from" a filing unless a retrieve call returned it.

Peer-comparison and ranking questions (several companies, one ratio):
- State the peer set and the single formula, and apply the SAME formula and data basis to every company. Never mix one company's aggregate dollars with another's per-share figures.
- Dividend payout ratio: cash-flow-statement dividends paid divided by GAAP net income attributable to the company's shareholders, same fiscal year, both from each company's FY 10-K. Say that the basis is paid, not declared. Per-share declared dividends divided by diluted EPS is a labelled cross-check, or the fallback only if aggregate paid dividends cannot be retrieved. If you fall back, apply it to every company.
- Name each company's fiscal year end where it differs from December 31. A peer that pays no dividend gets 0%, quoting the filing's statement, and is shown rather than omitted.
- Where GAAP earnings are distorted (for example by an impairment), keep the GAAP ranking as the headline and mention any adjusted figure separately.
- Keep full precision until the end. Give a ranked list highest to lowest, with each company's inputs, the arithmetic, and the source document.

Output: write plain text with no citation tags or markup. Before `submit_final_result`, re-check each figure against the retrieved text for period, units and label, and say which document each figure came from. Submit while budget remains.
</file>

<notes>
kept -> inv1 tool_guidance (open all companies' 10-Ks together, same formula/basis, plain text) -> base1 mixed KO aggregate dollars with PEP/KDP per-share and used snippets (1/1 base); inv1 opened 10-Ks at turn 2 and got aggregate figures for peers with consistent basis in 5 turns.
revised -> inv1 task-facts paragraph (KO 8,359 / 10,631) dropped -> in inv1's rollout the embedded facts led it to skip the KO retrieval and cite "figures given in the task", leaving the subject company unverified; dom1 re-read KO from the filing. Added a rule to open the subject company's 10-K too and not rely on remembered or prompt-supplied figures.
dropped -> dom1 skill dividend_payout_peer_compare and its systemprompt trigger line -> dom1 spent turn 1 loading the skill and reached the same ranking/values (KDP 82.86, KO 78.63, PEP 75.48, MNST 0) as inv1 at higher cost ($0.455 vs $0.311); a library lesson says skills only added load turns. Its useful content (paid vs declared, peer set, non-payers 0%, fiscal year ends, GAAP headline) is folded into the short tool_guidance paragraph instead.
kept -> dom1 content on paid-vs-declared basis, fallback applying to all companies, and verifying KO from its own 10-K -> dom1 retrieved KO, PEP, KDP, MNST in one batched turn with multi-figure prompts; merged as a "ask for several related figures at once" line.
No candidate rollout produced nothing: both submitted, so neither edit is flagged unsafe. Both candidates reached identical numbers, so the merge is supported but not independently proven.
</notes>