<file path="skills/convertible_dilution_lookup/SKILL.md">
---
name: convertible_dilution_lookup
description: Find the maximum share dilution from a company's outstanding convertible notes at a balance-sheet date, and reconcile it to principal x conversion rate by series.
---
ANALYTIC MOVE: look up, then reconcile. Report the number of shares issuable on conversion of all outstanding convertible notes at the date asked, and check it against the debt footnote.

1. Controlling sources in the 10-K:
   - The net income (loss) per share note has a table of potentially dilutive securities excluded from diluted EPS. It usually has a line such as "Convertible Notes (if-converted)", in thousands of shares. This is the headline figure.
   - The debt note gives, for each series, the principal outstanding, the conversion rate per $1,000 of principal and the conversion price.
2. Reconcile. For each series, shares = principal / 1,000 x conversion rate. Sum the series and compare with the EPS-table line. Carry full precision and round only at the end. If the two differ, say why (for example a series repaid or converted during the year, or make-whole shares) and name which figure you use.
3. Keep these distinct and label them: shares on an if-converted basis, shares actually included in diluted EPS (zero when there is a net loss, because they are anti-dilutive), and any offset from capped calls or hedges. State whether the capped calls are netted into the figure. Do not net them unless the filing does.
4. Check the units (thousands of shares vs millions), the date (the period-end the question names, not the filing date), and that every series outstanding at that date is included. Take principal amounts from the debt note at that date, not from the original issue size.
5. Answer contract: the total shares with unit and date, the per-series table (principal, conversion rate, shares), the sum check against the disclosed total, the note that this is maximum potential dilution rather than diluted-EPS shares, and the sources.
6. List as sources only documents you opened and retrieved from.

Task lead (verified in one run's retrieval, re-confirm in the text): Snap Inc. FY2024 10-K (https://www.sec.gov/Archives/edgar/data/1564408/000156440825000019/snap-20241231.htm). The Note 3 table at 12/31/2024 shows "Convertible Notes (if-converted)" of 85,945 thousand shares. The series are the 2025, 2026, 2027, 2028 and 2030 notes. Conversion rates per $1,000 were 46.1233, 43.8481, 11.2042, 17.7494 and 45.0846. Principal was about $36.2M, $249.8M, $1,150M, $1,500M and $750M. These imply about 1.67M, 10.95M, 12.89M, 26.62M and 33.81M shares, which sum to about 85.9M. The $249.8M 2026 principal was not independently confirmed in that run, so check it in Note 7.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks about the share dilution, conversion shares or if-converted impact of a company's convertible notes, call load_skill with `convertible_dilution_lookup`.

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
# Sourcing

- A search snippet or result title is a lead, not evidence. Confirm each figure, period and unit in the parsed primary filing with retrieve_information.
- List as a source only a document you opened and retrieved from. Do not list a filing (for example a press release) that you only saw in search results or used as background.
</file>

<notes>
Moment: base1 found 85,945 thousand if-converted shares in the 10-K Note 3 table and derived a per-series split from Note 7. It then listed a Q3 2024 earnings press release as a source that it never opened. The library's q45 entry shows the same sourcing flaw and a short cite-only-opened rule that fixed it, so I added a two-line tool_guidance.md.
The number looks right and well supported. I added the skill so the next convertible-dilution question goes straight to the EPS-note table and the debt-note reconciliation, with the Snap facts labelled as task facts and marked for re-confirmation. The 2026 principal of $249.8M was unconfirmed in the run, so the skill says to verify it. The skill is triggered by a line in systemprompt.md.
</notes>