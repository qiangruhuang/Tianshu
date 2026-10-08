# Paper 1 v0.3 → v0.4 Claim–Evidence Audit

**Source manuscript:** `Paper1_Manuscript_v0.3_External_Validity_Gate.docx`  
**Audit date:** 2026-10-08  
**Trigger:** completed E6b confirmatory PASS, GitHub Actions run `37713826709`

## 1. Audit conclusion

The v0.3 manuscript remains structurally usable, but several statements are now stale because they describe E5 as the external-validity gate and present third-party planner replication as future work.

The required change is not to expand the experimental story. It is to **reclassify the evidence layers**:

- E5 = public-topology stress test with study-authored masks and clean-room planner;
- E6b = independent external-validity gate with native public semantics, independent oracle, Fast Downward 26.6, and VAL;
- search reduction = positive in E1/E5 but null in E6b under mature preprocessing.

The manuscript should explicitly report this null rather than imply that E5 search reductions generalize to Fast Downward.

---

## 2. Page 1 — draft status

### v0.3 problem

The draft status states that “E5 external-validity gate” is complete and that the remaining strengthening is replication on an established third-party planner.

### Required v0.4 correction

Replace with:

> The definitive E1 mechanism benchmark, E3 component ablations, E4 configuration-only transfer, E5 public-topology stress test, and E6b independent external-validity gate are complete. E6b uses held-out IPC-3 Rovers p09–p20, a separately implemented native-semantic admission oracle, Fast Downward 26.6, and VAL. All 12 Full and 12 GSC tasks solved within the frozen resource cap, every GSC plan validated against the original public PDDL, and no non-admitted provider appeared in a returned plan. Fast Downward translated Full and GSC to identical effective search problems on all 12 holdout tasks, so the external result supports semantic correctness and solvability preservation rather than a planner-independent speedup.

Delete the statement that third-party planner replication remains outstanding.

---

## 3. Page 2 — Abstract

### v0.3 problem

The abstract calls the three-task E5 study an “external-validity gate” and emphasizes the 38.5%, 45.5%, and 66.7% search reductions. This was defensible before E6b but is now incomplete.

### Required v0.4 correction

- rename E5 evidence to **public-topology stress test**;
- add E6b as the actual independent external-validity gate;
- keep E5 search reductions as conditional mechanism evidence;
- add the E6b mature-planner null explicitly.

### Recommended abstract logic

> In the controlled benchmark, GSC matches eligibility truth and outperforms same-cardinality controls when inadmissible alternatives survive into search. A public Rovers topology stress test reproduces this direction under a clean-room planner. We then freeze an independent holdout on Rovers p09–p20 using native public semantics, an independently implemented admission oracle, Fast Downward 26.6, and VAL. The gate passes with 12/12 Full and 12/12 GSC tasks solved, zero solvability regressions, zero VAL failures, and zero non-admitted-provider exposure. However, Fast Downward translates Full and GSC to identical effective search problems on all 12 tasks. GSC is therefore supported as a governed domain-synthesis and auditability boundary; computational benefit is conditional rather than planner-independent.

---

## 4. Page 13 — Section 5.7

### v0.3 heading

`5.7 E5: external-validity gate on public IPC-3 Rovers planning instances`

### Required heading

`5.7 E5: public-topology stress test on IPC-3 Rovers planning instances`

### Required interpretation change

The first sentence should state that E5 tests whether the E1 search-pollution effect survives a public planning topology, **not** that it provides fully independent semantic validation.

Add a final sentence to the subsection:

> Because E5 overlays study-authored governance masks and uses a clean-room planner, it is treated as a topology stress test; semantic and planner independence are tested separately in E6b.

---

## 5. Add Section 5.8 — E6b Methods

Required elements:

- held-out Rovers p09–p20;
- frozen benchmark commit and source blob identities;
- native PDDL capability/state predicates only;
- no study-authored runtime mask;
- independent JavaScript S-expression oracle;
- Fast Downward 26.6, `lama-first`, 300 s, 4 GiB;
- VAL frozen commit;
- validation against original public PDDL;
- frozen PASS criteria;
- performance endpoints explicitly secondary.

Do not call native PDDL predicates “independent safety labels.” They are independently authored executable planning semantics.

---

## 6. Pages 21–22 — E5 Results and figures

### Keep

The E5 quantitative results remain valid:

- task 03: 109 → 67 generated nodes, 38.5% reduction;
- task 05: 321 → 175, 45.5%;
- task 07: 321 → 107, 66.7%;
- q=1 convergence;
- Random-core validity differences.

### Change labels

- Figure 6: “Public-topology stress test on IPC-3 Rovers tasks.”
- Table 6: “E5 public-topology stress test at q=0.”

### Add boundary sentence

> E5 demonstrates that semantic admission can reduce search burden on a public planning topology when governance-invalid alternatives remain in the planner's effective representation; E6b separately tests whether the admission rule remains sound under native semantics and an established planner.

---

## 7. Add Section 6.7 — E6b Results

Recommended heading:

**6.7 E6b passes the frozen external-validity gate but yields a mature-planner performance null**

Required primary results:

- independent-oracle mismatch: 0;
- uncovered native goals: 0;
- 58/58 rovers, 60/65 cameras, 47/58 stores admitted;
- Full evaluable: 12/12;
- GSC solved: 12/12;
- Full-solved → GSC-unsolved: 0;
- GSC VAL failures: 0;
- non-admitted-provider exposures: 0;
- gate status: PASS.

Required secondary result:

- translator variables/facts/operators/task size/relevant atoms/necessary variables/necessary operators/landmarks equal in 12/12;
- expansions equal in 12/12;
- generated states equal in 12/12;
- plan lengths equal in 12/12;
- final plan bytes equal in 12/12;
- median generated states Full = GSC = 4,863.5;
- median expanded Full = GSC = 145;
- median plan length Full = GSC = 45;
- median wall time Full 0.1275 s vs GSC 0.1246 s;
- GSC wall time faster on 6/12 and slower on 6/12.

Interpret this as a mature-planner null, not a failed gate.

---

## 8. Page 23 — Discussion 7.1

### v0.3 problem

The text says E5 is the external gate and that independent semantic annotation / established planner replication remain future strengthening steps.

### Required v0.4 replacement logic

> E5 and E6b answer different questions. E5 shows that semantic admission can reduce search pollution on an independently authored planning topology when inadmissible alternatives survive into a generic planner's search representation. E6b removes study-authored masks, uses held-out native public semantics, and executes through Fast Downward 26.6 and VAL. E6b passes every frozen correctness and solvability criterion but produces no additional search reduction because Full and GSC translate to the same effective Fast Downward problem. The evidence therefore supports explicit governed domain synthesis and conditional computational benefit rather than a universal complexity reduction.

---

## 9. Page 25 — Threats to validity

### Replace “Reference planners” bullet

Old logic: Fast Downward replication remains desirable.

New logic:

> **Planner dependence.** E6b completes replication with Fast Downward 26.6 and shows a full search-burden null: Full and GSC have identical translated problems and search counts on all 12 holdout tasks. This limits generalization of the E1/E5 search-reduction effect and indicates that computational benefit depends on whether mission-irrelevant structure survives planner grounding and relevance preprocessing.

### Replace E5 mask bullet

> **Semantic scope.** E5 uses study-authored governance masks. E6b removes those masks and derives admission from native public PDDL capability/state semantics, but those predicates are not independently authored field safety or authorization labels. External semantic validity is therefore stronger than E5 but remains planning-domain, not operational-field, evidence.

Keep the conservative-freshness and synthetic-transfer limitations.

---

## 10. Page 26 — Conclusion

### v0.3 problem

The conclusion states that two stronger tests remain: established planner replication and independently authored admission annotations.

### Required v0.4 correction

The first gap is now closed by E6b. The second should be narrowed rather than left as a generic missing experiment.

Recommended final paragraph:

> The completed evidence supports GSC as an explicit governance boundary between persistent semantics and executable planning. Controlled experiments show that semantically coherent admission can reduce search pollution when irrelevant alternatives remain in the effective planning representation. The frozen E6b holdout further shows that the admission rule preserves native public-task solvability and returned-plan validity under Fast Downward 26.6 and VAL with zero oracle mismatch, validation failure, or non-admitted-provider exposure. Fast Downward simultaneously eliminates the excluded structure during translation, so no additional search advantage remains on the holdout. The resulting claim is not that GSC is a faster planner, but that explicit mission-conditioned domain synthesis creates a correctness, provenance, and accountability boundary whose computational benefit depends on the downstream planning stack.

---

## 11. Appendix / reviewer audit table

The v0.3 appendix states:

- “Evaluation completeness PASS WITH EXTERNAL-VALIDITY GAP”;
- “add an external planner/public benchmark for stronger venue positioning.”

These entries are obsolete.

Replace with:

| Dimension | v0.4 assessment | Remaining action |
|---|---|---|
| Contribution | PASS WITH NARROW CLAIM | Keep novelty on mission-conditioned Provider–Action admission |
| Controlled mechanism evidence | PASS | Preserve E1 same-cardinality falsification |
| Public-topology evidence | PASS | Keep E5 as topology stress test |
| Independent external validity | PASS | E6b run 37713826709 closes planner/validator gate |
| Computational generalization | BOUNDED | Report E6b mature-planner null explicitly |
| Field validity | NOT ESTABLISHED | Do not introduce field-performance language |
| Freshness optimality | NOT ESTABLISHED | Keep revision-only false blocks as limitation |

---

## 12. Stop rule

After the above edits, the experimental evidence package for Paper 1 should be considered complete.

The next step is **full-text v0.4 integration and adversarial review**, not further benchmark expansion.
