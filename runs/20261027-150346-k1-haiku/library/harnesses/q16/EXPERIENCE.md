# q16

- adopted: `agg1`
- components: 1 skill; 3,136 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (cite-only-opened, plain-text output, no empty-query search, no PDFs)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. A snippet is a lead, not evidence. Open the primary filing with parse_html_page and confirm with retrieve_information. Cite only documents opened and retrieved from. Write plain text with no <cite> markup. Never issue an empty-query search (inv1 and agg1 carried the explicit clause).
observed: base1 leaked raw <cite index> markup and listed three unopened sources (Nasdaq, Investing.com, Simpson Thacher). It also made a null-query web_search in turn 2. inv1 and dom1 produced clean plain text and listed only the opened 424B5, 8-K exhibit and certificate of designations. agg1 also produced clean text and listed only the opened 424B5, FWP and 8-K. agg1 still made one null-query web_search in turn 5 despite the rule, and tried to open an unopened Nasdaq press release, which timed out. This is one rollout per candidate, and the task-fact leads and the skill were bundled in the same edited runs.
verdict: confounded

component: tool_guidance.md ("unconfirmed option/upsize" rule in inv1 and dom1 versus "open the press release or FWP to confirm" rule in agg1)
candidates: inv1, dom1, agg1
change: inv1 and dom1 told the agent to call a fact unconfirmed if only a snippet showed it (option exercise, upsize). agg1 instead told the agent to open the relevant page to confirm a snippet-suggested material fact, and not to drop it or assert it unopened.
observed: inv1 opened the underwriting agreement (8-K EX-1.1), found no statement of exercise, and submitted with exercise "unconfirmed". It reported 45M shares plus a 6.75M option, and omitted the upsize. dom1 opened the 424B5 and the certificate of designations but not the 8-K body or an FWP. It said both the upsize and the exercise were unconfirmed, even though its certificate of designations retrieval showed 51,750,000 authorized shares. agg1 opened the FWP (retrieved: increased from 30,000,000 to 45,000,000 shares) and the 8-K body (retrieved: 51,750,000 shares issued, option exercised in full). It gave the full launch, priced and final sizes, each tied to an opened document. The behavioral divergence is at agg1 turns 4-7, where it opened the FWP and 8-K. This follows the instruction, though the retrievable facts also differed by candidate, and the single rollouts cannot rule out luck.
verdict: helped

component: skills/security_offering_terms/SKILL.md (plus the trigger line in systemprompt.md)
candidates: dom1, agg1
change: Added an on-demand skill for offering-terms summaries. It separates base size from option size, gross from net proceeds, and pricing date from settlement date. It requires an opened document before claiming exercise or upsizing and lists the terms to cover. agg1's version also names the pricing press release and the 8-K as the confirmation sources. Each carries a task lead.
observed: Both runs loaded the skill in turn 1 and produced term-by-term answers with each item separated. dom1 and agg1 covered more items (the dividend-stock payment mechanics, the floor price, the listing symbol, and the voting and fundamental-change terms) than inv1 did, but inv1 had no skill and still covered the main terms. agg1's skill step 4 ("open the press release before concluding unconfirmed") plausibly led to the FWP and 8-K opens. dom1's skill had a softer version of that step and it did not open them. Cost and turns rose: dom1 was 7 turns and $0.34, agg1 8 turns and $0.42, against inv1's 7 turns and $0.22. The skill and the tool_guidance edit were bundled in both runs.
verdict: confounded

component: systemprompt.md (trigger line for security_offering_terms)
candidates: dom1, agg1
change: Added one sentence telling the agent to call load_skill with `security_offering_terms` for securities-offering term questions.
observed: Both called load_skill as their first action. No skill-equipped run lacks the trigger, so its separate effect is not shown.
verdict: no observed effect

component: tool_guidance.md (embedded task lead: 424B5 URL and verified terms)
candidates: inv1 (in tool_guidance); dom1 and agg1 (in the skill)
change: Embedded the final 424B5 URL, the filing list and the key terms, labelled for re-confirmation.
observed: inv1 parsed the 424B5 in turn 1 with no discovery search. dom1 and agg1 still ran an edgar_search first, because the skill had to be loaded. All retrieved the terms from the opened text. base1 needed two searches to find the document. The saved turns did not change the substance of the answer.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks for the key terms of a registered securities offering (preferred, convertible, notes). The final prospectus supplement holds most terms, but the upsize from the launch size and the exercise of the over-allotment option appear only in the FWP, press release or closing 8-K. Search snippets mention those facts, and the base run repeats them unopened and leaks citation markup.
- **lesson**: In tool_guidance.md, add a rule that when a snippet suggests a material fact the prospectus does not state (an upsize, an exercised option, a closing), the agent opens the named confirming document (the FWP filed after pricing, or the closing 8-K body) with parse_html_page and retrieves the fact before stating it. If it cannot be opened, the agent says "unconfirmed". The rule is not "drop it unless the 424B5 says so". Keep this beside the cite-only-opened and plain-text rules.
- **evidence**: The "unconfirmed vs open to confirm" edit row. inv1 and dom1 declared the exercise and upsize unconfirmed. dom1 never opened the 8-K body or the FWP, even though its own retrieval showed 51,750,000 authorized shares. agg1 opened the FWP (30M to 45M shares) and the 8-K (51,750,000 shares issued, option exercised in full), then reported launch, base and final sizes with a source for each. The sourcing-hygiene row is confounded but consistent: every edited run kept sources to opened documents, unlike base1.
- **confidence**: low. This rests on one rollout per candidate. The contrast between agg1 and the others could also come from skill wording or luck, and nothing isolates the rule from the skill.
