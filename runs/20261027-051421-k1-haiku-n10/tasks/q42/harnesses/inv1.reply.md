<file path="skills/peer_payout_ratio_ranking/SKILL.md">
---
name: peer_payout_ratio_ranking
description: Compare one company's dividend payout ratio with its competitors for a fiscal year and rank them, on a single consistent definition.
---

# Peer dividend-payout ranking

**Analytic move:** retrieve the same two lines from each company's own annual filing, calculate on one basis, rank.

**Procedure**
1. Before searching, write down (a) the fiscal year and each company's year-end (the 52/53-week years differ), and (b) the peer set with a one-line reason for each peer. Use direct competitors in the same industry that are listed and file 10-Ks. Peers that pay no dividend go in the ranking at 0.00% with a note saying so. Do not silently drop them or add unrelated companies.
2. Primary definition, applied identically to every company: **dividends paid to common shareholders (cash flow statement, financing section) ÷ net income attributable to the company's common shareholders (income statement)**, both from the FY 10-K. Name the table, period and units for each figure. Search with the company, "10-K", fiscal year and the statement name. A web_search excerpt of the statement is acceptable if the filing cannot be opened. Say which one you used.
3. Cross-check with dividends per share ÷ diluted EPS. Dividends declared and dividends paid differ in timing, so state which per-share figure you used. If the two methods give a different ranking, say so and headline the primary method. Do not mix methods across companies, and do not take a third-party "payout ratio" field as an input.
4. Adjusted (non-GAAP) EPS ratios are secondary. Show them only as labelled context, and only if GAAP net income is distorted by one-off items (impairments, for example). Do not let them silently replace the GAAP ratio.
5. Re-check before submitting: every company has both inputs from the same fiscal year, the units match (millions vs thousands), and the sort order matches the numbers. Recompute each ratio once from unrounded inputs.
6. Answer contract: a ranked list from highest to lowest with the ratio to two decimals, the dividends and net income behind each ratio, the peer-set rationale, a clear statement of where the subject company ranks, and the source of each figure (opened filing or search excerpt). Plain text with no raw citation tags.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks you to compare or rank a company's dividend payout ratio (or similar ratio) against competitors, call load_skill with `peer_payout_ratio_ranking`.

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

- Fix the companies, form type (10-K), and fiscal year before searching. Search with company, form, year and the statement or line item (for example "PepsiCo 10-K 2024 consolidated statement of cash flows dividends paid"), not with the question's wording. Always pass a non-empty `query`.
- Several companies can be searched in one turn, but search results are only leads. Each figure that enters a calculation must be seen as text for the right company and period, not as a title or URL.
- `edgar_search` and `parse_html_page` on sec.gov often return HTTP 403, and `parse_html_page` cannot read PDFs. Do not retry a 403 and do not call `edgar_search` again after one failure. Make one targeted `web_search` per missing figure and read the statement from the excerpt. You may try `parse_html_page` once on a non-sec.gov HTML copy. If it works, store it under a clear key and ask `retrieve_information` one targeted question at a time.
- Cite only URLs that appeared in tool output. Say whether each figure came from an opened filing or a search excerpt.
- Do arithmetic on unrounded numbers, re-check it once, and round only the final result.
- Write the answer as plain text with no raw citation tags. Once the figures are in hand and re-checked, call `submit_final_result` right away.
</file>

<notes>
Motivating moment: base1 issued six searches in one turn, then submitted from excerpts. It computed payout as DPS ÷ EPS and mixed bases: KDP used dividends paid per share against GAAP EPS depressed by impairments, PEP used a per-share figure of declared vs. paid uncertain, and it leaned on a third-party "payout ratio" field. It never opened a filing or used the cash-flow dividends / net income lines. It also left raw cite tags in the answer, and the ranking flipped between GAAP and adjusted bases (KDP first vs last) with no principal definition. Added: a skill (triggered from systemprompt) fixing the peer set up front, one consistent primary definition (cash-flow dividends paid ÷ net income attributable to common), a DPS/EPS cross-check, adjusted ratios as labelled secondary, and re-check/answer contract. tool_guidance was added to require seen-text figures per company, 403 fallback, and a clean-text answer. No task-specific figures are embedded because none were read from opened filings.
</notes>