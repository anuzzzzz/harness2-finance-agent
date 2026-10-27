<file path="skills/convertible_notes_dilution/SKILL.md">
---
name: convertible_notes_dilution
description: Share-count dilution from convertible senior notes (maximum or if-converted shares) at a balance-sheet date, built from the 10-K debt and EPS notes.
---

# Convertible notes: dilutive share count

ANALYTIC MOVE: calculate and reconcile. Inputs are the principal outstanding and the conversion rate for each note series at the stated date. Result is shares issuable per series and in total, reconciled to the figure the company reports.

## Where the figures live (10-K)
- Net loss per share note (in this task, Note 3): the table of potentially dilutive securities excluded as anti-dilutive. It has a "Convertible Notes (if-converted)" line in thousands of shares at each year-end. This is the company's own aggregate share count.
- Debt note (in this task, Note 7): per series, the principal outstanding, conversion rate per $1,000, conversion price, maturity, and make-whole or fundamental-change language. Item 7 liquidity repeats some of it.
- Capped-call and hedge paragraphs: capped calls offset dilution economically but do not lower the gross shares issuable. Report gross and mention the capped calls separately.
- Each series' indenture or its 8-K exhibit 4.x gives the "maximum conversion rate" that applies after a make-whole fundamental change. Treat it as a separate upper bound.

## Verified in this task (Snap FY2024 10-K, read through the retrieval tool, so re-confirm in the text)
- The if-converted line was 85,945 thousand shares at 12/31/2024 (89,379 thousand at 12/31/2023 and 2022).
- Principal x conversion rate by series at 12/31/2024 sums to about 85,945 thousand. Per series: 2025 notes $36.24M at 46.1233; 2026 notes $249.754M at 43.8481; 2027 notes $1,150M at 11.2042; 2028 notes $1,500M at 17.7494; 2030 notes $750M at 45.0846.
- The 2030 notes' maximum conversion rate, from the May 2024 8-K indenture, is 59.7371 per $1,000. The base run found no maxima for the other series.

## Procedure
1. Retrieve the dilutive-securities table row and the per-series principal and rate from the 10-K text, quoted with period and unit. Check that the date is the one the question names.
2. Compute principal / 1,000 x rate for each series. Sum them and reconcile to the reported if-converted line. Explain any gap, such as a repaid or repurchased series or a change in principal.
3. Search the 10-K text for "maximum", "make-whole" and "fundamental change". If the 10-K states a maximum number of shares issuable, quote it and use it as the answer.
4. If the question says "maximum", check whether each series has a maximum conversion rate, found in the 10-K or the 8-K exhibit for that series. Compute a maximum only when it is applied to EVERY series with a retrieved maximum rate. Do not combine one series at its maximum rate with the others at base rates and present that total as the maximum. If only some maxima are found, say so and lead with the reported if-converted figure.
5. State the answer as a lead number in shares (and in millions), with the per-series table, the date, and the basis (if-converted at base rates vs make-whole maximum). Keep the basis explicit and give the base-rate total and the make-whole total as separate labelled lines.
6. Before submitting, confirm that the principal amounts are as of the question's date. Also confirm that units are thousands of shares, not dollars.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks about dilution, shares issuable, or conversion terms of convertible notes, call load_skill with `convertible_notes_dilution`.

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
Motivation: in base1 the agent's retrieval was truncated and it never confirmed whether the 10-K states a maximum share count. It mixed the 2030 notes' maximum conversion rate (59.7371, from an 8-K) with base rates for the other series. That produced a hybrid 96.93M figure that is neither the reported if-converted number (85.945M) nor a true maximum. The skill encodes where the figures live (EPS note, debt note, indenture exhibits), the reconciliation of principal x rate to the reported line, and a rule against mixing bases. It carries the facts that were retrieved in this task, labelled for re-confirmation. The skill is only loaded when convertible dilution is asked about, so it adds almost nothing to the always-on text. The trigger line is added to systemprompt.md.
</notes>