# Custos 4.2 seed — reinstatement as succession, under a typed
# reversal condition

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges finding #33 only. Executed under ruling R14 of the
> ruling record supplement 2 of 2026-08-01 (sha256 7c5f6491976bd5
> fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670), option C.
> Offered to the drafting authority, which owns the wording.
>
> **This is a re-ruling under `CONTRIBUTING.md` property 2, and
> the touched sentence was itself ruled on eight days earlier.**
> R2's consequence list states that "L1103's monotonicity is true
> as written". R14 re-scopes exactly that sentence. The
> re-scoping is the ruling's own instruction and the collision is
> named here rather than left for a reader to find.

---

## What this seed carries

One destination, one condition on reaching it, and one sentence
re-scoped so that the destination is sayable.

A finding is `defeated(merit, M)`. At the same law head and
position, the bundle grows to include committed evidence that
clause M's own enactment failed cryptographic verification, or
was made by an actor lacking the invoked power. Every destination
the ratified text admits is closed: staying `defeated` cites a
defeat the bundle falsifies, against the Ground Axiom; `affirmed`
and `pending` are forbidden edges from `defeated`;
`self-convicted` requires the *subject's* contradiction, and the
defeater's invalidity is not the subject's; and an act is the
table's own escape hatch, but no act occurred — only evidence
arrived.

R14 rules the destination: an ordinary succession, computed fresh
by full discharge. What makes it more than a restatement of R1 is
the second half — a typed condition that says *when* a succession
may reverse a terminal value, so that the answer does not become
"any later finding may say anything."

## Repair 1 — the destination

**Ratified spans.** Cited, not edited. The forbidden rows that
close the exits (L1072–1075):

> | affirmed | defeated | settled findings do not flip; new
> defeat evidence yields a new finding at a new position |
> | defeated | affirmed | defeat is not un-cited; rehabilitation
> is an act, not a transition |
> | affirmed | pending | evidence does not un-arrive |
> | defeated | pending | evidence does not un-arrive |

And the ex-ante clause that makes the trap constructible
(L1106–1109):

> Defeating evidence is ex-ante enumerable: everything that could
> defeat a question is in that question's committed requirement
> space before appraisal begins, which is what makes defeat a
> citation rather than a surprise.

**The defect.** Two of the four ratified defeater classes are
undercutter-shaped — `crypto` ("a cryptographic verification
failed") and `authority` ("the actor lacked the invoked power"),
at L1129–1132 — and both can apply to the *defeating* clause's
own enactment. So the case is reachable by ordinary means, not
constructed.

R2 forecloses half of it and the half it forecloses is the wrong
half. R2/B rules out the *short-circuit* case, where a `defeated`
is returned while an enumerated check sits unexamined. It says
nothing about the *later-arrival* case, where the defeater's
validity check was examined and passed against the bundle as it
then stood, and the falsifying evidence arrives afterward. There
the trap is still built: R1 makes the growth a new finding rather
than a mutation, and L1103's "refines and never contradicts" at a
fixed law head still closes the `affirmed` exit.

**Replacement — a clause in section 7.3, after the
position-indexing declaration.**

> **Succession under re-discharge.** Where committed evidence
> growth falsifies a ground a prior finding cites, the question
> is appraised afresh at the next position: F(E′, L, p′),
> computed by full discharge of the question's entire committed
> requirement space over the grown bundle. With the defeater's
> enactment falsified, the defeat no longer discharges, and the
> fold returns whatever the requirement space now yields —
> possibly `affirmed`.
>
> The prior `defeated` stands at its coordinate forever.
> Reinstatement is not an edge and adds none: it is a new fact at
> a new coordinate whose bundle contains the undercut.

Nothing here is a transition. Under R1 the transition system
constrains the lawful succession of findings across positions on
one question, never the mutation of a stored value, so the
forbidden `defeated → affirmed` edge is not crossed — it was
never in play, exactly as the revocation case was not in play for
finding #7.

## Repair 2 — the reversal condition, typed

Without a condition, repair 1 says that any later finding may
differ from any earlier one, which empties the forbidden table of
content. The condition is what keeps it full.

> **Reversal condition.** A succession may reverse a terminal
> value only where the evidence growth falsifies a ground the
> prior finding cites — an **undercut**. Added contrary weight —
> a **rebuttal** — never reverses a terminal value, however
> heavy. Whether the growth is an undercut is decided by the
> pertinence half of bearing: the falsified artifact is a member
> of the prior finding's own cited ground.

The condition is computable from the closed triple and needs no
new machinery, because R13 already built the lookup. Pertinence
asks whether a convicted artifact is a member of a finding's
birth-committed enumerations; the reversal condition asks whether
a *falsified* artifact is a member of the same enumerations. One
test, two callers.

The asymmetry between undercut and rebuttal is the whole content
of the rule. A rebuttal argues that the conclusion is wrong; the
finding it attacks is still grounded in what it cited, and
letting it reverse would be exactly the flipping the forbidden
table forbids. An undercut says that what the finding cited does
not stand; the finding is not outweighed but ungrounded, and the
Ground Axiom will not hold an ungrounded finding as a permanent
truth about the record.

## Repair 3 — the monotonicity sentence, re-scoped

**Ratified span (L1101–1106).** Cited, not edited.

> **The evidence ordering.** Findings are ordered by evidence
> growth: where one committed bundle is a subset of another,
> appraisal under the larger bundle refines and never contradicts
> appraisal under the smaller — monotonicity is over the subset
> order on bundles at a fixed law head and position, never over
> wall time.

**The defect.** The sentence claims monotonicity in the *truth*
order for a defeasible system. A defeasible system's whole
subject is verdicts that later evidence can reverse; claiming
they never contradict is claiming the system is not defeasible.
What the four-valued design actually delivers is monotonicity in
the knowledge order: the record only grows, no finding is erased,
no citation un-happens.

**Replacement.**

> Findings are ordered by evidence growth, and the order is over
> knowledge rather than over truth: where one committed bundle is
> a subset of another, appraisal under the larger bundle refines
> the **record** — no finding at a coordinate is erased, no
> citation un-happens, and every earlier finding remains
> recomputable from its own triple. Verdicts across successions
> may reverse, and only under the reversal condition above.
> Monotonicity is over the subset order on bundles, never over
> wall time.

## Ground for the re-scoping, and the collision it carries

The four-valued codomain was chosen because it carries two orders
rather than one — a value's position in the truth order and its
position in the information order are different facts about it,
and a lattice of four is the smallest structure that separates
them. Growth of evidence moves a finding up the information
order, which is what "refines" names correctly. It does not
promise that the truth-order verdict is preserved, and the
ratified sentence read as though it did.

R2's consequence list states that "L1103's monotonicity is true
as written", and under R2's own subject matter it was: with full
discharge binding every terminal value, the short-circuit case
that would have contradicted it cannot arise. The later-arrival
case can, and R2 did not reach it — which the docket's own
correction of 2026-07-31 states. So this is not a contradiction
between two rulings; it is one ruling's scope, made visible by a
case the other did not cover. The seed states it that way because
the ruling trail is part of the record, and because a drafting
pass that quietly reworded the sentence would erase the trail.

## The forbidden table survives, with sharpened reasons

No row is removed. Two reasons change.

> | defeated | affirmed | defeat is not un-cited. A verdict
> reversal is lawful only as succession, and only where committed
> growth falsifies the cited defeat; absent that, rehabilitation
> remains an act, not a transition |

The original reason bundled two phenomena under one clause.
**Taint-cure** — a poisoned voice made clean again — really is an
act and nothing else, because no bytes cure a taint: section
7.2's `unresolved-conflict` species is cured by an owned act of
the party whose conflict it is (L1005–1006), and R6 routes the
taint current there. **Ground-evaporation** — the cited defeat
turning out never to have stood — is not a cure at all; nothing
is rehabilitated, because the ground was never good. The table
now says which is which, and "rehabilitation is an act, not a
transition" remains exactly right for the case it was written
for.

The no-backward-edge wall stands unbreached, for the same reason
repair 1 crosses no edge: a succession is not a transition. That
is the position-indexing declaration doing the work, and this
seed adds nothing to it.

## Undercut named as a category, and the divergence stated

> **Undercut.** An attack on a ground's applicability rather than
> on a conclusion's content. Custos ranks defeat by class and
> resolves competing defeats by the canonical selection rule;
> undercuts of a cited ground do not compete for rank at all,
> and act instead through the reversal condition above.

The literature holds that undercutting attacks succeed
irrespective of priority, while this document adjudicates all
defeat by class rank — which models undercutters as high-ranked
rebuttals. R14 rules that the divergence is stated rather than
hidden, and stating it is cheap: the two ratified undercutter-
shaped classes keep their ranks for the ordinary case, and the
reversal condition is the separate path an undercut of a *cited*
ground takes.

*Marked as prior rather than as cited bytes:* the identification
of this doctrine with ASPIC+, and the claim that the
argumentation literature treats undercut as priority-independent,
is sourced from finding #33's own framing and from training
prior, not re-verified against those sources here. What is
verified against the ratified bytes is that `crypto` and
`authority` are applicability attacks and are ranked (L1129–1132),
and that `self-convicted` is one undercutter promoted to its own
value.

## Why not indefeasibility

Option A — defeat is indefeasible by evidence, reachable only
through an act — is one sentence and is honest about being an
expressiveness limit. R14 rejects it, and the ground is worth
carrying into the candidate: indefeasibility *mandates sustained
false testimony*. A standing finding cites a ground the committed
record proves invalid, consumers must keep acting on it, and no
evidence can dislodge it. A document whose first axiom is that a
finding carries its ground cannot hold that as a permanent state.

## Notes for the drafting authority

Things surfaced in drafting that R14 did not name.

1. **The knowledge order needs a coiner, or it needs to be
   derived in place.** Section 3's third reading rule says terms
   of art from other communities appear with their coiner named
   (L559–562, "This document derives; it does not allude"), and
   the document honors it for Searle and for Hohfeld. "Knowledge
   order" is such a term. Either the drafting pass names its
   source, or it states the two orders from the codomain's own
   four values without borrowing the vocabulary. *Marked:* the
   attribution of the two-order structure to the four-valued
   logic literature is from prior, not from any cited artifact in
   this repository.

2. **The reversal condition inherits R13's residue about
   "question".** It is stated over "the prior finding's own cited
   ground", and knowing which prior finding is the relevant one
   requires knowing when two appraisals share a question — the
   same undefined term the bearing seed flags. The two repairs
   should be read together, and if the drafting pass anchors
   "question" anywhere, both clauses lean on the anchor.

3. **Full discharge over the grown bundle may be expensive, and
   the ruling makes it mandatory.** The destination is computed
   by full discharge of the *entire* requirement space, not by
   re-examining the falsified check alone. That is correct — R2
   binds every terminal value — but it means a single falsifying
   span forces a complete re-appraisal. If the drafting pass
   wants to say that an engine may cache the unaffected checks,
   the place to say it is the engine-interior confession of
   section 15, not here; and if it does not say it, an
   implementer may reasonably wonder. Recorded rather than
   resolved.

4. **The `affirmed → defeated` row is untouched and asymmetric
   under this repair.** Reinstatement of an affirmed finding by
   an undercut of *its* cited ground is the mirror case, and the
   reversal condition as drafted covers it — the clause says
   "reverse a terminal value", not "reverse a defeat". The
   forbidden table's first row keeps its reason, and the mirror
   case is the succession that row's second clause already
   describes ("new defeat evidence yields a new finding at a new
   position"). If the drafting pass intends the condition to be
   symmetric, the first row's reason should be sharpened in the
   same pass; if it intends an asymmetry, it owes the ground.

5. **Station obligations: three vectors, routed to #15.**
   Reinstatement — the falsifier strikes a cited defeater, and
   the succession reverses. Rebuttal-stability — heavy contrary
   evidence arrives and the terminal value does not move. And the
   R13-compound — the falsifier strikes an artifact the prior
   finding did not cite, so pertinence fails and there is no
   reversal. The third is the one that exercises the condition as
   a condition rather than as a permission.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Executed under | Ruling record supplement 2, 2026-08-01, sha256 `7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670` — R14, option C |
| Finding discharged | #33 (evidence falsifying a cited defeat has no lawful destination) |
| Depends on | R1 (succession, not mutation), R2 (full discharge), R13 (pertinence, which computes the reversal condition) |
| Re-ruling | **Yes** — L1103 is re-scoped, and R2's consequence list asserted it true as written; §7.3's transition system is a §15 fixed wall |
| Wall status | No backward edge stands unbreached — a succession is not a transition |
| Station obligations, elsewhere | reinstatement; rebuttal-stability; the R13-compound → #15 |
| Ratified bytes altered | None |
