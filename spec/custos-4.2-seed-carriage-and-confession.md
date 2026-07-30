# Custos 4.2 seed — carriage, confession, and the section 17 gate lists

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges findings #40, #45, #46, #47 and #48 only; every other
> span of the sections it touches stands as ratified. Offered to
> the drafting authority, which owns the wording — a contributor
> supplies the repair shape, and where the shape is a scoping, the
> scope itself, because a boundary named in prose is not yet a
> repair.

---

## What this seed carries

Five repairs across four sections, sharing one defect shape: in
each, the document states as **settled** or as **total** something
its own other sections leave open or partial. None of the five
requires a design choice. Each is discharged by scoping a claim to
what the document already supports elsewhere.

| Finding | Section | The claim that overreaches |
|---|---|---|
| #40 | §6, §14 | the conviction-kind family is total over rejections it does not cover |
| #45 | §17 | a reserved genus may be emitted before it is recognized |
| #46 | §14 | "the encoding layer is closed" in both directions |
| #47 | §17 | the compact-form gate list is complete |
| #48 | §6 | the existing toolchain consumes the edict, full stop |

Three of the five (#46, #47, #48) sit on the wire, and each was
found by re-anchoring the ratified text against the current CESR
specification and the reference implementation rather than against
the document's own account of them. That is the register these
repairs are written in: where the substrate is the authority, the
substrate's own words fix the scope.

None of the five is contested. Where a broader attack on the same
span was raised and refuted in the review that produced these, the
refutation is noted with the repair, so the drafting authority can
see what is *not* being proposed.

---

## Repair 1 — the conviction-kind family, scoped to convictions (#40)

### Ratified spans, cited and not edited

§14 (L1973–1983) requires every conviction to name its kind, from
a family of two, and closes:

> A conviction record from which the kind cannot be read is
> unauditable and therefore not a conviction record.

§6 (L874–876) says:

> completeness is decidable by the replay itself, and a replay
> that reaches for a span the cone lacks convicts the cone as
> short.

### The defect

Two rejections the document itself names fall outside both kinds.
A short cone is well-formed bytes violating no clause — absent
evidence, which the codomain types as a pending finding, not a
conviction. And a refusal of an invocation is not a conviction and
so has no kind to name. §14's own closing sentence then makes the
gap self-executing: a record whose kind cannot be read is "not a
conviction record", which is correct for a refusal and wrong for a
short cone, because §6 has already called the short cone a
conviction.

§9 shows the shape of the fix already in the document's hand
(L1322–1326): "a digest mismatch, a coordinate mismatch, and a
clause violation are three different refusals".

### Replacement, §6 L874–876

> completeness is decidable by the replay itself, and a replay
> that reaches for a span the cone lacks yields a pending finding
> whose typed requirement set names the missing span; the cone is
> short, which is a defect of carriage and not a conviction.

### Replacement, §14 — one sentence appended after L1983

> The family is total over convictions and over nothing else:
> absence of committed evidence discharges as a pending finding,
> and refusal of an invocation is an operational fact under the
> separation rule of section 7.5 — neither is a conviction, and
> neither carries a kind.

### Residual, flagged and deliberately not carried here

The finding's third repair item — annotating each of §17's six
must-reject boundary vectors (L2289–2296) with its expected
codomain value, defeater class and conviction kind — is more than
a sentence, and it is the seam where this meets the conformance
vector work. It should travel with the vectors, not with this
seed. Finding #40 is not fully discharged until it does.

---

## Repair 2 — no emission under an unrecognized genus (#45)

### Ratified span, cited and not edited

§17 (L2262–2272) makes a genus reservation an enactment, with
steward recognition "a distinct, later, bilateral event — a
federation-shaped recognition, not a precondition", and closes by
calling the document's own reservation "enacted, unrecognized, and
honest about the difference".

### The defect

Reservation-by-enactment is sound bookkeeping and is not in
question. Emission is the exposure. CESR states that the protocol
genus and version table is "the only table that all protocols MUST
share (i.e., has identical values)". If two domains lawfully
reserve the same three Base64 characters, or the stewards later
allocate them elsewhere, streams already emitted are archived
forever and mis-frame under a conforming parser — silently,
because CESR is self-framing and framing is a pure function of the
code. Governance streams are precisely the class this document
promises will replay indefinitely.

### What is *not* proposed

A broader attack on this paragraph was raised and **refuted** in
the same review: §17's derive-or-refuse bootstrap, its must-reject
boundary vector for "a grammar migration not admitted under the
grammar previously in force" (L2290–2295), and the reference
implementation's fail-loud rejection of an unallocated genus mean
the design is already fail-closed and enters nothing into the
shared table. The paragraph is the openness clause working as
intended. Only emission is at issue.

### Replacement — appended to the Genus paragraph after L2272

> Until recognition, a domain SHALL NOT emit CESR streams under an
> unrecognized governance genus on any interoperable surface:
> governance events travel in the recognized KERI/ACDC genus, and
> the reservation travels as committed evidence of its own
> enactment, never as a wire claim.

This is consistent with §14's travel posture (L2034–2041), which
already forbids this document travelling as an allocation request.
The clause closes fully, and can simply be struck, on steward
recognition of the reservation.

---

## Repair 3 — the encoding layer is closed in one direction (#46)

### Ratified span, cited and not edited

§14 (L2026–2032):

> is confessed, not cured, by this document: the encoding layer is
> closed (a serialization either parses canonically or fails), but
> semantic latitude above it (threshold derivation defaults,
> receipt-race edges, escrow retention) remains open wherever the
> substrate's own law is silent. A federated GARD SHALL state
> which latitude it has closed by committed profile and which it
> inherits open.

### The defect

The claim holds in the consumer direction and fails in the
producer direction, where CESR grants latitude twice. Serialization
kind is chosen per field map: "Each field map in a Stream MUST use
one of the serialization types from the JSON, CBOR, or MGPK set.
Each field map MAY have a different serialization type." And the
digest algorithm is the producer's: "Each serialization may use a
different cryptographic digest algorithm as indicated by its
derivation code. This provides interoperable future-proofing."

An exhaustive search of CESR for a requirement or prohibition of a
specific serialization kind or digest code, for any message class,
finds none. That latitude is real and it is the producer's.

The consequence is worse than the inaccuracy. Because §14 tells an
implementer the encoding layer needs no profile, a conforming
implementation confesses its threshold defaults and escrow
retention and confesses nothing about the two choices that
actually determine whether two implementations produce the same
bytes. This clause is the mechanism that keeps the other carriage
gaps invisible.

### Replacement — §14 L2026–2032

> is confessed, not cured, by this document: the encoding layer
> admits no interpretive latitude in the consumer direction (a
> serialization either parses canonically or fails), but the
> producer direction is open where the substrate leaves it open —
> serialization kind and digest derivation code are the producer's
> choice — as is semantic latitude above it (threshold derivation
> defaults, receipt-race edges, escrow retention), wherever the
> substrate's own law is silent. A federated GARD SHALL state
> which latitude it has closed by committed profile — including
> its serialization kind and its digest derivation code — and
> which it inherits open.

### A related argument checked and withdrawn

A stronger version of this finding held that CESR-native field
maps carry no serialization-kind indicator at all. That was
checked against the live specification and **withdrawn**: the same
CESR paragraph continues "Instead, the in-memory object
representation of the field map may inject a placeholder version
string, `v` field, whose value is a version string but with the
serialization kind set to `CESR`." The mechanism exists. The
residual — and the reason this repair is offered at all — is that
the placeholder is `may` rather than `MUST`, and lives only in the
in-memory representation, never in the serialization.

---

## Repair 4 — the compact-form gate list (#47)

### Ratified span, cited and not edited

§17 (L2276–2281):

> is a committed deliverable gated, in order, on: the
> bundle-commitment rule (a committed preimage recipe by which one
> digest addresses a receipt together with its attachments; owed
> because the substrate's receipt form does not make its
> identifier field self-addressing), the governed ilk-table seats
> of track two, and conformance vectors exercising both
> presentation orders.

### The defect

The gate's diagnosis is right — the KERI specification confirms a
receipt's `d` addresses "the key event being receipted, not the
receipt message itself", so a bundle-commitment recipe is genuinely
owed. But the recipe as gated is under-determined twice, and an
implementation can stand every listed gate and still compute a
different digest.

**Domain.** Attachments are count-code-framed CESR material, and
the text and binary domains are two lossless encodings with
different bytes. The reference implementation asserts exactly this
relation in its own composability predicate: the same primitive,
two distinct byte strings related by Base64.

**Counter-table version.** Framing is table-dependent, and v1 and
v2 reassign the letter space across every code the compact form
would touch — the same receipt couple is `-C` under one table and
`-M` under the other, with `-A` and `-G` likewise reassigned.

### Replacement — §17 L2276–2281

> is a committed deliverable gated, in order, on: the
> bundle-commitment rule (a committed preimage recipe by which one
> digest addresses a receipt together with its attachments —
> naming the domain, text or binary, over which the preimage is
> taken, and the counter-table genus and version under which its
> framing is read; owed because the substrate's receipt form does
> not make its identifier field self-addressing), the governed
> ilk-table seats of track two, and conformance vectors exercising
> both presentation orders.

Adding to the gate list of an already-undischarged deliverable
commits nothing new. It makes an existing gate satisfiable.

---

## Repair 5 — the edict's carriage claim, scoped to rest (#48)

### Ratified span, cited and not edited

§6 Object typing (L905–908):

> Object forms typed this way are consumable by the substrate's
> existing toolchain; nothing here requires a bespoke parser.

### The defect

The claim is true of the edict at rest and false of the edict in
motion. §6 also mandates that "An edict's content SHALL be a bare
self-addressed data item" — and a `v`-less field map cannot be a
top-level stream element. CESR: "The Version String, `v` field
MUST be the first field in any top-level field map of any
interleaved JSON, CBOR, or MGPK serialization." The reference
implementation refuses the form outright, raising on a missing
version string both when parsing and when constructing.

Meanwhile §15 (L2069–2072) confesses "the carriage encoding of
this document's object classes" is open. So §6 asserts as settled
precisely what §15 confesses as undesigned, and the two cannot
both be right.

### Scope, stated so the repair is not read too widely

This concerns top-level carriage in interleaved JSON, CBOR or
MGPK. Framing a **native** CESR element does not depend on a
version string — the count code carries the framing information
itself. The repair should not be read as "a bare SAD can never
appear in a CESR stream".

### Replacement — §6 L905–908

> Object forms typed this way are consumable by the substrate's
> existing toolchain at rest: computing and verifying the SAID of
> a bare self-addressed data item requires no bespoke parser.
> Their carriage as stream elements is a different question and
> remains an undesigned deliverable under section 15; nothing in
> this paragraph settles whether an edict travels as sealed data
> or inside the substrate's wrapper for non-native serializations.

### Why this and not more

This is the minimal closure. It removes the contradiction with §15
without deciding the carriage, and it preserves the two things the
ratified text gets right: the bare-SAD mandate itself (an issuer
field would smuggle a spine) and the at-rest claim (the substrate
seals bare SADs by digest routinely, and computes and verifies
their SAIDs with no `v` field).

**Deciding the carriage is a separate design act**, not an
editorial one, and this seed does not attempt it. If the drafting
authority prefers to decide it now, finding #48 should be moved to
the ruling docket instead of taking this repair.

---

## What this seed does not touch

The ratified bytes. Every span above is quoted for reference and
remains the law until a successor edition is ratified as an
enactment citing Custos 4.1's digest as predecessor, per §16.
`tools/verify_kernel.py` passes unchanged with this file present,
because this file is not the kernel and claims no pin.
