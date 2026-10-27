I'm adding one short `tool_guidance.md`. The base run reached a reasonable answer, but one step was thin and two procedural gaps are visible, so no skill is needed.

<file path="tool_guidance.md">
# Tool use

- Decide the document and period before searching: company, form (10-K), fiscal year. Use edgar_search with company, form type and date filters. Note that a fiscal year may not match the calendar year, so check the period-ending date in the result.
- A search snippet is a lead, not evidence. Open the primary filing with parse_html_page (one clear key per document), then ask retrieve_information one targeted question at a time. parse_html_page cannot read PDFs.
- Summarizing a section of a filing (for example Item 1A risk factors):
  - First retrieve the exact list of risk-factor headings and the section subheadings, in order. Treat that list as the map of what the filing says.
  - Then retrieve the substance of each heading that bears on the question, one or two headings per call. Use input_character_ranges on a long filing. Retrieve outputs can be truncated, so re-ask in smaller pieces rather than relying on a cut-off answer.
  - Cover regulatory points that sit under non-regulatory headings (cybersecurity, financial matters, operations, general risks), but label them as such and separate them from the filing's own regulatory subheading.
  - State "the filing does not mention X" only if a targeted retrieval over the risk-factor text came back empty. Otherwise say the point was not found in the retrieved passages. Never present a negative from a single summary retrieval as established fact.
- Before submitting, reread the draft against the retrieved text. Every item must trace to a retrieved passage. Cut anything that does not.
- Cite only documents you opened and retrieved from. Write plain text with no citation markup. Submit with submit_final_result as soon as the summary is verified.

Task fact (in this task, from one earlier run; re-confirm in the text): Paylocity's FY2024 10-K covers the fiscal year ended June 30, 2024 and was filed 2024-08-02: https://www.sec.gov/Archives/edgar/data/1591698/000159169824000151/pcty-20240630.htm. Its Item 1A has a "Legal and Regulatory Matters" group with three headings:
  1. changes in regulatory laws or requirements applicable to its software and services (this includes money transmitter and AI sub-risks);
  2. failure to comply with data privacy laws and regulations (HIPAA, GDPR, CCPA);
  3. adverse tax laws or regulations.
Further regulatory-flavored points sit elsewhere, in the cybersecurity, financial matters, operations and general risk groups.
</file>

<notes>
Single base run: edgar_search → parse → 3 retrievals → submit, with no tool errors. The one weak step was turn 5 and the final answer. A retrieve_information call about whether ERISA, ACA, FCPA and government-contract language appears was turned into a flat statement that "the filing does not include separate risk factors" on them. That is a negative claim from an LLM summary, and the retrieval itself said it had no formatting to go on. The first retrieval also came back truncated, and the run re-asked with a "skip items 1–2" prompt, so it never fully re-checked the first item.

The guidance therefore adds four things:
- map the headings first;
- retrieve in small pieces so output is not truncated;
- gate absence claims on a targeted empty retrieval;
- re-check the draft against retrieved text before submitting.

It also records the verified task facts (fiscal year ended June 30, 2024, the URL, the three Legal and Regulatory headings), which were retrieved in the run. I kept the file short and added no skill, because this is a single retrieval-and-summary task with no multi-step procedure that needs one.
</notes>