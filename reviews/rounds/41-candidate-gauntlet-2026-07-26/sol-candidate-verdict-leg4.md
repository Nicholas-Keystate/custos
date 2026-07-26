Verdict: **REPAIRS-FIRST**

## Part A — repair grades

| Repair | Grade | Finding |
|---|---|---|
| R-A2 — structure-verifier discrimination | **PARTIAL** | The fifteen predecessor disposition rows are now strongly verified, but the additions asserted by the structure census remain unverified. |
| R-A3 — usage/docstring | **COMPLETE** | The docstring predeclares first-match assignment and documents only `--expect-digest` ([census-41-r4.py:12](</Users/hun-magnon/Documents/KERI/standard-annealing/reviews/rounds/41-candidate-gauntlet-2026-07-26/census-41-r4.py:12>), [census-41-r4.py:16](</Users/hun-magnon/Documents/KERI/standard-annealing/reviews/rounds/41-candidate-gauntlet-2026-07-26/census-41-r4.py:16>)). Argparse matches that interface ([census-41-r4.py:166](</Users/hun-magnon/Documents/KERI/standard-annealing/reviews/rounds/41-candidate-gauntlet-2026-07-26/census-41-r4.py:166>)). |
| R-A4 — exactly-one prose | **COMPLETE** | The appendix accurately attributes uniqueness to predeclared first-match order, without claiming classifier mutual exclusivity ([doc-under-review-r4.md:2330](</Users/hun-magnon/Documents/KERI/standard-annealing/reviews/rounds/41-candidate-gauntlet-2026-07-26/doc-under-review-r4.md:2330>)). |

Pinned-byte checks passed:

- Graded document: `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05`
- Both census scripts: `2def3bc7cf900855fe555fce772ad5343f8bce604f4ee022a203ff7fd3768f4b`
- Script copies are byte-identical.
- Unpinned mode: exit 0.
- Correctly pinned mode: exit 0.
- Wrong digest: exit 1.

The green census recomputed 1,546 predecessor nonblank lines, 181 deltas, all eight stated group totals, and zero unexplained.

### R-A2 discrimination confirmed

The verifier parses fifteen rows and compares predecessor numbers, byte-exact titles, `n+1` targets, and candidate headings ([census-41-r4.py:92](</Users/hun-magnon/Documents/KERI/standard-annealing/reviews/rounds/41-candidate-gauntlet-2026-07-26/census-41-r4.py:92>)).

The original passed. Independent in-memory mutations all refused:

- Renamed mapped heading
- False disposition target
- Renamed structure-census heading
- Falsified table title
- Deleted row
- Extra row
- Missing mapped heading
- Falsified group total

Thus the r3 under-discrimination over the fifteen predecessor rows is repaired.

## Part B — residual promise/behavior gap

The appendix defines the structure census more broadly than those fifteen rows. It expressly accounts for the candidate head, introduction, Chapter 1, section 9 additions, section 17, and the appendix, concluding “zero additions unaccounted” ([doc-under-review-r4.md:2447](</Users/hun-magnon/Documents/KERI/standard-annealing/reviews/rounds/41-candidate-gauntlet-2026-07-26/doc-under-review-r4.md:2447>)). The preamble says the committed generator verifies “the structure census” against final bytes ([doc-under-review-r4.md:2321](</Users/hun-magnon/Documents/KERI/standard-annealing/reviews/rounds/41-candidate-gauntlet-2026-07-26/doc-under-review-r4.md:2321>)).

The code verifies only:

- The fifteen predecessor mappings to candidate sections 2–16
- Presence of section 17 with `GEL` somewhere in its heading
- Presence of the literal `### Structure census`

It does not verify the candidate head, introduction, Chapter 1, the claimed Chapter 1 seed digest, section 9 additions, or the appendix’s additions inventory. In-memory mutations independently showed that all of these still pass structure verification:

- Rename Chapter 1’s first heading: **PASS**
- Delete Chapter 1 whole: **PASS**
- Rename the candidate head: **PASS**
- Delete the Introduction heading: **PASS**

Consequently, the executing-code correspondence is:

- Delta census: **confirmed**
- Total and eight group counts: **confirmed**
- Fifteen predecessor rows/titles/targets/headings: **confirmed**
- Full stated structure census, especially “zero additions unaccounted”: **not confirmed**

This is blocking because the verifier prints the unqualified result “structure census verified” ([census-41-r4.py:226](</Users/hun-magnon/Documents/KERI/standard-annealing/reviews/rounds/41-candidate-gauntlet-2026-07-26/census-41-r4.py:226>)) after accepting deletion of an addition that the structure census expressly accounts for.

No ceremony checklist applies under **REPAIRS-FIRST**.

Strongest reversal consideration: read “structure census” narrowly as only the fifteen predecessor disposition rows requested by R-A2. That reading makes R-A2 complete, but it cannot sustain FIT because the appendix itself includes and closes an additions census under the same heading, while the preamble and success output qualify neither claim.