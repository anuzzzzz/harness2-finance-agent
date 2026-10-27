I merged the INV tool guidance (revised) with the DOM skill (task fact removed) and left `LongTermMEMORY.md` empty. All three rollouts submitted the same answer, so the evidence supports process edits only. The edits are meant to save wasted turns on SEC 403 errors and to make the sourcing statement honest.

<file path="tool_guidance.md">
# Tool use

- Decide the company, form type (10-K / 10-Q) and fiscal period first. As of the question date, use the latest filing already published.
- SEC endpoints often return HTTP 403 here. `edgar_search` failed in every run that tried it, and `parse_html_page` on sec.gov URLs also returned 403. Do not retry a 403 and do not loop on index pages. Go straight to `web_search` (company, form, fiscal year, and the specific table or line item). Results often include the filing text and give the sec.gov URL.
- You may try `parse_html_page` once on the filing URL, then `retrieve_information` for targeted questions. If the parse fails, work from the search excerpt.
- A figure seen only in a search excerpt must be described as such in the answer. Never call it "verified against the filing" unless you opened the filing. Still check period, units (thousands vs millions) and whether the figure is discounted or undiscounted, and check that the table foots.
- Do the arithmetic on unrounded numbers, re-add the components once, and round only the final result.
- Write the answer as plain text, with no raw citation tags. Submit with `submit_final_result` as soon as the figures are in hand. Do not spend the remaining budget on extra searching.
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

<file path="skills/lease_maturity_schedule/SKILL.md">
---
name: lease_maturity_schedule
description: Answer questions on operating/finance lease (or debt, purchase-obligation) maturities "in the next N years", with the share of the total.
---

# Lease / obligation maturity questions

**Analytic move:** calculate. Sum the first N annual rows of the maturity table, then divide by the table's total. Inputs are the undiscounted annual payments and the undiscounted total.

**Where the figures live:** in the latest 10-K filed on or before the question date, in the Leases note, in the table "maturities of lease liabilities". It sits next to the lines "Less: interest" and "Present value of lease liabilities". The figures may be in thousands, so check the table header.

**Procedure**
1. Pick the latest annual filing as of the question date. For an April 2025 question this is the FY2024 10-K (period ended Dec 31, 2024), not an older 10-K and not a later 10-Q that was not yet filed. Get the table from the filing text where possible (see tool guidance for 403 fallbacks), not from memory. Confirm every year row and the total.
2. Use the right lease type. Operating and finance leases usually have separate tables or columns, so use the one the question names. Do not mix in sublease income or the balance-sheet lease liabilities.
3. "Next three years" means the first three fiscal-year rows after the balance-sheet date (for FY2024: 2025, 2026 and 2027). Exclude "Thereafter" and the later years.
4. Percentage: the default denominator is **total undiscounted lease payments**, because the numerator is undiscounted. Show the PV-based share (against the liability net of imputed interest) only as a labelled secondary figure. Never mix an undiscounted numerator with a PV denominator without saying so.
5. Check that the table foots: the rows must sum to the total, and total minus interest must equal the PV. If not, you have misread a row or the units.

**Answer contract:** each annual figure with its year and unit (state $ thousands as given), the unrounded sum, the percentage to two decimals, the denominator used, the filing and period, and the URL. Plain text, no raw citation tags. Say plainly if the table came from a search excerpt rather than the opened filing.
</file>

<notes>
kept -> inv1 tool_guidance (revised) -> edgar_search returned 403 in 2/2 rollouts that used it (base1 turns 1-2, dom1 turns 2-3) and parse_html_page on sec.gov returned 403 in 2/2 (inv1 turn 1, dom1 turn 4). I rewrote the guidance to say 403s are common and to go straight to web_search. I dropped the "edgar_search first" preferred chain.
revised -> inv1/dom1 verification wording -> dom1 labelled the figures "Verified" while it only had a search excerpt. The guidance now requires saying plainly when the figures came from a search excerpt.
kept -> dom1 skill lease_maturity_schedule plus its trigger line in systemprompt -> it fixes the first-three-rows rule, the undiscounted denominator, the footing check and plain-text citations. This addressed the base1 hedge between two denominators and its leftover cite tags. All three rollouts reached the same figures, so this is a modest quality gain at low always-on cost (one line).
dropped -> task-specific MSCI figures in dom1's skill and inv1's LongTermMEMORY -> they are unverified (no run opened the filing) and tied to one task. In memory they would be always-on and could mislead other tasks. LongTermMEMORY stays empty.
dropped -> inv1's "confirm snippet figures in the filing text" as a hard step -> the filing was unreachable (403) in 2/2 runs that tried it, so it is now a conditional statement of limitation.
</notes>