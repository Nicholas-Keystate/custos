# Adversarial review record — Custos 4.1

Two independent adversarial reviews of the ratified 4.1 edition,
run 2026-07-27 against `spec/custos-4.1.md` at sha256
`ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05`.

These are **post-ratification** reviews. They do not bear on 4.1's
ratification, which closed at KEL sn 187/188; they are findings
against the edition of record, and they seed the next candidate by
the route `CONTRIBUTING.md` describes.

## The two axes

They were run deliberately as a matched pair, on opposite priors,
and the useful signal is where they agree.

**Inside the substrate's assumptions.** A five-persona panel
reasoning within KERI's own doctrine — detection-not-prevention,
observer-local resolution, survivability rather than
invulnerability. Personas: protocol-security-verifier-realist
(SEC), kr-relation-algebra-theorist (KRT),
spec-precision-language-designer (SPC), first-principles-skeptic
(SKP), governance-interop-lifecycle-architect (GOV). Synthesis in
`keri-review-panel-custos-4.1.md`: 15 raw findings, 14 after
dedupe, 3 blockers, 0 refuted on verification.

**Rejecting them.** A single outside lens
(`dao-l2-outside-lens-custos-4.1.md`) prompted as a senior
DAO/Ethereum/L2-governance adversary, deliberately importing the
blockchain priors the KERI-native panel is instructed to refuse.
Its headline: Custos "has validity rules but no settlement layer."

Both stopped at the same place — the replay promise, and the
warranty economics that rest on a re-folding population that does
not yet exist. That two reviews built on incompatible foundations
converged there is the datum, more than either verdict alone.

## Files

| File | Axis |
|---|---|
| `keri-review-panel-custos-4.1.md` | Panel synthesis: executive verdict, findings table, machine-readable manifest |
| `protocol-security-verifier-realist-custos-4.1.md` | KERI-native (SEC) |
| `kr-relation-algebra-theorist-custos-4.1.md` | KERI-native (KRT) |
| `spec-precision-language-designer-custos-4.1.md` | KERI-native (SPC) |
| `first-principles-skeptic-custos-4.1.md` | KERI-native (SKP) |
| `governance-interop-lifecycle-architect-custos-4.1.md` | KERI-native (GOV) |
| `dao-l2-outside-lens-custos-4.1.md` | Outside lens (DAO / L2) |

## Preserved bytes

Per the convention in `reviews/rounds/README.md`, these files are
published as produced. They contain absolute filesystem paths from
the drafting workspace (`/home/daniel/code/…`, `/tmp/…`) and
target paths that resolve against a reviewer's local checkout of
the KERI specification repository. Those strings are preserved
rather than rewritten, because `MANIFEST.txt` binds the files as
reviewed. Resolve them against this repository's layout: the
reviewed bytes are `spec/custos-4.1.md` at the digest above.

The panel synthesis names its target as the KERI spec repo in the
`Targets:` field; that is the re-anchoring corpus the personas
read for substrate cross-reference, not the subject. The subject
is Custos 4.1 throughout.

## Verify

    cd reviews/keri-panel-custos-4.1
    shasum -a 256 -c MANIFEST.txt

## Disposition

Every finding was triaged and filed as an issue against this
repository; the tentative ones are marked as theories rather than
settled findings, per `CONTRIBUTING.md`'s standard that a claim
sourced from inference must say so.

| Issue | Severity | Finding |
|---|---|---|
| #2 | BLOCKING | Canonical defeat-selection is self-contradictory (SPC-F1) |
| #3 | BLOCKING | Pending payload ordering underspecified (not in the panel record; surfaced by applying SPC-F1's shape to the other ordering sites) |
| #4 | OBSERVATION | §3.2 pin discipline — tentative (SPC-F5) |
| #5 | OBSERVATION | "Predicate congruence" naming — tentative (KRT-F3) |
| #6 | BLOCKING | Self-conviction trigger vs required payload; antinomy (SPC-F2) |
| #7 | BLOCKING | No lawful motion for revocation of a grounding credential (KRT-F1) |
| #8 | MAJOR | Warranty framing unconditional at load-bearing sites (SEC-F1, GOV-F3) |
| #9 | MAJOR | Byte-identity predicate vs §16's semantic discharge test (SPC-F3, GOV-F2) |
| #10 | MAJOR | "Same refusals, byte for byte" vs refusal-is-not-committed (SPC-F4) |

Findings in the panel record not yet filed as separate issues —
KRT-F2 (no composition operator over the seven primitives),
KRT-F4 (§8 widens the ACDC operator codomain), SKP-F1 (motivating
harm not instantiated), SKP-F2 (composition claim overreaches the
frame boundary), GOV-F1 (governance-minted ilks consume the
substrate's shared wire namespace) — remain open in this record
and are candidates for triage.
