# Paper 1 — Focused Novelty Refresh (2026-10-08)

**Purpose:** re-run the manuscript hard-stop check before freezing the v0.4.x storyline. This is a targeted prior-art refresh, not an expansion of the literature review.

## Hard-stop question

Has recent work already jointly established the specific contribution claimed by GSC:

1. mission-conditioned synthesis of a heterogeneous Provider–Action planning domain from current provider/capability/state/policy information;
2. Provider–Action **domain membership itself** as a first-class governance object;
3. direct evaluation of membership with cardinality-matched controls rather than only downstream task success; and
4. a held-out native-semantic planning/validation gate?

## Result

**Hard stop not triggered.**

The closest planning neighbors remain:

- John & Koopmann: ontology-mediated planning / OWL-DL planning rewriting;
- Borgwardt et al.: planning with ontologies under coherence-update semantics;
- Köcher et al.: semantic capability models to solver-ready planning formulations;
- Ligneul et al. (ADAMAS): ontology + automated mission planning, monitoring, and replanning;
- Holmberg, Ioup & Abdelguerfi: a knowledge-graph translation layer producing mission-aware planner inputs;
- KGLAMP: dynamic KG-guided heterogeneous multi-robot PDDL/problem generation and replanning;
- Platform-Aware Mission Planning: mission planning coupled to safety/executability verification.

These works substantially constrain what GSC can claim. The paper must not claim novelty for ontology–planning integration, semantic planner-input generation, runtime replanning, or plan validation in isolation.

## Recent governance neighbors

Recent 2026 governance/agent-runtime work also sharpens the boundary:

- **PlanFence**, arXiv:2609.03340v2, focuses on derivation currency and dependency-scoped validation before protected actions.
- **ATR**, arXiv:2609.08015, separates version conflicts from decision conflicts and selectively revalidates affected conditions.
- **Cognitive Admission Control**, arXiv:2609.16313, maps consequential actions to assurance obligations and dispatch-time guards.
- **AID-Guard**, arXiv:2608.21159, addresses stateful authorization-to-effect closure across commit, retry, and recovery.
- **LATTICE** presents a governance-first architecture for authorized autonomous AI operations.

These are important conceptual neighbors for authorization/admission/freshness, but they do not construct and directly evaluate a classical mission-specific Provider–Action planning domain in the manner studied here.

## Frozen novelty framing

The defensible contribution is:

> **GSC makes mission-conditioned Provider–Action membership an explicit, version-bound, auditable artifact between persistent semantic knowledge and a downstream planner, and evaluates that domain membership directly.**

Supporting novelty comes from the evaluation design:

- eligibility density;
- independent generator labels in the controlled study;
- same-cardinality and core-preserving controls;
- component ablations;
- configuration-only transfer;
- public-topology stress test;
- held-out native-semantic external gate with cross-implementation adapter, Fast Downward, and VAL.

## Claims that remain prohibited

Do not claim that GSC is:

- the first ontology-planning system;
- the first semantic compiler for planning;
- the first runtime admission mechanism;
- the first stale-plan validator;
- a generally faster planner interface;
- independently validated for field safety/authorization policy.

## Research decision

No new experiment or reframing is required by this literature refresh. Continue with manuscript consolidation and citation-level review.
