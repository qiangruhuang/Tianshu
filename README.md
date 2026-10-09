# Tianshu — Governed Semantic Compilation (GSC)

This repository is the maintained research workspace for **Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning**.

## Current status — 9 October 2026

Paper 1's **experimental program and reproducibility package are closed**. The current pre-submission candidate is **v0.6.0 RAS (anti-defensive + Nature-style rewrite)**. Remaining work requires human author metadata and final submission decisions rather than additional experiments.

- E0–E5: complete.
- E6a Satellite pilot: complete; retained transparently as a low-selectivity pilot.
- E6b held-out IPC-3 Rovers p09–p20: **PASS** under the frozen confirmatory gate.
- Fast Downward 26.6 + VAL: verified through GitHub Actions run `37713826709`.
- Full-domain evaluable: **12/12**; Full-solved→GSC-unsolved: **0**; GSC VAL failures: **0**; non-admitted-provider exposures: **0**.
- Mature-planner result: **null**. Full and GSC have identical effective translated/search problems and identical final plans on all 12 E6b tasks.
- Primary submission target: **Robotics and Autonomous Systems (RAS)**.
- Current manuscript: **Paper1_Manuscript_v0.6.0_RAS_AntiDefensive_Nature.md**.
- Supplementary/reproducibility appendix: complete.
- Elsevier generative-AI disclosure: included in the candidate manuscript.
- Submission-compliance gate: **PASS WITH HUMAN-METADATA BLOCKERS ONLY**.
- Writing/narrative gate: **PASS** after anti-defensive-writing + Nature-style restructuring and polishing; scientific-change status = NONE.

Final scientific storyline:

> **correct governed domain synthesis + conditional computational benefit**

GSC is supported as an explicit, auditable, mission-conditioned Provider–Action domain-admission boundary. Search reduction occurs when mission-irrelevant/governance-invalid structure survives downstream planner preprocessing; it is **not** a planner-independent speedup claim.

## Canonical project files

- [`research/GSC_PROJECT_MASTER.md`](research/GSC_PROJECT_MASTER.md) — single source of truth; v1.9.
- [`docs/index.html`](docs/index.html) — maintained browser-oriented research panorama.
- [`research/manuscript/Paper1_CURRENT_v1.2.md`](research/manuscript/Paper1_CURRENT_v1.2.md) — authoritative manuscript version/hash manifest.
- [`research/manuscript/Paper1_Manuscript_v0.6.0_RAS_AntiDefensive_Nature.md`](research/manuscript/Paper1_Manuscript_v0.6.0_RAS_AntiDefensive_Nature.md) — current full manuscript.
- [`research/manuscript/Paper1_v0.6.0_AntiDefensive_Nature_Rewrite_Audit.md`](research/manuscript/Paper1_v0.6.0_AntiDefensive_Nature_Rewrite_Audit.md) — writing-restructure and scientific-regression audit.
- [`research/manuscript/Paper1_Supplementary_Material_v1.0.md`](research/manuscript/Paper1_Supplementary_Material_v1.0.md) — supplementary evidence and E6b per-instance paired results.
- [`research/manuscript/Paper1_RAS_Declarations_Author_Metadata_v1.0.md`](research/manuscript/Paper1_RAS_Declarations_Author_Metadata_v1.0.md) — author/CRediT/funding/COI/AI-disclosure sign-off packet.
- [`research/manuscript/Paper1_PreSubmission_Release_Manifest_v1.0.md`](research/manuscript/Paper1_PreSubmission_Release_Manifest_v1.0.md) — candidate immutable-release manifest.
- [`research/figures/generate_paper_figures_v1_2.py`](research/figures/generate_paper_figures_v1_2.py) — reproducible PNG/PDF/EPS figure generator.
- [`e6b/results/run-37713826709/`](e6b/results/run-37713826709/) — frozen confirmatory summaries.

Current manuscript SHA-256:

`7d20b5f09a0f335834fb1a2fcc92460de7f13a789ce796f5ba6c13bf6dee2298`

## Remaining submission decisions

1. author order and affiliations;
2. corresponding-author details;
3. funding/grant statement;
4. CRediT contributions;
5. competing-interest declaration;
6. optional acknowledgements;
7. all authors approve the generative-AI declaration;
8. decide whether to mint an immutable repository release/DOI;
9. final live RAS portal check;
10. explicit manuscript-content approval before DOCX/PDF generation.

No additional benchmark should be added merely to recover a positive speedup.

## Evidence boundary

All completed results are software/formal-model, parameterized synthetic, or public planning-benchmark evidence. They do not establish field performance, physical safety, sensing accuracy, engagement effectiveness, communication latency, or unrestricted domain generality.
