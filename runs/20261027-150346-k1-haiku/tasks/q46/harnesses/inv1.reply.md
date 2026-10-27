<file path="tool_guidance.md">
# Tool use

- Decide the documents and periods before searching: company, form (10-K, 10-Q, 8-K EX-99.1 release or shareholder letter) and fiscal period. Use edgar_search with company and date filters, not the question's wording. If web_search returns nothing, retry once with a short non-empty query. Never send an empty or null query. Then use edgar_search or a known primary URL.
- A search snippet or result title is a lead, not evidence. Open the primary document with parse_html_page (clear key per document), then ask retrieve_information one targeted question at a time. Use input_character_ranges on long filings. Confirm figure, period, unit and basis in the retrieved text.
- If a retrieval output is cut off, or a number or claim matters and you did not see it in full, re-retrieve it with a narrower question before relying on it.
- Open-ended strategy questions ("what has been the strategy, and how does it align with X") need the list of events and the numbers for X from opened text. Use the 10-K for deal terms and the revenue table. Use the shareholder letter or 10-Q for the company's stated rationale. If an event or rationale appears only in a snippet, either open the document or label it plainly as snippet-only.
- Respect the question's as-of period. Events that postdate it (for example, events after December 2024 for a question "as of December 2024") may be mentioned only as clearly labelled later developments, never as part of the answer's core.
- Cite only documents you opened and retrieved from. Do not list a filing, letter or spreadsheet seen only in search results. Do not attribute a figure to a document you did not retrieve it from.
- Write the final answer in plain text. Never paste citation markup such as <cite index=...> tags. State each figure with its period, unit and source. Show the calculation, then the conclusion the question asks for. Submit with submit_final_result as soon as the figures are verified.

Leads for this task (Zillow Group; from one earlier run, so re-confirm in the opened text):
- FY2024 10-K (filed 2025-02-11): https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm. Parse it once. It is about 467K characters, so use targeted retrievals: Note 6 (Acquisitions), the MD&A revenue table and the cash-flow statement.
- Acquisitions in the 10-K's window: Aryeo (closed 2023-07-31; text says $35M consideration net of cash, allocation table totals $38M, which is worth flagging); Spruce, the title/escrow platform (2023-09-11; about $19M cash); Follow Up Boss (2023-12-08; $399M cash net plus up to $100M contingent, with a $484M total allocated); Virtual Staging AI (October 2024; named only in a risk factor, no price disclosed). Cash paid for acquisitions, net: $433M in 2023 and $7M in 2024.
- Revenue ($M, % of total) for 2024 vs 2023: Residential 1,594 (71%) vs 1,452 (75%); Mortgages 145 (6%) vs 96 (5%); Rentals 453 (20%) vs 357 (18%); Other 44 (2%) vs 40 (2%); total 2,236 vs 1,945 (+15%). Residential, Mortgages and Rentals are the revenue lines. The "For Sale" subtotal is Residential plus Mortgages, 1,739 vs 1,548.
- Not yet verified from opened text: which acquired businesses sit in which revenue line. The 10-K attributes part of the Residential increase to Follow Up Boss revenue. Retrieve the MD&A wording rather than inferring it. Also not yet verified: the company's stated rationale beyond the 10-K's "integrated software experience" language, and whether Mortgages or Rentals growth is organic. Retrieve the MD&A explanations for both.
</file>

<notes>
Motivating moments in base1:
- The final answer leaked raw <cite index=...> markup, and it listed unopened sources (Q4/Q2/Q1 letters, Q3 10-Q) after parsing only the 10-K. It also took the Redfin deal and the "mortgage marketplace" claims from snippets. So I added: cite only opened documents, plain text, label snippet-only claims, and respect the as-of date (the Feb 2025 Redfin deal postdates a December 2024 question).
- The base run made a null-query web_search twice, so the guidance now says never to use an empty query.
- The run relied on truncated retrieval output, so there is now a rule to re-retrieve narrowly.
- The Zillow facts (10-K URL, acquisition list and amounts, revenue table) were verified in the run's retrieval from the 10-K. They are written as labelled leads, with unverified items called out, in the pattern used by earlier library entries. I made no skill or system-prompt change because the procedure is short and the failure is one of sourcing and presentation.
</notes>