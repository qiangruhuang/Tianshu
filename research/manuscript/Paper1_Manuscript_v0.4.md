# WORKING MANUSCRIPT DRAFT v0.4

# Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning

**From persistent open-world knowledge to versioned closed-world planning domains**

Author information to be added for submission.

**Draft date:** 8 October 2026  
**Draft status:** Experimental evidence chain closed through the frozen E6b independent external-validity gate. E0–E5 are complete; E6b passed on held-out IPC-3 Rovers p09–p20 using an independently implemented native-semantic oracle, Fast Downward 26.6, and VAL. The manuscript is now in claim-consolidation and adversarial-review stage.

**Evidence boundary.** All reported evidence is software/formal-model, parameterized synthetic, or public planning-benchmark evidence. It does not establish field performance, physical safety, sensing accuracy, engagement effectiveness, communication latency, or unrestricted domain generality.

---

## Abstract

Semantic knowledge bases and autonomous planners operate under different runtime assumptions. Persistent ontologies accumulate reusable and potentially incomplete knowledge about capabilities, providers, actions, and policies, whereas execution requires state-current facts and a bounded action set. Existing ontology-mediated planners reconcile ontology reasoning with classical planning, semantic capability models generate solver-ready formulations, knowledge-graph translation layers shape planner inputs, and runtime validators check generated plans. These lines do not by themselves make the current membership of heterogeneous provider–action instances an explicit, independently testable governance object.

We introduce **Governed Semantic Compilation (GSC)**, a mission-conditioned domain-synthesis boundary that materializes a versioned closed-world Mission Snapshot, performs an entry Readiness check, screens global action templates against current semantic requirements, safety state, and provider availability, and emits a planning-admissible Provider–Action domain with rejection provenance and snapshot binding. Authorization-dependent actions remain explicit symbolic preconditions, while a post-plan validator conservatively rejects plans whose current state no longer matches the snapshot that justified them.

We evaluate GSC using a frozen prototype regression, a 12,600-evaluation controlled scaling benchmark, component ablations, configuration-only transfer to a five-phase search-and-rescue/inspection domain, a public-topology Rovers stress test, and a frozen independent external-validity gate. In the controlled benchmark, GSC exactly matches generator-owned eligibility labels; at \(N=640,\rho=0.05\), blind search solves 30/30 GSC instances versus 20/30 with a same-cardinality core-preserving random control and 0/30 with state-aware or full domains. Under A*, all methods solve, but median generated nodes are 4, 31, 308, and 612, respectively. A public Rovers topology stress test reproduces search-pollution reductions of 38.5–66.7% when study-authored governance masks are selective.

We then freeze an independent holdout on IPC-3 Rovers p09–p20 with no synthetic governance mask, a separately implemented JavaScript admission oracle, Fast Downward 26.6, and VAL. All 12 Full-domain and all 12 GSC problems solve within the fixed resource cap; no Full-solved instance becomes unsolved under GSC, every GSC plan validates against the original public PDDL, and no returned plan references a non-admitted provider. E6b therefore passes every prespecified external-validity criterion. However, Fast Downward translates Full and GSC to identical effective search problems on all 12 tasks, yielding identical translated variables, facts, operators, expansions, generated states, plan lengths, and final plans. These results support governed semantic domain synthesis as an explicit correctness, provenance, and accountability boundary. Search reduction is a conditional benefit when mission-irrelevant structure survives downstream planner preprocessing, not a planner-independent guarantee.

**Keywords:** ontology-mediated planning; semantic compilation; capability-based systems; autonomous planning; runtime governance; plan validation; knowledge graphs; domain synthesis

---

# 1. Introduction

Autonomous mission systems increasingly rely on semantic models to describe heterogeneous platforms, capabilities, environmental context, and task rules. Ontologies and knowledge graphs are attractive because they can accumulate persistent knowledge, support semantic queries, and decouple a functional capability from any particular implementation. Planning and execution, however, operate under a different regime. A plan must be generated for a concrete mission state in which provider health, mission facts, policy conditions, and authority are current. A capability that is known to exist in persistent knowledge is therefore not necessarily available to the mission now, and an action that is meaningful in the broader domain is not necessarily admissible in the present planning instance.

This paper studies the operational boundary between semantic knowledge and executable planning domains rather than the general problem of ontology-based planning itself. The question is narrow but consequential: **before a planner searches, which provider–action instances should be admitted into the current mission domain, and on what current evidence?**

Prior work has established several important parts of this pipeline. Ontology-mediated planning explicitly studies the interaction between open-world ontology semantics and closed-world classical planning, including OWL-DL rewriting and coherence-update semantics [1,2]. Semantic capability descriptions can be transformed into solver-ready planning formulations [3]. ADAMAS integrates an ontology with automated action planning, mission execution, and replanning for autonomous drones [4]. Knowledge-graph translation layers and KGLAMP further show that semantic state, policies, and heterogeneous capabilities can shape planner inputs and support adaptation as conditions change [5,6]. These advances make a broad contribution claim such as “ontology plus planning” untenable.

Plan verification and runtime freshness form another neighboring line. Platform-Aware Mission Planning couples mission planning with lower-level safety and executability verification [7], while neuro-symbolic hierarchical planning has combined knowledge-graph retrieval with symbolic validation [8]. More recent work explicitly separates stale records from stale decisions: PlanFence validates the dependencies used by a pending action [9], ATR distinguishes version conflicts from decision conflicts and selectively rechecks affected conditions [10], and Cognitive Admission Control binds consequential actions to risk-conditioned assurance evidence [11]. Snapshot binding or stale-plan invalidation therefore cannot be claimed as novel in isolation.

GSC is positioned upstream of these mechanisms. It treats the mission-specific planning domain itself as an artifact that must be justified from persistent semantics plus a current operational snapshot. GSC separates a persistent semantic model from a versioned closed-world Mission Snapshot, applies an entry Readiness check, and compiles global action templates into provider-specific actions using current semantic requirements, encoded safety policy, and provider availability. The output is a planning-admissible Provider–Action domain with explicit rejection provenance and snapshot binding. Authorization-dependent actions remain represented through explicit planning predicates; a narrower executable subset records which compiled actions are currently dispatch-admissible. After planning, a validator conservatively rejects a plan whose snapshot identity, revision, or hash no longer matches the state that justified the compiled domain.

The experimental design focuses on mechanism rather than an end-to-end mission score. We define **eligibility density** \(\rho\) as the fraction of globally instantiated action templates that are admissible for a current mission and vary \(\rho\) independently of global action-set size. GSC is compared with Full-domain planning, weaker capability/state filters, a generator-owned eligibility oracle, and same-cardinality random controls. A core-preserving random control always retains the task-critical action chain, allowing us to test whether the effect comes from selecting the right actions rather than merely selecting fewer actions. State perturbations and component ablations separately test Readiness, semantic/safety admission, freshness binding, post-plan validation, and provenance.

The evidence chain is intentionally layered. The definitive E1 benchmark contains 30 paired mission instances for every \(N\times\rho\) cell, three clutter topologies, balanced provider-redundancy strata, seven domain-selection methods, and two controlled search strategies. E3 uses 5,400 component-ablation trials. E4 transfers the unchanged runtime core to a five-phase SAR/inspection configuration using configuration only. E5 moves the search-pollution mechanism onto public IPC-3 Rovers topology using a separate clean-room planner, while retaining study-authored governance masks. Finally, E6b removes those masks and evaluates a frozen native-semantic holdout with an independent admission implementation, Fast Downward 26.6 [16], and VAL [17].

The resulting evidence gives two complementary results. First, semantically coherent domain admission can materially reduce search pollution when inadmissible alternatives survive into the planner's effective representation. Second, this computational effect is not universal: in E6b, Fast Downward's own translation and relevance preprocessing reduces Full and GSC to identical effective search problems. The external holdout nevertheless passes all semantic correctness, solvability-preservation, validation, and provider-exposure criteria. This boundary condition sharpens rather than weakens the contribution: GSC is fundamentally a **governed domain-synthesis boundary**, while computational benefit depends on the downstream planning stack.

The paper makes three primary contributions:

1. **Mission-conditioned Provider–Action domain synthesis.** We formalize and implement a boundary that converts persistent semantic knowledge plus a versioned closed-world snapshot into a planning-admissible Provider–Action domain, while preserving reasons for rejection and the state binding of generated artifacts.

2. **Mechanism-aware evaluation of domain membership.** We introduce eligibility density, generator-owned admissibility labels, and same-cardinality controls to distinguish semantic action selection from the trivial effect of reducing action count. Component ablations identify distinct failure modes of Readiness, semantic/safety admission, freshness binding, validation, and provenance.

3. **Bounded external validation.** We show that the frozen admission rule preserves native public-task solvability and returned-plan validity on held-out IPC-3 Rovers instances under a separately implemented admission oracle, Fast Downward 26.6, and VAL. The same external experiment identifies the boundary of the computational claim: a mature planner can absorb the pruning effect through its own preprocessing.

---

# 2. Related Work

## 2.1 Ontology-mediated planning and semantic capability models

Ontology-based robot autonomy has long used reusable semantic models to organize domain knowledge, action concepts, and capabilities [13]. More directly, ontology-mediated planning studies how logical background knowledge interacts with classical planning. John and Koopmann separate OWL-DL ontologies from planning formalisms and rewrite ontology-mediated problems into PDDL [1]. Borgwardt et al. explicitly frame the open-world/closed-world mismatch and introduce coherence-update semantics with a polynomial compilation into classical planning [2]. These works address the general semantic-reconciliation problem; GSC does not claim a new ontology-planning logic or a generic OWL-to-PDDL transformation.

A second line converts machine-readable capability descriptions into solver-ready models. Köcher et al. generate SMT planning encodings from a semantic capability model, allowing required and provided capabilities to determine valid capability sequences [3]. Muppasani et al. construct a planning ontology for planners, domains, problems, and plan explanations [12]. These studies show that capability and planning metadata can be machine interpretable. GSC instead focuses on the **runtime membership of provider-specific actions** under one current mission snapshot and records why globally defined templates are admitted, authorization-pending, or pruned.

## 2.2 Knowledge-graph translation and adaptive mission planning

ADAMAS is a particularly close systems-level neighbor because it combines an ontology with automated planning, execution monitoring, and replanning for autonomous drone missions [4]. Holmberg et al. use a knowledge graph as a mission-aware translation layer that compiles semantic information into planner-consumable artifacts and supports adaptation as spatiotemporal information changes [5]. KGLAMP dynamically updates a knowledge graph encoding relations, reachability, and heterogeneous robot capabilities and grounds LLM-generated planning representations before replanning [6].

The distinction is therefore not that semantic knowledge can influence planning. GSC treats the **membership of a snapshot-specific Provider–Action domain as a first-class governance decision** and evaluates this membership directly. The experimental design centers on admissibility precision/recall, rejected-action provenance, same-cardinality controls, and external semantic preservation rather than only downstream mission success.

## 2.3 Plan validation, runtime assurance, and stale derived decisions

Planning-domain governance should also be separated from post-plan verification. Platform-Aware Mission Planning connects mission planning to lower-level safety and executability checks through abstraction and refinement [7]. Petruzzellis et al. combine knowledge-graph retrieval, hierarchical planning, and symbolic validation of expected versus observed states [8].

Recent agent-runtime work further shows that version freshness and decision validity are not equivalent. PlanFence validates only the shared records on which an action depends [9]. ATR distinguishes any version change from a decision-relevant conflict [10]. Cognitive Admission Control binds consequential actions to risk-conditioned assurance evidence and dispatch-time guards [11]. These results inform the positioning of GSC: the current global snapshot fence is supporting runtime control and is deliberately conservative; the upstream contribution is the construction and auditability of the planning domain.

## 2.4 Positioning relative to planner preprocessing

Classical planners also perform grounding, relevance analysis, and representation transformations. Fast Downward, for example, translates a PDDL problem into a multi-valued representation before heuristic search [16]. Such preprocessing can remove structure that is irrelevant to a goal. This is algorithmically useful but conceptually distinct from GSC.

Planner preprocessing asks which symbolic structure is useful for solving the already constructed planning problem. GSC asks which provider–action instances are permitted to constitute that planning problem given semantic requirements, provider availability, safety state, and authorization. In E6b these two mechanisms overlap for a narrow class of native Rovers irrelevance, producing identical effective Fast Downward problems. This overlap is reported explicitly rather than treated as equivalence: GSC additionally provides upstream rejection reasons, snapshot provenance, and governance semantics that need not be reducible to goal relevance.

### Table 1. Positioning against the closest technical lines

| Prior-art line | What it already establishes | What this paper studies instead |
|---|---|---|
| Ontology-mediated planning [1,2] | Logical coupling/compilation between ontologies and classical planning | Runtime synthesis of a mission-specific Provider–Action domain from a versioned snapshot |
| Semantic capability planning [3] | Capability models can generate solver-ready formulations | Provider instantiation and current admissibility under capability, state, safety, and authorization |
| KG translation/adaptive planning [4–6] | Semantic facts can shape planner inputs and support replanning | Domain membership as a measurable governance object with explicit rejection provenance |
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

E5 tests whether the E1 search-pollution effect depends on the custom four-stage topology. It uses public IPC-3 Rovers STRIPS instances 03, 05, and 07 [14], containing heterogeneous rovers, stores, cameras, traversal, soil/rock sampling, imaging, and communication actions.

The public PDDL topology is unchanged. Because the benchmark does not contain the study's governance semantics, E5 overlays a study-authored runtime mask over rovers, cameras, and rover-specific traversal edges. This mask defines which already grounded PDDL operators are admissible for a synthetic Mission Snapshot.

Planning is performed by a separate clean-room typed-STRIPS implementation that imports no GSC or project planner code. It uses static-precondition pruning, backward relevance pruning, and greedy best-first search with \(h_{\text{add}}\). Every returned plan is replayed against the original PDDL transition semantics before governance validity is checked.

A PDDL-valid reference plan is used only to construct solution-preserving fixtures. Mask openness \(q\in\{0,0.25,0.50,0.75,1.00\}\). Resources used by the reference plan are retained and remaining resources are admitted probabilistically. Random-core is forced to retain the reference-plan operators and is filled to exactly the GSC grounded-operator count. Each task × \(q\) cell uses 30 paired seeds, producing 1,800 runs.

E5 is classified as a **public-topology stress test**, not the final external-validity gate, because its admission masks are study-authored and its planner is a clean-room implementation.

## 5.8 E6a: native-semantic Satellite pilot

Before E6b, we froze a native-semantic admission mapping for IPC-3 Satellite. A post-freeze static audit showed that required observation modes quickly covered almost all available satellites and instruments, leaving insufficient provider selectivity for a strong confirmatory gate. The pilot is retained rather than discarded, and the frozen mapping is not changed post hoc to manufacture pruning.

## 5.9 E6b: independent external-validity gate using native Rovers semantics

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

### Independent oracle

The compiler-side implementation is in Python. A second implementation uses a separate Node.js/JavaScript recursive S-expression parser, independent intermediate structures, and a separate data-reading path. A frozen oracle manifest is compared object by object with the compiler result. Fail-closed tests verify that deleting an expected admission or modifying the manifest identity is detected.

### Planner and validator

Planning uses **Fast Downward 26.6** [16] with frozen alias `lama-first`, 300 s, and 4 GiB per run. The Full and GSC variants use the same original mission goals and resource cap.

Every returned GSC plan is validated against the **original, unmodified public domain/problem** using VAL [17], with source fixed to commit:

`3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`.

### Prespecified gate

E6b passes only if all conditions hold:

1. source identities match the frozen files;
2. independent-oracle mismatch = 0;
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

Thus, in the controlled benchmark, semantic admission reduces frontier pollution even when an admissible heuristic protects solve rate.

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

These results show that the controlled search-pollution mechanism can persist on independently authored planning topology when governance-invalid alternatives remain in the effective planner representation. They do not establish independent semantic labels or mature-planner speedup.

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

The independent JavaScript oracle matches the compiler with **zero admission mismatches**. Across the 12 held-out Rovers problems, the rule admits:

- 58/58 rovers;
- 60/65 cameras;
- 47/58 stores.

Thus, 16/181 provider-related objects (8.84%) are excluded while all 136 native mission-output goals retain at least one semantic witness.

Fast Downward 26.6 solves **12/12 Full-domain** and **12/12 GSC** tasks within the frozen 300-s/4-GiB cap. No Full-solved problem becomes GSC-unsolved. Every returned GSC plan passes VAL against the original unmodified public domain/problem, and no GSC plan references a non-admitted provider. Source file identities, Fast Downward version, and VAL source commit match their frozen identities.

### Table 5. E6b frozen external-validity gate

| Prespecified criterion | Result |
|---|---:|
| Source identity mismatches | 0 |
| Admission serialization mismatches | 0 |
| Independent-oracle mismatches | 0 |
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

The wall-time difference is consistent with run noise rather than a stable effect.

The logs indicate a direct boundary condition for the mechanism: the cameras and stores removed by GSC are also irrelevant to the native mission goals, and Fast Downward's translation/relevance processing eliminates their associated planning structure in the Full condition before search. Consequently, the two variants converge to the same effective planning task.

E6b therefore strengthens the **semantic correctness, solvability-preservation, and external-toolchain** claim while limiting the computational claim. GSC does not guarantee a mature-planner search reduction when the planner already removes equivalent irrelevant structure.

---

# 7. Discussion

## 7.1 What the complete evidence supports

The complete evidence supports a bounded claim about governed domain synthesis across three distinct layers.

First, E1 provides controlled mechanism evidence. GSC matches generator-owned eligibility labels across all \(N\times\rho\) cells, and same-cardinality Random-core demonstrates that preserving only action count is insufficient. Under low eligibility density, incorrect domain membership pollutes search even when the task-critical action chain remains available.

Second, E3 and E4 establish that domain admission is part of a broader but separable runtime-governance mechanism. Readiness avoids pointless downstream work, compile-time safety prevents invalid actions from entering the domain, snapshot binding protects against stale target state, post-plan validation prevents several classes of false allow, and provenance is necessary for traceability. The unchanged core transfers to a second five-phase configuration without domain-specific runtime code.

Third, E5 and E6b separate two aspects of externality that were conflated in earlier drafts. E5 demonstrates that search-pollution reduction can persist on a public planning topology when governance-invalid alternatives remain in a clean-room planner's effective search space. E6b removes study-authored admission masks, freezes native public semantics, and uses an independent oracle, Fast Downward, and VAL. It passes every semantic, solvability, validation, and provider-exposure criterion.

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

**E6b semantic scope.** E6b eliminates the study-authored masks and derives admission from native public PDDL capability/state semantics. Those predicates are independently authored executable planning semantics, not independent operational safety/authorization labels.

**Planner dependence.** E6b gives a complete mature-planner search null: Full and GSC translate to identical effective tasks and have identical search counts/plans on all 12 holdout problems. This directly limits generalization of the E1/E5 computational effect.

**Controlled-sample scope.** E1 contains 30 paired instances per cell; E3/E4 use 100 trials per scenario. These quantify mechanism stability under seeded generation, not sampling of a real operational population.

**Conservative freshness.** Any revision/hash change invalidates an old plan. This favors fail-closed behavior over continuity and is not an optimal selective-revalidation strategy.

**Cross-domain scope.** E4's second domain remains synthetic and intentionally shares the paper abstraction. It supports software-configuration portability, not unrestricted domain-independent autonomy.

**Field scope.** Neither the C-UAS fixture nor IPC planning benchmarks establish sensing accuracy, real-world safety, physical-effect validity, communication robustness, or operational effectiveness.

---

# 8. Conclusion

A system can know many capabilities, providers, and actions without all of them being admissible for the mission now. Governed Semantic Compilation addresses this operational gap by materializing a versioned closed-world Mission Snapshot, checking mission readiness, and synthesizing a provider-specific planning domain from current semantic requirements, encoded safety state, and provider availability. Authorization remains explicit at the planning/execution boundary, and generated artifacts retain rejection provenance and snapshot binding.

The completed evidence supports GSC as an explicit governance boundary rather than a new planner. In the 12,600-evaluation E1 benchmark, GSC exactly matches independent eligibility truth and outperforms same-cardinality random selection when governance-invalid alternatives pollute search. E3 shows that Readiness, safety admission, freshness, post-plan validation, and provenance are distinct load-bearing components. E4 transfers the unchanged runtime core to a five-phase SAR/inspection configuration. E5 shows that search-pollution reduction can persist on public Rovers topology under a generic planner.

The frozen E6b holdout then closes the external planner/validator gate. On held-out IPC-3 Rovers p09–p20, the native-semantic rule has zero independent-oracle mismatch, all 12 Full and all 12 GSC tasks solve, every GSC plan validates against original PDDL using VAL, and no returned plan exposes a non-admitted provider. At the same time, Fast Downward translates Full and GSC to identical effective problems, eliminating the search advantage on this holdout.

The resulting claim is deliberately precise: **GSC provides correct, auditable, mission-conditioned domain synthesis; computational benefit is conditional on the downstream planner and problem representation.** The work does not establish field performance, universal complexity reduction, or optimal freshness. Within those bounds, it provides a reproducible way to make the boundary between persistent semantic knowledge and executable planning explicit and testable.

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

---

# References

[1] T. John and P. Koopmann, “Planning with OWL-DL Ontologies,” in *Proceedings of the 27th European Conference on Artificial Intelligence (ECAI 2024)*, Frontiers in Artificial Intelligence and Applications, vol. 392, pp. 4165–4172, 2024. doi:10.3233/FAIA240988.

[2] S. Borgwardt, D. Nhu, and G. Röger, “Automated Planning with Ontologies Under Coherence Update Semantics,” in *Proceedings of the 22nd International Conference on Principles of Knowledge Representation and Reasoning (KR 2025)*, pp. 751–761, 2025. doi:10.24963/kr.2025/72.

[3] A. Köcher, L. M. Vieira da Silva, and A. Fay, “Automated Process Planning Based on a Semantic Capability Model and SMT,” arXiv:2312.08801, v2, 2024.

[4] C. Ligneul, É. Saux, M. Olivares, Y. Ruichek, and Y. Haralambous, “Integrating ontology with automated action planning for autonomous drone mission management system,” *Robotics and Autonomous Systems*, vol. 202, art. 105460, 2026. doi:10.1016/j.robot.2026.105460.

[5] E. Holmberg, E. Ioup, and M. Abdelguerfi, “A Knowledge-Graph Translation Layer for Mission-Aware Multi-Agent Path Planning in Spatiotemporal Dynamics,” arXiv:2510.21695, 2025.

[6] C. L. Shek, F. M. Tariq, S. Bae, D. Isele, and P. Gupta, “KGLAMP: Knowledge Graph-guided Language model for Adaptive Multi-robot Planning and Replanning,” arXiv:2602.04129, 2026.

[7] S. Panjkovic, A. Cimatti, A. Micheli, and S. Tonetta, “Platform-Aware Mission Planning,” *Proceedings of the International Conference on Automated Planning and Scheduling*, vol. 35, no. 1, pp. 93–101, 2025. doi:10.1609/icaps.v35i1.36105.

[8] F. Petruzzellis, C. Cornelio, and P. Liò, “Hierarchical Planning for Complex Tasks with Knowledge Graph-RAG and Symbolic Verification,” in *Proceedings of the 42nd International Conference on Machine Learning*, PMLR, vol. 267, pp. 49105–49127, 2025.

[9] E. Chen, S. Wang, and C. G. Brinton, “Fresh Memory, Stale Plans: Dependency-Scoped Validation for Distributed LLM-Agent Memory,” arXiv:2609.03340, 2026.

[10] Y. Lyu, Y. Ren, R. Lai, and W. Liu, “From Version Conflicts to Decision Conflicts: Selective Revalidation for Long-Running AI Agents,” arXiv:2609.08015, 2026.

[11] J. He and D. Yu, “Cognitive Admission Control: Risk-Conditioned Assurance for Consequential Actions in Agentic Distributed Systems,” arXiv:2609.16313, 2026.

[12] B. C. Muppasani, N. Gupta, V. Pallagani, B. Srivastava, R. Mutharaju, M. N. Huhns, et al., “Building a planning ontology to represent and exploit planning knowledge and its applications,” *Discover Data*, vol. 3, art. 55, 2025. doi:10.1007/s44248-025-00093-9.

[13] A. Olivares-Alarcos, D. Beßler, A. Khamis, P. Gonçalves, M. K. Habib, J. Bermejo-Alonso, et al., “A review and comparison of ontology-based approaches to robot autonomy,” *The Knowledge Engineering Review*, vol. 34, e29, 2019. doi:10.1017/S0269888919000237.

[14] D. Long and M. Fox, “The 3rd International Planning Competition: Results and Analysis,” *Journal of Artificial Intelligence Research*, vol. 20, pp. 1–59, 2003.

[15] Y. Alkhazraji, M. Frorath, M. Grützner, M. Helmert, T. Liebetraut, R. Mattmüller, M. Ortlieb, J. Seipp, T. Springenberg, P. Stahl, and J. Wülfing, “Pyperplan,” Zenodo, 2020. doi:10.5281/zenodo.3700819.

[16] M. Helmert, “The Fast Downward Planning System,” *Journal of Artificial Intelligence Research*, vol. 26, pp. 191–246, 2006. doi:10.1613/JAIR.1705.

[17] R. Howey, D. Long, and M. Fox, “VAL: Automatic Plan Validation, Continuous Effects and Mixed Initiative Planning Using PDDL,” in *Proceedings of the 16th IEEE International Conference on Tools with Artificial Intelligence (ICTAI 2004)*, pp. 294–301, 2004. doi:10.1109/ICTAI.2004.120.
