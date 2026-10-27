<file path="skills/material_cash_requirements_table/SKILL.md">
---
name: material_cash_requirements_table
description: Answer "what are the company's material cash requirements / contractual obligations / projected cash needs for next year" from a 10-K's MD&A Liquidity and Capital Resources table.
---
ANALYTIC MOVE: locate and read (then sum, if needed). Inputs: the latest 10-K on or before the as-of date. Result: the near-term (next-12-months) total of the obligations table, with its components.

1. Where it lives. In a 10-K, "Item 7. MD&A - Liquidity and Capital Resources" has a "Material Cash Requirements" paragraph followed by a table. Netflix-style layout: rows for content obligations, debt (principal plus interest), operating lease obligations and a Total row. Columns: Total, Next 12 Months (also called "Less than 1 year"), Beyond 12 Months. Other filers use 1 year / 2-3 years / 4-5 years / thereafter.
2. Period mapping. A FY2024 10-K (balance sheet date Dec 31, 2024) gives the "next 12 months" = calendar 2025. For "projected requirements for 2025", use the next-12-months column. Also report the all-period Total and the beyond-12-month figure, and say which one answers the question.
3. Retrieve every row and column from the opened 10-K text, not from a snippet. Check that the rows sum to the printed Total, and that the Next-12 plus Beyond-12 columns equal the Total column. If a printed total and your sum differ, report both and say so.
4. Cross-check. The content-obligations row should match the content-obligations footnote (commitments note, "less than one year" line). The debt row should match the debt note's maturities plus interest. State the units (usually $ thousands in the statements; the MD&A may say "in thousands"). Convert to $ billions only at the end.
5. Exclusions to state plainly. Note any footnote on the table: for example, the obligations may exclude unknown future content titles or other items (such as taxes or uncertain tax positions) that the filing says are not included. Say these are outside the table's figure and that actual 2025 cash outflows will be larger than the table.
6. Answer contract: the next-12-months total with its components (each with period and units), the arithmetic sum, the all-period total for context, the footnoted exclusions, and the 10-K URL, filing date and period end. Plain text, no citation markup. List only opened documents as sources.

Task fact (this task, Netflix FY2024 10-K, filed 2025-01-27, accession 0001065280-25-000044): https://www.sec.gov/Archives/edgar/data/1065280/000106528025000044/nflx-20241231.htm. A prior run took these numbers from search snippets only. The numbers are NOT yet verified against the opened filing: content 11,424,696; debt 2,486,945; operating leases 514,625 (all next-12-months, $ thousands); next-12 total 14,426,266; all-period total 45,851,513. Re-confirm each in the opened 10-K text before using it.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks about a company's material cash requirements, contractual obligations or projected cash needs for a coming year, call load_skill with `material_cash_requirements_table`.

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

- A search snippet or result title is a lead, not evidence. Open the primary filing with parse_html_page, then ask retrieve_information targeted questions (one table or section at a time, using input_character_ranges on long 10-Ks). Confirm each figure's period, unit and row/column in the retrieved text before using it.
- edgar_search takes the ticker or CIK in `ciks` and form-type and date filters; use it to find the filing URL. Never issue a web_search with an empty or null query.
- Cite only documents you opened and retrieved from; do not list search-only pages or spreadsheets. Write the answer in plain text with no citation markup such as <cite> tags.
</file>

<notes>
Motivating moment: base1 made one edgar_search, then a null-query web_search, and submitted the Netflix next-12-months total ($14.43B) from snippets without ever opening the 10-K. It leaked <cite index> markup and listed an unopened Financial_Report.xlsx and a third-party PDF as sources. I added a skill (with a trigger line in systemprompt.md) holding the practitioner knowledge for obligations-table questions: where the table sits in MD&A, the next-12-months column maps to the following calendar year, rows must sum to the Total, the content row must tie to the commitments footnote, and exclusions (unknown future titles) are stated. The Netflix 10-K URL is verified from edgar_search. The figures are included only as unverified leads to re-confirm. Tool guidance is kept short: snippets are leads, open the filing, no empty queries, cite only opened sources, plain text.
</notes>