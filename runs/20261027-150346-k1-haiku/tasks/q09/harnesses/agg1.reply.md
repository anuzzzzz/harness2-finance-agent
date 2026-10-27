<file path="skills/guidance_vs_actual/SKILL.md">
---
name: guidance_vs_actual
description: Measure how far a company's reported result beat or missed its own prior guidance (margin, revenue, EPS), in bps, percent or dollars, using the right pair of earnings releases and keeping GAAP and non-GAAP separate.
---
ANALYTIC MOVE: result minus guidance, where the guidance was issued one quarter before the result.

1. Fix the two documents before searching. The ACTUAL is in the earnings release (8-K EX-99.1) for the target quarter. The GUIDANCE is in the "Outlook" table of the PRIOR quarter's release (issued about three months earlier). A quarter-N release is the wrong place for quarter-N guidance. Use edgar_search with company and date filters, or the URLs in the lead below. Then parse_html_page each release under its own key.
2. With retrieve_information, ask separately: (a) the guided metric for the target quarter, with midpoint, ± band and GAAP/non-GAAP labels as printed; (b) the actual for that quarter on the same basis, in dollars and as a percent of revenue. Confirm that period, basis and unit match on both sides. Never compare a GAAP actual with a non-GAAP guide.
3. Headline = actual minus guidance midpoint (1 percentage point = 100 bps; beat positive, miss negative). Use the company-stated rounded percentage for the headline (e.g. the release's "26.9%"). Also give an unrounded cross-check of dollars / revenue, computed carefully and labelled as a cross-check. Say plainly if the two differ in the last digits.
4. State where the actual sits against the guided range: above, inside or below. Give the distance to the nearest end. If the range is derived from midpoint ± band, say so. If management says "above the high end", check which basis (GAAP or non-GAAP) the statement refers to.
5. Take every figure from retrieved text, not from snippets or memory. Do not cite a document you did not open.
6. Answer with: the sign and size in the requested unit; guidance (midpoint, range, basis, period); actual (basis, dollars, percent, period); the calculation; the position versus the range; and the URLs of both releases.

Task lead (unverified; re-confirm in text): Micron fiscal Q3 2024 (quarter ended May 30, 2024). Actual release: https://www.sec.gov/Archives/edgar/data/723125/000072312524000016/a2024q3ex991-pressrelease.htm. Guidance release (fiscal Q2 2024, issued March 2024): https://www.sec.gov/Archives/edgar/data/723125/000072312524000004/a2024q2ex991-pressrelease.htm. The 10-Q rounds gross margin to a whole percent, so use the release for the actual.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks whether a company beat or missed its own guidance or outlook (in bps, %, or $), call load_skill with `guidance_vs_actual`.

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

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K EX-99.1 earnings release), fiscal period. Prefer edgar_search with company and date filters over question-worded web_search. If web_search returns 0 results, retry once with a shorter query, then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Before any figure enters a calculation, open the primary document with parse_html_page (store it under a clear key), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP basis in the retrieved text. Do not say a filing "reports" or "states" a figure you did not retrieve. If a document cannot be fetched, say so and name where the figure came from.
- parse_html_page cannot read PDFs. Use the HTML 8-K EX-99.1 or the 10-K/10-Q instead.
- Use input_character_ranges on long filings rather than re-reading everything.
- When the company states a rounded figure (e.g. "26.9%"), use it for the headline comparison and give an unrounded recomputation only as a labelled cross-check. Carry full precision otherwise and round only the final result.
- Write the final answer in plain text with no citation markup. State each input with its period, unit and source, then the calculation.
- Once every input is verified in primary text, submit with submit_final_result immediately.
</file>

<notes>
merged -> inv1 + dom1 -> both candidates defined the same `guidance_vs_actual` skill. In both rollouts (inv1 4 turns, dom1 5 turns, both submitted) the agent loaded it, parsed the Q2 and Q3 SEC releases, and retrieved 25.5% ± 1.5% GAAP guidance against 26.9% actual. The base run skipped the filings and answered from snippets. I kept one skill and combined the two versions.
kept -> inv1 tool_guidance.md -> base1 made three web_search calls and never opened a primary document; inv1 opened and retrieved from both releases. This is the verify-in-primary-text rule from the q44 library entry, which was also adopted there.
kept -> inv1 skill structure (prior-quarter guidance, same-basis actual, midpoint headline from the company-stated percentage) -> the inv1 and dom1 runs followed it and reached 140 bps.
kept -> dom1 additions (position against the range, GAAP vs non-GAAP caveat on "above the high end", derived range flagged) -> dom1's answer used them to stop the non-GAAP "above the high end" claim being read as GAAP. This is one rollout, so the evidence is weak.
revised -> dom1 unrounded cross-check -> dom1 reported 26.8933% and 139.33 bps, but 1832/6811 is about 26.898%, so about 139.77 bps (base1 had this). The skill now says to compute the cross-check carefully and label it as a cross-check.
kept -> systemprompt trigger line -> one line, identical in effect in both candidates. It names `guidance_vs_actual`, as required.
dropped -> nothing else changed; LongTermMEMORY.md and guardrails.md stay empty. No candidate rollout failed to submit.
</notes>