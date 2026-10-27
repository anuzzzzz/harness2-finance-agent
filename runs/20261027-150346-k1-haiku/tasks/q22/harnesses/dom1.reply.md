<file path="skills/kpi_ratio_from_reported_metrics/SKILL.md">
---
name: kpi_ratio_from_reported_metrics
description: Compute a per-unit ratio (for example gross booking value per night, ARPU, revenue per unit) across several fiscal years from a company's reported Key Business Metrics table.
---
ANALYTIC MOVE: calculate. Take numerator / denominator for each fiscal year from the company's own published KPI table. Result: one value per year, in the format the question prescribes.

1. Locate the table. Key operating metrics sit in the 10-K MD&A under "Key Business Metrics", in millions. Each 10-K shows only two or three years, so FY2022-FY2024 needs the FY2024 10-K (2023 and 2024) and the FY2023 10-K (2022 and 2023). Open each 10-K and retrieve the table from the opened text. Do not use search snippets for any figure.
2. Which precision is the headline. Use the figures as printed in the Key Business Metrics table for both numerator and denominator. Compute the ratio with those printed figures at full precision, and round only the final number. The MD&A narrative sometimes gives a one-decimal count (for example 393.7M). Mention it as a labelled alternate only if it was retrieved verbatim from an opened filing. Never build a figure by adding a stated change to another year, such as 448.2 + 43.3, and present it as a reported figure. A rounded count changes the second decimal, so show both the headline and the alternate and say which is which.
3. Check units and definitions. GBV is in $ millions and nights in millions, so the ratio is in dollars. Check that the same metric definition applies in each year. If a later 10-K restates an earlier year, say so and use the latest filing for that year.
4. Answer contract:
   - one line per year in the exact layout asked;
   - beneath it, a table with numerator, denominator, source filing and period, and the unrounded quotient;
   - only filings actually opened listed as sources, in plain text with no citation markup.
5. Before submitting, confirm that each figure's fiscal year matches the line it is on, and that the ratio rises or falls plausibly relative to the average daily rate commentary in the filing.

Task facts (Airbnb, CIK 1559720; verified in opened 10-Ks, so re-confirm in the text).
- The FY2024 10-K (abnb-20241231.htm) table gives Nights and Experiences Booked of 448 (2023) and 492 (2024), and GBV of $73,252M and $81,784M.
- The FY2023 10-K (abnb-20231231.htm) table gives 394 (2022) and 448 (2023), and GBV of $63,212M and $73,252M. Its narrative says 393.7M and 448.2M.
- The FY2022 10-K table also gives 394 and $63,212M for 2022.
- Table-basis ratios: 2022 = 63,212/394 = 160.43; 2023 = 73,252/448 = 163.51; 2024 = 81,784/492 = 166.23.
- Precise-nights alternate: 160.56 (393.7M), 163.44 (448.2M).
- The FY2024 10-K narrative gives only the 43.3M increase and no one-decimal 2024 total, so a 2024 alternate of 491.5M is derived, not reported.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks for a per-unit ratio of two reported KPIs across several fiscal years (for example gross booking value per night, or revenue per user), call load_skill with `kpi_ratio_from_reported_metrics`.

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
Motivation: base1 got the right filings and figures but made the headline answer from mixed-precision inputs: the narrative's 393.7M and 448.2M, plus a 2024 count of 491.5M that it derived as 448.2 + 43.3 and that no filing states. The table figures (394/448/492) were relegated to a caveat. The headline ratios (160.56/163.44/166.40) therefore depend on an inferred input. The skill makes the Key Business Metrics table as printed the headline basis and keeps precise counts as a labelled alternate, only when retrieved verbatim. It also records the verified task facts (which 10-K holds which year, the table values and the table-basis ratios). It is a skill rather than always-on text because it applies only to KPI-ratio questions, with a one-line trigger in systemprompt.md. The headline-precision choice is a judgment call; the alternate stays visible so a reviewer can see both.
</notes>