Merged: inv1's general tool rules, plus one concentration-disclosure line from dom1's skill. I dropped the Shift4 leads and the skill.

<file path="tool_guidance.md">
# Tool use

- Decide the filing and period before searching: company, form type and fiscal period. For a year-end disclosure question, use edgar_search with the company name, form 10-K and a date range, or open a known primary URL. Never send web_search an empty or null query. If a search returns thin results, retry once with a short non-empty query, then use edgar_search.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key), then ask retrieve_information one targeted question at a time. Use input_character_ranges on long filings. Confirm the figure, period and unit in the retrieved text.
- A retrieval answer that ends mid-sentence or says it is truncated is incomplete. Re-ask a narrower question (one section, or one character range) before concluding that something is not disclosed. State "not disclosed" only after the relevant note and the risk-factor section have each been queried.
- Do not name a counterparty, vendor, bank or percentage in the answer unless a retrieved passage from an opened document states it. If you infer it, label it as an inference. Do not cite a document that you did not open. In particular, do not cite a prospectus or press release seen only in a snippet, and do not carry an older-period disclosure into a current-period answer.
- Concentration or dependency questions (vendor, supplier, customer, sponsor bank): check the Note 1 concentration paragraph and the Item 1A risk factors in the as-of-year 10-K. Quote each dependency and say how many counterparties it covers and whether the filing names them. Say whether any share or amount is quantified, and give the exit terms and backup language as stated. Report customer, reseller or merchant percentage limits separately from the vendor dependency.
- Keep the answer in plain text, with no citation markup. State each figure with its period, unit and source section. End with the sources dictionary in the prescribed format. Submit with submit_final_result as soon as the figures are verified.
</file>

<notes>
kept -> inv1 (general tool_guidance rules: truncation re-ask, no unverified names, cite only opened docs, no null queries) -> base1 asserted "Citizens Bank" after the retrieved note named no bank, cited an unopened 2020 424B4, and used a null-query search. inv1 avoided all three and submitted in 3 turns.
revised -> inv1 -> removed the Shift4-specific leads (URL and facts): they are task-specific, and the run still parsed the 10-K directly. They carry no transfer value and cost always-on characters.
revised -> dom1 -> folded the skill's core content (Note 1 plus Item 1A, named or not, quantified or not, exit terms, offsetting concentrations kept separate) into a single tool_guidance line instead of a skill. dom1 took 5 turns against 3 for inv1 with equivalent content. Earlier library entries (q47-q49) also showed no skill benefit over always-on guidance.
dropped -> dom1 skill and systemprompt trigger line -> the skill's extra effect is not isolated from the inv1 run, which reached the same answer, quality and sourcing without it. It added load turns, and its embedded Shift4 facts are task-specific.
kept -> base -> the systemprompt, guardrails and memory are unchanged. The base sources-dictionary requirement is restated in tool_guidance because base1 omitted the dictionary.
</notes>