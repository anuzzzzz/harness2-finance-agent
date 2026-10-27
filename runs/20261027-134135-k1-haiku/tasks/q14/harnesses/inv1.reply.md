<notes>
KEEP_BASE. Only one rollout exists, so there is no divergence between runs to fix.

The base run followed a sound process:
- It searched edgar_search for the 10-Ks with the company, CIK and form type filters.
- It parsed the FY2024 and FY2023 10-Ks in parallel and retrieved CFO, capex and revenue with period, unit and row label.
- It noticed that the FY2022 CFO of 4,504 is distorted by the Zillow Offers wind-down, which includes a roughly $3.9B inventory decrease.
- It showed capex both as property and equipment only and as property and equipment plus intangibles.
- It submitted at turn 4 with sources and unrounded arithmetic.

I see no repeated failure, no tool error and no skipped invariant to trace an edit to. Adding always-on rules or a skill would cost context on every run without changing behaviour that was already correct. The cross-check of FY2022 figures against the FY2022 10-K, which was found but not parsed, is a one-off optional step. It is not a failure observed in this trajectory.
</notes>