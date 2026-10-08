# Tianshu — Governed Semantic Compilation (GSC)

This repository is the maintained research workspace for **Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning**.

## Current status

- E0–E5: **complete**.
- E6a Satellite native-semantics pilot: **complete**; retained transparently as a low-selectivity pilot.
- E6b held-out Rovers p09–p20: **PASS** on the frozen independent external-validity gate.
- Confirmatory execution: GitHub Actions run **37713826709** using Fast Downward 26.6 and VAL commit `3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`.

E6b passed with 12/12 Full-domain tasks and 12/12 GSC tasks solved, zero Full→GSC solvability regressions, zero VAL failures, zero non-admitted-provider exposures, zero independent-oracle mismatches, and exact source/toolchain identity checks.

The mature-planner performance result is a **null**: Full and GSC have identical Fast Downward translator/search statistics and identical final plans on all 12 holdout instances. This narrows the computational claim. GSC is positioned as a governed semantic domain-synthesis boundary; search reduction is conditional on whether mission-irrelevant structure survives downstream planner preprocessing.

## Canonical project files

- [`research/GSC_PROJECT_MASTER.md`](research/GSC_PROJECT_MASTER.md) — single source of truth for research status, claims, experiment state, and changelog.
- [`docs/index.html`](docs/index.html) — maintained browser panorama for collaborators and non-specialists.
- [`research/E6b_Confirmatory_Interpretation_v1.0.md`](research/E6b_Confirmatory_Interpretation_v1.0.md) — scientific interpretation of the confirmatory PASS and mature-planner null.
- [`research/manuscript/Paper1_v0.4_E6b_Integration_Guide.md`](research/manuscript/Paper1_v0.4_E6b_Integration_Guide.md) — manuscript-level integration plan.
- [`e6b/`](e6b/) — frozen E6b protocol, oracle, runner, runbook, execution records, and committed result summaries.

## Maintenance rule

**Project Master Markdown first → HTML second → GitHub synchronization.** Completed experiments are never silently reinterpreted. Frozen protocols receive new version numbers if changed. Scientific PASS/FAIL/INCONCLUSIVE is kept separate from CI/infrastructure failures.

## Current research phase

The external-validity evidence chain for Paper 1 is closed. The next phase is:

**Paper 1 v0.4 full-text integration → Claim–Evidence consistency audit → adversarial reviewer pass → submission-target formatting.**

Do not add another benchmark merely to recover a positive speed effect after the E6b mature-planner null. New experiments should be added only if manuscript review identifies a specific unresolved claim-evidence gap.

## Evidence boundary

All evidence remains software/formal-model, parameterized synthetic, or public planning-benchmark evidence. It does not establish field performance, physical safety, sensing accuracy, engagement effectiveness, command latency, or unrestricted domain generality.
