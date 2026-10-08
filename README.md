# Tianshu — Governed Semantic Compilation (GSC)

This repository is the maintained research workspace for **Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning**.

## Current status — 8 October 2026

Paper 1's **experimental program is closed** and the project has entered journal-submission consolidation.

- E0–E5: complete.
- E6a Satellite pilot: complete; retained transparently as a low-selectivity pilot.
- E6b held-out IPC-3 Rovers p09–p20: **PASS** under the frozen confirmatory gate.
- Fast Downward 26.6 + VAL: verified through GitHub Actions run `37713826709`.
- Full-domain evaluable: **12/12**; Full-solved→GSC-unsolved: **0**; GSC VAL failures: **0**; non-admitted-provider exposures: **0**.
- Mature-planner performance result: **null**. Full and GSC have identical effective translated/search problems and identical final plans on all 12 E6b tasks.
- Primary submission target: **Robotics and Autonomous Systems (RAS)**.
- Current manuscript: **v0.5.1 RAS**, with terminology/logic audit complete.

Final scientific storyline:

> **correct governed domain synthesis + conditional computational benefit**

GSC is supported as an explicit, auditable, mission-conditioned Provider–Action domain-admission boundary. Search reduction occurs when mission-irrelevant/governance-invalid structure survives downstream planner preprocessing; it is **not** a planner-independent speedup claim.

## Canonical project files

- [`research/GSC_PROJECT_MASTER.md`](research/GSC_PROJECT_MASTER.md) — single source of truth.
- [`docs/index.html`](docs/index.html) — maintained browser-oriented research panorama.
- [`research/E6b_Confirmatory_Interpretation_v1.0.md`](research/E6b_Confirmatory_Interpretation_v1.0.md) — scientific interpretation of E6b.
- [`research/manuscript/Paper1_Manuscript_v0.4.md`](research/manuscript/Paper1_Manuscript_v0.4.md) — last complete full manuscript committed directly to GitHub.
- [`research/manuscript/Paper1_v0.5_RAS_Submission_Delta.md`](research/manuscript/Paper1_v0.5_RAS_Submission_Delta.md) — RAS-oriented manuscript delta.
- [`research/manuscript/Paper1_v0.5.1_RAS_Terminology_Audit.md`](research/manuscript/Paper1_v0.5.1_RAS_Terminology_Audit.md) — final terminology/logic audit.
- [`research/manuscript/Paper1_Target_Venue_Decision_v1.0.md`](research/manuscript/Paper1_Target_Venue_Decision_v1.0.md) — venue decision.
- [`research/manuscript/Paper1_Claim_Evidence_Citation_Audit_v1.0.md`](research/manuscript/Paper1_Claim_Evidence_Citation_Audit_v1.0.md) — claim/evidence/citation audit.
- [`research/figures/Paper1_Figure_Table_Package_v1.0.md`](research/figures/Paper1_Figure_Table_Package_v1.0.md) — submission figure/table plan.
- [`research/figures/generate_paper_figures.py`](research/figures/generate_paper_figures.py) — reproducible figure generator.
- [`e6b/results/run-37713826709/`](e6b/results/run-37713826709/) — primary committed confirmatory result summaries.

The complete current manuscript `Paper1_Manuscript_v0.5.1_RAS.md` and rendered figure package are also maintained in the project Library.

## E6b confirmatory identity

- benchmark: `aibasel/downward-benchmarks@e21d49c2cb61d147a46c5966f2581bf6fd422b9f`
- Fast Downward: `26.6`, `--alias lama-first`, 300 s / 4 GiB
- VAL: `3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`
- GitHub Actions run: `37713826709`
- artifact ID: `11522843338`
- artifact ZIP SHA-256: `36fc77b08100eb655ab575c8ca1c70f6a349f373cf19d38994b6bfb9b814d5a8`

## Current submission package

Completed:

- RAS-oriented ~260-word abstract;
- RAS-oriented Introduction;
- five frozen main figures and reproducible generation script;
- final 2026 literature refresh;
- Claim–Evidence–Citation audit;
- terminology/logic audit;
- Highlights draft;
- cover-letter draft;
- graphical-abstract brief;
- submission checklist.

Remaining work is presentation/metadata only:

1. final full-manuscript copy edit;
2. final figure typography/layout check;
3. normalize references against the current RAS submission portal/Guide;
4. add authors, affiliations, funding, COI, and CRediT;
5. generate DOCX/PDF only after explicit manuscript-content approval.

A new experiment is justified only if a later reviewer identifies a concrete claim that cannot be supported or removed using the existing evidence.

## Evidence boundary

All completed results are software/formal-model, parameterized synthetic, or public planning-benchmark evidence. They do not establish field performance, physical safety, sensing accuracy, engagement effectiveness, communication latency, or unrestricted domain generality.