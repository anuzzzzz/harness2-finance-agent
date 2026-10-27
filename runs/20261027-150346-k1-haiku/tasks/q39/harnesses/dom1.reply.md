<file path="skills/guidance_metrics_inventory/SKILL.md">
---
name: guidance_metrics_inventory
description: Answer "what metrics does company X guide on in its earnings reports" by reading the outlook section of the latest earnings release and supplemental deck, then listing each guided metric with its period, basis and latest range.
---
ANALYTIC MOVE: classify and list. Input: the company's most recent earnings release and any supplemental or investor deck filed as of the question's date. Result: the complete list of metrics the company gives forward ranges or targets for, each with its period, basis and unit.

1. Find the controlling documents.
   - Open the latest earnings release (8-K EX-99.1) for the most recent completed quarter before the as-of date. Open the supplemental or investor-update exhibit (often EX-99.2) if the filing has one.
   - Ignore filings dated after the as-of date. Search results often surface later quarters.
   - Guidance is usually in an "Outlook" or "Guidance" section, a table at the end of the release or deck, or the CFO prepared remarks. Do not infer the list from news snippets or the earnings-call Q&A, since journalists report only the headline items (usually EPS).
2. Build the list by asking retrieve_information for every guided line: "list every forward-looking metric in the outlook or guidance section, with its period (next quarter or full year), range, and whether it is GAAP or adjusted". Ask a second time for items the first answer may have missed. Common categories are revenue or revenue growth, capacity or volume, unit costs, margin, fuel or other key input prices, EPS, non-operating items, tax rate, capital expenditure, free cash flow, and leverage or debt targets.
3. Separate the metrics into three groups.
   - Next-quarter guidance (the quarterly outlook table).
   - Full-year guidance (often a different set, for example free cash flow, capex and leverage appear only for the year).
   - Longer-term targets (multi-year, investor-day items). Label each metric with its group.
4. Record for each metric: the exact name as the company writes it, the unit (percent change versus the prior-year period, cents or dollars per share, $ per gallon, $ billions), the GAAP or adjusted basis, and the range. Keep "year over year growth" separate from "absolute level". Never convert or restate a range.
5. Do not mix periods. A quarter guided in January is not the same as a full year guided at the same time. If the question is generic ("what does it guide on"), give the structure (the full list) first, then the latest ranges as illustrations, labelled with the date of the release they came from.
6. Consistency checks before submitting.
   - Each metric you list was seen in the opened text. If you add one from another source (a transcript, a prior-year deck), say which document and mark it as not in the latest release.
   - If the release and the deck disagree on the metric list, report both and say which is more recent.
   - Do not claim that a metric is not guided unless you searched the outlook table and the remarks and found nothing. Say "not found in the opened documents" instead.
7. Answer contract: a headline sentence; a table or list of metrics grouped as quarterly, full-year and longer-term, each with unit, basis and latest range with its period; the release and date; and sources limited to documents actually opened and retrieved from. Write plain text with no citation markup.

Task leads (Delta Air Lines, NYSE: DAL; taken from search results only, so confirm in the opened text). The December-quarter 2024 earnings release is likely https://www.sec.gov/Archives/edgar/data/27904/000168316825000182/delta_ex9901.htm (filed January 2025, the latest before April 7, 2025). The January 2024 supplemental deck is https://www.sec.gov/Archives/edgar/data/27904/000168316824000244/delta_ex9902.htm, which is the prior-year version and not the latest. Check whether the January 2025 filing has its own EX-99.2 deck or investor-update exhibit. Do not use filings dated after April 7, 2025 (for example the one that reports the March 2025 quarter). Earlier snippets suggested the guided items include revenue growth, operating margin, EPS, capacity, non-fuel unit cost, fuel price per gallon, free cash flow and leverage. That list is not yet verified in opened text, so confirm each one and add any that appear (for example non-operating expense or tax rate).
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks which financial metrics a company guides on or provides outlook for in its earnings reports, call load_skill with `guidance_metrics_inventory`.

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

- A search snippet or result title is a lead, not evidence. Open the primary document (8-K EX-99.1 or EX-99.2, 10-Q, 10-K) with parse_html_page, then confirm each figure and list with retrieve_information. Never send an empty query.
- Cite only documents you opened and retrieved from. Do not cite or lean on filings dated after the as-of date.
- Write the final answer in plain text with no citation markup such as <cite> tags.
</file>

<notes>
Motivation: base1 never opened any document. It answered from web_search snippets about Delta's guidance. It mixed a January 2024 deck (prior year) with January 2025 call commentary. It listed fuel and free cash flow/leverage as "confirmed for the 2024 deck" without opening it. It listed unopened sources, and the snippets carried markup artifacts. The question is a "what metrics" inventory, so the practitioner knowledge is where guidance lives (the outlook table of the latest release or deck as of the date) and how to group it (quarterly, full-year, long-term), plus state basis and units. Added an on-demand skill with a trigger line in systemprompt.md. The Delta URLs are labelled leads, not verified facts: they appeared in search results but no run opened them. The always-on tool_guidance is kept to three short sourcing lines drawn from earlier library entries (q45 to q48 pattern: snippets are leads, cite only opened documents, no citation markup), so the always-on cost stays small.
</notes>