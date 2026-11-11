# P20 — Incremental entropy test beyond Euclidean confidence (11 Nov 2026)

Exploratory independent-seed test, RNG 2041. Source: Fashion-MNIST and ISOLET dataset archives. Code derives from P19; uses original train/test partitions and train-only StandardScaler. ISOLET 1200 train / 150 calibration / 250 test; Fashion 650 train / 100 calibration / 160 test. k=7; p grid [1,1.5,2,3,4]. Query entropy is squared-positive-minmax coordinate entropy. FullP selection uses majority-class vote purity. All screening policies use **20% FullP-query budget**, not measured 20% compute.

A hybrid score is low-confidence percentile rank plus beta times centered high-entropy percentile rank. Beta selected on **calibration outcomes only** from [-2,-1,-0.5,0,0.5,1,2]; tie-break chooses smallest |beta|. Evaluation test partition not used to choose beta within P20, but the same official test pool has been used during prior exploratory P18/P19 analyses; therefore this is NOT an independent confirmatory experiment.

| Dataset | L2 | FullP | Confidence 20% | Hybrid 20% | Chosen beta |
|---|---:|---:|---:|---:|---:|
| ISOLET | 82.40% | 85.20% | 84.40% | 84.40% | 0 |
| Fashion-MNIST | 70.00% | 71.25% | 71.25% | 71.25% | -1 |

**Finding:** No incremental accuracy advantage from entropy on either dataset. This does not support entropy-specific superiority. Fashion hybrid matched FullP at lower candidate-query budget, but confidence alone did the same. Differences on these small subsets are unstable.

**Risks:** post-hoc repeated experimentation, one seed, very small test partitions, no inferential intervals, no end-to-end timing, training sample size too small for strong classification claims. Future testing must use a new genuinely untouched benchmark or pre-registered split and compare with confidence and random baselines, including latency. Do not alter the original manuscript to claim positive results unsupported by this test.

The associated experimental script and JSON output were supplied separately as supplementary materials.
