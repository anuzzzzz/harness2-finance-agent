---
name: board_nominee_lookup
description: Identify who was nominated, elected or appointed to a company's board in a given year, using the proxy statement (Proposal 1) and 8-Ks, and separate new nominees from incumbents.
---
ANALYTIC MOVE: classify and trace. Determine which people were nominated for the board in the year the question names, and which of them (if any) are new.

1. Pin the event. "Nominated in YEAR" means the slate in the proxy statement (DEF 14A) filed in YEAR for that year's annual meeting, normally Proposal 1 "Election of Directors". It is different from "appointed" (8-K Item 5.02 or a press release) and from "elected" (8-K Item 5.07 vote results). State which event your answer is.
2. Controlling sources, in order:
   - the DEF 14A filed in YEAR (use edgar_search with form_types DEF 14A and the year's dates). Open it with parse_html_page and retrieve the full nominee list, plus any sentence saying who is a new nominee, was recommended by the Nominating Committee, or is not standing for re-election.
   - the YEAR 8-K Item 5.07 for the vote results, to confirm the nominees were elected.
   - 8-K Item 5.02 and company press releases for mid-year appointments or departures.
   - the prior-year DEF 14A, only if the new-versus-incumbent status is not stated in the current one.
3. Do not answer from a later filing's narrative (for example a 2025 proxy describing a 2024 search) unless the nominee was in the YEAR proxy. A person appointed or selected after the YEAR slate was set is a different answer from the YEAR nominees. Report both if the question is ambiguous, with the primary answer being the person on the YEAR proxy slate.
4. Answer contract: the full list of nominees on the YEAR slate, with each person's status (incumbent or new) and any committee or chair role the proxy states; the event and date for each; any later appointment shown separately and labelled; the sources actually opened.
5. Check before submitting: the count of nominees matches the number of directors elected in the 8-K; the proxy's fiscal-year and meeting date match the question's year.

In this task (BBSI, Barrett Business Services, CIK 902791), leads to re-confirm in the text: the 2024 DEF 14A is https://www.sec.gov/Archives/edgar/data/902791/000095017024046428/bbsi-20240422.htm (filed 2024-04-22; PRE 14A 2024-04-10). The 8-K reporting the June 3, 2024 annual meeting is https://www.sec.gov/Archives/edgar/data/902791/000095017024069322/bbsi-20240603.htm and says eight directors were elected. A base run answered "Mark S. Finn" from the 2025 proxy and an April 7, 2025 press release, without opening the 2024 proxy. Finn's appointment was effective April 7, 2025, so he was not on the 2024 slate. Read the 2024 DEF 14A nominee list and check whether it identifies a new nominee.
