# q45

- adopted: `agg1`
- components: 0 skills; 3,248 always-on chars

## Why this was chosen
trivial: single final

## What each edit did
component: tool_guidance.md (inv1 version: generic rules plus a rule to open the 10-K for full-year questions, quarterly sum only as a cross-check, empty-search fallback, plus an Airbnb-specific paragraph naming the 10-K line)
candidates: inv1
change: Added tool guidance telling the agent to open the 10-K in the same turn as any earnings-release exhibit for a full-year question, and to treat a quarterly sum as a cross-check. It also included a task block stating that $1,407M is in the 10-K and giving the file name.
observed: base1 parsed only the Q4 letter, summed four quarters including an unconfirmed Q4 figure, and never opened the 10-K. inv1 started with a 10-K edgar_search, parsed the 10-K and the letter in parallel at turn 2, and read the annual line from the cash flow statement and the Adjusted EBITDA reconciliation at turn 3 (1,407 vs 1,120). It submitted at turn 4 for $0.099. The task block gave the 10-K filename and the value, so the contribution of the generic rule alone is confounded. base1 reached the same 1,407 value, so the gain is in sourcing quality rather than in the number.
verdict: confounded

component: skills/non_gaap_adjustment_lookup/SKILL.md and the systemprompt.md trigger line
candidates: dom1
change: Added a skill, loaded on a prompt trigger, that sends the agent to the 10-K annual reconciliation with the cash flow statement and the SBC note as cross-checks. It forbids silently summing quarters and flags 1,407 as an unverified lead.
observed: dom1 spent turn 1 on load_skill. It then parsed the 10-K at turn 2 and retrieved the reconciliation, cash flow and Note 12 figures in one call at turn 3. It submitted at turn 4 for $0.095. This is about the same cost and turn count as inv1, with the same value. The extra load turn bought no visible gain over a tool_guidance rule. The skill embedded task-specific values and URLs. The answer also carried a caveat that the figures came from an automated parse.
verdict: no observed effect

component: tool_guidance.md (agg1 version: generic rules only; open the 10-K for full-year questions, a quarterly sum is only a cross-check, empty-search fallback, cross-check garbled rows in another table, per-figure sourcing)
candidates: agg1
change: Kept the 10-K-first rule and the cross-check logic from inv1 and removed the Airbnb-specific block, so there were no company URLs or values in the harness.
observed: agg1 turn 1: the first edgar_search with a date filter returned 0 results, and the second search without the date filter found the 10-K. It parsed only the 10-K at turn 2 and retrieved the reconciliation row at turn 3 (1,407 / 1,120, Adjusted EBITDA 4,041). A second retrieve at turn 4 confirmed the cash flow line, and it submitted at turn 5 for $0.187. This is the same value as inv1 and dom1, reached without task-specific hints. Cost was higher, with one wasted search and a repeat retrieval. One rollout.
verdict: helped

## Transferable lesson
- **cue**: A full-fiscal-year non-GAAP or reconciliation figure is asked for, and the earnings-release exhibit (shareholder letter) shows only quarterly columns, so a base run rebuilds the year by summing quarters.
- **lesson**: In tool_guidance.md, add a generic rule that full-year questions open the 10-K at the same time as any earnings-release exhibit, read the annual column, and use a quarterly sum only as a cross-check. Cross-check garbled table rows against a second table, such as the cash flow statement. Do not put company URLs or values in the rule, and do not create a skill for it.
- **evidence**: base1 (never opened the 10-K, summed quarters, self-flagged Q4 as unverified) versus inv1 and agg1 (opened the 10-K at turn 2 and read the annual line directly, 4 and 5 turns). agg1 achieved this with no task-specific content. dom1's skill reached the same result but added a load turn with no gain at about the same cost.
- **confidence**: low. One rollout per arm, all reached the same value 1,407, and inv1 supplied task hints, so the evidenced gain is document-backed sourcing and not a different answer.
