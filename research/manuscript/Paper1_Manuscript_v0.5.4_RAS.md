# RAS SUBMISSION WORKING DRAFT v0.5.4

# Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning

Author information to be added for submission.

**Draft date:** 8 October 2026  
**Draft status:** Experimental evidence is closed through the frozen E6b confirmatory external-validity gate. E0–E5 are complete; E6b passed on held-out IPC-3 Rovers p09–p20 using a separately implemented native-semantic admission path, Fast Downward 26.6, and VAL. The manuscript is in RAS submission preparation.

**Revision note:** v0.5.4 adds the Elsevier-required generative-AI disclosure before the References and links the frozen supplementary/reproducibility package. No scientific method, experiment, result, threshold, or claim boundary changes.

**Previous revision note:** v0.5.3 is a pre-layout copy-edit consolidation of v0.5.2. It standardizes terminology, removes duplicated meta-language, and tightens paragraph flow while preserving all methods, numerical results, evidence boundaries, and citations.

**Evidence boundary.** All reported evidence is software/formal-model, parameterized synthetic, or public planning-benchmark evidence. It does not establish field performance, physical safety, sensing accuracy, engagement effectiveness, communication latency, or unrestricted domain generality.

---

## Abstract

Persistent semantic models let autonomous mission systems reuse knowledge about capabilities, providers, actions, and policies, but not every known action is admissible for the current mission. We introduce **Governed Semantic Compilation (GSC)**, a mission-conditioned boundary that materializes a versioned closed-world Mission Snapshot, checks readiness, and compiles global action templates into a planning-admissible Provider–Action domain with rejection provenance and snapshot binding. Authorization-dependent actions remain explicit planning preconditions, while post-plan validation blocks plans that no longer match current state.

We evaluate GSC as a domain-membership mechanism rather than a new planner. In a 12,600-evaluation controlled benchmark, GSC exactly matches generator-owned eligibility labels. At \(N=640\) and eligibility density \(\rho=0.05\), blind search solves 30/30 GSC instances versus 20/30 with a same-cardinality core-preserving random control and 0/30 with state-aware or full domains; under A*, median generated nodes are 4, 31, 308, and 612.

A frozen external-validity gate then uses held-out IPC-3 Rovers p09–p20, native public semantics, a separate admission implementation, Fast Downward 26.6, and VAL. All 12 Full and 12 GSC tasks solve; no Full-solved instance becomes GSC-unsolved, every GSC plan validates against the original public PDDL, and no plan uses a non-admitted provider. Fast Downward nevertheless reduces Full and GSC to identical effective search problems on all 12 tasks. GSC therefore provides correct, auditable, mission-conditioned domain synthesis; search reduction is conditional on whether irrelevant structure survives downstream planner preprocessing.

**Keywords:** ontology-mediated planning; semantic compilation; autonomous mission planning; runtime governance; plan validation; capability-based systems; domain synthesis

---

# 1. Introduction

Autonomous mission systems often need two forms of knowledge at once. They need persistent semantic knowledge that can be reused across missions—capabilities, providers, action types, policies, and relationships—and they need an executable planning model that is specific to the current mission state. These are not the same object. A provider that is represented in persistent knowledge may be unavailable now; an action that is meaningful in the general domain may be disallowed by the current safety state or authorization; and a plan generated from an earlier state may no longer be releasable.

Existing work already connects semantics and planning in several ways. Ontology-mediated planning reconciles logical background knowledge with classical planning [1,2]; semantic capability models can generate solver-ready formulations [3]; ADAMAS integrates ontology-based mission knowledge with automated planning, execution monitoring, and replanning [4]; knowledge-graph approaches shape planner inputs and adaptive multi-robot planning [5,6]; and recent autonomous-driving work carries ontology/SWRL reasoning into PDDL mission planning and trajectory optimization [19]. Runtime assurance and governance are also established concerns: platform-aware planning and symbolic validation check executability and consistency [7,8], while recent admission/freshness work separates current evidence, authority, and decision validity [9–11,18]. The contribution of this paper is therefore not “ontology plus planning,” semantic validation in general, or a new search algorithm.

We focus on a narrower runtime question: **which heterogeneous provider–action instances should be allowed to constitute the current planning domain before search begins?** We call this boundary **Governed Semantic Compilation (GSC)**. Persistent semantic knowledge and current operational state are materialized into a versioned closed-world Mission Snapshot. A Readiness gate first decides whether the mission has enough current capability and valid entry conditions to justify planning. The compiler then instantiates only providers that satisfy the current semantic requirements, encoded safety state, and availability conditions. It emits a planning-admissible Provider–Action domain together with rejection reasons and snapshot/revision/hash provenance. Authorization-dependent actions remain explicit planning preconditions, and a post-plan validator blocks plans that no longer match the state that justified the compiled problem.

This formulation makes domain membership measurable independently of planner success. We define **eligibility density** \(\rho\) as the fraction of globally instantiated actions that are admissible for the current mission and vary \(\rho\) independently of global action-library size. The definitive controlled benchmark compares GSC with Full-domain planning, weaker filters, a generator-owned eligibility oracle, and same-cardinality random controls. The principal negative control preserves the task-critical action chain and exactly matches the GSC domain size, so differences cannot be attributed to cardinality alone. State perturbations and component ablations separately test Readiness, semantic/safety admission, freshness binding, post-plan validation, and rejection provenance.

The evidence is deliberately layered. E1 contains 12,600 method–planner evaluations across action-library size, eligibility density, clutter topology, and provider redundancy. E3 contains 5,400 component-ablation trials. E4 transfers the unchanged runtime core from the original heterogeneous C-UAS configuration to a five-phase SAR/inspection configuration using configuration only. E5 moves the search-pollution mechanism onto public IPC-3 Rovers topology with a separate clean-room planner while retaining study-authored governance masks. E6b then removes those masks and tests a frozen held-out Rovers corpus using native public semantics, a separate admission implementation path, Fast Downward 26.6, and VAL.

The resulting evidence gives a useful boundary condition. In controlled E1 and public-topology E5 settings, semantic admission can materially reduce search pollution when mission-invalid alternatives survive into the planner's effective representation. In E6b, by contrast, Fast Downward's own translation and relevance preprocessing removes the same native-goal-irrelevant structure, and Full and GSC become identical effective search problems. The external gate nevertheless passes every prespecified solvability, validation, source-identity, and non-admitted-provider criterion. We therefore interpret GSC primarily as a **governed domain-synthesis boundary**, with computational reduction as a conditional downstream benefit rather than a universal property.

The paper makes three contributions:

1. **Mission-conditioned Provider–Action domain synthesis.** GSC converts persistent semantic knowledge plus a versioned operational snapshot into a planning-admissible provider-specific domain while preserving rejection provenance and state binding.
2. **Mechanism-aware domain-membership evaluation.** Eligibility density, generator-owned labels, and same-cardinality controls distinguish semantic selection from arbitrary pruning, while ablations isolate the roles of readiness, safety admission, freshness, validation, and provenance.
3. **Bounded external validation.** A frozen native-semantic Rovers holdout verifies solvability preservation and returned-plan validity under a separate admission implementation, Fast Downward 26.6, and VAL, while also exposing the boundary of the search-reduction claim.

**Figure 1** summarizes the architecture and the separation between semantic admission, planner search, and post-plan validation.

---

# 2. Related Work

## 2.1 Ontology-mediated planning and semantic capability models

Ontology-based robot autonomy has long used reusable semantic models to organize domain knowledge, action concepts, and capabilities [13]. More directly, ontology-mediated planning studies how logical background knowledge interacts with classical planning. John and Koopmann separate OWL-DL ontologies from planning formalisms and rewrite ontology-mediated problems into PDDL [1]. Borgwardt et al. explicitly frame the open-world/closed-world mismatch and introduce coherence-update semantics with a polynomial compilation into classical planning [2]. These works address the general semantic-reconciliation problem; GSC does not claim a new ontology-planning logic or a generic OWL-to-PDDL transformation.

A second line converts machine-readable capability descriptions into solver-ready models. Köcher et al. generate SMT planning encodings from a semantic capability model, allowing required and provided capabilities to determine valid capability sequences [3]. Muppasani et al. construct a planning ontology for planners, domains, problems, and plan explanations [12]. These studies show that capability and planning metadata can be machine interpretable. GSC instead focuses on the **runtime membership of provider-specific actions** under one current mission snapshot and records why globally defined templates are admitted, authorization-pending, or pruned.

## 2.2 Knowledge-graph translation and adaptive mission planning

ADAMAS is a particularly close systems-level neighbor because it combines an ontology with automated planning, execution monitoring, and replanning for autonomous drone missions [4]. Holmberg et al. use a knowledge graph as a mission-aware translation layer that compiles semantic information into planner-consumable artifacts and supports adaptation as spatiotemporal information changes [5]. KGLAMP dynamically updates a knowledge graph encoding relations, reachability, and heterogeneous robot capabilities and grounds LLM-generated planning representations before replanning [6]. An et al. extend the same semantic-to-planning direction in autonomous driving: a Triplet Ontological Semantic Model and SWRL rules infer maneuvers that are translated into PDDL mission plans and continuous trajectory factors [19]. This provides an especially recent demonstration that a shared semantic representation can span reasoning and planning; it does not, however, treat current heterogeneous provider–action membership as a separately governed and directly evaluated runtime artifact.

The distinction is therefore not that semantic knowledge can influence planning. GSC treats the **membership of a snapshot-specific Provider–Action domain as a first-class governance decision** and evaluates this membership directly. The experimental design centers on admissibility precision/recall, rejected-action provenance, same-cardinality controls, and external semantic preservation rather than only downstream mission success.

## 2.3 Plan validation, runtime assurance, and stale derived decisions

Planning-domain governance should also be separated from post-plan verification. Platform-Aware Mission Planning connects mission planning to lower-level safety and executability checks through abstraction and refinement [7]. Petruzzellis et al. combine knowledge-graph retrieval, hierarchical planning, and symbolic validation of expected versus observed states [8].

Recent agent-runtime work further shows that version freshness and decision validity are not equivalent. PlanFence makes derivation currency explicit and rechecks an action-specific dependency frontier before a protected action [9]. ATR distinguishes any version change from a decision-relevant conflict [10]. Cognitive Admission Control binds consequential actions to risk-conditioned assurance evidence and dispatch-time guards [11]. Jørgensen and Ma similarly propose bounded enterprise autonomy in which semantic validity, procedural admissibility, policy, delegated authority, controlled execution, and provenance remain separate responsibilities around a proposed action [18]. Their contribution is a review-informed conceptual enterprise control framework rather than a classical planning-domain compiler or an empirical study of planner-domain membership. These results inform the positioning of GSC: the current global snapshot fence is supporting runtime control and is deliberately conservative; the upstream contribution is the construction and auditability of the planning domain.

## 2.4 Positioning relative to planner preprocessing

Classical planners also perform grounding, relevance analysis, and representation transformations. Fast Downward, for example, translates a PDDL problem into a multi-valued representation before heuristic search [16]. Such preprocessing can remove structure that is irrelevant to a goal. This is algorithmically useful but conceptually distinct from GSC.

Planner preprocessing asks which symbolic structure is useful for solving the already constructed planning problem. GSC asks which provider–action instances are permitted to constitute that planning problem given semantic requirements, provider availability, safety state, and authorization. In E6b these two mechanisms overlap for a narrow class of native Rovers irrelevance, producing identical effective Fast Downward problems. This overlap is reported explicitly rather than treated as equivalence: GSC additionally provides upstream rejection reasons, snapshot provenance, and governance semantics that need not be reducible to goal relevance.

### Table 1. Positioning against the closest technical lines

| Prior-art line | What it already establishes | What this paper studies instead |
|---|---|---|
| Ontology-mediated planning [1,2] | Logical coupling/compilation between ontologies and classical planning | Runtime synthesis of a mission-specific Provider–Action domain from a versioned snapshot |
| Semantic capability planning [3] | Capability models can generate solver-ready formulations | Provider instantiation and current admissibility under capability, state, safety, and authorization |
| KG translation/adaptive planning [4–6,19] | Semantic facts can shape planner inputs, PDDL mission plans, and replanning | Domain membership as a measurable governance object with explicit rejection provenance |
| Bounded action governance [18] | Semantic validity, process admissibility, authority, controlled execution, and provenance can be separated around proposed actions | Classical Provider–Action planning-domain membership is compiled and evaluated directly before planner search |
| Planner verification [7,8] | Plans can be checked for safety, executability, or consistency | Upstream action-domain admission plus downstream validation/freshness |
| Freshness/admission [9–11] | Stale or under-evidenced actions can be blocked/revalidated | Semantic domain synthesis; global freshness is supporting control |
| Planner preprocessing [16] | Planning structure can be translated/pruned for search | Explicit governance of what is allowed into the planning problem |

---

# 3. Problem Formulation

## 3.1 Persistent knowledge and operational state

Let \(O\) denote a persistent semantic model containing domain concepts, capability relations, provider descriptions, and stable policies. \(O\) may be maintained under open-world semantics and can legitimately remain incomplete. Let \(M\) denote a mission specification defining required capabilities, goals, and success conditions.

Execution at time \(t\) is represented by a closed-world **Mission Snapshot** \(S_t\). The snapshot materializes the facts that the runtime is willing to treat as current for planning. It includes mission facts \(F_t\), equipment/provider state \(E_t\), authorization state \(U_t\), safety/policy state \(P_t\), a revision \(r_t\), a snapshot identifier, and a content hash \(h_t\). The snapshot is therefore not an alternative ontology; it is an operational truth boundary derived from persistent semantics and current state sources.

## 3.2 Action templates, planning-admissible actions, and executable actions

Let \(A_{\text{global}}\) be a library of globally defined action templates. Each template \(a\) declares required capabilities, semantic prerequisites, symbolic preconditions/effects, a safety requirement when applicable, an authorization level, and monitoring metadata. A provider \(p\) is a concrete equipment or service instance that can implement one or more capabilities.

For a template–provider pair \((a,p)\), planning admissibility at time \(t\) is:

\[
G_{\text{plan}}(a,p\mid M,S_t)
=
\operatorname{Sem}(a,S_t)
\land
\operatorname{Safe}(a,S_t)
\land
\operatorname{Provides}(p,\operatorname{ReqCap}(a))
\land
\operatorname{Available}(p,S_t).
\]

The current implementation treats authorization differently from non-dispatch admission. L1 actions can be dispatch-admissible after validation; L2/L3 actions may remain in the planning domain while authorization remains an explicit symbolic precondition. We therefore distinguish a planning-admissible domain \(D_t^{\text{plan}}\) from a currently executable subset \(D_t^{\text{exec}}\):

\[
D_t^{\text{plan}}
=
\{a[p] : G_{\text{plan}}(a,p\mid M,S_t)=1\},
\]

\[
D_t^{\text{exec}}
=
\{x\in D_t^{\text{plan}} :
\operatorname{authorization}(x,S_t)\text{ is granted or }x\text{ is L1}\}.
\]

This distinction preserves the principle that a plan is not equivalent to permission to execute.

## 3.3 Eligibility density and mechanism hypothesis

Define eligibility density \(\rho_t\) as the fraction of globally instantiated action templates that are eligible under benchmark ground truth:

\[
\rho_t=
\frac{|A_{\text{eligible}}(t)|}
{|A_{\text{global}}|}.
\]

Low \(\rho\) indicates that the persistent action library contains many actions that are meaningful in the broader domain but not admissible for the present mission state.

The mechanism hypothesis is not that fewer actions always make planning faster. It is that **semantically correct selection preserves mission-relevant structure while removing inadmissible branches**, and should therefore outperform size-matched eligibility-blind pruning on semantic correctness, solvability, and—when such branches survive into search—planning burden.

## 3.4 Version-bound plan lifecycle

A plan \(\pi_t\) is generated from a problem bound to \((\text{snapshot\_id}_t,r_t,h_t)\). Before dispatch, the validator requires the live state to retain the expected snapshot identity, revision, and hash, then checks action membership, current authorization, symbolic preconditions, provider state, and encoded safety invariants.

A binding mismatch causes conservative rejection. This prevents a plan generated under \(S_t\) from silently outliving the state that justified it. The current design intentionally over-invalidates: even a revision that leaves the plan semantically valid forces revalidation or replanning. This is treated as a known design boundary rather than a novelty claim.

---

# 4. Governed Semantic Compilation

## 4.1 Semantic source and Mission Snapshot

The research prototype uses an OWL/RDF knowledge layer for persistent semantics and a deterministic bridge that materializes Mission Snapshots. In the current C-UAS fixture, the formal model contains 393 ontology triples and 260 positive ABox triples, for 653 RDF triples in the validated design-state model. RDF/SHACL/HermiT checks detect malformed or inconsistent fixtures, while SPARQL supports capability and relationship discovery.

These implementation counts are descriptive rather than contributory. The method requires only that persistent provider/capability relationships can be queried and that current state can be materialized into a closed-world snapshot.

The snapshot bridge records equipment health, capability aliases, mission facts, required authorization levels, roles, safety flags, essential capabilities, revision, source-ontology hash, and a snapshot identifier derived from stable state content. Planning never runs directly over the open-world ontology.

## 4.2 Readiness as an entry gate

Before compiling an action domain, a Readiness Gate determines whether the mission has enough current information and capability to justify planning. The current gate checks that each essential capability has at least one AVAILABLE provider, that required L2/L3 authority roles exist, that no encoded G0 invariant is already violated, and that no explicit mission contradiction is present.

Readiness and compilation are deliberately separate. Readiness asks whether the mission is eligible to enter planning; compilation asks which provider-specific actions are eligible to constitute the current domain. A provider failure with a backup should change the compiled domain and plan, whereas failure of the final provider for an essential capability should block the planning cycle before search.

## 4.3 Provider–Action domain synthesis

The compiler iterates over the global action library in a fixed order. It checks semantic-required facts, safety flags, provider existence, capability coverage, and provider health. For each surviving provider, it creates a grounded Provider–Action instance and preserves the source template and provider identifiers. L2/L3 actions receive the appropriate authorization predicates.

Every rejected template produces a structured reason such as `PRUNED_SEMANTIC`, `PRUNED_SAFETY`, or `PRUNED_RESOURCE`. Every retained action records its provider and whether current authorization makes it immediately executable or authorization-pending.

The output package contains:

- \(D_t^{\text{plan}}\);
- \(D_t^{\text{exec}}\);
- the planning problem;
- a feasibility/rejection report;
- provider and capability provenance;
- snapshot/revision/hash bindings;
- hashes of generated artifacts.

This makes domain membership auditable independently of the downstream planner.

### Algorithm 1. Governed Semantic Compilation

```text
Input: persistent mappings O, mission M, snapshot S_t, global templates A_global

1  R ← Readiness(S_t)
2  if R is not ready:
3      return blocked package with reasons

4  for each template a ∈ A_global:
5      if semantic-required facts are absent:
6          record PRUNED_SEMANTIC
7          continue
8      if encoded safety condition is false:
9          record PRUNED_SAFETY
10         continue
11     P ← AVAILABLE providers covering ReqCap(a)
12     if P is empty:
13         record PRUNED_RESOURCE
14         continue
15     for each provider p ∈ P:
16         instantiate a[p]
17         add authorization predicate if L2/L3
18         add a[p] to D_plan
19         if L1 or current authorization is GRANTED:
20             add a[p] to D_exec

21 emit D_plan, D_exec, planning problem,
   feasibility/rejection provenance, revision/hash bindings
```

## 4.4 State-conditioned planning

The base prototype uses a deterministic reference STRIPS planner in an independent process. The planner receives only the compiled domain/problem, solves for the mission goal, and returns the action sequence with search metadata. No new search algorithm is claimed; the simple planner isolates the effect of domain synthesis.

Three frozen truthfulness fixtures demonstrate state dependence. Under the nominal snapshot, the plan uses the primary radar for detection, a fusion provider for identification, a soft-mitigation provider, and the fusion provider for assessment. If reliable observation is already available, detection is omitted. If the primary radar is FAILED, the detection template remains relevant but is instantiated with the RF/EO backup provider. No hard-coded plan identifier is used.

E6b later tests the same conceptual boundary using an external planner, Fast Downward 26.6.

## 4.5 Version-bound validation and recompilation

A candidate plan is not automatically executable. The validator checks snapshot identity, revision, snapshot hash, and problem binding. It then verifies action membership, current authorization, provider state, symbolic preconditions, and encoded global safety conditions.

The execution supervisor increments state revision after successful actions or provider failures, recompiles the domain, and replans when a failure invalidates the current route. The frozen regression includes a provider-failure replan and an identification timeout retry across six planning cycles.

The freshness fence is intentionally coarse. Revision-only changes invalidate an old plan even when recompilation produces the same action sequence. Dependency-scoped or decision-scoped revalidation could reduce this false blocking [9,10], but adding such a subsystem would change the research question; it is left as a future extension.

---

# 5. Experimental Design

## 5.1 Research questions and evidence hierarchy

The study asks five linked questions.

**RQ1 — Semantic admission.** Does governed compilation reproduce an independent definition of admissibility while global action-set size increases and eligibility density decreases?

**RQ2 — State truthfulness.** Do controlled changes in provider state, observation, capability, safety, and authorization produce the expected domain/plan changes, and are stale plans rejected?

**RQ3 — Mechanism isolation.** Are observed benefits due to selecting the right actions rather than simply selecting fewer actions, and which governance components are load-bearing?

**RQ4 — Configuration portability.** Can the same readiness/compiler/validator core operate in a structurally different non-C-UAS mission using configuration rather than domain-specific runtime code?

**RQ5 — External validity.** Does the frozen admission idea preserve native public-task semantics, solvability, and plan validity under a separately implemented semantic oracle, an established third-party planner, and an independent validator?

Evidence is layered: E0 is a regression anchor; E1 is the definitive controlled mechanism benchmark; E2 retains deterministic truthfulness fixtures; E3 isolates components; E4 tests configuration-level transfer; E5 tests public planning topology; E6a is a transparent native-semantic pilot; and E6b is the confirmatory external-validity gate.

## 5.2 E0: frozen research-core regression

E0 reruns the existing research core without changing mission-planning logic. It checks four Readiness fixtures, 20/40/60/80-template domain-stress cases, three planner-truthfulness states, four negative validator cases plus a valid control, and the execution supervisor. Planner timing includes process startup and is excluded from real-time or OODA claims.

## 5.3 E1: definitive scaling × eligibility-density benchmark

E1 constructs controlled four-stage planning instances with a configurable global action library. Global template count \(N\) varies over 20, 40, 80, 160, 320, and 640; target eligibility density \(\rho\) varies over 0.05, 0.10, 0.25, 0.50, and 1.00. Each \(N\times\rho\) cell contains 30 paired mission instances.

Seeds are balanced across three distractor topologies—uniform, front-loaded, and late-loaded—and provider-redundancy strata 1, 2, and 4. The generator owns eligibility labels independently of the tested compiler. Four ineligibility causes are used: missing provider, failed provider, blocked semantic condition, and blocked safety condition.

Seven domain-selection methods are compared:

1. Full-domain;
2. Capability-only;
3. State-aware;
4. GSC;
5. Random cardinality-matched pruning;
6. Random-core, which preserves the four task-critical actions and fills the remaining GSC-sized domain randomly;
7. Oracle, the generator-owned eligible set.

Random-core is the principal negative control because it matches GSC cardinality without trivially deleting the mission chain.

Two search strategies use a common 1,000-expansion cap. Blind BFS probes branching pollution. A* uses an admissible remaining-stage heuristic. Primary outcomes are semantic precision/recall, solve rate, node expansions, generated nodes, action checks, and peak frontier. Runtime is secondary. The design produces 12,600 method–planner evaluations.

## 5.4 E2: state-perturbation matrix

E2 retains six deterministic perturbations over the original P0 snapshot:

- reliable observation becomes available;
- primary detection provider fails;
- an essential identification/assessment capability is lost;
- a G0 unsafe fact activates;
- L2 authorization is revoked;
- revision changes while operational facts remain otherwise equivalent.

For each case we rerun Readiness, compile a new domain, solve when permitted, and challenge the old nominal plan against the changed snapshot.

## 5.5 E3: component ablation

E3 isolates five functions in a generic runtime harness:

- Readiness;
- safety gating during compilation;
- revision/hash freshness binding;
- post-plan validation;
- rejected-action reason provenance.

Six configurations—full plus five ablations—are challenged with nine scenarios using 100 seeds per scenario and provider redundancy 1/2/4. An independent execution oracle labels whether a challenged plan is valid under the current snapshot. Primary diagnostics are false allow, false block, unnecessary planner calls, invalid actions admitted to \(D^{\text{plan}}\), and provenance coverage.

## 5.6 E4: configuration-only non-C-UAS transfer

E4 freezes the generic readiness/compiler/planner/validator runtime and instantiates a second domain entirely through configuration. The original C-UAS fixture contains four phases:

`Detect → Identify → Mitigate → Assess`.

The transfer configuration contains five non-weaponized SAR/inspection phases:

`Locate → Inspect → MapAccess → Relay → DeliverAid`.

The transfer criterion is strict: the core runtime file must retain the same SHA-256 hash and acquire no domain-specific branch. Each domain is evaluated on eight perturbation scenarios with 100 seeds per scenario, yielding 1,600 trials.

## 5.7 E5: public-topology stress test on IPC-3 Rovers

E5 tests whether the E1 search-pollution effect depends on the custom four-stage topology. It uses public IPC-3 Rovers STRIPS instances 03, 05, and 07 [14], obtained from the public Pyperplan benchmark distribution [15], containing heterogeneous rovers, stores, cameras, traversal, soil/rock sampling, imaging, and communication actions.

The public PDDL topology is unchanged. Because the benchmark does not contain the study's governance semantics, E5 overlays a study-authored runtime mask over rovers, cameras, and rover-specific traversal edges. This mask defines which already grounded PDDL operators are admissible for a synthetic Mission Snapshot.

Planning is performed by a separate clean-room typed-STRIPS implementation that imports no GSC or project planner code. It uses static-precondition pruning, backward relevance pruning, and greedy best-first search with \(h_{\text{add}}\). Every returned plan is replayed against the original PDDL transition semantics before governance validity is checked.

A PDDL-valid reference plan is used only to construct solution-preserving fixtures. Mask openness \(q\in\{0,0.25,0.50,0.75,1.00\}\). Resources used by the reference plan are retained and remaining resources are admitted probabilistically. Random-core is forced to retain the reference-plan operators and is filled to exactly the GSC grounded-operator count. Each task × \(q\) cell uses 30 paired seeds, producing 1,800 runs.

E5 is classified as a **public-topology stress test**, not the final external-validity gate, because its admission masks are study-authored and its planner is a clean-room implementation.

## 5.8 E6a: native-semantic Satellite pilot

Before E6b, we froze a native-semantic admission mapping for IPC-3 Satellite. A post-freeze static audit showed that required observation modes quickly covered almost all available satellites and instruments, leaving insufficient provider selectivity for a strong confirmatory gate. The pilot is retained rather than discarded, and the frozen mapping is not changed post hoc to manufacture pruning.

## 5.9 E6b: confirmatory external-validity gate using native Rovers semantics

E6b addresses the two principal limitations of E5: study-authored admission masks and a project-created planner.

### Frozen corpus and identities

The confirmatory corpus is IPC-3 Rovers p09–p20 from `aibasel/downward-benchmarks`, pinned to repository commit:

`e21d49c2cb61d147a46c5966f2581bf6fd422b9f`.

These 12 instances were not used in E5. Domain and problem Git blob identities are frozen before execution.

### Native-semantic admission

No synthetic governance mask is added. Admission is derived only from facts already authored in the public PDDL, including:

- `equipped_for_soil_analysis`;
- `equipped_for_rock_analysis`;
- `equipped_for_imaging`;
- `store_of`;
- `on_board`;
- `supports`;
- `calibration_target`;
- `can_traverse`;
- `visible`;
- `visible_from`;
- initial rover and lander positions;
- original mission-output goals.

For soil/rock goals, an eligible rover must possess the appropriate capability and a store, reach the required waypoint through rover-specific traversal edges that are also publicly visible, and retain a route from the goal waypoint to a waypoint that can communicate to a lander. For an image goal, an eligible rover/camera pair must support the requested mode, have a calibration target with a reachable visible calibration waypoint, reach a waypoint visible from the requested objective, and retain a communication route.

The rule is mission-goal-conditioned and based on independently authored executable planning semantics. These predicates are not interpreted as real field safety or authorization labels.

### Cross-implementation oracle

The compiler-side implementation is in Python. A second implementation uses a separate Node.js/JavaScript recursive S-expression parser, independent intermediate structures, and a separate data-reading path. A frozen oracle manifest is compared object by object with the compiler result. Fail-closed tests verify that deleting an expected admission or modifying the manifest identity is detected.

This oracle is independent at the **implementation path** level, not an independently authored policy ground truth: both implementations operationalize the same prespecified adapter rule over externally authored PDDL semantics. Semantic externality comes from the public benchmark facts and goals; the cross-implementation comparison tests whether the frozen adapter is implemented consistently.

### Planning-only guarded compilation

The original public Rovers domain/problem remain the semantic truth source and are never overwritten. The GSC condition is implemented as a **planning-only guarded copy**, rather than by deleting public objects, facts, preconditions, effects, or goals. The compiler adds three static predicates:

- `gsc_admitted_rover(r)`;
- `gsc_admitted_store(s)`;
- `gsc_admitted_camera(c)`.

`gsc_admitted_rover` is conjoined to the preconditions of rover-dependent actions; `gsc_admitted_store` is additionally required by `sample_soil`, `sample_rock`, and `drop`; and `gsc_admitted_camera` is additionally required by `calibrate` and `take_image`. The compiled problem adds the corresponding admitted-provider facts to the initial state. No original public predicate or transition is rewritten. The Full condition uses the original public PDDL directly.

This construction makes the intervention explicit: GSC changes only the static admission contract seen by the planner. Returned GSC action sequences are then interpreted and checked under the untouched public transition semantics.

### Planner and validator

Planning uses **Fast Downward 26.6** [16] with frozen alias `lama-first`, 300 s, and 4 GiB per run. The Full and GSC variants use the same original mission goals and resource cap.

Every returned GSC plan is validated against the **original, unmodified public domain/problem** using VAL [17], with source fixed to commit:

`3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`.

This independent replay is important because a plan that is valid only because of an accidental artifact in the guarded planning copy would fail validation under the original benchmark semantics.

### Prespecified gate

E6b passes only if all conditions hold:

1. source identities match the frozen files;
2. cross-implementation oracle mismatch = 0;
3. Fast Downward reports version 26.6;
4. VAL source commit matches the frozen commit;
5. at least 10/12 Full-domain instances solve under the fixed cap;
6. no Full-solved instance becomes GSC-unsolved;
7. every returned GSC plan passes VAL against original PDDL;
8. no GSC plan uses a non-admitted provider.

Search time, expanded/generated states, and plan length are secondary. A search-speed improvement is **not** required for PASS.

---

# 6. Results

## 6.1 E0 reproduces the intended domain, plan, and validation behavior

With 20, 40, 60, and 80 global templates, GSC produces six planning actions in every case, corresponding to pruning ratios of 70.0%, 85.0%, 90.0%, and 92.5%. The compiled reference planner expands four nodes and solves all cases. The ungated baseline expands 714 nodes at \(N=20\), reaches the 2,501-node cap at \(N=40\) and \(N=60\), and times out after 2,333 expansions at \(N=80\).

Because the baseline and GSC domains differ semantically as well as in size, E0 is used only as a reproducibility anchor. E1 provides the same-cardinality controls required for mechanism interpretation.

Readiness behaves as designed: nominal passes, loss of the shared provider for Identify/AssessEffect reports missing essential capability, absence of the required L3 responsibility role is blocked, and an active G0 unsafe fact is rejected before planning. The truthfulness fixture generates distinct plans under nominal, pre-observed, and primary-provider-failed states. The validator accepts the valid control and rejects an unknown action, stale revision, revoked authorization, and an injected G0 violation.

## 6.2 E1: semantic domain quality, not cardinality alone, governs controlled search burden

GSC and Oracle have admissibility precision = recall = 1.000 in every tested cell and solve every BFS/A* instance.

At \(N=640,\rho=0.05\), blind BFS gives:

- GSC: 30/30 solved (Wilson 95% CI 0.886–1.000);
- Random-core: 20/30 (0.488–0.808);
- State-aware: 0/30;
- Full-domain: 0/30.

Random-core solve rate falls to 10/30 at \(\rho=0.10\), 8/30 at \(\rho=0.25\), and 5/30 at \(\rho=0.50\). At \(\rho=1\), all actions are eligible and every method converges to 30/30.

A* solves every displayed \(N=640\) instance, but generated nodes still track semantic domain quality. At \(\rho=0.05\), medians are:

- GSC/Oracle: **4**;
- Random-core: **31**;
- State-aware: **308**;
- Full-domain: **612**.

At \(\rho=0.50\), the corresponding medians are 4, 163.5, 164, and 324. At \(\rho=1\), all are 4.

Thus, in the controlled benchmark, semantic admission reduces frontier pollution even when an admissible heuristic protects solve rate. **Figure 2** isolates this effect at \(N=640,\rho=0.05\): GSC and Random-core have the same cardinality, but their search burden and blind-search solvability remain materially different.

### Table 2. Definitive E1 results at \(N=640\) under blind BFS

| \(\rho\) | Method | Domain actions | Precision | Recall | Solve rate | Median expansions |
|---:|---|---:|---:|---:|---:|---:|
| 0.05 | GSC | 32 | 1.000 | 1.000 | 1.00 | 4 |
| 0.05 | Oracle | 32 | 1.000 | 1.000 | 1.00 | 4 |
| 0.05 | Random-core | 32 | 0.171 | 0.171 | 0.67 | 571 |
| 0.05 | State-aware | 336 | 0.095 | 1.000 | 0.00 | 1000 |
| 0.05 | Full-domain | 640 | 0.050 | 1.000 | 0.00 | 1000 |
| 0.10 | GSC | 64 | 1.000 | 1.000 | 1.00 | 4 |
| 0.10 | Random-core | 64 | 0.143 | 0.143 | 0.33 | 1000 |
| 0.25 | GSC | 160 | 1.000 | 1.000 | 1.00 | 4 |
| 0.25 | Random-core | 160 | 0.269 | 0.269 | 0.27 | 1000 |
| 0.50 | GSC | 320 | 1.000 | 1.000 | 1.00 | 4 |
| 0.50 | Random-core | 320 | 0.503 | 0.503 | 0.17 | 1000 |
| 1.00 | GSC | 640 | 1.000 | 1.000 | 1.00 | 4 |
| 1.00 | Random-core | 640 | 1.000 | 1.000 | 1.00 | 4 |
| 1.00 | State-aware | 640 | 1.000 | 1.000 | 1.00 | 4 |
| 1.00 | Full-domain | 640 | 1.000 | 1.000 | 1.00 | 4 |

Expansion counts at 1000 are censored by the fixed cap.

## 6.3 E2: state perturbations produce expected plan changes and conservative over-invalidation

When a reliable observation becomes available, the new plan shortens from four actions to three by omitting detection. When the primary radar is marked FAILED, the compiled domain decreases from six to five actions and the new four-action plan substitutes the RF/EO backup. The old nominal plan is rejected in both cases because its snapshot binding is stale.

Loss of the shared identification/assessment provider causes Readiness to report missing essential capabilities. An active G0 unsafe fact is blocked at Readiness. Revoking L2 authorization leaves six planning actions in the domain but removes the authorization fact required for mitigation, making the current problem unsolvable.

A revision-only perturbation leaves operational facts and the replanned sequence unchanged, but the old plan is still rejected because snapshot identifier/revision/hash changed. This is fail-closed but deliberately conservative.

## 6.4 E3: component ablations identify distinct failure modes

Across 5,400 ablation trials, Full GSC produces no false allows across authorization revocation, selected-provider failure, target change, and unknown-action injection: **0/400**.

Removing only the freshness fence permits all target-change challenges, yielding **100/400 false allows**. Removing post-plan validation permits all four challenge classes, yielding **400/400**.

Without Readiness, missing-capability and G0 entry cases invoke downstream planning in **200/200** trials even though the full configuration blocks them before planning. Without safety gating in the compiler, the safety-blocked case produces a plan in **100/100** trials and admits mean **1.99 invalid Provider–Action instances/trial** before validation blocks execution. Removing rejection reasons reduces provenance coverage from 100% to 0%. Full global freshness produces **100/100 false blocks** under revision-only changes.

### Table 3. E3 diagnostic ablations

| Variant | Diagnostic | Result | Interpretation |
|---|---|---:|---|
| Full GSC | Four post-plan challenges | 0/400 false allow | No challenged invalid plan released |
| −Readiness | Missing capability + G0 | 200/200 unnecessary planner calls | Entry gate prevents downstream work |
| −Safety compile | Safety-blocked entry | plan 100/100; mean 1.99 invalid actions/trial | Failure shifts from compile to validation |
| −Freshness | Target changed | 100/100 false allow | Snapshot binding is load-bearing |
| −Validator | Auth/provider/target/unknown action | 400/400 false allow | Current-state validation is load-bearing |
| −Reason provenance | Safety-blocked entry | 0% vs 100% reason coverage | Traceability loss without execution change |
| Full GSC | Revision-only | 100/100 false block | Global freshness is over-conservative |

## 6.5 E4: the same runtime core transfers to a five-phase non-C-UAS configuration

The transfer adds only SAR/inspection configuration. The generic governance runtime SHA-256 is identical before and after transfer, and no domain-specific branch is added.

Across 800 trials per domain, both C-UAS and SAR/inspection produce **0 false allows and 0 false blocks over 600 decision-relevant trials per domain**. When the selected first-phase provider fails, recompilation recovers in all trials with redundancy 2 or 4 (**66/66 per domain**) and cannot recover when redundancy is 1, yielding the expected overall 66/100 recovery.

The same limitation also transfers: revision-only change is rejected in 100/100 trials in both domains even when the plan remains valid. E4 supports configuration-level portability within the shared abstraction, not field equivalence or unrestricted domain generality.

## 6.6 E5: search-pollution reduction persists on public Rovers topology

The public Rovers instances have substantially different planning structure from the four-stage E1 generator. After static and relevance pruning, tasks 03, 05, and 07 contain 60, 141, and 153 grounded operators; the clean-room planner finds baseline plans of length 14, 22, and 18.

Across all 15 task × mask cells, GSC returns PDDL-valid and governance-valid plans in 30/30 paired seeds. At \(q=1\), every method operates on the complete grounded domain and search counts converge.

At the most restrictive mask (\(q=0\)), median generated nodes fall:

- task 03: **109 → 67** (38.5%);
- task 05: **321 → 175** (45.5%);
- task 07: **321 → 107** (66.7%).

On task 07, the reduction weakens from 57.0% at \(q=0.25\) to 40.8% at \(q=0.50\), 26.8% at \(q=0.75\), and 0% at \(q=1\).

The same-cardinality control remains informative. On task 05, Random-core achieves only 6/30 governance-valid solves at \(q=0\), 9/30 at \(q=0.25\), 17/30 at \(q=0.50\), and 26/30 at \(q=0.75\), despite retaining a known feasible reference-plan core. GSC remains 30/30. On task 07, Random-core is governance-valid but generates a median 232 nodes versus 107 for GSC at \(q=0\).

These results show that the controlled search-pollution mechanism can persist on independently authored planning topology when governance-invalid alternatives remain in the effective planner representation. They do not establish independent semantic labels or mature-planner speedup. **Figure 3** summarizes the \(q=0\) public-topology reductions and should be read together with the prespecified \(q=1\) convergence condition.

### Table 4. E5 public-topology stress test at \(q=0\)

| Task | Full ops | GSC ops | GSC valid | Random valid | GSC generated | Full generated | Reduction |
|---|---:|---:|---:|---:|---:|---:|---:|
| 03 | 60 | 57 | 30/30 | 27/30 | 67 | 109 | 38.5% |
| 05 | 141 | 111 | 30/30 | 6/30 | 175 | 321 | 45.5% |
| 07 | 153 | 113 | 30/30 | 30/30 | 107 | 321 | 66.7% |

## 6.7 E6a: Satellite is semantically independent but insufficiently selective

The frozen Satellite mapping successfully derives admissibility from public PDDL semantics without a study-authored runtime mask. However, post-freeze audit shows that required modes admit every satellite and nearly every instrument across the standard p01–p20 set. The pilot therefore supplies a semantic-consistency check but insufficient provider selectivity for the primary confirmatory gate. It is retained as a negative design lesson rather than omitted post hoc.

## 6.8 E6b: the frozen external-validity gate passes but yields a mature-planner performance null

The frozen E6b gate passes every prespecified criterion.

The cross-implementation JavaScript oracle matches the Python compiler with **zero admission mismatches**. Across the 12 held-out Rovers problems, the rule admits:

- 58/58 rovers;
- 60/65 cameras;
- 47/58 stores.

Thus, 16/181 provider-related objects (8.84%) are excluded while all 136 native mission-output goals retain at least one semantic witness. **Figure 4** makes this modest external selectivity explicit rather than treating E6b as a high-pruning stress test.

Fast Downward 26.6 solves **12/12 Full-domain** and **12/12 GSC** tasks within the frozen 300-s/4-GiB cap. No Full-solved problem becomes GSC-unsolved. Every returned GSC plan passes VAL against the original unmodified public domain/problem, and no GSC plan references a non-admitted provider. Source file identities, Fast Downward version, and VAL source commit match their frozen identities.

### Table 5. E6b frozen external-validity gate

| Prespecified criterion | Result |
|---|---:|
| Source identity mismatches | 0 |
| Admission serialization mismatches | 0 |
| Cross-implementation oracle mismatches | 0 |
| Uncovered native goals | 0 |
| Fast Downward 26.6 identity | verified |
| VAL frozen source commit | verified |
| Full-domain evaluable | 12/12 |
| Required minimum Full evaluable | 10/12 |
| Full-solved → GSC-unsolved | 0 |
| GSC VAL failures | 0 |
| Non-admitted-provider exposures | 0 |
| **Gate status** | **PASS** |

The external execution does **not** reproduce the search reduction observed in E1 and E5. Full and GSC are identical on all 12 instances in:

- Fast Downward translator variables;
- facts;
- operators;
- translated task size;
- relevant atoms;
- necessary variables/operators;
- landmark counts;
- expanded states;
- generated states;
- plan length;
- final `sas_plan` bytes.

Across the 12 pairs:

- median generated states: Full = GSC = **4,863.5**;
- median expanded states: Full = GSC = **145**;
- median plan length: Full = GSC = **45**;
- median wall time: Full **0.1275 s**, GSC **0.1246 s**;
- GSC is faster in 6/12 wall-time pairs and slower in 6/12.

The wall-time difference is consistent with run noise rather than a stable effect. **Figure 5** displays the mature-planner null directly: the GSC/Full ratios for generated states, expanded states, and plan length are 1.00 for all 12 holdout instances.

The logs indicate a direct boundary condition for the mechanism: the cameras and stores removed by GSC are also irrelevant to the native mission goals, and Fast Downward's translation/relevance processing eliminates their associated planning structure in the Full condition before search. Consequently, the two variants converge to the same effective planning task.

E6b therefore strengthens the **semantic correctness, solvability-preservation, and external-toolchain** claim while limiting the computational claim. GSC does not guarantee a mature-planner search reduction when the planner already removes equivalent irrelevant structure.

---

# 7. Discussion

## 7.1 What the complete evidence supports

The complete evidence supports a bounded claim about governed domain synthesis across three distinct layers.

First, E1 provides controlled mechanism evidence. GSC matches generator-owned eligibility labels across all \(N\times\rho\) cells, and same-cardinality Random-core demonstrates that preserving only action count is insufficient. Under low eligibility density, incorrect domain membership pollutes search even when the task-critical action chain remains available.

Second, E3 and E4 establish that domain admission is part of a broader but separable runtime-governance mechanism. Readiness avoids pointless downstream work, compile-time safety prevents invalid actions from entering the domain, snapshot binding protects against stale target state, post-plan validation prevents several classes of false allow, and provenance is necessary for traceability. The unchanged core transfers to a second five-phase configuration without domain-specific runtime code.

Third, E5 and E6b separate two aspects of externality that were conflated in earlier drafts. E5 demonstrates that search-pollution reduction can persist on a public planning topology when governance-invalid alternatives remain in a clean-room planner's effective search space. E6b removes study-authored admission masks, freezes native public semantics, and uses a cross-implementation admission oracle, Fast Downward, and VAL. It passes every semantic, solvability, validation, and non-admitted-provider criterion.

The E6b performance null is an important part of the final evidence. It shows that semantic admission is not a planner-independent complexity reduction. Fast Downward can remove the same goal-irrelevant structure in its own preprocessing. The correct interpretation is therefore:

> GSC makes planning-domain membership explicit, state-conditioned, and auditable. Search reduction is a conditional consequence when mission-irrelevant structure survives into the downstream planner's effective representation.

## 7.2 Why GSC is not redundant with planner preprocessing

A natural question after E6b is whether planner relevance pruning makes GSC unnecessary. The answer depends on what the system is trying to guarantee.

Fast Downward preprocessing optimizes a symbolic planning problem **after that problem has already been constructed**. GSC governs what is allowed to constitute that problem. The two mechanisms overlap when a non-admitted provider is also simply irrelevant to the current native planning goals, as occurred for 5 cameras and 11 stores in E6b. They diverge when domain membership depends on facts that are not equivalent to symbolic goal relevance—for example provider health, safety policy, organizational authorization, mission-specific semantic requirements, or current operational trust.

GSC also emits artifacts that conventional relevance pruning does not aim to provide: rejection reasons, provider/capability provenance, snapshot identifiers, revision/hash bindings, and an executable subset distinct from the planning-admissible domain. These properties make the compilation result an auditable contract between semantic knowledge and planning.

The E6b null is therefore not evidence that planner preprocessing and GSC are interchangeable. It is evidence that **one class of native-semantic irrelevance can be eliminated by both mechanisms**, and that performance claims must account for the downstream planner.

## 7.3 Relationship to ontology-planning theory

The open-world/closed-world distinction is not presented as a new theoretical discovery. Ontology-mediated planning already studies logical reconciliation between ontology semantics and classical planning [1,2]. Our use is operational: the persistent semantic model is not itself the current planning state. Current provider health, mission facts, policy flags, and authorization must be materialized into a state boundary before a mission-specific Provider–Action domain is synthesized.

GSC is therefore closer to runtime domain admission over heterogeneous capability providers than to a new description-logic planning formalism.

Holmberg et al. [5], ADAMAS [4], and KGLAMP [6] are particularly close systems-level neighbors because they compile or ground semantic mission information into planner-consumable forms. The remaining contribution is not “semantic compilation” in the abstract. It is the treatment of current provider–action membership as a separately justified artifact, combined with evaluation that directly tests membership quality and its downstream consequences.

## 7.4 Freshness is necessary but deliberately conservative

The present validator uses snapshot identity, revision, and hash as a global fence. E2 and E3 show why that fence is load-bearing for some stale-decision challenges, but they also quantify its cost: revision-only changes are falsely blocked in 100/100 trials even when the independently evaluated plan remains valid.

PlanFence and ATR [9,10] show that dependency-scoped or decision-scoped revalidation can avoid unnecessary invalidation. For this paper, the appropriate response is not to add another subsystem but to state the limitation. The global fence guarantees that compiled domains/plans do not silently escape the state that justified them. Selective freshness is a separate design question.

## 7.5 Scope, safety, and application boundary

The current implementation remains a mission-level software/formal-model prototype. The C-UAS fixture includes heterogeneous sensing, fusion, mitigation, authorization, provider failure, and evidence roles, but the experiments do not measure real detection probability, physical engagement effectiveness, networked command latency, or field safety.

E4 demonstrates absence of a hidden C-UAS branch in the generic runtime, not equivalence to field deployment in SAR. E6b strengthens external semantic/planning evidence using an independently authored benchmark but remains a classical planning benchmark. Its capability/state predicates are not independently authored field safety or authorization rules.

A deployment claim would require separately validated sensor/effect interfaces, communication-failure models, hardware-in-the-loop or field testing, operational safety analysis, and human authorization studies. None of those claims are made here.

## 7.6 Threats to validity

**Synthetic mechanism benchmark.** E1 intentionally controls eligibility and governance-invalid clutter. Its large search effects should be interpreted as mechanism evidence, not universal planner speedups.

**Study-authored E5 masks.** E5 uses external planning topology but experimenter-authored governance masks and reference-plan-preserving fixtures. It therefore tests topology and mechanism transfer rather than independent semantic truth.

**Recent-neighbour scope.** Contemporary work already couples ontology-grounded semantics to PDDL mission planning [19] and separates semantic validity, authority, and controlled execution around agent actions [18]. The claimed novelty therefore remains the runtime Provider–Action domain-membership boundary and its direct mechanism/external evaluation, not semantic planning or governed action execution in general.

**E6b semantic scope.** E6b eliminates the study-authored masks and derives admission from native public PDDL capability/state semantics. Those predicates are independently authored executable planning semantics, not independent operational safety/authorization labels.

**Oracle-rule coupling.** The JavaScript oracle is implementation-independent from the Python compiler, but both instantiate the same frozen study-defined mapping from native PDDL facts/goals to provider eligibility. The zero-mismatch result therefore supports reproducible implementation of the adapter; it is not evidence that an independent domain expert authored an identical admission policy.

**External selectivity.** E6b excludes 16/181 provider-related objects (8.84%), concentrated in five cameras and eleven stores, while all 58 rovers are admitted. The gate is consequently strong evidence for no-loss semantic admission and external toolchain validity, but not a high-selectivity external stress test.

**Planner dependence.** E6b gives a complete mature-planner search null: Full and GSC translate to identical effective tasks and have identical search counts/plans on all 12 holdout problems. This directly limits generalization of the E1/E5 computational effect.

**Controlled-sample scope.** E1 contains 30 paired instances per cell; E3/E4 use 100 trials per scenario. These quantify mechanism stability under seeded generation, not sampling of a real operational population.

**Conservative freshness.** Any revision/hash change invalidates an old plan. This favors fail-closed behavior over continuity and is not an optimal selective-revalidation strategy.

**Cross-domain scope.** E4's second domain remains synthetic and intentionally shares the paper abstraction. It supports software-configuration portability, not unrestricted domain-independent autonomy.

**Field scope.** Neither the C-UAS fixture nor IPC planning benchmarks establish sensing accuracy, real-world safety, physical-effect validity, communication robustness, or operational effectiveness.

---

# 8. Conclusion

Governed Semantic Compilation addresses a specific gap between persistent semantic knowledge and executable planning: a system can know many capabilities, providers, and actions without all of them being admissible for the mission now. GSC makes that boundary explicit by materializing a versioned closed-world Mission Snapshot, checking readiness, synthesizing a provider-specific planning domain, recording rejection provenance, and binding downstream artifacts to the state that justified them.

The completed evidence supports GSC as a governance boundary rather than a new planner. E1 shows that semantically coherent membership can outperform same-cardinality random selection when inadmissible alternatives survive into search; E3 separates the roles of Readiness, safety admission, freshness, validation, and provenance; E4 demonstrates configuration-level transfer of the unchanged core; and E5 shows that the search-pollution mechanism can persist on public Rovers topology.

E6b closes the prespecified external planner/validator gate on held-out native Rovers semantics: all frozen solvability, validation, source-identity, and non-admitted-provider criteria pass. At the same time, Fast Downward translates Full and GSC to identical effective problems on all 12 holdout tasks. The final claim is therefore deliberately narrow: **GSC provides correct, auditable, mission-conditioned domain synthesis; computational benefit is conditional on the downstream planner and problem representation.** The work does not establish field performance, universal complexity reduction, or optimal freshness.

---

# Data, Code, and Reproducibility

The maintained research workspace is:

`https://github.com/qiangruhuang/Tianshu`

The frozen E6b confirmatory execution is GitHub Actions run `37713826709`. Primary committed result summaries are under:

`e6b/results/run-37713826709/`

The frozen E6b benchmark commit is:

`aibasel/downward-benchmarks@e21d49c2cb61d147a46c5966f2581bf6fd422b9f`.

The validator source is pinned to:

`KCL-Planning/VAL@3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`.

The manuscript's software/formal-model evidence should be interpreted under the explicit scope limitations in Section 7.6.

Detailed frozen protocols, per-instance E6b paired results, and toolchain identities are summarized in `Paper1_Supplementary_Material_v1.0.md` and the public project repository.

---

# Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

During the preparation of this work, the authors used OpenAI ChatGPT to assist with literature triage, manuscript organization and language refinement, code review, reproducibility documentation, and preparation of figure-generation scripts. All experimental designs, frozen decision rules, analyses, external-tool executions, result verification, interpretations, and final manuscript content were reviewed by the authors, who take full responsibility for the content of the published article.

The reported numerical results were produced by executable analysis/planning code and independently verifiable toolchains rather than by generative-AI inference.

---

# References

[1] T. John and P. Koopmann, “Planning with OWL-DL Ontologies,” in *Proceedings of the 27th European Conference on Artificial Intelligence (ECAI 2024)*, Frontiers in Artificial Intelligence and Applications, vol. 392, pp. 4165–4172, 2024. doi:10.3233/FAIA240988.

[2] S. Borgwardt, D. Nhu, and G. Röger, “Automated Planning with Ontologies Under Coherence Update Semantics,” in *Proceedings of the 22nd International Conference on Principles of Knowledge Representation and Reasoning (KR 2025)*, pp. 751–761, 2025. doi:10.24963/kr.2025/72.

[3] A. Köcher, L. M. Vieira da Silva, and A. Fay, “Automated Process Planning Based on a Semantic Capability Model and SMT,” arXiv:2312.08801, v2, 2024.

[4] C. Ligneul, É. Saux, M. Olivares, Y. Ruichek, and Y. Haralambous, “Integrating ontology with automated action planning for autonomous drone mission management system,” *Robotics and Autonomous Systems*, vol. 202, art. 105460, 2026. doi:10.1016/j.robot.2026.105460.

[5] E. Holmberg, E. Ioup, and M. Abdelguerfi, “A Knowledge-Graph Translation Layer for Mission-Aware Multi-Agent Path Planning in Spatiotemporal Dynamics,” in *2025 IEEE International Conference on Big Data (BigData)*, Macau, China, pp. 1–10, 2025. doi:10.1109/BigData66926.2025.11478529.

[6] C. L. Shek, F. M. Tariq, S. Bae, D. Isele, and P. Gupta, “KGLAMP: Knowledge Graph-guided Language model for Adaptive Multi-robot Planning and Replanning,” arXiv:2602.04129, 2026.

[7] S. Panjkovic, A. Cimatti, A. Micheli, and S. Tonetta, “Platform-Aware Mission Planning,” *Proceedings of the International Conference on Automated Planning and Scheduling*, vol. 35, no. 1, pp. 93–101, 2025. doi:10.1609/icaps.v35i1.36105.

[8] F. Petruzzellis, C. Cornelio, and P. Liò, “Hierarchical Planning for Complex Tasks with Knowledge Graph-RAG and Symbolic Verification,” in *Proceedings of the 42nd International Conference on Machine Learning*, PMLR, vol. 267, pp. 49105–49127, 2025.

[9] E. Chen, S. Wang, and C. G. Brinton, “Fresh Memory, Stale Plans: Derivation Currency for Distributed LLM-Agent Memory,” arXiv:2609.03340v2, 2026. doi:10.48550/arXiv.2609.03340.

[10] Y. Lyu, Y. Ren, R. Lai, and W. Liu, “From Version Conflicts to Decision Conflicts: Selective Revalidation for Long-Running AI Agents,” arXiv:2609.08015, 2026.

[11] J. He and D. Yu, “Cognitive Admission Control: Risk-Conditioned Assurance for Consequential Actions in Agentic Distributed Systems,” arXiv:2609.16313, 2026.

[12] B. C. Muppasani, N. Gupta, V. Pallagani, B. Srivastava, R. Mutharaju, M. N. Huhns, et al., “Building a planning ontology to represent and exploit planning knowledge and its applications,” *Discover Data*, vol. 3, art. 55, 2025. doi:10.1007/s44248-025-00093-9.

[13] A. Olivares-Alarcos, D. Beßler, A. Khamis, P. Gonçalves, M. K. Habib, J. Bermejo-Alonso, et al., “A review and comparison of ontology-based approaches to robot autonomy,” *The Knowledge Engineering Review*, vol. 34, e29, 2019. doi:10.1017/S0269888919000237.

[14] D. Long and M. Fox, “The 3rd International Planning Competition: Results and Analysis,” *Journal of Artificial Intelligence Research*, vol. 20, pp. 1–59, 2003.

[15] Y. Alkhazraji, M. Frorath, M. Grützner, M. Helmert, T. Liebetraut, R. Mattmüller, M. Ortlieb, J. Seipp, T. Springenberg, P. Stahl, and J. Wülfing, “Pyperplan,” Zenodo, 2020. doi:10.5281/zenodo.3700819.

[16] M. Helmert, “The Fast Downward Planning System,” *Journal of Artificial Intelligence Research*, vol. 26, pp. 191–246, 2006. doi:10.1613/JAIR.1705.

[17] R. Howey, D. Long, and M. Fox, “VAL: Automatic Plan Validation, Continuous Effects and Mixed Initiative Planning Using PDDL,” in *Proceedings of the 16th IEEE International Conference on Tools with Artificial Intelligence (ICTAI 2004)*, pp. 294–301, 2004. doi:10.1109/ICTAI.2004.120.

[18] B. N. Jørgensen and Z. G. Ma, “Governing Agentic AI in Enterprise Workflows: A Bounded-Autonomy Framework for Delegated Authority and Controlled Execution,” *Information*, vol. 17, no. 9, art. 923, 2026. doi:10.3390/info17090923.

[19] Y.-C. An, J.-H. Choi, J.-W. Pyo, S.-H. Bae, and T.-Y. Kuc, “Unified Semantic Reasoning and Planning for Autonomous Driving,” *Sensors*, vol. 26, no. 18, art. 5973, 2026. doi:10.3390/s26185973.
