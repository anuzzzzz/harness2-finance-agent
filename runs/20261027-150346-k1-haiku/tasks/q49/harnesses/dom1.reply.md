I'm adding a skill for annual guidance-beat counting and a short tool-guidance file. The base run answered from search snippets and parsed no document. It leaked citation markup. It also listed PDFs and articles it never opened as sources, and counted beats against only the final raised range. The skill is `guidance_beat_count_multi_year`, with a trigger line in `systemprompt.md`.

<file path="skills/guidance_beat_count_multi_year/SKILL.md">
---
name: guidance_beat_count_multi_year
description: Count how many fiscal years a company beat its own annual adjusted EPS (or similar) guidance, and state the guidance for the current fiscal year, from the earnings releases that issued and updated the guidance.
---
ANALYTIC MOVE: compare, then count. Inputs: for each fiscal year in the window, (a) the guidance issued at the start of the year, (b) the final guidance in force before year-end, (c) the reported actual. Result: a per-year BEAT / IN RANGE / MISS table, a count, and the current-year guidance.

1. Fix the window and the benchmark. "Last two years (FY2023 and FY2024)" means the two fiscal years, not calendar years. General Mills' fiscal year ends in late May. The question does not say which guidance counts, so report BOTH benchmarks per year and give the count on each: (i) the INITIAL guidance, from the prior fiscal year's Q4 release (late June), and (ii) the FINAL guidance, from the Q3 release (March), which is often narrowed or raised. Say which one the headline count uses and why. If the question could mean quarterly beats against consensus, say that is a different measure and do not mix it into the annual count. Do not invent a quarterly count unless you retrieved each quarter's actual and consensus from opened text.
2. Retrieve from opened primary documents (8-K EX-99.1 releases). The Q4 release of year N holds the year-N actual AND the initial guidance for year N+1. So two Q4 releases (FY2022 and FY2023, FY2024) cover most of the window. The Q1, Q2 and Q3 releases hold the revisions.
3. Basis checks, each stated explicitly:
   - Guidance is usually given as % growth in CONSTANT CURRENCY off the prior-year adjusted diluted EPS base. The release also states the actual as % change in constant currency and as reported-currency % and dollars. Compare constant currency with constant currency. Also give the dollar figures ($ per share) and the reported-currency % change.
   - Adjusted diluted EPS is non-GAAP. Do not use GAAP diluted EPS. Note any currency effect (for example "foreign currency translation had X percentage-point impact").
   - If the actual's constant-currency % equals the top of the range, call it "at the top end". Do not say it is above the range unless it exceeds it.
4. Current-year guidance (as of the question's date). Use the LATEST release before that date (the Q3 release in March for a fiscal year ending in May). Quote the adjusted diluted EPS range, with the basis (constant-currency % change versus the prior-year base), AND what it replaced. Convert to a dollar range using the prior-year adjusted EPS base, and label it a derived approximation. Pay attention to the sign: "down 7 to 8 percent" is a decline.
5. Answer contract: a table (year; initial guidance; final guidance; actual in % and $; verdict on each benchmark); the count; the current-year guidance and its history in the year (initial, then each revision); the calculation; and sources limited to documents actually opened and retrieved from. Plain text, no citation markup.

Task leads (General Mills, GIS; taken from search results only, so re-confirm in the opened text and do not treat as retrieved figures):
- Q4 FY2023 release, with the FY2023 actual and the FY2024 outlook: https://www.sec.gov/Archives/edgar/data/40704/000119312523176744/d41355dex99.htm
- Q4 FY2024 release, with the FY2024 actual and the FY2025 outlook: https://www.sec.gov/Archives/edgar/data/40704/000119312524168511/d786387dex99.htm
- Q3 FY2025 release (March 2025), with the latest FY2025 outlook: https://www.sec.gov/Archives/edgar/data/40704/000119312525057150/d902176dex99.htm
- Q3 FY2023 release: https://www.sec.gov/Archives/edgar/data/40704/000119312523077267/d816383dex99.htm. Q2 FY2024 release: https://www.sec.gov/Archives/edgar/data/40704/000119312523299294/d660865dex99.htm.
- The FY2023 initial guidance sits in the June 2022 Q4 FY2022 release, which must be found with edgar_search (General Mills, 8-K, June 2022).
- An earlier run, from snippets only, reported FY2024 adjusted EPS of $4.52 (+6% constant currency; initial guide +4 to 6%, narrowed to +4 to 5%) and FY2023 of $4.30 (+10% constant currency). It reported the March 2025 FY2025 EPS guide as down 7 to 8% constant currency. Verify all of these in the text.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks how many years or times a company beat, met or missed its own annual guidance, or asks for the current-year guidance, call load_skill with `guidance_beat_count_multi_year`.

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

- A search snippet or result title is a lead, not evidence. Open the primary document (8-K EX-99.1 release, 10-Q, 10-K) with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm each figure's period, unit and GAAP/non-GAAP basis in the retrieved text. This applies to guidance, actuals and the current-year outlook alike.
- parse_html_page cannot read PDFs. Use the HTML 8-K exhibit instead. Never send an empty search query; use edgar_search with company and date filters to find a release.
- Cite only documents you opened and retrieved from. Do not list PDFs, articles or releases seen only in search results.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags.
</file>

<notes>
Motivation: base1 ran only web_search calls and never called parse_html_page or retrieve_information. It built the FY2023 and FY2024 guidance and actuals from snippets and leaked raw citation markup. It listed PDFs and articles it never opened, such as the q4cdn PDFs and Baking Business. It also compared actuals only with the final raised range, without giving the initial-guidance comparison. It left the ambiguity (annual guidance versus quarterly consensus) as a caveat and gave no table. The new skill states the practitioner structure: Q4 release of year N holds the actual and the initial guide for N+1; report both initial and final benchmarks; compare constant currency with constant currency; "at top end" is not "above"; derive a dollar range for the current-year guide and label it as derived. It carries the verified-from-snippet leads, labelled for re-confirmation. The tool_guidance file is short; it carries the open-then-retrieve and cite-only-opened rules that the library showed changed this behaviour. The trigger line in systemprompt.md names the skill.
</notes>