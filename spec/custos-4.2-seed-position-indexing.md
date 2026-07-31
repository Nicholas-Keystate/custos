# Custos 4.2 seed — position-indexed findings, and what contested standing returns

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges findings #7 and #24 only; every other span of
> sections 7.3 and 7.4 stands as ratified. Executed under rulings
> R1 and R6 of the ruling record of 2026-07-30 (sha256 45a6d7208f
> 0faca82946f2bfacb04799994b5cf2c9afdef53f24def9d8cf8552).
> Offered to the drafting authority, which owns the wording.

---

## What this seed carries

One declaration and one rewording, and they are the same repair
seen from two sides.

The declaration says what a finding **is**: an immutable fact of a
closed triple, not a value that moves through a state machine.
Section 7.3's transition system then constrains the lawful
succession of findings across positions on one question, and never
the mutation of a stored value.

The rewording follows from it. Section 7.4 says a lower-tier
self-conviction "converts" what was affirmed above to contested
standing — a verb that presumes the mutation the declaration
denies, and a noun that is not in the codomain.

Both are re-rulings under `CONTRIBUTING.md` property 2: they touch
wording inside section 15's fixed walls, and they return through
the front door with their findings as evidence.

## Repair 1 — the closed triple

**Ratified spans.** Cited, not edited. Section 7.3's Inputs clause
(L1033–1038):

> **Inputs.** A finding is a function of exactly three inputs: the
> committed evidence bundle, the committed law head under which it
> is appraised, and the appraisal position. No other input — wall
> clocks, local state, operator discretion, ambient configuration
> — may influence a finding. Two evaluations of the same triple
> SHALL return byte-identical findings.

And the forbidden edge the finding is built on (L1072):

> | affirmed | defeated | settled findings do not flip; new defeat
> evidence yields a new finding at a new position |

**The defect.** The document forbids `affirmed → defeated`
absolutely and provides no motion for the prospective termination
of a grounding credential's lifecycle. Section 1.1's own worked
example — may the holder of credential X act in role Y? — sits on
that gap. X's TEL emits `rev`, which is evidence growth at a fixed
law head, and the table has no answer. Three conforming readings
survive and they are neither equal nor nested: the finding stays
`affirmed` and carries force on a revoked ground; it moves to
`defeated` and violates the wall; or every revocable-grounded
standing is perpetually `pending`, which guts `affirmed`.

The Inputs clause names the three inputs and stops. It does not
say whether a finding **is** that function's value at a coordinate
or a variable the function updates — and the whole question turns
on which.

**Replacement — a declaration added to section 7.3, before the
transition tables.**

> **Findings are position-indexed.** A finding is an immutable
> fact of a closed triple, never a mutating value:
>
> ```
> finding = F(E, L, p)
> ```
>
> - **E, the committed evidence bundle**, is a set of committed
>   log spans closed by citation. Each span is a triple of log
>   identifier, coordinate range, and digest: the GEL span, every
>   cited key-event span, every cited registry span. Registry
>   state is a member of E, not an ambient condition E is read
>   against — axiom 2 already says so, and this clause states the
>   consequence rather than the fact.
> - **L, the committed law head**, is the SAID of the Constitution
>   state the question is appraised under. E is typed by L: the
>   law head commits the question's requirement space ex-ante, and
>   the bundle inhabits the evidence-type that law declares.
> - **p, the appraisal position**, is a log coordinate — an
>   identifier and a sequence number in committed order. It is
>   never wall-clock.
>
> The transition system of this section constrains the lawful
> succession of findings across positions on one question. It does
> not describe the mutation of a stored value, and no clause of
> this document licenses reading it that way. "Settled findings do
> not flip" therefore means that no coordinate's fact is ever
> rewritten: `affirmed@p` and `defeated@p′` are two independent
> lawful findings about one question, and neither displaces the
> other.
>
> The engine profile is not a member of the triple. It is the
> lens-side citation whose inertness conformance tests, under the
> reversal condition.

**Ground.** The revocation case dissolves without opening a wall.
A `rev` event is a new span, therefore a new E, therefore a new
finding at a new position. No edge is crossed because no edge was
ever in play — the succession of findings across positions is not
what the transition table governs.

The load-bearing sentence is axiom 2's, at L248–250, and it is
already ratified:

> The log spans a fold reads — the GEL span, every cited key-event
> and registry span — are members of the evidence bundle, never a
> substitute for its completeness.

So the repair here is not a new commitment. It is a commitment the
axioms already forced and the text had not yet said. The finding's
own second clause at L1072 was pointing at it: "new defeat
evidence yields a new finding at a new position."

## Repair 2 — what contested standing returns

**Ratified span (4.1 L1157–1161).** Cited, not edited.

> - **Duplicity taints upward.** A self-conviction at a lower tier
>   does not un-happen the history above it: committed history is
>   monotonic, first-seen survives, and what was affirmed above
>   converts to contested standing rather than to nothing.

**The defect.** "Contested standing" appears exactly once in 2471
lines, is defined nowhere, and is not a member of the four-valued
codomain that section 15 fixes as the evaluator's return type "and
nothing else". Section 7.4 imports the taint current as a binding
wall, so the wall returns something no verifier can consume.

Two implementations written blind against the ratified bytes both
had to leave the codomain to express this clause, and both
independently named the escape `ContestedStanding`. The defect is
demonstrated by their agreement, not inferred from disagreement: a
codomain declared total cannot express the output of a clause the
document imports as binding.

**Replacement.**

> - **Duplicity taints upward.** A self-conviction at a lower tier
>   does not un-happen the history above it: committed history is
>   monotonic, and what was affirmed above stands at its
>   coordinate. The self-conviction enters the record as new
>   committed spans, and at the next appraisal position the fold
>   returns `pending`, carrying the taint as a typed requirement
>   element of species **unresolved-conflict**.
>
>   Contested standing is not a finding value and not a fifth
>   member of the codomain. It is an evidence event with a typed
>   consequence, and the consequence is the pending finding above.
>   No missing bytes cure a taint and no log growth cures it; only
>   a committed act by a named actor does, which is what section
>   7.2 already says of that species — rehabilitation is an act,
>   not a transition.

**Ground.** Under repair 1 this crosses no forbidden edge, because
nothing mutates. The `affirmed` at its coordinate stands forever;
the `pending` is a different finding about the same question at a
later position, and the succession `affirmed@p` then `pending@p′`
is not the forbidden `affirmed → pending` edge — that edge
prohibits un-arriving evidence within one appraisal, which is not
what happened here.

The species is not invented. Section 7.2's ratified amendment
block enumerates the four species, and L1005–1006 already assigns
this one its cure:

> **unresolved-conflict** is cured by an owned act of the party
> whose conflict it is

So the taint's cure path was already written, waiting for a clause
to route to it. The codomain's totality wall stands unbreached and
needs no fifth value.

**On the verb.** "Converts" is replaced rather than defined. A
finding that cannot change cannot convert into anything, and the
word is what made two careful implementers reach for a standing
value — they read a transformation and built one. Succession
vocabulary says what actually happens: the earlier finding stands,
a later finding differs, and the difference is evidence growth.

## Notes for the drafting authority

Some things surfaced in drafting that the findings did not name.

1. **The declaration names a member the document cannot yet
   derive.** E's first named member is "the GEL span". Finding
   #35 — BLOCKING, unruled — is precisely the claim that which
   anchored spans constitute the GEL is underivable under track
   one: three plausible derivations were exhibited from identical
   committed bytes, each yielding a different Constitution, with
   no diagnostic. Axiom 2 has the same exposure and this seed
   inherits it, because the seed follows axiom 2's own sentence.

   This does not block the repair. The declaration is correct
   whichever way #35 is ruled, and stating the triple's members is
   what makes the gap legible rather than latent. But the seed
   should not be read as having closed it, and a candidate that
   lands this without ruling #35 has a foundation with one member
   whose extent is not derivable from committed bytes.

2. **The forbidden table's rows now need re-reading, and the
   candidate should say so once.** Every row is stated in
   transition vocabulary — "does not flip", "does not un-arrive",
   "does not reopen". Under repair 1 these are constraints on
   lawful succession, not on mutation, and a reader who takes them
   as mutation constraints will draw the wrong conclusion in
   exactly the case finding #7 found. Rather than reword seven
   rows, one sentence above the table would carry it: the rows
   name successions that no evidence growth licenses.

3. **Repair 2's succession is not listed as a permitted edge, and
   should not be.** The permitted-transition table has no
   `affirmed → pending` row, and adding one would break the
   forbidden table. What repair 2 describes is not an edge at all;
   it is two findings at two positions. If the candidate wants the
   reader to find that quickly, the place to say it is the
   terminality paragraph, which currently reads as though
   `affirmed` were final in a stronger sense than position-
   indexing supports.

4. **Reachability for antinomy follows from repair 1 and is
   drafted elsewhere.** R10 rules that an antinomy discovered
   after affirmation is a new terminal finding at a new position,
   needing no new edge. That is this seed's declaration doing the
   work, but the antinomy constructor itself is held pending #32
   (bearing at the registry and governance tiers) and is not in
   this file.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Executed under | Ruling record 2026-07-30, sha256 `45a6d7208f0faca82946f2bfacb04799994b5cf2c9afdef53f24def9d8cf8552` — R1, R6 |
| Findings discharged | #7 (prospective revocation of a grounding credential), #24 (contested standing's return value) |
| Re-ruling | Yes, both — section 7.3's transition system and section 7.4's upward currents are section 15 fixed walls |
| Exposure inherited, not created | #35 (GEL span membership) — E's first member |
| Related, not in this seed | #6 / R10 (antinomy constructor), held pending #32 |
| Status | Unpinned draft; enters the 4.2 candidate by succession |
| Ratified bytes altered | None |
