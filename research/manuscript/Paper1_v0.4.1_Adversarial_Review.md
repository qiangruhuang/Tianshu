# Paper 1 v0.4.1 — Adversarial Reviewer Audit

**Manuscript:** *Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning*  
**Review date:** 2026-10-08  
**Evidence state:** E0–E5 complete; E6b confirmatory gate PASS  
**Review objective:** identify claim–evidence failures that could still justify new research before submission. This review is not intended to manufacture additional experiments after observing the E6b mature-planner null.

## Overall recommendation

**MINOR-TO-MODERATE MANUSCRIPT REVISION; NO NEW EXPERIMENT REQUIRED.**

The experimental program is sufficiently coherent for a bounded software/formal-model contribution. The strongest evidence is the combination of controlled same-cardinality falsification (E1), component necessity (E3), configuration-only transfer (E4), public-topology stress evidence (E5), and a prespecified held-out native-semantic gate with Fast Downward 26.6 and VAL (E6b).

The main submission risk is now **framing**, not missing experiment count. The manuscript is defensible if it consistently presents GSC as an explicit, auditable, mission-conditioned domain-admission boundary and presents search reduction as conditional.

---

## Concern A — Fast Downward already removes the same irrelevant structure. Why is GSC not redundant?

**Disposition: CLOSED at claim level.**

If the contribution were search pruning, E6b would substantially weaken it. The defensible distinction is architectural and semantic:

- Fast Downward optimizes an already constructed planning problem.
- GSC determines which Provider–Action instances are allowed to constitute that problem under current capability, availability, safety/policy, and authorization state.
- GSC produces rejection provenance and snapshot binding.
- Goal relevance is not equivalent to governance admissibility.

Keep the framing: **correct governed domain synthesis with conditional computational benefit**.

Do not claim a general planning complexity reduction or mature-planner speedup.

---

## Concern B — The E6b oracle is not independent policy ground truth

**Disposition: CLOSED after v0.4.1 terminology correction.**

The JavaScript oracle is independent at the implementation-path level but instantiates the same frozen study-defined adapter rule as the Python compiler.

Two independence claims must remain separate:

1. **semantic-source externality:** public IPC capabilities, connectivity, initial state, and mission goals;
2. **implementation-path independence:** separate Python and JavaScript parser/code paths.

Use “cross-implementation oracle” or “separately implemented admission oracle.” Do not call it an independently authored safety/policy oracle.

---

## Concern C — E6b external selectivity is modest

**Disposition: OPEN AS A LIMITATION, NOT A RESEARCH BLOCKER.**

E6b excludes:

- 5/65 cameras;
- 11/58 stores;
- 0/58 rovers.

Total exclusion = **16/181 provider-related objects = 8.84%**.

E6b is therefore strong evidence for no-loss external semantic admission and external toolchain validity, but not a high-selectivity external stress test. E5 supplies the selective public-topology regime, with its study-authored-mask limitation reported separately.

Do not add a new benchmark solely to obtain larger pruning.

---

## Concern D — E5 uses solution-preserving, study-authored masks

**Disposition: CLOSED BY RECLASSIFICATION.**

E5 is correctly presented as a **public-topology stress test**, not independent semantic validation. The known feasible reference plan and synthetic mask are useful for mechanism isolation but must remain explicit in Methods.

E6b supplies the stronger native-semantic/planner/validator externality.

---

## Concern E — E1 generator truth and compiler share the same conceptual eligibility vocabulary

**Disposition: BOUNDED, NOT FATAL.**

The generator owns labels independently of compiler output, but both derive from the study's formal eligibility specification. The result is strong controlled implementation/mechanism evidence, not universal semantic truth.

E6b partially mitigates this by moving facts/goals to an externally authored domain and adding a separate adapter implementation.

---

## Concern F — C-UAS framing may imply field/physical claims

**Disposition: CLOSED if current evidence-boundary language is retained.**

The manuscript must continue to state that it does not measure detection probability, physical engagement effectiveness, field safety, command latency, or operational performance.

The C-UAS configuration is a heterogeneous mission fixture, not a field effectiveness validation.

---

## Concern G — Limited inferential statistics in E1

**Disposition: ACCEPTABLE FOR THE CURRENT DESIGN.**

E1 is a parameterized mechanism study rather than a sample from an operational population. Its key inferential structure is paired seeded design, 30 instances/cell, same-cardinality controls, a rho=1 null condition, Wilson intervals for key binomial outcomes, and external boundary testing.

Adding a large grid of p-values would not create operational population inference. The manuscript should continue to state that repeated synthetic trials quantify mechanism stability, not real-world incidence.

---

## Concern H — Does E6b alter PDDL semantics to force validity?

**Disposition: CLOSED in v0.4.1 Methods.**

The frozen runner creates a planning-only guarded copy by adding static `gsc_admitted_rover/store/camera` predicates and conjoining them to relevant action preconditions. No original public predicate, object, fact, precondition, effect, or goal is deleted or rewritten. Every returned GSC plan is validated by VAL against the untouched original public PDDL.

This implementation contract must remain explicit.

---

## Literature/novelty audit

A focused 2026-10-08 refresh did not identify a work that simultaneously:

1. constructs a mission-conditioned heterogeneous Provider–Action planning domain from current provider/capability/policy state;
2. treats domain membership as the primary governance object;
3. evaluates membership directly with same-cardinality controls; and
4. performs a held-out public native-semantic planner/validator gate.

Closest planning neighbors remain ontology-mediated planning, semantic capability transformations, ADAMAS, KG translation layers, KGLAMP, and platform-aware planning. Recent agent-governance systems address action/effect admission and assurance rather than construction of a classical planning domain.

**Novelty hard-stop: not triggered.**

The paper still must not claim novelty for ontology–planning integration, generic runtime admission, or freshness checking in isolation.

---

## Reference-quality updates incorporated into v0.4.1

- Holmberg, Ioup, and Abdelguerfi's KG translation layer is cited as the published IEEE BigData 2025 paper, DOI `10.1109/BigData66926.2025.11478529`.
- arXiv:2609.03340 is updated to v2 title **“Fresh Memory, Stale Plans: Derivation Currency for Distributed LLM-Agent Memory.”**
- Fast Downward and VAL have canonical literature references.

---

## Final claim–evidence verdict

| Claim | Evidence | Verdict |
|---|---|---|
| GSC can synthesize a mission-conditioned Provider–Action domain | E0/E1/E2 | **Supported** |
| Membership matches controlled eligibility truth | E1 | **Supported in controlled benchmark** |
| Benefit is more than arbitrary cardinality reduction | E1 Random-core | **Supported** |
| Governance components have distinct roles | E3 | **Supported for tested challenges** |
| Runtime core transfers without C-UAS-specific branches | E4 | **Supported within shared abstraction** |
| Search-pollution reduction can survive public topology | E5 | **Supported conditionally** |
| Admission preserves native public task solvability/validity under mature external tools | E6b | **Supported; frozen gate PASS** |
| GSC generally accelerates mature planners | E6b null | **Not supported** |
| Global freshness is efficient/optimal | E2/E3 | **Not supported** |
| Field/physical safety or operational effectiveness | none | **Not supported** |

---

## Research decision

**Paper 1 experimental program remains CLOSED.**

The adversarial review found no claim–evidence gap that justifies a new experiment.

Next work package:

1. freeze v0.4.1 as the working full manuscript;
2. build publication-quality figures/tables from existing evidence only;
3. perform sentence-level claim–citation review;
4. perform target-venue formatting and final language editing;
5. generate DOCX/PDF only after explicit approval.

A new experiment is permitted only if a later reviewer identifies a concrete claim that cannot be supported or removed using the existing evidence.
