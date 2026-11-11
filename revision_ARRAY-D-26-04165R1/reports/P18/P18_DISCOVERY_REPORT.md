# P18 — Exploratory high-dimensional entropy-gate reversal

Date: 2026-11-11. Inputs: Fashion-MNIST and ISOLET source archives. Both contain the required labeled images/features.

**Design:** Official dataset train/test partitions; stratified subsets (seed 42). ISOLET: 1,200 train, 150 calibration, 250 test, 617 features. Fashion-MNIST: 650 train, 100 calibration, 160 test, 784 features. Train-only StandardScaler, k=7, p={1,1.5,2,3,4}; full search chooses p maximizing training-neighborhood vote purity with deterministic tie-breaks. Entropy is Shannon entropy of squared per-query minmax-positive transformed standardized coordinates. Budgets fixed to 10%, 20%, 40% full-search queries, same for every screening policy. FullP predictions precomputed offline; this is **not a runtime experiment**.

| Method at 20% FullP budget | ISOLET accuracy | Fashion-MNIST accuracy |
|---|---:|---:|
| L2, 0% | 81.60% | 70.625% |
| Original high entropy priority | 81.60% | 70.625% |
| **Low entropy priority** | 82.00% | **72.50%** |
| Low Euclidean confidence | **84.80%** | 71.875% |
| Random | 81.60% | 69.375% |
| FullP, 100% | 84.40% | 72.50% |

**Hidden gap:** With fixed tau=.92, 248/250 (99.2%) ISOLET and 144/160 (90%) Fashion test queries trigger full exponent search; the entropy gate saturates in these high-dimensional cases. On Fashion-MNIST, low-entropy priority matched FullP accuracy with 20% of queries searched, but ISOLET low-confidence screening was stronger. High-entropy ranking was weak on both. AUC for predicting query-level FullP benefit: high entropy .327 (ISOLET) / .333 (Fashion); low L2 confidence .907/.807, based on only 9/6 positive benefit cases and hence unstable.

**Novelty hypothesis, NOT demonstrated superiority:** An entropy-direction-aware, validation-calibrated, budget-controlled gate might fix high-dimensional saturation. This is a NEW variant, not evidence for the original high-entropy gate. It must be compared against low-confidence screening and random under a precommitted test protocol. Test-policy choices were explored post hoc; do not cite the best policy as an unbiased confirmatory result.

**Limitations:** Small subsets, one seed, no inferential intervals, no runtime or ANN, retrospective budgets, test exploration and potential selection bias. Next: lock selection on calibration data and evaluate on a genuinely untouched test partition across multiple seeds, measuring full pipeline latency. Do not make superiority claims now.

The experimental script and JSON output are supplied in the separate supplementary archive, not in this public report directory. The ISOLET `.Z` members require decompression with `uncompress -c`.
