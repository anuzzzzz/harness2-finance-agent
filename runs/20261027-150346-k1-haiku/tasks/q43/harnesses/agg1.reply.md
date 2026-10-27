<file path="skills/revenue_growth_volume_vs_take_rate/SKILL.md">
---
name: revenue_growth_volume_vs_take_rate
description: Split a marketplace or platform company's revenue (or similar) growth into volume (gross bookings, GMV, TPV, units) and rate/take-rate effects, with the reported-versus-adjusted reconciliation and segment mix check an analyst needs.
---
ANALYTIC MOVE: decompose. Revenue = Volume x Take rate, so the change in revenue is a volume effect plus a take-rate effect. Inputs are the company-defined volume metric and revenue for two consecutive fiscal years. The result is each driver's share of growth, plus the reasons the take rate moved.

1. Inputs from the 10-K (MD&A highlights, key metrics, segment results). Retrieve both years of volume and revenue from the same document, with units ($ millions), and note reported vs constant-currency growth. Use reported dollars in the calculation. If volume by segment is only quarterly, sum the four quarters and check the sum equals the consolidated total.
2. State the formula before computing, using one convention that sums exactly: TR0 = Rev0/Vol0, TR1 = Rev1/Vol1. Volume effect = (Vol1 - Vol0) x TR0. Take-rate effect = (TR1 - TR0) x Vol1. Check that the two sum to the revenue change. Share = effect / revenue change; shares can be negative or exceed 100%. Say the split depends on the ordering convention. Carry full precision; round only final figures. Show take rates in % to two decimals and the change in bps.
3. Reconcile reported vs underlying. Read the MD&A for non-volume items that move revenue relative to volume: business-model changes reclassifying costs to contra revenue, currency basis, acquisitions, segments with a different revenue model (e.g. freight, where revenue is about 100% of bookings). Retrieve any disclosed amount with its exact wording and re-retrieve it if the output was cut off. The headline is the reported basis. Give an adjusted view (add back the disclosed impact) as a separate labelled view, say it is your estimate, and say which year(s) it was applied to. Do not blend the two. If the filing's narrative attributes growth to a driver, quote it as corroboration.
4. Segment mix check. Compute each segment's take rate for both years (segment revenue / segment volume) and confirm segments sum to consolidated. A flat consolidated rate can hide offsetting segment moves or a mix shift; say which segment moved it.
5. Answer contract: the first sentence gives the direct answer ("X% volume, Y% take rate", reported basis) and mentions that an adjusted view is given below if material. Then inputs with period, unit and source; take rates and bps change; dollar effects and shares with the sum check; the labelled adjusted view; the segment note; sources limited to documents actually opened.

Leads for Uber FY2024 (earlier runs retrieved these; re-confirm in the opened text). Source: 10-K https://www.sec.gov/Archives/edgar/data/1543151/000154315125000008/uber-20241231.htm. Gross Bookings $137,865M to $162,773M; Revenue $37,281M to $43,978M; reported take rate about 27.04% to 27.02% (flat). The 10-K says business model changes (certain sales and marketing costs classified as contra revenue) reduced 2024 revenue by $863M (Mobility) and $713M (Delivery). No 2023 amount was found. Segment revenue: Mobility 19,832 to 25,087; Delivery 12,204 to 13,750; Freight 5,245 to 5,141. Annual segment Gross Bookings are quarterly sums only.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks how much of a change in revenue came from a rate (take rate, price, margin, yield) versus volume (gross bookings, GMV, TPV, units), call load_skill with `revenue_growth_volume_vs_take_rate`.

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

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1) and fiscal period. Use edgar_search with company and date filters, not the question's wording. If web_search returns 0 results, retry once with a short non-empty query (never an empty or null one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (clear key), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP basis in the retrieved text. Use input_character_ranges on long filings.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K exhibit.
- Quote every input to a calculation from retrieved text and re-check each against that text before submitting. If a retrieval output is cut off or you rely on a figure you did not see in full, re-retrieve it with a narrower question.
- Cite only documents you opened and retrieved from. Do not list a PDF, proxy or other filing seen only in search results, and do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text with no citation markup. Lead with the headline answer to the question asked, then inputs (period, unit, source), the calculation, and any labelled alternate view. Submit with submit_final_result as soon as the figures are verified.
</file>

<notes>
kept -> dom1 skill (revenue_growth_volume_vs_take_rate), merged with inv1's skill -> both rollouts submitted with identical correct figures; dom1's segment mix check and reported-headline convention added value (Mobility 28.79%→30.22% vs Delivery 19.15%→18.43% explained the flat take rate), inv1's re-retrieve-if-truncated and quote-corroboration points folded in; one skill instead of two to save context.
dropped -> inv1's separate growth_driver_decomposition skill -> duplicated dom1's formula and sum check; only one trigger line kept.
kept -> inv1 tool_guidance (cite-only-opened, no null-query search, PDF note, re-check inputs) -> base1 listed the unopened ARS PDF as a source and issued a null-query web_search; inv1 and dom1 (which also opened only the 10-K) did not.
revised -> inv1 task leads removed from always-on tool_guidance -> library evidence (q48) says task-specific leads carry no transfer value and cost always-on chars; a compact labelled lead stays inside the on-demand skill only.
kept -> reported basis as headline, adjusted ($1,576M add-back, 18.58% rate share) as labelled secondary -> all three runs got the same numbers (-0.58% / 81.42% / 18.58%); only the headline framing differed, and the question's wording ("take-rate expansion") is ambiguous, so both views are delivered with the reported one first.
</notes>