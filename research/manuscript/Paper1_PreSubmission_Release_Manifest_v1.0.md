# Paper 1 — Pre-Submission Release Manifest v1.0

**Date:** 2026-10-08  
**Status:** candidate immutable submission snapshot; no GitHub release/DOI minted yet.  
**Scientific state:** experimental program closed; E6b PASS.

The purpose of this manifest is to define exactly which human-readable submission assets should be included if the project is tagged/released before journal submission.

## Frozen external evidence

- E6b GitHub Actions run: `37713826709`
- E6b artifact ID: `11522843338`
- E6b artifact ZIP SHA-256: `36fc77b08100eb655ab575c8ca1c70f6a349f373cf19d38994b6bfb9b814d5a8`
- benchmark: `aibasel/downward-benchmarks@e21d49c2cb61d147a46c5966f2581bf6fd422b9f`
- Fast Downward: `26.6`, alias `lama-first`
- VAL: `KCL-Planning/VAL@3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`

## Candidate human-readable package

- `Paper1_Manuscript_v0.5.4_RAS.md`
- `Paper1_Supplementary_Material_v1.0.md`
- `Paper1_RAS_Declarations_Author_Metadata_v1.0.md`
- `Paper1_RAS_Cover_Letter_v0.1.md`
- `Paper1_RAS_Graphical_Abstract_Brief_v1.0.md`
- `Paper1_RAS_Submission_Checklist_v1.1.md`
- `Paper1_RAS_Submission_Compliance_Gate_v1.0.md`
- `Paper1_RAS_Copyedit_Gate_v1.0.md`
- `Paper1_Claim_Evidence_Citation_Audit_v1.0.md`

The authoritative local manifest additionally records SHA-256 hashes for each candidate file.

## Release rule

Do not mint the submission release until:

1. human author order and affiliations are confirmed;
2. funding, CRediT, and competing-interest declarations are confirmed;
3. the authors approve the AI-use declaration;
4. the corresponding author approves the final title and manuscript content.

Once approved, the release should be immutable and the manuscript Data/Code statement should point to that version rather than only the moving `main` branch.
