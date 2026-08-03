# Charter — the carriage-encoding design round (issued 2026-08-01)

**Issued by:** the ratifying authority, per ruling R5
(`reviews/ruling-record-2026-07-30.md` @ `45a6d720…`, as
clarified by supplement 1 @ `e7ca1111…` and extended by
supplement 2 @ `7c5f6491…`). Tracker: issue #57.

## Purpose

Design the carriage encoding of this standard's object classes —
finding, warranty, requirement element, refusal record, bundle
preimage, covenant-seal data — as a group act, entering per §15's
own route: review by others, findings never edits. The round's
output, once ratified through the ordinary gauntlet, discharges
R5's forward commitment: byte-identity as the conformance
predicate, by construction rather than by hope.

## Why a round, and not a pin (the R5 grounds, standing)

The "one decision" is several, and each has live alternatives:
serialization kind; field schemas (now stable through the second
sitting's rulings, but R19's track question remains open); SAID
coverage (what a finding's SAID commits, hence what a warranty
citing it stakes); versioning and succession of the encoding
itself; genus composition. Two live implementations exist whose
authors' input is worth more before ratification than after; an
encoding pinned by fiat would have made both retroactively
nonconformant.

## Participants

- **Daniel Hardman** (dhh1128) — invited; two blind
  implementations, both adversarial review rounds, and the
  carriage findings (#45–#48) are his.
- **Samuel Smith** — invited. Stated plainly for the record: Sam
  has not reviewed any Custos artifact to date; his practice
  enters this corpus only as cited readings of his published
  specifications (ACDC's disclosure discipline, the CESR genus
  tables, the typed-seal grammar). This charter is the designed
  on-ramp for his actual eyes, and the round should be prepared
  for his findings to be foundational rather than marginal.
- **Reviewers with KERI-systems design depth** — open seat;
  entry per the repo's covenant (findings, not edits).
- **The ratifying authority** — convenes, rules on the round's
  docket, never pre-empts.

## The decision surface (inputs pinned)

1. **R5's six decisions** (record + supplement 1): serialization
   kind; field schema per object class; SAID coverage; encoding
   versioning; genus composition; the predicate vocabulary
   (settled by supplement 1 C-1: refusal grounds with §9's
   three-kind seal discipline; admission sets subsumed through
   corpus identity and named explicitly in §16's repair).
2. **The R19 contingency** (#36, held on #55/#56): whether
   Custos enactments collapse to the (td, ts) registry form or
   retain distinct ilks. Under R19/A the gate-2 ilk seats do not
   exist; the round SHALL NOT design against seats until #55
   reports. #56 (ask upstream to retain `upd`) precedes.
3. **Pin granularity** (R20): the encoding SHALL be designed
   against declared functional dependencies — which byte streams
   depend on which rule sets — so the granularity mismatch R20
   repaired at the law layer is not rebuilt at the wire layer.
   CESR table composition with declared dependencies is the
   candidate shape; the round adjudicates it.
4. **Portable clause language** (R17): whether a covenant seal
   may seal against another domain's law requires a clause
   citation form that travels; in-domain sealing needs only
   GEL-SAIDs. Scope decision belongs to the round.
5. **The carriage findings already filed:** #45 (genus
   stewardship), #46 (producer choices exempted from "the
   encoding layer is closed"), #47 (bundle preimage domain +
   counter-table version), #48 (bare-SAD framability), #53
   (BBAB bearing on SAID coverage), and the gate-1 bundle
   preimage decomposition (issue #1). These are the round's
   opening docket, not afterthoughts.

## Constraints the round inherits (not open for redesign)

- The three-voice doctrine: KEL anchors always; heavyweight
  envelope vanilla-processable; compact form committed-endpoint
  routes only. The compact form changes cost, never meaning —
  and never audience.
- The one-way-coverage law: identity covers interior bytes;
  endorsement stands outside; commitments compose outward.
  Bundle identity is computed over the assembly from outside
  (gate-1's ground).
- The two-layer liability split: carriage commitment and
  judgment commitment are distinct signatures over distinct
  preimages (never-blur, by construction).
- R18's conditional blinding mandate; R20's semantics pinning;
  the designation chain of R15 (whatever the wire form, the
  law-head derivation SHALL remain computable from it).
- Interim discipline until the round lands (enforced by the
  harness): same-engine byte-grade under pinned fixture-local
  serialization; cross-engine semantic-grade (full payload); a
  divergence report states its grade.

## Sequencing

1. #56 asked upstream; #55 feasibility reported.
2. R19 ruled (its own sitting; A+D composition of R15 heard
   there if the (td, ts) track lands).
3. Round convenes on the decision surface above.
4. Output enters as findings; the ratifying authority dockets
   and rules; ratification through the ordinary gauntlet.

## Non-gating

The round does not gate the 4.2 candidate (R5, standing). 4.2
carries the semantic predicate and the byte-identity forward
commitment; the round's output lands in the first edition after
its ratification.
