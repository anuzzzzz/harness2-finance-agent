# Library

Each entry is an earlier task whose harness was chosen, stored with its full component tree and why it was picked.

## `harnesses/q04/`
- harness: 1 skill; 3,206 always-on chars
- cue: A multi-period question that supplies its own output template with a stated precision (for example "[X.X]%"), while the base system prompt carries a blanket "at least two decimal places" rule.

## `harnesses/q05/`
- harness: 0 skills; 1,525 always-on chars
- cue: A "who was nominated / appointed / elected in year Y" question where the later-year proxy describes a year-Y search but the formal seating or vote falls in year Y+1. The agent can reach company IR-site filings, while sec.gov search returns 403 and null-query searches return nothing.

## `harnesses/q09/`
- harness: 1 skill; 2,848 always-on chars
- cue: A "how much did the company beat or miss its own guidance" question where the guidance is a midpoint ± range, the filing reports the actual both as a rounded percent and as dollar amounts, and sec.gov fetches return 403.

## `harnesses/q14/`
- harness: 1 skill; 2,992 always-on chars
- cue: A multi-year ratio question (FCF margin, payout, margin trend) where the earliest year is distorted by a discontinued operation or wind-down, where sec.gov fetches return 403, and where some inputs are reachable only through search excerpts or aggregator pages.

## `harnesses/q19/`
- harness: 1 skill; 2,954 always-on chars
- cue: Primary-source fetch tools (EDGAR search or page parsing) fail with HTTP 403 in this environment, and the agent can only reach filing text through web_search excerpts.

## `harnesses/q30/`
- harness: 1 skill; 3,059 always-on chars
- cue: A "total shares / maximum dilution from instruments outstanding at a date" question where the 10-K aggregate line is reachable only through search excerpts, and per-series terms (principal, conversion rate) are spread over several filings.

## `harnesses/q42/`
- harness: 1 skill; 3,032 always-on chars
- cue: A question asks to rank one company's ratio (payout, margin, yield) against competitors for a fiscal year, where peers differ in whether they pay or report the metric and where GAAP earnings carry one-offs that can reorder the ranking.

## `harnesses/q45/`
- harness: 1 skill; 3,132 always-on chars
- cue: A "what was the adjustment/add-back for X in year Y" question on a non-GAAP reconciliation, where sec.gov fetches return 403, PDFs cannot be parsed, and the figure is reachable only through web_search excerpts.

