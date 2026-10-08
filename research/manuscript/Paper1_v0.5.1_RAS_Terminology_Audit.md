# Paper 1 v0.5.1 — RAS Terminology Audit

**Date:** 2026-10-08  
**Complete manuscript:** project Library `/Tianshu/manuscript/Paper1_Manuscript_v0.5.1_RAS.md`

This revision changes terminology only; no method, experiment, result, threshold, or claim changes.

## Corrections

1. Prespecified E6b gate wording changed from `independent-oracle mismatch = 0` to **`cross-implementation oracle mismatch = 0`**.
2. Discussion wording changed from `provider-exposure criterion` to **`non-admitted-provider criterion`**.
3. Admission-oracle language is kept consistent with the actual design: the JavaScript and Python paths are independently implemented, but both instantiate the same frozen study-defined adapter rule over externally authored PDDL semantics.

## Language consistency

The working manuscript is internally consistent with American-English technical spelling in the checked high-frequency terms (`behavior`, `authorization`, `organization`, `optimization`). No mixed British/American spelling pattern requiring a global conversion was detected.

## Logic review

A deterministic paragraph-logic review found:

- Abstract/Introduction: one short-paragraph warning corresponding to the contributions transition; no substantive logic defect.
- Discussion/Conclusion: no paragraph-logic issues.

The experimental gate remains closed and no new benchmark is justified by this audit.