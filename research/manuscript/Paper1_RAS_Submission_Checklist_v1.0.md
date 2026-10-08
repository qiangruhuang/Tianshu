# Paper 1 — RAS Submission Checklist v1.0

**Primary target:** Robotics and Autonomous Systems  
**Working manuscript:** `Paper1_Manuscript_v0.5_RAS.md`  
**Date:** 2026-10-08

## Research gate

- [x] E0–E5 complete.
- [x] E6b frozen confirmatory gate PASS.
- [x] Mature-planner null retained in main text.
- [x] No new benchmark required by adversarial review.
- [x] Final 2026 literature refresh completed.
- [x] Claim–Evidence–Citation audit completed.
- [x] Evidence boundary explicitly excludes field performance and physical safety.

## Manuscript

- [x] RAS-oriented title.
- [x] Abstract compressed to ~260 words.
- [x] Introduction rewritten around autonomous mission planning.
- [x] E5 consistently classified as public-topology stress test.
- [x] E6b cross-implementation oracle terminology corrected.
- [x] E6b 8.84% external-selectivity limitation stated.
- [x] Fast Downward null integrated into Results, Discussion, and Conclusion.
- [ ] Final full-manuscript copy edit.
- [ ] Check every figure/table callout after layout.
- [ ] Normalize references to the journal's final style at submission stage.

## Figures and tables

- [x] Fig.1 architecture frozen.
- [x] Fig.2 E1 same-cardinality mechanism frozen.
- [x] Fig.3 E5 public-topology reduction frozen.
- [x] Fig.4 E6b native provider admission frozen.
- [x] Fig.5 E6b mature-planner null frozen.
- [x] Reproducible figure generator committed.
- [x] Figure data committed.
- [ ] Final typography sizing check for journal layout.
- [ ] Decide which detailed tables move to Supplement after typesetting.

## Submission materials

- [x] Highlights draft.
- [x] Cover-letter draft.
- [x] Graphical-abstract brief.
- [ ] Confirm current upload requirements in the journal submission portal immediately before submission.
- [ ] Add author names/affiliations and corresponding-author details.
- [ ] Add funding, competing-interest, and author-contribution statements.
- [ ] Finalize data/code availability statement.
- [ ] Add repository release/tag/DOI if created before submission.

## Reproducibility

- [x] Canonical repository: `qiangruhuang/Tianshu`.
- [x] E6b GitHub Actions run: `37713826709`.
- [x] Artifact ID: `11522843338`.
- [x] Frozen benchmark commit recorded.
- [x] Fast Downward version/config recorded.
- [x] VAL commit recorded.
- [x] Result hashes preserved.

## Hard-stop rules

Do not:

- add another benchmark to recover speedup;
- hide the E6b mature-planner null;
- call the cross-implementation oracle independent policy ground truth;
- claim E6b is a high-selectivity external test;
- claim field or physical safety;
- rerun experiments after formatting begins unless a reproducibility error is found.
