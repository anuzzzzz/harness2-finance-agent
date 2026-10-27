# q06

- adopted: `agg1`
- components: 0 skills; 5,000 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md (general rules: snippet is a lead, open primary documents with parse_html_page then retrieve_information, cite only opened documents, plain text with no citation markup, no empty-query searches, as-of cutoff)
candidates: inv1, dom1, agg1
change: Went from empty to a rule set. The rules say snippets are leads only, each company's guidance must be read from an opened document, post-as-of-date filings must not be used or cited, only opened documents may be sources, and the answer is plain text. agg1 added a rule to open the call transcript and check who said a figure, and to treat an analyst's unconfirmed figure as not company guidance. inv1 and dom1 lacked that rule.
observed: base1 ran three web_searches, opened nothing, listed unopened sources (the Meta IR release and a CNBC article), and leaked <cite index> markup. inv1, dom1 and agg1 each parsed the Meta Q4 release and the Alphabet Q4 release, and none leaked markup. inv1 and dom1 listed only opened documents. inv1 opened the Amazon 10-K but not the call, and said the $100B wording was unconfirmed and seen only in snippets. dom1 and agg1 opened the Amazon call transcript and found that $100B was an analyst's question, with management saying only that $26.3B was a representative run rate. The effect was on verification and sourcing. The ranking cannot be separated from the task-fact leads, which were embedded in inv1 and agg1, and dom1 carried its own leads in its skill.
verdict: confounded

component: tool_guidance.md (task-fact leads: Meta, Alphabet and Amazon URLs and snippet-derived guidance figures)
candidates: inv1, agg1 (dom1 carried similar leads in its skill)
change: Embedded the Meta and Alphabet Q4 release URLs and the guided figures, labelled "re-confirm in the opened text". agg1 also embedded the Amazon transcript URL.
observed: agg1 parsed all three documents in turn 1 and submitted in 3 turns, at $0.008. inv1 needed 6 turns, with several edgar_searches and one null-query web_search, despite the Meta and Alphabet URLs. The retrieved figures matched the leads. The task-specific content has no transfer value beyond turn savings.
verdict: no observed effect

component: skills/capex_guidance_compare/SKILL.md and the trigger line in systemprompt.md
candidates: dom1
change: Added an on-demand skill for ranking forward spending guidance across companies. It covers an as-of cutoff, definitional differences, point versus range handling and an answer contract, plus leads. systemprompt.md gained a line telling the agent to load it.
observed: dom1 loaded the skill first, then ran three edgar_searches, parsed the three documents and the transcript, and submitted in 6 turns. inv1, with no skill, also took 6 turns and reached the same ranking. The skill's definition notes appear in dom1's caveats, but inv1 also noted definitional differences without the skill. dom1 and agg1 both opened the transcript, so the skill is not shown to have driven that. agg1 dropped the skill and submitted in 3 turns.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks which of several companies plans to spend the most (capex, buybacks) for a future year. One company's figure is commonly reported by the press as a round number, but it may come from call commentary or an analyst's question rather than a release. Base search snippets and news pages make the figure look like formal guidance.
- **lesson**: In tool_guidance.md, require that each company's guided figure be read from an opened primary document, the release or 10-K. Where a figure appears only on the earnings call, require opening the transcript and recording who said it and whether it was prepared remarks or an analyst's question, labelling it "management commentary" or "not guidance" accordingly. Also require stating whether the ranking holds at every end of each range. Keep this in always-on tool_guidance, not a skill.
- **evidence**: Rows 1 and 3. base1 relied on snippets, which treated Amazon's $100B as guidance, and listed unopened sources. dom1 and agg1 opened the transcript and found that the $100B was an analyst's number and management said only that $26.3B was a representative run rate. inv1 never opened the transcript and left the figure as "unconfirmed, from press coverage". The skill row shows dom1's skill run matched inv1's skill-free run in turn count and ranking.
- **confidence**: low. Each candidate is a single rollout. agg1 carried the transcript-check rule together with the leads and received the same lead URLs as the others. Amazon ranked first in every run, so the evidence is about verification and honest labelling, not accuracy. agg1's answer headlined "Amazon, but only on an implied basis" and then compared Alphabet against Meta as the formal-guidance ranking, which complicates the headline for a reader.
