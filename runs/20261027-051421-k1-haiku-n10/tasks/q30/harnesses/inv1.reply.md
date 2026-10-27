<file path="tool_guidance.md">
# Tool use

- Before searching, fix the company, form type (10-K / 10-Q / 8-K) and fiscal period. As of the question date, use the latest filing already published. Search with those terms plus the exact line item. Always pass a non-empty `query`; a null query returns unrelated results.
- SEC endpoints often return HTTP 403 here. `edgar_search` and `parse_html_page` on sec.gov both failed in the earlier run. Do not retry a 403 and do not call `edgar_search` again after one failure. Make one or two targeted `web_search` calls (company, form, year, table name). Results often quote the table text and give the sec.gov URL. You may try `parse_html_page` once on a non-sec.gov HTML copy. If it works, store it under a clear key and ask `retrieve_information` one targeted question at a time. `parse_html_page` cannot read PDFs.
- Check the line item before using it: name the table, the period and the units (thousands vs millions).
- Cite only URLs that appeared in tool output. Do not give a figure you have not seen in tool output.
- Say in the answer whether the figure came from an opened filing or a search excerpt. Do not call an excerpt-only figure "verified".
- Do the arithmetic on unrounded numbers, re-check it once, and round only the final result. Once the figures are in hand, call `submit_final_result` right away.
</file>

<file path="skills/convertible_dilution_lookup/SKILL.md">
---
name: convertible_dilution_lookup
description: Find the maximum number of shares issuable on conversion of a company's outstanding convertible notes at a balance-sheet date, and reconcile it to the per-series figures.
---

# Convertible-note dilution ("maximum shares from the converts as of date X")

**Analytic move:** retrieve and reconcile. Two look-alike figures exist, and the question picks one.

**Where the figures live (10-K for the fiscal year ending on the date asked)**
- Net loss / earnings per share note: the table of securities excluded from diluted EPS as anti-dilutive. It has a "Convertible Notes (if-converted)" line, in thousands of shares, for the year-end date and prior years. This is the aggregate across all series.
- Debt / convertible senior notes note: per-series principal, conversion rate per $1,000 and conversion price. Some filings state a maximum share count for a series, including any make-whole increase. This can be higher than the EPS-table figure.

**Procedure**
1. Fix the balance-sheet date and the filing. Use the 10-K for that fiscal year, not an older 10-K or a 10-Q.
2. Get the aggregate if-converted line from the EPS note. Note its units.
3. Cross-check against the debt note: for each series still outstanding at the date, principal ÷ 1,000 × conversion rate, summed. Exclude series already repaid or converted. If the sum matches the EPS line, report it. If the debt note states a maximum including make-whole, report both and say which one answers "maximum".
4. Do not use a single series' ceiling (for example one issue's maximum with the initial purchasers' option) as the total.
5. Answer contract: the share count with units, the table and section, the period, the series covered, and the cross-check result. Say plainly whether it came from an opened filing or a search excerpt.

**Task fact (labelled, unconfirmed):** in this task (Snap Inc, 12/31/2024), a search excerpt of the FY2024 10-K showed "Convertible Notes (if-converted) 85,945" thousand shares (89,379 in 2023 and 2022) in the anti-dilutive securities table. The filing itself was not opened (403), and no per-series cross-check was made. Re-verify it.
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

<notes>
Moments in base1: the agent called edgar_search with a 403, a null-query web_search, and parse_html_page on sec.gov (403) before it found the figure in search excerpts. It then submitted 85,945 thousand without a per-series cross-check. It also cited an 8-K URL that never appeared in its tool output. tool_guidance.md is copied from the q19/q45 library pattern: one bounded fallback, non-empty query, cite only seen URLs, and disclose the excerpt basis. The new skill covers the narrow procedure: take the aggregate if-converted line from the EPS note, then reconcile it to the per-series conversion math in the debt note. It separates that figure from make-whole or per-series maxima. The agent's own text mixed in the 2030 notes' 44.8M ceiling without reconciling it. The 85,945 figure is stored as a labelled, unconfirmed task fact because it was seen only in an excerpt. A trigger line in systemprompt.md names the skill.
</notes>