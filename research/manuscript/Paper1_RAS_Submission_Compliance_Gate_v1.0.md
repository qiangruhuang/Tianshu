# Paper 1 — RAS / Elsevier Submission Compliance Gate v1.0

**Date:** 2026-10-08  
**Manuscript candidate:** `Paper1_Manuscript_v0.5.3_RAS.md`  
**Target:** *Robotics and Autonomous Systems* (Elsevier)

## Decision

**PASS WITH AUTHOR-METADATA BLOCKERS ONLY.**

No research, result, citation-content, or manuscript-structure change is required by the current submission-format audit.

## References

Elsevier's current *Your Paper Your Way* guidance states that there are no strict reference-formatting requirements at initial submission provided the reference style is consistent and sufficient bibliographic metadata are supplied; DOI inclusion is encouraged. Current manuscript: 19 references, all 19 cited, no missing citation numbers.

Detailed punctuation/journal-abbreviation normalization is therefore not a pre-submission scientific blocker. Recheck the live RAS portal at upload time for any journal-specific override.

## Tables

Five main tables are editable manuscript text, numbered/called out in sequence, and are not raster images. **PASS.**

## Main figures

Elsevier's current artwork guidance recommends EPS/PDF for vector graphs/technical drawings. Action completed:

- generator upgraded to `generate_paper_figures_v1_2.py`;
- five main figures now produce PNG preview + PDF vector + EPS vector;
- PDF outputs were rendered back to images and visually inspected with no clipping, overlap, broken symbol, or missing text;
- PDF/PS output requests embedded TrueType standard sans-serif fonts.

**PASS.**

## Highlights

Five Highlights, 70–79 characters each, no unexplained acronym, within Elsevier's general 85-character guidance. Elsevier requests a separate Word Highlights file at final-files stage; DOCX remains deferred under the project's Markdown-first approval gate.

**Content PASS; final file-format conversion pending approval.**

## Abstract

236 words; no citations; GSC defined at first use; includes purpose, controlled result, external validation, mature-planner null, and final claim boundary. **PASS.**

## Graphical abstract

A frozen brief exists. Final graphical-abstract production is optional/journal-workflow dependent and is not a scientific blocker.

## Data/code availability

Dedicated statement complete, with project-generated artifacts distinguished from third-party benchmark/tool sources. **PASS.**

## Remaining true blockers

1. author names/order;
2. affiliations;
3. corresponding-author details;
4. funding/grant statement;
5. CRediT contributions;
6. competing-interest declaration;
7. acknowledgements if applicable;
8. optional repository release/DOI decision;
9. final portal-specific upload check;
10. explicit approval before DOCX/PDF manuscript generation.

## Final status

**RAS submission engineering: PASS WITH AUTHOR-METADATA BLOCKERS ONLY.**

The experimental program remains closed.
