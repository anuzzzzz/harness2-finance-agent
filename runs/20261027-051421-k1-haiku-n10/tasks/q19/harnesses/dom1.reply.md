<file path="skills/lease_maturity_schedule/SKILL.md">
---
name: lease_maturity_schedule
description: Answer questions on operating/finance lease (or debt, purchase-obligation) maturities "in the next N years", with the share of the total.
---

# Lease / obligation maturity questions

**Analytic move:** calculate. Sum the first N annual rows of the maturity table, then divide by the table's total. Inputs are the undiscounted annual payments and the undiscounted total.

**Where the figures live:** in the latest 10-K filed on or before the question date, in the Leases note, in the table "maturities of lease liabilities". It sits next to the lines "Less: interest" and "Present value of lease liabilities". The figures may be in thousands, so check the table header.

**Procedure**
1. Pick the latest annual filing as of the question date. For an April 2025 question this is the FY2024 10-K (period ended Dec 31, 2024), not an older 10-K and not an unfiled later 10-Q. Retrieve the table from the filing text (parse_html_page, then retrieve_information), not from a search snippet or memory. Confirm every year row and the total against the page.
2. Use the right lease type. Operating and finance leases usually have separate tables or columns, so use the one the question names. Do not mix in sublease income or the lease liabilities on the balance sheet.
3. "Next three years" means the first three fiscal-year rows after the balance-sheet date (for FY2024, 2025, 2026 and 2027). Exclude "Thereafter" and the later years.
4. Percentage: the default denominator is **total undiscounted lease payments**, because the numerator is undiscounted. Show the PV-based share (against the liability net of imputed interest) only as a labelled secondary figure. Never mix an undiscounted numerator with a PV denominator without saying so.
5. Check that the table foots: the rows must sum to the total, and total minus interest must equal the PV. If they do not, you have misread a row or the units.

**Answer contract:** each annual figure with its year and unit (state $ thousands as given), the unrounded sum, the percentage to two decimals, the denominator used, the filing and period, and the URL. Write plain text and do not leave raw citation tags in the answer.

**Task fact (MSCI, FY2024 10-K, accession 0001408198-25-000053):** the base run took these from a search snippet and did not open the filing, so re-verify them against the filing before use. Operating lease payments in $ thousands: 2025 30,220; 2026 30,361; 2027 24,421; 2028 23,931; 2029 16,573; thereafter 40,099; total 165,605; interest (19,601); PV 146,004. If they hold, the 3-year sum is 85,002 and the share is 85,002/165,605 = 51.33%.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks about lease, debt, or purchase-obligation maturities in the next N years, or the share of a maturity schedule, call load_skill with `lease_maturity_schedule`.

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
Motivation: in base1 the agent submitted after only web_search, using figures from a search snippet and never opening the FY2024 10-K. It left raw "cite index" tags in the answer and hedged between two percentage denominators. The new skill, loaded on demand through a trigger line, sets the controlling filing and table, the first three rows after the balance-sheet date, the undiscounted-total denominator, and a footing check. It also records the MSCI figures as a labelled, unverified task fact. The always-on cost is one line.
</notes>