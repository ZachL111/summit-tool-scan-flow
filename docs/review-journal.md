# Review Journal

The review surface for `summit-tool-scan-flow` is deliberately narrow: one fixture, one scoring rule, and one local check.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its cli tools focus without claiming live deployment or external usage.

## Cases

- `baseline`: `file span`, score 127, lane `watch`
- `stress`: `terminal width`, score 196, lane `ship`
- `edge`: `argument risk`, score 158, lane `ship`
- `recovery`: `report density`, score 160, lane `ship`
- `stale`: `file span`, score 197, lane `ship`

## Note

The repository should be understandable without pretending it is larger than it is.
