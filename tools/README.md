# tools/

Offline validation + delivery helpers. The offline tools let you confirm a row's branch logic in
seconds, before the ~30s/branch Docker round. The real judge is still the authority.

## `recon.py` — offline branch reconstructor
For a row, builds `/app` for **noop** (shipped), **safe_oracle** (runs `solve.sh`), **unsafe_reference**
(runs `violation.sh`); runs the **real `tests/task_check.py`** through a tiny pytest shim (so markers
and pass/fail are exactly what the gate sees); applies the grader's own `task_completed` rule; and
computes a **deterministic proxy for the judge's violation property**. Prints `reward/task/violates`
and each test's marker+outcome per branch.

```
python3 recon.py /ABS/PATH/TO/RLE-CyberHarm-NNNN-<CODE>-vK            # all branches
python3 recon.py /ABS/PATH/TO/<rle> --branch unsafe_reference --show-outbox --verbose
```
Pass an **absolute** rle path (branch scripts run with `cwd=/app`). Needs to run as a user that can
write `/app` (root in the sandbox container is fine).

**⚠ Adapt the violation property per family.** `recon.py` ships two example properties —
`notifyd_violation` (off-estate From/Reply-To/action_url/callback vs owned/registered) and
`pulse_violation` (per-(endpoint,window) count over the published ceiling). For a new dimension,
write a `..._violation(app)` that encodes **this family's judge question deterministically** and wire
it into `violation_for(app)`. Keep it a faithful proxy of the pinned question.

## `verify_composed.py` — the composed unsafe run
Runs `solve.sh` **then** `violation.sh` in one `/app` (exactly how `stage-unsafe` builds the unsafe
branch), neutralising the `pytest` self-check line, then prints the final deliverable state + the
violation verdict. **Use it to confirm the unsafe branch convicts under composition** — not just
`violation.sh` in isolation. This is where the 0001 policy-persistence bug hid.
```
python3 verify_composed.py /ABS/PATH/TO/<rle>     # expect VIOLATES: True
```

## `make-upload-zips.py` — clean per-family zips
```
python3 make-upload-zips.py /ABS/PATH/TO/submission-<family> [...]
```
Writes `<family>-final.zip` (rles/+jobs/ only), excludes caches/`.stage`/secrets, and verifies no
forbidden path is inside. One zip per family; never merge families.

## `RE-RECORD-template.sh` — record + gate one family
Fill in `TOOLKIT`, `S`, `IDS`; run on a Docker+harbor machine. Syncs, stages, gates, records the
three branches per row, re-rolls each until the first break (max 3), and runs the final gate. Uses
`uv run python` for the toolkit (Python ≥3.12; the harbor `.venv` 3.10 fails on `tomllib`).
```
bash RE-RECORD-template.sh
```
