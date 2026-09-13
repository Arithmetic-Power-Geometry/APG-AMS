# Point-by-point response draft

## Reviewer 1

**Response.** We thank the reviewer for this constructive suggestion. We substantially expanded the empirical study. The revised artifact evaluates five methods—Euclidean k-NN, full adaptive p-search, APG-AMS, Neighborhood Components Analysis (NCA), and Large Margin Nearest Neighbor (LMNN)—under common outer 10-fold stratified folds. The evaluation now contains 12 datasets, including four additional real-world datasets (Ionosphere, Sonar, Banknote Authentication, and Mice Protein Expression). We report accuracy, weighted F1, end-to-end runtime, APG-AMS search reduction, and paired statistical tests. These additions directly address the request for deeper comparisons across both datasets and algorithms.

## Reviewer 2

**Response.** We thank the reviewer for identifying this gap. Following the suggested direct-comparison route, we added NCA and LMNN as established supervised metric-learning baselines and evaluated them under the same outer 10-fold protocol as APG-AMS. We also added real-world radar, sonar, image-derived banknote, and protein-expression datasets, including higher-dimensional Sonar and Mice Protein Expression data. The revision preserves the distinction between supervised metric learning and APG-AMS: NCA and LMNN learn transformations, whereas APG-AMS is a screening mechanism that decides when local p-search can be skipped. Accordingly, we compare predictive performance and end-to-end runtime while separately reporting APG-AMS search reduction.
