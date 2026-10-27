---
name: board_nominee_lookup
description: Identify who was nominated, elected or appointed to a company's board in a given year, using the proxy statement (Proposal 1) and 8-Ks, and separate new nominees from incumbents.
---
ANALYTIC MOVE: classify and trace. Determine which people were nominated for the board in the year the question names, and which of them (if any) are new.

1. Pin the event. "Nominated in YEAR" means the slate in the proxy statement (DEF 14A) filed in YEAR for that year's annual meeting, normally Proposal 1 "Election of Directors". It is different from "appointed" (8-K Item 5.02 or a press release) and from "elected" (8-K Item 5.07 vote results). State which event your answer is.
2. Controlling sources, in order:
   - the DEF 14A filed in YEAR (edgar_search with form_types DEF 14A and the year's dates). Open it with parse_html_page and retrieve the full nominee list, each person's status (new, continuing, re-nominated), and any sentence naming a new nominee, a Nominating Committee recommendation, or a director not standing for re-election.
   - the YEAR 8-K Item 5.07 for the vote results, to confirm the nominees were elected.
   - 8-K Item 5.02 and company press releases for mid-year appointments or departures.
   - the prior-year or following-year DEF 14A, only if status or a board search is described there.
3. The primary answer is the person or slate on the YEAR proxy. A later filing's narrative (for example a following-year proxy describing a search run in YEAR) or a later appointment is a different event: report it separately and labelled, with its own date and source, and only if you retrieved it from an opened document. Do not present it as the YEAR nominee unless the YEAR proxy says so.
4. Answer contract: the full YEAR slate with each person's status and any roles the proxy states; the event and date for each; any later or related appointment shown separately; the sources actually opened.
5. Check before submitting: the nominee count matches the number of directors elected in the 8-K; the meeting date and year match the question.

Leads for BBSI (Barrett Business Services, CIK 902791), re-confirm in the text: 2024 DEF 14A https://www.sec.gov/Archives/edgar/data/902791/000095017024046428/bbsi-20240422.htm (filed 2024-04-22). 8-K for the June 3, 2024 annual meeting https://www.sec.gov/Archives/edgar/data/902791/000095017024069322/bbsi-20240603.htm. Two runs read these: eight incumbents were nominated and elected (Carley, Clabby, Cusick, Kramer, Meeker, Moradi, Morehouse, Price), and the proxy names no new nominee. Mark S. Finn was appointed effective April 7, 2025 (press release and 2025 DEF 14A https://ir.bbsi.com/sec-filings/all-sec-filings/content/0000950170-25-056284/bbsi-20250421.htm), after a Nominating Committee search that the 2025 proxy says ran in 2024. Mention him as a separate, labelled item only if you open one of those documents.
