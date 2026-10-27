I composed the final harness from `inv1`'s tool guidance, without its task-specific leads and with one added fiscal-quarter rule. No skill and no other file changes.

<file path="tool_guidance.md">
# Tool use

- Decide the documents and period before searching: company, form (8-K press release, 10-Q, 10-K) and fiscal period. Use edgar_search with company, form and date filters, not the question's wording. If web_search returns nothing, retry once with a short non-empty query (never an empty or null one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm the wording, period and unit in the retrieved text. Use input_character_ranges on long filings.
- parse_html_page cannot read PDFs. Use the HTML filing or exhibit.
- For "when is X expected" questions, the answer is management's stated expectation as of the question's date. Open the announcement release and the latest periodic filing (10-Q or 10-K) filed on or before that date. Quote each expectation with its filing date. If they differ or were revised, give the latest one and name the earlier one. State the expectation the question asks about first. Any later status (for example, that production has since started) goes after it as a labelled update, from an opened document only.
- Fiscal labels: when a filing says "second quarter of 2025" or similar, check the company's fiscal year-end on the cover page and convert the label to calendar months. Do not read a fiscal quarter as a calendar quarter, and do not call a past-tense statement in a filing inconsistent without first checking the fiscal calendar.
- Cite only documents you opened and retrieved from. Do not list a filing or article seen only in search results, and do not attribute a quote to a document you did not retrieve it from.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags or truncated quotes. State the answer first, then the supporting quotes with filing and date. Submit with submit_final_result as soon as the figures are verified.
</file>

<notes>
kept -> inv1 tool_guidance (open primary docs, cite only opened, plain text, expectation rule) -> base1 ran 2 searches and opened nothing, leaked <cite> markup, truncated a quote mid-word and listed unopened SEC filings as sources; inv1 and dom1 each parsed the press release, 10-K and 10-Q and did not leak markup (1 base failure, 0 of 2 candidate repeats).
revised -> inv1 task-specific leads dropped -> the URLs and facts came from snippets and carry no transfer value; both candidates retrieved the same facts from the opened text, so the leads are not needed.
revised -> added fiscal-label conversion line (from dom1's skill step 3) -> dom1's final answer called the 10-Q's "second quarter of 2025" inconsistent with a February 2025 filing date and left it unresolved, while inv1 resolved it as Aug-Oct 2024 fiscal Q2. A short always-on rule is cheaper than a skill.
dropped -> dom1 skill milestone_timing_lookup and its systemprompt trigger line -> the procedure is short and fits in tool guidance. Despite the skill's fiscal-year step, dom1 still left the fiscal ambiguity open, and it also issued a null-query web_search, so the skill showed no advantage over inv1's skill-free run (1 rollout each).
dropped -> dom1 Smucker task facts -> unverified snippet leads with no transfer value.
</notes>