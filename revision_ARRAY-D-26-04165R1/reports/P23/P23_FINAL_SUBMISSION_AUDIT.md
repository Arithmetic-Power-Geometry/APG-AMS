# P23 — Array manuscript revision and reproducibility audit (11 November 2026)

Manuscript: ARRAY-D-26-04165R1, *APG-AMS: Entropy-Guided Screening for Adaptive Metric Search in Distance-Based Learning*.

## Deliverables created in the conversation
- **16-page** revised manuscript, Elsevier `elsarticle` PDF and editable LaTeX source.
- Five-page point-by-point reviewer response for **Reviewers 3, 5, 6 and 8**, plus pasteable reply text. Reviewers 1 and 2 had earlier replies in the platform.
- Flat, independently compiled LaTeX source ZIP containing the three external PNG figures; complete release ZIP includes supplementary evidence scripts, archived outputs, cover letter, highlights and an audit.
- Original public repository `Arithmetic-Power-Geometry/APG-AMS` was read and left unchanged; private revision repository `Arithmetic-Power-Geometry/APG_AMS` used for the review audit.

## Citation and typesetting verification
- Seven tables, four figures, three algorithms: **all have manuscript citations**.
- 27 bibliography items: **all cited**.
- No unresolved LaTeX references or overfull boxes.
- The distributable source ZIP independently builds a 16-page PDF.

## Actual experimental rerun checks
- **P06**: all 108 parameter configurations independently regenerated and summary CSV compared exactly.
- **P18, P19**: both ISOLET and Fashion-MNIST L2, FullP, and 20%-budget screening policy outcomes reproduced from the uploaded dataset ZIPs.
- **P21**: exact JSON regenerated; no certified queries on the two high-dimensional subsets.
- **P20**: rerun did *not* complete before the execution limit. Archived result is retained but **not newly verified**.
- **P22**: archived output and source checked, but not freshly rerun.
- Full original 12-dataset benchmark and grouped Mice Protein source **not independently rerun and verified here**.

## Essential scientific caveats
- 66.47% is saved candidate-exponent evaluations **relative to FullP**, not equivalent elapsed-time speedup.
- P22 33.15–65.55% savings count **Minkowski p-power coordinate terms after a separate Euclidean initialization scan**; this does not prove full-query computational work reduction or speedup.
- Exploratory P18–P20 results reused official test pools during method development; not independent confirmatory replications.
- Grouped Mice Protein 51.67% is provisional, third-party source requires official-source verification.
- No production approximate-nearest-neighbor benchmark or optimized standalone FullP latency test; entropy-specific superiority over low-confidence screening has not been established.

## Release hash
- Complete ZIP SHA-256: `93eac0ec5d61877273cc9bcb9f4b5d698d889554f581fc578c25d55fedcfda15`
- Revised manuscript PDF SHA-256: `9fe4ad1778018ef2abe3f1fe9a81f3e00c2d67d7fe6a70b3f1b30190b0a311a9`

The PDF/ZIP binaries are attached to the current ChatGPT conversation, **not committed as GitHub files**.

## Submission
Editor email of 3 Nov 2026 requests point-by-point responses; revision due **17 Nov 2026**. The peer review platform requires a response to every reviewer comment. Files have been prepared, but no submission action has been performed.
