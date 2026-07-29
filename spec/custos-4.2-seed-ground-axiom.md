# Custos 4.2 seed — keyword force for the Ground Axiom

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges finding #29 only; every other span of sections 1.4,
> 7.1 and 7.3 stands as ratified. Offered to the drafting
> authority, which owns the wording — a contributor supplies the
> repair shape and, where a sentence must acquire normative force,
> a candidate sentence, because "add a keyword" is not yet a
> repair until someone says which sentence and which keyword.

---

## What this seed carries

Section 3's first reading rule makes normativity a property of
individual sentences: "The set of ruled spans is the document's
normative content; prose between them motivates and derives but
binds nothing on its own" (4.1:538–540). Applied to section 7.1,
that rule disqualifies the sentence the same paragraph calls "the
load-bearing decision of this document" (4.1:935–936), because it
carries no BCP 14 keyword. Axiom 1 (4.1:240–242) carries none
either.

For three of the four codomain values the obligation survives
elsewhere: section 7.3's required-payload bullets rule `defeated`,
`pending` and `self-convicted` with a SHALL apiece (4.1:1042–1053).
There is no bullet for `affirmed`. So no ruled span of the
ratified edition requires an `affirmed` finding to carry any
ground, and an evaluator emitting bare affirmations violates no
normative commitment while contradicting the axiom the document
builds its replay argument on.

Two repairs follow, and they are not alternatives — the first
without the second still leaves `affirmed` without a ruled
payload, and the second without the first still leaves the typing
rule unruled.

Neither repair is reachable by a fixture. Both implementations
that surfaced this pinned the axiom as binding and enforced it at
construction, which is the right engineering and almost certainly
the drafter's intent; the defect is visible only to a reader who
applies section 3 to section 7.1 rather than reading section 7.1
as obviously binding.

## Repair 1 — the Ground Axiom as a ruled span

The typing rule must bind, and it must bind as a *typing* rule:
the claim is not that a well-behaved evaluator attaches grounds,
but that a groundless value is not a member of the type at all.

Two sites are available and the drafting authority may take
either or both. Section 7.1 is the site where the axiom is applied
as a typing rule; section 1.4 is the site where it is stated as an
axiom and imported as a floor.

**At section 7.1**, replacing the unkeyworded typing sentence
(4.1:933–934, "A value that does not carry its ground is not a
member of this type, whatever else it may be"):

> A finding SHALL carry its ground — the citation, requirement, or
> proof that justifies it. A value that does not carry its ground
> is not a member of this type, whatever else it may be, and an
> evaluator SHALL NOT return one.

**At section 1.4, axiom 1** (4.1:240–242):

> 1. **Ground.** A finding SHALL carry its ground — citation,
>    requirement, or proof — or it is not a finding. The codomain
>    admits no bare verdicts.

The second is the smaller edit and keeps the axiom's voice. It
carries one consequence worth naming: the other four axioms are
stated in the same unkeyworded voice, so keywording axiom 1 alone
invites the reading that axioms 2–5 deliberately do not bind. See
the note below.

## Repair 2 — the `affirmed` required payload

Section 7.3's "Required payloads" (4.1:1040–1053) enumerates three
of the four constructors. The fourth needs a bullet in the same
voice, naming the ground section 7.1 already describes for it
("the evidence bundle and the clause set under which it was
appraised", 4.1:944–946):

> - An affirmed finding SHALL carry the identity of the committed
>   evidence bundle over which it was appraised and the clause set
>   under which it was appraised. Neither is reconstructible from a
>   bare verdict; both MUST be explicit or uniquely re-derivable
>   from a committed referent.

The closing sentence deliberately mirrors the `defeated` bullet's
(4.1:1045–1047), because the same reason applies: a consumer that
cannot re-derive what an affirmation rested on cannot replay it,
and an affirmation that cannot be replayed is the judge testifying
where the record should — the failure section 1.4 axiom 2 names.

This repair also closes the narrower observation that section
7.3's payload enumeration presents itself as complete while
omitting one of the four values.

## Notes for the drafting authority

**The general question is larger than this finding.** Reading rule
1 makes normativity sentence-local, but several of this document's
most consequential commitments are stated as *definitions*,
*axioms*, and *typing rules* rather than as keyworded obligations.
Section 15's "What is fixed" enumeration is unkeyworded prose
asserting six binding walls; section 1.4's five axioms are
unkeyworded; the codomain's closure at four values is unkeyworded.
Patching them one at a time will not converge.

Two coherent resolutions exist, and this seed does not choose
between them:

- **Keyword the load-bearing sentences**, accepting that the
  document acquires many more SHALLs and that the axioms' voice
  changes.
- **Amend reading rule 1** to admit a second class of normative
  content — definitions, axioms, and typing rules — stated once,
  with a rule for how a reader recognizes one. This is the smaller
  textual change and the larger doctrinal one.

The second is probably closer to what the document already means:
an axiom that must be keyworded to bind is not functioning as an
axiom. But it needs the recognition rule stated, or "which
sentences bind" becomes a judgment call, which is the condition
reading rule 1 exists to eliminate.

**Coupling.** If reading rule 1 is amended rather than the
sentences keyworded, repair 1 becomes unnecessary and repair 2
remains necessary — the `affirmed` bullet is a gap in an
enumeration, not a keyword problem. Findings #20 and #21 bear on
the same soft spot from the wall-enumeration side.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Findings discharged | #29 (Ground Axiom unruled; `affirmed` without a ruled payload) |
| Findings coupled, not discharged | #20, #21 (the wall enumerations are unkeyworded prose raising the same question at section 15) |
| Alternative resolution offered, not chosen | amend reading rule 1 to admit axioms and typing rules as a second class of normative content |
| Status | Unpinned draft; enters the 4.2 candidate by succession |
| Ratified bytes altered | None |
