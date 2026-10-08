# Tianshu — Governed Semantic Compilation (GSC)

This repository is the maintained research workspace for **Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning**.

## Current status — 8 October 2026

Paper 1's **experimental program is closed**. Pre-layout copy-edit and RAS/Elsevier submission-engineering gates have both passed; remaining blockers are author metadata and final portal packaging.

- E0–E5: complete.
- E6a Satellite pilot: complete; retained transparently as a low-selectivity pilot.
- E6b held-out IPC-3 Rovers p09–p20: **PASS** under the frozen confirmatory gate.
- Fast Downward 26.6 + VAL: verified through GitHub Actions run `37713826709`.
- Full-domain evaluable: **12/12**; Full-solved→GSC-unsolved: **0**; GSC VAL failures: **0**; non-admitted-provider exposures: **0**.
- Mature-planner performance result: **null**. Full and GSC have identical effective translated/search problems and identical final plans on all 12 E6b tasks.
- Primary submission target: **Robotics and Autonomous Systems (RAS)**.
- Current authoritative manuscript: **v0.5.3 RAS**.
- Pre-layout copy-edit gate: **PASS**.
- RAS/Elsevier submission-compliance gate: **PASS WITH AUTHOR-METADATA BLOCKERS ONLY**.

Final scientific storyline:

> **correct governed domain synthesis + conditional computational benefit**

GSC is supported as an explicit, auditable, mission-conditioned Provider–Action domain-admission boundary. Search reduction occurs when mission-irrelevant/governance-invalid structure survives downstream planner preprocessing; it is **not** a planner-independent speedup claim.

## Canonical project files

- [`research/GSC_PROJECT_MASTER.md`](research/GSC_PROJECT_MASTER.md) — single source of truth; current version v1.7.2.
- [`docs/index.html`](docs/index.html) — maintained browser-oriented research panorama.
- [`research/manuscript/Paper1_CURRENT_v1.0.md`](research/manuscript/Paper1_CURRENT_v1.0.md) — authoritative manuscript version/hash manifest.
- [`research/manuscript/Paper1_v0.5.3_Copyedit_Delta.md`](research/manuscript/Paper1_v0.5.3_Copyedit_Delta.md) — final pre-layout copy-edit delta.
- [`research/manuscript/Paper1_RAS_Copyedit_Gate_v1.0.md`](research/manuscript/Paper1_RAS_Copyedit_Gate_v1.0.md) — copy-edit gate.
- [`research/manuscript/Paper1_RAS_Submission_Compliance_Gate_v1.0.md`](research/manuscript/Paper1_RAS_Submission_Compliance_Gate_v1.0.md) — current RAS/Elsevier format gate.
- [`research/manuscript/Paper1_Data_Code_Availability_v1.0.md`](research/manuscript/Paper1_Data_Code_Availability_v1.0.md) — data/code statement.
- [`research/manuscript/Paper1_RAS_Submission_Metadata_v1.0.md`](research/manuscript/Paper1_RAS_Submission_Metadata_v1.0.md) — abstract/keywords/highlights package.
- [`research/manuscript/Paper1_RAS_Submission_Checklist_v1.1.md`](research/manuscript/Paper1_RAS_Submission_Checklist_v1.1.md) — current checklist.
- [`research/manuscript/Paper1_Claim_Evidence_Citation_Audit_v1.0.md`](research/manuscript/Paper1_Claim_Evidence_Citation_Audit_v1.0.md) — claim/evidence/citation audit.
- [`research/figures/generate_paper_figures_v1_2.py`](research/figures/generate_paper_figures_v1_2.py) — reproducible PNG/PDF/EPS main-figure generator.
- [`e6b/results/run-37713826709/`](e6b/results/run-37713826709/) — primary committed confirmatory result summaries.

The complete current manuscript is maintained in the project Library at:

`/Tianshu/manuscript/Paper1_Manuscript_v0.5.3_RAS.md`

SHA-256:

`3fa988a466c38f716c7ade29f1ecea01c9710a897b073b92831df4888e095f2f`

## E6b confirmatory identity

- benchmark: `aibasel/downward-benchmarks@e21d49c2cb61d147a46c5966f2581bf6fd422b9f`
- Fast Downward: `26.6`, `--alias lama-first`, 300 s / 4 GiB
- VAL: `3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`
- GitHub Actions run: `37713826709`
- artifact ID: `11522843338`
- artifact ZIP SHA-256: `36fc77b08100eb655ab575c8ca1c70f6a349f373cf19d38994b6bfb9b814d5a8`

## Current submission package

Completed:

- v0.5.3 RAS pre-layout manuscript candidate;
- 236-word standalone abstract;
- seven keywords;
- five Highlights, each within Elsevier's general 85-character guidance;
- five frozen main figures;
- PNG previews plus PDF/EPS vector submission sources;
- render-back visual verification of all five PDF figures;
- final 2026 literature refresh;
- Claim–Evidence–Citation audit;
- adversarial review;
- terminology/logic audit;
- pre-layout copy-edit gate;
- Data/Code Availability statement;
- cover-letter draft;
- graphical-abstract brief;
- RAS/Elsevier submission-compliance gate;
- submission checklist v1.1.

Remaining work is author/submission metadata only:

1. author order and affiliations;
2. corresponding-author details;
3. funding/grant statement;
4. CRediT contributions;
5. competing-interest declaration;
6. acknowledgements if applicable;
7. optional repository release/DOI decision;
8. final live RAS portal requirement check;
9. DOCX/PDF manuscript generation only after explicit content approval.

A new experiment is justified only if a later reviewer identifies a concrete claim that cannot be supported or removed using the existing evidence.

## Evidence boundary

All completed results are software/formal-model, parameterized synthetic, or public planning-benchmark evidence. They do not establish field performance, physical safety, sensing accuracy, engagement effectiveness, communication latency, or unrestricted domain generality.
