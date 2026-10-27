# Library

Each entry is an earlier task whose harness was chosen, stored with its full component tree and why it was picked.

## `harnesses/q01/`
- harness: 1 skill; 3,065 always-on chars
- cue: An open-ended "how has the company addressed X (a pending deal, a legal block, a regulatory event) and what is the effect on operations" question, with a fixed as-of date. Primary filings exist both before and after that date. The base run reads only the annual report, takes later events from search snippets, and lists unopened documents (including post-date filings) as sources.

## `harnesses/q02/`
- harness: 1 skill; 2,998 always-on chars
- cue: A multi-year trend question about a company-reported KPI (ARPU/ARM, subscribers, margin). Each 10-K shows only about three years of the metric. The base run answers from snippets, opens no filing, leaks citation markup, and lists unopened filings and PDFs as sources.

## `harnesses/q03/`
- harness: 0 skills; 4,161 always-on chars
- cue: A "beat or miss versus the prior quarter's guidance range, in bps" question. The guidance sits in the previous quarter's earnings release and the actual in the target quarter's release. The base run answers from snippets, opens neither, lists unopened pages as sources, leaks citation markup, and gives two competing headline numbers (against the high end and against the midpoint).

## `harnesses/q04/`
- harness: 1 skill; 3,072 always-on chars
- cue: A multi-period question asks about guidance (a range or a comparison) with an exact answer format. Each period's guide is printed in the prior period's earnings release. The base agent answers from search snippets, opens no filing, and defaults to two decimals.

## `harnesses/q05/`
- harness: 1 skill; 3,030 always-on chars
- cue: A question asks who was nominated, appointed or elected to a board (or similar governance event) in a named year. The base run finds that year's proxy and 8-K in search results but never opens them. It answers from a later year's snippets, a press release or a following-year proxy narrative, and lists unopened sources.

## `harnesses/q06/`
- harness: 0 skills; 5,000 always-on chars
- cue: A question asks which of several companies plans to spend the most (capex, buybacks) for a future year. One company's figure is commonly reported by the press as a round number, but it may come from call commentary or an analyst's question rather than a release. Base search snippets and news pages make the figure look like formal guidance.

## `harnesses/q08/`
- harness: 0 skills; 4,792 always-on chars
- cue: A question that carries a measurement qualifier ("at close", "as of the closing date", "fair value") on a figure, where the first filing's retrieval returns only the headline or announced amount and says it does not break the figure down.

## `harnesses/q09/`
- harness: 1 skill; 3,094 always-on chars
- cue: A question asks how a company's result compared with its own prior guidance, in bps, % or $. The base agent answers from web-search snippets and never opens the two earnings releases. The guidance sits in the prior quarter's release, and GAAP and non-GAAP figures sit side by side.

## `harnesses/q10/`
- harness: 0 skills; 3,435 always-on chars
- cue: A simple multi-year growth or ratio question (CAGR, YoY) where the latest 10-K's three-year comparative table covers both endpoints. The base run opens only an older filing, takes the newer endpoint from a search snippet, and then cites the unopened latest filing as the source of that figure.

## `harnesses/q11/`
- harness: 1 skill; 2,493 always-on chars
- cue: A question asks for a simple filing-disclosed count (shares outstanding by class, a cover-page figure) with a prescribed answer template. The base harness is bare, and one run answers from search-result titles without opening any filing.

## `harnesses/q12/`
- harness: 1 skill; 3,309 always-on chars
- cue: A question asks to project a period from several monthly or earlier-period reports (a historical average growth rate applied to a base) and compare the result with guidance stated in a different currency, and the base run works from search snippets.

## `harnesses/q14/`
- harness: 1 skill; 3,345 always-on chars
- cue: A multi-year ratio or trend question (for example FCF margin) is answerable from one filing's three-year comparative columns. The base run opened the latest two or three 10-Ks and listed a filing it never opened as a source. It also picked one ambiguous input definition (capex) without a labelled alternate, and left a distorted year unquantified.

## `harnesses/q15/`
- harness: 0 skills; 3,996 always-on chars
- cue: A simple ratio question (turnover, margin) answerable from one 10-K's income statement and two balance-sheet columns. The base run answers from earnings-release snippets without opening any filing, lists unopened release pages as sources, leaks citation markup, and shows two unranked ratio variants.

## `harnesses/q16/`
- harness: 1 skill; 3,136 always-on chars
- cue: A question asks for the key terms of a registered securities offering (preferred, convertible, notes). The final prospectus supplement holds most terms, but the upsize from the launch size and the exercise of the over-allotment option appear only in the FWP, press release or closing 8-K. Search snippets mention those facts, and the base run repeats them unopened and leaks citation markup.

## `harnesses/q17/`
- harness: 0 skills; 3,350 always-on chars
- cue: A multi-year ratio or trend question where the latest 10-K carries three years of the numerator but only two years of the denominator metric. The base run is numerically right but its final answer lists an earlier-year filing it never opened and leaks citation markup.

## `harnesses/q18/`
- harness: 0 skills; 4,552 always-on chars
- cue: A "does the company report metric X, and how is it defined" question where the metric's disclosure changed after SEC staff comments. The CORRESP/UPLOAD letters form a series, and the first letter states a commitment that a later letter revises. The base run answers from snippets and opens nothing.

## `harnesses/q20/`
- harness: 1 skill; 1,689 always-on chars
- cue: A question asks for the change in a company-published ratio or rate (effective tax rate, margin, growth %) in bps or points. The filing states the rates rounded to one decimal, and recomputing from dollar amounts gives a slightly different delta.

## `harnesses/q21/`
- harness: 0 skills; 3,589 always-on chars
- cue: A question asks about a company's dependency or concentration risk (vendor, processor, sponsor bank, supplier) as of a fiscal year-end. The base run finds the 10-K note but then adds a counterparty name it inferred and cites an older prospectus it never opened.

## `harnesses/q22/`
- harness: 0 skills; 4,501 always-on chars
- cue: A multi-year per-unit ratio question (such as GBV per night) built from a company KPI table that is printed rounded to whole millions. The same 10-K narrative gives one-decimal counts for some years but not for the latest year. The base run mixes the narrative counts with a count it derives by adding a reported change.

## `harnesses/q23/`
- harness: 0 skills; 3,557 always-on chars
- cue: A "when is X expected to start or open" question with an as-of date, where later filings before that date report that the event has already happened. The company uses a fiscal year that differs from the calendar year, and the later filing says "second quarter of 2025". The base run answers from snippets and a news item that gives a calendar date.

## `harnesses/q24/`
- harness: 0 skills; 2,344 always-on chars
- cue: A simple lookup of one table figure in a single filing (for example a debt principal total or a subtotal after excluding one line). Unedited runs usually open the filing, but one run answered from search-result titles or snippets and listed a spreadsheet it never opened.

## `harnesses/q25/`
- harness: 1 skill; 2,867 always-on chars
- cue: A question asks to summarize or list a category of risk factors (regulatory, cybersecurity, competitive) from a long 10-K, and the only extraction tool is an LLM retrieval over one huge parsed document. Outputs are truncated, and the agent tends to turn one broad retrieval into a flat "the filing does not mention X" statement.

## `harnesses/q26/`
- harness: 0 skills; 3,822 always-on chars
- cue: A simple lookup-and-ratio question whose inputs sit in one sentence of a single 10-K (for example a headcount split in Human Capital). The base run answers from a snippet of a third-party reproduction of the filing. It lists the unopened SEC filing as a source and leaks citation markup.

## `harnesses/q27/`
- harness: 0 skills; 3,770 always-on chars
- cue: A "what are the terms of instrument X (debt, hybrid, preferred) as of FY Y" question where one 10-K debt note holds the terms. The base run finds the 10-K URL but answers from snippets, never opens the filing, lists unopened spreadsheets and press releases as sources, and leaks citation markup.

## `harnesses/q28/`
- harness: 0 skills; 4,003 always-on chars
- cue: A "what are the company's material cash requirements / contractual obligations for next year" lookup answerable from one table in the latest 10-K's MD&A. The base run answers from snippets, leaks citation markup, and lists an unopened spreadsheet and PDF as sources. The filing's table footnotes name obligations excluded from the table.

## `harnesses/q29/`
- harness: 0 skills; 3,997 always-on chars
- cue: A "list the company's KPIs/operating statistics for fiscal year X" question answerable from one table in the latest 10-K's MD&A. The base run already finds the right table, but it uses a ticker where a CIK is required, issues a null-query search, lists an unopened secondary article as a "cross-check", and claims it confirmed rows after a truncated retrieval.

## `harnesses/q30/`
- harness: 1 skill; 3,039 always-on chars
- cue: A question asks for a total that a filing discloses in one table line (for example an if-converted share count) and that can also be rebuilt from per-instrument inputs in a debt note. The base run reports the disclosed total plus a derived split. It flags one input as unconfirmed, and it lists a filing it never opened as a source.

## `harnesses/q31/`
- harness: 0 skills; 3,627 always-on chars
- cue: A what-if or projection question (growth rate plus margin change) where the base-year metric is not a printed line, so the agent must derive it from revenue and cost of sales. A similarly named segment margin also exists. The base run does the arithmetic correctly but cites a page that returned HTTP 403 and issues a null-query search.

## `harnesses/q32/`
- harness: 0 skills; 3,260 always-on chars
- cue: A simple lookup or mix-percentage question whose answer sits in one table of the latest periodic filing. The base run finds and opens that filing correctly, but it also quotes a press-release sentence from a search snippet, lists the unopened release as a source, and issues a null-query search.

## `harnesses/q33/`
- harness: 1 skill; 3,694 always-on chars
- cue: A what-if question whose arithmetic is a delta times a balance (a rate shift on debt, a price change on volume), where the base run fetches a third-party "current rate" or tax rate from search snippets that the calculation does not need. The base run also lists unopened pages as sources, and the base net income is a loss.

## `harnesses/q34/`
- harness: 0 skills; 3,285 always-on chars
- cue: A question asks for a share or mix percentage (channel partners, a customer type, a segment or region) that the 10-K prints in a revenue note, and the base run answers from search snippets or XBRL spreadsheet results. It cites the 10-K and a Financial_Report.xlsx it never opened, and it issues a null-query search.

## `harnesses/q35/`
- harness: 0 skills; 3,898 always-on chars
- cue: A question asks for the largest or smallest line in a non-GAAP reconciliation (adjustment, add-back). The full-year table is in one earnings-release exhibit. The base run gets the right figure but leaks `<cite>` markup, lists an unopened mirror or secondary page as a source, and wastes turns on empty-query searches.

## `harnesses/q36/`
- harness: 0 skills; 4,715 always-on chars
- cue: A deal-terms question ("what price was X acquired at", with equity value and enterprise value) where the target's and acquirer's filings print different figures for the same measure. One figure appears only in an investor-presentation PDF that parse_html_page cannot read. The base run answers from snippets and lists unopened sources.

## `harnesses/q37/`
- harness: 0 skills; 4,273 always-on chars
- cue: A question asks for a program-to-date total "incurred as of" a date (merger restructuring, integration or synergy costs). The annual income-statement lines sum to a number that differs from the company's own stated cumulative figure. The base run finds both only after extra retrievals and lists unopened filings or spreadsheets as sources.

## `harnesses/q38/`
- harness: 0 skills; 4,751 always-on chars
- cue: A "beat or miss versus the prior quarter's guidance, in bps or %" question where the actual period's earnings release exists on EDGAR but web_search returns it poorly or not at all. The base run answers from snippets, a transcript and a 10-K subtraction.

## `harnesses/q39/`
- harness: 1 skill; 3,344 always-on chars
- cue: An open-ended "what metrics does company X guide on / provide outlook for" question with an as-of date. The base run answers from search snippets and an older year's supplemental deck, and mixes guidance items across years.

## `harnesses/q40/`
- harness: 0 skills; 4,387 always-on chars
- cue: A question asks for the line items of a company's non-GAAP reconciliation (for example, the adjustments from net income to Adjusted EBITDA). The full-year table sits in the 10-K MD&A, and the base run reaches it but pads its answer with unopened filings.

## `harnesses/q41/`
- harness: 0 skills; 3,768 always-on chars
- cue: A simple single-figure lookup (a quarterly KPI such as comparable store sales) where the question's wording differs from the company's metric name and the sign may be negative. The base run answers from search snippets, passes a ticker to a CIK-only search field, and lists unopened pages as sources.

## `harnesses/q42/`
- harness: 1 skill; 3,259 always-on chars
- cue: A question asks to compare or rank a company's ratio (payout, margin, leverage) against its competitors. The base agent works from search snippets, mixes GAAP and adjusted bases, gives two competing rankings, and never opens one peer's filing.

## `harnesses/q43/`
- harness: 1 skill; 3,174 always-on chars
- cue: A question asks how much of a revenue change came from a rate (take rate, price, margin) versus volume. The filing gives both years of the volume metric and of revenue, and also discloses a reclassification or business-model change that moves the reported rate without moving volume. The base run improvises the split and mixes reported and adjusted figures.

## `harnesses/q44/`
- harness: 1 skill; 3,179 always-on chars
- cue: A question asks for a single reported KPI that web search returns as a snippet, often from a PDF letter, while the filing's HTML is parseable. The base harness has no rule that a snippet must be confirmed in the primary text.

## `harnesses/q45/`
- harness: 0 skills; 3,538 always-on chars
- cue: A question asks for one full-year line from a non-GAAP reconciliation or footnote. The earnings-release exhibit gives only quarterly columns, so the agent sums quarters from the 8-K. The base run then lists other filings (10-Qs, the 10-K) as sources that it never opened.

## `harnesses/q46/`
- harness: 1 skill; 3,415 always-on chars
- cue: An open-ended "what has the company's strategy been, and how does it align with X" question with a stated time window and as-of date. The agent needs the deal or event list, the spend, and the X breakdown. The base run opens only the latest annual report. It fills the rest from search snippets and lists the unopened documents as sources.

## `harnesses/q47/`
- harness: 1 skill; 2,591 always-on chars
- cue: A "beat or miss versus guidance" question that needs two documents, the release that issued the guidance and the release that reports the actual. The base run opens the guidance document but takes the actual from a search snippet, lists the unopened actual-period document as a source, and leaks citation markup.

## `harnesses/q48/`
- harness: 0 skills; 4,741 always-on chars
- cue: A "how did the actual results compare with the company's prior-quarter full-year guidance" question that needs two documents, the earlier release that issued the guidance and the release that reports the full-year actual. Search snippets carry both sets of figures, and the base run answers from snippets without opening either document.

## `harnesses/q49/`
- harness: 0 skills; 5,467 always-on chars
- cue: A "how many times did the company beat its own guidance over the last N years, and what is the current guidance" question. The base run answers from search snippets. The guidance is revised during each year, and the Q4 release of one year holds both that year's actual and the next year's initial outlook.

## `harnesses/q50/`
- harness: 0 skills; 4,495 always-on chars
- cue: A multi-quarter "beat or miss versus the prior quarter's guidance (revenue midpoint x margin guide)" question with a prescribed output format, such as "QX - $XXX million (X.X %)". The base run answers from search snippets, opens no earnings release, and lists unopened sources.

