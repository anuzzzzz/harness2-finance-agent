<file path="skills/dividend_payout_peer_compare/SKILL.md">
---
name: dividend_payout_peer_compare
description: Compare dividend payout ratios across a company and its competitors for a fiscal year and rank them, on one consistent basis from each company's 10-K.
---

# Dividend payout ratio: peer comparison and ranking

**Analytic move:** compare. Inputs are, for each company, FY dividends and FY earnings. The result is a ranked list on one basis.

## Definition (state it in the answer)
Payout ratio = common dividends ÷ net income attributable to common shareholders, for the same fiscal year.
- Primary basis: aggregate cash dividends paid (cash flow statement, financing section, "dividends paid" or "cash dividends paid") ÷ GAAP net income attributable to the company (income statement).
- Use the same basis for every company. Do not divide dollars by dollars for one company and per-share by per-share for another.
- Per-share declared dividends ÷ diluted GAAP EPS is an acceptable cross-check, and it is the fallback only if the aggregate paid figure cannot be retrieved. If you fall back, say so and apply it to every company.
- Dividends declared and dividends paid differ by timing (a Q4 dividend declared in December may be paid in January). Say which one you used.
- GAAP and adjusted/non-GAAP payout differ materially when there are impairments or one-offs. Rank on GAAP. Add one line showing the adjusted figure only if the company's own release reconciles it.

## Peer set
- Competitors means direct peers in the same line of business that file with the SEC and have FY2024 data. For Coca-Cola, start from PepsiCo, Keurig Dr Pepper and Monster Beverage. Add other listed bottlers or beverage peers only if you can open their filings (for example Coca-Cola Consolidated).
- State the peer set in the answer. A company that pays no dividend has a payout ratio of 0% and goes last. Show it rather than omitting it.
- Fiscal year ends differ (for example PepsiCo's FY2024 ends in late December and KDP's on Dec 31). Use each company's fiscal 2024 and state the period end.

## Where the figures live
- 10-K Item 8: the consolidated statements of cash flows (dividends paid), and the income statement (net income attributable to shareowners, diluted EPS).
- Equity statement or notes: dividends declared per share.
- Do not use aggregator pages (payout ratio TTM on MarketBeat, GuruFocus and similar) as the figure. They use different periods and bases. Only filings dated on or before April 07, 2025 count.

## Task facts to re-verify (found in a prior run, not yet confirmed from opened documents)
- In this task, Coca-Cola's 10-K reportedly shows dividends paid of $8,359M in 2024 and net income attributable to shareowners of $10,631M, a ratio of about 78.63%. Confirm both from the opened 10-K (cash flow statement and income statement).
- The earlier run did not retrieve PepsiCo's or KDP's aggregate dividends paid, and it mixed bases. Retrieve each company's cash-flow dividends and net income from its own FY2024 10-K.

## Answer contract
1. A ranked list from highest to lowest payout ratio, with Coca-Cola's rank clearly marked.
2. A table per company with: fiscal year end, dividends ($M), net income attributable to the company ($M), ratio to two decimals, and the source document.
3. The arithmetic shown, unrounded until the end.
4. The basis stated (paid vs declared, GAAP) and the peer set stated.
5. Before submitting, confirm every figure comes from an opened primary document (not from memory or search snippets), and that the period, units (millions) and share count basis match across companies.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question compares dividend payout ratios (or dividend payouts against earnings) across a company and its competitors, call load_skill with `dividend_payout_peer_compare`.

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
Motivation (base1): the run answered from search snippets and opened no filing. It mixed bases: aggregate dollars for KO ($8,359M / $10,631M) but per-share declared dividends over diluted EPS for PepsiCo and KDP. It added a KO cross-check using an EPS figure ("$2.46") that it admitted was not in its sources. It also built KDP's dividend as nine-month plus a guessed Q4 amount. Because of the mixed bases, the ranking (KDP > KO > PEP > MNST) is shaky. The new skill, loaded by a trigger line, fixes the definition (cash dividends paid ÷ GAAP net income attributable), requires the same basis for every peer, fixes the peer set and the placement of non-payers, and says where the figures live in the 10-K. It also records KO's figures as labelled leads to re-verify, not as established facts. Skill form was chosen because the trigger (a payout-ratio peer comparison) is recognisable and the content is reusable across the research desk. The always-on cost is one trigger line.
</notes>