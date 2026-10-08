# Governed Semantic Compilation (GSC) — Project Master

> **Paper 1:** Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning  
> **Repository:** `qiangruhuang/Tianshu`  
> **Master version:** v1.2  
> **Last updated:** 2026-10-08  
> **Role:** single source of truth for research status, evidence level, locked decisions, reproducibility, and next actions.

## 0. Maintenance contract

1. Update this Markdown first.
2. Never overwrite or silently reinterpret a completed experiment.
3. A frozen protocol may change only by creating a new version and documenting why.
4. Synchronize `docs/index.html` only after this Master is updated.
5. Do not write a gate as PASS until its frozen execution actually produces that result.
6. GitHub Actions infrastructure failure is not a scientific FAIL or INCONCLUSIVE result.
7. DOCX/PDF generation remains outside the research phase until the research content is explicitly approved.

Canonical repository layout:

- `research/GSC_PROJECT_MASTER.md` — research truth;
- `docs/index.html` — maintained visual panorama for collaborators and non-specialists;
- `e6b/` — byte-preserved frozen E6b assets and execution documentation;
- `.github/workflows/e6b-confirmatory.yml` — confirmatory execution environment.

---

# 1. Research question

**When a system knows many possible providers and actions, which provider–action instances should be admitted into the planner for this mission, under the current state and policy, before search begins?**

Persistent semantic knowledge and executable planning have different requirements. An ontology or knowledge graph can legitimately contain reusable capabilities, multiple providers, general action templates, stable policies, and incomplete/open-world knowledge. A planner instead requires a bounded current problem: which providers are healthy now, which facts are trusted now, which safety/authorization conditions apply now, and which provider–action instances should enter this particular planning domain.

The central failure mode is therefore not merely “bad planning.” A planner can search correctly over the wrong action domain.

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

The contribution is intentionally narrower than “ontology + planning.” The first-class object is **mission-conditioned Provider–Action domain membership**.

---

# 3. Claim boundary

## Supported by completed evidence

1. Mission-conditioned Provider–Action admission is implementable as a separate planning boundary.
2. In controlled experiments, semantically coherent admission reduces search pollution beyond the trivial effect of reducing action count.
3. Readiness, compile-time safety admission, freshness binding, post-plan validation, and rejection provenance have distinct measurable roles.
4. The same core runtime transfers without a domain-specific code branch from the C-UAS fixture to a five-phase SAR/inspection configuration.
5. The E5 effect survives an independently authored public planning topology.
6. E6b establishes native-benchmark semantic independence at the static/oracle layer using a held-out public corpus and separately implemented oracle.

## Not supported at the current evidence level

- universal planning-complexity reduction;
- planner-independent speedup;
- field safety or physical performance;
- sensing or effect effectiveness;
- unrestricted cross-domain autonomy;
- optimal freshness/revalidation;
- independent human-authored binary safety-policy labels for E6b;
- a final E6b PASS before Fast Downward 26.6 + VAL completes.

---

# 4. Evaluation architecture

| Experiment | Core question | Evidence | Status |
|---|---|---|---|
| E0 | Does the frozen prototype reproduce intended behavior? | regression anchor | **Complete** |
| E1 | Does semantic selection outperform weaker/same-size alternatives for the right reason? | controlled mechanism benchmark | **Complete** |
| E2 | Do state changes truthfully change domain/plan behavior? | state-perturbation fixtures | **Complete as mechanism fixtures** |
| E3 | Which governance components are load-bearing? | component ablations | **Complete** |
| E4 | Does the same runtime core transfer beyond the original configuration? | configuration-only transfer | **Complete** |
| E5 | Does the effect survive public planning topology? | IPC-3 Rovers topology stress test | **Complete** |
| E6a | Can Satellite native semantics form the confirmatory gate? | external pilot | **Complete pilot; insufficient selectivity** |
| E6b | Does frozen admission preserve native public semantics with an independent oracle, mature planner, and independent validator? | independent external-validity gate | **Static/oracle complete; planner execution in progress on GitHub Actions** |

---

# 5. Key results

## E0 — frozen regression

For global template counts 20, 40, 60, and 80, GSC compiles to **6 actions in every case**. Pruning ratios are 70.0%, 85.0%, 90.0%, and 92.5%. The compiled reference planner requires 4 expansions in all four cases; the ungated baseline requires 714 expansions at N=20, reaches the 2,501-node cap at N=40 and N=60, and times out after 2,333 expansions at N=80.

E0 is a reproducibility anchor, not the primary causal result.

## E1 — definitive controlled mechanism benchmark

**12,600 method–planner evaluations**, with 30 paired mission instances per N×ρ cell. The key falsification control is same-cardinality core-preserving Random-core: reducing action count alone cannot explain the result.

GSC matches the generator-owned eligibility oracle in every tested cell:

- semantic precision = **1.000**;
- semantic recall = **1.000**.

At **N=640, ρ=0.05**:

- blind search: GSC 30/30 solved; Random-core 20/30; State-aware 0/30; Full-domain 0/30;
- A*: all solve, but median generated nodes are GSC 4, Random-core 31, State-aware 308, Full-domain 612.

At ρ=1 the advantage disappears as pre-specified because all actions are admissible.

## E2 — state-conditioned truthfulness

- reliable observation added → detection is omitted and the plan shortens;
- primary provider failure → failed provider leaves the compiled domain and a backup is selected;
- essential capability loss → Readiness blocks planning;
- G0 unsafe fact → Readiness blocks entry;
- L2 authorization revoked → authorization-dependent action remains representable but the current problem becomes unsolvable;
- revision-only metadata change → old plan is rejected even if replanning returns the same action sequence.

The last case exposes a deliberate limitation: global freshness is fail-closed but over-conservative.

## E3 — component ablations

**5,400 trials.** Across authorization revocation, selected-provider failure, target change, and unknown-action injection:

- Full GSC: **0/400 false allows**;
- − freshness fence: **100/400 false allows**;
- − post-plan validator: **400/400 false allows**.

Additional diagnostics:

- − Readiness: **200/200 unnecessary planner invocations** across missing-capability + G0 entry cases;
- − compile-time safety: plan appears in **100/100** safety-blocked cases; mean **1.99 invalid Provider–Action instances/trial** enter the planning domain;
- − rejection reasons: provenance coverage falls from **100% to 0%**;
- full global freshness: **100/100 revision-only false blocks**.

## E4 — configuration-only transfer

Five-phase SAR/inspection configuration:

`Locate → Inspect → MapAccess → Relay → DeliverAid`

No domain-specific branch was added; generic core SHA-256 remained unchanged. Across **800 trials per domain**:

- decision-relevant false allow/block: **0/600; 0/600 per domain**;
- selected-provider failure recovery: **66/100 overall**, **66/66 when redundancy ≥2**;
- revision-only false block: **100/100**.

This supports portability within the shared `Mission → Capability → Provider → Action` abstraction, not unrestricted domain generality.

## E5 — public-topology stress test

E5 is deliberately no longer called the final external-validity gate. It uses public IPC-3 Rovers tasks 03, 05, and 07 with a separately implemented generic STRIPS planner, but the runtime governance masks remain study-authored.

Total: **1,800 runs**.

At q=0:

| Task | Full ops | GSC ops | GSC valid | Random-core valid | GSC generated | Full generated | Reduction |
|---|---:|---:|---:|---:|---:|---:|---:|
| 03 | 60 | 57 | 30/30 | 27/30 | 67 | 109 | 38.5% |
| 05 | 141 | 111 | 30/30 | 6/30 | 175 | 321 | 45.5% |
| 07 | 153 | 113 | 30/30 | 30/30 | 107 | 321 | 66.7% |

At q=1 all methods converge as pre-specified.

---

# 6. E6 independent external-validity program

## E6a — Satellite pilot

A frozen IPC-3 Satellite native-semantic pilot was completed. Post-freeze audit showed that required modes quickly covered nearly all instruments and every satellite, leaving too little provider selectivity. The pilot is retained transparently rather than post-hoc changing rules to manufacture pruning.

## E6b — confirmatory Rovers holdout

### Frozen corpus

IPC-3 Rovers **p09–p20**, held out from E5.

Benchmark commit:

`aibasel/downward-benchmarks@e21d49c2cb61d147a46c5966f2581bf6fd422b9f`

No synthetic governance mask is added.

### Native semantic source

Admission is derived only from public PDDL facts such as `equipped_for_*`, `store_of`, `on_board`, `supports`, `calibration_target`, `can_traverse`, `visible`, `visible_from`, initial positions, and original mission-output goals.

### Independent oracle evidence

The frozen rule is implemented independently by:

1. the Python compiler-side runner; and
2. a Node.js/JavaScript recursive S-expression parser with a separate intermediate representation.

Agreement is exact:

- **58/58 rovers admitted**;
- **60/65 cameras admitted**;
- **47/58 stores admitted**;
- **136 native mission-output goals**;
- **0 uncovered goals**;
- **0 object-level admission mismatches**.

Fail-closed checks also pass: deleting an expected camera label triggers mismatch; modifying the manifest triggers SHA-256 rejection; a two-rover fixture detects non-admitted provider exposure.

### Frozen planner/validator layer

- Fast Downward **26.6**;
- `--alias lama-first`;
- **300 s** per run;
- **4 GiB** per run;
- VAL commit `3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`;
- GSC plans validated against the **original unmodified public PDDL**.

### Frozen PASS criteria

E6b passes only if all hold:

1. source identities verified;
2. independent-oracle mismatch = 0;
3. Fast Downward reports 26.6;
4. VAL checkout matches the frozen commit;
5. at least **10/12 Full-domain problems solved** under the fixed cap;
6. Full-solved → GSC-unsolved regressions = **0**;
7. VAL failures for returned GSC plans = **0**;
8. non-admitted-provider action exposure = **0**.

Search time, generated nodes, and plan length are secondary diagnostics. **A speedup is not required for PASS.** If fewer than 10 Full problems are evaluable, status is `INCONCLUSIVE`.

### Execution history

- **2026-09-23:** local sandbox attempt stopped before planner outcomes because Fast Downward/VAL were absent and outbound network was blocked. Recorded as `NOT EXECUTED`, not scientific FAIL/INCONCLUSIVE.
- **2026-10-08, GitHub run #1:** workflow startup failed before any job was instantiated because the initial CI file used runner context at job-level environment definition. This is infrastructure-only; no scientific outcome was opened.
- **2026-10-08, GitHub run #2:** startup issue corrected without changing any frozen scientific parameter. The `frozen-e6b` GitHub-hosted Linux job entered normal execution. Final scientific status must come only from the frozen `gate_summary.json`.

---

# 7. Evidence ladder

```text
E0  Reproducibility
 ↓
E1  Controlled mechanism evidence
 ↓
E2  State-conditioned truthfulness
 ↓
E3  Component necessity / failure modes
 ↓
E4  Configuration-level portability
 ↓
E5  External planning topology
 ↓
E6b Native public semantics + independent oracle
 ↓
[Executing] Fast Downward 26.6 + VAL confirmatory gate
```

The strength of the manuscript claim follows the highest completed rung, not the most ambitious planned rung.

---

# 8. Main interpretation

> A persistent semantic library should not be treated directly as the executable planning domain. A mission-conditioned compilation boundary can make provider–action membership explicit, auditable, state-bound, and empirically testable. Controlled and public-topology experiments show that selecting a semantically coherent action subset can reduce invalid or distracting alternatives while preserving mission-relevant structure.

The manuscript is strongest when it remains focused on **domain admission as a first-class governance object** rather than planner speed.

---

# 9. Limitations

1. Completed experiments are software/formal-model or parameterized synthetic evaluations.
2. E4's second domain is synthetic and intentionally shares the same abstraction.
3. E5 governance overlays are experimenter-authored.
4. E6b uses independently authored executable capability/state predicates, not externally authored binary safety-policy labels.
5. Current global snapshot freshness over-blocks revision-only changes.
6. Planner performance remains heuristic- and topology-dependent.
7. No claim is made about real detection, physical effects, network latency, operational safety, or field effectiveness.

---

# 10. Reproducibility and GitHub execution

The frozen E6b research bundle is byte-preserved under `e6b/bundle_parts/`. The reconstructed ZIP must equal:

`SHA256 8ff25602bcabc58eed52b781d882d51966dd02dc28b02ebf77db1166ca59d9ac`

`e6b/README.md` records the six part hashes, bundle contents, frozen external identities, and PASS criteria. `.github/workflows/e6b-confirmatory.yml` reconstructs and verifies the package before it can reach the planner stage.

Required scientific return files include:

- `gate_summary.json`
- `paired_results.csv`
- `static_audit.csv`
- `independent_oracle_check.json`
- `toolchain_identity.json`
- `source_identity.json`

No corpus, rule, alias, resource cap, validator commit, or threshold may be altered after observing outcomes.

---

# 11. Collaboration guide

New collaborators should read in this order:

1. this Master, Sections 1–3;
2. evidence Sections 4–6;
3. `e6b/README.md`;
4. the frozen E6b protocol and Runbook reconstructed from the byte-preserved bundle;
5. the manuscript integration patch only after the gate result is known.

CI infrastructure problems must be fixed only at the execution/container layer. Scientific logic is frozen.

---

# 12. Next research action

1. Complete GitHub Actions run #2.
2. Retrieve and audit the raw artifact.
3. Classify E6b strictly as `PASS`, `FAIL`, or `INCONCLUSIVE` from `gate_summary.json`.
4. Update this Master first.
5. Synchronize `docs/index.html`.
6. Update the root README.
7. Apply only the result-compatible conditional manuscript patch.
8. Run a final claim–method–result consistency audit.

Do not add another experiment unless E6b exposes a specific unresolved methodological question.

---

# 13. Changelog

## v1.2 — 2026-10-08

- Established `qiangruhuang/Tianshu` as the canonical collaboration repository.
- Added byte-preserved frozen E6b research package with SHA-256 verification.
- Added GitHub Actions execution route for the frozen Fast Downward 26.6 + VAL gate.
- Separated CI infrastructure status from scientific PASS/FAIL/INCONCLUSIVE.
- Recorded run #1 as startup infrastructure failure with no planner outcome opened.
- Corrected only the workflow execution context and started run #2 under unchanged scientific parameters.
- Continued the maintenance contract: **Master Markdown → HTML → GitHub synchronization**.

## v1.1 — 2026-09-23

- Recorded the sandbox pre-execution environment block while preserving outcome blindness.
- Added the independent JavaScript oracle and fail-closed tests.

## v1.0 — 2026-09-23

- Created the project-level single source of truth.
- Consolidated E0–E5 evidence and E6a/E6b external-validity program.
