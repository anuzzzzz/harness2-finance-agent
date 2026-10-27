# Run `20261027-150346-k1-haiku`

executor `claude-haiku-5-5` · editor `claude-sonnet-5-5` · judge `claude-sonnet-5-5` · k=1 · tasks=50 · web search on

| condition | correct (all criteria) | criteria pass rate | delivered | cost / task |
|---|---|---|---|---|
| base harness | 62.0% | 77.2% | 100.0% | $0.09 |
| Harness² k=1 | 72.0% | 83.8% | 100.0% | $1.05 (incl. $0.32 editor) |
| base ×4, blind pick (matched-cost control) | 62.0% | 79.6% | 100.0% | — |
| hand-written 'open the filing' guidance (static arm) | 68.0% | 82.2% | 100.0% | $0.11 |

Paired by task (criteria pass rate): Harness² better 8, base better 1, tie 41; sign test p = 0.04; mean difference +6.6 points (bootstrap 95% CI [+1.5, +13.3]).
Matched-cost control (blind pick among 4 base runs): correct 62.0%, pass rate 79.6%; oracle best-of-base 70.0% / 85.0%. Harness² vs control paired: 6 / 3 / 41 (p = 0.51). Noise floor: base pass rate varies by 7.0 points (SD) between re-runs of the same question.
Static arm vs Harness² paired: Harness² better 6, static better 5, tie 39 (p = 1.00); static vs base: static better 9, base better 3.
Judge: 97.0% of criteria unanimous across votes, 11 parse failures. Mean answer length: base 2690 chars, Harness² 2395.
Library entries written: 47. Stage errors: 0. Judge cost $5.20. Total $57.76.

## By stage

| stage | n | correct | pass rate | delivered | KEEP_BASE | mean cost |
|---|---|---|---|---|---|---|
| agg1 | 50 | 72.0% | 83.8% | 100.0% | 6.0% | $0.11 |
| base1 | 50 | 62.0% | 77.2% | 100.0% |  | $0.09 |
| ctl2 | 50 | 62.0% | 79.8% | 100.0% |  | $0.07 |
| ctl3 | 50 | 66.0% | 79.2% | 100.0% |  | $0.07 |
| ctl4 | 50 | 64.0% | 76.1% | 100.0% |  | $0.07 |
| dom1 | 50 | 68.0% | 81.6% | 100.0% | 6.0% | $0.11 |
| inv1 | 50 | 64.0% | 80.6% | 100.0% | 6.0% | $0.10 |
| static1 | 50 | 68.0% | 82.2% | 100.0% |  | $0.11 |

## By category

| category | n | base correct | H² correct | base pass rate | H² pass rate |
|---|---|---|---|---|---|
| Adjustments | 4 | 75.0% | 75.0% | 75.0% | 75.0% |
| Beat or Miss | 7 | 42.9% | 57.1% | 66.7% | 73.2% |
| Complex Retrieval | 3 | 33.3% | 66.7% | 90.6% | 94.4% |
| Financial Modeling  Projections | 4 | 50.0% | 50.0% | 83.2% | 85.7% |
| Market Analysis | 3 | 0.0% | 0.0% | 28.3% | 32.0% |
| Numerical Reasoning | 8 | 75.0% | 100.0% | 81.2% | 100.0% |
| Simple retrieval - Qualitative | 9 | 77.8% | 88.9% | 85.2% | 96.3% |
| Simple retrieval - Quantitative | 9 | 88.9% | 88.9% | 88.9% | 88.9% |
| Trends | 3 | 33.3% | 33.3% | 62.2% | 62.2% |

## Tasks

| task | category | base | H² (chosen) | cost |
|---|---|---|---|---|
| q07 | Simple retrieval - Qualitative | ✓ 100.0% | ✓ 100.0% (agg1) | $0.25 |
| q44 | Simple retrieval - Quantitative | ✓ 100.0% | ✓ 100.0% (agg1) | $0.56 |
| q19 | Numerical Reasoning | ✓ 100.0% | ✓ 100.0% (agg1) | $0.96 |
| q09 | Beat or Miss | ✓ 100.0% | ✓ 100.0% (agg1) | $0.41 |
| q45 | Adjustments | ✓ 100.0% | ✓ 100.0% (agg1) | $0.85 |
| q30 | Financial Modeling  Projections | ✓ 100.0% | ✓ 100.0% (agg1) | $1.66 |
| q04 | Complex Retrieval | ✓ 100.0% | ✓ 100.0% (agg1) | $0.56 |
| q42 | Market Analysis | ✗ 16.7% | ✗ 16.7% (agg1) | $2.31 |
| q14 | Trends | ✗ 16.7% | ✗ 16.7% (agg1) | $1.51 |
| q05 | Simple retrieval - Qualitative | ✗ 0.0% | ✓ 100.0% (agg1) | $0.42 |
| q11 | Simple retrieval - Quantitative | ✓ 100.0% | ✓ 100.0% (agg1) | $1.04 |
| q20 | Numerical Reasoning | ✗ 50.0% | ✓ 100.0% (agg1) | $1.04 |
| q47 | Beat or Miss | ✓ 100.0% | ✓ 100.0% (agg1) | $0.62 |
| q35 | Adjustments | ✓ 100.0% | ✓ 100.0% (agg1) | $0.52 |
| q12 | Financial Modeling  Projections | ✗ 72.7% | ✗ 72.7% (agg1) | $1.07 |
| q16 | Complex Retrieval | ✗ 91.7% | ✗ 83.3% (agg1) | $2.30 |
| q01 | Market Analysis | ✗ 11.1% | ✗ 22.2% (agg1) | $2.18 |
| q17 | Trends | ✓ 100.0% | ✓ 100.0% (agg1) | $1.74 |
| q25 | Simple retrieval - Qualitative | ✗ 66.7% | ✗ 66.7% (agg1) | $0.66 |
| q34 | Simple retrieval - Quantitative | ✓ 100.0% | ✓ 100.0% (agg1) | $0.79 |
| q24 | Numerical Reasoning | ✓ 100.0% | ✓ 100.0% (agg1) | $0.75 |
| q48 | Beat or Miss | ✗ 62.5% | ✗ 62.5% (agg1) | $0.57 |
| q40 | Adjustments | ✓ 100.0% | ✓ 100.0% (agg1) | $0.93 |
| q43 | Financial Modeling  Projections | ✗ 60.0% | ✗ 70.0% (agg1) | $1.39 |
| q06 | Complex Retrieval | ✗ 80.0% | ✓ 100.0% (agg1) | $0.69 |
| q46 | Market Analysis | ✗ 57.1% | ✗ 57.1% (agg1) | $2.60 |
| q02 | Trends | ✗ 70.0% | ✗ 70.0% (agg1) | $0.62 |
| q18 | Simple retrieval - Qualitative | ✓ 100.0% | ✓ 100.0% (agg1) | $0.87 |
| q32 | Simple retrieval - Quantitative | ✓ 100.0% | ✓ 100.0% (agg1) | $0.45 |
| q10 | Numerical Reasoning | ✓ 100.0% | ✓ 100.0% (agg1) | $1.21 |
| q38 | Beat or Miss | ✗ 0.0% | ✗ 0.0% (agg1) | $0.50 |
| q33 | Adjustments | ✗ 0.0% | ✗ 0.0% (agg1) | $1.42 |
| q31 | Financial Modeling  Projections | ✓ 100.0% | ✓ 100.0% (agg1) | $0.48 |
| q39 | Simple retrieval - Qualitative | ✓ 100.0% | ✓ 100.0% (agg1) | $0.47 |
| q08 | Simple retrieval - Quantitative | ✗ 0.0% | ✗ 0.0% (agg1) | $0.93 |
| q13 | Numerical Reasoning | ✓ 100.0% | ✓ 100.0% (agg1) | $0.97 |
| q03 | Beat or Miss | ✗ 66.7% | ✓ 100.0% (agg1) | $0.51 |
| q23 | Simple retrieval - Qualitative | ✓ 100.0% | ✓ 100.0% (agg1) | $0.86 |
| q37 | Simple retrieval - Quantitative | ✓ 100.0% | ✓ 100.0% (agg1) | $1.37 |
| q15 | Numerical Reasoning | ✓ 100.0% | ✓ 100.0% (agg1) | $1.56 |
| q49 | Beat or Miss | ✗ 37.5% | ✗ 50.0% (agg1) | $0.90 |
| q29 | Simple retrieval - Qualitative | ✓ 100.0% | ✓ 100.0% (agg1) | $1.91 |
| q36 | Simple retrieval - Quantitative | ✓ 100.0% | ✓ 100.0% (agg1) | $0.70 |
| q26 | Numerical Reasoning | ✓ 100.0% | ✓ 100.0% (agg1) | $0.71 |
| q50 | Beat or Miss | ✓ 100.0% | ✓ 100.0% (agg1) | $0.64 |
| q27 | Simple retrieval - Qualitative | ✓ 100.0% | ✓ 100.0% (agg1) | $1.29 |
| q28 | Simple retrieval - Quantitative | ✓ 100.0% | ✓ 100.0% (agg1) | $0.41 |
| q22 | Numerical Reasoning | ✗ 0.0% | ✓ 100.0% (agg1) | $3.56 |
| q21 | Simple retrieval - Qualitative | ✓ 100.0% | ✓ 100.0% (agg1) | $1.44 |
| q41 | Simple retrieval - Quantitative | ✓ 100.0% | ✓ 100.0% (agg1) | $0.43 |
