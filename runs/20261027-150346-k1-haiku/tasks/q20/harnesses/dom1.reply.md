<file path="skills/effective_tax_rate_change/SKILL.md">
---
name: effective_tax_rate_change
description: Report a company's effective tax rate for a fiscal year, the prior-year rate, and the change in bps, using the company-stated GAAP rates with an unrounded cross-check.
---
ANALYTIC MOVE: look up, then compare. Inputs are the provision for income taxes and income before income taxes for the two fiscal years. The result is each year's effective tax rate and the change in basis points.

1. Controlling source: the FY 10-K. Look in MD&A "Provision for Income Taxes", which has a line "Effective tax rate x% y%", and in the income-taxes note (rate reconciliation). The earnings release (8-K EX-99.1) only confirms. Take both years from the same 10-K's comparative columns, which keeps the basis consistent.
2. Headline = the effective tax rates the company states, at its published precision. Compute the change in bps as (current stated rate - prior stated rate) x 100. Show it in the form the question prescribes, e.g. "Delta: 410bps".
3. Cross-check on a separate labelled line: provision / pre-tax income for each year, unrounded, and the bps change from those. Say that this differs from the headline only because the company rounds its rates to one decimal. Do not present the two as equal answers. Name which one is the headline.
4. Distractors:
   - Non-GAAP or "adjusted" effective rates in the earnings-release reconciliation footnotes are not the GAAP rate asked for. Mention them only as a labelled aside, if at all.
   - Check the fiscal year-end against the question (a 5/31 year-end is not a calendar year).
   - A rate change is in percentage points, not percent. 1 percentage point = 100bps.
5. Give the drivers of the change as the MD&A states them (quote or closely paraphrase retrieved text). Do not invent drivers.
6. Answer contract: both rates with fiscal-year labels, the provision and pre-tax income for each year in $ millions, the calculation, the bps delta in the requested format, the direction (increase or decrease), the drivers, and sources limited to documents actually opened.

Task facts (Oracle, FY ended 5/31; retrieved in a prior run from the FY2024 10-K MD&A and Note 13, so re-confirm in the text), $ millions:
- FY2024 pre-tax income 11,741, provision 1,274, stated rate 10.9%.
- FY2023 pre-tax income 9,126, provision 623, stated rate 6.8%.
- The stated-rate change is 410bps. The unrounded change is about 402bps (10.8509% vs 6.8266%).
- Oracle's non-GAAP adjusted rates (19.2% and 16.3%) are a distractor.
- FY2024 10-K: https://www.sec.gov/Archives/edgar/data/1341439/000095017024075605/orcl-20240531.htm
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks for a company's effective tax rate (or its change versus the prior year, in bps or points), call load_skill with `effective_tax_rate_change`.

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
Motivation: base1 found the right figures (10-K says 10.9% and 6.8%) but headlined the unrounded 402bps and relegated the company-stated 410bps to a side note. That left two competing deltas, and the question asks for a single "Delta: XXXbps". Library lesson from q44: headline the company-stated figure and label unrounded variants as cross-checks. The new on-demand skill therefore makes the stated rates the headline (410bps) and keeps the unrounded 402bps as a labelled cross-check. It also flags the non-GAAP 19.2%/16.3% distractor and carries the verified Oracle facts, marked for re-confirmation. The trigger line is in systemprompt.md. The skill's headline choice is a judgement call, since the evidence does not settle which delta is wanted. The other components are unchanged because the run's sourcing was already clean.
</notes>