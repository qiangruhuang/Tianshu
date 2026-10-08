# Tianshu — Governed Semantic Compilation (GSC)

This repository is the maintained research workspace for **Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning**.

## Current status

- E0–E5: completed.
- E6a Satellite native-semantics pilot: completed; retained as a low-selectivity pilot.
- E6b Rovers p09–p20: frozen protocol, static audit, cross-implementation oracle agreement, and fail-closed checks completed.
- E6b Fast Downward 26.6 + VAL confirmatory planner execution: **pending**. A first attempt in the ChatGPT sandbox was blocked before any planner outcome was opened because the required toolchain was unavailable and outbound network access was disabled.

## Canonical project files

- [`research/GSC_PROJECT_MASTER.md`](research/GSC_PROJECT_MASTER.md) — single source of truth for research state, claims, experiment status, and changelog.
- [`docs/index.html`](docs/index.html) — browser-oriented research panorama for collaborators and non-specialists.
- [`e6b/`](e6b/) — frozen E6b protocol, oracle, runner, runbook, and execution records.

## Maintenance rule

**Update the project Master Markdown first, then synchronize the HTML.** Completed experiments are never silently reinterpreted; frozen protocols receive new version numbers if they are changed. Planner outcomes may not be used to tune the E6b corpus, admission rule, resource caps, or PASS criteria.

## Next confirmatory action

Run the frozen E6b Full/GSC pairs with **Fast Downward 26.6 (`--alias lama-first`, 300 s, 4 GiB)** and validate every returned GSC plan against the original public PDDL with **VAL commit `3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`**.

The GitHub Actions workflow in `.github/workflows/e6b-confirmatory.yml` is designed to execute this frozen gate in a network-enabled Linux environment and preserve the raw outputs.

## Evidence boundary

All completed results are software/formal-model or parameterized synthetic evidence. They do not establish field performance, physical safety, sensing accuracy, engagement effectiveness, or unrestricted domain generality.
