# q42

- adopted: `agg1`
- components: 0 skills; 4,625 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: tool_guidance.md (peer-comparison rule: open every company's FY 10-K in one turn, one formula and data basis for all companies, per-share only as a labelled cross-check, plain text with no citation tags)
candidates: inv1, agg1 (dom1 carried the same content in a skill)
change: Added generic tool guidance. It defines the payout ratio as cash-flow-statement dividends paid divided by GAAP net income attributable. It requires the same basis for every peer. It says to open all 10-Ks together, to report non-payers as 0%, and to name fiscal year ends. It also bans citation markup.
observed: base1 answered from search snippets after one search turn. It mixed KO aggregate dollars (78.63%) with PEP and KDP per-share figures, and it reconstructed KDP's dividend from nine-month data plus a guessed Q4. It also left raw cite tags in the answer. inv1 and agg1 each ran edgar_search per ticker at turn 1, parsed all the 10-Ks in parallel at turn 2, and retrieved the cash-flow dividends and net income at turn 3. Both submitted aggregate-basis ratios: KDP 82.86%, KO 78.63%, PEP 75.48%, MNST 0%. KDP's rank (first) did not change from base1, but PEP's and KDP's values did (75.48 and 82.86 against 76.69 and 84.76). Each arm is one rollout, and dom1 reached the same numbers via the skill, so the effect of the guidance specifically is not isolated.
verdict: helped

component: tool_guidance.md (inv1's task-facts paragraph giving KO's $8,359M and $10,631M as verified)
candidates: inv1
change: Embedded Coca-Cola's dividends and net income in the guidance and told the agent to re-verify the peers only.
observed: inv1 never opened KO's 10-K and cited "figures given in the task" in its answer. That left the subject company unverified in the delivered numbers. agg1 and dom1, which had no such paragraph, retrieved KO from the filing at turn 3 and turn 4 respectively. The values agreed with the embedded ones.
verdict: hurt

component: tool_guidance.md (agg1's rule to open the subject company's 10-K too and not trust remembered or prompt-supplied figures; retrieve several related figures per call)
candidates: agg1
change: Replaced inv1's task-facts paragraph with a generic instruction to re-read the subject company's figures from its own filing. Added a line to ask for dividends paid, net income, diluted EPS and declared DPS in one retrieve call.
observed: agg1 retrieved KO, PEP, KDP and MNST in four parallel retrieve calls at turn 3 and submitted at turn 4. Its answer showed a KO declared-basis cross-check (1.94 / 2.46 = 78.86%), which base1 had done with an EPS figure it said was not in its sources. No PEP cross-check appeared because EPS was not requested for PEP. Since it is a single rollout, the contribution is confounded with the shared peer-comparison rule.
verdict: confounded

component: skills/dividend_payout_peer_compare/SKILL.md and the systemprompt.md trigger line
candidates: dom1
change: Added a skill, loaded by a prompt trigger, with the same definition (paid basis, same basis for all companies), peer-set guidance and non-payer rule. It also embedded KO's figures as leads to re-verify.
observed: dom1 spent turn 1 on load_skill and then needed searches without ticker filters at turn 2. Its edgar_search results were noisy, with unrelated issuers such as Kellanova and Berkshire. It reached the same numbers as inv1 and agg1 in 5 turns at $0.455, against inv1's $0.311. It retrieved KO's figures from the filing, labelling them as leads to be re-verified, which is the behavior agg1 later wrote into tool_guidance. The load turn added cost with no visible gain over tool_guidance, though the cost differences also reflect ticker filters and are not cleanly attributable.
verdict: no observed effect

## Transferable lesson
- **cue**: A multi-company comparison or ranking on one ratio (payout, margin, leverage), where the base run answers from search snippets and mixes data bases across companies (aggregate dollars for one, per-share for others, or reconstructed figures).
- **lesson**: In tool_guidance.md, add a generic peer-comparison rule: state the peer set and one formula, and apply the same data basis to every company. Open every company's 10-K in the same turn, including the subject company, and retrieve the same line items from each. Treat per-share ratios only as a labelled cross-check. Do not embed the subject company's figures in the guidance as "verified". An agent that sees them will skip retrieving them (inv1 cited "figures given in the task"). If prior figures are mentioned, label them as leads and require re-reading from the filing. Do not build a skill for this.
- **evidence**: Rows 1 to 3. base1 mixed bases and used snippets. inv1 and agg1 opened the 10-Ks in parallel and produced like-for-like aggregate ratios in 4 to 5 turns. inv1's embedded KO facts led it to skip KO's retrieval, while agg1 re-read KO. dom1's skill reached the same numbers but added a load turn (about $0.455 against $0.311 for inv1 and $0.455 for agg1, so cost evidence is mixed).
- **confidence**: low. One rollout per arm. All three edited runs reached identical values, so the evidenced gain is consistent basis and filing-backed sourcing, not a different ranking. The inv1 skip-retrieval problem is a single instance.
