# q11

- adopted: `agg1`
- components: 1 skill; 2,493 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: skills/cover_page_share_count/SKILL.md
candidates: dom1, agg1
change: Added an on-demand skill for share-count-by-class questions. It names the latest 10-K/10-Q cover page as the controlling source, requires a check for a newer 10-Q, and says to list every non-zero class and name zero classes in a short note. It also says to retrieve the exact cover sentence, to put answer lines in the question's template before any prose, and to cite only opened filings. It carries the verified Airbnb cover counts as a task fact. agg1 added "not from memory or search snippets" and "retrieved from", and marked the fact verified in two runs.
observed: Both runs loaded the skill first, ran one date-filtered edgar_search, parsed the 10-K, retrieved the cover sentence and submitted in 4 turns, with only the 10-K cited. Both gave the Class A/B/H lines first, with Class C noted as zero. base1 (no skill) reached the same figures in 4 turns, but it wrapped them in prose, added a Class A/B-only aside and did not state the cover-date versus balance-sheet distinction. The figures were the same in base1, dom1 and agg1. inv1 (base harness, no skill) skipped the filing and submitted different figures from an unopened proxy (see the guidance row). The skill carried the 10-K URL and the counts, so the direct route may come from the task fact rather than from the procedure. The skill's effect on the figures is not isolated.
verdict: confounded

component: systemprompt.md
candidates: dom1, agg1
change: Added one trigger line telling the agent to call load_skill with `cover_page_share_count` when asked for shares outstanding by class.
observed: Both candidates called load_skill as their first action. No skill-equipped run lacks the trigger, so the trigger's separate effect is not shown.
verdict: no observed effect

component: tool_guidance.md
candidates: agg1
change: Went from empty to four bullets. Decide the document and period first, with edgar_search filters. Never use a null query in web_search. A snippet or result title is a lead, so confirm the figure, date and unit in retrieved text from the opened document. Cite only documents opened and retrieved from. Submit once verified.
observed: The only evidence for the failure it targets is inv1, which ran on the base harness. inv1 made a null-query web_search, saw search-result titles only, never parsed a filing, and submitted Class A 433,034,896 / Class B 185,611,689. It attributed these to a 2025 proxy "as of April 7, 2025" that it never opened, and it contradicted the 10-K cover retrieved in the other runs. agg1 carried this guidance and also the skill, and it verified in the 10-K. dom1 had the skill but no guidance, and it also verified. The skill alone therefore prevented the failure in dom1. The guidance's own effect cannot be separated from the skill's. inv1 is a single rollout. Its figures are unverified and may be wrong, or may be a real later proxy count.
verdict: confounded

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks for a simple filing-disclosed count (shares outstanding by class, a cover-page figure) with a prescribed answer template. The base harness is bare, and one run answers from search-result titles without opening any filing.
- **lesson**: In tool_guidance.md, state that a count is never submitted unless read from retrieved text of an opened filing, forbid null-query web_search, and forbid citing a filing seen only in search results. Put the template-first formatting rule and the latest-cover-page-before-the-question-date rule in an on-demand skill triggered from systemprompt.md. Keep always-on text to the verification rules.
- **evidence**: The tool_guidance and skill rows. inv1 (base harness) made a null-query search, never parsed a filing and submitted unverified counts from an unopened proxy. base1, dom1 and agg1 each opened the 10-K and retrieved the cover sentence, and gave identical counts. Which edit prevented the failure is not isolated, because dom1 verified with the skill alone and agg1 had both.
- **confidence**: low. Behavior diverged in only one rollout (inv1). That run's figures were not checked against its cited source, and the skill and guidance were never varied independently.
