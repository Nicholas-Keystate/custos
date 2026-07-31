# Custos 4.2 seed — one conformance predicate

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges finding #9 only. Executed under ruling R5 of the
> ruling record of 2026-07-30 (sha256 45a6d7208f0faca82946f2bfacb
> 04799994b5cf2c9afdef53f24def9d8cf8552). Offered to the drafting
> authority, which owns the wording.

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
> - the refusal grounds, where refusal fires;
> - the cited law head;
> - the corpus identity.
>
> [OPEN — section 16's ratified discharge criteria include
> **admission sets**, which this enumeration does not name.
> Whether an admission set is carried inside the grounds and is
> therefore already tested, or is a distinct component that
> belongs on this list, is not settled by the ruling and is not
> this seed's to decide. Until it is settled, a conformance
> harness SHOULD test admission-set equality as a separate
> component, on the ground that a test which is redundant costs
> nothing and a test which is missing costs a divergence.]
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

1. **"Refusal class" is not a term this document uses, so this
   seed does not introduce it.** The ruling's enumeration says
   "refusal class where refusal fires". Section 16 says "refusal
   grounds"; section 9 (L1322–1325) names three refusal kinds by
   seal — digest mismatch, coordinate mismatch, clause violation.
   The seed uses **refusal grounds**, the ratified term, on the
   assumption that the ruling was naming the same commitment. If a
   refusal *class* is meant to be a new typed field distinct from
   its grounds, this component is wrong and the candidate needs a
   definition before a harness can test it.

2. **The refusal component is the least grounded part of the
   predicate, and #41 is why.** This clause makes refusal a
   compared component. Sub-question 11a asks what a compound
   result even *is* when one component refuses — refuse the whole
   invocation and discard the computed components, or return a
   product with a refused coordinate, which is an object outside
   what section 7.1 says the evaluator returns. Both readings
   conform today. Until it is ruled, two engines can agree on
   every finding and still differ on the object this predicate
   tells them to compare, which is the same defect this seed
   exists to close, one level up.

   Section 7.5's own words point at the first reading — "the
   evaluator SHALL refuse the invocation" — and under R11's
   ruling that refusals replay as decisions, the first reading is
   the natural companion. It still has to be stated.

3. **The convergence argument depends on R4's ordering wall
   surviving as this seed reads it.** The ruling record annotates
   that wall as retyped by R9, while R9's text retypes a different
   wall. If the ordering wall was retyped in some way that leaves
   an ordering derivable from something other than committed
   bytes, the third leg of the convergence argument weakens and
   this seed's claim that byte-identity follows by construction
   needs re-examining. Raised on the docket; recorded here because
   this is the clause that leans on it.

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
| Executed under | Ruling record 2026-07-30, sha256 `45a6d7208f0faca82946f2bfacb04799994b5cf2c9afdef53f24def9d8cf8552` — R5 |
| Findings discharged | #9 (three predicates, one obligation) |
| Re-ruling | No |
| Depends on | R2, R3, R4 — the convergence argument's three legs |
| Open inside the seed | admission sets (section 16's fourth criterion); refusal component pending #41 |
| Explicitly not settled | the carriage encoding — routed to its own design round, tracked at #57 |
| Unblocks | #11, #14, #15 |
| Status | Unpinned draft; enters the 4.2 candidate by succession |
| Ratified bytes altered | None |
