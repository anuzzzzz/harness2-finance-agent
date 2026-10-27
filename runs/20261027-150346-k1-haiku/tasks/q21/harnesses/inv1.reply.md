<file path="tool_guidance.md">
# Tool use

- Decide the filing and period before searching: company, form type and fiscal period. For a year-end disclosure question, use edgar_search with the company name, form 10-K and a date range, or open a known primary URL. Never send web_search an empty or null query. If a search returns thin results, retry once with a short non-empty query, then use edgar_search.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key), then ask retrieve_information one targeted question at a time. Use input_character_ranges on long filings. Confirm the figure, period and unit in the retrieved text.
- A retrieval answer that ends mid-sentence or says it is truncated is incomplete. Re-ask a narrower question (one section, or one character range) before concluding that something is not disclosed. State "not disclosed" only after the relevant note and the risk-factor section have each been queried.
- Do not name a counterparty, vendor, bank or percentage in the answer unless a retrieved passage from an opened document states it. If you infer it, label it as an inference. Do not cite a document that you did not open. In particular, do not cite a prospectus or press release seen only in a snippet, and do not carry an older-period disclosure into a current-period answer.
- Keep the answer in plain text, with no citation markup. State each figure with its period, unit and source section. Submit with submit_final_result as soon as the figures are verified.

Leads for this task (Shift4 Payments, FY2024 vendor concentration; verified in the base run's retrieval, re-confirm in the opened text):
- Primary source: FY2024 Form 10-K, filed 2025-02-19, https://www.sec.gov/Archives/edgar/data/1794669/000179466925000011/four-20241231.htm (about 535k characters when parsed).
- In this task, the governing text is Note 1, "Summary of Significant Accounting Policies", under the heading "Concentration Risk" (about p. 85). It says North American merchant processing is facilitated by one unnamed vendor, and it gives no percentage or amount. The same note covers the dependence on a member-bank sponsor (180 days to find a replacement).
- In this task, Item 1A also says that in the U.S., EU and Canada the company depends on a single third-party processor. Query Item 1A once more for the exact wording and for any other concentration (for example, VAR or merchant shares) so that the answer is complete rather than truncated.
</file>

<notes>
Motivated by base1: its retrieve_information output was truncated (1,464 chars cut), and the agent still concluded from partial text. It also added an unverified claim that Citizens Bank is the sponsor and cited a 2020 424B4 it never opened, using a snippet's two-vendor claim. It issued a null-query web_search too. The new tool_guidance.md adds bounded rules for truncation, unverified names and sources, and no null queries. It also records the verified facts about this task's source (10-K URL, Note 1 Concentration Risk, Item 1A single processor). No skill was added, because the procedure is short.
</notes>