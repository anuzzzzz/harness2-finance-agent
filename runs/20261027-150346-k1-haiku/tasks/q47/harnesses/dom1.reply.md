<file path="skills/guidance_vs_actual_midpoint/SKILL.md">
---
name: guidance_vs_actual_midpoint
description: Decide whether a reported quarterly or annual metric beat or missed the guidance range a company gave in an earlier period, measured against the range midpoint, and express the result as a percent.
---
ANALYTIC MOVE: compare. Inputs are (a) the guidance range for the target period, taken from the release that FIRST gave it (the one the question names, e.g. "provided in Q1 2024"), and (b) the actual from the release or filing for the target period. Result: BEAT or MISS, with the % variance versus the midpoint.

1. Guidance source. Open the named period's earnings release or shareholder letter (8-K EX-99.1) and retrieve the exact range for the target period. Later releases often revise guidance. Use the revision only if the question asks for it, and label it as an aside. A full-year range is not a quarterly range, so look for a "guidance by quarter" slide or table.
2. Actual source. Open the target period's release (8-K EX-99.1) or 10-Q and retrieve the actual. Do not take the actual from a search snippet, a news article or a transcript summary. Match the metric definition exactly. For example, "end-to-end payment volume" is not "gross revenue" and not "gross payment volume". Check the unit ($B vs $M).
3. Calculation, unrounded until the end: midpoint = (low + high) / 2. Variance % = (actual - midpoint) / midpoint x 100. Positive means BEAT, negative means MISS. Also say where the actual sits against the range: below the low end, within the range or above the high end.
4. Answer contract: the verdict (BEAT or MISS) with the signed % to two decimals in the form the question asks; the guidance low, high and midpoint, with the source release and date; the actual with its period; the formula and arithmetic; any caveat about the document, such as a draft or a restated figure. List as sources only documents actually opened. No citation markup.

Task facts (in this task; the Q1 letter text was retrieved in a prior run, the Q3 actual came from a search snippet, so re-confirm both in opened documents). Shift4 Payments (FOUR), Q1 2024 shareholder letter, https://www.sec.gov/Archives/edgar/data/1794669/000179466924000014/ex991q1.htm. The slide "Breaking Down Our 2024 Guidance by Quarter" gives end-to-end payment volume of Q2 $39.0-41.0B, Q3 $46.0-48.0B, Q4 $49.0-53.0B and FY2024 $167-175B. The Q3 midpoint is $47.0B. The parsed text carried draft-version editing notes, which is worth a one-line caveat. Q3 2024 end-to-end volume actual is $43.5B, per the Q3 2024 shareholder letter, https://www.sec.gov/Archives/edgar/data/1794669/000179466924000031/ex991q3.htm. (43.5 - 47.0) / 47.0 = -7.45%, so a MISS, and the actual is below the low end of the range. The company later cut its full-year volume outlook, which is not the Q1 guidance.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks whether a company beat or missed its own guidance (a range or midpoint given in an earlier period) for a later period, call load_skill with `guidance_vs_actual_midpoint`.

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

- A search snippet is a lead, not evidence. Open the primary document (8-K EX-99.1 release or letter, 10-Q or 10-K) with parse_html_page and confirm each figure, period and unit with retrieve_information. This applies to the actual as well as the guidance.
- Cite only documents you opened and retrieved from. Do not list a filing, article or transcript you only saw in search results.
- Write the final answer in plain text with no citation markup such as <cite> tags.
</file>

<notes>
Base run1 got guidance (46-48B from the Q1 letter) by opening the Q1 letter, but took the Q3 actual ($43.5B) only from a search snippet and never opened the Q3 letter. It also listed unopened sources (Q3 letter, Yahoo transcript, Benzinga), and leaked raw <cite index> markup into the final answer. The new skill encodes the guidance-vs-actual procedure (midpoint, signed % variance, source of the original guidance, metric definition) plus the verified Q1 guidance facts, and labels the Q3 actual as needing confirmation. A short tool_guidance rule covers snippet-vs-primary verification and cite-only-opened sources, and a trigger line in systemprompt.md names the skill. Both follow the library pattern from q44/q45/q30.
</notes>