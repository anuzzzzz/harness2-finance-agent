<file path="skills/non_gaap_adjustment_lookup/SKILL.md">
---
name: non_gaap_adjustment_lookup
description: Retrieve a company's full-year non-GAAP reconciling adjustment (e.g. stock-based compensation in Adjusted EBITDA) from the 10-K and cross-check it.
---

# Non-GAAP adjustment for a fiscal year

ANALYTIC MOVE: read one line item of the company's non-GAAP reconciliation (Adjusted EBITDA, adjusted net income, free cash flow) for the full fiscal year the question names.

WHERE THE FULL-YEAR FIGURE LIVES
1. Governing source: the 10-K for that fiscal year. The reconciliation is in MD&A under "Non-GAAP Financial Measures" or "Key Business Metrics and Non-GAAP", with an annual column. Use `edgar_search` with form 10-K and the ticker to get the URL.
2. Cross-checks, all from the same 10-K:
   - Cash flow statement (operating section) shows the stock-based compensation add-back.
   - The equity note or the income statement footnote gives SBC by function.
   - The MD&A line item should equal these, unless the reconciliation excludes some items. If they differ, report the reconciliation line as the answer, say why they differ, and give both.
3. The Q4 8-K Exhibit 99.1 shareholder letter often shows only quarterly columns. Do not build a full-year figure by adding four quarters when one quarter has not been read from the table. A derived sum is a fallback only. If you use it, label it as derived and read every quarter from a document.

ANSWER CONTRACT
- The figure with fiscal year, units (millions or thousands) and the exact row label from the reconciliation.
- The prior-year comparative from the same table.
- The document and table it came from, and the cross-check result.
- If asked for the "adjustment", state the sign. An add-back is positive in the reconciliation.

CHECKS BEFORE SUBMIT
- The column is the full fiscal year, not a quarter or nine months.
- Units match the table header.
- The figure agrees across the reconciliation, the cash flow statement and the SBC footnote, or the difference is explained.
- Name the `retrieve_information` call that produced the figure and quote the row.

IN THIS TASK (Airbnb, FY2024; verified only as locations, not values)
- The 10-K is https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm (accession 0001559720-25-000010). The Q4 letter is https://www.sec.gov/Archives/edgar/data/1559720/000119312525026054/d915198dex991.htm.
- The earlier run parsed only the letter. The letter's reconciliation is quarterly, and its extraction was garbled. The run never opened the 10-K. It summed the quarters (295, 382, 362 and an unconfirmed Q4 of 368 = 1,407), which it flagged as least verified.
- Treat 1,407 as a lead. Confirm the annual figure in the 10-K reconciliation and the cash flow statement. Use `input_character_ranges` or a targeted prompt on the 10-K for "Stock-based compensation expense" in the Adjusted EBITDA table. If the Q4 quarter is below the nine-month-to-year difference, resolve it.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks for a non-GAAP reconciling adjustment (e.g. stock-based compensation in Adjusted EBITDA) for a fiscal year, call load_skill with `non_gaap_adjustment_lookup`.

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
Motivating moment: base1 parsed only the Q4 shareholder letter, whose reconciliation had no full-year column and extracted garbled. It then summed quarterly SBC figures, including a Q4 value (368) it admitted it could not confirm. It cited the 10-K but never opened it, and submitted a derived 1,407 as the annual figure. The edit adds a skill that sends the agent to the 10-K annual reconciliation, with the cash flow statement and the SBC footnote as cross-checks. It forbids silently summing quarters and labels 1,407 as an unverified lead. It does not assert a value. The always-on cost is a single trigger line in systemprompt.md.
</notes>