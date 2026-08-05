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

Ruling R5, as clarified by supplement 1 C-1, settles the conformance
predicate: two folds agree when they agree on the full payload of
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

`decides` names the tracker findings the vector settles, where it
settles one. `status` is `specifiable` or `held`, and a held vector
says what it is held on.

## What the corpus covers

Every station obligation assigned by the ratified edition's section
17 and by the rulings of the record and supplements 2 and 3 carries
at least one vector. The verifier fails the build if a listed
obligation has none, which is the pressure this file exists to
apply: a ruling that assigns a discriminating record and never gets
one is how the 4.1 canonical-selection contradiction survived a full
gauntlet round and the census gate.

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

It is not a claim about the 4.2 candidate. Every vector here is
derived from ratified 4.1 bytes and from rulings, both of which are
in this repository. The candidate is assembled elsewhere, and vectors
that need to cite it will be written when it can be cited.

It does not presume external recognition. A genus reservation enacted
and consumed as committed evidence is testable; recognition by an
external steward is not, and no vector may pretend otherwise.
