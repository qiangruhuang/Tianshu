# Paper 1 v0.4 — E6b Integration Guide

**Manuscript:** *Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning*  
**Purpose:** integrate the completed E6b external-validity gate without overstating the mature-planner performance result.  
**Date:** 2026-10-08

## 1. Editorial decision

Paper 1 should now close the experimental program and move to claim consolidation.

The recommended top-level story is:

> Persistent semantic knowledge should not be passed directly to a planner as if all known providers/actions were currently admissible. GSC makes mission-conditioned Provider–Action membership explicit, version-bound, auditable, and testable. Controlled experiments show that semantic admission can reduce search pollution when invalid alternatives survive into search. A frozen external holdout then shows that the same admission rule preserves native public-task solvability and plan validity under Fast Downward 26.6 and VAL, while also showing that mature planner preprocessing can absorb the search-reduction benefit.

This story is stronger than a generic speedup claim because it is supported by both positive and null evidence.

---

# 2. Title

The current title remains suitable:

**Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning**

Do not add “efficient”, “accelerated”, or similar performance language to the title.

---

# 3. Abstract — required change

## Recommended structure

1. Problem: persistent semantics and executable planning domains operate under different runtime assumptions.
2. Method: versioned Mission Snapshot + Readiness + governed Provider–Action compilation + provenance + post-plan validation.
3. Controlled evidence: E1 mechanism benchmark and same-cardinality control.
4. External evidence: E6b PASS on held-out IPC-3 Rovers p09–p20 with independent oracle, Fast Downward 26.6, and VAL.
5. Boundary condition: mature planner preprocessing eliminates the E6b search difference.
6. Claim: governed domain synthesis is validated; computational benefit is conditional.

## Candidate abstract result paragraph

In a 12,600-evaluation controlled benchmark, GSC exactly matched generator-owned eligibility labels and, at the hardest low-density setting, solved 30/30 blind-search instances versus 20/30 for a same-cardinality core-preserving random control and 0/30 for state-aware or full domains. Component ablations isolated the roles of Readiness, compile-time safety admission, snapshot freshness, post-plan validation, and rejection provenance, while an unchanged runtime core transferred to a five-phase SAR/inspection configuration. We then froze an independent external-validity gate on held-out IPC-3 Rovers p09–p20: source identities, a separately implemented JavaScript admission oracle, Fast Downward 26.6, and VAL were fixed before planner outcomes. All 12 Full and 12 GSC tasks solved within the resource cap, every GSC plan validated against the original public PDDL, and no non-admitted provider appeared in a returned plan. However, Fast Downward translated Full and GSC to identical effective search problems on all 12 tasks, yielding identical expansions, generated states, plan lengths, and plans. These results support governed semantic domain synthesis as an explicit correctness and auditability boundary; search reduction is a conditional benefit rather than a planner-independent guarantee.

Avoid compressing the E6b null into “no performance loss.” The stronger and more informative statement is that mature preprocessing made the effective search problems identical.

---

# 4. Introduction — contribution bullets

The contribution list should contain three primary claims.

### Contribution 1 — runtime domain-admission boundary

We formalize and implement a mission-conditioned semantic compilation boundary that converts a persistent semantic model plus a versioned closed-world Mission Snapshot into a planning-admissible Provider–Action domain, with explicit rejection provenance and state binding.

### Contribution 2 — mechanism-aware evaluation

We evaluate domain membership directly using eligibility density, generator-owned labels, same-cardinality controls, and component ablations, separating semantic action selection from the trivial effect of reducing action count.

### Contribution 3 — bounded external validation

We show that the frozen admission rule preserves native public-task solvability and returned-plan validity on held-out IPC-3 Rovers instances under an independently implemented oracle, Fast Downward 26.6, and VAL. The same experiment provides a boundary condition: Fast Downward preprocessing collapses Full and GSC to identical effective search problems, so computational benefit cannot be claimed as planner-independent.

Do not describe freshness checking itself as a standalone novelty.

---

# 5. Methods — new E6b subsection

## Suggested heading

**5.8 E6b: independent external-validity gate using native Rovers semantics**

## Required content

State explicitly:

- holdout corpus: IPC-3 Rovers p09–p20;
- E5 used only p03/p05/p07;
- benchmark repository commit and frozen problem/domain blob identities;
- no study-authored governance mask in E6b;
- native PDDL facts used for admission;
- independent JavaScript S-expression oracle separated from the Python compiler path;
- Fast Downward 26.6 with `lama-first`, 300 s, 4 GiB;
- VAL frozen to commit `3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`;
- VAL checks returned GSC plans against original unmodified PDDL;
- PASS criteria were frozen before planner outcomes;
- performance endpoints were secondary and not required for PASS.

## Important terminology

Use:

> independently authored executable capability/state semantics

Do not use:

> independently authored safety labels

The IPC benchmark contains planning-domain facts, not real operational authorization labels.

---

# 6. Results — E6b subsection

## Suggested heading

**6.7 E6b passes the frozen external-validity gate but yields a mature-planner performance null**

## Recommended Results text

The frozen E6b gate passed all prespecified criteria. Source file identities matched the frozen IPC-3 Rovers corpus, the independently implemented JavaScript oracle produced zero admission mismatches relative to the compiler, and all 136 native mission-output goals retained at least one admissible witness. Across p09–p20, the admission rule retained 58/58 rovers, 60/65 cameras, and 47/58 stores. Fast Downward 26.6 solved all 12 Full-domain and all 12 GSC instances within the fixed 300-s/4-GiB cap. No Full-solved instance became unsolved under GSC, all 12 returned GSC plans passed VAL against the original unmodified public PDDL, and no returned plan referenced a non-admitted provider. E6b therefore passed the independent external-validity gate.

The external execution did not reproduce the search reduction observed in E1 and E5. Full and GSC had identical translator variables, facts, operators, relevant atoms, landmark counts, expanded states, generated states, plan lengths, and final plan bytes on all 12 holdout instances. Median generated states were 4,863.5 in both conditions, median expanded states were 145 in both, and median plan length was 45 in both. Median wall time was 0.1275 s for Full and 0.1246 s for GSC, with GSC faster in six instances and slower in six. Inspection of the translation logs indicates that Fast Downward's relevance/translation preprocessing removes the excluded cameras and stores from the effective planning problem even in the Full condition. The E6b result therefore supports semantic soundness and solvability preservation under an established planner while identifying a boundary condition for the computational claim.

## Main table

Add a compact E6b gate table rather than a large per-instance performance table.

| Frozen criterion | Result |
|---|---:|
| Source identity mismatches | 0 |
| Independent-oracle mismatches | 0 |
| Uncovered native goals | 0 |
| Full evaluable | 12/12 |
| Full-solved → GSC-unsolved | 0 |
| GSC VAL failures | 0 |
| Non-admitted-provider exposure | 0 |
| Gate status | PASS |

A supplementary per-instance table can contain wall time, expansions, generated states, plan length, and admitted/total providers.

---

# 7. Discussion — interpretation change

## 7.1 Main interpretation

Do not combine E5 and E6b into one generic “external speedup” result.

Recommended distinction:

- E5 shows that semantic admission can reduce search pollution on a public planning topology when inadmissible alternatives survive into the planner's effective search representation.
- E6b shows that the frozen semantic adapter is sound under external native semantics and independent third-party planning/validation, but also shows that Fast Downward can remove the same irrelevant structure during preprocessing.

This distinction turns the mature-planner null into a mechanism result rather than an embarrassment.

## 7.2 Computational claim

Recommended wording:

> GSC does not introduce a planner-independent complexity reduction. Its computational benefit depends on how much mission-irrelevant structure survives the planner's own grounding, relevance analysis, and preprocessing. When the planner already eliminates that structure, as in E6b, GSC's measurable contribution is upstream semantic governance, auditability, and explicit state-conditioned domain membership rather than additional search reduction.

## 7.3 Why GSC still matters when the planner prunes the same actions

The paper should explicitly answer this anticipated reviewer question.

A downstream planner's relevance pruning and GSC are not equivalent governance mechanisms:

1. planner preprocessing optimizes a symbolic planning problem after it has been constructed;
2. GSC decides which provider–action instances are admissible before the problem enters the planner;
3. GSC records rejection reasons and snapshot provenance;
4. GSC can enforce safety/availability/authorization semantics that are not reducible to goal relevance;
5. the output is an auditable contract between persistent semantics and planning, independent of downstream heuristic behavior.

E6b demonstrates overlap in one narrow class of native Rovers irrelevance; it does not collapse the conceptual boundary between governance admission and planner preprocessing.

---

# 8. Threats to validity — revised bullets

### Synthetic mechanism evidence

E1 deliberately controls action clutter and eligibility. Its search effects should not be read as unconditional planner speedups.

### E5 masks

E5 uses public topology but experimenter-authored runtime masks. It remains a topology stress test, not the strongest semantic-validity evidence.

### E6b semantic scope

E6b eliminates study-authored masks and uses native public planning semantics, but these predicates are not independent field safety/authorization annotations.

### Planner dependence

E6b demonstrates a complete mature-planner null for search burden: Fast Downward translates Full and GSC to the same effective problem. This limits computational generalization and should be reported as a boundary condition.

### Field scope

Neither E5 nor E6b establishes physical sensing accuracy, real command latency, field safety, or operational effectiveness.

### Freshness

Global revision invalidation remains deliberately conservative and produces revision-only false blocks.

---

# 9. Conclusion — recommended final framing

Recommended closing claim:

> Governed Semantic Compilation addresses the operational boundary between persistent semantic knowledge and executable planning by making mission-conditioned Provider–Action membership explicit, version-bound, and auditable. Controlled experiments show that correct semantic admission can reduce search pollution when inadmissible alternatives survive into search, while component and transfer studies isolate the roles of readiness, safety admission, freshness, validation, and provenance. A frozen external holdout on native IPC-3 Rovers semantics then preserves solvability and plan validity under Fast Downward 26.6 and VAL with zero oracle mismatch, validation failure, or non-admitted-provider exposure. Fast Downward simultaneously removes the excluded structure during translation, eliminating any additional search benefit on the holdout. The resulting claim is therefore not that GSC is a faster planner, but that explicit governed domain synthesis provides a correctness and accountability boundary whose computational benefit depends on the downstream planning stack.

---

# 10. Figure/table implications

Recommended main-paper visual structure:

1. **Figure 1:** GSC semantic-to-planning boundary and data contracts.
2. **Figure 2:** E1 controlled benchmark / eligibility-density mechanism result.
3. **Figure 3:** E3 ablation failure-mode matrix.
4. **Figure 4:** E4 transfer / unchanged-core evidence.
5. **Figure 5:** E5 topology stress result plus E6b boundary-condition panel.
6. **Table 1:** claim-to-evidence mapping.
7. **Table 2:** E6b frozen gate criteria and PASS result.

For Figure 5, a useful two-panel message is:

- left: E5 q=0 reductions (38.5%, 45.5%, 66.7%);
- right: E6b Full/GSC generated-state ratio = 1.00 for all 12 tasks.

This makes the conditional computational claim visually explicit.

---

# 11. Research stop rule

The experimental program for Paper 1 should now be considered closed unless adversarial manuscript review identifies a specific unresolved claim-evidence inconsistency.

Do **not** add another external benchmark simply to obtain a positive speed effect after observing the E6b null. That would weaken the confirmatory logic.

The next work package is:

**Paper 1 v0.4 full-text integration → claim/evidence consistency audit → adversarial reviewer pass → submission-target formatting.**
