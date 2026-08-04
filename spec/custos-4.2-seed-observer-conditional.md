# Custos 4.2 seed — the convictability claims are
# observer-conditional

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges finding #8 only. Executed under ruling 8a of the
> ruling record supplement 2 of 2026-08-01 (sha256 7c5f6491976bd5
> fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670). Offered to
> the drafting authority, which owns the wording.

---

## What this seed carries

Three cross-references, and no change of substance.

8a asked whether section 12.4's mutual convictability and section
13.2's cross-frame duplicity floor are guaranteed properties or
observer-conditional ones. The ruling confirms observer-
conditional, which is what the bytes already say: the quantifiers
range over verifiers holding the bytes and never promise that set
is non-empty.

Since the escalation resolves to the reading the text already
carries, the repair is the residual the finding named — the
conditionality lives in one paragraph while the claims live in
three others.

## Repair — carry the grade inline

**Ratified spans.** Cited, not edited. The confession, in the
abstract (L38–43):

> That economy is the design's claim, stated at the design's
> grade: its deployment-scale record — an open replaying
> population exercising the credible threat — is a committed,
> unfinished deliverable of this standard's record, and no clause
> below presumes it discharged.

The three sites. Section 5 (L811–814):

> the three things every verifier in every frame computes
> identically from the same committed inputs under the
> substrate's pinned semantics, because their agreement is
> cryptographic rather than negotiated

Section 12.4 (L1730–1741):

> No authority ranks frames. The discipline between them is
> mutual convictability over the shared medium: … A frame that
> speaks with two voices … is convictable by anyone holding both
> logs. … A warrantor whose attested finding diverges from replay
> is convicted on its own signature by any verifier that
> recomputes.

Section 13.2 (L1871–1877):

> - **In the medium** — cross-frame duplicity convicts its author
>   for every verifier holding the pair, under no frame's law …

**The finding, as filed and as it stands.** #8's filed claim was
that the three sites state the property unconditionally. Against
the ratified bytes that is falsified: each site carries its own
quantifier restriction — "every verifier holding the pair", "any
verifier that recomputes", "anyone holding both logs" — so the
conditionality is present at every site. What survives is the
residual the finding also names: a reader arriving at section 5,
12.4 or 13.2 is not carrying L38–43 with them, and a restriction
that says *for whoever re-folds* does not by itself tell the
reader that the set of re-folders may be empty.

**Replacement.** At each of the three sites, one clause naming
the dependency where the claim is made, cross-referencing the
abstract's confession. The shape, offered for the section 12.4
site and matching at the other two:

> The discipline is observer-conditional by construction: each
> conviction above holds for a verifier that holds the bytes and
> recomputes, and this document commits no floor under the
> existence of such a verifier beyond the availability charter's.
> The abstract states the grade.

## Ground

The posture is survivability-correct and should be confirmed
rather than repaired. Watchers make conviction likely; nothing
makes it guaranteed. A standard that promised a non-empty
replaying population would be promising a deployment fact on
behalf of parties it does not control, which is the class of
claim section 14's stated-evidence-scale duty exists to forbid
(L1941–1957).

So the whole content of the repair is that a reader meets the
grade where the claim is made. The abstract's confession then
reads as the general statement of a discipline the body
practises, rather than as a disclaimer the body forgets.

## Notes for the drafting authority

1. **Section 15's observation premise is adjacent and is not the
   same sentence, so the cross-reference target is a choice.**
   L2092–2100 rules that completeness of view is never a
   committed property of any enumerable party and that the total
   view is a join no single party holds. That is about what any
   one observer *sees*; the abstract's confession is about
   whether the replaying population *exists*. Both bear on the
   three sites and neither subsumes the other. The ruling names
   the abstract; a drafting pass may reasonably cite both, and
   should not silently substitute the observation premise for the
   confession, which is the nearer-to-hand and weaker of the two.

2. **Section 5's site differs in kind from the other two, and the
   clause should not be identical.** Sections 12.4 and 13.2 claim
   that a conviction *holds* for whoever re-folds. Section 5
   claims that every verifier *computes identically* — a claim
   about the function, which is true unconditionally, alongside a
   claim about verifiers, which is not. #8's own framing makes
   the distinction: sameness-of-function does not deliver
   sameness-of-observation. The section 5 clause should say that
   the identity is a property of the computation and that the
   observation is not promised.

3. **No station obligation is assigned and none is owed.** The
   sitting lists conformance vectors for six rulings and not for
   8a. A cross-reference discharges no behavior and is not
   testable by a fixture, which is the correct reason for the
   omission.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Executed under | Ruling record supplement 2, 2026-08-01, sha256 `7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670` — sub-question 8a |
| Finding discharged | #8, re-scoped to the cross-reference residual; the escalation is answered by confirmation |
| Sites | §5 (L811–814), §12.4 (L1730–1741), §13.2 (L1871–1877) → the abstract's confession (L38–43) |
| Re-ruling | No |
| Station obligations | None owed |
| Ratified bytes altered | None |
