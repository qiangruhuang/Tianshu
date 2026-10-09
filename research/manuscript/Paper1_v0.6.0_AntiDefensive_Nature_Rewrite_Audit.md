# Paper 1 v0.6.0 — Anti-Defensive + Nature Writing/Polishing Audit

**Date:** 2026-10-09  
**Source:** `Paper1_Manuscript_v0.5.4_RAS.md`  
**Output:** `Paper1_Manuscript_v0.6.0_RAS_AntiDefensive_Nature.md`  
**Target journal:** *Robotics and Autonomous Systems*  
**Scientific-change status:** **NONE** — writing/organization only.

## Applied writing frameworks

1. **Anti-Defensive Writing** (`Adkid-Zephyr/anti-defensive-writing-Skill`): organize around the strongest defensible value, remove work-report chronology and self-undermining language, give each experiment one argumentative duty, and avoid manufacturing reviewer objections.
2. **nature-writing** (`Yuan1z0825/nature-skills`): rebuild the argument before polishing sentences; keep one central claim, the shortest sufficient evidence chain, and section-specific jobs.
3. **nature-polishing**: tighten paragraph logic and English prose while preserving facts, terminology, references, and evidence boundaries.

The target remains RAS, so Nature-derived rules were used as writing guidance rather than Nature journal formatting policy.

## Narrative changes

- Reframed the paper around **mission-conditioned Provider–Action domain membership as a runtime contract**.
- Replaced repeated “what GSC is not” language with positive positioning against semantic planning, runtime assurance, and planner preprocessing.
- Reorganized Introduction around problem → gap → mechanism → causal evaluation → external gate.
- Rewrote Related Work as relationship-based synthesis instead of defensive novelty disclaimers.
- Preserved E6b's mature-planner null but recast it as a **planner-preprocessing boundary condition** that explains when semantic admission produces additional search savings.
- Replaced the 10-item `Threats to validity` inventory with a four-paragraph, claim-specific **Scope of inference** section.
- Shortened Conclusion to reinforce the paper's central memory point without reopening a list of weaknesses.
- Renamed E6a/E6b Results headings to describe what each experiment establishes rather than what it “fails” to show.

## Main-text compression

| Section | v0.5.4 words | v0.6.0 words | Change |
|---|---:|---:|---:|
| Abstract | 237 | 247 | +10 |
| Introduction | 743 | 599 | -144 |
| Related Work | 901 | 713 | -188 |
| Results | 1922 | 1899 | -23 |
| Discussion | 1225 | 674 | -551 |
| Conclusion | 210 | 159 | -51 |

The largest reduction is in Discussion, where Results replay and reviewer-facing self-audit were removed while conclusion-changing boundaries remained visible.

## Defensive-language audit

| Phrase family | Before | After |
|---|---:|---:|
| `does not` | 7 | 1 |
| `do not` | 3 | 1 |
| `cannot` | 2 | 1 |
| `rather than` | 17 | 6 |
| `not a` | 8 | 3 |
| `not establish` | 3 | 1 |
| `not claim` | 1 | 0 |
| `insufficient` | 4 | 0 |
| `negative design` | 1 | 0 |
| `deliberately` | 6 | 1 |
| `intentionally` | 4 | 1 |
| `weaker` | 1 | 0 |
| `limitation` | 4 | 1 |
| `threats to validity` | 1 | 0 |

## Scientific regression checks

- Key frozen numerical/toolchain anchors missing after rewrite: **0**
- Missing anchors: `[]`
- Reference entries present: **19**
- Cited references without entries: **[]**
- Reference entries unused in text: **[]**
- Source SHA-256: `817e3d4ab99441353246dc7d0e54a25c7fcb241279eed90aa71d74b56d0894aa`
- Output SHA-256: `7d20b5f09a0f335834fb1a2fcc92460de7f13a789ce796f5ba6c13bf6dee2298`

## Evidence preserved in main text

The rewrite retains the E1 same-cardinality falsification, E3 ablation failures, E4 configuration transfer, E5 q=0 reductions and q=1 convergence, E6a low-selectivity pilot, E6b 12/12 Full and GSC solves, zero VAL failure, zero non-admitted-provider exposure, 16/181 native provider exclusions, the Fast Downward identical-effective-task result, and all frozen source/toolchain identities.

## Submission-layout QA

- Final submission DOCX rendered to **21 pages**.
- All 21 pages visually inspected via contact-sheet plus page-level checks.
- Five figures and five tables render without clipping or overlap.
- Inline and display mathematics render correctly after normalizing Pandoc math delimiters.
- PDF preflight: openable, unencrypted, 21 pages, text-based (not scanned).

## Final storyline

> **GSC makes mission-conditioned Provider–Action membership an auditable runtime contract; semantic admission reduces search when governance-invalid structure survives downstream planner preprocessing.**
