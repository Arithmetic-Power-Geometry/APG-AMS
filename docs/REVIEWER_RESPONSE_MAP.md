# Reviewer-response experiment map

## Reviewer 1

Request: more evidence through more in-depth comparisons across datasets and different algorithms.

Artifact response:
- keeps the original eight datasets;
- adds direct NCA baseline under the same folds;
- supports optional LMNN baseline;
- reports accuracy, weighted F1, runtime, and APG search reduction;
- retains threshold-ablation and runtime-scaling workflows in the local artifact package.

## Reviewer 2

Request: add either extra applications or direct comparison with established metric-learning methods; reviewer explicitly mentions large-scale similarity search, retrieval, or high-dimensional data as desirable applications.

Artifact response:
- implements the direct established-method comparison route through NCA and optional LMNN;
- preserves Synthetic-50D as a high-dimensional stress/failure case;
- includes runtime and search-reduction accounting because APG-AMS is a computational screening contribution.

## Interpretation

NCA and LMNN learn supervised transformations. APG-AMS screens whether local p-search can be skipped. They should therefore be compared empirically without claiming they solve identical optimization problems.
