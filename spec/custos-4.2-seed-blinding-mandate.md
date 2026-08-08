# Custos 4.2 seed — a blinding factor where the design already
# chose to withhold

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges finding #44 only. Executed under ruling R18 of the
> ruling record supplement 2 of 2026-08-01 (sha256 7c5f6491976bd5
> fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670), option A.
> Offered to the drafting authority, which owns the wording.
>
> The mechanism is **cited, not reinvented**: the substrate's
> credential layer already specifies a blinding-factor discipline
> and states why it is needed. This seed makes it required in one
> scoped case and designs nothing.

---

## What this seed carries

One ruled span, scoped to the case where the design has already
chosen to withhold.

The document designs commit-now/disclose-later in several places
and never requires a blinding factor. Most governance evidence is
meant to be public and needs none. The finding bites only where
a SAID is committed while its preimage is deliberately held back
— and in exactly those places the hash is being asked to do
concealment work it cannot do unaided.

## Repair — the conditional mandate

**Ratified spans.** Cited, not edited. The edict's identity
(L849–853):

> - **Edict** — a committed governance act of one frame: a bare
>   SAID-addressed content (never an issuer-bearing container;
>   the center is the SAID), sealed by a GEL event at a
>   coordinate …

The typing clause that permits but does not require the field
(L898–901). The digest seal, which commits bytes that need not
travel (L1299–1302). The contest window (L1403–1404):

> - **when effective** — from immediately to after a contest
>   window measured in log positions, never in wall-clock time;

The anchor grade that makes the commitment maximally visible
(L1357–1360):

> Designated act classes — charter, revocation of a seat,
> enactment amending law, and the succession acts of section 16 —
> SHALL anchor in establishment events.

And section 6's undisclosed spans (L918–920), which are appraised
by the ordinary pending species.

**The defect.** A case-insensitive search of all 2471 ratified
lines for `entropy`, `nonce`, `uuid`, `salt` or `blinding`
returns zero matches. Two conforming implementations — one
blinding, one not — both satisfy section 6's typing SHALL, so the
divergence is silent uncommitted latitude under section 14's own
interpretive-latitude duty (L2023–2032).

**Replacement — a clause in section 6's object typing.**

> Any object whose self-addressing identifier is committed in
> advance of its intended disclosure SHALL carry a
> substrate-grade blinding factor, in the credential layer's own
> discipline for that field. An object born disclosed is exempt:
> where the content travels with, or before, its identifier,
> there is no preimage to guess.

## Ground — governance preimages are near the worst case

The substrate's credential layer is explicit that a
self-addressing identifier conceals only when the content it
ranges over carries entropy; without it an adversary may
reconstruct block contents from the identifier and the schema by
rainbow or dictionary attack.

*Marked, and not verified here.* That statement is relayed from
finding #44, which quotes the ACDC specification at
`spec-body.md:89` @ `f96ef54` and records verification against
upstream main on 2026-07-30. No checkout of that specification is
present in this repository's environment, so the quotation is not
re-verified in this seed. The drafting pass should re-verify
before the clause travels, and R20's semantics pin is the
mechanism by which the revision it verifies against stops being
ambient.

Governance content is close to the worst case for that attack,
and each of the three factors is a property this document
committed on purpose:

- **The seat roster is public in the GEL**, because law is
  committed and replayable.
- **The act kinds come from a closed table**, because section 17
  makes the grammar committed law rather than convention.
- **The coordinate is public**, because a position is a log
  coordinate in committed order.

So the search space is roster × act-kind × coordinate — trivially
small against a 256-bit digest. The very properties that make the
domain replayable are what shrink the preimage space, which is
why this cannot be left to a deployment profile to notice.

## Ground — a contest window that advertises its own subject

The concrete case is the one the finding exhibits, and it is
built entirely from ratified clauses.

A domain commits a contest window on seat revocations, measured
in log positions. A revocation edict is anchored and, by the
anchor-grade rule, lands in an establishment event — maximally
visible and non-erasable. Its identifier is public immediately
while the preimage is withheld. The target grinds the small
candidate space, recovers the content, and spends the full
contest window acting on it, while the frame believes the act is
committed-but-undisclosed.

That is **fail-silent confidentiality**: a guarantee that is
absent without any signal that it is absent. R15's fail-loud law
must-rejects exactly this class one layer up, where a membership
rule that can yield a proper subset without a refusal is
inadmissible. The same standard applied to disclosure gives the
mandate: a withheld preimage either is concealed or fails
visibly, and an unblinded SAID over a small space does neither.

## The confessed limit

> Blinding guards the preimage. It does not guard the traffic
> pattern: that an anchor exists, at which coordinate, in which
> act class, and at which anchor grade remains visible to every
> observer, and no clause of this document conceals it.

The limit belongs in the text rather than in a companion, because
a reader who has just been told that withheld content is blinded
will otherwise infer more privacy than the design delivers. And
the visibility is not a leak to be regretted: anchor existence
and grade are what make the record auditable, and the medium
being honest about what it publishes is the property the rest of
the standard is built on. What is repaired is a case where the
document promised concealment it could not deliver; what is not
repaired is the metadata the document never promised to conceal.

## Composition

**With #48's bare-SAD shape.** The finding's own note is that a
blinding field on a bare self-addressed data item is exactly the
shape #48 is examining for framability. The mandate does not
prejudge that work: it requires the field, in the substrate's own
discipline, and leaves the wire question to the carriage findings
and the encoding round.

**With section 6's disclosure posture.** The kernel commits the
full-disclosure baseline and scopes confidentiality profiles to
deployment law (L910–922). The mandate does not disturb that: it
does not require anything to be withheld. It says that where
something *is* withheld, the withholding must be real.

**With R19, if it lands on the `(td, ts)` track.** The docket's
own note on R19 observes that the blinded update form is a
privacy gain and should be weighed against R18. If governance
acts come to travel with their content inside a blind by default,
the mandate's scope narrows to the objects still committed bare.
That is a shrinking of the clause's reach, not a conflict, and
the clause as drafted needs no amendment for it.

## Notes for the drafting authority

Things surfaced in drafting that R18 did not name.

1. **"In advance of its intended disclosure" needs a decidable
   reading, and the honest one is producer-side.** No verifier can
   tell from bytes whether a producer intended to disclose later,
   so the clause cannot be a verifier-checkable predicate in the
   way section 17's must-reject vectors are. What a verifier can
   check is the contrapositive at the sites the document already
   names — a contest window is open, a cone span is withheld —
   and a drafting pass should decide whether the mandate is
   stated over producer intent (a duty, breach-convictable when
   exhibited) or over those enumerated sites (checkable, and
   narrower). The seed drafts intent and flags that the vector
   story differs between the two.

2. **The existing confidentiality companion cannot discharge
   this.** `companions/confidentiality-and-anchored-delivery.md`
   describes the terrain well and is informative; an informative
   companion cannot fill a normative gap, and the docket says so.
   Recorded because the companion's existence is the most likely
   reason a reader would think the gap already closed.

3. **The mandate creates a new must-reject and the sitting
   assigns it no vector.** R18 is the one ruling in the sitting
   with no station obligation listed, and a clause with a SHALL
   and no discriminating record is, by section 17's own sentence,
   a guard that has never been shown failing (L2303–2306). A
   natural vector exists and is cheap: an object committed in
   advance of disclosure without a blinding factor, expected
   must-reject. Whether it is owed is the authority's call; the
   asymmetry with the other six rulings is recorded rather than
   resolved.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Executed under | Ruling record supplement 2, 2026-08-01, sha256 `7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670` — R18, option A |
| Finding discharged | #44 (commit-now/disclose-later with no blinding factor) |
| Mechanism | The substrate credential layer's blinding-factor discipline — cited, not reinvented |
| Unverified citation | The ACDC rationale is relayed from #44's verification at `f96ef54` and **not re-verified here**; no checkout of that specification is present |
| Composes with | #48 (bare-SAD shape); R19's blinded-update track, if it lands |
| Re-ruling | No |
| Station obligations | None assigned by the sitting; one candidate vector recorded in the notes |
| Ratified bytes altered | None |
