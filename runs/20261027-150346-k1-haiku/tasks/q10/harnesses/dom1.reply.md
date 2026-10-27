<file path="tool_guidance.md">
# Tool use

- A search snippet, result title or aggregator page is a lead, not evidence. Every figure in a calculation must be retrieved from a primary document you opened: parse_html_page on the 10-K, 10-Q or 8-K exhibit, then retrieve_information with one targeted question. Do this for the end-period figure as well as the start-period figure.
- Prefer the single filing that carries all the needed years. A 10-K income statement shows three fiscal years, so check whether the latest 10-K already covers the whole window before opening older ones.
- If web_search returns nothing, retry once with a short non-empty query. Never send an empty or null query. Use edgar_search or a known sec.gov URL instead.
- Cite only documents you opened and retrieved from. Do not list a 10-K, aggregator or spreadsheet seen only in search results, and do not attribute a figure to a section you did not read. Do not put remarks about your own memory or recollection in the answer.
- Write the final answer in plain text with no citation markup. State each figure with its fiscal period, unit and source, then the calculation, then the result.
</file>

<file path="skills/multi_year_cagr/SKILL.md">
---
name: multi_year_cagr
description: Compute a compound annual growth rate (revenue or another line) between two fiscal years from filed statements, with period count, units and sources checked.
---
ANALYTIC MOVE: calculate. Inputs are the start-year and end-year values of the same line, taken from filed statements. The result is CAGR = (End / Start)^(1 / n) - 1.

1. Period count. n = end fiscal year minus start fiscal year ("2022 to 2024" means n = 2, not 3). Confirm the company's fiscal year end, because a non-calendar fiscal year changes which statement holds each year.
2. Source of each value. Open the latest 10-K, which has three years of income-statement columns. Retrieve the start-year and end-year values from that one statement, so both use the same definitions. If the start year is outside that filing, open the earlier 10-K. If it was restated or recast, prefer the later filing's comparative figure and say so. Use total revenue from the consolidated statements of operations, not a segment or non-GAAP number, unless the question asks for one.
3. Units. Statements are usually in thousands. Keep both values in the same unit. State the unit in the answer.
4. Calculation, with no intermediate rounding. Show the ratio End / Start, the root and the result. Round only the final percentage to two decimals. Also give the total growth over the window (End / Start - 1) as a cross-check. CAGR must lie between 0 and the simple total growth. Taking the square root of the ratio when n = 2 should give the same answer as the formula.
5. Answer contract: the CAGR to two decimals; both values with fiscal year, unit and source document; n; the formula and arithmetic. Sources are limited to documents actually opened.

Task facts (Palantir Technologies, calendar fiscal year; re-confirm in the opened text). FY2023 10-K, https://www.sec.gov/Archives/edgar/data/1321655/000132165524000022/pltr-20231231.htm. Its statement of operations, in thousands, shows revenue of 2,225,012 (2023), 1,905,871 (2022) and 1,541,889 (2021); this was retrieved in an earlier run. FY2024 10-K, https://www.sec.gov/Archives/edgar/data/1321655/000132165525000022/pltr-20241231.htm. The earlier run did NOT open it and used 2,865,507 for FY2024 from outside the filing, so retrieve the FY2024 revenue from this filing's statement of operations (it also carries the 2022 comparative) before using it. If the retrieved values are 2,865,507 and 1,905,871, then CAGR = sqrt(2,865,507 / 1,905,871) - 1 = about 22.62%.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks for a compound annual growth rate (CAGR) or multi-year growth rate of a reported line, call load_skill with `multi_year_cagr`.

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
Motivating moment (base1): the run parsed only the FY2023 10-K and retrieved the 2022 revenue (1,905,871) from it. It never opened the FY2024 10-K. The FY2024 figure (2,865,507) was not retrieved from any opened document, yet the answer said the "FY2024 10-K MD&A revenue table shows this, with government at $1,569,605 and commercial at $1,295,902". It also listed the unopened FY2024 10-K and Bullfincher as sources, leaked a "my own recollection was wrong" aside into the answer, and issued a null-query search. The number (22.62%) was right, so the edits target verification and sourcing.
- tool_guidance.md: a short always-on rule that every figure, including the end-period one, must be retrieved from an opened primary document. It also says to cite only opened documents, to send no empty queries, and to keep memory remarks out of the answer. The empty file is replaced.
- skills/multi_year_cagr (plus the trigger line in systemprompt.md): holds the CAGR practitioner checks. n is end year minus start year, both values come from the same statement and unit, total revenue is used, and a sanity check against total growth is applied. It contains verified Palantir 2022 figures (retrieved in base1) and flags FY2024 as not yet retrieved from source. This is a task fact, labelled as such.
</notes>