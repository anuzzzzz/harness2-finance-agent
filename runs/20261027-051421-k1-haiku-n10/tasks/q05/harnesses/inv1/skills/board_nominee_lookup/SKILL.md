---
name: board_nominee_lookup
description: Identify who was nominated, appointed or elected to a company's board in a stated year, using the filings dated in that year and the later filings that describe it.
---

# Board nominee / appointment lookup ("who was nominated to the board in year Y")

**Analytic move:** retrieve and disambiguate. "Nominated", "appointed", "elected" and "selected" are different events with different dates and different filings. The question's verb and year choose which one.

**Sources, in order**
1. The proxy statement (DEF 14A) filed in year Y, section "Election of Directors" / "Nominees": the slate the board put forward for the year-Y annual meeting. A DEFA14A or the voting-results 8-K (Item 5.07) gives the same slate and outcome.
2. 8-Ks filed in year Y, Item 5.02: appointments, resignations and new nominees between meetings. Check every 8-K the search returns for year Y; do not skip one because its title is generic.
3. The press-release page on the company IR site for year Y.
4. The next year's proxy (DEF 14A filed in Y+1): its "Nominating Committee" / "Director selection" text often describes searches done in year Y. This is retrospective. It tells you who was identified or selected, not necessarily when the board formally acted.

**Procedure**
1. Write down, before searching: the company, the year Y, the verb used, and which of the sources above matches it.
2. Open the year-Y source for that verb (parse_html_page on the IR-site URL, store it, then retrieve_information). Ask for the full nominee list, and for each person: new or incumbent, date of nomination or appointment, and committee/independence details. Do not rely on a snippet list.
3. Open the year Y+1 proxy too, and compare. If a name appears only in the retrospective text and not in a year-Y filing, say that, and give the date of the formal action.
4. If the year-Y filings show a newly named person (new nominee or appointee) and a different person was only selected in year Y but seated later, report both with their dates and say which one best fits the question's verb. Lead with the one the question's wording and year point to. Do not choose by default the person from the latest filing.
5. Re-check before submitting: the name spelling, the date, the event type, and that every claimed slate or list was seen in opened text. State whether each fact came from an opened filing or a search excerpt.

**In this task (BBSI, Barrett Business Services), facts seen so far; re-verify before use**
- The 2025 DEF 14A (ir.bbsi.com, filed April 21, 2025) says the Nominating Committee searched in 2024 and the Board selected Mark S. Finn; his election was effective April 7, 2025. This paragraph was opened.
- The 2024 slate (eight names: Carley, Clabby, Cusick, Kramer, Meeker, Moradi, Morehouse, Price) came only from a DEFA14A search snippet and was not opened. A June 5, 2024 8-K at ir.bbsi.com appeared in search results and was not opened. Open both, and the 2024 DEF 14A, before concluding who was "nominated" in 2024.

**Answer contract:** the name(s), the event type and date for each, the filing and section that establish it, whether each source was opened or an excerpt, and the URL. Plain text, no raw citation tags.
