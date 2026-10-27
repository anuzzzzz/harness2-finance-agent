# Results

One row per run. *correct* = every rubric criterion passed (Vals' accuracy); *pass rate* = share of criteria passed. *paired* = tasks where Harness² beat / lost to / tied the base on pass rate. Each run's full summary is the JSON next to this file; trajectories are in the run's workflow artifact.

| run | executor / editor | k | tasks | web search | correct (base → H²) | pass rate (base → H²) | control pass rate | static-rule pass rate | paired W/L/T | cost per task (base → H²) | run total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `20261027-051421-k1-haiku-n10` | haiku-5-5 / sonnet-5-5 | 1 | 10 | on | 70.0% → 70.0% | 88.9% → 82.2% | — | — | 1/2/7 | $0.04 → $0.42 | $4.64 |
| `20261027-134135-k1-haiku` | haiku-5-5 / sonnet-5-5 | 1 | 10 | on | 70.0% → 80.0% | 83.9% → 91.7% | — | — | 3/0/7 | $0.07 → $0.66 | $6.99 |
