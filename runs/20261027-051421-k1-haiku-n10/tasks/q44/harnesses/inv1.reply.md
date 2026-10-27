<file path="tool_guidance.md">
# Tool guidance

**Order of work:** Before searching, decide the company, form type (10-K, 10-Q, 8-K earnings exhibit or shareholder letter) and fiscal period the question needs. Search with those filters, not with the question's wording.

**Chain:** Use edgar_search (or web_search for the primary document URL), then parse_html_page to store the document under a clear key, then retrieve_information. Ask retrieve_information one targeted question at a time. On long filings, use input_character_ranges instead of re-reading everything.

**edgar_search failure** (for example a 403 on the ticker lookup): do not repeat the same call.
- Make one retry with the numeric CIK instead of the ticker if you know it.
- Otherwise switch to web_search. Always give web_search a non-empty query with the company, form and year, for example "Airbnb 2024 10-K sec.gov".
- Look for the primary document: sec.gov/Archives, or the company investor-relations site or its CDN.
- Then run parse_html_page on that URL.

**Enough evidence:**
- The submitted figure must be read from the text of a primary document that you opened with parse_html_page and queried with retrieve_information. Search-result snippets and aggregator sites are leads, not confirmation.
- Confirm the metric name, the region or segment, the period, and the units or definition. Examples are "excluding experiences", or full year versus quarter.
- If the primary document truly cannot be opened after two different attempts, submit the best-supported figure and say plainly which source it came from. Do this before the budget runs low.

**Re-check before submitting:** Re-read the exact line the figure came from. Make sure it is the requested year and not the prior-year column, and the requested region and not the total.

**Task fact (unverified lead, from one earlier run):** For Airbnb FY2024 "Average Nights per Booking" by region, search excerpts of Airbnb's Q4 2024 financial document (https://s26.q4cdn.com/656283129/files/doc_financials/2024/q4/2395a7f3-5507-497a-971b-f3e4b606c6c7.pdf) suggested Asia Pacific = 3.3. The company-wide figure was 3.8 for 2024 against 3.9 for 2023. The document was never opened, so confirm this in the document text, or in the 10-K, before relying on it.
</file>

<notes>
Base run 1: edgar_search hit a 403 and the agent gave up on primary sources. It then submitted from a search snippet, admitting it never opened the document (3.3 for APAC). The edits address that earlier divergence:
- one bounded fallback for the edgar_search failure, plus a rule to avoid web_search with an empty query (it was called with query=null);
- an explicit "enough evidence" definition requiring the primary document to be opened and the figure re-checked before submission;
- the unverified task lead (the Q4 2024 PDF URL and the 3.3 figure), labelled as unverified so the next run can confirm it quickly.
No skill was added, because the issue is ordinary sequencing and tool failure, not a multi-step workflow.
</notes>