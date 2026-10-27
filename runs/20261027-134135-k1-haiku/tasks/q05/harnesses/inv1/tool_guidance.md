# Tool guidance

Before searching, decide which document and period the question needs: company, form type (10-K, DEF 14A proxy, 8-K item, press release exhibit) and the calendar or fiscal year named in the question. Search with those filters, not the question's wording. Use only documents dated on or before April 07, 2025.

- `edgar_search`: pass the ticker or CIK, a date range covering the year the question names, and the form type. If it returns 0 results, change the filters once. If it still returns nothing, use `web_search` once for the primary document. Do not repeat an empty `web_search`.
- `parse_html_page`: store each primary document under a clear key (for example `bbsi_def14a_2024`). Open the primary filing before answering. A search snippet or a third-party page (news sites, aggregators) is a lead, not evidence.
- `retrieve_information`: ask one targeted question at a time, and quote the sentence or row verbatim with its date. On long filings, use `input_character_ranges`.

Enough evidence means the answer was read from a primary document that was actually opened and retrieved, and that document's year matches the year in the question. Do not say a fact was "read from" a filing unless a retrieve call returned it. Name the document and section for each fact.

Board, nominee and officer questions ("who was nominated, appointed or elected in <year>"):
- The governing documents are the proxy statement (DEF 14A) filed that year, which lists the nominees and states which are new, and any 8-K Item 5.02 filed that year. Open the proxy first, in the same turn as the 8-K, and retrieve the full nominee list with each person's status (incumbent or new nominee, and who recommended the nominee).
- Match the verb and the year in the question. "Nominated in 2024" is a proxy-year event, and an "appointed" event in a different year does not answer it. Do not answer with a person from a later-dated filing. If such a later filing (for example a 2025 proxy) mentions a 2024 process, treat it only as a lead and confirm in the 2024 documents.
- If the proxy names several nominees, say which are new and which are re-nominated incumbents, then answer the question as asked. If the question could mean either, give the new nominee(s) first and list the full slate.
- In this task (BBSI, CIK 0000902791), `edgar_search` with ciks ["BBSI"] and dates 2024-01-01 to 2025-04-07 returns the 2024 DEF 14A (filed 2024-04-22, https://www.sec.gov/Archives/edgar/data/902791/000095017024046428/bbsi-20240422.htm), the PRE 14A (filed 2024-04-10) and the 8-K of 2024-06-05 on the annual meeting vote. The first run submitted a name from an April 2025 press release without opening any of these, and did not find the 2024 nominee.

Before `submit_final_result`, re-check that the person, the action (nominated, appointed or elected) and the year match the question, and that each came from an opened document. Write plain text with no citation tags. Submit while budget remains.
