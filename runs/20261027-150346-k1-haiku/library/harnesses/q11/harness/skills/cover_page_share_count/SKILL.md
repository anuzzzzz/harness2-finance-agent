---
name: cover_page_share_count
description: Report shares of common stock outstanding by class for a company, from the latest 10-K/10-Q cover page, in the exact format the question requests.
---
ANALYTIC MOVE: look up (no arithmetic). Required result: the outstanding share count for each class of common stock, with its as-of date and source.

1. Controlling source: the cover page of the most recent periodic filing (10-K or 10-Q) filed on or before the question date. The cover states counts as of a recent date, usually a few weeks after period end. The balance sheet and equity note give counts as of the period end, and these usually differ. Use the cover-page counts unless the question names a balance-sheet date. Say which date you used.
2. Check that no newer 10-Q has been filed before the question date. Use edgar_search with form_types and a start_date filter.
3. List every class the cover shows. Include each class with a non-zero count, and name any class shown as zero ("no shares of Class C outstanding") only in a short note. If a class is described differently from the others (for example held by a subsidiary), say so in one line and do not silently drop it.
4. Retrieve the exact cover sentence with retrieve_information and read the numbers from that text, not from memory or search snippets. Keep full digits, with no rounding and no change of units. Cover counts are in shares, not thousands.
5. Format: if the question gives a template (for example "Class X: X shares" with line breaks), put the answer lines in exactly that template, one class per line, before any explanation. Keep the lines in class order. Put the as-of date, the filing and the sources after the lines.
6. Cite only the filing you opened and retrieved from.

Task fact (verified in two runs, re-confirm in the text): the Airbnb FY2024 10-K (filed 2025-02-13, https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm) cover page, as of January 31, 2025, shows Class A 432,876,657; Class B 188,462,942; Class C none; Class H 9,200,000.
