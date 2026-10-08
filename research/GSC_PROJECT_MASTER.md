# Governed Semantic Compilation (GSC) — Project Master

> **Paper 1:** Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning  
> **Repository:** `qiangruhuang/Tianshu`  
> **Master version:** v1.6  
> **Last updated:** 2026-10-08  
> **Current phase:** experimental program closed; manuscript/figures/citation consolidation  
> **Role:** single source of truth for research state, claim boundaries, reproducibility, and next actions.

## 0. Maintenance contract

1. Update this Markdown first, then synchronize `docs/index.html`.
2. Never silently reinterpret completed experiments.
3. Preserve null/negative results when they define the claim boundary.
4. Frozen protocols may change only through an explicit new version.
5. A CI failure is not a scientific FAIL; a scientific status must come from the frozen gate.
6. Do not add a benchmark merely to recover a preferred effect direction.
7. DOCX/PDF remain outside the research phase until manuscript content is explicitly approved.

---

# 1. Research question

**When a system knows many possible providers and actions, which provider–action instances should be admitted into the planner for this mission, under the current state and policy, before search begins?**

Persistent semantic knowledge can legitimately contain reusable capabilities, multiple providers, general action templates, stable policy, and incomplete/open-world knowledge. A planner needs a bounded current problem. GSC therefore treats **mission-conditioned Provider–Action domain membership** as an explicit governance artifact between persistent semantics and planner search.

```text
Persistent semantic model + mission + current operational state
                         ↓
                Mission Snapshot
                         ↓
                    Readiness
                         ↓
                 GSC Compiler
        admitted Provider–Action domain
        + rejection provenance
        + snapshot/revision/hash binding
                         ↓
                     Planner
                         ↓
                    Validator
```

---

# 2. Final claim boundary

## Supported

1. Mission-conditioned Provider–Action admission is implementable as a separate planning boundary.
2. In the controlled E1 benchmark, semantically coherent action selection reduces search pollution beyond the trivial effect of selecting fewer actions.
3. Readiness, compile-time safety admission, freshness binding, post-plan validation, and rejection provenance are separable load-bearing mechanisms.
4. The same generic runtime core transfers without a domain-specific branch from the C-UAS fixture to a five-phase SAR/inspection configuration.
5. E5 shows that the controlled search-pollution direction can survive public planning topology when governance-invalid alternatives remain in the effective search representation.
6. **E6b passes the frozen independent external-validity gate** on held-out public native semantics with a cross-implementation oracle, Fast Downward 26.6, and VAL.
7. E6b supports semantic soundness, solvability preservation, non-admitted-provider exclusion, and external planner/validator independence on the frozen Rovers holdout.

## Not supported

- universal planning-complexity reduction;
- planner-independent speedup;
- a claim that GSC must reduce search under mature planners;
- field safety or physical performance;
- sensing/effect effectiveness;
- unrestricted cross-domain autonomy;
- optimal freshness/revalidation;
- independently authored field safety/authorization labels for E6b.

**Final storyline:**

> **correct governed domain synthesis + conditional computational benefit**

---

# 3. Evaluation architecture

| Experiment | Question | Evidence | Final status |
|---|---|---|---|
| E0 | Frozen prototype reproducibility | regression anchor | **Complete** |
| E1 | Is semantic selection better than weaker/same-size alternatives for the right reason? | 12,600 controlled evaluations | **Complete** |
| E2 | Do current-state changes truthfully change domain/plan behavior? | deterministic state perturbations | **Complete** |
| E3 | Which governance components are load-bearing? | 5,400 ablation trials | **Complete** |
| E4 | Does the same runtime core transfer beyond the original configuration? | configuration-only five-phase transfer | **Complete** |
| E5 | Does the search-pollution effect survive public planning topology? | IPC-3 Rovers topology stress test | **Complete** |
| E6a | Is Satellite suitable as a native-semantic confirmatory gate? | external pilot | **Complete pilot; insufficient selectivity** |
| E6b | Does frozen admission preserve native public semantics with independent implementation/planner/validator paths? | confirmatory external-validity gate | **PASS — run 37713826709** |

---

# 4. Core results

## E1 — definitive mechanism benchmark

At `N=640, rho=0.05`:

- blind search solved: GSC 30/30; Random-core 20/30; State-aware 0/30; Full-domain 0/30;
- A* median generated nodes: GSC 4; Random-core 31; State-aware 308; Full-domain 612;
- GSC semantic precision = recall = 1.000 across tested cells;
- at `rho=1`, all methods converge as prespecified.

Interpretation: same-cardinality Random-core shows that the effect is not explained by action count alone.

## E3 — component ablations

Across 5,400 trials:

- Full GSC: 0/400 false allows across four post-plan challenge classes;
- without freshness: 100/400 false allows;
- without validator: 400/400 false allows;
- without Readiness: 200/200 unnecessary planner calls in missing-capability/G0 cases;
- without compile-time safety gating: safety-blocked case produces a plan in 100/100 trials and mean 1.99 invalid Provider–Action instances/trial enter the domain;
- revision-only changes cause 100/100 false blocks under global freshness.

## E4 — configuration-only transfer

Five-phase transfer configuration:

`Locate → Inspect → MapAccess → Relay → DeliverAid`

The generic runtime core SHA-256 remains unchanged and no domain-specific runtime branch is added. Across 800 trials/domain, decision-relevant false allow/block is 0/600 per domain; selected-provider-failure recovery is 66/66 when redundancy >=2.

## E5 — public-topology stress test

IPC-3 Rovers tasks 03/05/07; 1,800 runs; study-authored masks; separate clean-room planner.

At q=0, median generated-node reductions vs Full-domain are:

- task 03: 38.5%
- task 05: 45.5%
- task 07: 66.7%

At q=1 the methods converge. E5 is classified as **public-topology stress test**, not final semantic external validation.

---

# 5. E6b confirmatory external-validity gate

## Frozen design

- holdout: IPC-3 Rovers p09–p20;
- benchmark commit: `e21d49c2cb61d147a46c5966f2581bf6fd422b9f`;
- no synthetic governance mask;
- native PDDL capability/state semantics only;
- Python compiler vs separately implemented Node.js/JavaScript recursive S-expression oracle;
- Fast Downward 26.6, `--alias lama-first`, 300 s/run, 4 GiB/run;
- VAL commit `3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`;
- returned GSC plans validated against original, unmodified public PDDL.

## Static/native-semantic evidence

- rovers: 58/58 admitted;
- cameras: 60/65 admitted;
- stores: 47/58 admitted;
- total provider-related objects: 165/181 admitted; **16/181 excluded = 8.84%**;
- native mission-output goals: 136;
- uncovered goals: 0;
- cross-implementation admission mismatches: 0.

## Confirmatory identity

- GitHub Actions run: `37713826709`
- head commit: `64c3f66cf95951fac180487b18a26d78e681507b`
- artifact ID: `11522843338`
- artifact ZIP SHA-256: `36fc77b08100eb655ab575c8ca1c70f6a349f373cf19d38994b6bfb9b814d5a8`

## Frozen gate result

| Criterion | Result |
|---|---:|
| Source identity mismatch | **0** |
| Cross-implementation oracle mismatch | **0** |
| Uncovered native goals | **0** |
| Fast Downward 26.6 | **verified** |
| VAL frozen commit | **verified** |
| Full-domain evaluable | **12/12** |
| Required minimum | **10/12** |
| Full-solved → GSC-unsolved | **0** |
| GSC VAL failures | **0** |
| Non-admitted-provider exposure | **0** |

## **E6b scientific status: PASS**

---

# 6. Mature-planner boundary result

E6b's performance outcome is a clean null.

Full and GSC are identical in 12/12 pairs for:

- translator variables, facts, operators, and task size;
- relevant atoms and necessary variables/operators;
- landmark counts;
- expanded states;
- generated states;
- plan length;
- final `sas_plan` bytes.

Across 12 pairs:

- median generated states: Full = GSC = 4,863.5;
- median expanded states: Full = GSC = 145;
- median plan length: Full = GSC = 45;
- median wall time: Full 0.1275 s, GSC 0.1246 s;
- GSC faster in 6/12 wall-time pairs and slower in 6/12.

Mechanistic interpretation: Fast Downward translation/relevance preprocessing removes the same native-goal-irrelevant structures that GSC removes upstream. E5 and E6b therefore are not contradictory.

**Computational claim:**

> Semantic admission can reduce search pollution when irrelevant structure survives planner preprocessing. It is not a planner-independent complexity reduction.

---

# 7. Final literature/novelty refresh — 2026-10-08

Two September 2026 peer-reviewed neighbours were added to the working manuscript:

1. Jørgensen & Ma, *Information* 17(9):923, doi:10.3390/info17090923 — separates semantic validity, process admissibility, policy, delegated authority, controlled execution, and provenance around agent-proposed actions.
2. An et al., *Sensors* 26(18):5973, doi:10.3390/s26185973 — carries ontology/SWRL reasoning into PDDL mission planning and continuous trajectory optimization for autonomous driving.

These works narrow the novelty claim but do not trigger the novelty hard-stop. GSC does **not** claim ontology-to-PDDL integration, semantic validity, or governed execution in general as novel. The retained contribution is the mission-conditioned heterogeneous Provider–Action planning-domain membership boundary plus its direct mechanism and external evaluation.

---

# 8. Current manuscript package

GitHub:

- `research/manuscript/Paper1_Manuscript_v0.4.md` — last complete full manuscript committed to GitHub;
- `research/manuscript/Paper1_v0.4.1_Delta.md` — guarded-PDDL/oracle/selectivity corrections;
- `research/manuscript/Paper1_v0.4.2_Literature_Citation_Delta.md` — final literature refresh;
- `research/manuscript/Paper1_Claim_Evidence_Citation_Audit_v1.0.md` — citation audit;
- `research/figures/Paper1_Figure_Table_Package_v1.0.md` — figure/table plan.

Project Library contains the complete current full manuscript `Paper1_Manuscript_v0.4.2.md` and publication figures.

Main figures are now frozen as:

1. GSC architecture;
2. E1 same-cardinality mechanism evidence;
3. E5 public-topology conditional search reduction;
4. E6b native provider admission/selectivity;
5. E6b mature-planner null.

---

# 9. Research stop rule and next action

**Paper 1 experimental program is closed.**

No additional external benchmark should be added merely to recover a positive speedup. The mature-planner null is a valid boundary result and should remain visible.

Next work package:

1. integrate Figures 1–5 into the manuscript;
2. reduce repeated numerical reporting across Abstract/Results/Discussion/Conclusion;
3. complete final sentence-level reference-format normalization;
4. choose/finalize target-venue formatting;
5. generate DOCX/PDF only after explicit manuscript-content approval.

A new experiment is justified only if a later reviewer identifies a concrete claim that cannot be supported or removed using the existing evidence.

---

# 10. Evidence boundary

All evidence remains software/formal-model, parameterized synthetic, or public planning-benchmark evidence. E4's second domain is synthetic; E5 masks are study-authored; E6b native semantics are not independently authored field safety/authorization labels; E6b selectivity is modest; global freshness is conservative; and no field-performance or physical-safety claim is made.