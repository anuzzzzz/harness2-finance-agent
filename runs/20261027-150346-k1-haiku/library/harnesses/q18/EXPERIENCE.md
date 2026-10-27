# q18

- adopted: `agg1`
- components: 0 skills; 4,552 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, parse_html_page then retrieve_information the definition verbatim, cite only opened documents with exact URLs, plain text without citation markup, no empty-query searches, respect as-of date)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. The base run had no rules. The edited versions require the 10-K definition to be retrieved verbatim from opened text. They allow only opened documents as sources and tell the agent to label post-as-of filings as later developments. agg1 and dom1 added "check gross and net separately; say 'not reported' only after searching with several wordings". agg1 added "look for later letters in a comment-letter series before stating the final position".
observed: base1 ran one edgar_search and one web_search and opened nothing. It listed five unopened sources, one with a malformed URL (".../000010149/filename1.pdf"), and its definition came from snippets. inv1, dom1 and agg1 all parsed the FY2025 10-K and the Q3 10-Q (turn 1 or 2) and retrieved the definition and the ~98% figure from the text. All listed only opened documents with exact URLs, and none leaked markup. The core answer was the same in every run: gross revenue retention is reported at about 98%, with the same definition and ARR exclusions. The difference is in verification and sourcing. Rules and the URL leads were bundled in each edited run, so the rules' effect cannot be separated from the leads.
verdict: confounded

component: tool_guidance.md (correspondence rule plus a lead to the second SEC letter, accession ...24-000192)
candidates: agg1 (inv1 and dom1 had the first letter only)
change: agg1 told the agent to look for a later letter in the same comment-letter series and gave the URL of the 9/19/2024 letter, labelled unverified.
observed: agg1 parsed both letters in turn 1. The second letter states that Workday "no longer intend[s] to include disclosure related to net revenue retention rates". This gives a coherent account that matches the filings. inv1 and dom1 opened only the 9/4 letter, which promises net retention disclosure. Both ended with an unresolved "discrepancy" paragraph (inv1 said "I could not determine why the net rate was omitted"; dom1 said it did not find a later explanation). The lead and the rule were bundled, and each run is one rollout. The contrast is clear, though, and the follow-up letter was reached only in agg1, which had the lead.
verdict: helped

component: skills/company_kpi_definition_lookup/SKILL.md plus the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill for "does the company report metric X and how is it defined". It covers the gross and net variants, the definition contract, the disclosure history through the CORRESP letters, and the Workday leads. systemprompt.md gained a line telling the agent to load it.
observed: dom1 loaded the skill first and then took 7 turns, against 3 for inv1 and 5 for agg1. The factual content matched inv1 and agg1, and dom1 was the least resolved on the net-retention history. It did run an extra retrieval on the 10-Q, which confirmed that net retention was absent. A rule to say "not reported" only after multiple wordings was also in agg1's always-on text. The skill added turns and cost ($0.184 against $0.096 and $0.098) with no visible gain. The task leads in the skill were the same as those in the other candidates' tool_guidance.
verdict: no observed effect

component: systemprompt.md (trigger line only)
candidates: dom1
change: Added one sentence directing the agent to load company_kpi_definition_lookup.
observed: dom1 called load_skill as its first action. No run isolates the trigger from the skill.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A "does the company report metric X, and how is it defined" question where the metric's disclosure changed after SEC staff comments. The CORRESP/UPLOAD letters form a series, and the first letter states a commitment that a later letter revises. The base run answers from snippets and opens nothing.
- **lesson**: In tool_guidance.md, add a rule that when a metric was added, changed or dropped, the agent must open every letter in the comment-letter series, including follow-ups, before stating the company's final position. If the filings contradict a stated commitment, it should say so. Give the follow-up letter URLs from edgar_search as labelled leads. Keep the verbatim-definition and cite-only-opened-documents rules in the same file. Do not add a skill for a single lookup.
- **evidence**: The "correspondence rule plus second-letter lead" row. agg1 opened both letters and reported the reversal ("no longer intend to include net revenue retention"). inv1 and dom1 opened only the first letter and ended with an unexplained discrepancy. The skill row shows that the skill run cost more turns than the always-on runs for the same facts. The general tool_guidance row is confounded and supports only the sourcing hygiene.
- **confidence**: low. One rollout per candidate, and the follow-up lead was bundled with other edits in agg1. The contrast on the second letter is direct, but it is a single instance.
