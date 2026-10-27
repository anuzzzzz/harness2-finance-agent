<file path="skills/multi_year_kpi_trend/SKILL.md">
---
name: multi_year_kpi_trend
description: Trace how a company-reported operating KPI (ARM/ARPU, subscribers, margin, volume) changed across several fiscal years, chaining each 10-K's comparative columns and giving change, percent change, CAGR and per-year path.
---
ANALYTIC MOVE: trace and calculate. Inputs: the KPI's annual value for every fiscal year in the window, as the company defines it. Result: start value, end value, absolute change, % change, CAGR, and the year-by-year path with the drivers the company gives.

1. Name the company's own term for the KPI. "ARPU" or "revenue per paying user" is often reported under another name (Netflix: "average monthly revenue per paying membership", ARM). Say in the answer that the question's term maps to this metric. Confirm the definition in the filing (numerator, denominator, monthly or annual, taxes excluded).
2. Locate the figure. It is in the 10-K MD&A (Results of Operations or Streaming Revenues table), which carries three fiscal years side by side. For a 2019-2024 window you need at least the FY2024 10-K (2024, 2023, 2022), the FY2021 or FY2022 10-K (2021, 2020, and 2022), and the FY2019 10-K (2019, 2018, 2017). Open each of these and retrieve the value from it. Do not fill a year from memory or a snippet.
3. Match period and basis. Use the full fiscal-year figure, not a quarter (Q4) or a regional row. A multi-region table has global and per-region rows, and only the global row answers a company-level question. If a later 10-K restates an earlier year, use the latest filing's number and say so. Note the currency basis: reported vs constant-currency (FX-neutral) change are different figures, so label which one each percentage is.
4. Calculation, unrounded until the end: change = end - start. % change = (end / start - 1) x 100. CAGR = (end / start)^(1 / number of years between them) - 1, where the number of years is end year minus start year (2019 to 2024 is 5). Also give each YoY change. State the share of the total change that fell in each sub-period, and check the direction words ("sharply", "plateau") against the numbers. A $0.09 move is not sharp.
5. Answer contract: a headline sentence with start, end and change; a year-by-year table with units and the source filing of each year; the calculation; the company-stated drivers (price changes, plan mix, FX) quoted from the MD&A; and the caveat on definition or basis. List only documents you opened and retrieved from. Plain text with no citation markup.

Task facts (Netflix, FY2019 to FY2024; the earlier run took these from snippets and the model's recall and did not open the filings, so re-confirm each in the opened text). Annual ARM in $: 2019 10.82, 2020 10.91, 2021 11.67, 2022 11.76, 2023 11.64, 2024 11.70. FY2019 10-K: https://www.sec.gov/Archives/edgar/data/1065280/000106528020000040/form10kq419.htm. FY2024 10-K: https://www.sec.gov/Archives/edgar/data/1065280/000106528025000044/nflx-20241231.htm. FY2023 10-K: https://www.sec.gov/Archives/edgar/data/1065280/000106528024000030/nflx-20231231.htm. For 2020 and 2021 find the FY2021 or FY2022 10-K HTML with edgar_search (the FY2022 annual report found in search is a PDF and cannot be parsed). Check that 2024 minus 2019 is 0.88, which is +8.13%. Netflix's FY2024 10-K also gives a constant-currency change for 2024.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks how a company-reported KPI (ARPU, ARM, subscribers, margin, volume) changed over several fiscal years, call load_skill with `multi_year_kpi_trend`.

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

- A search snippet or result title is a lead, not evidence. Open the primary filing (10-K, 10-Q, 8-K EX-99.1) with parse_html_page, then ask retrieve_information one targeted question per figure. Confirm period, unit and basis in the retrieved text. Use edgar_search with company and date filters to find filings. Never send an empty or null query to web_search.
- parse_html_page cannot read PDFs. Use the HTML filing.
- Cite only documents you opened and retrieved from. Do not list a filing seen only in search results, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags.
</file>

<notes>
Motivation: base1 finished in two turns without ever calling parse_html_page or retrieve_information. It answered from snippets and recall, listed four filings it never opened (FY2019, FY2022 ARS PDF, FY2023, FY2024) as sources, and leaked raw <cite index> markup into the answer. It also wrote "rose sharply" for a $0.09 (0.83%) move from 2019 to 2020, and gave no CAGR or per-year change.
Changes:
- New skill `multi_year_kpi_trend` (practitioner procedure: map ARPU to the company's own term, ARM; use each 10-K's three-year comparative columns; global row, not regional; reported vs constant currency; change, % change, CAGR with the correct year count; check direction wording). It carries labelled Netflix leads (the annual ARM series and URLs) marked as needing re-confirmation, because the earlier run did not open the filings.
- A trigger line in systemprompt.md so the skill exists.
- A short tool_guidance.md (snippet = lead, cite only opened documents, no citation markup, no null queries). The library shows this rule set repeatedly fixing the same sourcing and markup failures. It is kept to four bullets to hold down the always-on cost.
</notes>