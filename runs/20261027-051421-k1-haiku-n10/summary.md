# Run `20261027-051421-k1-haiku-n10`

executor `claude-haiku-5-5` · editor `claude-sonnet-5-5` · judge `claude-sonnet-5-5` · k=1 · tasks=10 · web search on

| condition | correct (all criteria) | criteria pass rate | delivered | cost / task |
|---|---|---|---|---|
| base harness | 70.0% | 88.9% | 100.0% | $0.04 |
| Harness² k=1 | 70.0% | 82.2% | 100.0% | $0.42 (incl. $0.27 editor) |

Paired by task (criteria pass rate): Harness² better 1, base better 2, tie 7.
Library entries written: 8. Stage errors: 0. Judge cost $0.43. Total $4.64.

## By stage

| stage | n | correct | pass rate | delivered | KEEP_BASE | mean cost |
|---|---|---|---|---|---|---|
| agg1 | 10 | 70.0% | 82.2% | 100.0% | 20.0% | $0.04 |
| base1 | 10 | 70.0% | 88.9% | 100.0% |  | $0.04 |
| dom1 | 10 | 80.0% | 88.3% | 100.0% | 10.0% | $0.04 |
| inv1 | 10 | 80.0% | 90.0% | 100.0% | 10.0% | $0.04 |

## By category

| category | n | base correct | H² correct | base pass rate | H² pass rate |
|---|---|---|---|---|---|
| Adjustments | 1 | 100.0% | 100.0% | 100.0% | 100.0% |
| Beat or Miss | 1 | 100.0% | 100.0% | 100.0% | 100.0% |
| Complex Retrieval | 1 | 100.0% | 100.0% | 100.0% | 100.0% |
| Financial Modeling  Projections | 1 | 100.0% | 100.0% | 100.0% | 100.0% |
| Market Analysis | 1 | 0.0% | 0.0% | 33.3% | 50.0% |
| Numerical Reasoning | 1 | 100.0% | 100.0% | 100.0% | 100.0% |
| Simple retrieval - Qualitative | 2 | 50.0% | 50.0% | 94.4% | 61.1% |
| Simple retrieval - Quantitative | 1 | 100.0% | 100.0% | 100.0% | 100.0% |
| Trends | 1 | 0.0% | 0.0% | 66.7% | 50.0% |

## Tasks

| task | category | base | H² (chosen) | cost |
|---|---|---|---|---|
| q07 | Simple retrieval - Qualitative | ✓ 100.0% | ✓ 100.0% (agg1) | $0.18 |
| q44 | Simple retrieval - Quantitative | ✓ 100.0% | ✓ 100.0% (agg1) | $0.20 |
| q19 | Numerical Reasoning | ✓ 100.0% | ✓ 100.0% (agg1) | $0.23 |
| q09 | Beat or Miss | ✓ 100.0% | ✓ 100.0% (agg1) | $0.35 |
| q45 | Adjustments | ✓ 100.0% | ✓ 100.0% (agg1) | $0.44 |
| q30 | Financial Modeling  Projections | ✓ 100.0% | ✓ 100.0% (agg1) | $0.45 |
| q04 | Complex Retrieval | ✓ 100.0% | ✓ 100.0% (agg1) | $0.53 |
| q42 | Market Analysis | ✗ 33.3% | ✗ 50.0% (agg1) | $0.84 |
| q14 | Trends | ✗ 66.7% | ✗ 50.0% (agg1) | $0.57 |
| q05 | Simple retrieval - Qualitative | ✗ 88.9% | ✗ 22.2% (agg1) | $0.41 |
