# Governed Semantic Compilation (GSC) — Project Master

> **Paper 1:** Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning  
> **Repository:** `https://github.com/qiangruhuang/Tianshu`  
> **Master version:** v1.9  
> **Last updated:** 2026-10-09  
> **Current phase:** RAS manuscript narrative finalized with anti-defensive + Nature-style restructuring; human author metadata / immutable release decision / final portal packaging pending  
> **Current full manuscript:** `Paper1_Manuscript_v0.6.0_RAS_AntiDefensive_Nature.md`  
> **Role:** single source of truth for research status, claim boundaries, reproducibility, and submission state.

---

## 0. Maintenance contract

1. Update this Master first, then synchronize `docs/index.html`.
2. Never silently reinterpret a completed experiment.
3. Preserve null/negative results when they define the claim boundary.
4. Frozen protocols change only through an explicit new version.
5. CI/infrastructure status is distinct from scientific PASS/FAIL/INCONCLUSIVE.
6. Do not add a benchmark merely to recover a preferred effect direction.
7. The Paper 1 experimental program is closed unless a later reviewer identifies a concrete claim–evidence gap that cannot be removed or supported using existing evidence.
8. DOCX/PDF generation remains outside the research phase until manuscript content is explicitly approved.

---

# 1. Research question and final storyline

**Research question:** when a system knows many possible providers and actions, which Provider–Action instances should be admitted into the planner for this mission, under the current state and policy, before search begins?

GSC treats **mission-conditioned Provider–Action domain membership** as an explicit governance artifact between persistent semantic knowledge and planner search:

```text
Persistent semantics + mission + current operational state
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

**Final storyline:**

> **correct governed domain synthesis + conditional computational benefit**

GSC is not claimed as a new search algorithm, a generic ontology-to-PDDL contribution, or a universal planning-speedup method.

---

# 2. Final claim boundary

## Supported

1. Mission-conditioned Provider–Action admission is implementable as a separate planning boundary.
2. E1 shows that semantically coherent action selection reduces search pollution beyond the trivial effect of selecting fewer actions under the controlled benchmark.
3. E3 shows that Readiness, compile-time safety admission, freshness, validation, and rejection provenance have separable roles.
4. E4 transfers the unchanged generic runtime core from the original C-UAS fixture to a five-phase SAR/inspection configuration without a domain-specific runtime branch.
5. E5 shows that the controlled search-pollution direction can survive public planning topology when governance-invalid alternatives remain in the effective planner representation.
6. **E6b passes the frozen confirmatory external-validity gate** on held-out public native semantics using a cross-implementation admission oracle, Fast Downward 26.6, and VAL.
7. E6b supports solvability preservation, returned-plan validity, non-admitted-provider exclusion, and external planner/validator independence on the frozen Rovers holdout.

## Not supported

- universal planning-complexity reduction;
- planner-independent speedup;
- a claim that GSC must reduce search under mature planners;
- field safety or physical performance;
- sensing/effect effectiveness;
- unrestricted cross-domain autonomy;
- optimal freshness/revalidation;
- independently authored field safety/authorization labels for E6b.

---

# 3. Evidence chain

| Experiment | Evidence | Final status |
|---|---|---|
| E0 | frozen prototype regression | **Complete** |
| E1 | 12,600 controlled method–planner evaluations | **Complete** |
| E2 | deterministic state perturbations | **Complete** |
| E3 | 5,400 component-ablation trials | **Complete** |
| E4 | configuration-only five-phase transfer | **Complete** |
| E5 | IPC-3 Rovers public-topology stress test | **Complete** |
| E6a | Satellite native-semantic pilot | **Complete pilot; insufficient selectivity** |
| E6b | held-out native Rovers + cross-implementation oracle + Fast Downward + VAL | **PASS — run 37713826709** |

---

# 4. Core results

## E1 — controlled mechanism

At `N=640, rho=0.05`:

- blind search solved: GSC 30/30; Random-core 20/30; State-aware 0/30; Full-domain 0/30;
- A* median generated nodes: GSC 4; Random-core 31; State-aware 308; Full-domain 612;
- GSC semantic precision = recall = 1.000 across tested cells;
- at `rho=1`, methods converge as prespecified.

Same-cardinality Random-core is the key falsification: the effect is not explained by action count alone.

## E3 — component necessity

Across 5,400 trials:

- Full GSC: 0/400 false allows across four post-plan challenge classes;
- without freshness: 100/400 false allows;
- without validator: 400/400 false allows;
- without Readiness: 200/200 unnecessary planner calls in missing-capability/G0 cases;
- without compile-time safety gating: safety-blocked case produces a plan in 100/100 trials and mean 1.99 invalid Provider–Action instances/trial enter the domain;
- global freshness causes 100/100 false blocks under revision-only changes.

## E4 — configuration-only transfer

Five-stage transfer configuration:

`Locate → Inspect → MapAccess → Relay → DeliverAid`

The generic runtime core SHA-256 remains unchanged and no domain-specific runtime branch is added. Across 800 trials/domain, decision-relevant false allow/block is 0/600 per domain; selected-provider-failure recovery is 66/66 when redundancy ≥2.

## E5 — public-topology stress test

IPC-3 Rovers 03/05/07, 1,800 runs, study-authored masks, separate clean-room planner.

At q=0, median generated-node reductions vs Full-domain are:

- task 03: 38.5%
- task 05: 45.5%
- task 07: 66.7%

At q=1 methods converge. E5 is **not** independent semantic validation.

---

# 5. E6b confirmatory external-validity gate

## Frozen design

- holdout: IPC-3 Rovers p09–p20;
- benchmark commit: `e21d49c2cb61d147a46c5966f2581bf6fd422b9f`;
- no synthetic runtime governance mask;
- native public PDDL capability/state semantics;
- Python compiler path vs separately implemented JavaScript S-expression admission path;
- Fast Downward 26.6, `--alias lama-first`, 300 s/run, 4 GiB/run;
- VAL commit `3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`;
- returned GSC plans validated against original unmodified public PDDL.

## Static/native-semantic evidence

- rovers: 58/58 admitted;
- cameras: 60/65 admitted;
- stores: 47/58 admitted;
- total: 165/181 admitted; **16/181 excluded = 8.84%**;
- native goals: 136;
- uncovered goals: 0;
- cross-implementation admission mismatches: 0.

## Confirmatory result

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

Reproducibility identity:

- GitHub Actions run `37713826709`;
- artifact ID `11522843338`;
- artifact ZIP SHA-256 `36fc77b08100eb655ab575c8ca1c70f6a349f373cf19d38994b6bfb9b814d5a8`.

---

# 6. Mature-planner boundary result

E6b's secondary performance endpoint is a clean null.

Full and GSC are identical in 12/12 pairs for:

- translator variables/facts/operators/task size;
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
- median wall time: Full 0.1275 s; GSC 0.1246 s;
- GSC faster in 6/12 wall-time pairs and slower in 6/12.

Interpretation: Fast Downward translation/relevance preprocessing removes the same native-goal-irrelevant structures that GSC removes upstream. E5 and E6b are therefore not contradictory.

**Computational claim:**

> Semantic admission can reduce search pollution when irrelevant structure survives planner preprocessing. It is not a planner-independent complexity reduction.

---

# 7. Current submission package — RAS

**Primary target:** *Robotics and Autonomous Systems*.

Current authoritative full manuscript:

- `Paper1_Manuscript_v0.6.0_RAS_AntiDefensive_Nature.md`
- SHA-256: `7d20b5f09a0f335834fb1a2fcc92460de7f13a789ce796f5ba6c13bf6dee2298`
- v0.6.0 applies anti-defensive-writing, Nature-style argument restructuring, and Nature-style language polishing while preserving all experiments, numbers, frozen gates, references, and claim boundaries.

RAS-facing state:

- abstract: **236 words**;
- keywords: **7**;
- highlights: **5**, each **70–79 characters**, satisfying Elsevier's ≤85-character general highlight guidance;
- current references: 19, all used in text and no missing citation numbers;
- final 2026 literature refresh complete;
- adversarial review complete: **no new experiment required**;
- pre-layout copy-edit gate: **PASS**;
- Data/Code Availability statement complete;
- submission metadata package complete;
- cover letter draft complete;
- graphical-abstract brief complete;
- submission checklist complete;
- supplementary/reproducibility material complete;
- author/declaration packet complete with unresolved human metadata explicitly marked;
- generative-AI disclosure inserted in the candidate manuscript;
- pre-submission immutable-release manifest prepared.

GitHub manuscript assets:

- `research/manuscript/Paper1_CURRENT_v1.2.md`
- `research/manuscript/Paper1_v0.5.2_RAS_Compliance_Delta.md`
- `research/manuscript/Paper1_v0.5.3_Copyedit_Delta.md`
- `research/manuscript/Paper1_RAS_Copyedit_Gate_v1.0.md`
- `research/manuscript/Paper1_RAS_Submission_Metadata_v1.0.md`
- `research/manuscript/Paper1_Data_Code_Availability_v1.0.md`
- `research/manuscript/Paper1_RAS_Highlights_v1.1.txt`
- `research/manuscript/Paper1_RAS_Cover_Letter_v0.1.md`
- `research/manuscript/Paper1_RAS_Graphical_Abstract_Brief_v1.0.md`
- `research/manuscript/Paper1_RAS_Submission_Checklist_v1.0.md`
- `research/manuscript/Paper1_Claim_Evidence_Citation_Audit_v1.0.md`
- `research/manuscript/Paper1_Manuscript_v0.6.0_RAS_AntiDefensive_Nature.md`
- `research/manuscript/Paper1_v0.6.0_AntiDefensive_Nature_Rewrite_Audit.md`
- `research/manuscript/Paper1_Supplementary_Material_v1.0.md`
- `research/manuscript/Paper1_RAS_Declarations_Author_Metadata_v1.0.md`
- `research/manuscript/Paper1_PreSubmission_Release_Manifest_v1.0.md`

---

# 8. Figures

Main figure sequence is frozen:

1. GSC architecture;
2. E1 same-cardinality mechanism evidence;
3. E5 public-topology conditional search reduction;
4. E6b native provider admission/selectivity;
5. E6b mature-planner null.

Current generator:

- `research/figures/generate_paper_figures_v1_2.py`

Submission figure sources are generated as PNG previews plus **PDF/EPS vector files** and have passed render-back visual inspection.

Figure philosophy: mechanism → public topology → external semantics → mature-planner boundary. The mature-planner null stays in the main paper.

---

# 9. Final literature/novelty position

2026-10-08 literature refresh adds two particularly close recent neighbours:

- Jørgensen & Ma (2026): bounded enterprise action governance;
- An et al. (2026): ontology/SWRL → PDDL autonomous-driving mission planning.

They narrow the novelty claim but do not trigger the novelty hard-stop.

GSC does **not** claim ontology-to-PDDL integration, semantic validity, generic governed execution, or stale-plan validation in general as novel. The retained contribution is:

> mission-conditioned heterogeneous Provider–Action planning-domain membership as a first-class governance boundary, together with direct mechanism testing and a held-out native-semantic external gate.

---

# 10. Data/code availability

Recommended statement is maintained in:

`research/manuscript/Paper1_Data_Code_Availability_v1.0.md`.

The public repository contains frozen protocols, reproducibility workflows, E6b result summaries, and figure-generation scripts. Third-party benchmark/tool sources remain under their upstream repositories and licenses; this project records version-pinned identities and reproducible fetch/build paths rather than claiming redistribution ownership.

The study contains no human-participant or animal data.

---

# 11. Remaining work before submission

Scientific work remaining: **none**, unless a later reviewer identifies a specific unresolved claim–evidence gap.

Submission work remaining:

The scientific/reproducibility package is now frozen. Remaining items require human author decisions rather than additional research:

1. author names/order and affiliations;
2. corresponding-author details;
3. funding/grant statement;
4. CRediT author contributions;
5. competing-interest declaration;
6. optional acknowledgements;
7. decide whether to mint a repository release/DOI before submission;
8. perform the final live RAS portal requirement check;
9. explicitly approve content before DOCX/PDF manuscript generation.

Reference punctuation/house-style normalization is not a hard blocker under Elsevier's current Your Paper Your Way guidance; figure source-format compliance is complete with EPS/PDF outputs.

---

# 12. Evidence boundary

All evidence remains software/formal-model, parameterized synthetic, or public planning-benchmark evidence. E4's second domain is synthetic; E5 masks are study-authored; E6b native semantics are not independently authored field safety/authorization labels; E6b selectivity is modest; global freshness is conservative; and no field-performance or physical-safety claim is made.

---

# 13. Changelog

## v1.9 — 2026-10-09

- Applied the user-requested anti-defensive-writing skill and Nature writing/polishing workflow to the full manuscript.
- Reorganized the paper around the strongest defensible value: mission-conditioned Provider–Action membership as an auditable runtime contract.
- Removed reviewer-facing self-audit and defensive novelty disclaimers while preserving all conclusion-changing evidence and scope boundaries.
- Reframed the E6b mature-planner null as the mechanism boundary created by downstream planner preprocessing.
- Replaced the long Threats-to-validity inventory with claim-specific `Scope of inference`.
- Completed claim/evidence/reference regression and submission-layout QA; no scientific result changed.
- Promoted `Paper1_Manuscript_v0.6.0_RAS_AntiDefensive_Nature.md` as the current writing candidate.

## v1.8 — 2026-10-08

- Promoted `Paper1_Manuscript_v0.5.4_RAS.md` to the current candidate manuscript.
- Added Elsevier-compatible generative-AI disclosure immediately before References.
- Added `Paper1_Supplementary_Material_v1.0.md` with frozen E1/E3/E4/E5 details and the 12-instance E6b paired table.
- Added a human-signoff declarations/author-metadata packet covering CRediT, funding, COI, ethics, data/code, and AI use.
- Added a pre-submission release manifest with SHA-256 identities; no immutable release/DOI has been minted yet.
- Confirmed current Elsevier policy: substantive generative-AI manuscript assistance should be disclosed; AI-generated graphical abstracts are not used in this project.
- Remaining blockers are now exclusively human metadata, release/DOI decision, portal check, and explicit approval before DOCX/PDF generation.

## v1.7.2 — 2026-10-08

- Completed RAS/Elsevier submission-compliance gate: PASS with author-metadata blockers only.
- Downgraded reference house-style normalization from pre-submission blocker to live-portal/proof-stage check under Your Paper Your Way.
- Upgraded figure generator to v1.2 with PNG preview + PDF/EPS vector outputs.
- Rendered all five PDF figures back to images and visually verified them.
- Added submission checklist v1.1.
- Current remaining blockers are author/funding/CRediT/COI metadata, optional repository release/DOI, and final live portal packaging.

## v1.7.1 — 2026-10-08

- Promoted v0.5.3 RAS to authoritative pre-layout candidate.
- Copy-edit gate PASS: no scientific or structural rewrite required.
- Standardized E6b as confirmatory external-validity gate and cross-implementation admission oracle.
- Integrated the isolated Figure 1 callout; no method/result/claim changes.
- Updated authoritative manuscript SHA-256 and Abstract count to 236 words.

## v1.7 — 2026-10-08

- Made v0.5.2 RAS the authoritative current manuscript.
- Recorded full-manuscript SHA-256 and added `Paper1_CURRENT_v1.2.md`.
- Added RAS submission metadata and Data/Code Availability statement.
- Added publication figure generator v1.1.
- Confirmed 235-word abstract, seven keywords, and five <=85-character Highlights.
- Reconfirmed all 19 references are used with no missing citation numbers.
- Moved project status from manuscript consolidation to **RAS submission preparation**.

## v1.6 — 2026-10-08

- E6b PASS, mature-planner null, literature refresh, adversarial review, figure freeze, and target-venue decision consolidated.
