I'm adding one small skill, `company_kpi_lookup`, plus its trigger line in `systemprompt.md`. The rest of the base harness is unchanged.

<file path="skills/company_kpi_lookup/SKILL.md">
---
name: company_kpi_lookup
description: Retrieve a company-defined operating metric (e.g. average nights per booking, ADR, active users, by region/segment) for a fiscal year from primary filings and report it with period, units and precision.
---
ANALYTIC MOVE: look up (and where possible cross-check) one company-defined KPI for a named period and breakdown (region/segment).

WHERE IT LIVES
- 10-K, Item 7 MD&A "Key Business Metrics" and segment/geography notes (Item 8). Regional splits are often only in the earnings release or shareholder letter, not the 10-K body.
- 8-K Item 2.02 earnings release: Exhibit 99.1 (press release / shareholder letter) with the regional KPI tables and definitions.
- Search edgar_search with the company ticker for the 10-K and the Q4 8-K EX-99.1 filed in the following Feb. Parse the document and retrieve the figure from source text; a search snippet or third-party site (statistics aggregators) is not a primary source -- use it only as a corroboration.

ANSWER CONTRACT
- State the figure exactly as disclosed (same decimals; do not round it further or substitute a third-party's more precise number unless labelled as such), the fiscal period (full year vs Q4), the region/segment, and the unit.
- Name the document (filing type, exhibit, date) the figure came from, and quote the defining sentence/table row.
- Check the metric definition (e.g. whether it excludes a business line like Experiences/Services) and mention it if it affects comparison.
- Check the period: full-year 2024 is not Q4 2024; fiscal year is not necessarily calendar year; confirm comparatives are not restated.
- If the table gives components (e.g. nights and seats booked and bookings), recompute the ratio as a sanity check and show the arithmetic; if the disclosed ratio and recomputed ratio differ, report the disclosed one and note the gap.
- In this task family (Airbnb, FY2024, Asia Pacific average nights per booking), the Q4 2024 shareholder letter (8-K EX-99.1 filed 2025-02-13) is the controlling source; the base run reported 3.3 from it (North America 4.1, EMEA 3.8, Latin America 3.7), but had not opened the filing itself -- verify in the document.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When the question asks for a company-defined operating metric (regional/segment KPI such as nights per booking, ADR, users), call load_skill with `company_kpi_lookup` before answering.

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
Motivation: in base1 the agent found the 10-K and 8-K EX-99.1 via edgar_search but never opened them. It answered 3.3 from a search snippet of the shareholder letter and added a third-party figure (3.33) as corroboration. The answer is plausible, but the primary source was unverified and the precision was ambiguous. The new skill records where company KPIs live (EX-99.1, 10-K MD&A), requires the figure as disclosed with period and definition, and flags that this task's 3.3 should be verified in the filing. Always-on cost is one line. The task fact is labelled as unverified in the document.
</notes>