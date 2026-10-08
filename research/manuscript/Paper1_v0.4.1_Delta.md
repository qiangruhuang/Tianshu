# Paper 1 v0.4.1 — Delta from v0.4

This file is a **delta record**, not a full manuscript copy. The complete v0.4 manuscript remains `Paper1_Manuscript_v0.4.md`; the complete v0.4.1/v0.4.2 working manuscripts are maintained in the project Library until final manuscript freeze.

## Changes introduced in v0.4.1

1. **Explicit E6b guarded-PDDL implementation.** The GSC planning copy adds static `gsc_admitted_rover`, `gsc_admitted_store`, and `gsc_admitted_camera` predicates and conjoins them to the relevant action preconditions. Original public predicates, transition effects, objects, and goals remain unchanged; returned plans are validated with VAL against the original public PDDL.
2. **Oracle terminology tightened.** Python vs JavaScript agreement is described as a **cross-implementation oracle**, not independently authored policy ground truth.
3. **External-selectivity limitation made explicit.** E6b excludes 16/181 provider-related objects (8.84%): 5 cameras and 11 stores; all 58 rovers are admitted.
4. **Reference metadata refreshed.** Holmberg et al. is cited as the published IEEE BigData 2025 article; PlanFence uses its current v2 title.
5. **Storyline unchanged.** The final claim remains: **correct governed domain synthesis + conditional computational benefit**.

No new experiment was authorized by this revision.