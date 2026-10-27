<file path="skills/interest_rate_sensitivity_net_income/SKILL.md">
---
name: interest_rate_sensitivity_net_income
description: Estimate the dollar and percent effect on net income (or net loss) if a company's debt were refinanced at a higher or lower interest rate, using the debt note, income statement and tax line from the 10-K.
---
ANALYTIC MOVE: calculate, then compare. Inputs are (a) total debt at fiscal year-end, (b) the rate shift in percentage points, (c) the tax treatment and (d) the reported net income or loss. Result: the incremental annual interest in dollars, the new net income, and the % change.

1. The shift is additive, so the current rate is NOT needed. Incremental pre-tax interest = total debt x shift (3 points = 0.03). Do not pull a third-party "weighted-average rate" (WACC pages, stock-analysis sites). It is not a filing figure and it does not change the incremental amount. If you show the implied current rate for context, label it as derived: interest and debt expense / debt, and say which.
2. Debt base. Open the 10-K debt note and the MD&A liquidity section and retrieve total debt at year-end including the short-term portion and current maturities. The MD&A usually says "debt balances totaled $X". Check whether the note total and any capital-resources table (principal vs carrying value) differ. Use the carrying-value total as the base and show the other figure as a sensitivity if it differs. State the year-end date.
3. Net income base. Retrieve from the income statement: net income or loss, net income attributable to the parent, and income tax expense or benefit and pre-tax result. Use "attributable to [company] shareholders" as the headline net income and name the choice. Units are usually $ millions.
4. Tax. Give two lines: (a) pre-tax impact = debt x shift; (b) after-tax impact = pre-tax x (1 - tax rate). Take the tax rate from the 10-K. Use the statutory 21% as a labelled alternative if the effective rate is distorted (a loss, a valuation allowance, a tiny benefit). Never take the tax rate from an unopened or third-party page. Lead with the simplest reading of the question (debt x shift against reported net income) and give the after-tax figure as a clearly labelled second.
5. Sign handling. If the company reported a net LOSS, the extra interest makes the loss larger. New result = reported - impact (for example -11,817 - 1,616 = -13,433). Percent = impact / |reported| x 100, expressed as "the loss grows by X%". Say whether a positive or negative percent is meant. Do not report a bare "-13.67%" without saying what it means.
6. Caveats, one line each: the full-year effect assumes all debt reprices on day one (in reality it reprices only as it matures or is refinanced); fixed-rate debt is not repriced until maturity; capitalized interest and interest income are ignored.
7. Answer contract: debt base with date and source; shift; the dollar impact (pre-tax, and after-tax if shown); the reported net income or loss; the new net income or loss; the % change with its sign convention; the arithmetic unrounded until the end; sources limited to documents actually opened and retrieved from. Plain text, no citation markup.

Task facts (Boeing FY2024 10-K; the earlier run retrieved these, so re-confirm in the text). The 10-K is https://www.sec.gov/Archives/edgar/data/12927/000001292725000015/ba-20241231.htm (about 477K characters; use targeted retrievals).
- Net loss attributable to Boeing shareholders: $(11,817)M. Total net loss: $(11,829)M. Net loss attributable to common shareholders: $(11,875)M after $58M of preferred dividends.
- Interest and debt expense: $2,725M in 2024 (2,459 in 2023).
- MD&A: "debt balances totaled $53.9 billion" at Dec 31, 2024, of which $1.3 billion short-term. The debt note gives total debt of $53,864M. The Capital Resources table shows $54,369M for long-term debt including the current portion. Resolve which is carrying value and which is principal.
- The 10-K does not disclose a weighted-average rate. The debt note gives only coupon ranges by category.
- Pre-tax increment on $53,864M x 3% = $1,615.92M. Against $11,817M, that is 13.67%. Re-confirm the tax figures from the income statement before giving an after-tax number.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks what a change in interest rates (refinancing debt at higher or lower rates) would do to net income, call load_skill with `interest_rate_sensitivity_net_income`.

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

- A search snippet or result title is a lead, not evidence. Open the primary document (10-K, 10-Q, 8-K exhibit) with parse_html_page, then confirm each figure, period and unit with retrieve_information. Never send an empty or null query to web_search; use edgar_search with company and date filters.
- Prefer filing figures to third-party aggregator pages. If a third-party figure is used, label it as such.
- Cite only documents you opened and retrieved from. Do not list a page or spreadsheet seen only in search results, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags.
</file>

<notes>
Motivating moments in base1: (1) It used a 5.31/5.32% weighted-average rate from stock-analysis-on.net, and a 3.10% effective tax rate from an FCFF page it never opened, to answer a question where the 3-point increment does not depend on the current rate. The 10-K gives no weighted-average rate. (2) The final answer leaked raw <cite index> markup and listed unopened pages (Financial_Report.xlsx, the FCFF page) as sources. (3) It presented a percent against a negative net-income base with only a caveat; the skill sets out the sign convention. (4) It did not resolve the 53,864 vs 54,369 debt figures. The skill encodes the debt x shift calculation, the debt base, the tax and net-loss handling, and verified Boeing facts labelled as task facts. A short tool_guidance and a trigger line in systemprompt.md carry the sourcing hygiene, following the pattern in library entries q45 to q48.
</notes>