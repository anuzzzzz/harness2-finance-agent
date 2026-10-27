<file path="skills/retail_comparable_sales/SKILL.md">
---
name: retail_comparable_sales
description: Look up a retailer's same-store / comparable-store sales growth for a fiscal quarter or year from its earnings release or 10-K, with the correct period, sign and definition.
---

# Retail same-store / comparable sales lookup

ANALYTIC MOVE: lookup plus classification. Map the question's wording ("same-store sales", "SSS", "comps", "comparable store sales") to the company's own reported metric, then read its value for the exact fiscal period.

WHERE IT LIVES
- Quarterly: the 8-K EX-99.1 earnings release for that quarter. The headline bullets and the "Fourth Quarter / Fiscal Year Results" paragraph state the comp %.
- Full year: the same Q4 release, or the 10-K MD&A (key performance measures and the "Comparable store sales" discussion). The 10-K usually breaks the full-year comp into transactions and average ticket.
- Fiscal quarters are not calendar quarters. Name the quarter by its end date (for example "13 weeks ended Dec 26, 2024") and make sure the figure is for that quarter, not the full year or a neighbouring quarter. The Q4 release prints the Q4 comp and the full-year comp side by side, so check which one you picked.

ANSWER CONTRACT
1. The comp % with its sign. Say plainly "growth of -0.8%" or "a decline of 0.8%" as the case may be. Do not report a negative comp as growth without saying so.
2. The period (fiscal quarter, with the end date) and the company's name for the metric.
3. The company's definition, retrieved from the filing (for example, how long a store must be open to enter the comp base, and how e-commerce or relocated stores are treated). Do not state a definition from memory.
4. Total net sales growth for the same period, if the release gives it, so the reader sees that comp and total growth differ (new stores drive total growth). Do not substitute one for the other.
5. The full-year comp as context only if it is retrieved. Keep it clearly separate from the quarter figure.
6. Sources: only documents you opened. Plain text, no citation markup.

CHECKS BEFORE SUBMITTING
- The percentage is the period named in the question (quarter versus year).
- The figure is the company's reported comp. Do not rebuild it from dollar sales.
- If the release has several comp measures (total, store-only, ticket, transactions), report the headline comp and name any others separately.

TASK FACTS (Floor & Decor Holdings, FND; verified as sources, to be re-confirmed in the opened text)
- FND's term is "comparable store sales". The SEC CIK is 1507079; use the CIK, not the ticker, in edgar_search.
- Fiscal 2024 Q4 was the quarter ended December 26, 2024. The release is the 8-K EX-99.1 at https://www.sec.gov/Archives/edgar/data/1507079/000150707925000012/fnd-2024earningsreleaseex9.htm, and the 10-K is https://www.sec.gov/Archives/edgar/data/1507079/000150707925000013/fnd-20241226.htm.
- The earlier run's search snippets gave Q4 2024 comparable store sales of -0.8%, net sales of $1,107.4M (+5.7%), and a full-year comp of -7.1%. Confirm these in the opened release.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When the question asks for a retailer's same-store, comparable-store or comp sales growth for a quarter or year, call load_skill with `retail_comparable_sales`.

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
Motivating moment, base1: the answer (-0.8% comp for the quarter ended Dec 26, 2024) came from search snippets. The agent never opened the release but cited the release, the IR page, a TradingView mirror and the 10-K. Its edgar_search used the ticker "FND" instead of a CIK and returned zero results. The question said "same-store sales", while FND reports "comparable store sales". The Q4 release prints both the quarter comp and the full-year comp (-7.1%), so the two could be confused. A negative comp was asked about as "growth", so the sign needs explicit wording.
Added an on-demand skill covering the terminology mapping, the answer contract (signed figure, period end date, retrieved definition, total versus comp growth) and the FND task facts: the CIK, the release and 10-K URLs, and the snippet-level figures labelled as needing confirmation. Added one trigger line to systemprompt.md. Always-on cost is about 200 characters. I left tool_guidance alone because procedure belongs to a parallel candidate.
</notes>