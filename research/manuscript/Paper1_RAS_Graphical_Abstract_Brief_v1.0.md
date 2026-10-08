# RAS Graphical Abstract Brief v1.0

## Objective

Communicate the full paper in one left-to-right visual without implying universal planner speedup.

## Composition

### Left — Persistent knowledge is broader than the current mission

Show reusable capabilities, multiple providers, global action templates, and policy/authorization relations.

### Center — Governed Semantic Compilation

Mission Snapshot → Readiness → Provider–Action admission → planning-admissible domain.

The GSC box should explicitly emit:

- admitted Provider–Action set;
- rejection provenance;
- snapshot/revision/hash binding.

### Right — Evidence and boundary

**Controlled mechanism**
- same-cardinality control;
- GSC 4 generated nodes vs Random-core 31 at `N=640, rho=.05`;
- blind search 30/30 vs 20/30.

**External gate PASS**
- Rovers p09–p20;
- Full 12/12 solved;
- GSC 12/12 solved;
- VAL failures 0;
- non-admitted-provider exposure 0.

**Mature-planner boundary**
- Fast Downward preprocessing;
- Full effective task = GSC effective task in 12/12;
- no universal speedup claim.

## One-line takeaway

**Govern what enters the planner; do not assume every semantically known action belongs to the current planning problem.**

## Constraints

- application-neutral; no weapon imagery;
- generic provider/capability icons or boxes;
- no final “speedup” arrow;
- reuse manuscript Fig.1 semantics rather than creating a second architecture;
- final visual emphasis: auditable domain admission, with computational reduction shown as conditional.
