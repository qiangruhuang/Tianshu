# Paper 1 — Figure & Table Package v1.0

**Date:** 2026-10-08  
**Rule:** all figures summarize existing evidence only; no post-hoc benchmark selection or new experiment.

## Main Figure 1 — GSC architecture

**Purpose:** establish the paper's contribution before any performance result.

**Flow:** persistent semantics + mission + current state → versioned Mission Snapshot → Readiness → GSC Compiler → planning-admissible Provider–Action domain + rejection provenance + snapshot/revision/hash binding → Planner → Validator.

**Caption principle:** GSC is the explicit mission-conditioned domain-membership boundary, not a new search algorithm.

## Main Figure 2 — E1 same-cardinality mechanism evidence

At `N=640, rho=0.05`:

- A* median generated nodes: GSC 4; Random-core 31; State-aware 308; Full-domain 612.
- Blind-search solved: GSC 30/30; Random-core 20/30; State-aware 0/30; Full-domain 0/30.

**Interpretation:** Random-core has the same cardinality and retains the task-critical chain, so the contrast isolates semantic selection rather than simple size reduction.

## Main Figure 3 — E5 public-topology stress test

At `q=0`, median generated-node reductions versus Full-domain are:

- Rovers 03: 38.5%
- Rovers 05: 45.5%
- Rovers 07: 66.7%

At `q=1`, methods converge. This is a conditional public-topology search-pollution result, not the final external semantic-validity evidence.

## Main Figure 4 — E6b native provider admission

Across held-out Rovers p09–p20:

- rovers: 58/58 admitted;
- cameras: 60/65 admitted;
- stores: 47/58 admitted;
- total provider-related objects: 165/181 admitted;
- excluded: 16/181 = 8.84%;
- native goals with >=1 witness: 136/136.

**Interpretation:** E6b is a no-loss external semantic gate with modest but non-zero selectivity, not a high-pruning stress test.

## Main Figure 5 — E6b mature-planner null

For every p09–p20 pair under frozen Fast Downward 26.6:

- generated-state ratio GSC/Full = 1.00;
- expansion ratio GSC/Full = 1.00;
- plan-length ratio GSC/Full = 1.00.

Also identical in 12/12 pairs: translator variables, facts, operators, relevant atoms, landmarks, and final `sas_plan` bytes.

**Interpretation:** Fast Downward preprocessing removes the same native-goal-irrelevant structure upstream GSC excludes, establishing the boundary of the computational claim.

---

# Main tables

1. **Related-work positioning** — include the September 2026 nearest neighbours on bounded action governance and ontology→PDDL autonomous-driving planning.
2. **E1 definitive mechanism table** — retain the `N=640` blind-BFS table.
3. **E3 diagnostic ablations** — retain component-level failure modes.
4. **E5 q=0 public-topology summary** — label consistently as public-topology stress test.
5. **E6b frozen gate table** — retain in the main paper; this is the key external-validity table.

# Compression rule

- Abstract: only one E1 contrast and one E6b PASS/null statement.
- Results: full numerical detail.
- Discussion: interpretation, not numerical repetition.
- Conclusion: one E6b PASS sentence plus one computational-boundary sentence.

# Supplement candidates

Move detailed grids/traces to supplement if page pressure is high:

- full E1 `N × rho` grid;
- E2 perturbation traces;
- complete E3 5,400-trial cell table;
- E4 per-scenario details;
- E5 q=0.25/0.50/0.75 results;
- E6b 12-pair wall-time table;
- GitHub Actions build/audit logs.

Keep the E6b mature-planner null itself in the main text.