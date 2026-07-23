# Custos

**An open standard for Governed Autonomic Replayable Domains (GARDs)
on KERI.**

> **Abstract** —
> 
> This document presents the GARD — Governed Autonomic
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
standard; **GARD** names the object class it defines. 

The smallest GARD is one identifier that has committed how it will
behave and keeps the receipts — one key state, one page of law,
one log binding them. An ecosystem-scale authority and a single
person's identifier are the same species at different masses. The
specification opens with exactly this minimal case, before any
definition.

## Status

**Ratified.** The kernel at `spec/` is Custos 4.0, ratified and
effective 2026-07-23 by enactment in the maintainers' governance
event log — ratification anchored at KEL sn 181, effectuation at
sn 182, kernel SAID
`ELDBQXbJ20g3K-MSIqvcz1z4dSzasKxx8FkBovmo8cF1`. The full record,
including the adopted-grade confession the kernel's own genesis
knot requires of this domain, is in `SUCCESSION.md`. The text
reached ratification through three first-round adversarial
reviews, two second-look reviews, and a succession-completeness
audit, all repairs executed in bytes (`PROVENANCE.md`).

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
