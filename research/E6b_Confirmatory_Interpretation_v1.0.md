# E6b Confirmatory Interpretation v1.0

**Project:** Tianshu / Governed Semantic Compilation (GSC)  
**Date:** 2026-10-08  
**Frozen confirmatory run:** GitHub Actions `37713826709`  
**Scientific status:** **PASS**

## 1. Purpose

This note records the post-execution scientific interpretation of the frozen E6b external-validity gate. It does not modify the frozen protocol, corpus, admission rule, planner configuration, resource limits, validator commit, or PASS criteria.

The main reason for this note is that E6b produced two simultaneous findings that must be represented together:

1. a strong positive external-validity result for semantic correctness, solvability preservation, provider-exposure safety, and independent planner/validator execution; and
2. a clean null result for search reduction under Fast Downward 26.6 on the frozen Rovers holdout.

The second result narrows the computational claim but strengthens the paper by preventing an unjustified universal speedup interpretation.

---

## 2. Frozen gate result

The frozen `gate_summary.json` reports:

- source identity mismatches: **0**;
- admission serialization mismatches: **0**;
- independent-oracle mismatches: **0**;
- uncovered native goals: **0**;
- Fast Downward 26.6 identity verified: **true**;
- VAL source commit verified: **true**;
- Full-domain evaluable: **12/12**;
- Full-solved → GSC-unsolved regressions: **0**;
- GSC VAL failures: **0**;
- non-admitted-provider action exposures: **0**.

The frozen minimum was 10/12 Full-domain evaluable tasks. E6b therefore **passes every prespecified gate condition**.

All 12 GSC plans validate with VAL against the original unmodified public PDDL.

---

## 3. Native-semantic selectivity

Across Rovers p09–p20, the native-semantic admission rule retained:

- rovers: **58/58**;
- cameras: **60/65**;
- stores: **47/58**.

In total, 165/181 provider-related objects were admitted and **16/181 (8.84%) were excluded**.

All 136 native mission-output goals retained at least one valid witness.

This establishes non-zero semantic selectivity without study-authored runtime masks.

---

## 4. Mature-planner null effect

Despite excluding 5 cameras and 11 stores, Full and GSC become the same effective planning problem under Fast Downward 26.6 on every frozen holdout instance.

Independent post-run audit of the raw Fast Downward logs shows equality in **12/12 pairs** for:

- translator variables;
- translator facts;
- translator operators;
- translator task size;
- relevant atoms;
- necessary variables;
- necessary operators;
- landmark counts;
- expanded states;
- generated states;
- plan length;
- final `sas_plan` SHA-256.

Paired performance summary:

- median generated states: Full = GSC = **4,863.5**;
- median expanded states: Full = GSC = **145**;
- median plan length: Full = GSC = **45**;
- median wall time: Full **0.127506 s**, GSC **0.124590 s**;
- GSC faster in wall time: **6/12**;
- GSC slower in wall time: **6/12**;
- median paired wall-time difference (GSC − Full): approximately **−0.00068 s**.

The wall-time differences are therefore consistent with runtime noise rather than a stable performance effect.

---

## 5. Mechanistic interpretation

The E6b null is consistent with the following mechanism:

> GSC excludes provider objects that are semantically irrelevant to the mission goals, but Fast Downward's own translation/relevance preprocessing independently removes the corresponding irrelevant planning structure before search.

Under this regime, GSC and Full converge **after translation**, even though the pre-planning semantic admission sets differ.

This explains why E5 and E6b are not contradictory:

- **E5:** governance-invalid alternatives survived into the clean-room planner's effective search space, so semantic admission reduced generated nodes by 38.5–66.7% at q=0.
- **E6b:** Fast Downward preprocessing removed the same class of irrelevant alternatives before search, so GSC produced no additional search reduction.

The computational benefit is therefore **planner- and topology-conditional**, while the governance/semantic correctness benefit remains directly observable.

---

## 6. Revised claim hierarchy

### Primary claim — strengthened

GSC provides an explicit, auditable, mission-conditioned domain-admission boundary that preserves native-task solvability and plan validity under independent public semantics, an established third-party planner, and an independent validator.

### Secondary claim — retained but conditioned

Semantic domain admission can reduce search pollution when governance-invalid or mission-irrelevant alternatives survive the downstream planner's own preprocessing.

### Claim that should be removed

GSC should **not** be presented as a generally faster planner interface or as guaranteeing a search-space reduction under mature planners.

---

## 7. Consequences for manuscript structure

The paper should use E1/E5 and E6b for different evidentiary roles:

- **E1:** causal mechanism and same-cardinality falsification;
- **E3:** load-bearing governance components;
- **E4:** configuration-level portability;
- **E5:** evidence that search-pollution reduction can persist on public planning topology when irrelevant alternatives remain in the search representation;
- **E6b:** independent semantic correctness, solvability preservation, external planner/validator replication, and the boundary condition that mature preprocessing may absorb the computational benefit.

The paper's central story is therefore **governed domain synthesis**, not planner acceleration.

---

## 8. Research decision

**Do not add another benchmark solely to recover a speedup.**

The external-validity question posed by the frozen E6b protocol is closed. Adding a new benchmark after observing the mature-planner null would risk turning the study into post-hoc search for a positive performance effect.

The appropriate next phase is manuscript-level adversarial review:

1. integrate E6b into Methods and Results;
2. revise the Abstract and Introduction so search reduction is conditional rather than universal;
3. make the mature-planner null explicit in Results and Discussion;
4. distinguish semantic external validity from field validation;
5. audit every performance sentence against E1/E5/E6b evidence.

No additional experiment should be added unless that review identifies a specific unresolved claim-evidence gap unrelated to recovering a preferred effect direction.
