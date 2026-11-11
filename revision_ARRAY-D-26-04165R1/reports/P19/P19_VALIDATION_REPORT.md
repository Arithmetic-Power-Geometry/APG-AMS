# P19 independent-seed screening validation — 2026-11-11

New seed 2027, versus P18 seed 42; ISOLET and Fashion-MNIST official train/test source archives. ISOLET: 1200 train, 150 calibration, 250 test, 617 dimensions; Fashion: 650 train, 100 calibration, 160 test, 784 dimensions. Train-only standardization, k=7, p={1,1.5,2,3,4}, 20% full-search-query budget.

| Policy | ISOLET | Fashion-MNIST |
|---|---:|---:|
| L2 | 88.40% | 75.625% |
| FullP (100% search) | 88.80% | 78.125% |
| High entropy, 20% | 88.00% | 76.250% |
| Low entropy, 20% | 88.00% | 75.625% |
| Low Euclidean confidence, 20% | 88.40% | 78.125% |
| Random, 20% | 88.00% | 76.250% |
| Calibration-selected policy, 20% | low confidence: 88.40% | low confidence: 78.125% |

**Finding:** The P18 apparent low-entropy advantage on Fashion-MNIST did not replicate. Confidence screening matched FullP accuracy on the Fashion-MNIST subsample at 20% query budget, but this does not establish entropy-specific novelty. Do not claim APG-AMS superiority.

**Limitations:** exploratory small stratified subsets, one new seed, same official test pools explored previously, post-hoc research direction, no latency benchmark, no uncertainty intervals. Fixed budget counts FullP query selections, not measured speedups.

The experimental script and JSON output were supplied as separate supplementary materials. Further validation should test whether an entropy-derived residual adds value beyond Euclidean confidence on a fresh held-out protocol.