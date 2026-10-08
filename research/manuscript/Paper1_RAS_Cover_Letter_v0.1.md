# Cover Letter — Robotics and Autonomous Systems (Draft v0.1)

Dear Editor,

Please consider our manuscript, **“Governed Semantic Domain Compilation for Heterogeneous Autonomous Mission Planning,”** for publication as a Research Article in *Robotics and Autonomous Systems*.

Autonomous mission systems increasingly combine persistent semantic knowledge with automated planning, but the information represented in a reusable ontology or knowledge graph is not necessarily admissible for the current mission state. Our manuscript studies a specific boundary that remains under-examined in existing ontology-mediated planning and mission-management systems: **which heterogeneous provider–action instances should be allowed to constitute the current planning domain before search begins?**

We introduce **Governed Semantic Compilation (GSC)**, a mission-conditioned domain-synthesis mechanism that materializes a versioned operational snapshot, checks mission readiness, compiles current Provider–Action membership, records rejection provenance, and binds planning artifacts to the state that justified them. The contribution is not a new search algorithm or a general ontology-to-PDDL transformation.

The evaluation is designed to isolate this mechanism. A 12,600-evaluation controlled benchmark includes generator-owned eligibility labels and same-cardinality core-preserving random controls, allowing semantic selection to be separated from the trivial effect of using fewer actions. We additionally perform component ablations, configuration-only transfer to a five-phase search-and-rescue/inspection mission, and a public IPC-3 Rovers topology stress test.

The strongest external test is a frozen held-out evaluation on IPC-3 Rovers p09–p20. It uses native public semantics, a separately implemented admission path, Fast Downward 26.6, and VAL validation against the original public PDDL. All 12 Full-domain and 12 GSC problems solve, no Full-solved task becomes GSC-unsolved, every GSC plan passes VAL, and no returned plan uses a non-admitted provider. At the same time, Fast Downward reduces Full and GSC to identical effective search problems on all 12 holdout instances. We report this null result prominently because it defines the boundary of the computational claim: GSC provides an explicit and auditable domain-admission contract, while search reduction is conditional on whether irrelevant structure survives downstream planner preprocessing.

We believe the manuscript fits *Robotics and Autonomous Systems* because it addresses a computational module of autonomous mission systems at the intersection of semantic knowledge representation, automated planning, heterogeneous providers, runtime adaptation, and plan validation. The journal has also recently published closely related work on ontology-integrated autonomous mission management and heterogeneous mission planning, while our study focuses on the distinct problem of runtime Provider–Action domain membership and its direct evaluation.

All reported evidence is software/formal-model, parameterized synthetic, or public planning-benchmark evidence. We make no claim of field performance, physical safety, or unrestricted domain generality. The frozen confirmatory workflow, source identities, result summaries, and maintained research materials are available in the project repository.

This manuscript is original, has not been published elsewhere, and is not under consideration by another journal. Author, funding, conflict-of-interest, and data/code statements will be finalized before submission.

Thank you for considering our work.

Sincerely,

[Corresponding Author Name]  
[Affiliation]  
[Email]
