<file path="skills/peer_payout_ratio_ranking/SKILL.md">
---
name: peer_payout_ratio_ranking
description: Compare one company's dividend payout ratio with its competitors for a fiscal year and rank them, on one stated definition, with an adjusted-basis comparison.
---

# Peer dividend-payout ranking

**Analytic move:** retrieve the same two lines for every company from its own FY filing, calculate on one basis, rank.

**Procedure**
1. Before searching, write down (a) the fiscal year and each company's year-end (52/53-week years differ), and (b) the peer set with a one-line reason per peer. Peers are listed direct competitors in the same industry that file 10-Ks. Take them from the target's 10-K competition discussion and standard industry lists. A peer that pays no common dividend goes in the ranking at 0.00% and is labelled a non-payer, with the filing language quoted. Do not silently drop non-payers or add unrelated companies. Explain any exclusion (for example bottlers or non-U.S. filers) in one clause.
2. Headline definition, applied identically to every company: **common dividends paid (cash flow statement, financing section) ÷ net income attributable to common shareholders (GAAP, income statement)**, both for the same fiscal year. Name the table, period and units of each figure. A web_search excerpt of the statement is acceptable if the filing cannot be opened. Say which you used.
3. Cross-check with dividends per share ÷ GAAP diluted EPS. Declared and paid dividends differ in timing, so say which per-share figure you used. Use an annual declared total, not an annualized current rate, unless you label it. If the two methods rank differently, say so and keep the cash-based ranking as the headline. Never mix methods across companies. Never take a third-party precomputed "payout ratio" as an input; use it only as a labelled cross-check.
4. Adjusted ratio (dividends per share ÷ company non-GAAP/core/comparable EPS) is a labelled secondary comparison. Always show it when GAAP earnings carry large one-offs (impairments, restructuring, settlements), because those can change the ranking. If the GAAP and adjusted rankings differ, state that in one sentence, with the one-off that causes it.
5. Re-check before submitting: both inputs come from the same fiscal year for every company, units match (millions vs thousands), per-share and total-dollar ratios for one company roughly agree (explain any gap), and the sort order matches the numbers. Recompute each ratio from unrounded inputs once and round only at the end, to two decimals.
6. Answer contract: a ranked list from highest to lowest with the ratio to two decimals, the dividends and net income behind each ratio, the definition, the peer-set rationale, the target's position in the ranking, the adjusted comparison, and the source of each figure (opened filing or search excerpt). Plain text with no raw citation tags, ending with the sources dictionary.
</file>

<file path="systemprompt.md">
You are a financial agent. You are given a question and you need to answer it using the tools provided.
You will not be able to interact with the user or ask clarifications, you must answer the question only based on the information provided.

You should answer all questions as if the current date is April 07, 2025.

You will have access to a data storage system. You can use this system to store parsed contents of HTML pages retrieved from the web.
You can then use the retrieve_information tool to apply answer questions or gather information from the stored documents using LLM-based prompts.
This data storage system is designed to help you avoid context window issues.

When a question asks you to compare or rank a company's dividend payout ratio (or a similar payout, yield or margin ratio) against competitors or peers, call load_skill with `peer_payout_ratio_ranking`.

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
# Tool use

- Fix the companies, form type (10-K) and fiscal year before searching. Search with company, form, year and the statement or line item (for example "PepsiCo 10-K 2024 consolidated statement of cash flows dividends paid"), not the question's wording. Always pass a non-empty `query`.
- Several companies can be searched in one turn, but search results are only leads. Each figure that enters a calculation must be seen as text for the right company and period, not as a title or URL.
- `edgar_search` and `parse_html_page` on sec.gov often return HTTP 403 here, and `parse_html_page` cannot read PDFs. Start with `web_search`. Do not call `edgar_search` repeatedly after a failure. Make one targeted `web_search` per missing figure and read the statement from the excerpt. You may try `parse_html_page` once on a non-sec.gov HTML copy; if it works, store it under a clear key and ask `retrieve_information` one targeted question at a time.
- Cite only URLs that appeared in tool output. Say whether each figure came from an opened filing or a search excerpt.
- Do arithmetic on unrounded numbers, re-check it once, and round only the final result.
- Write the answer as plain text with no raw citation tags. Once the figures are in hand and re-checked, call `submit_final_result` right away.
</file>

<notes>
kept -> inv1 (skill, cash-dividends-paid ÷ net income primary definition, DPS/EPS cross-check) -> base1 mixed paid vs declared DPS against impairment-depressed GAAP EPS and used a third-party payout field; inv1 applied one definition across all peers and cross-checked, in 2 turns with no 403 flailing.
kept -> dom1 (GAAP vs adjusted comparison, peer-set sourcing from 10-K, non-payer handling, per-share vs total-dollar agreement check) -> dom1 flagged that the KDP ranking flips between GAAP and adjusted (impairments), which base1 noted only in a caveat; merged into the single skill as a required labelled comparison.
revised -> inv1/dom1 skills merged into one skill `peer_payout_ratio_ranking` with one trigger line -> the two skills overlap almost entirely; one skill avoids duplicate procedure and one trigger line is enough.
kept -> inv1 tool_guidance -> dom1 (no guidance) made 4 consecutive edgar_search calls that all returned 403 in turn 2, while inv1 went straight to targeted web_search; softened to "start with web_search" because the evidence is 1 rollout per side.
dropped -> inv1 inclusion of Celsius as a default peer -> peer set is a judgement call and only one run added it; the skill leaves peer choice to the agent with a stated rationale instead of hard-coding it.
dropped -> any embedded task figures -> neither candidate read the figures from opened filings, so none were stored.
</notes>