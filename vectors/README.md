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

`ledger.json` is the corpus. `../tools/verify_vectors.py` proves the
ledger's integrity — never an engine's conformance.

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

Two entries are held. The equivalence vector for the two event-form
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
