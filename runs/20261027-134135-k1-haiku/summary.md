# Run `20261027-134135-k1-haiku`

executor `claude-haiku-5-5` · editor `claude-sonnet-5-5` · judge `claude-sonnet-5-5` · k=1 · tasks=10 · web search on

| condition | correct (all criteria) | criteria pass rate | delivered | cost / task |
|---|---|---|---|---|
| base harness | 70.0% | 83.9% | 100.0% | $0.07 |
| Harness² k=1 | 80.0% | 91.7% | 100.0% | $0.66 (incl. $0.24 editor) |

Paired by task (criteria pass rate): Harness² better 3, base better 0, tie 7.
Library entries written: 8. Stage errors: 0. Judge cost $0.39. Total $6.99.

## By stage

| stage | n | correct | pass rate | delivered | KEEP_BASE | mean cost |
|---|---|---|---|---|---|---|
| agg1 | 10 | 80.0% | 91.7% | 100.0% | 20.0% | $0.13 |
| base1 | 10 | 70.0% | 83.9% | 100.0% |  | $0.07 |
| dom1 | 10 | 80.0% | 90.0% | 100.0% | 20.0% | $0.13 |
| inv1 | 10 | 80.0% | 90.0% | 100.0% | 20.0% | $0.08 |

## By category

| category | n | base correct | H² correct | base pass rate | H² pass rate |
|---|---|---|---|---|---|
| Adjustments | 1 | 100.0% | 100.0% | 100.0% | 100.0% |
| Beat or Miss | 1 | 100.0% | 100.0% | 100.0% | 100.0% |
| Complex Retrieval | 1 | 100.0% | 100.0% | 100.0% | 100.0% |
| Financial Modeling  Projections | 1 | 100.0% | 100.0% | 100.0% | 100.0% |
| Market Analysis | 1 | 0.0% | 0.0% | 16.7% | 50.0% |
| Numerical Reasoning | 1 | 100.0% | 100.0% | 100.0% | 100.0% |
| Simple retrieval - Qualitative | 2 | 50.0% | 100.0% | 94.4% | 100.0% |
| Simple retrieval - Quantitative | 1 | 100.0% | 100.0% | 100.0% | 100.0% |
| Trends | 1 | 0.0% | 0.0% | 33.3% | 66.7% |

## Tasks

| task | category | base | H² (chosen) | cost |
|---|---|---|---|---|
| q07 | Simple retrieval - Qualitative | ✓ 100.0% | ✓ 100.0% (agg1) | $0.19 |
| q44 | Simple retrieval - Quantitative | ✓ 100.0% | ✓ 100.0% (agg1) | $0.50 |
| q19 | Numerical Reasoning | ✓ 100.0% | ✓ 100.0% (agg1) | $0.49 |
| q09 | Beat or Miss | ✓ 100.0% | ✓ 100.0% (agg1) | $0.26 |
| q45 | Adjustments | ✓ 100.0% | ✓ 100.0% (agg1) | $0.65 |
| q30 | Financial Modeling  Projections | ✓ 100.0% | ✓ 100.0% (agg1) | $1.03 |
| q04 | Complex Retrieval | ✓ 100.0% | ✓ 100.0% (agg1) | $0.40 |
| q42 | Market Analysis | ✗ 16.7% | ✗ 50.0% (agg1) | $1.74 |
| q14 | Trends | ✗ 33.3% | ✗ 66.7% (agg1) | $0.99 |
| q05 | Simple retrieval - Qualitative | ✗ 88.9% | ✓ 100.0% (agg1) | $0.34 |
