# Contributing to Custos

**This document is a projection of the contribution covenant, not
the covenant itself.** When this repository's governance event
log is live, the committed covenant governs and this file merely
mirrors it — per the standard's own rule: a repository preserves
history; what binds is computed from the committed log, never
read off a mirror. Until then, this projection is the working
statement of the membrane.

## The rule

**Contributors enter via findings, not edits.**

A finding is a claim against committed bytes: a defect, a
contradiction, a gap, a failing vector, an unlisted opening. It
names artifacts and coordinates — never people. File findings as
GitHub issues; substantial findings may arrive as pull requests
adding a review document under `reviews/` (the exhibit there,
`keri-native-review.md`, shows the genre: severity, line cite,
ground, and a repair *shape* — never a rewrite).

## What happens to a finding

```
finding → triage → ruling (maintainers' ratifying authority)
        → repairs executed under rulings → next candidate edition
```

Two hard properties of the pipeline:

1. **Ratified text is never edited.** Ratification binds content
   permanently; only succession supersedes it. Findings against
   the current edition seed the next candidate, which travels the
   same road this text did: candidate → adversarial review rounds
   → ratification → log-anchored effectuation. Merge commits that
   land candidate changes cite the ruling that authorized them.
2. **Findings on ruled material return for re-ruling — never
   silent repair.** If a finding touches wording the ratifying
   authority already ruled on, it is not quietly patched; it goes
   back up as a re-ruling question with the finding as evidence.
   The ruling trail is part of the record.

## Standards for findings

- **Cite bytes.** A finding lives or dies on its coordinates:
  file, line, quoted span. Claims without coordinates are
  discussion, not findings (discussion is welcome too — label it).
- **Repair shapes, not rewrites.** State what a repair must
  accomplish and why; the drafting authority owns wording.
- **Severity honestly.** BLOCKING (falsifies committed text or
  breaks replayability) / MAJOR (doctrine loss or contradiction) /
  MINOR (vocabulary, teaching, polish) / OBSERVATION.
- **Mark speculation.** A claim sourced from memory or training
  prior rather than the cited bytes must say so. Unmarked
  prior-claims are themselves a defect.
- **Artifacts, never people.** Findings attach to committed
  bytes. This is also the courtesy discipline: reviews of
  adjacent communities' work travel as questions to them, never
  as defect reports about them.

## Verification

Before filing a byte-level finding, verify you hold the bytes you
think you hold:

```
python tools/verify_kernel.py
```

## License

By contributing you agree your contributions to specification
text are licensed under the Community Specification License 1.0
(LICENSE.md) and contributions to tooling under Apache-2.0
(LICENSE-CODE).
