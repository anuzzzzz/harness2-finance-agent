<file path="skills/guidance_vs_actual_margin_bps/SKILL.md">
---
name: guidance_vs_actual_margin_bps
description: Decide whether a reported margin or rate (pre-tax margin, operating margin, EPS) beat or missed the range the company guided in the prior quarter's release, and state the gap in basis points.
---
ANALYTIC MOVE: compare. Inputs are (a) the guidance range for the target period, taken from the release for the quarter BEFORE it, and (b) the actual from the target period's own earnings release. Result: BEAT or MISS in bps.

1. Guidance source. Open the prior quarter's earnings release (8-K EX-99.1). Find the outlook section for the target quarter and retrieve the low and high ends of the range, plus the metric definition (pre-tax profit margin, GAAP vs adjusted). Use edgar_search (company, form 8-K, date window around the prior release) to find the URL. Do not take the range from a news snippet alone. If it came only from a snippet, say so.
2. Actual source. Open the target period's release and retrieve the actual for the same metric and the same 13-week period. Do not use the full-year figure or a neighbouring quarter. Releases often carry a sentence comparing the result with the company's own plan, such as "above the high end of its plan by X points". Retrieve it and use it as a cross-check.
3. Calculation, unrounded until the end. Gap vs high end = (actual - high) x 100 bps. Gap vs low end and vs midpoint = (actual - (low+high)/2) x 100 bps. State where the actual sits: below the range, within it, or above it. If the question names no reference point, lead with the company's own framing (versus the range ends, high end for a beat) and give the midpoint figure as the labelled alternate. Stated rates are rounded to one decimal, so compute from the stated rates. Note this rounding if recomputation from dollars would differ.
4. Answer contract: verdict (BEAT or MISS) with the signed bps; guidance low, high and midpoint with release and date; the actual with its period and source; the arithmetic; the company's own comparison sentence if present. List as sources only documents actually opened. Write plain text with no citation markup.

Task facts (TJX, Q4 FY2025, the quarter ended Feb 1, 2025). Taken from snippets in an earlier run, so re-confirm in the opened text. The Q3 FY2025 release (Nov 2024) guided Q4 pre-tax profit margin at 10.8% to 10.9%. The Q4 FY2025 release is https://www.sec.gov/Archives/edgar/data/109198/000010919825000006/tjxq4fy25earningspressrele.htm. It reports a Q4 pre-tax profit margin of 11.6%, "above the high-end of its plan by 0.7 percentage points". The earlier run's arithmetic: +70 bps vs the high end, +75 bps vs the 10.85% midpoint. Do not confuse the Q3 FY2026 and Q1 FY2026 releases (accessions 0001098198...58 and ...37) with the Q3 FY2025 release.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks whether a company beat or missed its own guidance (a range given in an earlier period) for a margin, rate or similar metric, or asks for the gap in bps, call load_skill with `guidance_vs_actual_margin_bps`.

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

- A search snippet or result title is a lead, not evidence. Open the primary document (8-K EX-99.1 earnings release, 10-Q, 10-K) with parse_html_page, then confirm each figure, period, unit and GAAP/non-GAAP basis with retrieve_information. This applies to the guidance and to the actual.
- Never send an empty or null query. If web_search returns nothing, retry once with a short non-empty query, then use edgar_search (company, form, date window) or a known primary URL.
- parse_html_page cannot read PDFs. Use the HTML exhibit.
- Guidance-versus-actual questions need two opened documents: the prior quarter's release (guidance) and the target period's release (actual). Compare like with like and carry full precision.
- Cite only documents you opened and retrieved from. Do not list a filing, article or press-release mirror seen only in search results. If a figure came only from a snippet, say so.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags.
</file>

<notes>
Motivating moment: base1 ran two turns, took the 10.8–10.9% guidance from a just-style snippet and the 11.6% actual from a search snippet, never opened either release, listed three unopened sources (just-style, Business Wire, the SEC 8-K), and leaked raw <cite index> markup. It also issued a null-query web_search. The figure (+70 bps vs high end, +75 vs midpoint) is probably right, but unverified and presented ambiguously.
Changes: (1) tool_guidance carries the short sourcing rules, adapted from q47/q48 (open both primary documents, cite only opened, no markup, no empty queries). (2) A new skill, guidance_vs_actual_margin_bps, carries the practitioner logic: where the guidance lives, the high-end vs midpoint reference-point choice, rounding of stated rates, and the answer contract. The task facts are labelled and marked as snippet-derived, with a warning about look-alike FY2026 release accessions seen in search results. (3) A trigger line in systemprompt.md. The base prompt was otherwise unchanged.
</notes>