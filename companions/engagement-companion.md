# Engagement companion — the substrate's revisions of record

Custos 4.1 §3 says the substrate is cited by name and never
restated, and that "the revision of record for each specification
is pinned in the engagement companion under this document's own
pin discipline". This is that companion.

Informative, like every companion: the ratified edition rules on
any divergence. But this one carries a load the others do not, and
the load is stated plainly below before the table, because a
reader who takes the table for more than it is will be misled.

## What this companion can and cannot do

The ratified edition's fold reaches outside its own bytes in two
places. §7.1 and §7.2 make the substrate's superseding-recovery
calculus the decision procedure for self-conviction and for the
window-open species. §8 and §12.2 make the carriage
specification's threshold-operator semantics decide which slots a
pending requirement set enumerates. Both procedures live in
documents that change.

§7.3 rules that a finding is a function of exactly three inputs
and that two evaluations of the same triple SHALL return
byte-identical findings. That rule is only as good as the pinning
of the two procedures above, and **this companion is not a
pin in the ratified sense**. A pin in that sense is committed: its
digest enters the governance event log by enactment, the way the
edition's own digest did at sn 187. Nothing in a repository file
can do that. Which bytes are law is computed from the GEL, never
read off any mirror — the edition's own rule, applied here.

So this companion is a **record of the engagement surface as
observed at authorship**, offered so the gap is legible and
mechanically checkable, and so a future enactment has something
exact to pin. It is not a reconstruction of what Custos 4.1 was
ratified against.

**It cannot be that reconstruction, and the dates show why.**
Custos 4.1 was ratified 2026-07-23 and effective at sn 188. Three
of the five artifacts below moved after that date. Whatever
revisions the 4.1 ceremony ran against were not recorded at the
time, and cannot now be recovered from this repository. Anyone
needing that answer must ask the maintainers, and should treat a
silence as a silence.

## The revisions of record, as observed 2026-07-30

Specifications are stewarded by the Trust Over IP Foundation's
KERI specification working group. Each is pinned three ways: the
upstream repository, the commit any reader can resolve, and the
SHA-256 of the specification body at that commit under the
edition's own whole-file pin discipline.

| Artifact | Upstream | Commit | Date | Body file | SHA-256 of body |
|---|---|---|---|---|---|
| KERI specification | `trustoverip/kswg-keri-specification` | `71cb54ebb445dd9d8cb33cd29a5f50894fafc569` | 2026-07-28 | `spec/spec-body.md` | `10df5b8ca9395ce8d4270a84fb7338124b0bd8c80dfc27b65601418b3c4533c4` |
| ACDC specification | `trustoverip/kswg-acdc-specification` | `f96ef5430542ed03e6761cdf4e0b3d569812ea90` | 2026-07-27 | `spec/spec-body.md` | `2dd0a1ec3f438ce242342a8443e2f85514bb0cf96e8102ab86b519cbfd9f2654` |
| CESR specification | `trustoverip/kswg-cesr-specification` | `7a6adca678c3669ecde84c352c9bba9c9cfc8203` | 2026-03-17 | `spec/spec-body.md` | `984ce5f08ce6bce81f102143e75389026afe5a425485bf118f0448c3c59a0610` |
| Dossier specification | `trustoverip/kswg-dossier-specification` | `c2d261c1a237a16b3803ae015c3fe800eeaf231b` | 2026-06-30 | `spec/dossier-spec-body.md` | `1090e6f896754ae253982c76221a075b454ff27a880909708070fb419e4a5438` |
| keripy (reference implementation) | `WebOfTrust/keripy` | `8e67f2e6a789c367e7be39fbf376c1f60c6f9692` | 2026-07-29 | — | pinned by commit |

Verify any row without trusting this file:

```
git clone https://github.com/trustoverip/kswg-cesr-specification
git -C kswg-cesr-specification show 7a6adca:spec/spec-body.md | sha256sum
```

## The dossier specification is not in §3's substrate of record

§3 names KERI, ACDC and CESR, with keripy as the reference
implementation. It does not name the dossier specification. Yet
§8 and §12.2 dereference that specification's threshold-operator
semantics to decide requirement-set contents, which §7.3's
byte-identity rule ranges over.

The row is carried above because the dependency is real. Making
it lawful is an edit to the ratified text and therefore a matter
for succession, not for this file. Recorded here so the successor
edition has it.

## A caution about the carriage specification's stability

The dossier specification's threshold operators were rewritten
three times on 2026-06-09: `4dae85a` introduced the `MxN`, `RMxN`,
`MxQ` and `RMxQ` operators; `e99878d` unified the threshold field
as `m`; `ff5b0a4` replaced `m` with weighted-unity thresholds.

That is same-day iteration on then-unreleased text, and it should
not be cited as evidence that any replay has already flipped. It
is offered for the narrower point it does support: the surface
this edition folds under was under active revision weeks before
ratification, and the ratified bytes record no revision at all.

## Status of this companion

Written 2026-07-30, after the 4.1 ratification, to give a named
but absent artifact a body. Two things remain outstanding and
neither is discharged here:

1. **The digest of this file is not pinned by any enactment.**
   Until it is, this is a record and not a commitment.
2. **The notation register of §14 does not exist.** §14 says each
   ratified name "resolves one hop to its minting artifact through
   the notation register — a companion artifact whose digest the
   ratification enactment SHALL pin beside this document's own".
   The sn 187 ratification pinned a succession object, an evidence
   manifest and a lineage record. It did not pin a notation
   register, because there is not one. That is a separate and
   undischarged SHALL, and it is not this companion's to satisfy.

`tools/verify_kernel.py` checks that companions named by role in
the ratified text exist. This file makes the engagement companion
check pass. The notation register is reported as an outstanding
debt rather than a failure, because producing it requires an
enactment and not a repository edit.
