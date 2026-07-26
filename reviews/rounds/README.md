# Adversarial round records

Each directory is a closed gauntlet round: briefs, the exact bytes
graded each leg (`doc-under-review*.md`), the reviewer's findings
and verdicts, tool snapshots, and a `MANIFEST.txt` of sha256
digests over every artifact.

**These files are sealed records — published byte-exact.** The
verdict documents contain absolute filesystem paths from the
drafting workspace (e.g. `/Users/…/standard-annealing/…`); those
strings are part of the sealed bytes and are preserved rather than
rewritten, because the MANIFEST digests bind the files as graded.
Resolve such paths against this repository's layout: the graded
candidate bytes are the `doc-under-review*.md` files beside each
verdict, and the ratified result is `spec/custos-4.1.md`.

Verify any round:

    cd reviews/rounds/<round-dir>
    shasum -a 256 -c MANIFEST.txt

Round index:

| Round | Subject | Verdict trail |
|---|---|---|
| `41-taxonomy-gauntlet-2026-07-25` | Chapter 1 seed (3 legs) | 11 findings → REPAIRS-FIRST → FIT-FOR-CANDIDATE |
| `41-candidate-gauntlet-2026-07-26` | Full 4.1 candidate (5 legs) | 5 MAJORs → 2 PARTIAL → 1 PARTIAL → 1 PARTIAL (tool-only) → FIT-FOR-CEREMONY |
