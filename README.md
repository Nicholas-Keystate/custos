# Custos

**An open standard for Governed Autonomic Replayable Domains (GARDs)
on KERI.**

> **Abstract** —
> 
> KERI detects; a GARD adjudicates. Key state infrastructure ends
> at a deliberately drawn line: an honest validator must not trust
> duplicitous key state — and nothing follows. Detection without
> consequence leaves every consumer of key state to improvise its
> own governance above that line, and improvisation does not
> compose. This standard specifies the layer that gives detected
> facts their consequence under committed law: the governed domain
> — a domain whose law is committed to a governance event log, the
> GEL; whose judgment is computed from that log by a fold, the
> Gever; and whose every act enters the record it is judged by.
> The property this yields is replayable governance: any stranger
> holding the logs computes the same Constitution, the same
> findings, the same refusals, byte for byte. Through adjudication
> a domain acts, and is held to account, by the same committed
> judgments.

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

**Ratified.** The edition of record at `spec/` is **Custos 4.1**,
ratified and effective 2026-07-26 by enactment in the maintainers'
governance event log — ratification anchored at KEL sn 187,
effectuation at sn 188, edition sha256
`ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05`.
Custos 4.0 (ratified 2026-07-23, sn 181/182) stands superseded
whole and byte-immutable at `spec/custos-4.0-kernel-draft.md`; the
full lineage, including the adopted-grade confession the
specification's own genesis knot requires of this domain, is in
`SUCCESSION.md`. The 4.1 text
reached ratification through a three-leg adversarial gauntlet on
its Chapter 1 seed and a five-leg full-document gauntlet
(convergence 5 MAJORs → 0, verdicts sealed; the complete round
records are in `reviews/rounds/`), atop 4.0's own three
first-round reviews, two second-look reviews, and
succession-completeness audit (`PROVENANCE.md`).

**This repository is a projection, never an authority.** Per the
specification's own succession clause: a repository or mirror
preserves history; *which bytes are law is computed from the
governance event log, never read off any mirror.* Verify, don't
trust: `python tools/verify_kernel.py`.

## Map

| Path | What |
|---|---|
| `spec/custos-4.1.md` | **The standard, edition of record** (Chapter 1 typing + 17 sections; abstract above is its opening) |
| `spec/custos-4.0-kernel-draft.md` | Predecessor edition, superseded whole, byte-immutable |
| `spec/custos-4.1-chapter1-seed.md` | The graduated Chapter 1 seed bytes (the census verifier checks 4.1's Chapter 1 is byte-exact to this) |
| `SUCCESSION.md` | The detached succession record: lineage 3.1→…→4.1, digests, anchor coordinates |
| `reviews/rounds/` | The 4.1 adversarial record: Chapter-1 gauntlet (3 legs) and full-document gauntlet (5 legs), sealed verdicts, round manifests |
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
