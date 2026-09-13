# APG-AMS

Reproducibility artifact for **APG-AMS: Entropy-Guided Screening for Adaptive Metric Search in Distance-Based Learning**.

This repository supports the revised Array submission by providing:

- a reference implementation of APG-AMS;
- Euclidean k-NN and full local p-search baselines;
- direct comparison scaffolding for Neighborhood Components Analysis (NCA);
- optional LMNN comparison when `metric-learn` is installed;
- reproducible 10-fold stratified cross-validation;
- threshold ablation;
- runtime/search-reduction accounting;
- automated tests and GitHub Actions CI.

The artifact is designed to address reviewer requests for deeper algorithmic comparisons and stronger experimental evidence.

## Methods

Candidate Minkowski exponents: `p in {1, 1.5, 2, 3, 4}`.

For each query, APG-AMS computes normalized entropy of squared coordinate weights. If entropy is below threshold `tau`, Euclidean distance is used. Otherwise, all candidate p-values are evaluated and the local-purity-maximizing candidate is selected.

NCA and LMNN are treated as supervised metric-learning baselines and are not presented as the same class of method as APG-AMS. Their role is empirical comparison under a common evaluation protocol.

## Quick start

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/run_benchmarks.py --output results/benchmark_summary.csv
python scripts/run_threshold_ablation.py --output results/threshold_ablation.csv
python scripts/run_runtime_scaling.py --output results/runtime_scaling.csv
```

Optional LMNN baseline:

```bash
python -m pip install metric-learn
python scripts/run_benchmarks.py --include-lmnn --output results/benchmark_summary_with_lmnn.csv
```

## Reproducibility principles

- Standardization is fit only on the training fold.
- NCA is fit only on the training fold.
- LMNN, when used, is fit only on the training fold.
- The same outer stratified folds are used for all compared methods.
- No test labels are used during training or preprocessing.
- Search reduction is reported separately from wall-clock runtime.

## Repository layout

```text
src/apg_ams/        Core implementation
scripts/            Reproduction scripts
tests/              Automated tests
results/            Generated CSV outputs
docs/               Reviewer-mapping and artifact notes
.github/workflows/  Continuous integration
```

## License

Apache License 2.0.
