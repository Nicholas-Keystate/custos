# Custos 4.2 seed — one conformance predicate

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges finding #9 only. Executed under ruling R5 of the
> ruling record of 2026-07-30 (sha256 45a6d7208f0faca82946f2bfacb
> 04799994b5cf2c9afdef53f24def9d8cf8552), with the predicate's
> vocabulary settled by supplement 1, C-1, its refusal component
> given its object by 11a, and its law head extended by R20, both
> of supplement 2 of 2026-08-01 (sha256 7c5f6491976bd5fb12dcbab4c
> 1520002f9f5a1cdf9bf94dc2f0964bb1aea2670). Offered to the
> drafting authority, which owns the wording.

---

## What this seed carries

Three sites state the conformance obligation and they state three
different predicates. This seed unifies them on one, and defines
that one where the document currently has no definition at all.

The unification is the ruling's real content. The choice of
*which* predicate is second-order, and the ruling makes it in a
way that costs nothing later: semantic full-payload equality now,
byte-identity by construction once the carriage encoding lands.

The carriage encoding itself is **not** pinned here. R5 routes it
to its own design round, and this seed must not be read as
prejudging it.

## The three sites

**Section 2 (L422–424).** Cited, not edited.

> The GARD's defining obligation is replay: a conforming domain
> MUST make every judgment it issues recomputable,
> byte-identically, by any verifier holding its committed logs.

**Section 7.3 (L1038).** Cited, not edited.

> Two evaluations of the same triple SHALL return byte-identical
> findings.

**Section 16 (L2139–2142).** Cited, not edited.

> cross-implementation interoperability (two independent
> implementations deriving equal corpus identities, admission
> sets, refusal grounds, and cited law heads from one committed
> corpus in both presentation orders)

**The defect.** Sections 2 and 7.3 make byte-identity the
class-defining obligation. Section 15 leaves the carriage encoding
an undesigned deliverable, so byte-identity has no referent yet —
there are no bytes to be identical in. Section 16 then tests
something else entirely: four equalities, none of which is
byte-identity and one of which is not on the other lists at all.

The section 16 list is also short in a way the tracker has already
demonstrated. **It does not include the findings themselves.** Two
implementations can derive equal corpus identities, equal
admission sets, equal refusal grounds and equal cited law heads
while emitting different findings — which is exactly what happened
in finding #27, where two blind engines emitted different `pending`
findings from one committed input. That divergence would have
passed section 16's discharge test.

## Repair — one predicate, defined once

**Replacement, stated once and cited by all three sites.**

> **The conformance predicate.** Two folds agree when they agree
> on the full payload of every finding they return. Agreement is
> tested component by component over:
>
> - the finding value;
> - where the value is self-convicted, its kind;
> - the grounds, in canonical order;
> - the typed requirement set, including each element's species;
> - the refusal grounds, with the seal kind named, where refusal
>   fires;
> - the cited law head, including the external-specification
>   revision digests it commits;
> - the corpus identity, which carries the admission set.
>
> **Admission sets are compared through corpus identity.** Section
> 16's fourth criterion is neither dropped nor duplicated here. An
> admission set — which committed events the substrate's own
> admission mechanics accepted into the corpus — is a constituent
> of corpus identity, because two implementations with different
> admission sets cannot derive equal corpus identities. Section
> 16's own enumeration keeps admission sets named explicitly, as
> the ratified text already has them, so an implementer meets the
> criterion where it is testable and the predicate computes it
> once.
>
> **Equal semantics pins are a precondition of comparison, not a
> component of it.** The law head commits the revision digests of
> every external specification whose semantics the fold consumes.
> Two engines pinning different revisions of the
> superseding-recovery calculus are appraising under two
> different law heads; they are not two folds of one triple, and a
> difference between their findings is not a conformance failure.
> A harness SHALL establish equal semantics pins before it
> compares, and a divergence report over unequal pins SHALL say
> so.
>
> Until the carriage encoding of this document's object classes
> is ratified, this predicate is the obligation, and it is
> semantic: two folds satisfying it conform, whatever
> serialization each uses internally.
>
> **Byte-identity is the same predicate at the layer that does not
> exist yet.** The moment an encoding is ratified, byte-identity
> follows by construction rather than by a new requirement — the
> semantic components above determine the finding uniquely, so two
> conforming folds have nothing left to differ about except the
> encoding, and the encoding is then pinned. Sections 2 and 7.3
> state the obligation in its byte form as a forward commitment;
> this section states what discharges it today.
>
> **Comparison grade.** A comparison between two folds is
> byte-grade only where both use one ratified encoding, or one
> engine compares against itself under a pinned fixture-local
> serialization. Every other comparison is semantic-grade. **A
> divergence report SHALL state its grade**, because a byte
> difference under two different serializations is not evidence
> of nonconformance and a report that omits the grade cannot be
> read.

**Ground for the convergence claim.** Byte-identity as a forward
commitment is only honest if nothing semantic is left undetermined
when the encoding arrives. Three rulings closed the known sources
of semantic variance:

- **R2** — a fold may not return a terminal value with an
  enumerated check unexamined, so the defeat citation is
  deterministic at a fixed triple rather than a function of
  examination order.
- **R3** — species enters the dedup and sort keys, so the
  requirement set is total over the element and two engines cannot
  emit sets of different cardinality or different order.
- **R4's ordering wall**, with the canonical-order seed's byte
  comparison rule beneath it, so every ordering a fold consumes is
  derivable from committed bytes.

With those closed, the finding is unique up to serialization. That
is what makes the byte-identity sentence a commitment rather than
a hope, and it is why this seed does not weaken sections 2 and 7.3
— it states them at the layer that exists.

**Ground for the section 16 repair.** The discharge criteria are
widened to the predicate above, so the interoperability
deliverable is discharged by testing what the document is actually
about. A discharge test that would have passed #27 was not testing
the class-defining obligation.

## What is not in this seed

**The carriage encoding is not pinned.** R5 routes it to a design
round in a group setting rather than settling it, because the "one
decision" is several — serialization kind, field schemas still
moving under R6, R8 and R10 and the dossier question, SAID
coverage, versioning, and genus composition with the ilk-table
seats — and because section 15's own ratified text routes that
deliverable through review by others entering as findings.

This seed is written so that it stays correct under every outcome
of that round. It names no serialization, no field layout, no
digest coverage, and no genus.

## Notes for the drafting authority

Some things surfaced in drafting that finding #9 did not name.

1. **The vocabulary is settled, and the seed's assumption was
   right.** The ruling's enumeration said "refusal class where
   refusal fires"; the document has no such term. Section 16 says
   "refusal grounds", and section 9 (L1322–1325) names three
   refusal kinds by seal — digest mismatch, coordinate mismatch,
   clause violation — and rules that a record blurring them is
   unauditable. Supplement 1, C-1, corrects the enumeration to
   **refusal grounds, with the seal kind named per section 9's
   three-kind discipline**: the same commitment under its ratified
   name, and the component above carries both halves. Nothing new
   was meant, and nothing new is introduced.

2. **The refusal component now has its object.** This clause makes
   refusal a compared component, and until 11a was ruled two
   engines could agree on every finding and still differ on what
   they were comparing. Supplement 2 settles it: if any component
   of a compound invocation refuses, the invocation refuses; the
   refusal record cites the components already computed, which
   stand as ordinary findings at their own coordinates; and no
   product object ever contains a refused coordinate. Section
   7.5's own words — "the evaluator SHALL refuse the invocation" —
   were pointing at that reading, and the codomain wall is what
   forecloses the other one. The compared object is therefore
   determinate: a refusal record with grounds and seal kind, plus
   the findings that were computed.

3. **The convergence argument's third leg holds.** It depends on
   R4's ordering wall surviving as this seed reads it, and the
   record's annotation marking that wall retyped by R9 put the leg
   in doubt. Supplement 1, E-1, resolves it as an erratum: R9
   retyped exactly one wall — first-seen survival — and the
   canonical-ordering wall stands precisely as R4 adjudicated it.
   So every ordering a fold consumes remains derivable from
   committed bytes, and byte-identity still follows by
   construction once an encoding lands.

4. **The grade discipline needs somewhere to live besides prose.**
   "A divergence report SHALL state its grade" is a requirement on
   a report, not on a fold, and nothing in the document defines a
   divergence report. Either the conformance-vector companion
   (#15) owns the report format and this sentence cites it, or the
   sentence should be softened to a SHOULD until something can
   enforce it. As written it is a `SHALL` with no verifier.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Executed under | Ruling record 2026-07-30, sha256 `45a6d7208f0faca82946f2bfacb04799994b5cf2c9afdef53f24def9d8cf8552` — R5; vocabulary settled by supplement 1 C-1; refusal object by supplement 2 11a; law head extended by supplement 2 R20, sha256 `7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670` |
| Findings discharged | #9 (three predicates, one obligation) |
| Re-ruling | No |
| Depends on | R2, R3, R4 — the convergence argument's three legs |
| Open inside the seed | None — admission sets resolved through corpus identity (C-1), refusal component resolved by 11a |
| Explicitly not settled | the carriage encoding — routed to its own design round, tracked at #57 |
| Unblocks | #11, #14, #15 |
| Status | Unpinned draft; enters the 4.2 candidate by succession |
| Ratified bytes altered | None |
