<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks for free cash flow, FCF margin, or another cash-flow ratio (CFO minus capex, over revenue) and its trend across several fiscal years, call load_skill with `fcf_margin_trend`.

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

- Before searching, fix the company, form (10-K / 8-K Exhibit 99.1), and fiscal years. Search with company, form, year and the line item name. Always pass a non-empty `query`; a null query returned unrelated results.
- `edgar_search` and `parse_html_page` on sec.gov returned HTTP 403 in this environment (the Zillow run hit both). Do not retry a 403 and do not call `edgar_search` again after one failure. Use `web_search` with company, form, year and table name; excerpts often quote the table and give the sec.gov URL. `parse_html_page` cannot read PDFs.
- If a non-sec.gov HTML page carries the statements (in this task, `https://stockanalysis.com/stocks/zg/financials/cash-flow-statement/` parsed successfully), store it under a clear key and ask `retrieve_information` one targeted question at a time. Treat such a page as a lead: say it is a third-party data set, and confirm each key figure (period, units, continuing vs total operations) against a filing excerpt when one is reachable.
- Cite only URLs that appeared in tool output. State in the answer whether each figure came from an opened filing, a search excerpt, or a third-party data page. Do not call a figure "verified" unless you saw it in filing text.
- Do arithmetic on unrounded numbers, re-check it once, and round only the final result. Once the figures are in hand, call `submit_final_result` right away.
- Write the answer as plain text with no raw citation tags.
</file>

<file path="skills/fcf_margin_trend/SKILL.md">
---
name: fcf_margin_trend
description: Compute free cash flow (CFO minus capex) and FCF margin over several fiscal years and describe the trend.
---

# FCF margin trend over several fiscal years

**Analytic move:** retrieve three inputs per year (CFO, capex, revenue), calculate FCF and FCF ÷ revenue, then describe direction year by year.

**Procedure**
1. Fix the years the question names and the definition it gives. "Approximate FCF as CFO − capex" means: net cash provided by operating activities minus purchases of property and equipment. Name the exact cash-flow line used as capex. Purchases of intangibles or capitalized software are not part of that line unless the filing combines them; if they are separate, show them only as a one-line sensitivity.
2. Get the latest filing that covers each year, preferably the one where the year appears as the most recent column, and note any restatement. A 3-year cash-flow statement in the FY2024 10-K covers FY2022–FY2024 in one table; if unreachable, use the FY2023 10-K (FY2021–FY2023) plus FY2024 results (8-K Exhibit 99.1 or 10-K).
3. Revenue must be on the same basis as the cash flows. Check whether discontinued operations are excluded from revenue but included in CFO (cash-flow statements often are not split). If so, the earliest year's margin can be distorted. Give the number as computed, name the cause, and show the margin change between the later years separately.
4. Record units (thousands vs millions) and check each figure's period before use. Do not take a third-party data page's precomputed FCF or margin as an input; recompute from CFO, capex and revenue, and use the page's values only as a cross-check.
5. Recheck before submitting: FCF = CFO − capex for each year, margin = FCF ÷ revenue, and the stated trend direction matches the numbers.
6. Answer contract: a per-year table (CFO, capex, FCF, revenue, margin to two decimals), the trend in words with percentage-point changes between consecutive years, any distortion flagged, and each figure's source (opened filing, search excerpt, or third-party page).
</file>

<notes>
Moments in base1: edgar_search 403 and the null-query web_search at turn 1-2, parse_html_page 403 on the 10-K at turn 2, and a final answer that listed 10-K URLs that never opened, with FY2022 revenue taken from a third-party history and no disclosure of that. The skill covers the multi-step FCF trend procedure and the Zillow Offers discontinued-operations distortion (FY2022 CFO 4,504 against continuing revenue 1,958, a 224% margin). tool_guidance gives a bounded 403 fallback, the stockanalysis page that parsed in this task, and a requirement to state each figure's source type. A trigger line in systemprompt.md names the skill. I did not store the final numbers as facts, because the runs did not read them from filing text.
</notes>