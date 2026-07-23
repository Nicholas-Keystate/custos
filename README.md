# Custos

**An open standard for Governed Autonomic Replayable Domains (GARDs)
on KERI.**

> **Abstract** — A governance layer for KERI-based identifier
> infrastructure is presented. KERI settles who speaks for an
> identifier: key state committed to witnessed, end-verifiable
> logs; duplicity — two voices at one coordinate — evident to any
> observer holding both; recovery provided at the key tier; the
> trust decision ruled in KERI's own words (an honest validator
> MUST NOT trust key state carrying unreconciled evidence of
> duplicity). There KERI deliberately stops. Whether a duplicitous
> authority keeps its seat, whether acts it signed retain standing,
> what a counterparty is owed once trust is withdrawn — these are
> law above key state, and KERI imposes none; every consuming
> system improvises its consequences, and improvisation does not
> compose. This document presents the GARD — Governed Autonomic
> Replayable Domain — which extends end-verifiability from control
> provenance to governance provenance: law, evidence, and judgment
> as committed bytes under one identifier, every judgment
> recomputable by any verifier holding the logs. Ambient
> verifiability, carried from key state to judgment. KERI detects;
> a GARD appraises. The boundary between those two verbs is the
> boundary of this document: everything below it belongs to the
> substrate and is cited, never restated; everything above it is
> specified here.

## Why "Custos"

*Custos* is Latin: the guard, the keeper. The classical question —
*quis custodiet ipsos custodes?*, who guards the guardians? — is
the question this standard exists to answer mechanically. Custos's
answer: the committed log guards the guardian, because the
guardian cannot speak except onto the record. **Custos** names the
standard; **GARD** names the object class it defines. The pairing
follows the substrate's own convention: KERI is the protocol's
name, AID is what it mints.

The smallest GARD is one identifier that has committed how it will
behave and keeps the receipts — one key state, one page of law,
one log binding them. An ecosystem-scale authority and a single
person's identifier are the same species at different masses. The
specification opens with exactly this minimal case, before any
definition.

## Status

**Draft, pre-ratification.** The kernel at `spec/` is the
candidate text of Custos 4.0, through three first-round
adversarial reviews, two second-look reviews, and a succession-
completeness audit against its predecessor (all repairs executed
in bytes; see `PROVENANCE.md`). Ratification is an enactment in
the maintainers' governance event log; when it lands, this README
will carry the ratified digest and its enactment coordinate.

**This repository is a projection, never an authority.** Per the
specification's own succession clause: a repository or mirror
preserves history; *which bytes are law is computed from the
governance event log, never read off any mirror.* Verify, don't
trust: `python tools/verify_kernel.py`.

## Map

| Path | What |
|---|---|
| `spec/custos-4.0-kernel-draft.md` | The standard (15 sections; abstract above is its opening) |
| `SUCCESSION.md` | The detached succession record: predecessor digest, lineage, replay notes |
| `reviews/keri-native-review.md` | A full adversarial review of the kernel against the KERI/ACDC/CESR specification bytes — the contribution genre this project invites, exhibited |
| `reviews/sol-33-completeness-audit.md` | Succession-completeness audit of the predecessor against this edition |
| `reviews/migration-register-3.3-to-4.0.md` | Disposition register for the predecessor's content (ruling: publish-by-digest, no row-by-row migration) |
| `upstream/` | Questions addressed to adjacent communities (X.509 trust-route assumptions, for review) |
| `tools/` | Executable verification: conservativity gate + kernel digest checks (Apache-2.0) |
| `companions/` | Companion documents roadmap (GLEIF EGF mapping · philosophy · confidentiality & anchored delivery) |

## Contributing

**Findings, not edits.** See `CONTRIBUTING.md`. A finding is a
claim against committed bytes — a defect, a contradiction, a gap,
a failing vector. It names artifacts and coordinates, never
people. Ratified text is never edited; findings seed the next
candidate, which travels the same adversarial road this text did.

## License

Specification text: [Community Specification License 1.0](LICENSE.md).
Executable tooling: [Apache-2.0](LICENSE-CODE).
