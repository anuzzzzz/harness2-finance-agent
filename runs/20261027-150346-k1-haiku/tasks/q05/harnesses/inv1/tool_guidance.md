# Tool use

- Decide the document and period before searching: company, form (10-K, 10-Q, 8-K, DEF 14A), and the calendar or fiscal year the question names. Use edgar_search with company, form_types and date filters, not the question's wording. If web_search returns 0 results or is called with an empty query, retry once with a short non-empty query, then use edgar_search.
- A search snippet, result title or press-release summary is a lead, not evidence. Open the primary document for the period asked about with parse_html_page (clear key per document), then ask retrieve_information one targeted question at a time. Confirm the name, date, event and period in the retrieved text.
- Match the event and year to the question. If the question asks what happened in year X, the answer must come from year-X filings. If the best evidence is from a different year (for example a 2025 appointment for a 2024 question), do not substitute it silently. Check the year-X filing first, then say plainly how the other-year item relates.
- For "who was nominated/elected/appointed" questions, the answer may be a slate rather than one person. Retrieve the full nominee list and any named new nominee, with each person's status (new, continuing or re-nominated), and answer what the question asks, not an adjacent event.
- Cite only documents you opened and retrieved from. Do not list a filing as a source, or attribute a fact to it, unless you retrieved that fact from it.
- Write the final answer in plain text with no citation markup. Give the answer first, then the supporting facts with dates and sources. Submit with submit_final_result as soon as the facts are verified in primary text.

Task leads (BBSI, CIK 902791; found by edgar_search, contents not yet verified, so re-confirm in the text):
- The 2024 proxy is DEF 14A filed 2024-04-22: https://www.sec.gov/Archives/edgar/data/902791/000095017024046428/bbsi-20240422.htm. Its "Election of Directors" or nominee section is the controlling source for who was nominated in 2024. A PRE 14A was filed 2024-04-10.
- The 8-K for the June 3, 2024 annual meeting (filed 2024-06-05) reports the vote: https://www.sec.gov/Archives/edgar/data/902791/000095017024069322/bbsi-20240603.htm.
- An earlier run answered "Mark S. Finn" from snippets of the 2025 proxy and an April 7, 2025 appointment release. It never opened the 2024 DEF 14A, so that answer was not checked against the 2024 nominee list.
