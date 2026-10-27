<file path="tool_guidance.md">
# Tool guidance

- Decide the company, form type (10-K, 10-Q, 8-K Ex. 99.1, shareholder letter) and fiscal period before searching. Use those in the query, not the question's wording.
- Chain: find the primary document URL (edgar_search or web_search), then parse_html_page with a clear key, then retrieve_information with one targeted question and the same key. Ask for the exact sentence or table row, including the column header and the period.
- If edgar_search fails (for example a 403 on the ticker lookup), don't repeat the identical call. Switch to web_search with a company, form and year query to find the document URL.
- If parse_html_page returns 403 for a sec.gov URL, try another HTML copy of the same disclosure, such as an 8-K Ex. 99.1 or an IR-site page. parse_html_page cannot read PDFs, so look for an HTML version.
- Before submitting, check that the figure matches the requested metric label, region or segment, fiscal year (not the prior-year column) and units. If the figure rests only on a search excerpt because the primary document could not be opened, say so in the answer. Submit before the budget runs low.
</file>

<notes>
kept -> inv1 (edgar_search fallback, enough-evidence and re-check rules, trimmed) -> edgar_search 403 in 2/2 rollouts that used it (base1, inv1, dom1 all hit it), sec.gov parse 403 and PDF-not-parseable in 2/2 rollouts that tried those; a short generic fallback line addresses the repeated dead ends.
dropped -> inv1 "avoid empty web_search query" rule -> in every rollout the query=null call was the one that returned results, probably a trace artifact; a rule against it could break the working path.
dropped -> inv1 and dom1 embedded Airbnb "3.3" task fact -> a task-specific answer in always-on or skill text is unverified (never opened in any rollout) and does not generalize to later tasks in the library.
dropped -> dom1 skill operating_kpi_lookup and its systemprompt trigger line -> dom1 took 6 turns versus 4 for inv1 and reached the same answer with the same excerpt-only verification; no specific moment shows the skill changed the outcome, so it adds always-on cost for no demonstrated gain.
all three rollouts submitted; none produced nothing, so there is no unsafe-edit flag. The change is a small always-on tool_guidance file.
</notes>