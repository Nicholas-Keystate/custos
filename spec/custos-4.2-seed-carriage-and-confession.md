# Custos 4.2 seed — carriage, confession, and the section 17 gate lists

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Repairs #46 and part of #40 for the candidate, and removes one
> contradiction on #48 without deciding it; every other span of
> the sections it touches stands as ratified. **None of the three
> findings closes on this seed.** All of #45–#48 are the
> carriage-encoding round's opening docket (charter of
> 2026-08-01, item 5; tracker #57), and the round is where their
> design questions are settled — this file only stops the
> ratified text from asserting what the round has not decided.
> Repairs for #45 and #47 were drafted here and **withdrawn to
> their issues on 2026-07-31**, because ruling R19 — whether §17
> keeps both event-form tracks — may delete the text they amend,
> and R19 is itself blocked on #55. See "What was withdrawn, and
> why". Offered to
> the drafting authority, which owns the wording — a contributor
> supplies the repair shape, and where the shape is a scoping, the
> scope itself, because a boundary named in prose is not yet a
> repair.

---

## What this seed carries

Three repairs across three sections, sharing one defect shape: in
each, the document states as **settled** or as **total** something
its own other sections leave open or partial. None requires a
design choice. Each is discharged by scoping a claim to what the
document already supports elsewhere.

Two further repairs of the same shape were drafted here and have
been withdrawn to their issues; the last section of this file says
why, and the withdrawal is about sequencing rather than about
whether they are right.

| Finding | Section | The claim that overreaches |
|---|---|---|
| #40 | §6, §14 | the conviction-kind family is total over rejections it does not cover |
| #46 | §14 | "the encoding layer is closed" in both directions |
| #48 | §6 | the existing toolchain consumes the edict, full stop |

Two of the three (#46, #48) sit on the wire, and each was
found by re-anchoring the ratified text against the current CESR
specification and the reference implementation rather than against
the document's own account of them. That is the register these
repairs are written in: where the substrate is the authority, the
substrate's own words fix the scope.

None of the three is contested. Where a broader attack on the same
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
> neither carries a kind. A refusal record carries its own
> typing instead: refusal grounds, with the seal kind named per
> section 9's three-kind discipline, and citations to the
> components already computed where the refusal answers about a
> composition seam.

### Residual, flagged and deliberately not carried here

The finding's third repair item — annotating each of §17's six
must-reject boundary vectors (L2289–2296) with its expected
codomain value, defeater class and conviction kind — is more than
a sentence, and it is the seam where this meets the conformance
vector work. It should travel with the vectors, not with this
seed. Finding #40 is not fully discharged until it does, and the
issue stays open on that residual.

The vocabulary the residual note asked for now exists. Supplement
2's 11a rules that refusal propagates the invocation, that the
refusal record cites the components already computed, and that its
grounds are named per §9's three-kind discipline — so the vectors
can state a refusal's expected value in ratified terms rather than
inventing a field to hold it. The appended sentence above uses
that vocabulary, which is why the annotation work can now be
written against something.

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

### The mechanism that closes it — R20's functional-dependency
### declaration

The replacement above names what a GARD must state and leaves the
instrument unnamed, which was a gap while no instrument existed.
R20 supplies one. Supplement 2 rules that the Constitution commits
the revision digests of every external specification whose
semantics its fold consumes, and words the clause as a
**functional-dependency declaration**: it names the predicate set
consumed, and the digest is where those predicates currently live.

Serialization kind and digest derivation code are exactly that
shape one layer down. They are producer choices the substrate
leaves open, and a GARD closing them is declaring which byte
streams depend on which rule sets — the same declaration in the
carriage direction. So the committed profile this repair requires
is not a new device: it is R20's declaration applied where the
bytes are produced rather than where the law is read, and the
encoding round inherits the granularity question under the same
ruling (charter, item 3).

The pairing also fixes the reason this clause is worth repairing
at all. A confession that names threshold defaults and escrow
retention while omitting serialization kind and digest code is a
declaration with the load-bearing dependencies left out.

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
editorial one, and this seed does not attempt it.

**Where the decision now lives.** The seed originally offered to
move #48 to the ruling docket if the drafting authority preferred
to settle it rather than scope it. That option has been taken in a
better form: the charter of 2026-08-01 puts bare-SAD framability
on the carriage-encoding round's opening docket (item 5), together
with #45, #46, #47 and #53. So the repair above and the round are
working on one question at two layers, and the pointer is stated
here so they do not fork — this file removes the contradiction
between §6 and §15, and the round decides what an edict actually
travels as. Finding #48 stays open until it does.

---

## What was withdrawn, and why

Repairs for **#45** (no emission under an unrecognized genus) and
**#47** (the compact-form gate's missing preimage domain and
framing version) were drafted in this file and removed from it on
2026-07-31. Both are back on their issues, and neither is
withdrawn as wrong.

Ruling **R19** asks whether §17 keeps both event-form tracks. Its
recommended outcome collapses to one, which deletes the genus
paragraph #45 amends and removes the second item of the ordered
gate list #47 extends. Under R19's other outcomes both repairs are
correct as drafted. So the exposure is not error; it is a second
pass over the same spans, and #47's own additions would have to be
rewritten into a restated list rather than appended to the
existing one.

The original plan was to rule R19 first. That is no longer
available on any near horizon: **#55** blocks R19 outright, because
the collapse recommendation rests on the substrate not *rejecting*
the `(td, ts)` form, which is a weaker claim than the form carrying
an edict, a warranty, a requirement element or a covenant seal —
and nobody has exhibited a Custos enactment in it. **#56** should
also precede the ruling, since retaining `upd` upstream removes the
collapse option's only substantial cost.

What stays here has no dependence on §17's track structure at all.
#46 in particular is the repair that matters most in this file, for
the reason repair 3 gives.

## What this seed does not touch

The ratified bytes. Every span above is quoted for reference and
remains the law until a successor edition is ratified as an
enactment citing Custos 4.1's digest as predecessor, per §16.
`tools/verify_kernel.py` passes unchanged with this file present,
because this file is not the kernel and claims no pin.
