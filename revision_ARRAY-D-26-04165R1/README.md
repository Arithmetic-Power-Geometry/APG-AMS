# ARRAY-D-26-04165R1 — supplementary revision evidence

This folder records exploratory research and audits for **APG-AMS: Entropy-Guided Screening for Adaptive Metric Search in Distance-Based Learning** (Elsevier *Array*, manuscript ARRAY-D-26-04165R1). The original reproducibility workflow remains in the repository root (`src/`, `scripts/`, `results/`, `tests/`).

## Available here
- `reports/P18/`: high-dimensional screening and gate-direction exploratory findings.
- `reports/P19/`: independent-seed screening validation and failure to replicate reversed-gate advantage.
- `reports/P20/`: entropy incremental-value test beyond confidence screening.
- `reports/P21/`: exact norm-bound certification audit.
- `reports/P22/`: exact early-abandon coordinate-work audit.
- `reports/P23/`: revision and reproducibility audit, including which reruns were completed.

## Important reproducibility status
These **reports are not a complete upload of the 26-file supplementary ZIP**. The complete source/data-output package is attached to the author's ChatGPT revision delivery and should be deposited separately before claiming the full supplement is publicly hosted here. In particular, the scripts and JSON/CSV outputs for P05, P06, P14, P15, and P18–P22 are not yet all in this GitHub folder. See `reports/P23/` for rerun status and unresolved limitations.

No new large-scale ANN comparison or entropy-specific superiority is claimed. The original 66.47% reduction is in candidate exponent evaluations relative to FullP, **not** wall-clock speed. The P22 coordinate savings exclude its Euclidean initialization scan. The grouped Mice Protein source requires independent verification.

## Existing public reproducibility files
- [Original experiment runner](../scripts/run_revision_experiments.py)
- [Benchmark results](../results/benchmark_summary.csv)
- [Source implementation](../src/apg_ams/)
- [Tests](../tests/)

**Date:** 11 November 2026. Revision due 17 November 2026.
