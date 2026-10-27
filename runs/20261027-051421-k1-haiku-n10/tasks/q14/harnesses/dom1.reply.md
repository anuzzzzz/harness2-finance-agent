I'm adding one skill for free-cash-flow margin trend questions, plus the trigger line that makes it loadable. The runs already reached a sensible answer, so this only encodes the practitioner checks they did not show consistently.

<file path="skills/fcf_margin_trend/SKILL.md">
---
name: fcf_margin_trend
description: Approximate free cash flow as operating cash flow minus capex, compute FCF margin over several fiscal years, and describe the trend.
---

# FCF margin trend (FCF ≈ CFO − capex, ÷ revenue, multi-year)

**Analytic move:** calculate, then classify the trend. For each fiscal year take CFO, capex and total revenue from the filings, compute FCF and FCF ÷ revenue unrounded, and state the direction year over year.

**Where the figures live**
- CFO: cash flow statement, "Net cash provided by (used in) operating activities", total-company line.
- Capex: investing section, "Purchases of property and equipment". For software or internet companies this line usually includes capitalized internal-use software. Purchases of intangibles (for example domain names) and capitalized-software lines are separate. Headline CFO − "purchases of property and equipment" as the question's approximation. Show the alternative that also deducts intangibles only as a labelled sensitivity, and only if the direction is unchanged.
- Revenue: income statement, total revenue, same fiscal year.
- Each 10-K carries three years of cash flows and income statement, so FY(N) and FY(N−2) come from one filing. Take FY2022 from the FY2023 or FY2024 10-K comparative columns. Check whether the comparatives were recast.

**Checks that change the answer**
1. Discontinued operations: if a business was wound down or reclassified (a large inventory unwind, for example), the cash flow statement may include discontinued operations while revenue shows continuing operations only. State that mismatch. A margin well above 100% is a red flag for it, not a result to present without comment. Give the headline on the stated formula, then identify the distorted year and the cause, quoting the working-capital or discontinued-operations line. If a continuing-operations CFO is disclosed, show it as a second labelled figure.
2. Use the revenue basis of the same filing and recast status as the CFO. Do not pair a restated revenue with an unrestated CFO without saying so.
3. Prefer figures read from the company's own filings. A data aggregator (stockanalysis, macrotrends) is only a labelled cross-check. Say which year's figure came only from an aggregator.
4. Units: confirm millions vs thousands. FCF margin is a percentage of total revenue. Report the change in percentage points between years, not a relative change.
5. Trend wording: for every year-over-year step say rises or falls with the percentage-point change. Say whether the overall FY(N−2)→FY(N) path is monotonic. If one year is an outlier, say what the trend looks like excluding it.

**Answer contract:** a table with CFO, capex, FCF, revenue and FCF margin for each year, with units and period. Add the formula, the arithmetic, the pp change per step, the one-sentence trend conclusion, the outlier or discontinued-operations explanation if applicable, and a source for each figure (filing or aggregator, opened or search excerpt). Round only at the end, to two decimals.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks for free cash flow, FCF margin or its trend over several years (CFO minus capex, divided by revenue), call load_skill with `fcf_margin_trend`.

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
Motivation, from base1: it took FY2022–FY2024 CFO, capex and the FCF margin straight from the stockanalysis aggregator. FY2022 revenue came from a Macrotrends history, not a filing. The answer cited 10-K URLs it had never opened (those fetches returned 403). The run produced a 224% FY2022 margin and explained it as the Zillow Offers wind-down. It gave the intangibles sensitivity unprompted. The skill makes these practitioner checks standard:
- the CFO vs revenue basis mismatch when discontinued operations are involved;
- capex line definitions;
- reading FY2022 from 10-K comparative columns;
- labelling aggregator-only figures;
- reporting percentage-point changes per step.
I did not embed this task's figures as durable facts. The only evidence is a third-party aggregator, so the skill carries only structural knowledge. The trigger line is added to systemprompt.md. Nothing else is changed.
</notes>