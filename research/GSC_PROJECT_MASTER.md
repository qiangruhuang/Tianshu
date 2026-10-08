# Governed Semantic Compilation (GSC) — Project Master

> **Paper 1:** Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning  
> **Repository:** `qiangruhuang/Tianshu`  
> **Master version:** v1.3  
> **Last updated:** 2026-10-08  
> **Role:** single source of truth for research status, evidence level, locked decisions, reproducibility, and next actions.

## 0. Maintenance contract

1. Update this Markdown first.
2. Never overwrite or silently reinterpret a completed experiment.
3. A frozen protocol may change only by creating a new version and documenting why.
4. Synchronize `docs/index.html` only after this Master is updated.
5. A gate is reported as PASS only when its frozen execution actually produces that result.
6. CI infrastructure failures are not scientific FAIL/INCONCLUSIVE results.
7. DOCX/PDF generation remains outside the research phase until the research content is explicitly approved.

Canonical repository layout:

- `research/GSC_PROJECT_MASTER.md` — research truth;
- `docs/index.html` — maintained visual panorama;
- `e6b/` — byte-preserved frozen E6b assets and execution documentation;
- `e6b/results/run-37713826709/` — primary confirmatory result files;
- `.github/workflows/e6b-confirmatory.yml` — confirmatory execution environment.

---

# 1. Research question

**When a system knows many possible providers and actions, which provider–action instances should be admitted into the planner for this mission, under the current state and policy, before search begins?**

Persistent semantic knowledge and executable planning have different requirements. An ontology or knowledge graph can contain reusable capabilities, multiple providers, general action templates, stable policies, and incomplete/open-world knowledge. A planner instead requires a bounded current problem: which providers are healthy now, which facts are trusted now, which safety/authorization conditions apply now, and which provider–action instances should enter this particular planning domain.

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

# 3. Claim boundary after E6b

## Supported by completed evidence

1. Mission-conditioned Provider–Action admission is implementable as a separate planning boundary.
2. In the controlled E1 mechanism benchmark, semantically coherent admission reduces search pollution beyond the trivial effect of reducing action count.
3. Readiness, compile-time safety admission, freshness binding, post-plan validation, and rejection provenance have distinct measurable roles.
4. The same core runtime transfers without a domain-specific branch from the C-UAS fixture to a five-phase SAR/inspection configuration.
5. E5 shows that the controlled search-reduction direction is not confined to the original four-stage synthetic topology, although E5 still uses study-authored governance masks and a clean-room planner.
6. **E6b PASSED the frozen independent external-validity gate:** held-out public native semantics, independent cross-implementation oracle, Fast Downward 26.6, and independently built VAL all agreed with zero semantic/solvability/validation regressions.
7. E6b therefore supports **semantic soundness, solvability preservation, provider-exposure safety, and planner/validator independence** for the frozen Rovers holdout.

## Not supported

- universal planning-complexity reduction;
- planner-independent speedup;
- a claim that GSC must reduce search under a mature planner;
- field safety or physical performance;
- sensing or effect effectiveness;
- unrestricted cross-domain autonomy;
- optimal freshness/revalidation;
- independent human-authored binary safety-policy labels for E6b.

A key E6b negative result is scientifically important: under Fast Downward 26.6, Full and GSC produce identical translated problem sizes, search counts, plan lengths, and final plans on all 12 holdout instances. The external gate therefore validates semantic preservation rather than universal performance gain.

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
| E6b | Does frozen admission preserve native public semantics with independent oracle/planner/validator? | independent external-validity gate | **PASS — run 37713826709** |

---

# 5. Key pre-E6 results

## E0 — frozen regression

For global template counts 20, 40, 60, and 80, GSC compiles to **6 actions in every case**. Pruning ratios are 70.0%, 85.0%, 90.0%, and 92.5%. The compiled reference planner requires 4 expansions in all four cases; the ungated baseline requires 714 expansions at N=20, reaches the 2,501-node cap at N=40 and N=60, and times out after 2,333 expansions at N=80.

## E1 — definitive controlled mechanism benchmark

**12,600 method–planner evaluations**, with 30 paired mission instances per N×ρ cell. Same-cardinality core-preserving Random-core is the main falsification control.

GSC matches the generator-owned eligibility oracle in every tested cell:

- semantic precision = **1.000**;
- semantic recall = **1.000**.

At **N=640, ρ=0.05**:

- blind search: GSC 30/30 solved; Random-core 20/30; State-aware 0/30; Full-domain 0/30;
- A*: all solve, but median generated nodes are GSC 4, Random-core 31, State-aware 308, Full-domain 612.

At ρ=1 the advantage disappears as pre-specified.

## E2 — state-conditioned truthfulness

- reliable observation added → detection omitted and plan shortens;
- primary provider failure → failed provider leaves the compiled domain and backup is selected;
- essential capability loss → Readiness blocks planning;
- G0 unsafe fact → Readiness blocks entry;
- L2 authorization revoked → current problem becomes unsolvable;
- revision-only metadata change → old plan rejected even if replanning returns the same action sequence.

The last case exposes the deliberate limitation that global freshness is fail-closed but over-conservative.

## E3 — component ablations

**5,400 trials.** Across authorization revocation, selected-provider failure, target change, and unknown-action injection:

- Full GSC: **0/400 false allows**;
- − freshness fence: **100/400 false allows**;
- − post-plan validator: **400/400 false allows**.

Additional diagnostics:

- − Readiness: **200/200 unnecessary planner invocations**;
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

## E5 — public-topology stress test

E5 uses public IPC-3 Rovers tasks 03, 05, and 07 with a separately implemented generic STRIPS planner but study-authored governance masks. Total: **1,800 runs**.

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

The frozen IPC-3 Satellite pilot was retained transparently after post-freeze audit showed too little provider selectivity for a strong confirmatory gate. No rule was changed to manufacture pruning.

## E6b — confirmatory Rovers holdout

### Frozen design

- Holdout: IPC-3 Rovers `p09`–`p20`, not used in E5.
- Benchmark commit: `aibasel/downward-benchmarks@e21d49c2cb61d147a46c5966f2581bf6fd422b9f`.
- No synthetic governance mask.
- Independent oracle: Python compiler path vs Node.js/JavaScript S-expression implementation.
- Fast Downward: **26.6**, `--alias lama-first`, 300 s/run, 4 GiB/run.
- VAL: commit `3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`.
- GSC plans validated against the **original unmodified public PDDL**.

Static/oracle evidence before planner outcomes:

- 58/58 rovers admitted;
- 60/65 cameras admitted;
- 47/58 stores admitted;
- 136 native mission-output goals;
- 0 uncovered goals;
- 0 object-level independent-oracle mismatches.

### Confirmatory execution

GitHub Actions run: **37713826709**  
Head commit: `64c3f66cf95951fac180487b18a26d78e681507b`  
Artifact ID: **11522843338**  
Artifact ZIP SHA-256: `36fc77b08100eb655ab575c8ca1c70f6a349f373cf19d38994b6bfb9b814d5a8`

Frozen `gate_summary.json` result:

```text
status                                      PASS
source_identity_mismatches                     0
admission_serialization_mismatches              0
independent_oracle_mismatches                   0
uncovered_native_goals                          0
Fast Downward 26.6 verified                  true
VAL source commit verified                   true
Full-domain evaluable                         12/12
Full-solved -> GSC-unsolved regressions          0
GSC VAL failures                                0
non-admitted action exposures                   0
required minimum Full evaluable               10/12
```

**Scientific conclusion: E6b PASS.**

All 12 Full and all 12 GSC problems solved within the frozen resource cap. Every GSC returned plan validated under VAL against the original public domain/problem, and no plan exposed a non-admitted provider.

### Secondary performance result: mature-planner null effect

The frozen protocol explicitly treated performance as secondary. The result is a clean null:

- Full vs GSC translator facts: **identical in 12/12**;
- Full vs GSC translator operators: **identical in 12/12**;
- Full vs GSC translator variables: **identical in 12/12**;
- expanded states: **identical in 12/12**;
- generated states: **identical in 12/12**;
- plan length: **identical in 12/12**;
- `sas_plan` bytes: **identical in 12/12**.

Across the 12 pairs:

- median generated states: Full = GSC = **4,863.5**;
- median expanded states: Full = GSC = **145**;
- median plan length: Full = GSC = **45**;
- median wall time: Full **0.1275 s**, GSC **0.1246 s**;
- GSC wall time was lower on 6 instances and higher on 6, consistent with runtime noise rather than a stable speed effect.

Interpretation: the 5 excluded cameras and 11 excluded stores do not change the final Fast Downward translated/search problem on this holdout. The logs are consistent with Fast Downward translation/preprocessing already eliminating the irrelevant alternatives before search. E6b therefore closes the external **semantic correctness / solvability / validation** gate, while simultaneously limiting the search-efficiency claim to planner/topology regimes where governance-invalid alternatives survive preprocessing.

This is not a weakness to hide. It makes the paper's claim more precise and reviewer-defensible.

### Execution audit trail

- 2026-09-23 local sandbox: `NOT EXECUTED`; toolchain/network blocked before outcomes.
- GitHub run #1: workflow startup context failure; no job/outcome.
- run #2: bundle reconstruction mismatch exposed an upload error; no outcome.
- run #3: reconstructed ZIP identity passed; frozen absolute-path manifest was non-portable; no outcome.
- run #4: bundle, benchmark, and Fast Downward 26.6 passed; VAL build was called without its required positional arguments; no outcome.
- **run #5: all infrastructure, identity, oracle, audit, planner, VAL, and final status steps passed; E6b scientific status = PASS.**

Only execution/container-layer fixes were made across runs #1–#5. The frozen bundle SHA, benchmark corpus, admission rule, planner version/alias, resource caps, VAL commit, and PASS criteria did not change.

---

# 7. Evidence ladder — closed for Paper 1

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
E5  External planning topology                          COMPLETE
 ↓
E6b Native public semantics + independent oracle        COMPLETE
 ↓
Fast Downward 26.6 + frozen VAL confirmatory gate       PASS
```

For Paper 1, the planned external-validity evidence chain is now closed. Additional experiments should not be added unless manuscript-level adversarial review identifies a specific unresolved claim-evidence gap.

---

# 8. Main scientific interpretation after E6b

> A persistent semantic library should not be treated directly as the executable planning domain. GSC makes mission-conditioned Provider–Action membership explicit, auditable, state-bound, and independently testable. Controlled experiments show that semantic admission can reduce search pollution when inadmissible alternatives survive into search. The independent E6b holdout shows that the same admission logic preserves native public-task solvability and plan validity under a mature third-party planner and independent validator. It does not show a universal search-speed advantage, because Fast Downward preprocessing collapses Full and GSC to the same effective search problem on this holdout.

The strongest story is therefore **correct governed domain synthesis**, with conditional computational benefit—not “GSC is a faster planner.”

---

# 9. Limitations

1. All evidence remains software/formal-model or parameterized synthetic/public-benchmark evidence, not field validation.
2. E4's second domain is synthetic and shares the same abstraction.
3. E5 governance overlays are study-authored.
4. E6b uses independently authored executable capability/state predicates, not independent human-authored binary safety-policy labels.
5. Current global freshness over-blocks revision-only changes.
6. E6b provides no mature-planner search reduction on p09–p20; performance benefit is conditional on planner preprocessing and problem topology.
7. No claim is made about real sensing, physical effects, network latency, operational safety, or field effectiveness.

---

# 10. Reproducibility

Frozen E6b input bundle SHA-256:

`8ff25602bcabc58eed52b781d882d51966dd02dc28b02ebf77db1166ca59d9ac`

Successful result artifact SHA-256:

`36fc77b08100eb655ab575c8ca1c70f6a349f373cf19d38994b6bfb9b814d5a8`

Primary result files are maintained under `e6b/results/run-37713826709/`. The GitHub Actions artifact preserves all plans, planner logs, VAL logs, admission manifests, and compiled PDDL for the run.

Required scientific outputs:

- `gate_summary.json`
- `paired_results.csv`
- `static_audit.csv`
- `independent_oracle_check.json`
- `toolchain_identity.json`
- `source_identity.json`

---

# 11. Collaboration guide

New collaborators should read:

1. Sections 1–3 of this Master;
2. E1/E3/E5/E6b evidence in Sections 5–6;
3. `e6b/README.md`;
4. `e6b/results/run-37713826709/E6b_RESULT_REPORT.md`;
5. the frozen protocol/Runbook reconstructed from `e6b/bundle_parts/`.

The main collaboration question is no longer “can E6b run?” It is now how to integrate the closed evidence chain into a concise paper without overstating the conditional performance effect.

---

# 12. Next research action

Do **not** add another benchmark automatically.

Next phase:

1. freeze E6b observed-results wording;
2. integrate E6b into Methods, Results, Discussion, Threats to Validity, Conclusion, and Abstract;
3. revise E5 wording from “external-validity gate” to “public-topology stress test” throughout;
4. explicitly report the E6b mature-planner null performance result;
5. run a final Claim–Evidence–Citation / method–result consistency audit;
6. perform adversarial reviewer review of the complete Paper 1 story;
7. only then decide whether any additional experiment is genuinely necessary.

---

# 13. Changelog

## v1.3 — 2026-10-08

- Completed frozen GitHub Actions E6b confirmatory execution, run `37713826709`.
- **E6b status = PASS** with 12/12 Full evaluable, zero solvability regressions, zero VAL failures, zero non-admitted action exposures, and zero oracle/source mismatches.
- Verified Fast Downward 26.6 and frozen VAL commit.
- Added the secondary null result: Full and GSC have identical translated/search counts and identical plans on all 12 holdout tasks.
- Narrowed the performance claim: E1/E5 search gains are conditional; E6b supports semantic correctness and preservation under a mature planner rather than universal speedup.
- Closed the planned Paper 1 external-validity evidence chain.

## v1.2 — 2026-10-08

- Established `qiangruhuang/Tianshu` as the canonical collaboration repository.
- Added byte-preserved frozen E6b package and GitHub Actions route.
- Separated CI infrastructure status from scientific status.

## v1.1 — 2026-09-23

- Preserved outcome blindness after the local sandbox pre-execution block.
- Added independent JavaScript oracle and fail-closed tests.

## v1.0 — 2026-09-23

- Created project-level single source of truth and consolidated E0–E6b design.
