<file path="tool_guidance.md">
# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1), fiscal period. Use edgar_search with company and date filters, not the question's wording. If web_search returns 0 results, retry once with a shorter query, then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (store it under a clear key, one per company), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP basis in the retrieved text. Use input_character_ranges on long filings rather than re-reading everything.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K EX-99.1 instead.
- Prefer the annual 10-K for full-year figures. If a figure is a sum of quarters or a derived quantity, say so and cross-check it against an annual figure in the same or another opened document.
- Multi-company comparisons: apply the same definition and basis to every company, and retrieve each company's inputs from its own filing before computing.
- Cite only documents you opened and retrieved from. Do not list a filing as a source, or attribute a figure to it, unless you retrieved that figure from it.
- Write the final answer in plain text with no citation markup. State each figure with its period, unit and source, then the calculation, then the result in the form the question asks for. Submit with submit_final_result as soon as the figures are verified in primary text.
</file>

<file path="skills/peer_payout_ratio_compare/SKILL.md">
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
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks you to compare or rank a company's dividend payout ratio (or a similar ratio) against its competitors, call load_skill with `peer_payout_ratio_compare`.

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
Motivating moment: base1 made five web_search calls and submitted without ever calling parse_html_page or retrieve_information. Every input came from search snippets, yet it listed 10-Ks, 10-Qs and press-release PDFs as sources. It also left basis and peer set implicit. Its GAAP and adjusted bases gave opposite orders, and it dropped Monster and National Beverage with only a caveat.

Edits:
- tool_guidance.md: snippet-is-a-lead rule, open each 10-K, cite only what was opened, PDF caveat and a multi-company same-basis rule. This follows the adopted q44/q45 pattern.
- New skill peer_payout_ratio_compare, triggered by a line in systemprompt.md. It fixes the peer set first, uses one definition and basis for all companies, cross-checks with cash dividends paid / net income, and lists excluded peers. The base run's figures are included only as unverified leads, and PepsiCo's 10-K was never opened.
</notes>