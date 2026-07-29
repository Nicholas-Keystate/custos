# Custos 4.2 seed — canonical order in section 7.3

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges findings #2 and #3 only; every other span of section
> 7.3 stands as ratified. Offered to the drafting authority, which
> owns the wording — a contributor supplies the repair shape and,
> where the shape is a total order, the order itself, because an
> order stated in prose is not yet a repair.

---

## What this seed carries

Two ordering clauses of section 7.3 are replaced. Both are on the
byte-identity path: one governs which defeat a defeated finding
cites, the other governs the serialization of a pending finding's
required payload. Neither is reachable by a fixture written
against a single implementation, which is why both survived the
4.1 gauntlet round and the census gate.

The replacements share one instrument, stated once and applied
twice: a **byte comparison rule** with the direction and the
comparison basis named at every component, and an explicit rule
for absent components and for keys of unequal length.

## The byte comparison rule

Stated here once so the two clauses below derive from it rather
than restate it. This paragraph is drafting scaffolding: the
candidate may inline it at both sites or hoist it, and if the
general ordering declaration of finding #11 is taken up, this rule
is the fragment that declaration subsumes.

> **Byte comparison.** Two committed values compare by the octets
> of their committed encoding, octet by octet from the first,
> ascending. Where neither value distinguishes the other within
> the octets they share, the shorter compares less. Nothing
> uncommitted — arrival order, storage order, local state,
> ambient sequence — enters a comparison at any component.

## Repair 1 — canonical selection

**Ratified span (4.1 L1123–1136).** Cited, not edited; it remains
the law until succession.

> **Canonical selection.** Where multiple defeats are simultaneously
> available for one question, the finding SHALL cite the
> lexicographic minimum of (defeater-class rank, citation
> identifier, subcode). [...] The subcode is the defeat's
> discriminator within its citation, assigned by the cited clause's
> own committed enumeration; where the clause defines none, the
> subcode is empty and orders last.

**The defect.** The paragraph names one selection rule in two
directions. "Lexicographic minimum" selects the empty subcode
first, because the empty string is a prefix of every string;
"orders last" selects it last. The clauses are reconcilable only
under an encoding the text does not pin, and no override
precedence is stated between them.

**Replacement.**

> **Canonical selection.** Where multiple defeats are
> simultaneously available for one question, the finding SHALL
> cite the least defeat under the total order this paragraph
> defines. Two verifiers holding the same bundle SHALL emit the
> same defeated finding down to the byte.
>
> The order is over the triple (defeater-class rank, citation
> identifier, subcode). The components are compared in that
> precedence, ascending at every component, and the first
> component that distinguishes two defeats decides between them.
>
> - **Defeater-class rank** is the defeat's class taken at its
>   position in this enumeration, lowest position first, carried
>   from the predecessor unchanged: **crypto** (a cryptographic
>   verification failed), **authority** (the actor lacked the
>   invoked power), **merit** (the content violates a committed
>   clause), **superseded** (a later lawful act displaced the
>   subject).
> - **Citation identifier** compares under the byte comparison
>   rule.
> - **Subcode** is the defeat's discriminator within its citation,
>   assigned by the cited clause's own committed enumeration. It
>   compares first by presence: a defeat carrying a subcode
>   compares less than a defeat whose cited clause defines no
>   enumeration and whose subcode is therefore empty. The empty
>   subcode is last at its component, never first, and this rule
>   governs the empty case in place of the byte comparison rule's
>   shorter-compares-less clause. Among defeats that carry a
>   subcode, comparison is under the byte comparison rule.
>
> Two defeats agreeing at all three components are one defeat.
> The order is therefore total over the defeats available to a
> question, and "the least" names exactly one.

**Ground.** The direction is now stated once, at the head, and
every component inherits it. Presence is made the primary key of
the subcode component rather than a trailing exception to a rule
stated in the opposite direction — which is what "orders last"
was reaching for and could not express while the head of the
paragraph said "minimum." The empty case is the one place where
byte comparison is displaced, and the displacement is stated
where the reader meets it.

## Repair 2 — the pending finding's required payload

**Ratified span (4.1 L1048–1051).** Cited, not edited.

> - A pending finding SHALL carry its typed requirement set:
>   deduplicated elements, each carrying requirement kind, subject
>   identifier, and the list of citing clauses, in canonical order
>   (subject, then kind, then citing-clause bytes).

**The defect.** The parenthetical names the key precedence and
nothing else. The direction is unstated at every component; the
comparison basis is stated for one component of three; the third
component is a list whose internal order is unstated and whose
comparison as a key is undefined; and "deduplicated" names no
key and no position relative to ordering.

**Replacement.**

> - A pending finding SHALL carry its typed requirement set:
>   deduplicated elements, each carrying requirement kind, subject
>   identifier, and the list of citing clauses, serialized in the
>   canonical order defined here. Two evaluations of the same
>   triple SHALL emit the same requirement set down to the byte.
>
>   Deduplication precedes ordering, and its key is the whole
>   element: two elements agreeing on subject identifier,
>   requirement kind, and citing-clause list are one element.
>
>   Elements are ordered by (subject identifier, requirement kind,
>   citing-clause list), compared in that precedence, ascending at
>   every component, and the first component that distinguishes
>   two elements decides between them. Subject identifier and
>   requirement kind each compare under the byte comparison rule.
>
>   Within an element, the citing-clause list is itself ordered by
>   its members under the byte comparison rule. Two citing-clause
>   lists compare as sequences: member by member from the first,
>   each member pair under the byte comparison rule, and where
>   neither list distinguishes the other within the members they
>   share, the shorter list compares less.

**Ground.** A list cannot serve as a sort key until its own order
is fixed, so the internal order is stated before the list is used
as a component. Deduplication is placed before ordering and given
a key, because a dedup key narrower than the element would let two
evaluators emit sets of different cardinality from one bundle —
a byte divergence upstream of any ordering question.

## Notes for the drafting authority

Three things surfaced in drafting that the findings did not name,
and that a ruling should settle before this seed is declared
final.

1. **The totality claim rests on an assumption about subcode
   assignment.** "Two defeats agreeing at all three components are
   one defeat" is sound where the subcode genuinely discriminates
   within its citation, which is what 4.1 says it does. It is not
   sound if two distinct defeats can share a class and a citation
   whose clause defines no enumeration — both subcodes are then
   empty and nothing separates them. Either that case is
   unreachable by construction, in which case the sentence stands
   and is worth stating as the reason, or it is reachable, in
   which case the order needs a fourth component and this seed is
   incomplete.

2. **"Committed encoding" is well-defined only once the carriage
   encoding is pinned.** The byte comparison rule names committed
   octets; finding #9 records that the carriage encoding of this
   document's object classes is an undesigned section 15
   deliverable. The order is not blocked by that — it needs a
   *deterministic* encoding, not a *particular* one, and it is
   correct under either resolution of #9. But the two are coupled,
   and the candidate should not read as though byte comparison
   silently settles #9.

3. **This seed is the short-term mechanical fix, not the
   commitment.** Finding #11 records the deeper diagnosis: two
   drifting sites are a symptom of a document that never states
   the semantics its own axioms imply. If that declaration is
   taken up, both clauses above should be re-derived from it
   rather than left standing as independent patches — otherwise
   the drift surface is still open and the next ordering clause
   drifts the same way.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Findings discharged | #2 (canonical selection), #3 (required-payload ordering) |
| Findings coupled, not discharged | #9 (conformance predicate), #11 (ordering-semantics declaration) |
| Status | Unpinned draft; enters the 4.2 candidate by succession |
| Ratified bytes altered | None |
