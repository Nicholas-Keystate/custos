# Custos 4.2 seed — no ambient inputs, in three faces

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file. Executed
> under the framing instruction of ruling record supplement 2 of
> 2026-08-01 (sha256 7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf
> 94dc2f0964bb1aea2670), which rules that R13, R15 and R20 are
> three faces of one commitment and instructs the drafting pass to
> state the generalized form once. Offered to the drafting
> authority, which owns the wording.
>
> This seed carries no repair of its own. It states the frame the
> R15 and R20 seeds instantiate, and it raises one question the
> supplement expressly left to the gauntlet: whether the
> generalized form enters as an axiom or as a corollary.

---

## What this seed carries

One declaration, placed with the fold axioms, and a grade
question the supplement declined to settle by ruling.

The supplement's opening (L13–18):

> One frame for the sitting: three of its rulings turned out to be
> faces of one commitment — no ambient ORDER (axiom 4), no ambient
> MEMBERSHIP (R15), no ambient SEMANTICS (R20). The 4.2 drafting
> pass should state the generalized form once — nothing the fold
> consumes may be underivable from committed bytes — with the
> three faces named and each carrying its discriminating refusal.

The generalization is not a new commitment looking for a home. It
is what two BLOCKING findings, filed independently by two review
rounds against two different sections, turned out to be saying at
once — and the reason neither was caught in drafting is that the
document states one face of the commitment and leaves the reader
to infer the others.

## Repair — the generalized declaration

**Ratified span.** Cited, not edited. Chapter 1's fourth axiom
(L266–270):

> 4. **No ambient order.** Any order the fold consumes — of
>    events, of clauses, of evidence — is derivable from
>    committed bytes, or is proven irrelevant to the result. An
>    uncommitted order that affects a finding is a commitment
>    without ground.

And the refusal axiom the faces route to (L261–264):

> 3. **Refusal.** Where committed law runs out, the fold refuses
>    rather than legislates. The refusal names what is missing.
>    Discretion at evaluation time is exactly what replay
>    eliminates; a fold that interprets has begun to enact.

**The defect.** Axiom 4 quantifies over *order* and stops. The
fold consumes three things it can fail to derive, not one: the
order of what it reads, the membership of what it reads, and the
semantics under which it reads. The document commits the first,
assumes the second, and inherits the third by citation.

Both gaps were found the same way — a blind implementation, or a
review round, reaching for a derivation the bytes do not carry.
Finding #35 states the omission in one line: axiom 4 says no
ambient order, and there is no matching no-ambient-membership.
Finding #43 reaches the same shape from the other side: the
decision procedures the fold executes live outside the closed
triple §7.3 declares, so a semantics revision is a fourth input
to a function ruled to have exactly three.

The consequence in each face is identical and is the one axiom 2
exists to forbid: two verifiers holding byte-identical committed
inputs compute different Constitutions, with nothing in the
record telling either that it diverged.

**Replacement — one declaration in section 1.4, and a scoping of
the fourth axiom to it.**

> **No ambient input.** Nothing a fold consumes may be
> underivable from committed bytes. The commitment has three
> faces, and a fold that cannot discharge any one of them
> refuses under axiom 3 rather than proceeding on an
> uncommitted derivation:
>
> - **Order.** Any order the fold consumes — of events, of
>   clauses, of evidence — is derivable from committed bytes, or
>   is proven irrelevant to the result. *Discriminating
>   refusal:* a stream whose fold order depends on arrival,
>   storage, or any ambient sequence does not conform; section
>   17's order vectors exercise the boundary.
> - **Membership.** Every span the fold consumes as a log of a
>   named kind SHALL be derivable from committed bytes.
>   *Discriminating refusal:* a stream whose governance registry
>   cannot be derived from the applicable founding-law referent
>   fires the bootstrap refusal, which names the underivable
>   commitment.
> - **Semantics.** Every external decision procedure the fold
>   executes SHALL be committed by revision, at the grade of the
>   law that folds under it. *Discriminating refusal:* a fold
>   whose committed semantics pin does not match the revision it
>   holds refuses, and the refusal names the mismatch; it does
>   not silently fold under whichever revision is installed.
>
> An uncommitted order, an underivable membership, or an unpinned
> semantics that affects a finding is a commitment without
> ground.

## Ground for the generalization

Axiom 2 already quantifies the way the generalization does. Its
closed-triple sentence (L245–247) says the inputs are "exactly
three, closed", and its next sentence (L248–250) says the log
spans a fold reads are members of the evidence bundle. Both
sentences are about what the fold may consume, not about order.
The fourth axiom then names one way consumption can go ungrounded
and does not say it is the only way — so a reader who takes the
enumeration as complete has read a closure the text does not
state, which is the same reading error §15's closing sentence
warns about for the six walls.

The three faces are not three restatements. Each fails
differently, which is why each needs its own refusal:

- An ambient **order** yields two Constitutions from one bundle,
  and the divergence is detectable by presenting the same stream
  twice in permuted arrival order. Section 17 already commits
  exactly that vector family (L2207–2211).
- An ambient **membership** yields two Constitutions from one
  stream, and the divergence is *not* detectable by permutation —
  both engines fold their own membership deterministically.
  Finding #35 exhibits three plausible derivations of the GEL
  from identical bytes, each well-formed, with no diagnostic.
- An ambient **semantics** yields two Constitutions from one
  engine at one checkout, separated only by time. Neither
  permutation nor a second implementation surfaces it; the
  divergence is invisible until someone replays an old triple
  against a moved upstream.

Three failure modes, three detection stories, one commitment. A
single declaration that names all three is what makes the third
one findable by a reviewer who has just learned about the first.

## Ground for routing each face to axiom 3

The refusal is what makes each face load-bearing rather than
hortatory. Section 17's bootstrap already exhibits the pattern at
the grammar grain (L2246–2252): where a verifier cannot derive
the initial track placement or ilk table from the applicable
committed founding-law referent, it "refuses the stream — a
missing rule, not missing evidence — and the refusal names the
underivable commitment." That sentence is the model, and both new
faces are drafted to it: the refusal is fired by an underivable
*rule*, names what could not be derived, and is distinguishable
by a consumer from a pending finding about missing *evidence*.

R15's sixth item makes the necessity explicit for the membership
face: any membership rule that can yield a proper subset of the
GEL without a refusal is must-reject. A face without its refusal
is exactly such a rule.

## The grade question, surfaced rather than decided

Supplement 2's R15 item 1 states the membership principle and
adds, in the same breath:

> (Drafting lean: corollary of axiom 4 generalized, not a new
> axiom — the gauntlet adjudicates grade.)

That lean is recorded here and not converted into a decision,
because the deciding principle is already on the record and it
points at the gauntlet. R4 adjudicated R1's position-indexing and
R2's discharge discipline out of the section 15 wall list on the
ground that new walls enter through their own gauntlet and never
as riders on a drift repair, and supplement 1's C-2 states the
test the exception has to pass: the no-fold-tier-selection wall
entered lawfully because it was the *retype* of an existing wall
whose stated obligation was a category error, and "a genuinely
new wall — one carrying a commitment no ratified text yet states
— takes the gauntlet road."

Applied here, the question is factual rather than editorial: does
any ratified text already state the membership and semantics
faces?

- For **membership**, the honest answer is close to yes but not
  yes. Axiom 2 says the spans a fold reads are members of the
  evidence bundle, and section 17's bootstrap requires the
  grammar to be derivable before the first governed event is
  admitted. Neither says which anchored spans are the GEL. The
  commitment is entailed by the axioms and not stated by them,
  which is exactly the position the ruling record's own pattern
  sentence describes — "nearly every blocker resolved to a
  missing commitment made explicit".
- For **semantics**, the answer is no. No ratified span requires
  a domain to commit the revision of an external decision
  procedure. Section 3 promises the pin (L574–576) and the
  promised artifact does not exist, which is a broken promise
  rather than an existing commitment.

So the two faces may not carry the same grade as each other, and
a drafting pass that makes them one axiom by fiat has decided
that question silently. The seed's position: state the
generalization once with all three faces, and let the gauntlet
rule on whether the result is axiom 6, a scoping of axiom 4, or a
derived declaration in section 1.4's closing paragraph. The text
above is drafted so that any of the three placements works
without rewording the faces.

## Notes for the drafting authority

Things surfaced in drafting that the supplement did not name.

1. **The axiom count is load-bearing prose in three places.**
   "Five axioms bind every fold" (L236), "These five axioms are
   the common floor" (L277), and "a fold satisfying the five
   axioms alone is not yet a conforming evaluator" (L288). If the
   generalization lands as a sixth axiom, all three move
   together, and the appendix of record accounts the delta. If it
   lands as a scoping of axiom 4, none of them moves. This is a
   reason to settle the grade before drafting, not after.

2. **The semantics face may be a different genus from the other
   two, and the seed does not hide it.** Order and membership are
   properties of the fold's *inputs* — of the bundle it consumes.
   Semantics is a property of the *procedure* the fold executes
   over that bundle. R20 closes the distance by making
   semantics-version a governed object, so the pin becomes
   committed content and the face becomes an input face again.
   But that closure is R20's ruling doing work, not an identity
   the three faces have on their own, and a drafting pass that
   presents them as obviously one thing overstates the unity the
   supplement claimed. The supplement says three faces of one
   commitment; it does not say three instances of one mechanism.

3. **Wall 6 is a re-ruling touchpoint.** R4 kept the
   canonical-ordering wall "reworded as the ambient-order
   declaration's constitutional hook", and supplement 1's E-1
   confirms R9 left that wall untouched. If axiom 4 is
   generalized, the hook's referent changes, and the section 15
   wall list either follows or is left pointing at a narrower
   declaration than the one that exists. Whichever way the
   drafting pass goes, it touches a section 15 fixed wall and
   returns as a re-ruling under `CONTRIBUTING.md` property 2.

4. **A fourth face is imaginable and is deliberately not
   drafted.** No ambient *identity* — which bytes are the subject
   of the question — is the shape the same argument would take
   one step further out, and section 4's genesis knot is where it
   would live. Nothing in the sitting rules on it, no finding
   exhibits it, and inventing a face to complete a pattern is the
   error this document's own comprehension gate forbids. Recorded
   so that a later reviewer who notices the symmetry finds the
   reasoning rather than filing it.

5. **The seed states no vectors of its own.** Each face's
   discriminating refusal owes a must-reject vector, and those
   vectors are already assigned: the order face's to section 17's
   existing families, the membership face's to R15's three
   vectors, the semantics face's to R20's two. They route to #15
   with their own seeds and are not duplicated here.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Executed under | Ruling record supplement 2, 2026-08-01, sha256 `7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670` — the sitting's framing instruction |
| Related records | Ruling record 2026-07-30 `45a6d720…` (R4's wall principle); supplement 1 `e7ca1111…` (C-2, the gauntlet test) |
| Findings behind the faces | #35 (membership), #43 (semantics); order is ratified as axiom 4 |
| Grade | **Open — axiom, scoping, or derived declaration. The supplement leans corollary and routes grade to the gauntlet.** |
| Re-ruling | Yes, if the drafting pass moves wall 6's referent — section 15 is a fixed wall |
| Instantiated by | `custos-4.2-seed-gel-designation.md` (membership), `custos-4.2-seed-semantics-pinning.md` (semantics) |
| Station obligations | None of its own; the faces carry theirs |
| Ratified bytes altered | None |
