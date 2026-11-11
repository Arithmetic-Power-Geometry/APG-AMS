# P22 exact early-abandon metric evaluation — 11 Nov 2026

ISOLET official training/test pools; seed 2901 stratified subsamples of 600 training and 60 test queries; 617 dimensions; train-only standardization; k=7. For each p in [1,1.5,2,3,4], seed current top-k using exact p distances of Euclidean top-7; scan all remaining candidates and terminate partial sum of nonnegative |x_i-q_i|^p when it exceeds the current kth exact sum. Coordinate order chosen by train-set variance only. Verify full ordered top-7 IDs against SciPy cdist.

| p | Coordinates avoided | Exact ordered top7 | SciPy cdist s | Python pruning s |
|---|---:|---|---:|---:|
| 1 | 33.15% | yes | 0.0167 | 7.0414 |
| 1.5 | 42.60% | yes | 0.2523 | 5.9772 |
| 2 | 49.75% | yes | 0.0152 | 5.3518 |
| 3 | 59.53% | yes | 0.2520 | 4.2210 |
| 4 | 65.55% | yes | 0.2457 | 3.5737 |

**Proof:** A partial p-power distance sum is a lower bound on the completed sum because every remaining term is nonnegative. A candidate with partial sum strictly larger than the current kth exact sum cannot enter the final top-k. Strict comparison and deterministic tie ordering preserve exact neighbor identity. This certificate is query- and candidate-specific, much tighter than P21's global norm ratio.

**Honest interpretation:** This demonstrates **exact arithmetic-work reduction** against exhaustive p-distance calculation; it does NOT demonstrate elapsed-time superiority, because the Python loop is much slower than optimized SciPy. Early abandonment is established prior art and not an entropy-specific novelty. A compiled/vectorized implementation and direct comparison to optimized FullP, L2, and confidence screening is needed. The method may be useful as an exact FullP subroutine in APG-AMS but cannot rescue unsupported entropy superiority.

Reproduce: `python p22_exact_pruning.py` with user-uploaded ISOLET and prepared extracted ISOLET data. Local results JSON accompanies script.