# Paper 1 — RAS Submission Metadata v1.0

**Journal:** Robotics and Autonomous Systems  
**Prepared:** 2026-10-08  
**Scientific state:** E0–E5 complete; E6b PASS; experimental program closed.

## Title

Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning

## Abstract

Persistent semantic models let autonomous mission systems reuse knowledge about capabilities, providers, actions, and policies, but not every known action is admissible for the current mission. We introduce **Governed Semantic Compilation (GSC)**, a mission-conditioned boundary that materializes a versioned closed-world Mission Snapshot, checks readiness, and compiles global action templates into a planning-admissible Provider–Action domain with rejection provenance and snapshot binding. Authorization-dependent actions remain explicit planning preconditions, while post-plan validation blocks plans that no longer match current state.

We evaluate GSC as a domain-membership mechanism rather than a new planner. In a 12,600-evaluation controlled benchmark, GSC exactly matches generator-owned eligibility labels. At N=640 and eligibility density ρ=0.05, blind search solves 30/30 GSC instances versus 20/30 with a same-cardinality core-preserving random control and 0/30 with state-aware or full domains; under A*, median generated nodes are 4, 31, 308, and 612.

A frozen external-validity gate then uses held-out IPC-3 Rovers p09–p20, native public semantics, a separate admission implementation, Fast Downward 26.6, and VAL. All 12 Full and 12 GSC tasks solve; no Full-solved instance becomes GSC-unsolved, every GSC plan validates against the original public PDDL, and no plan uses a non-admitted provider. Fast Downward nevertheless reduces Full and GSC to identical effective search problems on all 12 tasks. GSC therefore provides correct, auditable, mission-conditioned domain synthesis; search reduction is conditional on whether irrelevant structure survives downstream planner preprocessing.

**Word count:** 235.

## Keywords

1. ontology-mediated planning
2. semantic compilation
3. autonomous mission planning
4. runtime governance
5. plan validation
6. capability-based systems
7. domain synthesis

## Highlights

- Mission-conditioned compilation governs which provider actions enter planning.
- Same-size controls show semantic selection matters beyond reducing domain size.
- Held-out Rovers tasks preserve solvability and pass separate plan validation.
- A mature planner removes the same irrelevant structure in the holdout.
- Search benefits depend on whether irrelevant structure survives preprocessing.

All five highlights are <=85 characters including spaces.

## Data/code statement

Use `Paper1_Data_Code_Availability_v1.0.md`.

## Evidence boundary for submission forms

All reported evidence is software/formal-model, parameterized synthetic, or public planning-benchmark evidence. The study does not establish field performance, physical safety, sensing accuracy, engagement effectiveness, communication latency, or unrestricted domain generality.

## Items requiring author input before submission

- author names and order;
- affiliations;
- corresponding-author email;
- funding sources/grant numbers;
- CRediT author contributions;
- competing-interest declaration;
- optional acknowledgements;
- whether a repository release/DOI will be minted before submission.
