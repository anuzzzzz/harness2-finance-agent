<file path="tool_guidance.md">
# Tool guidance

Before searching, decide which document and period the question needs: company, form type (10-K, DEF 14A proxy, 8-K item, press release exhibit) and the calendar or fiscal year named in the question. Search with those filters, not the question's wording. Use only documents dated on or before April 07, 2025.

- `edgar_search`: pass the ticker or CIK, a date range covering the year the question names, and the form type. If it returns 0 results, change the filters once. If it still returns nothing, use `web_search` once for the primary document. Do not repeat an empty `web_search`.
- `parse_html_page`: store each primary document under a clear key (for example `co_def14a_2024`). Open the primary filing before answering. A search snippet or a third-party page (news sites, aggregators) is a lead, not evidence.
- `retrieve_information`: ask one targeted question at a time, and quote the sentence or row verbatim with its date. On long filings, use `input_character_ranges`.

Enough evidence means the answer was read from a primary document that was actually opened and retrieved, and that document's year matches the year in the question. Do not say a fact was "read from" a filing unless a retrieve call returned it. Name the document and section for each fact.

Board, nominee and officer questions ("who was nominated, appointed or elected in <year>"):
- The governing documents are the proxy statement (DEF 14A) filed that year, which lists the nominees and states which are new, and any 8-K Item 5.02 or 5.07 filed that year. Open the proxy first, in the same turn as any 8-K, and retrieve the full nominee list with each person's status (incumbent or new nominee).
- Match the verb and the year in the question. "Nominated in 2024" is a proxy-year event, and an "appointed" event in a different year does not answer it. Do not answer with a person from a later-dated filing. If a later filing mentions the earlier year's process, treat it only as a lead and confirm in that year's documents.
- If the proxy names several nominees, give the full slate, and say which are new and which are re-nominated incumbents. If none is new, say so plainly. Answer the question as asked.

Before `submit_final_result`, re-check that the person, the action (nominated, appointed or elected) and the year match the question, and that each came from an opened document. Write plain text with no citation tags. Submit while budget remains.
</file>

<notes>
kept (revised) -> inv1 tool_guidance -> base1 never opened the 2024 DEF 14A it had found and submitted a 2025 appointee; inv1 opened it at turn 1, retrieved the 8-nominee slate and submitted in 4 turns at $0.016. I removed the BBSI-specific URL block, since the library lessons say company facts in guidance are confounding and not reusable, and added 5.07 from dom1.
dropped -> dom1 skill board_nominee_lookup and systemprompt trigger -> dom1 spent turn 1 on load_skill and reached the same slate as inv1 in 6 turns; the library shows skills adding a load turn with no gain, and it embedded task-specific facts. dom1's content on 8-K and slate handling is folded into the tool guidance in short form.
kept -> systemprompt.md unchanged -> no evidence for changing it; no rollout failed to submit (base1, inv1 and dom1 all submitted).
</notes>