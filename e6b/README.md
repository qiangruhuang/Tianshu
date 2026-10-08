# E6b — Frozen Confirmatory External-Validity Gate

This directory preserves the confirmatory E6b research package without re-serializing any frozen scientific asset.

## Scientific status before GitHub execution

- Native-semantics static audit: complete.
- Cross-implementation Python vs JavaScript oracle agreement: complete.
- 136/136 native goals have at least one witness.
- Object-level admission mismatch: 0.
- Admitted resources: 58/58 rovers, 60/65 cameras, 47/58 stores.
- Fast Downward 26.6 + VAL confirmatory outcome: **not yet opened at repository bootstrap**.

E6b must not be called PASS until the frozen runner executes with the specified planner and validator.

## Byte-preserved research bundle

Original bundle:

`E6b_External_Validity_Gate_Research_Bundle_v1.1.zip`

SHA-256:

`8ff25602bcabc58eed52b781d882d51966dd02dc28b02ebf77db1166ca59d9ac`

The ZIP is stored as six Base64 text segments because the GitHub connector used for project synchronization writes UTF-8 files. The workflow concatenates the segments in lexical order, decodes the ZIP, verifies the SHA-256 above, and only then extracts the scientific assets.

| Segment | SHA-256 |
|---|---|
| `bundle_parts/part-00.b64` | `64fc756b8b11014958f6fa155a9df2b082cedea7e0fb39230219884d0e89ecb4` |
| `bundle_parts/part-01.b64` | `8c2709795ab117103a641fda1eb5aaffb814b8f1558081b3d957525705d8ac2d` |
| `bundle_parts/part-02.b64` | `1b5ab65243dbe2a72bcb774a846bd63bf51dcbcb790e1fb8168460ae3e6a15ab` |
| `bundle_parts/part-03.b64` | `fcfb886b9e786cf5073feb89640c6a1588c630108a0d303cb1e78a65147b27de` |
| `bundle_parts/part-04.b64` | `1fda020d013a8967127bd8659d91c8ef3b7624001975ee1bcfba5b5a0cadad3c` |
| `bundle_parts/part-05.b64` | `91d71461bbe39cdf043ec963dba251b496139744865c40731bb8a99c19e8a0e7` |

## Frozen files inside the bundle

- `E6b_Rovers_Native_Semantics_Confirmatory_Freeze_v1.1.md`
- `E6b_Independent_Oracle_Manifest_v1.0.json`
- `E6b_Cross_Implementation_Oracle_Audit_v1.0.md`
- `run_e6b_external_validity_gate_v1_1.py`
- `generate_e6b_independent_oracle.mjs`
- `E6b_Runbook_v1.1.md`
- `Paper1_E6b_Integration_Patch_v0.1.md`
- `E6b_Research_Checkpoint_v1.1.md`
- `E6b_ARTIFACTS_SHA256.txt`

`E6b_ARTIFACTS_SHA256.txt` is verified after extraction. The runner itself also pins the independent-oracle manifest hash and checks benchmark Git blob identities.

## Frozen external identities

- IPC-3 Rovers benchmark repository: `aibasel/downward-benchmarks`
- benchmark commit: `e21d49c2cb61d147a46c5966f2581bf6fd422b9f`
- holdout: `p09.pddl`–`p20.pddl`
- Fast Downward: `26.6`
- search configuration: `--alias lama-first`
- per-run time limit: `300 s`
- per-run memory limit: `4 GiB`
- VAL commit: `3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4`

## Frozen gate criteria

PASS requires all of the following:

1. source identities verified;
2. independent-oracle mismatch = 0;
3. Fast Downward reports 26.6;
4. VAL checkout matches the frozen commit;
5. at least 10/12 Full-domain problems solved under the fixed resource cap;
6. Full-solved → GSC-unsolved regressions = 0;
7. VAL failures for returned GSC plans = 0;
8. non-admitted-provider action exposure = 0.

If fewer than 10 Full-domain instances are evaluable, the frozen runner returns `INCONCLUSIVE`. Otherwise any logic/validation regression produces `FAIL`. Search speed is secondary and is **not required** for PASS.

## Outcome-blindness rule

Do not change the corpus, semantic admission rule, planner alias, resource limits, validator commit, or PASS threshold after observing planner outcomes. A technical CI failure is not a scientific FAIL/INCONCLUSIVE result unless `gate_summary.json` was produced by the frozen runner.
