<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. Use edgar_search with company and date filters, not the question's wording. If web_search returns 0 results, retry once with a short non-empty query (never an empty or null one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (clear key), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP basis in the retrieved text. Use input_character_ranges on long filings.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K exhibit.
- Quote every input to a calculation from retrieved text, then re-check each against that text before submitting. Carry full precision and round only the final figure. If a retrieval output is cut off or you are relying on a figure you did not see in full, re-retrieve it with a narrower question.
- Cite only documents you opened and retrieved from. Do not list a PDF, proxy or other filing seen only in search results, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text with no citation markup. Lead with the headline answer to the question asked, then the inputs (period, unit, source), the calculation, and any labelled alternate view. Submit with submit_final_result as soon as the figures are verified.

Leads for this task (Uber FY2024 revenue growth, take rate vs volume; re-confirm in the opened text):
- Source: Uber FY2024 10-K, https://www.sec.gov/Archives/edgar/data/1543151/000154315125000008/uber-20241231.htm (filed 2025-02-14). Item 7 holds the consolidated and segment tables. In this task a prior run retrieved: Gross Bookings $137,865M (2023) and $162,773M (2024); Revenue $37,281M and $43,978M. Segment revenue: Mobility 19,832 to 25,087, Delivery 12,204 to 13,750, Freight 5,245 to 5,141. Annual segment Gross Bookings are not printed; they are quarterly sums.
- The 10-K MD&A says business model changes in some countries classified certain sales and marketing costs as contra revenue, reducing 2024 revenue; the prior run recorded $863M (Mobility) and $713M (Delivery). Re-retrieve these exact amounts and their wording before using them, because that retrieval output was truncated.
- In this task, reported take rate (Revenue / Gross Bookings) was about flat, 27.04% to 27.02%. The question's "take-rate expansion" answer therefore depends on whether the contra-revenue effect is adjusted out, so show both bases.
</file>

<file path="skills/growth_driver_decomposition/SKILL.md">
---
name: growth_driver_decomposition
description: Split a revenue (or similar) change into a volume effect and a rate effect, such as take rate times gross bookings, price times units, or yield times balances, and report each driver's share of the growth.
---
ANALYTIC MOVE: decompose. Result = Rate x Volume, so the change in the result is the sum of a volume effect and a rate effect.

1. Define the terms from the company's own filing. Volume is the company's volume metric (e.g. Gross Bookings, units, volume). Rate = result / volume (e.g. take rate = revenue / gross bookings). Retrieve both years of the volume and the result from the same document, with units, and note any constant-currency vs reported difference. Use reported figures in the calculation.
2. State the formula before computing, and use one formula that sums exactly:
   - Volume effect = (Volume1 - Volume0) x Rate0
   - Rate effect = (Rate1 - Rate0) x Volume1
   - Check that the two effects sum to the total change.
   - Share of growth = effect / total change. Shares can exceed 100% or be negative when the rate fell.
3. Compute at full precision and round only the final percentages and amounts. Show the rates to at least two decimals in percent, and the rate change in bps.
4. Adjustments. If the filing says a reclassification, business-model change, acquisition or one-off distorted the rate, retrieve its disclosed amount and its wording. Compute the headline on reported figures, then add a second view labelled as adjusted, stating what was added back and to which year. Do not blend the two views, and say plainly that the adjustment is your estimate. If the filing's own narrative attributes the growth to a driver (e.g. "primarily attributable to an increase in Gross Bookings"), quote it as corroboration.
5. Answer contract: first sentence gives the direct answer (the share from rate vs volume, and which view it is); then inputs with period, unit and source; the formula and arithmetic; the labelled alternate; sources limited to documents opened.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks how much of a change in revenue or another result came from a rate (take rate, price, margin, yield) versus volume, call load_skill with `growth_driver_decomposition`.

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
Motivating moments in base1: it listed the ARS PDF as a source though it never opened it (same sourcing flaw seen in the q44/q45/q47/q48 library entries), so tool_guidance now carries the cite-only-opened rule. It also issued a null-query web_search after an empty first search, which the new guidance forbids. The contra-revenue amounts ($863M/$713M) entered the adjusted calculation from a retrieval output that was truncated, so I added a rule to re-retrieve any figure not seen in full, and the task lead says to re-confirm those amounts.

The main figures (GB 137,865 to 162,773; revenue 37,281 to 43,978) came from one retrieval of the 10-K and were internally consistent. I recorded them as labelled leads. The run's reported-vs-adjusted decomposition was sound but ad hoc, so I added a small on-demand skill for rate-vs-volume splits, with its trigger in systemprompt.md. It fixes one formula that sums exactly, requires a headline-first answer, and requires an adjusted view that is labelled separately and not blended with the reported one.

The task lead notes that the reported take rate was flat, so the answer depends on whether the contra-revenue effect is adjusted out. The skill and the lead therefore ask for both views.
</notes>