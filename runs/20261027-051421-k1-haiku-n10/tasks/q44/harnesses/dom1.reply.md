<file path="skills/operating_kpi_lookup/SKILL.md">
---
name: operating_kpi_lookup
description: Retrieve a company-reported operating metric (e.g. average nights per booking, ADR, nights booked, by region or segment) for a fiscal year from the primary source, with label, period and definition verified.
---
# Operating KPI by region / segment, for one fiscal year

ANALYTIC MOVE: look up (or derive) a single company-defined KPI for a named segment and period. Inputs: company, exact metric label, segment, fiscal year. Result: one figure with units, its period, and its source document.

1. Find the governing document. A company-defined KPI lives in the company's own filings and releases, not in aggregator sites (Backlinko, Wallstreetzen, Radical Storage and similar).
   - Candidates: the 10-K "Key Business Metrics" and MD&A sections and segment or geographic notes; the Q4/full-year 8-K earnings release (Ex. 99.1); the shareholder letter; the Q4 financial or investor deck on the IR site.
   - A search-result excerpt is a lead, not a verified figure. Open the document with parse_html_page or retrieve_information and read the table row yourself before citing it.
2. Verify the label, period and segment before quoting.
   - The label must match the question exactly. "Average nights per booking" is not "average length of stay", "nights and seats booked" or "ADR".
   - The period must be the full fiscal year asked, not a quarter, and not the prior-year comparative column. Read the column header.
   - Confirm the region definition. Company regions (e.g. North America, EMEA, Latin America, Asia Pacific) must match the question's wording.
   - Check footnotes for scope exclusions (e.g. "excluding Experiences") and quote them.
3. If the metric is not disclosed directly, derive it from disclosed components (e.g. nights booked ÷ bookings, or gross booking value ÷ ADR) for the same region and period. Show the arithmetic unrounded and state the units of each input (thousands vs millions). Say plainly that the figure is derived.
4. Run a consistency check. The segment figure should sit plausibly against the company-wide figure and the other regions in the same table. Where two sources disagree, prefer the primary filing and name the discrepancy.
5. Answer contract:
   - the figure with units and fiscal-year period;
   - the document and table it came from;
   - the company-wide figure and prior year, if shown, as context;
   - sources listed as URLs of documents actually opened.
   - If the figure rests only on a search excerpt or aggregator, say so explicitly in the answer.

Task fact (Airbnb, FY2024 average nights per booking, Asia Pacific): in the first run, the value 3.3 came only from a search excerpt of Airbnb's Q4 2024 financial deck (s26.q4cdn.com ... doc_financials/2024/q4/...pdf) and aggregators. It was not confirmed in a primary document the agent opened. Treat 3.3 as an unverified lead. Open the Q4 2024 deck, shareholder letter or 10-K, confirm the Asia Pacific row and the 2024 column, and only then cite it.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks for a company-reported operating metric (nights per booking, ADR, bookings, users, etc.) for a region, segment or fiscal year, call load_skill with `operating_kpi_lookup` before answering.

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
Motivating moment: base1 ended after one search; it quoted 3.3 for Asia Pacific (plus other regions' numbers) from search excerpts and aggregators, admitting it never opened the Airbnb document. Nothing verified the row, the 2024 column, or the label. I added an on-demand skill, operating_kpi_lookup, covering where company-defined KPIs live, label/period/segment verification, derivation when a KPI is not disclosed directly, and an answer contract. I recorded the Airbnb fact as an unverified lead only, since the evidence does not establish it from a primary document. The systemprompt change is one trigger line, and the skill costs nothing until it is invoked.
</notes>