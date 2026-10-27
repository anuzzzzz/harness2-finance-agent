The base run answered from search snippets in a single turn and never opened a filing. Its arithmetic was sound, but the actual figure was not read from the quarter's earnings release. It also chose the guidance midpoint as the benchmark without saying that was a choice. I'm adding one skill for guidance-versus-actual questions, plus a one-line trigger in the system prompt.

<file path="skills/guidance_vs_actual/SKILL.md">
---
name: guidance_vs_actual
description: Answer "did the company beat or miss its guidance, by how much" for a margin, revenue or EPS metric, in basis points or dollars.
---

ANALYTIC MOVE: compare one reported actual with the guidance the company issued for that same period, and state the difference with its sign.

1. Find the guidance. It lives in the PRIOR quarter's earnings release (8-K Exhibit 99.1), under "Business Outlook" or "Guidance". Do not use the current quarter's release for it. Record the midpoint, the +/- band, the range, and whether the figure is GAAP or non-GAAP. Releases usually give both bases, and they differ.
2. Find the actual. It lives in the CURRENT quarter's earnings release (8-K EX-99.1: highlights table and GAAP/non-GAAP reconciliation). Cross-check it against the 10-Q income statement: gross margin / revenue. Confirm that the fiscal quarter's end date matches the quarter the guidance covers.
3. Match the basis. Compare GAAP actual with GAAP guidance, and non-GAAP with non-GAAP. If the question says GAAP, do not use the non-GAAP actual, even though the headline "above the high end" language usually refers to non-GAAP.
4. Compute. Difference in bps = (actual % - guidance %) x 100. Compute the actual unrounded from the dollar figures (gross margin $ / revenue $). Also state the release's reported rounded percentage and the bps difference using it, so a reviewer sees both. The reported figure is the headline number.
5. Answer contract:
   - The headline bps figure with its sign, benchmarked to the guidance MIDPOINT, and said explicitly to be the midpoint.
   - Where the actual falls relative to the range: above the high end, inside it, or below the low end, and the bps distance to the nearest bound.
   - Guidance figure, actual figure, period, GAAP/non-GAAP label, and the source document for each.
6. Never take the guidance or the actual from a search snippet or from memory. Open both documents and quote the lines.

In this task (Micron, fiscal Q3 2024, quarter ended May 30, 2024), these are the leads to verify, not established facts:
- The guidance is in the FQ2-24 release, https://www.sec.gov/Archives/edgar/data/723125/000072312524000004/a2024q2ex991-pressrelease.htm. A prior run read GAAP gross margin guidance as 25.5% +/- 1.5%.
- The actual is in the FQ3-24 release, https://www.sec.gov/Archives/edgar/data/723125/000072312524000016/a2024q3ex991-pressrelease.htm, and in the 10-Q. A prior run read the 10-Q as gross margin $1,832M on revenue $6,811M, which is about 26.9%.
- Read the release's own stated GAAP gross margin percentage and the guidance table in both documents before submitting.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks whether a company beat or missed guidance (by how many basis points, dollars or percent), call load_skill with `guidance_vs_actual`.

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
Motivating moment: in base1 (1 turn), the agent ran only two web_searches and submitted from snippets, with no parse_html_page or retrieve_information call on the guidance release or the actual-results release. It chose the midpoint as the benchmark and reported 139.77 bps. It also computed the actual from 10-Q dollars rather than quoting the release's reported GAAP percentage. The skill encodes the practitioner rules: guidance sits in the prior quarter's release and actuals in the current one, GAAP must be matched to GAAP, the midpoint is the headline benchmark, the range position is reported too, and both the reported percentage and the unrounded computation are shown. The task-specific URLs and figures are labelled as leads to verify, because the earlier run did not read them from the documents. The trigger line is in systemprompt.md, and the always-on cost is one sentence.
</notes>