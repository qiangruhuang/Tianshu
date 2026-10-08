# Paper 1 — Claim–Evidence–Citation Audit v1.0

**Manuscript:** `Paper1_Manuscript_v0.4.2.md` (complete version maintained in project Library)  
**Date:** 2026-10-08  
**Decision:** **No new experiment required.**

## Automated citation integrity

- references present: 19 (`[1]`–`[19]`);
- distinct citation numbers used in text: 19;
- cited numbers without a reference entry: none;
- reference entries never cited: none.

## High-risk claim audit

| Claim | Evidence/source | Verdict |
|---|---|---|
| GSC is a mission-conditioned Provider–Action domain-synthesis boundary | method + implementation | PASS |
| E1 30/30 vs 20/30 vs 0/30 at N=640, rho=.05 | frozen E1 benchmark | PASS |
| E1 benefit is not arbitrary cardinality reduction | same-cardinality core-preserving Random-core | PASS |
| E3 components have distinct load-bearing roles | 5,400 ablation trials | PASS |
| E4 runtime transfers without a domain-specific branch | unchanged core hash + 1,600 trials | PASS within shared abstraction |
| E5 search-pollution effect survives public topology | IPC-3 Rovers 03/05/07 | PASS conditionally |
| E5 provides independent admission truth | study-authored masks | **DO NOT CLAIM** |
| E6b preserves native public-task solvability/validity | run 37713826709 | PASS |
| E6b cross-implementation oracle is independent policy ground truth | same frozen mapping, separate code paths | **DO NOT CLAIM** |
| E6b provides high external selectivity | 16/181 provider-related objects excluded | **DO NOT CLAIM** |
| GSC generally accelerates mature planners | E6b Full=GSC effective task in 12/12 | **NOT SUPPORTED** |
| GSC has field/physical safety evidence | no field experiment | **NOT SUPPORTED** |

## 2026 nearest-neighbour updates

Two September 2026 peer-reviewed studies were added to the working manuscript:

1. Jørgensen & Ma, *Information* 17(9):923 — bounded enterprise action governance, semantic/process/policy/authority separation, and controlled execution.
2. An et al., *Sensors* 26(18):5973 — ontology/SWRL reasoning connected directly to PDDL autonomous-driving mission planning and trajectory optimization.

These narrow the novelty claim but do not trigger a novelty hard-stop. The submission must not claim ontology-to-PDDL integration, governed execution, or semantic validity in general as novel.

## Remaining citation-level edits before submission

1. Consider adding [13] or [1,2] to the opening general statement about ontology/knowledge-graph reuse if the target venue expects citation-dense introductions.
2. Keep Fast Downward [16] adjacent to statements about translation/relevance preprocessing.
3. Internal experimental numbers should cite the final paper's figure/table callouts rather than external literature.
4. Label E5 consistently as **public-topology stress test**.
5. Use **cross-implementation oracle** for E6b; never “independent policy oracle.”
6. Keep the 8.84% E6b provider-exclusion limitation in Threats to Validity.
7. Keep the mature-planner null in the main text, not only the supplement.

## Submission gate

The evidence program remains closed. The next tasks are publication figures/tables, final reference normalization, and target-venue formatting. No additional benchmark is justified by this audit.