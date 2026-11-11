# P21 — Hidden-gap audit (11 November 2026)

P18's reversed entropy gate appeared to improve Fashion-MNIST at a 20% FullP-query budget: low entropy 116/160 vs confidence 115/160. This was a **one-query difference** on a test subset used during exploration. P19 did not replicate: low entropy 121/160 vs confidence 125/160. P20: low entropy 114/160 vs confidence 114/160. ISOLET confidence outperformed low entropy at 20% budget in P18 (212 vs 205 of 250), P19 (221 vs 220) and P20 (211 vs 210). Repeated test-pool reuse means these are not independent confirmatory replications.

**New exact certificate theorem.** For 1 <= p <= 4, the norm inequalities imply that if Euclidean distances r_(k+1) > sqrt(d) r_k, the Euclidean top-k neighbor set is unchanged for all p in [1,4]. Thus the FullP majority-vote label cannot change. This condition requires no entropy. It is mathematically valid but conservative.

**New P21 executed audit.** Same P20 seed 2041 and stratified subsets, k=7, train-only StandardScaler. ISOLET d=617, 250 test queries: required r8/r7 >24.839, observed maximum 1.070, certified 0/250. Fashion-MNIST d=784, 160 test queries: required >28.000, observed maximum 1.143, certified 0/160. Therefore generic norm bounds certify zero savings on these subsets.

**Research gap:** develop tighter query-specific certified distance intervals and compare optimized end-to-end runtime against FullP and low-confidence screening. No APG-AMS accuracy or entropy-specific superiority is established by P18–P21. Detailed local report, script and JSON are in the conversation artifacts.