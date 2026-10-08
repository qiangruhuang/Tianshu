# Tianshu — Governed Semantic Compilation (GSC)

This repository is the maintained research workspace for **Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning**.

## Current status — 8 October 2026

The experimental program for Paper 1 is **closed**.

- E0–E5: complete.
- E6a Satellite native-semantics pilot: complete; retained transparently as a low-selectivity pilot.
- E6b held-out IPC-3 Rovers p09–p20: **PASS** under the frozen confirmatory gate.
- Fast Downward 26.6 + VAL: independently verified through GitHub Actions run `37713826709`.
- Full-domain evaluable: **12/12**; Full-solved→GSC-unsolved: **0**; GSC VAL failures: **0**; non-admitted-provider exposures: **0**.
- Mature-planner performance result: **null**. Full and GSC have identical translated/search problems and identical final plans on all 12 E6b tasks.

The final scientific storyline is therefore:

> **correct governed domain synthesis + conditional computational benefit**

GSC is supported as an explicit, auditable, mission-conditioned Provider–Action domain-admission boundary. Search reduction occurs when mission-irrelevant/governance-invalid structure survives downstream planner preprocessing; it is **not** a planner-independent speedup claim.

## Canonical project files

- [`research/GSC_PROJECT_MASTER.md`](research/GSC_PROJECT_MASTER.md) — single source of truth.
- [`docs/index.html`](docs/index.html) — maintained browser-oriented research panorama.
- [`research/E6b_Confirmatory_Interpretation_v1.0.md`](research/E6b_Confirmatory_Interpretation_v1.0.md) — scientific interpretation of the frozen confirmatory result.
- [`research/manuscript/Paper1_Manuscript_v0.4.md`](research/manuscript/Paper1_Manuscript_v0.4.md) — last complete manuscript committed to GitHub.
- [`research/manuscript/Paper1_v0.4.1_Delta.md`](research/manuscript/Paper1_v0.4.1_Delta.md) — post-E6b manuscript corrections.
- `research/manuscript/Paper1_v0.4.2_Literature_Citation_Delta.md` — final 2026 literature refresh.
- `research/manuscript/Paper1_Claim_Evidence_Citation_Audit_v1.0.md` — sentence-level claim/evidence/citation audit.
- `research/figures/Paper1_Figure_Table_Package_v1.0.md` — submission figure/table plan.
- [`e6b/results/run-37713826709/`](e6b/results/run-37713826709/) — primary committed confirmatory result summaries.

## E6b confirmatory identity

- benchmark: `aibasel/downward-benchmarks@e21d49c2cb61d147a46c5966f2581bf6fd422b9f`
- Fast Downward: `26.6`, `--alias lama-first`, 300 s / 4 GiB
- VAL: `3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`
- GitHub Actions run: `37713826709`
- artifact ID: `11522843338`
- artifact ZIP SHA-256: `36fc77b08100eb655ab575c8ca1c70f6a349f373cf19d38994b6bfb9b814d5a8`

## Current manuscript phase

No additional benchmark is planned. The remaining work is:

1. publication-quality figures/tables from existing evidence;
2. sentence-level Claim–Evidence–Citation audit;
3. target-venue formatting and language editing;
4. DOCX/PDF only after explicit manuscript-content approval.

A new experiment is justified only if a later reviewer identifies a concrete claim that cannot be supported or removed using the existing evidence.

## Evidence boundary

All completed results are software/formal-model, parameterized synthetic, or public planning-benchmark evidence. They do not establish field performance, physical safety, sensing accuracy, engagement effectiveness, communication latency, or unrestricted domain generality.