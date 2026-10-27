# q42

- adopted: `agg1`
- components: 1 skill; 3,259 always-on chars

## Why this was chosen
trivial: single candidate

## What each edit did
component: tool_guidance.md
candidates: inv1, agg1 (dom1 did not change it)
change: Went from empty to a rule set: a snippet is a lead, not evidence. Open each company's 10-K with parse_html_page, one key per company, and ask retrieve_information targeted questions. Use edgar_search, not question wording. Cite only opened documents. For multi-company comparisons, use the same definition and basis for every company. No PDFs. Plain-text answer.
observed: base1 ran five web_search calls and never opened a filing. It cited unopened 10-Ks, 10-Qs and PDFs and gave two conflicting rankings. inv1 and agg1 opened every 10-K and retrieved inputs from the text. dom1 had no tool_guidance but also parsed and retrieved, because its skill said to, so the carrier of the retrieval behaviour is not isolated. All three edited runs reached the same GAAP figures (KDP 84.76%, KO 78.86%, PEP 76.69%).
verdict: confounded

component: skills/peer_payout_ratio_compare/SKILL.md (inv1 and agg1) and skills/peer_payout_ratio/SKILL.md (dom1)
candidates: inv1, dom1, agg1
change: Added an on-demand skill: name the peer set and show non-payers as excluded; use one definition for all companies (declared DPS / GAAP diluted EPS, with a cash-paid / net income cross-check); give one primary GAAP ranking, with adjusted EPS only as a labelled secondary column; open each 10-K and retrieve the inputs. dom1 and agg1 added PepsiCo's 52-week fiscal year and the sum of quarterly dividends. agg1 added a flag for special-dividend distortion (COKE) and an outlier flag. All carry unverified figure leads and 10-K URLs.
observed: All three loaded the skill first and parsed the 10-Ks, including PepsiCo's, which base1 never opened. Each submitted one committed GAAP ranking with a cash cross-check, where base1 had given two rankings. dom1 and agg1 also included Coca-Cola Consolidated and flagged its special-dividend distortion (5.00% headline vs 29.32% cash basis). inv1 only listed it as excluded. Because the skill came with tool_guidance in inv1 and agg1, and no skill-free run exists on the new harness, the skill's effect is not isolated. The shift to a single primary basis is plausibly due to the skill, since all three skill runs did it and base1 did not.
verdict: confounded

component: skills/peer_payout_ratio_compare/SKILL.md (adjusted-EPS handling and unverified leads)
candidates: inv1, dom1, agg1
change: Adjusted or core EPS may appear only as a labelled secondary column, only if retrieved from an opened document. The skill leads carried snippet figures (KO comparable EPS $2.88, KDP adjusted EPS $1.92) marked unverified.
observed: base1 headlined both bases as equal answers, which gave opposite orders. All three candidates kept GAAP primary. No run verified KO's $2.88 or KDP's $1.92, because the 10-Ks do not carry them. inv1 and dom1 gave only PepsiCo's core payout (65.31–65.32%), and agg1 dropped the adjusted column entirely. The secondary adjusted ranking in base1 was therefore not reproduced. Whether the GAAP-only answer is better is not settled by the record.
verdict: confounded

component: systemprompt.md
candidates: inv1, dom1, agg1
change: Added one trigger line telling the agent to call load_skill with the payout-comparison skill for payout-ratio peer comparisons.
observed: All three called load_skill as their first action. There is no skill-equipped run without the trigger, so its separate effect is not shown.
verdict: no observed effect

component: LongTermMEMORY.md / guardrails.md
candidates: none
change: Left empty in every candidate.
observed: None.
verdict: no observed effect

## Transferable lesson
- **cue**: A question asks to compare or rank a company's ratio (payout, margin, leverage) against its competitors. The base agent works from search snippets, mixes GAAP and adjusted bases, gives two competing rankings, and never opens one peer's filing.
- **lesson**: Add an on-demand skill, triggered by one line in systemprompt.md, that fixes the peer set and states exclusions, one definition and one GAAP primary basis for every company, and a cash-based cross-check. Adjusted EPS is only a labelled secondary column. Require each company's 10-K to be opened and retrieved from. Pair it with a tool_guidance.md rule that snippets are leads and that every company's inputs come from its own filing. Add edge cases to the skill (non-December fiscal year, special dividends, non-payers) rather than to always-on text.
- **evidence**: The tool_guidance and skill rows. base1 used five searches, opened no filing, cited unopened sources and gave two conflicting rankings. inv1, dom1 and agg1 all opened the three 10-Ks, including PepsiCo's, and submitted one GAAP ranking (KDP 84.76 > KO 78.86 > PEP 76.69) with a cash cross-check that gave the same order. dom1 and agg1 additionally retrieved the Coca-Cola Consolidated 10-K and flagged its special dividend.
- **confidence**: low. Each candidate is one rollout, and the guidance and the skill were never varied independently (dom1 had the skill alone and still verified). The figures were the same across runs, so the evidence shows a difference in verification and framing, not in accuracy. Whether GAAP-only is a better headline than showing both bases is not established.
