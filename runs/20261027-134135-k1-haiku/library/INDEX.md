# Library

Each entry is an earlier task whose harness was chosen, stored with its full component tree and why it was picked.

## `harnesses/q04/`
- harness: 0 skills; 4,160 always-on chars
- cue: A question needs figures from several dated filings, for example guidance stated in each prior-quarter release. The base run answers from search snippets, and the figures are easy to find in the search results.

## `harnesses/q05/`
- harness: 0 skills; 3,979 always-on chars
- cue: A question asks who was nominated, appointed or elected to a board or office "in <year>". The base run finds the in-year proxy in its search results but never opens it, and answers with a person from a later-dated press release or proxy while admitting the mismatch.

## `harnesses/q09/`
- harness: 0 skills; 4,224 always-on chars
- cue: A question asks whether a company beat or missed its own guidance and by how much (basis points, dollars or percent), and the base run answers from search snippets with no filing opened.

## `harnesses/q14/`
- harness: 0 skills; 3,905 always-on chars
- cue: A multi-year ratio or trend question (for example FCF margin, payout, margin by year) where the latest 10-K carries comparative columns. An unguided run may answer from aggregator snippets or open only the newest filings, and one year may be distorted by discontinued operations.

## `harnesses/q30/`
- harness: 0 skills; 4,155 always-on chars
- cue: A question uses a defined-sounding term ("maximum", "if-converted", "aggregate") for a figure that the filing may report under a different label, and the base run mixes bases from several sources (for example one series' make-whole maximum from an 8-K combined with other series' base rates) or cites documents dated after the as-of date.

## `harnesses/q42/`
- harness: 0 skills; 4,625 always-on chars
- cue: A multi-company comparison or ranking on one ratio (payout, margin, leverage), where the base run answers from search snippets and mixes data bases across companies (aggregate dollars for one, per-share for others, or reconstructed figures).

## `harnesses/q44/`
- harness: 0 skills; 3,731 always-on chars
- cue: A harness edit adds a rule that evidence must come from an opened primary document, but a later run's trajectory shows a submission with no document opened. Alternatively, the edit offers a pointer to a likely source for the metric.

## `harnesses/q45/`
- harness: 0 skills; 3,248 always-on chars
- cue: A full-fiscal-year non-GAAP or reconciliation figure is asked for, and the earnings-release exhibit (shareholder letter) shows only quarterly columns, so a base run rebuilds the year by summing quarters.

