# Custos 4.2 seed — the semantics a fold consumes are committed

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges the **domain layer** of finding #43 only. Executed
> under ruling R20 of the ruling record supplement 2 of 2026-08-01
> (sha256 7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb
> 1aea2670). Offered to the drafting authority, which owns the
> wording.
>
> **R20's edition layer is not in this file and must not be
> drafted here.** Writing the engagement companion, pinning it by
> the ratification enactment, and admitting the dossier
> specification to section 3's substrate of record are PR #50's
> subject, which the ruling names as the vehicle. This seed
> assumes that work lands and depends on none of its wording.

---

## What this seed carries

One commitment, at the grade of the law that folds under it.

Section 7.3 makes a finding a function of exactly three inputs
and forbids any other input from influencing it. Two decision
procedures the fold executes are defined outside those inputs:
the substrate's superseding-recovery calculus, which decides
`self-convicted` at the key tier and the `window-open` cure
species; and the dossier specification's threshold-operator
semantics, which decide which slots a pending requirement set
enumerates. Neither is pinned by anything the fold reads.

R1 sharpens this rather than softening it. With a finding ruled
an immutable function of a closed triple, a decision procedure
that can change under the engine's feet is a fourth input to a
function just declared closed.

## Repair — the semantics declaration

**Ratified spans.** Cited, not edited. The closed inputs
(L1033–1038):

> **Inputs.** A finding is a function of exactly three inputs:
> the committed evidence bundle, the committed law head under
> which it is appraised, and the appraisal position. No other
> input — wall clocks, local state, operator discretion, ambient
> configuration — may influence a finding. Two evaluations of the
> same triple SHALL return byte-identical findings.

The first external procedure, at the key tier (L957–959) and in
the cure species (L998–1005):

> **window-open** is cured when the substrate's superseding rules
> no longer admit a superseding event at the position … for a
> delegated log the window closes only when no lawful superseding
> rotation remains admissible under the substrate's
> delegated-recovery rules, which stay open longer (the
> substrate's own recovery calculus is the decision procedure …)

The second, in composed evidence (L1243–1257) and in the
transformation's resolve step (L1642–1649), where the dossier
specification's threshold operators decide which slots an
unsatisfied group enumerates.

And the promise that was to have covered both (L574–576):

> The revision of record for each specification is pinned in the
> engagement companion under this document's own pin discipline;
> within this document the substrate is cited by name and never
> restated.

**The defect.** This is not the cross-implementation debt section
2 and section 14 confess; neither confession reaches it. It is
intra-implementation drift over time: one conforming engine, one
pinned checkout, replaying the same committed triple later
against a changed substrate revision, and returning a different
cure species or a different unfilled-slot enumeration — in
violation of a ruled SHALL.

The drift is not hypothetical at the level that matters. Finding
#43 verified the superseding-recovery rules at KERI specification
revision `71cb54e` on 2026-07-30. A local checkout at `78946e4`,
read 2026-08-04, carries the same rules at the same coordinates.
Two different revisions, the same content, and **nothing in the
ratified bytes records which of them this edition folds under**.
That the content happened to hold is the point: an engine cannot
know that it held without a pin, and next time it may not.

**Replacement — a clause in the Constitution's committed content,
stated in section 3 and required of founding law.**

> **Committed semantics.** A GARD's founding law SHALL commit,
> for every external specification whose semantics its fold
> consumes, the predicate set consumed and the revision in which
> that predicate set is committed, by digest. A fold executing a
> consumed procedure under a revision other than the committed
> one refuses, and the refusal names the mismatched
> specification and revision; it does not fold under whichever
> revision is installed.
>
> Semantics-version is thereby a governed object under section
> 11's own criterion, and a substrate upgrade is a **migration
> enactment** at a committed coordinate: replay before the
> coordinate is deterministic under the old revision, replay
> after it is deterministic under the new, and the move itself is
> a replayable act rather than an operational fact.

## The enumeration is a functional-dependency declaration

The clause names what the fold *depends on*, and pins where those
dependencies currently live. It does not pin a file because the
file is interesting.

> **Consumed predicates.** The declaration enumerates the
> predicates the fold executes and identifies the artifact and
> revision that carries them. The whole-file digest is the
> address at which those predicates currently live, not the
> extent of the dependency: a revision that changes bytes outside
> the enumerated predicates changes the digest and not the
> semantics, and the declaration says so.

Two things follow, and both matter more than the wording.

First, an implementer can read the dependency without reading the
upstream diff. A pin that says only "revision X" tells a
verifier that something moved and nothing about whether it
mattered. A pin that says "these predicates, at revision X" makes
the question decidable.

Second, the enumeration is auditable in the direction that
catches drafting error. R20's second station obligation is
exactly this vector: a pinned rule the prose never mentioned
governs anyway. If the fold executes a predicate the declaration
does not enumerate, the declaration is short, and the vector is
what shows it.

## The superseding-recovery calculus, enumerated

The first consumed procedure is the substrate's superseding rules
for recovery at a location. The declaration enumerates them, and
the ruling requires no silence at the edges.

*Verified against a local checkout of the KERI specification at
`78946e4` on 2026-08-04, `spec/spec-body.md` §"Superseding Rules
for Recovery at a given location, SN": A0–A2 at :1806–:1810,
B1–B3 at :1815–:1819 under the B stem at :1813, C at :1821, C1 at
:1823, the latest-seen constraint at :1825. Finding #43 verified the same coordinates at `71cb54e`.*

- **A0–A2** — a rotation may supersede an interaction at the same
  sequence number where that interaction is not before another
  rotation; a non-delegated rotation may not supersede another
  rotation; an interaction may not supersede any event.
- **B1–B3** — the three conditions under which a delegated
  rotation may supersede the latest-seen delegated rotation at
  the same sequence number.
- **C and C1** — the recursive application to delegating events,
  and the discard when the root KEL is reached without
  satisfaction.
- **The latest-seen constraint** — earlier delegated rotations
  cannot be superseded at all.

**Why the last two cannot be left silent.** Section 7.2 rules
that `window-open` is cured when no lawful superseding rotation
remains admissible. Under the latest-seen constraint, no
superseding rotation is admissible against a delegated rotation
that is not the latest-seen — so the window over such a rotation
is *already closed*, and the cure has already happened. An engine
that consumes A and B but not the constraint holds that window
open indefinitely. Same triple, same law head, same position, two
different cure species, neither engine in error.

That is the whole finding, exhibited on one clause: a decision
procedure the ratified text gestures at and does not enumerate
changes a finding's payload. Consuming C1 and the latest-seen
constraint, or expressly excluding them with a stated ground, is
what closes it. Silence is what does not.

## The substrate upgrade as a migration enactment

Making the pin governance-grade is what buys the replay property,
and it is worth saying why the cheaper option does not.

A pin at document grade — the edition names a revision — is
correct for exactly one edition and gives a domain folding under
a later revision no lawful way to say so. The domain's choices
are then to be silently nonconformant or to wait for the next
edition of the standard. Neither is a governance act.

A pin at law grade makes the move an enactment: judged under the
law in force before it, committed at a coordinate, anchored, and
replayable. A stranger holding the logs computes which semantics
governed each position, and the migration is as auditable as any
other amendment. Section 11's criterion admits it without
strain — the consumed specification has a lifecycle, its
revisions are addressable, and law committed before a position
judges that position.

The confession the ruling attaches belongs in the text: pinning
does not pretend upstream stasis. It makes **when we move** a
committed, visible act.

## The forward-compatibility clause

> Where a consumed rule set exists as its own SAID-addressed
> artifact, re-pinning from a coarse dependency to a fine one is
> an ordinary migration enactment and requires no succession of
> this document.

The clause exists so that the granularity debt below is
confessed rather than structural. Today the superseding rules
live inside a whole specification file, so the coarse pin is
what is available. If the substrate later addresses that rule
set on its own, a domain moves its pin by enactment and no
re-ruling is needed. The mechanism does not change; only the
granularity does.

## The granularity debt, confessed

> The whole-file pin is confessed as granularity debt, not as
> design. A file digest over-approximates the dependency: it
> changes when anything in the file changes, so a domain whose
> fold is unaffected by an upstream edit must still enact a
> migration to say so.

The cost is real and is the honest price of the property. An
over-approximating pin produces migration enactments that carry
no semantic content, and a domain that finds itself enacting them
often has learned something about its dependency that the
declaration should record. That is the pressure the
forward-compatibility clause is designed to relieve, and pin
granularity is already an input to the encoding round's charter
(#57), where the wire-layer half of the same question is
adjudicated.

## What this seed does not carry

R20's edition layer, in full, and by ruling:

- the engagement companion is **written** and pinned by the
  ratification enactment, repairing L575, which currently cites a
  nonexistent artifact;
- the dossier specification is **admitted to section 3's
  substrate of record**, since it is currently unreachable by any
  pin at all.

PR #50 is the vehicle the ruling names, and it should absorb the
ruling's shape: the companion revs on its own clock; the ratified
spec never chases upstream. This seed is drafted so that it
composes with whatever wording lands there — it requires the
companion to exist, and requires nothing of its contents.

## Notes for the drafting authority

Things surfaced in drafting that R20 did not name.

1. **The enumeration the ruling gives is one rule short.** R20
   enumerates "A0–A2, B1–B3; C1 and the latest-seen constraint
   consumed or expressly excluded". The substrate's own
   enumeration carries **C** as a rule in its own right — the
   recursive application of A and B to delegating events — with
   C1 as its terminal case. A declaration that pins C1 without C
   pins a base case with no recursion. This is a transcription
   gap rather than a ruling defect, and the drafting pass should
   enumerate C alongside C1.

2. **The dossier half is enumerated nowhere yet.** The clause
   above is stated generally and exhibited on the substrate's
   recovery calculus. The threshold-operator semantics need the
   same treatment — which operators, which schema, which proof
   edge — and finding #43 names the coordinates it verified.
   Doing that enumeration properly requires the dossier
   specification to be in section 3's substrate of record, which
   is the edition layer's work. So the domain layer's clause can
   land now, and its second enumeration cannot be completed until
   PR #50 does. Recorded as a sequencing dependency, not as a
   blocker: the clause is correct with one enumeration and
   incomplete until it has two.

3. **A pin at law grade puts governance weight on an artifact
   nobody in the domain controls.** That is the cost R20's option
   A always carried and it does not disappear by being ruled. A
   domain whose upstream makes a security-critical fix must enact
   a migration to consume it, and until it does, its fold is
   deterministic *and wrong*. The honest framing is that the
   standard prefers a visible, replayable delay to an invisible,
   unreplayable update — but the text should say that plainly,
   because an implementer will meet the case.

4. **The refusal on mismatch is new machinery at a familiar
   grain, and its class needs naming.** Section 9's three refusal
   kinds are seal-shaped (digest mismatch, coordinate mismatch,
   clause violation) and supplement 1's C-1 rules that refusal
   grounds are named per that discipline. A semantics-pin
   mismatch is none of the three. Either the discipline grows a
   kind, or the mismatch is stated as an instance of an existing
   one, and a drafting pass should not leave the class to be
   inferred — the conviction-kinds duty of section 14
   (L1973–1983) is explicit that a record from which the kind
   cannot be read is not a conviction record.

5. **Station obligations: two vectors, routed to #15.** The
   semantics-pin mismatch, expected to refuse fail-loud. And
   enumeration completeness — a pinned rule the prose never
   mentioned governs anyway, which is the vector that catches a
   short declaration. The latest-seen exhibit above is the
   natural fixture for the second.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Executed under | Ruling record supplement 2, 2026-08-01, sha256 `7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670` — R20, domain layer |
| Finding addressed | #43 (external decision procedures unpinned), domain layer only |
| Not in this seed | R20's edition layer — the engagement companion and the dossier specification's admission to §3 — carried by **PR #50** |
| Frame | `custos-4.2-seed-no-ambient-inputs.md` — the semantics face |
| External verification | KERI specification `spec/spec-body.md` at local checkout `78946e4`, read 2026-08-04; #43's coordinates at `71cb54e` agree |
| Charter input | pin granularity and table composition with declared functional dependencies → #57 |
| Re-ruling | No |
| Station obligations, elsewhere | semantics-pin mismatch (refuse fail-loud); enumeration completeness → #15 |
| Ratified bytes altered | None |
