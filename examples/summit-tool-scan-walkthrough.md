# Summit Tool Scan Flow Walkthrough

This note is the quickest way to read the extra review model in `summit-tool-scan-flow`.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | file span | 127 | watch |
| stress | terminal width | 196 | ship |
| edge | argument risk | 158 | ship |
| recovery | report density | 160 | ship |
| stale | file span | 197 | ship |

Start with `stale` and `baseline`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

The next useful expansion would be a malformed fixture around terminal width and report density.
