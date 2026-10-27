<file path="skills/non_gaap_adjustment_lookup/SKILL.md">
---
name: non_gaap_adjustment_lookup
description: Retrieve a specific adjustment line (e.g. stock-based compensation) from a company's Adjusted EBITDA / non-GAAP reconciliation for a fiscal year.
---

# Non-GAAP adjustment lookup ("what was the adjustment for X in year Y")

**Analytic move:** retrieve and reconcile. The answer is one line of the company's own reconciliation table for the stated fiscal year, with its units and a check that the table foots.

**Where the figure lives**
- Q4/full-year earnings release (8-K Exhibit 99.1): the "Reconciliation of Net Income to Adjusted EBITDA" table, with quarterly and full-year columns. Use the full-year column for a "in 2024" question, not the Q4 column.
- 10-K, MD&A, "Adjusted EBITDA" or "Non-GAAP Financial Measures" section: the same table for the fiscal year, with the prior year beside it.
- The cash flow statement and the stock-based compensation footnote also report a stock-based compensation figure. It can differ from the add-back because of capitalized amounts, restructuring-related items, or items shown on other lines. For an "adjustment" question the reconciliation line is the controlling figure. Mention the cash-flow figure only if it differs, and label it.

**Procedure**
1. Fix the fiscal year the question names and the measure (Adjusted EBITDA vs free cash flow vs non-GAAP net income). Each has its own reconciliation and can list the same item separately.
2. Read the line from the opened document (the reconciliation table in the 10-K or release), not from memory. Record the unit in the table header (millions or thousands).
3. Foot the table: net income plus every listed adjustment must equal Adjusted EBITDA, with the correct signs. If the sum does not match, you misread a line, a column or a year.
4. Give the prior-year comparative from the same table, and the year-over-year change, only if useful for context. Do not add figures the question did not ask for.
5. Answer contract: the adjustment amount with year and units, the table it came from (document, section), Adjusted EBITDA and net income for the same year as the footing evidence, and the URL. If the figure came from a search excerpt rather than an opened filing, say so.

**This task's sources (Airbnb, FY2024):** the FY2024 10-K is at https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm. The Q4 2024 shareholder letter is at https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf. In the earlier run the stock-based compensation add-back (about $1,407M) was reported without the table having been opened and footed, so treat it as unconfirmed until the table is read and foots.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks for a specific adjustment or add-back in a non-GAAP reconciliation (Adjusted EBITDA, adjusted net income, free cash flow), such as stock-based compensation, call load_skill with `non_gaap_adjustment_lookup`.

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

<notes>
Moment: in base1 the agent hit 403s on edgar_search, then submitted $1,407M for Airbnb's 2024 SBC add-back without any visible retrieval of the reconciliation table. It cited a 10-Q (Q3) that was not among its search results. No footing check was shown and the source basis was not disclosed. I added a skill giving the practitioner knowledge: the full-year column of the Adjusted EBITDA reconciliation (10-K MD&A / Q4 release Ex. 99.1) is the controlling source; the cash-flow SBC figure can differ; the table must foot to Adjusted EBITDA; units and source basis must be stated. It also records verified source URLs from the search results for this task, and flags the $1,407M figure as unconfirmed rather than encoding it as fact. The trigger line is in systemprompt.md. I left tool guidance to the procedure candidate.
</notes>