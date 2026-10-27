<file path="skills/guidance_vs_actual/SKILL.md">
---
name: guidance_vs_actual
description: Answer "how much did company X beat or miss its guidance" for a margin, revenue or EPS line, in basis points, dollars or percent.
---

# Guidance vs actual

**Analytic move:** compare. Take the actual from the earnings release for the guided quarter, take the guidance from the PRIOR quarter's release (its "Business Outlook" table), and subtract them on the same basis.

**Where the figures live**
- Guidance: the 8-K Exhibit 99.1 press release for the quarter BEFORE the one in question, in the outlook table, usually as a midpoint ± a range.
- Actual: the 8-K Exhibit 99.1 for the guided quarter, which reports the margin to one decimal. The 10-Q income statement gives the dollars (gross margin and revenue) so the ratio can be computed. The 10-Q's percentage column is often rounded to a whole number, so do not use it as the reported margin.
- Management remarks such as "above the high end of guidance" often refer to the non-GAAP line. Do not transfer them to GAAP.

**Procedure**
1. Fix the basis the question names (GAAP or non-GAAP). Use the same basis for guidance and actual.
2. Fix the guided period. Match the company's fiscal quarter, not the calendar quarter.
3. The default beat or miss is actual minus the guidance MIDPOINT. Also state the low and high ends and whether the actual is inside, above or below the range.
4. For a margin, 1 percentage point = 100 bps. Compute two figures:
   - the company-reported one-decimal percentage minus the midpoint (how the company and analysts state it);
   - the unrounded ratio ($ gross margin / $ revenue) minus the midpoint.
   Headline the answer with the one-decimal reported figure and show the unrounded figure beside it. If they differ by under 1 bp, say so. Do not build a headline on a whole-percent rounding from a table.
5. State the sign (beat or miss) in words, with period, units, arithmetic and the source of each figure.
6. Before submitting, confirm that both figures are on the same basis, come from the right two releases, and use the same unit. If the figures came from search excerpts rather than an opened filing, say so.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks whether or by how much a company beat or missed its own guidance or outlook (margin, revenue, EPS), call load_skill with `guidance_vs_actual`.

When you have the final answer, you should call the `submit_final_result` tool with it. Your submission will not be processed unless you call this tool.

You should include any necessary step-by-step reasoning, justification, calculations, or explanation in your answer. You will be evaluated both on the accuracy of the final answer, and the correctness of the supporting logic.

When possible, please provide any calculated answers to at least two decimal places (e.g. 18.78% rather than 19%). Please do not round intermediate steps in any calculation - you should only round your final answer.

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

- Before searching, fix the company, document type and fiscal period. Guidance questions need two documents: the prior quarter's earnings release (the outlook) and the release or 10-Q of the quarter being judged (the actuals). Search by company, form, fiscal quarter and line item.
- SEC endpoints often return HTTP 403 here (`parse_html_page` on sec.gov failed in 2/2 base-style runs that tried it). Do not retry a 403 or loop on index pages. Make a targeted `web_search` and read the filing text in the excerpts. You may try `parse_html_page` once on a different URL, then `retrieve_information` with a specific question.
- A figure seen only in a search excerpt must be described as such. Do not say "verified in the filing", and do not cite a document as opened, unless you opened it or an excerpt quoted it.
- Check each figure before use: fiscal period, units, GAAP vs non-GAAP, and point value vs midpoint vs range.
- Do the arithmetic from unrounded inputs, re-check it once, and round only the final result.
- Write the answer as plain text with no raw citation tags. Submit with `submit_final_result` as soon as the figures are in hand.
</file>

<notes>
kept -> dom1 skill guidance_vs_actual (with trigger line in systemprompt) -> base1 and both candidates computed 139.77 bps off the same midpoint; a reusable beat/miss-vs-midpoint procedure with range check and GAAP/non-GAAP separation is generic and worth loading on demand.
revised -> dom1 skill -> dom1's turn-3 answer headlined "150 bps" off the 10-Q's whole-percent 27%, which is a rounding artifact; the skill now says to headline the one-decimal reported figure (26.9% → ~140 bps) and not use whole-percent table roundings.
dropped -> dom1 skill "Task fact" block and inv1 LongTermMEMORY entry -> task-specific figures from excerpts risk anchoring and false "verified" labels (library lesson from q19); the agents found these figures via search in 1 turn anyway.
kept -> inv1 tool_guidance.md (trimmed) -> base1 hit a 403 on parse_html_page at turn 1 and dom1 hit one at turn 2; inv1's bounded fallback and "describe excerpt-only figures as such" matched inv1's honest caveat, whereas base1 cited unopened documents without disclosure.
dropped -> inv1's "show difference on reported rounded figures" as an always-on line -> moved into the skill, where it is scoped to guidance questions and tied to the one-decimal reported figure.
kept -> dom1 systemprompt wording tweak "calculation" -> harmless; the trigger line is the substantive change. No candidate rollout failed to submit (inv1 1 turn, dom1 3 turns, both submitted).
</notes>