<file path="skills/guidance_implied_gross_profit/SKILL.md">
---
name: guidance_implied_gross_profit
description: Compare reported gross profit (non-GAAP or GAAP) with the dollar gross profit implied by prior-quarter guidance (revenue midpoint x guided gross margin), for several quarters, with an average.
---
ANALYTIC MOVE: compare, repeated per quarter, then average. Inputs per quarter: (a) revenue guidance and gross margin guidance for quarter N, from the earnings release for quarter N-1 (its "Current Outlook" section); (b) the actual non-GAAP gross profit for quarter N, from the reconciliation table in the release for quarter N. Result: implied guide $, actual $, difference $, difference %, BEAT or MISS.

1. Window. Take "the last 4 quarters" as the four most recent quarters reported on or before the as-of date (April 07, 2025). Check the date of the latest results release you can open. A quarter reported after the as-of date is excluded; say so. In this task (AMD) the window should be the four quarters of fiscal 2024. The Q4 2024 results release is dated about Feb 4, 2025. The Q1 2025 release falls after the as-of date.
2. Guidance document. Quarter N's guide is in the release that reported quarter N-1, so the Q1 2024 guide is in the Q4 2023 release. Open each guidance release and retrieve three items: the revenue midpoint (for example "approximately $X B, plus or minus $300M"), the non-GAAP gross margin percentage and the basis (non-GAAP, not GAAP). Quote the margin exactly as printed. AMD guides in half-point steps (for example 53.5%), so never round it to a whole percent or reuse the previous quarter's margin. Write down the exact sentence retrieved for each quarter.
3. Actual document. Open the release for quarter N. Retrieve the non-GAAP gross profit in dollars (millions) from the "Reconciliation of GAAP to Non-GAAP Financial Measures" table, in the current-quarter column and not the prior-quarter or year-ago column. Also retrieve actual revenue and non-GAAP gross margin as a cross-check. Gross profit divided by revenue should match the stated margin to within rounding. Do not rebuild gross profit as revenue x rounded margin, and do not use GAAP gross profit (it is lower because of amortization and similar items).
4. Calculation, at full precision. Implied guide GP = revenue midpoint x guided margin. Difference $ = actual GP - implied GP. Difference % = difference / implied GP x 100. Positive means BEAT, negative means MISS. Average = the simple mean of the four percentages. Also give the average dollar difference if useful, but label the percentage average as the headline. Round only at the end.
5. Answer contract: one line per quarter in exactly the format the question prescribes (for example "QX - $XXX million (X.X % BEAT or MISS)"). Apply the question's decimals and rounding to the printed figures (dollars to the unit the question shows, percent to the decimals shown), and keep a more precise version in the working. Then give the average beat/miss in the same format. Under the lines, show for each quarter the guidance source release and date, revenue midpoint, guided margin, implied GP, actual GP and source release. Label calendar quarters with the company's fiscal labels. List only documents actually opened.
6. Checks before submitting: (a) every guided margin was read from the text of the release that preceded that quarter; (b) every actual GP comes from the right column of a non-GAAP reconciliation; (c) the units are $ millions throughout; (d) the sign and the BEAT/MISS word agree; (e) the four quarters are consecutive and the labels match the fiscal periods.

Leads for AMD (retrieve and confirm in the text; none of these are verified figures). 8-K EX-99.1 releases on sec.gov, CIK 2488:
- https://www.sec.gov/Archives/edgar/data/2488/000000248824000009/q42023991final.htm (Q4 2023 results, gives the Q1 2024 guide)
- https://www.sec.gov/Archives/edgar/data/2488/000000248824000054/q12024991.htm (Q1 2024 results, gives the Q2 guide)
- https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/q22024991.htm (Q2 2024 results, gives the Q3 guide)
- https://www.sec.gov/Archives/edgar/data/2488/000000248824000161/q32024991.htm (Q3 2024 results, gives the Q4 guide)
- The Q4 2024 results release (about Feb 4, 2025) was seen in search only as a PDF of slides, which parse_html_page cannot read. Find its HTML 8-K exhibit with edgar_search (company AMD, form 8-K, Feb 2025).
A previous run on this task used only search snippets, assumed 54% for the Q4 2024 guide and 53.5% for the Q3 guide without opening the releases, and mislabelled which release held which guide. Check both margins in the opened text.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks how reported gross profit (or another dollar profit line) compared with the amount implied by prior-quarter revenue and margin guidance, over several quarters, call load_skill with `guidance_implied_gross_profit`.

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

- A search snippet or title is a lead, not evidence. Open each primary document (8-K EX-99.1 earnings release, 10-Q, 10-K) with parse_html_page, then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP basis in the retrieved text. This applies to guidance figures and to actuals. parse_html_page cannot read PDFs; use the HTML exhibit, found with edgar_search if needed.
- Guidance for a quarter sits in the release for the previous quarter; the actual sits in the release for the quarter itself. A question that compares them needs both documents opened for every period. Do not fill a guided figure from memory or from the neighbouring quarter.
- Respect the as-of date (April 07, 2025). Do not use releases dated after it.
- Never issue a search with an empty query. If a search returns nothing useful, retry once with a short non-empty query, then use edgar_search or a known URL.
- Follow the answer format the question prescribes (labels, units, decimals), and show the unrounded working beneath it.
- Cite only documents you opened and retrieved from. Do not list a filing, article or PDF seen only in search results. Write the answer in plain text with no citation markup such as <cite> tags.
</file>

<notes>
Moment: base1 ran only web_search calls (4) and opened no AMD release, then submitted. It used guided margins (53.5% for Q3, 54% for Q4) it never verified, sources mapped confusingly to guidance versus actual releases, and it printed two-decimal percentages with a .5 dollar figure even though the question prescribes "X.X %". AMD guides in half-point steps, so unverified margins are the main numeric risk. The edits are a skill (on-demand) carrying the practitioner procedure: guidance for quarter N is in the N-1 release, take actual non-GAAP gross profit from the reconciliation table, the as-of window excludes Q1 2025, follow the format. A trigger line in systemprompt.md. A short always-on tool_guidance covers open-primary-documents, source discipline, no empty queries and the prescribed format. Release URLs come from the base run's search results and are labelled as leads to re-confirm. I recorded no figures as verified, because the base run did not retrieve any.
</notes>