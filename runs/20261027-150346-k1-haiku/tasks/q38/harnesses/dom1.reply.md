<file path="skills/guidance_margin_vs_actual_bps/SKILL.md">
---
name: guidance_margin_vs_actual_bps
description: Compare a reported margin (for example Adjusted EBITDA / Gross Bookings) with the range the company guided the quarter before, at the midpoint, and give BEAT or MISS with the bps difference.
---
ANALYTIC MOVE: compare. Inputs are (a) the guided margin range for the target quarter, from the PRIOR quarter's earnings release (8-K EX-99.1, "Outlook" or "Business Outlook" section), and (b) the actual margin for the target quarter, from the target quarter's own release. Result: BEAT or MISS plus the difference in bps.

1. Guidance. Open the prior-quarter release and retrieve the guided margin range, the dollar ranges for the numerator and denominator, and the definition of the margin (for example "Adjusted EBITDA margin, calculated as a percentage of Gross Bookings"). The midpoint is (low + high) / 2 of the stated margin range. Where the margin is stated only as a rounded range, use that range. As a cross-check, also compute the midpoint dollar range ratio, and report it only as a secondary figure.
2. Actual. Open the target-quarter release (filed with the quarterly results, usually 5 to 6 weeks after quarter end) and retrieve the quarter's Adjusted EBITDA and its denominator, plus any stated margin. Match the definition exactly (Adjusted EBITDA versus net income; Gross Bookings versus revenue). Do not use a full-year or nine-month figure.
3. If the release gives no quarterly dollar figure, derive the quarter as full year minus the first nine months, using the 10-K and Q3 10-Q, and say it is derived. Cross-check the derived quarterly margin against any stated rounded margin (for example 2.6%) or the earnings call.
4. Calculation, unrounded until the end: actual margin = numerator / denominator. Difference in bps = (actual margin − guidance midpoint) × 10,000. Positive is a BEAT. Also state where the actual sits against the range (below, within or above). If the company's stated one-decimal margin gives a different bps figure from the computed one, give the computed figure as the headline, since the question defines the ratio, and the stated one-decimal variant as a labelled alternate. Both must have the same sign.
5. Answer contract: the verdict (beat or miss) plus bps in the first line; guidance low, high and midpoint with the release and date; actual numerator, denominator and margin with the period and unit ($ millions); the arithmetic; and sources limited to the documents actually opened. Plain text, no citation markup.

Task facts (Lyft; verified in the earlier run's retrieved text, so re-confirm).
- The Q3'24 release (8-K EX-99.1, https://www.sec.gov/Archives/edgar/data/1759509/000175950924000121/lyft-20240930xpressrelease.htm) guided Q4'24 as Gross Bookings of $4.28B to $4.35B, Adjusted EBITDA of $100M to $105M, and an Adjusted EBITDA margin of about 2.3% to 2.4% of Gross Bookings. The midpoint is 2.35%.
- Q4'24 actual: the earlier run did not open the Q4 release (the 8-K filed around 2025-02-11). It derived Adjusted EBITDA of $112.8M (FY $382.4M less 9M $269.6M) and Gross Bookings of $4,278.9M (FY $16,099.4M less 9M $11,820.5M). That gives 2.6361%, or about +29 bps versus the midpoint. The call and release describe the margin as 2.6%, which gives +25 bps. Open the Q4 release to confirm the quarterly dollar figures before submitting.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks whether a company's margin or other metric beat or missed its own prior-quarter guidance, in bps or %, call load_skill with `guidance_margin_vs_actual_bps`.

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
Motivation: the base run (base1) took Lyft's Q4'24 figures from search snippets and a transcript, derived Q4 EBITDA by subtraction, and never opened the Q4 release. The outcome is sensitive to the stated-versus-computed margin (+25 vs +29 bps), and the answer carried that ambiguity only as a caveat. I added an on-demand skill, following the library's guidance-vs-actual pattern (q09, q47, q48), that encodes the analytic move, the midpoint arithmetic, the definition check, and a rule for stated versus computed margin. It records the verified Q3'24 guidance facts (2.3% to 2.4%, midpoint 2.35%) and flags the unconfirmed Q4 dollar figures. It also adds a trigger line in systemprompt.md. I did not add always-on rules, because the library's tool_guidance for this class is owned by the procedure candidate.
</notes>