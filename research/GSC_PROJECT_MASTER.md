# Governed Semantic Compilation (GSC) — Project Master

> **Paper 1:** Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning  
> **Repository:** `https://github.com/qiangruhuang/Tianshu`  
> **Master version:** v1.5.1  
> **Last updated:** 2026-10-08  
> **Current phase:** experimental program closed; v0.4.1 manuscript consolidation, figures/tables, sentence-level citation audit, and target-venue formatting  
> **Role:** single source of truth for research status, claim boundaries, locked decisions, reproducibility, and next actions.

---

## 0. Maintenance contract

1. Update this Markdown first.
2. Never overwrite or silently reinterpret a completed experiment.
3. A frozen protocol changes only through a new explicit version.
4. Synchronize `docs/index.html` only after this Master is updated.
5. Scientific PASS/FAIL/INCONCLUSIVE must come from the frozen gate, not CI status alone.
6. Infrastructure failures are not scientific failures.
7. Preserve negative/null results when they define the claim boundary.
8. Do not add an experiment merely to recover a preferred effect direction.
9. DOCX/PDF generation remains outside the research phase until the manuscript content is explicitly approved.

Canonical repository layout:

```text
README.md
research/
  GSC_PROJECT_MASTER.md
  E6b_Confirmatory_Interpretation_v1.0.md
  manuscript/
    Paper1_v0.4_E6b_Integration_Guide.md
    Paper1_v0.3_to_v0.4_Claim_Evidence_Audit.md
docs/
  index.html
e6b/
  protocol/
  oracle/
  runner/
  records/
  results/run-37713826709/
.github/workflows/
  e6b-confirmatory.yml
```

---

# 1. Research question

**When a system knows many possible providers and actions, which provider–action instances should be admitted into the planner for this mission, under the current state and policy, before search begins?**

Persistent semantic knowledge and executable planning have different runtime requirements. A semantic model can contain reusable capabilities, alternative providers, general action templates, stable policies, and incomplete/open-world knowledge. A planner instead needs a bounded current problem: which providers are healthy now, which facts are trusted now, which safety/authorization conditions apply now, and which provider–action instances should enter the current planning domain.

The central failure mode is therefore not simply “bad planning.” A planner can search correctly over the wrong action domain.

---

# 2. Proposed mechanism

GSC inserts a governed compilation boundary between persistent semantics and planning:

```text
Persistent semantic model
        +
Mission specification
        +
Current operational state
        |
        v
Versioned Mission Snapshot
        |
        +--> Readiness gate
        |
        v
Governed Semantic Compiler
        |
        +--> admitted Provider–Action set
        +--> rejected actions + reason provenance
        +--> snapshot/revision/hash binding
        |
        v
Planner
        |
        v
Post-plan validator
        |
        +--> release only if current-state / authorization /
             provider / membership / freshness checks pass
```

The paper's first-class object is **mission-conditioned Provider–Action domain membership**.

The contribution is intentionally narrower than:

- generic ontology + planning;
- a new OWL-to-PDDL logic;
- planner design itself;
- stale-plan checking as a standalone novelty.

---

# 3. Final claim boundary after E6b

## 3.1 Supported by completed evidence

1. **Mission-conditioned Provider–Action admission is implementable as a separate planning boundary.**
2. **Semantic selection can reduce search pollution beyond the trivial effect of selecting fewer actions** in the controlled E1 setting.
3. **Readiness, compile-time safety admission, freshness binding, post-plan validation, and rejection provenance are separable load-bearing mechanisms.**
4. **The same generic runtime core transfers without a domain-specific branch** from the C-UAS fixture to a five-phase SAR/inspection configuration.
5. **The E5 search-pollution effect is not confined to the original synthetic four-stage topology**, although E5 still uses study-authored masks and a clean-room planner.
6. **E6b passes the frozen independent external-validity gate** using held-out public native semantics, a cross-implementation oracle implemented independently from the compiler, Fast Downward 26.6, and VAL.
7. E6b supports **semantic soundness, solvability preservation, non-admitted-provider exclusion, and planner/validator independence** on the frozen Rovers holdout.

## 3.2 Not supported

- universal planning-complexity reduction;
- planner-independent speedup;
- a claim that GSC must reduce search under mature planners;
- field safety or physical performance;
- sensing/effect effectiveness;
- unrestricted cross-domain autonomy;
- optimal freshness/revalidation;
- independently authored field safety/authorization labels for E6b.

## 3.3 Key boundary result

Under Fast Downward 26.6, Full and GSC become the **same effective planning/search problem on all 12 E6b holdout instances**.

Therefore:

> GSC is supported as a governed semantic domain-synthesis and accountability boundary. Computational benefit is conditional on whether mission-irrelevant or governance-invalid structure survives the downstream planner's own grounding and preprocessing.

---

# 4. Evaluation architecture

| Experiment | Core question | Evidence type | Final status |
|---|---|---|---|
| E0 | Does the frozen prototype reproduce intended behavior? | Regression anchor | **Complete** |
| E1 | Does semantic admission beat weaker/same-size alternatives for the right reason? | Controlled mechanism benchmark | **Complete** |
| E2 | Do state changes truthfully change domain/plan behavior? | State-perturbation fixtures | **Complete** |
| E3 | Which governance components are load-bearing? | Component ablations | **Complete** |
| E4 | Does the same runtime core transfer beyond the original configuration? | Configuration-only transfer | **Complete** |
| E5 | Does the search-pollution effect survive public planning topology? | IPC-3 Rovers topology stress test | **Complete** |
| E6a | Is Satellite suitable as a confirmatory native-semantic gate? | External pilot | **Complete pilot; insufficient selectivity** |
| E6b | Does frozen admission preserve native public semantics with independent oracle/planner/validator? | Independent external-validity gate | **PASS — run 37713826709** |

---

# 5. Key results before E6

## 5.1 E0 — frozen regression

For global action-template counts 20, 40, 60, and 80, GSC compiles to **6 actions** in every case.

- pruning ratios: 70.0%, 85.0%, 90.0%, 92.5%;
- compiled reference planner: 4 expansions in all four cases;
- ungated baseline:
  - N=20: 714 expansions;
  - N=40: 2,501-node cap;
  - N=60: 2,501-node cap;
  - N=80: timeout after 2,333 expansions.

E0 is a reproducibility anchor rather than the primary causal result.

## 5.2 E1 — definitive mechanism benchmark

**12,600 method–planner evaluations**, with 30 paired mission instances per N×ρ cell.

GSC matches the generator-owned eligibility oracle in every tested cell:

- semantic precision = **1.000**;
- semantic recall = **1.000**.

At **N=640, ρ=0.05**:

### Blind search

- GSC: **30/30**
- core-preserving Random-core: **20/30**
- State-aware: **0/30**
- Full-domain: **0/30**

### A*

All methods solve, but median generated nodes are:

- GSC: **4**
- Random-core: **31**
- State-aware: **308**
- Full-domain: **612**

At ρ=1 the advantage disappears as prespecified.

Interpretation: the main E1 result is **semantic selection**, not simply smaller cardinality.

## 5.3 E2 — state-conditioned truthfulness

Observed perturbations behave distinctly:

- reliable observation added → detection omitted and plan shortens;
- selected primary provider fails → provider leaves compiled domain and backup is selected;
- essential capability loss → Readiness blocks planning;
- G0 unsafe condition → Readiness blocks entry;
- L2 authorization revoked → current symbolic problem becomes unsolvable;
- revision-only metadata change → old plan is rejected even when replanning returns the same sequence.

The last case exposes a deliberate limitation: global freshness is fail-closed but over-conservative.

## 5.4 E3 — component ablations

**5,400 trials.**

Across authorization revocation, selected-provider failure, target change, and unknown-action injection:

- Full GSC: **0/400 false allows**
- without freshness fence: **100/400**
- without post-plan validator: **400/400**

Additional diagnostics:

- without Readiness: **200/200 unnecessary planner invocations**;
- without compile-time safety: safety-blocked case yields a plan in **100/100** trials and admits mean **1.99 invalid Provider–Action instances/trial**;
- without rejection provenance: reason coverage **100% → 0%**;
- full global freshness: **100/100 revision-only false blocks**.

## 5.5 E4 — configuration-only transfer

Second configuration:

`Locate → Inspect → MapAccess → Relay → DeliverAid`

The generic runtime core retains the same SHA-256 and adds no domain-specific branch.

Per domain:

- **800 trials**;
- decision-relevant false allow/block: **0/600; 0/600**;
- selected-provider failure recovery: **66/100 overall; 66/66 when redundancy ≥2**;
- revision-only false block: **100/100**.

This supports configuration-level portability inside the shared `Mission → Capability → Provider → Action` abstraction, not unrestricted domain generality.

## 5.6 E5 — public-topology stress test

Public IPC-3 Rovers tasks 03/05/07 with a separate generic STRIPS planner and study-authored governance masks.

Total: **1,800 runs**.

At q=0:

| Task | Full ops | GSC ops | GSC valid | Random-core valid | GSC generated | Full generated | Reduction |
|---|---:|---:|---:|---:|---:|---:|---:|
| 03 | 60 | 57 | 30/30 | 27/30 | 67 | 109 | 38.5% |
| 05 | 141 | 111 | 30/30 | 6/30 | 175 | 321 | 45.5% |
| 07 | 153 | 113 | 30/30 | 30/30 | 107 | 321 | 66.7% |

At q=1 all methods converge.

**Evidence classification:** public-topology stress test, not the strongest external semantic-validity evidence.

---

# 6. E6 independent external-validity program

## 6.1 E6a — Satellite pilot

The frozen IPC-3 Satellite pilot was retained transparently after audit showed too little provider selectivity for a strong confirmatory gate.

No admission rule was changed after inspection to manufacture pruning.

## 6.2 E6b — frozen Rovers confirmatory holdout

### Frozen design

- Holdout: IPC-3 Rovers `p09`–`p20`, separate from E5.
- Benchmark commit: `e21d49c2cb61d147a46c5966f2581bf6fd422b9f`.
- No synthetic runtime governance mask.
- Admission based only on native public PDDL capability/state semantics.
- Cross-implementation oracle: Python compiler path vs an independently implemented Node.js/JavaScript recursive S-expression implementation.
- Fast Downward: **26.6**.
- Search configuration: `--alias lama-first`.
- Resource cap: **300 s / 4 GiB per run**.
- VAL commit: `3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`.
- GSC plans validated against **original unmodified public PDDL**.
- Performance endpoints were secondary and not required for PASS.

### Static/native-semantic evidence

- rovers admitted: **58/58**
- cameras admitted: **60/65**
- stores admitted: **47/58**
- total provider-related objects admitted: **165/181**
- objects excluded: **16/181 = 8.84%**
- native mission-output goals: **136**
- uncovered goals: **0**
- independent-oracle mismatches: **0**

### Confirmatory execution identity

GitHub Actions run: **37713826709**  
Head commit: `64c3f66cf95951fac180487b18a26d78e681507b`  
Artifact ID: **11522843338**  
Artifact ZIP SHA-256:

`36fc77b08100eb655ab575c8ca1c70f6a349f373cf19d38994b6bfb9b814d5a8`

### Frozen gate result

| Frozen criterion | Result |
|---|---:|
| Source identity mismatches | **0** |
| Admission serialization mismatches | **0** |
| Independent-oracle mismatches | **0** |
| Uncovered native goals | **0** |
| Fast Downward 26.6 identity | **verified** |
| VAL frozen source commit | **verified** |
| Full-domain evaluable | **12/12** |
| Required minimum Full evaluable | **10/12** |
| Full-solved → GSC-unsolved | **0** |
| GSC VAL failures | **0** |
| Non-admitted-provider exposures | **0** |

## **Scientific conclusion: E6b PASS**

All 12 Full and all 12 GSC tasks solved within the frozen resource cap.

Every returned GSC plan passed VAL against the original public problem/domain.

No returned plan used a non-admitted provider.

---

# 7. E6b mature-planner null effect

The frozen protocol explicitly defined search performance as secondary.

The mature-planner result is a clean null.

Full and GSC are identical in **12/12 pairs** for:

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
- final `sas_plan` bytes.

Across 12 pairs:

- median generated states: Full = GSC = **4,863.5**
- median expanded states: Full = GSC = **145**
- median plan length: Full = GSC = **45**
- median wall time: Full **0.1275 s**, GSC **0.1246 s**
- GSC wall time lower: **6/12**
- GSC wall time higher: **6/12**

The wall-time variation is consistent with execution noise.

## Mechanistic interpretation

GSC removes 5 cameras and 11 stores, but these providers are also irrelevant under the native planning goals and facts. Fast Downward translation/relevance preprocessing removes the corresponding planning structure from the Full condition before search.

Therefore:

- E5 and E6b are **not contradictory**.
- E5 shows search reduction when governance-invalid alternatives survive to the effective search representation.
- E6b shows that a mature planner can independently eliminate the same class of native-goal-irrelevant structure.

The computational claim is thus:

> **Semantic admission can reduce search pollution when irrelevant structure survives planner preprocessing. It is not a planner-independent complexity reduction.**

---

# 8. Why GSC remains meaningful when planner preprocessing removes the same structure

Planner relevance pruning and GSC solve different problems.

1. **Timing**
   - Planner preprocessing acts after a planning problem has been built.
   - GSC governs what is allowed to enter the planner.

2. **Semantics**
   - Planner pruning is driven by symbolic reachability/relevance.
   - GSC can use availability, safety, policy, authorization, and provider state.

3. **Auditability**
   - GSC records rejection reasons.
   - It records the snapshot/revision/hash that justified admission.

4. **Architectural contract**
   - GSC creates an explicit boundary between persistent semantic knowledge and executable planning.
   - The governance decision is not hidden inside a planner-specific heuristic or grounder.

5. **Planner independence**
   - E6b shows that the correctness of admission can be tested independently even when the downstream planner later collapses the search representation to the same problem.

The paper's strongest contribution is therefore **correct governed domain synthesis**, with **conditional computational benefit**.

---

# 9. Evidence ladder — closed for Paper 1

```text
E0  Reproducibility                                      COMPLETE
 ↓
E1  Controlled mechanism evidence                       COMPLETE
 ↓
E2  State-conditioned truthfulness                      COMPLETE
 ↓
E3  Component necessity / failure modes                 COMPLETE
 ↓
E4  Configuration-level portability                     COMPLETE
 ↓
E5  External public planning topology                   COMPLETE
 ↓
E6b Native public semantics + independent oracle        COMPLETE
 ↓
Fast Downward 26.6 + frozen VAL confirmatory gate       PASS
```

The planned external-validity evidence chain is closed.

---

# 10. Current manuscript decision

The evidence program is closed. The current working manuscript state is:

- full Markdown manuscript v0.4 completed and synchronized to GitHub;
- local/Library v0.4.1 incorporates the explicit E6b planning-only guard implementation, cross-implementation-oracle terminology, external-selectivity limitation, and refreshed current references;
- adversarial review completed with the verdict **minor-to-moderate manuscript revision; no new experiment required**;
- focused 2026-10-08 novelty refresh completed; the novelty hard-stop was **not triggered**.

GitHub manuscript/review assets:

- `research/E6b_Confirmatory_Interpretation_v1.0.md`
- `research/manuscript/Paper1_v0.4_E6b_Integration_Guide.md`
- `research/manuscript/Paper1_v0.3_to_v0.4_Claim_Evidence_Audit.md`
- `research/manuscript/Paper1_Manuscript_v0.4.md`
- `research/manuscript/Paper1_v0.4.1_Adversarial_Review.md`
- `research/manuscript/Novelty_Refresh_2026-10-08.md`

The v0.4.x storyline is now frozen around:

> **correct governed domain synthesis + conditional computational benefit**

The next work package is:

**publication-quality figures/tables from existing results → sentence-level claim/citation audit → target-venue formatting/language editing → explicit approval before DOCX/PDF generation.**

No further benchmark should be added unless a later reviewer identifies a concrete claim that cannot be supported or removed using the existing evidence.

---

# 11. Research stop rule

Do **not** add another external benchmark merely to recover a positive search-speed effect.

That would weaken the confirmatory design because the mature-planner null is already an observed boundary condition.

Additional experiments are justified only when manuscript-level adversarial review identifies a **specific unresolved claim–evidence gap**.

---

# 12. Known limitations

1. Evidence remains software/formal-model, parameterized synthetic, or public planning-benchmark evidence.
2. E4's second domain is synthetic and shares the paper abstraction.
3. E5 governance overlays are study-authored.
4. E6b uses independently authored executable capability/state predicates, not independently authored field safety/authorization labels.
5. Global freshness is deliberately conservative and over-blocks revision-only changes.
6. E6b provides no mature-planner search reduction on p09–p20.
7. No claim is made about real sensing, physical effects, command latency, operational safety, or field effectiveness.

---

# 13. Collaboration and reproducibility

Primary public workspace:

`https://github.com/qiangruhuang/Tianshu`

Primary result summaries:

`e6b/results/run-37713826709/`

Required confirmatory result files:

- `gate_summary.json`
- `paired_results.csv`
- `static_audit.csv`
- `independent_oracle_check.json`
- `toolchain_identity.json`
- `source_identity.json`

Primary manuscript guidance:

- `research/E6b_Confirmatory_Interpretation_v1.0.md`
- `research/manuscript/Paper1_v0.4_E6b_Integration_Guide.md`
- `research/manuscript/Paper1_v0.3_to_v0.4_Claim_Evidence_Audit.md`

---

# 14. Changelog

## v1.5.1 — 2026-10-08

- Tightened E6b terminology: the JavaScript path is a cross-implementation oracle, not independently authored policy ground truth.
- Replaced ambiguous “provider-exposure safety” wording with “non-admitted-provider exclusion.”

## v1.5 — 2026-10-08

- Completed the full v0.4 Markdown manuscript integrating E6b PASS and the mature-planner null.
- Added explicit E6b planning-only guarded-PDDL implementation details: static admitted-provider predicates are conjoined to action preconditions while original public PDDL remains the validation truth source.
- Clarified that the JavaScript/Python oracle is cross-implementation independence, not independently authored policy ground truth.
- Added the external-selectivity limitation: 16/181 provider-related objects excluded, with all 58 rovers admitted.
- Updated the published Holmberg et al. IEEE BigData 2025 citation and current PlanFence arXiv v2 title.
- Completed an adversarial reviewer audit; no new experiment is required.
- Completed a focused 2026-10-08 novelty refresh; the novelty hard-stop was not triggered.
- Froze the experimental program and moved the project to figures/tables, sentence-level citation audit, and target-venue formatting.

## v1.4 — 2026-10-08

- Independently re-audited GitHub Actions run `37713826709` and its raw artifact.
- Confirmed all frozen E6b PASS criteria from `gate_summary.json`.
- Confirmed 12/12 equality for translator/search statistics and final plan bytes.
- Quantified native-semantic exclusion as **16/181 provider-related objects (8.84%)**.
- Added formal E6b scientific interpretation.
- Added Paper 1 v0.4 integration guide.
- Added v0.3 → v0.4 Claim–Evidence audit based on the current manuscript.
- Updated README and maintained HTML from “gate pending” to **E6b PASS**.
- Closed experimental expansion for Paper 1 absent a specific adversarial-review gap.

## v1.3 — 2026-10-08

- Completed GitHub-hosted frozen Fast Downward 26.6 + VAL confirmatory execution.
- E6b status = **PASS**.
- Recorded mature-planner null: Full and GSC effective search problems identical on p09–p20.

## v1.2 — 2026-10-08

- Established `qiangruhuang/Tianshu` as canonical collaboration workspace.
- Added GitHub Actions confirmatory route.

## v1.1 — 2026-09-23

- Attempted local confirmatory execution.
- Preserved outcome blindness after environment pre-execution block.

## v1.0 — 2026-09-23

- Created project single source of truth.
- Consolidated E0–E5 evidence.
- Froze E6 external-validity program.
