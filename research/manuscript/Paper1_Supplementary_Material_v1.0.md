# Paper 1 — Supplementary Material v1.0

**Manuscript:** *Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning*  
**Target journal:** *Robotics and Autonomous Systems*  
**Date:** 2026-10-08  
**Status:** Derived entirely from frozen/previously completed evidence. No new experiment is introduced here.

---

## S1. Purpose and evidence boundary

This supplement preserves detailed reproducibility information that would make the main manuscript unnecessarily dense. It does not extend the claim boundary.

All evidence remains software/formal-model, parameterized synthetic, or public planning-benchmark evidence. It does not establish field performance, physical safety, sensing accuracy, engagement effectiveness, communication latency, or unrestricted domain generality.

---

## S2. Evidence hierarchy

| Experiment | Purpose | Status |
|---|---|---|
| E0 | Frozen prototype regression | Complete |
| E1 | Controlled mechanism / same-cardinality falsification | Complete |
| E2 | State-conditioned truthfulness fixtures | Complete |
| E3 | Component ablations | Complete |
| E4 | Configuration-only transfer | Complete |
| E5 | Public-topology stress test | Complete |
| E6a | Native-semantic Satellite pilot | Complete pilot; insufficient selectivity |
| E6b | Confirmatory external-validity gate | **PASS** |

---

## S3. E1 controlled mechanism details

The definitive E1 benchmark contains 30 paired mission instances for each action-library-size × eligibility-density cell, three clutter topologies, balanced provider-redundancy strata, seven domain-selection methods, and two search strategies.

The key falsification is the **same-cardinality Random-core control**. Random-core is forced to retain the task-critical action chain and is filled randomly to exactly the GSC domain size. This prevents a trivial interpretation in which GSC appears favorable merely because it contains fewer actions.

At `N=640, rho=0.05`:

- blind search solved: GSC 30/30; Random-core 20/30; State-aware 0/30; Full-domain 0/30;
- A* median generated nodes: GSC 4; Random-core 31; State-aware 308; Full-domain 612;
- GSC and Oracle precision = recall = 1.000;
- at `rho=1`, all methods converge as prespecified.

The main manuscript contains the compact result table; the full frozen benchmark should be distributed with the public project package if retained for review.

---

## S4. E3 component-ablation diagnostics

Across 5,400 controlled trials:

| Configuration / challenge | Diagnostic result |
|---|---|
| Full GSC, four post-plan challenges | 0/400 false allows |
| Without freshness | 100/400 false allows |
| Without validator | 400/400 false allows |
| Without Readiness, missing-capability + G0 cases | 200/200 unnecessary planner invocations |
| Without compile-time safety | safety-blocked case yields plan in 100/100 trials |
| Without compile-time safety | mean 1.99 invalid Provider–Action instances/trial enter domain |
| Without rejection reasons | provenance coverage 100% → 0% |
| Full global freshness, revision-only | 100/100 false blocks |

These diagnostics support separation of Readiness, compile-time admission, freshness, post-plan validation, and provenance rather than treating them as one undifferentiated safety mechanism.

---

## S5. E4 configuration-only transfer

The second configuration uses the five-phase mission:

`Locate → Inspect → MapAccess → Relay → DeliverAid`

The generic runtime core SHA-256 remains unchanged and no domain-specific runtime branch is added.

Per domain:

- 800 trials;
- decision-relevant false allow/block: 0/600;
- selected-provider-failure recovery: 66/100 overall;
- recovery when redundancy ≥2: 66/66;
- revision-only false block: 100/100.

E4 supports configuration-level portability inside the shared `Mission → Capability → Provider → Action` abstraction. It does not establish unrestricted domain generality.

---

## S6. E5 public-topology stress test

E5 uses public IPC-3 Rovers 03/05/07, study-authored governance masks, and a separate clean-room typed-STRIPS planner.

At the most restrictive mask (`q=0`):

| Task | Full grounded ops | GSC ops | GSC valid | Random-core valid | Median generated GSC | Median generated Full | Reduction |
|---|---:|---:|---:|---:|---:|---:|---:|
| 03 | 60 | 57 | 30/30 | 27/30 | 67 | 109 | 38.5% |
| 05 | 141 | 111 | 30/30 | 6/30 | 175 | 321 | 45.5% |
| 07 | 153 | 113 | 30/30 | 30/30 | 107 | 321 | 66.7% |

At `q=1`, methods converge.

E5 is deliberately classified as a **public-topology stress test**, not independent semantic validation, because the governance masks are experimenter-authored.

---

## S7. E6b frozen confirmatory design

### S7.1 Frozen corpus and tools

- holdout: IPC-3 Rovers p09–p20;
- benchmark commit: `e21d49c2cb61d147a46c5966f2581bf6fd422b9f`;
- Fast Downward: `26.6`, alias `lama-first`;
- resource cap: 300 s and 4 GiB per run;
- VAL commit: `3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`;
- GSC plans validated against the original, unmodified public PDDL.

The cross-implementation admission path uses:

1. a Python compiler-side implementation; and
2. a separate Node.js/JavaScript recursive S-expression implementation.

Both instantiate the same frozen study-defined mapping over externally authored public PDDL semantics. The zero mismatch therefore tests reproducible implementation, not independently authored policy truth.

### S7.2 Native-semantic selectivity

Across the 12 holdout problems:

- rovers admitted: 58/58;
- cameras admitted: 60/65;
- stores admitted: 47/58;
- total provider-related objects admitted: 165/181;
- excluded: 16/181 = 8.84%;
- native mission-output goals: 136;
- goals without any witness: 0.

This is a **no-loss external semantic gate with modest selectivity**, not a high-pruning stress test.

### S7.3 Frozen PASS criteria and observed outcome

| Criterion | Frozen requirement / observed value |
|---|---|
| Source identity mismatch | observed 0 |
| Cross-implementation mismatch | observed 0 |
| Uncovered native goals | observed 0 |
| Fast Downward identity | verified 26.6 |
| VAL source identity | verified frozen commit |
| Full evaluable | observed 12/12; required ≥10/12 |
| Full-solved → GSC-unsolved | observed 0 |
| GSC VAL failures | observed 0 |
| Non-admitted-provider exposures | observed 0 |
| **Scientific status** | **PASS** |

GitHub Actions confirmatory run: `37713826709`.

---

## S8. E6b per-instance paired results

| Instance | Full generated | GSC generated | Full expanded | GSC expanded | Full plan | GSC plan | Full wall (s) | GSC wall (s) | VAL | Exposure |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| p09 | 1,428 | 1,428 | 70 | 70 | 36 | 36 | 0.171 | 0.110 | PASS | 0 |
| p10 | 3,124 | 3,124 | 138 | 138 | 39 | 39 | 0.121 | 0.114 | PASS | 0 |
| p11 | 2,115 | 2,115 | 99 | 99 | 36 | 36 | 0.111 | 0.104 | PASS | 0 |
| p12 | 664 | 664 | 32 | 32 | 21 | 21 | 0.103 | 0.108 | PASS | 0 |
| p13 | 4,964 | 4,964 | 239 | 239 | 46 | 46 | 0.124 | 0.132 | PASS | 0 |
| p14 | 2,793 | 2,793 | 110 | 110 | 33 | 33 | 0.117 | 0.119 | PASS | 0 |
| p15 | 13,103 | 13,103 | 408 | 408 | 46 | 46 | 0.131 | 0.122 | PASS | 0 |
| p16 | 5,594 | 5,594 | 250 | 250 | 44 | 44 | 0.124 | 0.127 | PASS | 0 |
| p17 | 4,763 | 4,763 | 127 | 127 | 54 | 54 | 0.169 | 0.166 | PASS | 0 |
| p18 | 6,691 | 6,691 | 152 | 152 | 46 | 46 | 0.198 | 0.208 | PASS | 0 |
| p19 | 21,802 | 21,802 | 499 | 499 | 74 | 74 | 0.255 | 0.251 | PASS | 0 |
| p20 | 37,608 | 37,608 | 746 | 746 | 99 | 99 | 0.369 | 0.371 | PASS | 0 |

Across all 12 instances:

- median generated states: Full = GSC = 4,863.5;
- median expanded states: Full = GSC = 145;
- median plan length: Full = GSC = 45;
- final `sas_plan` is byte-identical in every pair;
- GSC wall time is lower in 6/12 and higher in 6/12.

The small wall-time differences are treated as execution noise rather than a stable computational effect.

---

## S9. Interpretation of the mature-planner null

E6b does not reproduce E1/E5 search reduction because the objects excluded by the native-semantic GSC adapter are also irrelevant to the native Rovers goals. Fast Downward translation/relevance preprocessing eliminates their associated planning structure in the Full condition before search.

The result therefore identifies a mechanism boundary:

> Semantic admission can reduce search pollution when irrelevant structure survives planner preprocessing. It is not a planner-independent complexity reduction.

This null is retained in the main paper and is not treated as a failed experiment.

---

## S10. Reproducibility identities

Confirmatory artifact identity:

- GitHub Actions run: `37713826709`;
- artifact ID: `11522843338`;
- artifact ZIP SHA-256: `36fc77b08100eb655ab575c8ca1c70f6a349f373cf19d38994b6bfb9b814d5a8`.

Toolchain verification:

```text
Fast Downward 26.6
git revision [release]: 64c3f66
VAL expected:  3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4
VAL observed:  3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4
VAL binary in verified source tree: True
```

Primary committed/maintained reproducibility assets include:

- frozen E6b protocol;
- cross-implementation oracle manifest/generator;
- confirmatory runner;
- GitHub Actions workflow;
- gate summary;
- paired results;
- source/toolchain identities;
- figure-generation script.

---

## S11. Reproducibility policy

No post-outcome change was made to:

- holdout corpus;
- admission rule;
- planner version/alias;
- time or memory limits;
- validator commit;
- PASS criteria.

The study does not recommend rerunning E6b with altered limits or searching for a new benchmark solely to recover a favorable speedup.
