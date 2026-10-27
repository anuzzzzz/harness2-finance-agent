Merged the two candidates into one always-on `tool_guidance.md`. The skill and the `systemprompt.md` trigger are dropped. Neither candidate's run shows the skill helping, and the procedure is short.

<file path="tool_guidance.md">
# Tool use

- Decide the documents before searching: company, form (8-K EX-99.1 press release, Form 425, merger-agreement 8-K, 10-K or 10-Q) and event date. Use edgar_search with company and date filters. Never send a null or empty query. If web_search returns nothing, retry once with a short non-empty query, then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. Confirm each figure, its unit and its basis in the retrieved text. parse_html_page cannot read PDFs; use the HTML exhibit instead. Do not parse a very large S-4 or proxy for headline deal terms when the press release, 425 or 8-K already state them. If you search it, use input_character_ranges.
- Deal-price questions ("what price was X acquired at"): from opened documents retrieve (a) the per-share consideration and its form (cash, stock with an exchange ratio, or mixed), (b) equity value, (c) enterprise value and what it includes. For a stock deal, give the exchange ratio and the implied acquirer price (headline value / ratio), and say the value floats with the acquirer's share price until closing. Say whether the deal has closed as of April 07, 2025; if not, say "agreed to be acquired" and give the expected closing. Check equity value / per-share price against a plausible diluted share count.
- When two sources give different values for the same measure (for example enterprise value), report both, each with its source and whether it came from an opened document or only a snippet. Lead with the figure you confirmed in opened text. Do not call one "more precise" or "rounded" unless an opened document supports that.
- Respect the as-of date (April 07, 2025). Do not use documents dated after it.
- Cite only documents you opened and retrieved from. Do not list a PDF, article or filing seen only in search results as a source. If a figure came only from a snippet, say so in the text.
- Write the final answer in plain text with no citation markup (no <cite> tags). State each figure with its unit and source, then any check, then the conclusion in the form the question asks for. Submit with submit_final_result as soon as the figures are verified.

Leads for this task (Rocket Companies, RKT, agreeing to acquire Redfin, RDFN; announced March 10, 2025). These come from search results only, so re-confirm in the opened text:
- Reported terms: all-stock, fixed ratio 0.7926 RKT Class A shares per RDFN share, about $12.50 per share at signing, equity value about $1.75B. Enterprise value is about $2.4B in Redfin's filings and about $2.36B in Rocket's investor presentation (a PDF that cannot be parsed).
- Rocket press release (8-K EX-99.1): https://www.sec.gov/Archives/edgar/data/1805284/000095014225000696/eh250601250_ex9901.htm
- Redfin Form 425 FAQ: https://www.sec.gov/Archives/edgar/data/1382821/000162828025014827/redfin-425faqsround2.htm
- Redfin 8-K merger agreement (Item 1.01 states the ratio, equity value and EV): https://www.sec.gov/Archives/edgar/data/1382821/000162828025011457/rdfn-20250309.htm
</file>

<notes>
kept -> inv1 (snippets-are-leads, open primary docs, no null queries, cite only opened docs, plain text) -> base1 opened nothing and listed 5 unopened sources; inv1 and dom1 each opened the press release, FAQ and 8-K/425 and submitted (6 and 4 turns).
kept -> inv1 (deal-price procedure: consideration form, equity value, EV composition, pending status, implied checks) -> both candidates' final answers cover form, status and the equity-value/price cross-check; base1 never verified these from opened text.
revised -> dom1 skill announced_acquisition_terms, folded into always-on tool_guidance and skill deleted -> dom1 loaded it but the same content reached inv1 without a skill; the procedure is short and the library shows skills with no observed effect.
dropped -> dom1 systemprompt.md trigger line -> goes with the removed skill; leaving it would reference a missing skill.
revised -> both candidates' EV handling -> both still listed the unopened investor-presentation PDF as a source and inv1 called $2.36B "precise" without an opened source; the new rule says lead with the opened figure, report both, and keep snippet-only figures out of the sources list.
revised -> inv1 S-4 handling -> inv1 parsed the 1.1M-character S-4 and spent two retrievals finding no EV or price, while the 8-K and 425 already held the terms; added a rule not to parse the S-4 for headline terms.
kept -> leads block (URLs, reported figures) from both candidates, trimmed -> dom1 reached the answer in 4 turns with direct URLs; labelled for re-confirmation. The 8-K URL was added because inv1 found the $1.75B/$2.4B sentence there.
</notes>