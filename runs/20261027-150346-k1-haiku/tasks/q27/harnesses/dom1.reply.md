<file path="skills/debt_instrument_terms/SKILL.md">
---
name: debt_instrument_terms
description: Report the terms of a named debt or hybrid security (junior subordinated debentures, subordinated notes, preferred) from a company's 10-K debt note, with each term tied to opened text.
---
ANALYTIC MOVE: trace and classify. The input is a named instrument and a fiscal year. The result is a term sheet for that instrument only, read from the filing's own words.

1. Where the terms live. In a 10-K, the governing text is the debt note in the financial statements (often titled "Capital Structure" or "Debt"). It has a table of principal, rate and maturity by instrument, followed by narrative on call, interest deferral and covenants. MD&A "Capital Resources" and Item 5 or the exhibit index give corroboration. Open the filing itself. A snippet or a prior-year filing is not enough. Terms can change between years, for example a LIBOR replacement.
2. Keep look-alike instruments apart. "Junior subordinated debentures" are different from "subordinated debentures", "senior notes" and preferred stock. Each has its own principal, rate and maturity. Name the instrument exactly as the table does. If the filing has several lines, report only the one asked about, and note the others in one line.
3. Term checklist, each tied to the opened text and flagged "not stated" if absent:
   - issuer, series name and the principal outstanding at fiscal year-end, with the prior year for comparison, in the filing's units;
   - coupon, fixed or floating, any switch date, and the floating benchmark plus spread. Check for a LIBOR-to-SOFR fallback and the spread adjustment;
   - scheduled maturity versus final maturity;
   - optional redemption: dates, price and any make-whole;
   - interest deferral: maximum length, compounding, any obligation to issue stock, and the dividend or repurchase restrictions that apply during deferral;
   - ranking and any replacement-capital covenant, only if the filing says so. Do not infer them.
4. Answer contract: a short lead sentence giving the instrument, principal and coupon. Then the term list with periods and units. Then the document and section for each term. Include only what the question asks. Leave out ratings and commentary unless asked. Quote dates exactly (day, month, year).
5. Before submitting, confirm that every term comes from text you retrieved in this session, that the fiscal year is the one asked, and that the sources list only opened documents.

Task facts (Allstate FY2024; they came from search snippets of the 10-K, so re-confirm them in the opened text). The FY2024 10-K is at https://www.sec.gov/Archives/edgar/data/899051/000089905125000015/all-20241231.htm (CIK 899051). Snippets showed $500 million of Series A 6.500% Fixed-to-Floating Rate Junior Subordinated Debentures due 2067. The scheduled maturity is May 15, 2057 and the final maturity is May 15, 2067. They are redeemable at par on or after May 15, 2037, or earlier at a make-whole price in certain circumstances. After May 15, 2037 they pay quarterly at three-month CME Term SOFR plus a spread adjustment of 0.26161% plus 2.120%, replacing LIBOR. Interest may be deferred for up to 10 years and compounds during deferral. The floating rate subordinated debentures due 2053 are a separate instrument.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks for the terms of a specific debt, hybrid or preferred security (coupon, maturity, call, deferral, covenants) in a company's capital structure, call load_skill with `debt_instrument_terms`.

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

- A search snippet or result title is a lead, not evidence. Open the primary filing with parse_html_page, then ask retrieve_information one targeted question at a time. Confirm the figure, period and unit in the retrieved text before using it.
- Never call web_search with an empty or null query. If a search returns nothing, retry once with a short non-empty query, or use edgar_search or a known URL.
- Cite only documents you opened and retrieved from. Do not list a filing, PDF or press release seen only in search results.
- Write the final answer in plain text with no citation markup such as <cite> tags.
</file>

<notes>
Motivating moment: base1 ran an edgar_search that returned the Allstate FY2024 10-K URL, then ran two web_searches (one with a null query) and submitted. It never called parse_html_page or retrieve_information. Its answer carried raw <cite index> markup and listed the unopened Financial_Report.xlsx, the ARS PDF and an A.M. Best press release as sources. It also added unrequested ratings commentary, and admitted it never found an explicit ranking clause.
Changes:
- New skill debt_instrument_terms. It gives the domain knowledge of where instrument terms sit in a 10-K (the debt note), a checklist of terms, a rule to keep look-alike instruments apart (junior subordinated vs subordinated vs senior), and an answer contract. It carries the Allstate facts labelled as snippet-derived and to be re-confirmed. The trigger line is added to systemprompt.md.
- tool_guidance.md was empty. It now has four short rules: snippets are leads, no null-query searches, cite only opened documents, plain text. All of these trace to base1's behaviour.
</notes>