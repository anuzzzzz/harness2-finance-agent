I'm changing only `tool_guidance.md`; the base run's failures were in how it sourced and presented the answer, not in what it concluded.

<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (8-K EX-99.1 release or shareholder letter, 10-Q, 10-K) and fiscal period. Use edgar_search with company and date filters rather than the question's wording. If web_search returns nothing, retry once with a short non-empty query (never an empty one), then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm the figure, period, unit and GAAP/non-GAAP basis in the retrieved text. Use input_character_ranges on long documents.
- parse_html_page cannot read PDFs. Use the HTML 8-K exhibit or filing instead.
- Guidance-versus-actual questions need two opened documents. The guidance is in the release for the quarter BEFORE the period being judged, in its full-year column. The actual is in the release for the period itself. Retrieve every guided metric from the guidance document with its low and high ends. Retrieve the matching actual for each metric from the results document. Prefer a stated full-year figure to a sum of quarters. If you must sum quarters, say so and cross-check against a full-year figure.
- Compare like with like: the same metric definition, the same period (full year, not a quarter) and the same unit. Compute against the range (below, within or above) and the midpoint. Carry full precision and round only the final number.
- Before submitting, re-check each figure in the calculation against the retrieved text. A document that parsed successfully does not make a figure correct.
- Cite only documents you opened and retrieved from. Do not list a filing, article or PDF seen only in search results, and do not attribute a figure to a document you did not retrieve it from. If a figure came from a snippet only, say so plainly.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. State each figure with its period, unit and source, then the calculation, then the conclusion in the form the question asks for. Submit with submit_final_result as soon as the figures are verified.

Leads for this task (Lemonade FY2024 vs the Q3 2024 full-year guidance; taken from search snippets only, so re-confirm in the opened text):
- Guidance document: the Q3 2024 shareholder letter, 8-K EX-99.1, 2024-10-30, https://www.sec.gov/Archives/edgar/data/1691421/000169142124000128/lmndq32024shlfinal103024.htm. Its FY2024 column was reported to give: IFP about $940-944M, GEP $823-826M, revenue $522-524M, Adjusted EBITDA loss ($155)-($151)M.
- Results document: the Q4 2024 shareholder letter, 8-K EX-99.1, https://www.sec.gov/Archives/edgar/data/1691421/000169142125000021/lmndshareholderletterq42.htm. Snippets reported FY2024 IFP $944M, Adjusted EBITDA loss ($150)M and revenue about $526.5M. Look for a full-year GEP figure there instead of summing quarters.
- Check units ($ millions) and that the Adjusted EBITDA loss is compared with the right sign.
</file>

<notes>
Motivation: base1 ran four web_searches and then submitted, so it parsed and retrieved nothing. Every actual and guidance figure came from snippets (or, for GEP, from quarterly letters it never opened). It summed four quarters to get GEP instead of finding the full-year figure. It listed about eight sources it never opened, including a PDF and a proxy statement, and leaked raw <cite index> markup into the answer.

The edit is a tool_guidance rewrite in the same direction as the q47 and q09 library entries: snippets are leads only, both the guidance document and the results document must be opened, cite only what was opened, write plain text, and re-check figures before submitting. I generalised it as guidance-vs-actual procedure. It names the prior-quarter release as the guidance source and prefers a stated full-year figure over a sum of quarters.

The Lemonade facts (URLs, guided ranges, reported actuals) are labelled as unverified snippet leads, because no run opened either letter. I added no skill: the procedure is short and always applies to this question type. The q47 evidence showed a separate skill added no observable effect beyond tool_guidance.
</notes>