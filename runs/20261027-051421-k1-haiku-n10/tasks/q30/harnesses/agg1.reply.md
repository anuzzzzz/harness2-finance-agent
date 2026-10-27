<file path="skills/convertible_dilution_lookup/SKILL.md">
---
name: convertible_dilution_lookup
description: Find the maximum number of shares issuable on conversion of a company's outstanding convertible notes at a balance-sheet date, and reconcile it to the per-series figures.
---

# Convertible-note dilution ("maximum shares from the converts as of date X")

**Analytic move:** retrieve and reconcile. Several look-alike figures exist, and the question picks one.

**Where the figures live (10-K for the fiscal year ending on the date asked)**
- Net loss / earnings per share note: the table of securities excluded from diluted EPS as anti-dilutive. It has a "Convertible Notes (if-converted)" line, in thousands of shares, for the year-end date and prior years. This is the aggregate across all series and is the usual answer to "maximum dilutive impact".
- Debt / convertible senior notes note: per-series principal outstanding, conversion rate per $1,000 and conversion price. Some filings state a maximum share count for a series, including any make-whole increase. This can be higher than the EPS-table figure.
- An 8-K for a note issuance gives a maximum for that one series at issuance. It is not a year-end aggregate.

**Procedure**
1. Fix the balance-sheet date and the filing. Use the 10-K for that fiscal year, not an older 10-K or a 10-Q.
2. Get the aggregate if-converted line from the EPS note, using the current-year column. Note its units.
3. Cross-check against the debt note. For each series still outstanding at the date, compute principal outstanding ÷ 1,000 × conversion rate (or principal ÷ conversion price). Use principal outstanding at the date, not the original issue size. Exclude series repaid, converted or matured before the date. Sum the series. A later 10-Q's comparative column or the financial-statement tables can supply year-end principal if the 10-K text is not reachable.
4. If the sum matches the EPS line, report it. If the debt note states a make-whole maximum that differs, report both and say which one answers "maximum". If the series do not reconcile, say by how much and which figure you headline.
5. Do not use one series' ceiling (for example one issue's maximum including the initial purchasers' option) as the total. Do not add issuance-level maxima to the table total. Do not use diluted weighted-average shares or RSU/option counts.
6. Answer contract: the share count with units, the table and section, the period, the series covered with per-series shares, the cross-check result, and the prior-year comparative as brief context. Say plainly whether each figure came from an opened filing or a search excerpt.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks for the dilutive impact, share count or maximum shares issuable from convertible notes, call load_skill with `convertible_dilution_lookup`.

When you have the final answer, you should call the `submit_final_result` tool with it. Your submission will not be processed unless you call this tool.

You should include any necessary step-by-step reasoning, justification, calculations, or explanation in your answer. You will be evaluated both on the accuracy of the final answer, and the correctness of the supporting logic.

When possible, please provide any calculated answers to at least two decimal places (e.g. 18.78% rather than 19%). Please do not round intermediate steps in any calculations - you should only round your final answer.

At the end of your answer, you should provide your sources in a dictionary with the following format:
{
    "sources": [
        {
            "url": "https://example.com",
            "name": "Name of the source"
        },
        ...
    ]
}
</file>

<file path="tool_guidance.md">
# Tool use

- Before searching, fix the company, form type (10-K / 10-Q / 8-K) and fiscal period. As of the question date, use the latest filing already published. Search with those terms plus the exact line item. Always pass a non-empty `query`; a null query returns unrelated results.
- SEC endpoints often return HTTP 403 here. `edgar_search` and `parse_html_page` on sec.gov often fail. Do not retry a 403 and do not call `edgar_search` again after one failure. Make one or two targeted `web_search` calls (company, form, year, table name). Results often quote the table text and give the sec.gov URL. You may try `parse_html_page` once on a non-sec.gov HTML copy. If it works, store it under a clear key and ask `retrieve_information` one targeted question at a time. `parse_html_page` cannot read PDFs.
- Check the line item before using it: name the table, the period and the units (thousands vs millions).
- Cite only URLs that appeared in tool output. Do not give a figure you have not seen in tool output.
- Say in the answer whether the figure came from an opened filing or a search excerpt. Do not call an excerpt-only figure "verified".
- Do the arithmetic on unrounded numbers, re-check it once, and round only the final result. Once the figures are in hand, call `submit_final_result` right away.
- Write the answer as plain text with no raw citation tags.
</file>

<notes>
kept -> inv1 tool_guidance.md (with one added line on plain text, no cite tags) -> base1 hit edgar_search 403, a null-query web_search and a parse_html_page 403 before finding the figure, and cited an unseen 8-K URL; inv1 made no failed fetch and submitted in 2 turns; the same pattern appears in the q19/q45 library entries. Only 1 base rollout, so low confidence.
kept -> inv1 skill convertible_dilution_lookup as the base of the merged skill -> inv1 turn 2 searched the per-series principals and rates and summed them to 85,945,095, matching the EPS-table 85,945k. dom1 stopped at a partial reconciliation and said it could not fully reconcile.
revised -> dom1 skill content merged into the inv1 skill -> added dom1's rules: use principal outstanding at the date rather than issue size, exclude series repaid before the date, and treat issuance-8-K maxima as single-series figures. Both candidates' agents had mixed in the 44.8M 2030-notes ceiling.
revised -> added a hint that a later 10-Q comparative column can supply year-end principal -> dom1 failed to find 2025/2026 year-end principal, while inv1 got it from a 10-Q excerpt.
dropped -> the labelled task fact (Snap 85,945) in both skills -> the figure was seen only in excerpts. The q19 library entry showed embedded figures blur provenance and add no accuracy. All 3 runs found 85,945 by search alone.
kept -> trigger line in systemprompt.md, named `convertible_dilution_lookup` -> both candidate runs loaded their skill at turn 1; dom1's skill name was dropped in favour of inv1's.
dropped -> dom1 as a separate skill name `convertible_notes_dilution` -> it is a duplicate of the same skill, so I merged rather than concatenated. Neither candidate had a rollout that produced nothing; all 3 submitted.
</notes>