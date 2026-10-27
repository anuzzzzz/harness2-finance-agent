<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1), fiscal periods. Use edgar_search with the company CIK, form type and dates. If web_search returns 0 results, retry once with a short non-empty query (never an empty or null query), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document). Then ask retrieve_information one targeted question at a time. Confirm each figure's period, unit and basis in the retrieved text before it enters a calculation.
- parse_html_page cannot read PDFs. Use the HTML 10-K, 10-Q or 8-K EX-99.1.
- Multi-year ratio or trend questions: a 10-K carries comparative columns (income statement three years, key metrics often only two). Take each year from the latest filing that carries it, and open the older 10-K only if a year is missing. When the same year appears in two filings, check that the figures agree and say if one was restated.
- Carry full precision through the calculation and round only the final figure (two decimals for ratios and percentages). Recompute each ratio once from the retrieved inputs before submitting.
- Cite only documents you opened and retrieved from. Do not list a filing as a source, or attribute a figure to it, unless that figure was retrieved from it. Say plainly if a figure came from a comparative column in a different year's filing.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. Follow the shape the question asks for (for example one line per year plus a one-sentence comment), then give the inputs with period, unit and source, and the calculation. Submit with submit_final_result as soon as the figures are verified.
</file>

<notes>
kept -> inv1 tool_guidance general rules (snippet is a lead, cite only opened documents, plain text with no markup, no empty-query search, comparative-column sourcing) -> base1 leaked cite markup, listed the unopened FY2022 10-K, and opened with a null-query search (1/1 base). inv1 and dom1 both fixed all of these and submitted with the same correct 13.29/13.54/13.57 (2/2 candidates).
revised -> inv1 tool_guidance -> removed the embedded Airbnb task facts (figures, URLs). They carry no transfer value to later tasks, and the agent retrieved the numbers from the filings in every run anyway.
kept -> dom1 answer-shape point -> base1 added extra paragraphs beyond "each year on a separate line plus a one-sentence comment". Folded into one general sentence in tool_guidance (follow the shape the question asks for) instead of a skill.
dropped -> dom1 skill marketplace_take_rate and its systemprompt trigger -> dom1 took 4 turns against inv1's 3 with the same answer. The skill's content (the volume metric covers fewer years, use the older 10-K) is covered by the comparative-column rule, and the skill's separate effect was not isolated (dom1 also carried the tool_guidance rules).
kept -> systemprompt.md unchanged -> no evidence for a change; no rollout failed to submit (base1, inv1, dom1 all submitted).
</notes>