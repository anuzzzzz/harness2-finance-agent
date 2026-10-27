I made two edits, based on one base rollout. It answered about $3.30B ($3.25B plus the $50M adjustment) from a single Q1 2025 10-Q retrieval. It never opened the Feb 28, 2025 closing 8-K or the filing's acquisition note, and the question asks for consideration "measured at transaction close". It also leaked `<cite>` markup and listed filings it had not opened. Nothing here has been checked against a primary filing beyond what the base run retrieved.

<file path="skills/deal_consideration_at_close/SKILL.md">
---
name: deal_consideration_at_close
description: Determine the total consideration an acquirer paid for acquired businesses as measured at closing (headline price vs. closing-date value, cash vs. equity, adjustments), from the closing 8-K and the acquirer's periodic filings.
---
ANALYTIC MOVE: reconcile. Inputs: the headline price in the agreement, the closing-date settlement (cash, equity units issued, assumed debt, purchase-price adjustments), and the accounting basis. Result: one consideration figure at close, plus the bridge from the headline.

1. Separate three numbers and never blur them: (a) headline price at signing; (b) adjustments settled at closing (working capital, volume-weighted-price true-ups); (c) consideration measured at close, meaning cash plus the value of equity issued at the closing-date price, plus any assumed debt or contingent items. Say which one the question asks for.
2. Controlling sources, in order: the closing 8-K (Item 2.01 completion of acquisition, Item 3.02 unregistered share issuance, and any EX-99); the acquirer's next 10-Q or 10-K acquisition or business-combination note (consideration table, purchase price allocation); the subsequent-events note in the 10-K if the close came after year-end. Open at least the closing 8-K and the note, not only the MD&A summary.
3. Equity component: units or shares issued x the price the filing states at close (or the closing-date market price in the note). Show the multiplication. Do not substitute the signing-date price.
4. Check the accounting basis. If the deal was between entities under common control, the filing may record it at historical carrying amounts. Then state both the contractual consideration and the recorded amount, and say which the question's wording points to.
5. If a filing gives a headline figure and a separate adjustment, show the sum (for example headline + adjustment) and say whether the adjustment was settled in cash or units. Say explicitly when the filing does not say.
6. Check units ($ millions vs. billions), and that any shares issued to a third party (for example a licensor) are either included or explicitly excluded with a reason.
7. Answer contract: headline sentence with the figure; the bridge (headline, adjustments, closing value) with the period and date of each; the calculation; the accounting-basis caveat; sources limited to documents opened and retrieved from. Plain text, no citation markup.

Task facts (TKO Group, acquisition of Endeavor's PBR, On Location and IMG businesses; from one earlier run's retrievals, so re-confirm in the text). TKO Q1 2025 10-Q https://www.sec.gov/Archives/edgar/data/1973266/000095017025067220/tko-20250331.htm states total consideration of approximately $3.25 billion plus a $50 million purchase price adjustment. It also states that on Feb 28, 2025 about 26.54 million TKO OpCo common units and an equal number of Class B shares were issued to Endeavor. The 10-Q did not state a closing-date fair value, so look in the closing 8-K (filed 2025-02-28, accession 0001193125-25-040879) and the 10-K's acquisition and subsequent-events notes for a closing-date measure. The FY2024 10-K is https://www.sec.gov/Archives/edgar/data/1973266/000095017025027778/tko-20241231.htm.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks for the consideration paid in an acquisition or asset purchase, especially "at close" or "at closing", call load_skill with `deal_consideration_at_close`.

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

- A search snippet is a lead, not evidence. Open the primary document with parse_html_page and confirm each figure, period and unit with retrieve_information. If one filing's summary does not give the figure the question's wording asks for (for example a value "at close"), open the closing 8-K or the financial-statement note rather than answering from the summary.
- Never send an empty or null query to a search tool. parse_html_page cannot read PDFs; use the HTML filing.
- Cite only documents you opened and retrieved from. Write the final answer in plain text with no citation markup such as <cite> tags.
</file>

<notes>
Base1 answered $3.30B from one 10-Q retrieval, which itself said no closing-date fair value was stated. It never opened the Feb 28, 2025 closing 8-K or the acquisition note, though the question asks for consideration "measured at transaction close". It also leaked <cite> markup, listed unopened PDFs and filings as sources, and made a null-query search. A skill covers the headline vs. adjustment vs. closing-value reconciliation and the common-control caveat, and carries labelled task leads (10-Q figures, 8-K accession). A short tool_guidance adds the rules to open a second source when the summary lacks the asked-for measure, cite only opened documents, and write plain text. The skill is named in systemprompt.md.
</notes>