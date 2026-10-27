<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching. For a "guidance vs actual" question you need two documents: the release or letter that issued the guidance, and the release that reports the actual result. Name the company, form (8-K EX-99.1 shareholder letter or earnings release, 10-Q, 10-K) and fiscal period. Prefer edgar_search with company and date filters. If web_search returns nothing, retry once with a shorter query, then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Every figure that enters a calculation, both the guided range and the actual, must be read from a document you opened with parse_html_page (one clear key per document) and queried with retrieve_information. Ask one targeted question at a time. Confirm the figure, period, unit and basis in the retrieved text. Use input_character_ranges on long documents.
- If a parsed document shows signs of being a draft or has internal editing notes, or two places in it disagree, cross-check the figure in a second opened source before relying on it. Examples are the next quarter's letter, which restates prior guidance, and the earnings call transcript. If you cannot cross-check, say so plainly.
- parse_html_page cannot read PDFs. Use the HTML exhibits from edgar_search.
- Cite only documents you opened and retrieved from. Do not attribute a figure to a document you saw only in search results.
- Write the final answer in plain text with no citation markup such as <cite> tags. State each figure with its period, unit and source, then the calculation, then the result in the form the question asks for. Submit with submit_final_result as soon as the figures are verified.

Task facts (Shift4 Payments, FOUR; one run read these, so re-confirm them in the text):
- The Q1 2024 shareholder letter (https://www.sec.gov/Archives/edgar/data/1794669/000179466924000014/ex991q1.htm) has a slide "Breaking Down Our 2024 Guidance by Quarter". It gives Q3 2024 end-to-end payment volume of $46.0B to $48.0B, so the midpoint is $47.0B. Its Q2 range is $39.0B to $41.0B, and its full-year range is $167B to $175B. The parsed text carried draft markers.
- The Q3 2024 shareholder letter is https://www.sec.gov/Archives/edgar/data/1794669/000179466924000031/ex991q3.htm. A search snippet showed Q3 2024 E2E volume of $43.5B. That snippet was not opened, so retrieve it from the letter.
- The question asks about E2E payment volume, not gross payment volume.
- Variance against the midpoint is (actual - midpoint) / midpoint. Use the unrounded inputs and label the answer BEAT or MISS.
</file>

<notes>
Moments in base1:
- Parsed only the Q1 letter. The Q3 actual ($43.5B) came from a search snippet, and the Q3 letter was listed as a source without ever being opened. The new rule requires both the guidance and the actual to be read from opened documents.
- The Q1 letter text contained draft markers ("WORD DOC v9", "change to #s from Nancy") and an internal inconsistency ($183B vs $175B). The agent only caveated this. The new line asks for a cross-check in a second opened source.
- The final answer leaked `<cite index>` markup. The new line requires plain text.
- Task facts are labelled and carry the verified guidance range and the URLs. The actual figure is marked as unverified.
</notes>