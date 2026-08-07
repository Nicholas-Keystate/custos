# Custos 4.2 seed — the antinomy circuit

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file. Executed
> under ruling R10 of the ruling record of 2026-07-30 (sha256
> 45a6d7208f0faca82946f2bfacb04799994b5cf2c9afdef53f24def9d8cf855
> 2), completed by ruling R13 of supplement 2 of 2026-08-01
> (sha256 7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb
> 1aea2670).
>
> **The hold is discharged.** This seed was held on finding #32,
> which gated the constructor's admission condition. R13 rules
> that bearing decomposes into conviction and pertinence, both
> decidable from the closed triple. The blank the earlier draft
> carried is now filled from that ruling, and the seed is offered
> for merge. See "How the hold was discharged".

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
>   **Admission.** An antinomy circuit is admitted to this cell
>   when the conviction is grounded and the circuit bears on the
>   question. The conviction is grounded when every clause whose
>   enactment signature the circuit carries is committed in the
>   frame whose law the circuit convicts — section 7.4's
>   law-relative rule supplying the force, the violated predicate
>   being the joint satisfiability of that frame's own committed
>   clauses. The circuit bears on the question when a clause that
>   produced a member of the circuit is named in the finding's
>   discharged requirement space. Membership is flat: that space
>   is a finite enumeration committed at the finding's birth, and
>   no transitive closure is taken over it.
>
>   **Role dispatch.** A conviction that bears dispatches by the
>   convict's role with respect to the question. The two roles are
>   exhaustive over bearing convictions and no third is defined:
>
>   | Role of the convict | Test | Edge fired | Resulting value |
>   |---|---|---|---|
>   | Subject | the conviction strikes the question's own subject — for an antinomy, the frame whose committed clauses the circuit exhibits as jointly unsatisfiable, that frame being the question's law head | `→ self-convicted` | self-convicted, with the proof object and its kind |
>   | Ground | the conviction strikes a party whose artifact the finding cites, the question's own subject untouched | taint succession | pending, species unresolved-conflict |
>
>   A conviction that does not bear is not a conviction for this
>   question: it is ordinary evidence, and the evaluator consumes
>   it. Nothing in this table admits refusal — refusal answers law
>   running out on the question, never on this gate.

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

## How the hold was discharged

Finding #32 was not adjacent to this repair — it was inside it.
"Bearing" gates every edge into `self-convicted` (L1062, L1065,
L1066), gates terminality (L1085), and triggers section 13.1's
recourse (L1824), and the ratified text gives it a decision
procedure at exactly one tier: the key tier, where L957–959 defers
to the substrate's own superseding-recovery rules. An antinomy is
a T3 object by construction, so the earlier draft defined a
constructor for a transition whose admission condition, at the
tier where the constructor lives, was undefined.

R13 rules that bearing is not primitive. It decomposes into two
questions with separate committed homes, and both are decidable
from the closed triple.

**Conviction** — is this pair conviction-grade at all? At the
governance tier the answer was already ratified, in section 7.4's
law-relative rule (L1171–1174):

> Registry-tier and governance-tier duplicity are law-relative —
> they convict only within frames that committed the violated
> predicate, and a frame that never committed the predicate SHALL
> consume them as evidence, never as conviction.

For an antinomy the violated predicate is the joint satisfiability
of the frame's own committed clauses, and the circuit carries the
enactment signature of every clause that produced a member of the
set. So the frame that committed those clauses is exactly the
frame within which the circuit convicts, and no other frame is
asked to treat it as conviction. This is R10's "law-relative and
reflexive" force, arriving from a rule the ratified text already
carries rather than from a new commitment.

**Pertinence** — does the conviction touch *this* finding? R13
answers by flat membership in a finite enumeration committed at
the finding's birth: the evidence bundle's citation enumeration
under R1's closure, or the discharged requirement space under R2's
enumeration. For antinomy specifically the ruling names the
second branch — a producing clause of the circuit is in the
discharged space — and that is the branch the admission clause
above states. No transitivity is taken, because the bundle is
closed by citation and everything the finding leans on is in the
list flatly.

The reflexivity R10 asserted now has a home in R13's role
refinement. R13 fires the edge into `self-convicted` on conviction
together with *subject*-pertinence, and reserves *ground*-
pertinence — a cited third party convicted — for R6's taint
succession. An antinomy convicts the frame whose law the circuit
exhibits as unsatisfiable, and that frame is the question's own
law head, not a third party cited within it. The subject of an
antinomy conviction is therefore the frame itself, which is what
makes the edge the right destination and what makes the force
reflexive: a frame cannot escape a contradiction in its own law by
declining to recognize the conviction.

**The refuse/consume boundary #32 raised is dispositioned, not
deferred.** #32 observed that law being silent on *bearing* (where
axiom 3 says refuse) and law being silent on the *violated
predicate* (where section 7.4 says consume as evidence) are
indistinguishable from inside the fold. R13 rules that these were
one silence with one disposition: no committed predicate means no
conviction, so the pair is ordinary evidence and the evaluator
consumes it. Axiom 3's refusal guards law running out on the
*question*, never on this gate. The two indistinguishable silences
the blind implementation reported are the same silence, and it has
an answer.

What remains true from the earlier draft is the reason the hold
was right: `self-convicted` is terminal and unrehabilitatable, so
two verifiers resolving bearing differently would reach
permanently different terminal states from identical committed
evidence. That is what a ruled, one-sentence definition of bearing
prevents, and it is why R13's definition belongs in ratified 4.2
text rather than in this seed. This seed consumes that definition;
it does not restate it. The definition's own seed is
`spec/custos-4.2-seed-bearing.md`, and the two should be read
together and land together.

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
   never given. #39 has since been ruled (R17, supplement 2), and
   the shape of that ruling is worth borrowing: it split one
   undecidable "verification" into layers by epistemic grade and
   replaced an undecidable admissibility condition with a
   decidable test the section already carried. The same move is
   available here — carriage of the circuit and the presence of
   each derivation's cited spans are checkable by any consumer,
   and joint unsatisfiability is the layer that may honestly be
   left to the consuming frame's judgment.

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
| Completed by | Supplement 2, 2026-08-01, sha256 `7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670` — R13 |
| Finding addressed | #6 (the second trigger's unconstructible payload) |
| **Formerly blocked by** | **#32 — discharged by R13; the admission clause is the pertinence branch's clause-membership case** |
| Admission condition, source | §7.4 L1171–1174 (conviction, already ratified) + R13's discharged-space membership (pertinence) |
| Role dispatch | Carried as a table in the replacement clause — subject-pertinence fires `→ self-convicted`, ground-pertinence fires R6's taint succession |
| Companion seed | `spec/custos-4.2-seed-bearing.md` — R13's definition itself; read and land together |
| Re-ruling | Yes — section 7.3's transition system is a section 15 fixed wall |
| Reachability | Dissolved by R1; no new edge required |
| Station obligation, elsewhere | cardinality-3 antinomy fixture → #15 |
| Status | **Offered for merge.** |
| Ratified bytes altered | None |
