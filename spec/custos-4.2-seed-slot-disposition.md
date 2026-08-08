# Custos 4.2 seed — the threshold algebra transfers, the slot predicate does not

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges finding #42 only; every other span of section 8
> stands as ratified. Executed under adjudication S3-1 of
> supplement 3 of 2026-08-03 (sha256 79c7d7bd942787c57fc4e177d1fe
> c1424ae6e709d561e81b9ff0d860b48565cc), which rules the same
> sentence at the candidate's own numbering after the integration
> round reached it independently. Read against ruling R20 of
> supplement 2 of 2026-08-01 (sha256 7c5f6491976bd5fb12dcbab4c152
> 0002f9f5a1cdf9bf94dc2f0964bb1aea2670), which already names the
> dossier threshold semantics as a pinned external dependency, and
> against R3, which makes the species of a requirement element
> load-bearing for byte-identity. Offered to the drafting
> authority, which owns the wording.

---

## What this seed carries

One sentence of section 8 is scoped, one clause beneath it is
completed, and a third thing is recorded that finding #42 did not
name and that neither repair closes.

The finding is that section 8 claims a transfer from the key tier
that only half happens. The weighted-threshold *algebra* really is
one algebra at both ends of the system. The predicate that decides
**what enters the sum** is not shared at all: at the key tier it is
"did signature index `i` verify", and at the evidence tier it is a
multi-part cross-log check on an endorsement ACDC. An implementer
who reads the ratified sentence, wires the substrate's threshold
evaluator to an edge group, and concludes the obligation is
discharged has discharged the arithmetic and none of the slot
dispositions.

## Repair 1 — the reuse claim, scoped to the algebra

**Ratified span (4.1 L1256–1262).** Cited, not edited.

> The threshold algebra is one algebra at both ends of the system
> — the same weighted-threshold satisfaction that governs
> key-event signing governs evidence sufficiency — so a verifier
> that can evaluate a rotation can evaluate a quorum of
> endorsements (a derivation from the substrate's design, not new
> law).

**The defect.** The parenthetical is defensible and the sentence
it qualifies is not. Two claims are welded together: that the
threshold algebra is shared, which the dossier specification
states in its own words, and that a verifier able to evaluate one
can evaluate the other, which does not follow and is not true of
any implementation that exists.

The substrate's threshold evaluator takes a list of indices of
verified signatures and returns whether their weights reach unity.
A slot in a dossier edge group is `Endorsed` only when it
references a signed endorsement ACDC carrying disposition
`endorse` and an act appropriate to the operation, issued by the
endorser the slot's referenced ACDC names, anchored in that
endorser's KEL, with a `said` attribute equal to the dossier's
SAID — and, for the qualified operators, a qualification proof
that validates against the schema the operator's `qs` field names.

Reaching that verdict is a cross-log walk. Reaching the key tier's
verdict is an integer offset into a key list. The first is not a
capability the second confers.

**Replacement — 4.1 L1256–1262.**

> Threshold satisfaction here and at the key tier are **analogous
> constructions**: one satisfaction shape — weights over slots,
> summing to unity — over slot judgments of different kinds, and
> this document invents no threshold semantics of its own. The
> *slot judgment* is not shared, and it is this document's own
> fold question rather than the substrate's. At the key tier a
> slot is filled by a verified signature at a key-list offset. At
> the evidence tier a slot is filled by a disposition computed
> over a committed endorsement and its anchoring log — whether the
> cited credential *stands*, which is a question of schema, issuer
> qualification, registry state and disclosure state. A verifier
> that can evaluate a rotation therefore holds the shape and not
> the judgment, and an implementation SHALL NOT treat the
> substrate's threshold evaluator as discharging this section's
> composed-evidence obligation.
>
> Where the shared satisfaction predicate later exists as its own
> committed artifact upstream, both sites SHALL cite it by digest,
> and the analogy becomes a declared shared dependency by ordinary
> migration enactment — the same consume-coarse-now,
> refine-by-enactment discipline the fold-semantics pins carry. No
> re-ruling is owed for that move.

**Ground.** The repair keeps what the sentence was reaching for.
The parenthetical's real content is *we invented no new threshold
semantics*, which is true, sourced, and worth saying — the prior
review asked for exactly this kind of substrate reuse and the
ratified edition adopted the repair verbatim. What the sentence
should not do is convert a shared monoid into a shared verifier.

Section 14 makes this the document's own standard rather than an
outside demand: a claim about evidence scale that is not exercised
is "a defect of this document, reviewable as such." No m-ary or
threshold edge-group operator is implemented in the reference
implementation today, so the transfer claim has never run.

**The word the adjudication chose, and why it is the right one.**
S3-1 scopes the claim to *analogous constructions* rather than
striking it or defending identity, after the integration round's
two legs reached opposite verdicts on this one sentence — the
outside leg ruling it BLOCKING false generality, the same-family
leg citing it as a model. Both readings are correct at different
grains, and "analogous" is the word that carries the grain
distinction: the satisfaction shape coincides, the slot judgments
do not. The seed's earlier phrasing said the algebra transfers
and the predicate does not, which is the same claim in vocabulary
the candidate does not use; the ruling's word is adopted here.

One factual caution for the drafting pass, offered because the
adjudication's parenthetical could be read as settling it. The
observation that the reference implementation evaluates both ends
with one class describes a shape, not an exercised path: as of
`WebOfTrust/keripy` at commit `c63726654`, no m-ary or threshold
edge-group operator exists under `src/keri`, and the only
edge-operator logic is the unary set. The candidate should state
the coincidence of shape without implying that one evaluator has
been run against both kinds of slot, which is the overclaim this
repair exists to remove.

## Repair 2 — the pending discharge names the slot's disposition

**Ratified span (4.1 L1262–1267).** Cited, not edited.

> An unsatisfied operator group is not a defect and not a defeat:
> it discharges as a pending finding whose typed requirement set
> enumerates exactly the unfilled slots — each element naming the
> slot's required schema, its expected issuer, and the citing
> clause — so the cure path for insufficient composed evidence is
> readable off the finding itself.

**The defect.** "Unfilled" is not a disposition the cited grammar
has. The profiled operator conventions put every slot in exactly
one of three states: **Pending**, an anticipated endorsement from
a named candidate that has not arrived; **Endorsed**, an
authenticated act whose weight enters the sum; and **Declined**,
an authenticated refusal by the same candidate, whose weight does
not enter the sum but which records attributable dissent.

"Unfilled" collapses the first and the third. They are not the
same fact and they do not have the same cure. A pending slot is
cured by the candidate acting. A declined slot is never cured by
waiting — the candidate has acted, and the act was a refusal.

**Replacement — 4.1 L1262–1267.**

> An unsatisfied operator group is not a defect and not a defeat:
> it discharges as a pending finding whose typed requirement set
> enumerates exactly the slots whose weight did not enter the sum
> — each element naming the slot's required schema, its expected
> issuer, the citing clause, and **the slot's disposition under
> the profiled operator conventions this section cites** — so the
> cure path for insufficient composed evidence is readable off the
> finding itself. A slot awaiting an act and a slot whose
> candidate has refused are different elements of the requirement
> set, because they have different cure paths and only one of them
> is cured by waiting.

**Ground.** The clause's own promise is that the cure path is
readable off the finding. A requirement element that says
"unfilled" does not carry the cure path; it carries the arithmetic
result. The disposition is what the reader needs, it is already
computed by the evaluation the section requires, and naming it
costs nothing at the wire.

The seed does not restate the disposition vocabulary here, and
should not. R20 already rules that the dossier threshold semantics
are a pinned external dependency where used, so the three
dispositions are law by citation at a committed revision, not by
transcription into this document. Transcribing them would rebuild
at the evidence tier exactly the granularity problem R20 repaired
at the law tier.

## What neither repair closes — the species question

Recorded because it is a byte-identity exposure and it belongs to
whoever drafts the requirement-element repair, not to this seed.

Section 7.2 makes species a mandatory field of every requirement
element. R3 rules that species enters both the deduplication key
and the canonical order, as the fourth and final component. So the
species of a requirement element is load-bearing for the
byte-identity obligation at L1037–1038.

The ratified species enumeration is `absent`, `window-open`,
`unresolved-conflict`, and `expired/abandoned`. Nothing in the
document says which of them a slot's disposition maps to. A
`Pending` slot is plausibly `absent` — no bytes have arrived. A
`Declined` slot is plainly not `absent`, because the bytes did
arrive and are authenticated; it is an owned act by a named party,
which is the shape section 7.2 gives `unresolved-conflict` and its
cure. But the mapping is nowhere stated, and two engines that
choose differently emit requirement sets that differ in a key
component of the canonical order.

That is the divergence class of finding #27, one tier up: the
element carries a field the key must see, and the field's value is
undetermined by the text. #27's own resolution came by ruling, not
by drafting, which is why this seed flags the mapping rather than
choosing it.

## Notes for the drafting authority

1. **The finding asked for a narrowing or a fixture, and both now
   exist.** Its suggested repair was to narrow the sentence, or to
   exercise slot-disposition evaluation in a fixture before
   claiming the reuse. The narrowing is here. The fixture is
   `V-S31-01` of the conformance vector ledger, which S3-1's own
   station obligation assigns: an edge slot fed to a
   signing-threshold evaluator with no standing appraisal, expected
   to diverge from the ruled reading. That vector is what separates
   an engine holding the slot judgment from one holding only the
   satisfaction shape.

2. **The citations in the finding have already drifted, which is
   R20's own argument arriving uninvited.** Finding #42 cited the
   dossier specification by line number on 2026-07-30. Those lines
   have moved since; the claims are all still there, under section
   headings rather than at the cited offsets. Every citation in
   this seed is therefore by section name and quoted phrase. This
   is a small illustration of why R20 pins a revision digest and
   not a document: the semantics did not move, and the coordinates
   did, and only one of those two is something a replay can
   survive.

3. **What was verified, when, and against what.** The dossier
   claims above were re-read on 2026-08-05 against
   `trustoverip/kswg-dossier-specification` at commit `3900e62`,
   and the reference-implementation claims against
   `WebOfTrust/keripy` at commit `c63726654`. Both are *later*
   than the revisions the engagement companion records for the 4.1
   engagement surface (dossier `c2d261c`, keripy `8e67f2e`). The
   substance is unchanged across that interval — the threshold
   sentence, the three dispositions and the absent m-ary operators
   are the same — but this seed is not a claim about the pinned
   revisions, and a drafting pass that needs one should re-read at
   the pin.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Executed under | Supplement 3, 2026-08-03, sha256 `79c7d7bd942787c57fc4e177d1fec1424ae6e709d561e81b9ff0d860b48565cc` — adjudication S3-1 |
| Read against | R20 (dossier threshold semantics as a pinned dependency) and R3 (species in both keys), supplement 2, sha256 `7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670` |
| Finding discharged | #42 — the transfer claim and the unfilled-slot clause beneath it; independently rediscovered by the integration round as its outside leg's A12 |
| Not discharged here | the species mapping for slot dispositions; the translation profile (slot order, issuer qualification, revoked and undisclosed slot behavior), routed by S3-1 to the chartered encoding round, #57 |
| Re-ruling | No — neither span is inside a section 15 wall |
| Status | Unpinned draft; enters the 4.2 candidate by succession |
| Ratified bytes altered | None |
