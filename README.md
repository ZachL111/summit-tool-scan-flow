# summit-tool-scan-flow

`summit-tool-scan-flow` keeps a focused Python implementation around cli tools. The project goal is to package a Python local lab for scan analysis with negative fixtures, human-readable error snapshots, and documented operating limits.

## Reason For The Project

This is intentionally local and self-contained so it can be inspected without credentials, services, or seeded history.

## Summit Tool Scan Flow Review Notes

For a quick review, compare `file span` with `file span` before reading the middle cases.

## What It Does

- `fixtures/domain_review.csv` adds cases for file span and terminal width.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/summit-tool-scan-walkthrough.md` walks through the case spread.
- The Python code includes a review path for `file span` and `file span`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## How It Is Put Together

The core code exposes a scoring path and the added review layer uses `signal`, `slack`, `drag`, and `confidence`. The domain terms are `file span`, `terminal width`, `argument risk`, and `report density`.

The Python code keeps the review rule close to the tests.

## Run It

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Check It

The same command runs the local verification path. The highest-scoring domain case is `stale` at 197, which lands in `ship`. The most cautious case is `baseline` at 127, which lands in `watch`.

## Boundaries

No external service is required. A deeper version would add more negative cases and a clearer boundary around invalid input.
