# Custos 4.2 seed — the antinomy circuit

> DRAFT, AND HELD — repair seed for the 4.2 candidate, **not ready
> to merge**. Unpinned until declared final. Enters the candidate
> by succession; the ratified Custos 4.1 bytes (sha256 ff8b9e7a6e9
> 5239dcd1111340f4969720e526857f1746f116b42b5b405b72b05) are
> untouched by this file. Executed under ruling R10 of the ruling
> record of 2026-07-30 (sha256 45a6d7208f0faca82946f2bfacb0479999
> 4b5cf2c9afdef53f24def9d8cf8552).
>
> **Held on finding #32, which is BLOCKING and unruled.** The
> repair below states a payload for an edge whose admission
> condition — "bearing" — has a decision procedure at exactly one
> tier, and this constructor lives at another. The blank is marked
> in the replacement text and is the reason this seed is not
> offered for merge. See "Why this is held".

---

## What this seed carries

Section 7.3's `self-convicted` required payload is replaced. It
names one payload — the canonical proof package for a
contradictory pair — while the `pending → self-convicted` edge
admits two triggers, and the second cannot construct that payload.

The second trigger is antinomy: a contradiction sited in the
committed law rather than in the subject's bytes. R10 rules that
its constructor is a **circuit**, not a pair.

This is a re-ruling under `CONTRIBUTING.md` property 2.

## Repair — the self-convicted payload

**Ratified spans.** Cited, not edited. The payload (L1052–1053):

> - A self-convicted finding SHALL carry the identifier of the
>   canonical proof package for the contradictory pair.

And the edge that reaches it (L1058–1064):

> | pending | self-convicted | a bearing contradictory pair, **or
> new governed-status evidence** (committed evidence newly bearing
> on the subject's status under the governance tier's committed
> predicates), enters the bundle |

**The defect.** The `or` is a genuinely distinct trigger, not a
restatement — the `affirmed → self-convicted` and
`defeated → self-convicted` rows carry no such second disjunct, so
the asymmetry is deliberate. But a finding reaching the cell by the
second disjunct has no contradictory pair, and therefore nothing
from which to construct the payload its own `SHALL` requires.

One blind implementation recorded the consequence as an
unconstructible-proof error at the constructor boundary, having
made the Ground Axiom a typing rule so that a finding cannot be
built without its ground. That is a stronger statement than "two
engines may differ": under a faithful typing, the second trigger is
not merely under-specified but unrepresentable.

**Replacement.**

> - A self-convicted finding SHALL carry the identifier of the
>   canonical proof object for its conviction, and the object's
>   kind. Two kinds are defined and no others:
>
>   **Duplicity.** The proof object is the canonical proof package
>   for the contradictory pair, as elsewhere in this section. The
>   convicted party is the subject whose committed bytes carry the
>   pair.
>
>   **Antinomy.** The proof object is a **circuit**: a set of
>   grounded derivations that cannot jointly stand, together with
>   the exhibit of their joint unsatisfiability, together with the
>   enactment signatures of every clause that produced a member of
>   the set. Each derivation SHALL cite the evidence spans and the
>   clause SAIDs that carry it to its conclusion. The set SHOULD
>   be irredundant — no proper subset jointly unsatisfiable — and
>   an irredundant circuit is not required for conviction.
>
>   The convicted party of an antinomy is the GARD's
>   administrators, not the subject. Its force is law-relative and
>   reflexive: the conviction binds maximally in the very frame
>   whose law it convicts, and travels to other frames as evidence
>   about that GARD rather than as conviction of it.
>
>   [BLANK — see #32. The `pending → self-convicted` edge is gated
>   on the pair or the evidence *bearing*, and "bearing" has a
>   committed decision procedure only at the key tier (section 7.1,
>   L957–959). An antinomy is sited in committed law at the
>   governance tier, where nothing states how a verifier decides
>   bearing. This clause cannot state the admission condition for
>   the constructor it defines until #32 is ruled.]

**Ground for the circuit.** A pair cannot express the decisive
case. Three grounded derivations may be pairwise consistent and
jointly unsatisfiable — no two of them contradict, and all three
together cannot hold. A pair-shaped payload cannot represent that
at all, so an engine built to the ratified clause would either
fail to convict a real antinomy or would convict on an arbitrary
two of the three and misstate the ground.

Irredundancy is `SHOULD` rather than `MUST` because an honest
non-minimal circuit still convicts, and extracting a minimal core
can be expensive. A producer that cannot afford the extraction
should still be able to make the record.

**Ground for the bearer.** Every other path into this cell
convicts the subject. An antinomy convicts the party that enacted
the contradictory law, and that party is the GARD's
administrators — their enactment signatures are the leaf
signatures of the proof object, which is why the object carries
them. The force is reflexive because a frame cannot escape a
contradiction in its own law by declining to recognize the
conviction: the clauses that produced the derivations are the
frame's own committed clauses.

**Reachability.** Dissolved by R1, and nothing is owed here. An
antinomy discovered after a question was affirmed produces a new
terminal finding at a new position; no new edge is needed and the
forbidden table is not opened. That was the sub-question the
docket said mattered most, and position-indexing answers it
without touching a wall.

## Why this is held

Finding #32 is BLOCKING and unruled, and it is not adjacent to
this repair — it is inside it.

"Bearing" gates every edge into `self-convicted` (L1062, L1065,
L1066), gates terminality (L1085), and triggers section 13.1's
recourse (L1824). It is given a decision procedure at exactly one
tier: the key tier, where section 7.1 defers to the substrate's
superseding-recovery rules. The four-valued scheme is instantiated
at all three tiers, and nothing says how a verifier decides bearing
at T2 or T3 — including for the Gever, the evaluator this standard
exists to specify.

An antinomy is a T3 object by construction. So this seed defines a
constructor for a transition whose admission condition, at the tier
where the constructor lives, is undefined. Writing the clause with
that blank filled in by a drafter would be legislating the exact
question the docket asked be ruled alongside R10.

The docket asked for R10 and R13 to be ruled together, "because
rulings that disagree would be worse than either alone". R10
landed alone. This seed is the shape of the consequence: the
payload is stateable and the gate is not.

Two smaller couplings run the same way. R10's "law-relative and
reflexive" force is a commitment in the same territory as #32's
refuse/consume boundary — the distinction between law being silent
on *bearing* (axiom 3 says refuse) and law being silent on the
*violated predicate* (section 7.4 says consume as evidence, do not
refuse), which from inside the fold are indistinguishable. And
`self-convicted` is terminal and unrehabilitatable, so two
verifiers resolving bearing differently reach permanently
different terminal states from identical committed evidence.

**This seed should be reviewed now and merged after #32.** The
circuit is ruled and its shape does not depend on the ruling; the
clause around it does.

## Notes for the drafting authority

Some things surfaced in drafting that finding #6 and R10 did not
name.

1. **The payload clause now carries a kind, which is a small new
   commitment.** The ratified sentence names one payload and no
   kind. The replacement names two kinds and requires the finding
   to say which. That is forced — a consumer cannot verify a proof
   object without knowing what shape to verify — but it is
   additive rather than clarifying, and section 14's
   conviction-family rule should be checked for whether it already
   provides the typing this duplicates.

2. **"Cannot jointly stand" needs a decision procedure or an
   explicit deferral.** The circuit carries an exhibit of joint
   unsatisfiability, and the clause does not say what makes an
   exhibit valid. For a set of grounded derivations over committed
   clauses this is a real proof obligation, and the honest options
   are to name a checkable form or to say that the exhibit's
   sufficiency is the consuming frame's judgment. Leaving it
   unstated repeats the pattern finding #39 identifies for the
   covenant seal, where a verification procedure was named and
   never given.

3. **The conformance fixture is a station obligation, not part of
   this seed.** R10 requires a cardinality-3 antinomy fixture —
   pairwise consistent, jointly unsatisfiable — to enter the
   conformance corpus as the record separating circuit-payload
   engines from pair-payload engines. It belongs in #15 with R3's
   regression vector, and this seed does not carry it.

4. **The GARD's administrators are not a defined term.** The
   bearer clause names them and section 4 does not define them.
   Either that is an existing gap this seed surfaces, or
   "administrators" should be replaced by whatever committed role
   the founding law names, so a consumer can determine who was
   convicted from committed bytes rather than from context.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Executed under | Ruling record 2026-07-30, sha256 `45a6d7208f0faca82946f2bfacb04799994b5cf2c9afdef53f24def9d8cf8552` — R10 |
| Finding addressed | #6 (the second trigger's unconstructible payload) |
| **Blocked by** | **#32 (bearing at the registry and governance tiers) — BLOCKING, unruled** |
| Re-ruling | Yes — section 7.3's transition system is a section 15 fixed wall |
| Reachability | Dissolved by R1; no new edge required |
| Station obligation, elsewhere | cardinality-3 antinomy fixture → #15 |
| Status | **Held. Not offered for merge until #32 is ruled.** |
| Ratified bytes altered | None |
