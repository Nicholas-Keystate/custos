# The conformance vector corpus

A vector is an input shape and an expected result, published so that
anyone can run any implementation against it. The corpus is not a
test suite. A test suite belongs to an engine and moves when the
engine moves; a corpus is a committed artifact that both engines are
answerable to, which is the "any stranger" property applied to
conformance itself.

The consequence that matters: **a disagreement about an expected
value here is a finding against the specification, not a bug report
against an engine.** That is the correct direction of travel, and it
is why the corpus is worth publishing before a second implementation
exists.

`ledger.json` is the ledger, and the distinction matters. An entry
records that a vector is owed — which authority assigned it, where the
obligation lives in the ratified edition, what the case must
discriminate. Where a case has been written, the entry carries it. An
entry without a `case` is an obligation on the record and not yet a
vector, and the verifier's closing line reports both counts so the
difference cannot be read past. Today 18 of 69 entries state a case.

`../tools/verify_vectors.py` proves the ledger's integrity — never an
engine's conformance.

## What a case looks like, and why it has no bytes

A test vector is normally concrete data in and concrete data out. Here
there are no bytes to write: the carriage encoding has not ratified, so
no serialization exists to state an input in. That constrains the form
and does not excuse prose. A case is fully concrete at the semantic
layer — fixed symbols, named spans, an expected finding stated field by
field — and an implementer can build and run it against an engine's API
with no wire format at all.

The symbols are the fixture convention, stated once in the ledger's
`fixture_convention` block: `L1` a law head, `p14` a position, `E1` a
bundle given as the spans it closes, `C-merit-01` a committed clause
whose class names the defeater class it produces. They are fixture-local
and fixed, so two implementers building one case build the same case.
They become self-addressing identifiers when the encoding lands, and
nothing else about the case changes.

The shape is `given` and `then`:

```json
"case": {
  "given": {
    "question": "Q1", "law_head": "L1", "position": "p1",
    "bundle": ["gel:A1:0-12"],
    "defeats_available": [
      {"class": "merit", "citation": "C-merit-01", "subcode": ""}
    ]
  },
  "then": {
    "value": "defeated",
    "cites": {"class": "merit", "citation": "C-merit-01", "subcode": ""}
  }
}
```

That is `V-E42-01`, the sole-defeat empty-subcode boundary. An engine
reading "orders last" as a global sort key returns something else here,
which is the whole point of writing it down.

`then` states the expected value to the depth the case discriminates. A
field the case does not name is not constrained by it.

## What grade an expected value carries

Ruling R5, as clarified by supplement 1 C-1 and carried into the
ratified §17, settles the conformance predicate: two folds agree when they agree on the full payload of
every finding they return. Until the carriage encoding ratifies,
that predicate is semantic, so every expected value in this ledger is
stated semantically — over the finding value, the self-convicted kind
where it applies, the grounds in canonical order, the typed
requirement set including each element's species, the refusal grounds
with the seal kind named per section 9's three-kind discipline, the
cited law head, and the corpus identity that carries the admission
set.

A same-engine comparison may still run byte-grade under a pinned
fixture-local serialization. A cross-engine comparison is
semantic-grade. A divergence report states its grade, because a byte
difference under two different serializations is not evidence of
nonconformance.

The verifier enforces this: no entry may claim byte grade while
`grade_discipline.byte_grade_available` is false. When the encoding
round (tracker #57) lands, that flag flips and the expected values
gain a byte form by construction rather than by revision.

## How an entry reads

```json
{
  "id": "V-R10-01",
  "family": "conviction",
  "owed_by": {"source": "record-2026-07-30", "ruling": "R10"},
  "decides": [6],
  "input": "Three grounded derivations that are pairwise consistent and jointly unsatisfiable ...",
  "expect": "Self-convicted, with a circuit payload carrying the whole set ...",
  "grade": "semantic",
  "status": "specifiable"
}
```

`owed_by` is the authority that assigned the vector — a span of the
ratified edition, or a ruling of the record or one of its
supplements. Every source is pinned by SHA-256 in the ledger and
checked against the bytes on disk, so the corpus is bound to the
records it was derived from rather than to their paths.

`ratified_site` says where the obligation lives in `spec/custos-4.2.md`,
and it is the field to read before building a fixture. Where it says
"not carried", the ruling is on the record and the ratified edition
does not yet execute it — those vectors test a successor obligation
rather than the edition of record, and an implementer running the
corpus against 4.2 today should expect them to have nothing to bind
to. Eight entries are in that state, all from supplement 3: the
aggregate-membership pair and presentation forms (S3-3), the unseated
warrantor (S3-4), the charter floor and authentication grade (S3-5),
and the typed observation reports (S3-7).

`predecessor_site` appears on the edition-owed family, which was
assigned by 4.1's §17 and is now carried and extended by 4.2's §18.

`decides` names the tracker findings the vector settles, where it
settles one. `status` is `specifiable` or `held`, and a held vector
says what it is held on.

## What the corpus covers

Every station obligation assigned by the ratified edition and by the
rulings of the record and its four supplements carries at least one
vector. On the edition side that is §18's vectors paragraph — the
equivalence, boundary, refusal-boundary, recognition and order
families, with the boundary family extended under R15 to designation
and membership — and §19's gate three, whose equivalence,
must-reject and vanilla-passthrough families are new in 4.2 and have
no predecessor site. The verifier fails the build if a listed
obligation has none, which is the pressure this file exists to
apply: a ruling that assigns a discriminating record and never gets
one is how the 4.1 canonical-selection contradiction survived a full
gauntlet round and the census gate.

Supplement 4's errata carry three station obligations of their own,
and the corpus had one of them already. `V-R10-01` covers the
cardinality-3 circuit. `V-E41-01` and `V-E41-02` are new, and the
second is the discriminating one: it fails an engine that rejects a
circuit-shaped payload on the strength of the payload bullet's pair
wording. `V-E42-01` is also new, and it is not the vector that was
already here — `V-R03-02` tests two tied defeats where one subcode is
empty, while the erratum's boundary is the *sole* defeat with an
empty subcode, which is where "orders last" and "lexicographic
minimum" actually part company.

**Contributed entries.** Ten of the cases were drafted by the ratifying
authority and integrated on 2026-08-10; they carry a `contributed_by`
field. They discharge the vector debts of supplement 3's eighth and
ninth composition items — conditional seating, the watcher-invocation
law, identifier-as-office, governed vacancy — plus one from the
pre-fix keripy vintage that #1544 repaired. All are successor
obligations, so each carries `ratified_site: not carried`.

Their identifiers carry a sub-series letter (`W` for the watcher law,
`V` for vacancy, `O` for office). The id pattern admits it rather than
renaming ids already cited in review.

**Family, and what it is for.** A family is a filing label, not
provenance — `owed_by` already records which ruling produced an entry.
File by what the case discriminates. That is why the three
office-succession cases sit in three different families: one exercises
a covenant firing where the medium sees nothing, one lawful succession,
one self-conviction.

**The case ratchet.** Vectors owed by supplement 4 and supplement 5
must arrive as cases; the verifier fails the build otherwise. Older
entries carry a case where one has been written and a sketch where one
has not. The ratchet is forward-only on purpose — retrofitting 51
sketches at once would produce 51 guesses, and each one is worth writing
deliberately against the ruling that assigned it.

One entry is held. The equivalence vector for the two event-form
tracks waits on R19, which waits on #55 and #56. The rotation-covenant
families recorded as ripened in S3-9 wait on the recovery-branch
exception grammar, the one ruling that supplement 3 names as owed:
a covenant must not convict the medium's lawful cure, and the
exception must itself be committed law.

## What this corpus is not

It is not the harness. Building an engine-facing runner, and a second
implementation to run differentially against the first, is separate
work — the vectors have standalone value before either exists, and
they can be built by different people in parallel.

It is not a conformance verdict on any engine, and it is not the
ceremony gate. `tools/census-42.py` verifies the succession's own
lineage; this corpus verifies nothing and asserts what an engine
should return.

It does not presume external recognition. A genus reservation enacted
and consumed as committed evidence is testable; recognition by an
external steward is not, and no vector may pretend otherwise.
