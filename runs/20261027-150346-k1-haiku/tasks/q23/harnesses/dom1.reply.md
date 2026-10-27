<file path="skills/milestone_timing_lookup/SKILL.md">
---
name: milestone_timing_lookup
description: Answer "when is X expected to start, open or complete" questions (plant, facility, product launch, deal close) from company filings and releases, with the original and latest guidance and the as-of date handled explicitly.
---
ANALYTIC MOVE: trace. Find the company's own stated timing for one named project, in the controlling document, and say how that statement has evolved up to the as-of date.

1. Identify the project exactly as the company names it. The question's wording may be loose. For example, a "distribution center" may be a combined manufacturing and distribution facility. Say which project you matched and why.
2. Controlling sources, in order:
   - the announcement press release (8-K EX-99.1 or the investor-relations news page) for the ORIGINAL timing;
   - the latest 10-K or 10-Q on or before the as-of date (Item 1 / MD&A "Liquidity and capital resources" / capital-expenditure or "Other developments" notes) for the CURRENT timing;
   - a subsequent 8-K or release for any delay, fire, or acceleration.
   Open at least the announcement and the latest periodic filing with parse_html_page, then retrieve_information. Search snippets are leads only.
3. Check the wording and unit of time. "Calendar year 2025" is not "fiscal 2025". Check the company's fiscal year-end and say so if the filing uses fiscal quarters. Report exactly what the text says (a year, a quarter, "no later than"), and do not turn it into a month.
4. Compare filings. If the original and the latest statements differ, report both with their dates and name the latest as the current expectation. If they agree, say they agree. Record any stated risk to the timing (for example a fire or delay) and whether the company says it expects a delay.
5. As-of date. Answer in the "expected" frame the question uses. If a later opening, start or completion is documented in an opened source dated on or before the as-of date, add it as a clearly labelled update after the main answer. Do not substitute it for the expectation.
6. Answer contract: one direct sentence giving the expected timing; the dated statements behind it (original and latest) with the document name and date; any caveat on timing; sources limited to documents actually opened. Plain text, with no citation markup.

Task facts (J.M. Smucker, McCalla, Alabama Uncrustables facility; leads from search snippets in an earlier run, so re-confirm in the opened text): the Nov 2021 announcement described a $1.1B manufacturing facility and distribution center, with construction beginning no later than Jan 2022. Snippets of later 10-K and 10-Q text said construction began in 2022 with production expected to begin in calendar year 2025, and the 10-Q for the quarter ended Jan 31, 2024 said an equipment fire was not expected to cause significant delay. Smucker's fiscal year ends April 30. The ticker is SJM, not SJ. Open the press release and the latest 10-K or 10-Q to confirm the exact wording.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks when a company expects a facility, project, launch or deal to start, open or complete, call load_skill with `milestone_timing_lookup`.

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

- A search snippet or result title is a lead, not evidence. Open the primary document (press release, 8-K exhibit, 10-K, 10-Q) with parse_html_page and confirm the figure or statement, its period and its wording with retrieve_information before relying on it. If web_search returns nothing, retry once with a short non-empty query (never an empty one), then use edgar_search or a known primary URL.
- Cite only documents you opened and retrieved from. Do not list or lean on pages seen only in search results.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags or truncated quotes. Give the direct answer first, then the supporting statement with its date and source.
</file>

<notes>
Moment: base1 ran two web_searches and submitted from snippets without opening the press release or any filing. It leaked raw <cite index> markup, truncated a quote mid-word ("calen[dar year 2025]"), listed unopened SEC filings as sources, and mixed an unconfirmed "facility opened" news item into the answer, so the expected-timing answer was buried. The edits add a short always-on rule (open primary, cite only opened, plain text) and a skill for "when is X expected" questions. The skill covers original versus latest guidance, the calendar versus fiscal year distinction, labelling post-expectation updates, and the loose "distribution center" wording that maps to a combined facility. The Smucker facts (from snippets only) are labelled as leads to re-confirm. Confidence is low: one rollout, and the figure itself was not verified from opened documents.
</notes>