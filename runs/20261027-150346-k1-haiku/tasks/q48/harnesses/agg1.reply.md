Adopted inv1's tool_guidance wholesale, plus one line about garbled tables, and no skill.

<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (8-K EX-99.1 release or shareholder letter, 10-Q, 10-K) and fiscal period. Use edgar_search with company and date filters rather than the question's wording. If web_search returns nothing, retry once with a short non-empty query (never an empty one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP basis in the retrieved text. Use input_character_ranges on long documents.
- parse_html_page cannot read PDFs. Use the HTML 8-K exhibit or filing instead.
- Guidance-versus-actual questions need two opened documents. The guidance is in the release for the quarter BEFORE the period being judged, in its full-year column. The actual is in the release for the period itself. Retrieve every guided metric from the guidance document with its low and high ends. Retrieve the matching actual for each metric from the results document. Prefer a stated full-year figure to a sum of quarters. If you must sum quarters, say so and cross-check against a full-year figure.
- Compare like with like: the same metric definition, the same period (full year, not a quarter) and the same unit. Compute against the range (below, within or above) and the midpoint. For a loss metric, say plainly whether the loss was smaller (better) or larger (worse) than guided. Carry full precision and round only the final number.
- If a parsed table looks garbled, say so and cross-check it against the document's own text or a second opened source. A document that parsed successfully does not make a figure correct. Re-check each figure in the calculation against the retrieved text before submitting.
- Cite only documents you opened and retrieved from. Do not list a filing, article or PDF seen only in search results, and do not attribute a figure to a document you did not retrieve it from. If a figure came from a snippet only, say so plainly.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. State each figure with its period, unit and source, then the calculation, then the conclusion in the form the question asks for. Submit with submit_final_result as soon as the figures are verified.

Leads for this task (Lemonade FY2024 vs the Q3 2024 full-year guidance; taken from search snippets only, so re-confirm in the opened text):
- Guidance document: the Q3 2024 shareholder letter, 8-K EX-99.1, 2024-10-30, https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm. Its FY2024 column was reported to give: IFP about $940-944M, GEP $823-826M, revenue $522-524M, Adjusted EBITDA loss ($155)-($151)M.
- Results document: the Q4 2024 shareholder letter, 8-K EX-99.1, https://www.sec.gov/Archives/edgar/data/1691421/000169142125000021/lmndshareholderletterq42.htm. Look for a full-year GEP figure there instead of summing quarters.
- Check units ($ millions) and that the Adjusted EBITDA loss is compared with the right sign.
</file>

<notes>
kept -> inv1 tool_guidance.md -> base1 ran four web_searches, never parsed anything, listed about eight unopened sources and leaked <cite> markup; inv1 parsed both letters in turn 1, retrieved the full-year GEP of 827.3 directly, cited only the two opened letters and wrote plain text. 1 base rollout versus 1 inv rollout; the difference is a single-sample contrast.
revised -> inv1 tool_guidance.md -> added one line on garbled tables, taken from dom1's Q3 retrieval, which flagged the guidance table as garbled and cross-checked it. Also added loss-smaller-is-better wording, from dom1's verdict handling. These lines are small and apply to every run.
dropped -> dom1 skill guidance_vs_actual_range and its systemprompt trigger line -> dom1 and inv1 reached identical figures and verdicts with clean sourcing, and dom1 spent an extra turn loading the skill. The skill's content is already covered by tool_guidance, so its separate effect is unproven. Two other points support dropping it: it would be always-on trigger text, and the same lessons are already in the library as q47 and q09.
kept -> task leads in tool_guidance.md -> both candidate runs skipped discovery search because of the leads, and both re-retrieved the figures from the opened text. They are marked unverified. Their transfer value is low; they cost about 1.2k characters, well under the cap.
no unsubmitted rollout: base1, inv1 and dom1 all submitted, so no edit is flagged unsafe.
</notes>