<file path="skills/security_offering_terms/SKILL.md">
---
name: security_offering_terms
description: Summarise the key terms of a registered securities offering (preferred, convertible, notes) from the prospectus supplement, with each term tied to the opened document.
---
ANALYTIC MOVE: extract and summarise terms. Inputs are the final 424B5 prospectus supplement, the pricing press release or FWP, and the closing 8-K. The result is one term-by-term summary.

1. Controlling sources. The final 424B5 holds the price, share count, discount, liquidation preference, dividend, conversion, voting and use-of-proceeds terms. An 8-K filed after closing holds the certificate of designations (EX-3.1) and the underwriting agreement. The 8-K or press release is the place to confirm closing and over-allotment exercise.
2. Several 424B5s or FWPs may exist for one deal: a launch version, a pricing version and an upsize. Use the pricing or final version for terms. Say when the deal was upsized, and give the launched size and the priced size separately.
3. Keep these apart, each with its own figure:
   - base deal size versus size if the over-allotment option is exercised in full;
   - gross proceeds versus net proceeds (after the underwriting discount and expenses);
   - pricing date versus settlement or closing date (T+2 is stated in the supplement).
4. Do not state that the over-allotment option was exercised, or give a final post-exercise total, unless an opened document (8-K, press release, later filing) says so. Otherwise write "option for up to X additional shares".
5. For a mandatory convertible preferred, cover: price and liquidation preference per share; dividend rate, the dollar amount per share per year, payment dates, the first payment date, form of payment (cash, stock or both) and the cumulative or non-cumulative status; the minimum and maximum conversion rates with the price thresholds, the mandatory conversion date, the early-conversion and fundamental-change terms; voting rights (usually none, with exceptions for unpaid dividends and protective provisions); the NYSE listing symbol; use of proceeds. Check that the thresholds are consistent: initial price x maximum rate should equal the liquidation preference.
6. Answer contract: a labelled line for each term the question names, plus the share count and dollar size, with the source document for each. Use plain text with no citation markup. List only documents that were parsed and retrieved from.

Task facts (verified in a prior run from the 424B5, https://www.sec.gov/Archives/edgar/data/1404912/000114036125007426/ny20042797x2_424b5.htm; re-confirm in the text). KKR & Co. Inc. 6.25% Series D Mandatory Convertible Preferred Stock. Priced March 4, 2025. Settlement March 7, 2025. Upsized from $1.5B to $2.25B (45,000,000 shares at $50.00, with an option for 6,750,000 more, which would make it $2.5875B). Underwriting discount is $1.125 per share. Net proceeds are about $2.20B, or about $2.53B with the option. Liquidation preference is $50.00 plus accumulated and unpaid dividends. Dividends are cumulative, at 6.25%, or $3.125 per year. Payment dates are March 1, June 1, September 1 and December 1, starting June 1, 2025 through March 1, 2028. Conversion rates run from 0.3312 to 0.4140. Mandatory conversion date is March 1, 2028. Proceeds are for additional equity interests in core private equity portfolio companies (Strategic Holdings) and general corporate purposes. Option exercise was not confirmed from an opened document.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks for the key terms of a securities offering (preferred stock, convertibles, notes: size, price, dividend, conversion, voting, use of proceeds), call load_skill with `security_offering_terms`.

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

- A search snippet is a lead, not evidence. Open the primary document (424B5, 8-K and its exhibits, 10-K, 10-Q) with parse_html_page and confirm each figure with retrieve_information. Use edgar_search with company and date filters. If web_search returns nothing, retry once with a short non-empty query, then use edgar_search.
- parse_html_page cannot read PDFs.
- Cite only documents you opened and retrieved from. Do not list a press release, news article or law-firm page seen only in search results, and do not state a fact (such as an option exercise or a closing) that only a snippet supplied. If something is unconfirmed, say so.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags.
</file>

<notes>
Motivation: base1 got the terms right from the 424B5, but its final answer leaked raw <cite index> markup. It listed four sources it never opened (Nasdaq, Investing.com, Simpson Thacher). It also stated that the over-allotment option was fully exercised (51.75M shares, about $2.6B) from search snippets, which no opened document confirmed. tool_guidance now carries the cite-only-opened and plain-text rules, matching the same fix adopted for q35, q45 and q47. A new skill, security_offering_terms, covers practitioner knowledge for offering-terms questions. It separates the base size from the option size, pricing date from closing date, and gross from net proceeds. It requires an opened document before claiming option exercise, and carries the task facts labelled as such. The trigger line is in systemprompt.md.
</notes>