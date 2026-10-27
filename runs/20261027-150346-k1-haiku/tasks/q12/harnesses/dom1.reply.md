<file path="skills/monthly_revenue_vs_quarter_guidance/SKILL.md">
---
name: monthly_revenue_vs_quarter_guidance
description: Project a quarter's revenue from two reported months plus a growth-rate assumption for the third month, then compare it with the company's quarterly guidance range (currency conversion, midpoint and range position). Used for TSMC-style monthly revenue reporters.
---
ANALYTIC MOVE: calculate + compare. Inputs are (a) the two months already reported, (b) a growth assumption for the third month built from historical same-month growth, and (c) the quarterly guidance range. Result: implied quarter revenue and BEAT or MISS versus guidance, with the amount.

1. Guidance source. Take the range from the release that first issued it, which is the prior quarter's earnings release or management report, not from a snippet. Retrieve four things: the range, its currency, the exchange-rate assumption, and the date. Later updates, such as a "closer to the low end" comment, are labelled asides, not the guidance.
   - In this task (re-confirm in text): TSMC guided Q1 2025 revenue to US$25.0-25.8B in its 4Q24 results on Jan 16, 2025. The guidance is in USD, the monthly reports are in NT$, and the exchange-rate assumption (believed to be 1 USD = 32.8 NT$) must come from that release. A 1Q25 presentation that postdates the question date shows the actual average rate. Do not use it as the guidance assumption.
2. Reported months. Open each monthly revenue report (a TSMC 6-K, tsm-revenueYYYYMMDD.htm, or the pr.tsmc.com release). Retrieve net revenue in NT$ millions for the month and for the prior month. Use only data published on or before the question date. Releases dated after it, such as the April 10 March-revenue report, are off limits.
   - In this task (re-confirm): Jan 2025 NT$293,288M, Feb 2025 NT$260,009M.
3. Growth definition. "Growth rate in March" for a projection from February's base is month-over-month (March / February - 1) for each of the three prior years. State this definition. Show YoY (March vs same month of the prior year) only as a labelled cross-check, and say whether the verdict changes. Use the three most recent completed years (here 2022, 2023, 2024). For each year, retrieve both that February and that March NT$ figure from the monthly reports and compute from the unrounded figures. The company's stated percent is a cross-check.
   - Leads from an earlier run, to be re-confirmed in the reports (NT$M, Feb to Mar): 2022 146,933 to 171,967 (+17.04%); 2023 163,174 to 145,408 (-10.89%); 2024 181,648 to 195,211 (+7.47%). The simple average is about +4.54%.
4. Projection. March 2025E = Feb 2025 x (1 + average growth). Implied Q1 = Jan + Feb + March2025E in NT$M. Do not round before the end.
5. Comparison. Convert guidance to NT$ at the guidance rate, or convert implied revenue to USD at that same rate, and keep the two on the same basis. Report the difference against the low end, the midpoint ((low + high)/2) and the high end, in both currency and %. The verdict is stated against the midpoint, and the position in the range is stated explicitly (below, within or above). Say which side the answer sits on if the rate assumption moves.
6. Answer contract: the verdict plus the amount in US$B and %. A table of the three years' Feb, Mar and growth; the average; Jan, Feb and projected Mar; implied Q1 in NT$ and US$; guidance low, mid and high; the exchange-rate assumption and its source; one-line caveats (the simple average of three very different years, FX sensitivity). Cite only documents that were actually opened.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks you to project a quarter's revenue from monthly revenue reports and compare it with the company's quarterly guidance (for example TSMC), call load_skill with `monthly_revenue_vs_quarter_guidance`.

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

- A search snippet is a lead, not evidence. Every figure in a calculation (guidance range, exchange-rate assumption, monthly revenue) must be read from a document opened with parse_html_page and confirmed with retrieve_information. Do not call a figure "guidance" or "assumed" if you only inferred it from a different document.
- Respect the question's as-of date: do not use documents published after it, even if search returns them.
- Cite only documents you opened and retrieved from. Write the final answer in plain text with no citation markup such as <cite> tags.
</file>

<notes>
Motivation: base1 ran only web_search calls (one turn), opened no document, and built the answer from snippets. It inferred the guidance FX rate (32.8) from a later 1Q25 presentation table and said so, listed sources it never opened, and leaked raw <cite index> markup in the answer. It also did not state clearly why month-over-month growth was the chosen definition, and showed no alternative. The tool_guidance bullets target the snippet, inference and markup failures, the same pattern fixed in earlier library entries (q47, q35). The new skill encodes the practitioner knowledge for this task type: guidance is in USD while monthly reports are in NT$, so the guidance FX assumption must be sourced from the guidance release. Growth is defined as MoM Mar/Feb with YoY only as a labelled cross-check. Post-date reports are excluded. The result is stated against the midpoint plus the range position. Verified-in-snippets task figures (Jan/Feb 2025 and the 2022-24 Feb/Mar NT$ values) are included as labelled leads for re-confirmation. The 32.8 rate is marked as believed and needing confirmation, since the run did not verify it.
</notes>