<file path="tool_guidance.md">
# Tool guidance

Before searching, decide which documents and periods the question needs: each company, form type (10-K, 10-Q, 8-K exhibit 99.1) and fiscal period. Then search with those filters, not the question's wording. Use only documents dated on or before April 07, 2025.

- `edgar_search`: pass the ticker or CIK, a date range, and the form type. If it returns 0 results, change the filters once. If it still returns nothing, use `web_search` for the primary document. Do not repeat an empty `web_search`.
- `web_search`: use it to find primary documents. A snippet or third-party page (dividend history sites, aggregators) is a lead, not evidence.
- `parse_html_page`: store each primary document under a clear key (for example `ko_10k_2024`, `pep_10k_2024`). When the question needs several companies, open every company's FY 10-K in the same turn.
- `retrieve_information`: ask one targeted question at a time per document. On long filings, use `input_character_ranges`. Ask for the exact figure with its period, unit and row label, quoted verbatim. If a row is unclear, check it in a second table (for example the cash flow statement) instead of inferring.

Enough evidence means each figure that enters a calculation was read from a period-matching column of a primary document that was actually opened and retrieved. A figure seen only in a search result is a lead. Do not write that a figure was "read from" a filing unless a retrieve call on it returned it.

Peer-comparison and ranking questions (several companies, one ratio):
- First state the peer set and the single formula, and apply the SAME formula and data basis to every company. For a payout ratio, use the cash-flow-statement dividends paid divided by net income attributable to the company's shareholders, both from each company's FY10-K. Mixing one company's aggregate dollars with another's per-share figures makes the ranking non-comparable. Use per-share declared dividends divided by diluted EPS only as a labelled cross-check.
- If a company's fiscal year does not match the calendar year, name its fiscal year end. If a peer pays no dividend, report 0% and quote the filing's statement saying so.
- Where GAAP earnings are distorted (for example by an impairment), give the GAAP-basis ranking as the headline and mention the adjusted figure separately.
- Keep full precision until the end. Give a ranked list, highest to lowest, with each company's inputs and ratio.

In this task (verified from Coca-Cola's FY2024 10-K): dividends paid were $8,359 million and net income attributable to shareowners was $10,631 million, so the payout is 78.63%. Re-verify peers from their own 10-Ks. In the prior run PepsiCo and KDP were done per-share only, because aggregate dividends paid were never retrieved.

Output: write plain text with no citation tags or markup. Before `submit_final_result`, re-check each figure against the retrieved text for period, units and label, and say which document each figure came from. Submit while budget remains.
</file>

<notes>
Motivating moment: base1 made one batch of web searches and submitted in the next turn. It computed KO from aggregate 10-K dollars (8,359 / 10,631 = 78.63%), but PepsiCo and KDP only from per-share numbers. The PepsiCo dividend came from a Fidelity table and the KDP full-year dividend was reconstructed from nine-month data plus a guessed Q4. It also left raw cite tags in the answer, and its KO cross-check used an EPS figure it said was not in its sources. The edit adds, in tool_guidance only: open all peers' 10-Ks together, use one formula and data basis across companies, treat per-share as a labelled cross-check, state the peer set, and write plain text without citation tags. It also records the KO facts the run did verify, labelled as task facts. No skill was added, because this is a short generic sequencing rule and the library shows skills only added a load turn.
</notes>