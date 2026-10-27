# q01

- adopted: `agg1`
- components: 1 skill; 3,065 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, edgar_search with CIK and date filters, cite only opened documents, plain text with no citation markup, as-of date cutoff, no null queries)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. Snippets are leads only. Open primary documents with parse_html_page and confirm with retrieve_information. Cite only opened documents. Do not use documents dated after April 7, 2025. Write plain text with no `<cite>` tags. Never run a null-query search. inv1 and agg1 also said to read company-authored documents (8-K exhibits, DEFA14A) for "how addressed" questions. inv1 embedded task facts in the file. dom1's version was shorter.
observed: base1 parsed only the 10-K, then listed the Q1 2025 10-Q (dated after the cutoff), the CORRESP letter and the Jan 3 8-K as sources without opening them, and leaked `<cite index>` markup. It also asserted an April 6 memo and a May 21 deadline from snippets. All three edited runs wrote plain text and cited only documents they had opened. inv1 and agg1 opened the Jan 3/6 8-Ks, and inv1 also opened the Jan 27 DEFA14A, so they covered the lawsuits and public messaging that base1 and dom1 (10-K only) did not. The clean sourcing in dom1 and agg1 came with the skill, and inv1 had no skill, which points to the guidance. Each candidate is one rollout, and the 10-K facts were the same across runs.
verdict: confounded

component: skills/pending_merger_disclosure/SKILL.md and the trigger line in systemprompt.md
candidates: dom1, agg1
change: Added an on-demand skill for explaining how a company handled a pending deal. It sets a date cutoff, names the 10-K sections and company-authored 8-K and DEFA14A documents as controlling sources, and gives an answer contract: timeline, company actions, covenants, stakeholder effects, continuing operations, and what the filings do not say. agg1's version added a company-actions section and a step to open company-authored exhibits. Both skills carried task-fact leads and cutoff warnings.
observed: Both runs loaded the skill in turn 1. Both parsed the 10-K and gave a structured five-part answer ending with an omissions list. dom1 used the 10-K only, and its answer states the filing is silent on a termination fee or outside date while leaving out the lawsuit press release and any company messaging. agg1 additionally opened the Jan 6 exhibit, the March 14 8-K and the March 20 guidance release, and its answer includes the DOJ briefing extension and the Q1 guidance. That extra coverage matches the skill step on company-authored documents, but inv1 reached similar breadth without a skill. No skill-free run shares the guidance, so the skill's own effect is not isolated.
verdict: confounded

component: systemprompt.md
candidates: dom1, agg1
change: Added one line telling the agent to call load_skill with `pending_merger_disclosure` when asked how a company addressed a pending deal.
observed: Both runs called load_skill first. No skill-equipped run lacks the trigger, so the line's separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

component: task-fact leads (merger dates, URLs, "do not use the Q1 2025 10-Q") placed in inv1's tool_guidance and in the dom1 and agg1 skills
candidates: inv1, dom1, agg1
change: Gave verified 10-K facts and company-document URLs, and warned that the Q1 2025 10-Q post-dates the cutoff.
observed: All three runs parsed the 10-K in the first or second turn, and none listed the 10-Q. inv1 and agg1 used the supplied exhibit URLs directly. base1's snippet-based errors did not recur. Rules and leads were bundled in each edited run, so the leads' own effect is not separated.
verdict: confounded

## Transferable lesson
- **cue**: An open-ended "how has the company addressed X (a pending deal, a legal block, a regulatory event) and what is the effect on operations" question, with a fixed as-of date. Primary filings exist both before and after that date. The base run reads only the annual report, takes later events from search snippets, and lists unopened documents (including post-date filings) as sources.
- **lesson**: In tool_guidance.md, add three rules. (1) Respect the as-of date: do not use or list any filing dated after it, and check each source's filing date. (2) For "how has the company addressed" questions, open at least one company-authored document in addition to the 10-K risk factors (the 8-K exhibits and proxy-soliciting material found with edgar_search by CIK and date range), and report company actions separately from risks it warns about. (3) List as sources only documents that were opened and retrieved from. Keep these in always-on tool_guidance, and keep the answer layout (timeline, actions, covenants, stakeholder effects, omissions) in an on-demand skill.
- **evidence**: tool_guidance.md row and skill row. base1 listed an unopened post-date 10-Q, a CORRESP letter and an 8-K, and leaked `<cite>` markup. inv1 (guidance only, no skill), dom1 and agg1 all cited only opened documents. Only inv1 and agg1, whose guidance said to read company-authored documents, opened the Jan 3/6 8-Ks and, for inv1, the DEFA14A. dom1 had no such rule and stayed with the 10-K alone.
- **confidence**: low. One rollout per candidate, and the guidance, skill and task-fact leads were bundled in every edited run. The record shows a difference in sourcing hygiene and coverage, and gives no evidence about accuracy.
