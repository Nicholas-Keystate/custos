# Station record — seed-station round 42-4 (2026-08-06)

**Round directory:** `reviews/rounds/42-4-seed-station-2026-08-06/`.
**Subject:** `weave/42-taxonomy-chapter-v2.md` (sha256
`dfd1ddc1a092225470d2e075c0ad7eec55a4d10e892f38501d763212fcd2bd9a`,
405 lines, verified before reading) → successor
`weave/42-taxonomy-chapter-v3.md`.
**Method:** minimal byte surgery — v3 = v2 bytes + three enumerated
exact-match substitutions, each asserted exactly-once
(`surgery.py`, this directory, replayable). Everything outside the
three sites is byte-identical.
**Authority inputs (digest-verified before reading):**
- Gauntlet report `reviews/rounds/42-3-full-gauntlet-2026-08-05/gauntlet-report.md`
  = `f5220ca6e5868d4dc58f1102af7cb92fce2824bcb81464b89f08bd61aec4e2f1`.
- Supplement 3 `reviews/ruling-record-supplement-3-2026-08-03.md`
  = `79c7d7bd942787c57fc4e177d1fec1424ae6e709d561e81b9ff0d860b48565cc`.

## Successor digest

- `weave/42-taxonomy-chapter-v3.md` sha256
  **`260ed6e7f1d3b00347112a4a1b3224a2df7a9f0be41a9d977997426c5626d98b`**,
  419 lines.
- Diff vs v2: 3 hunks, 9 v2 lines replaced by 23 v3 lines
  (v2 sites 193–195, 363–367, 393). 23 lines touched in v3 —
  under the < 25 target; every other line byte-identical.

## The three repairs (drafting notes with authorities)

### R-1 — issuer non-observation is a surface obligation, not a type property

- **Authority:** GF-1 (BLOCKING) / N2 (was SOL A5) / SF-2, gauntlet
  report lines 63–103 and 644–654, 741–743. The conviction: local
  appraisal prevents a *semantic* phone-home requirement but does
  not structurally prevent issuer observation (registry queries,
  issuer-published endpoint resolution, correlatable acquisition
  identifiers, issuer-observable presentation registries); the bar
  must be tested at the transport and resolution surfaces.
- **Site:** seed §2.7, v2 lines 362–367 ("the bar is discharged by
  type rather than by audit alone … there is nothing to phone home
  about").
- **Repair:** the type argument is retained as exactly what it
  proves — meaning is computed at the consuming frame, so no clause
  of committed law can require issuer contact — and the residue is
  stated as the surface obligation: the bar is discharged only
  where the verification path itself avoids issuer-observable
  surfaces (non-issuer witnesses or caches; no resolution through
  issuer-published endpoints during appraisal; presentation
  registries, where used, holder-controlled), closed by the
  confession-with-force: transport-surface observation is a
  deployment property, testable at the acquisition path; a mandate
  of this class binds the path, not just the semantics.

### R-2 — the §2.4 presentation-form conflation

- **Authority:** SF-1 (gauntlet report lines 732–740) carrying the
  S3-3 seed-side ruling ("the conflation is the defect"): revealing
  a finding proves the finding was computed and committed, not that
  hidden evidence satisfies the clause; the three presentation
  forms must be distinguished.
- **Site:** seed §2.4, v2 lines 193–195 ("A finding is disclosed
  *instead of* its evidence; a no-disclosure mandate is discharged
  by construction rather than by promise").
- **Repair:** the sentence now carries the distinction by lift, not
  legislation — disclosure of a finding in place of its evidence is
  lawful under one of the three presentation forms the objects
  section of this standard types (replayed, warranted, or proven),
  and which form a mandate accepts is the mandate's own committed
  choice. The chapter cites the kernel-side machinery; it does not
  restate it.

### R-3 — the §2.8 confession list completes

- **Authority:** SF-3 (gauntlet report lines 744–746): the §2.8
  confession enumeration was incomplete — it did not confess the
  observation-surface gap (SF-2) and left the presentation-form
  dependency (SF-1) unstated.
- **Site:** seed §2.8, v2 line 393 (the confession list, before
  "The ur-element theorem of …").
- **Repair:** exactly two entries in the list's register: (a) this
  chapter does not claim that type-level locality closes
  transport-level observation; the surface obligation a mandate of
  the §2.0 class carries is stated where §2.7 defines the posture;
  (b) clause-selective consumption depends on the presentation
  machinery the objects section types; the postures of this chapter
  name what is disclosed, never how a disclosure is proven.

## Verification results (all executed, all pass)

- v2 pre-read digest check: match (`dfd1ddc1…`). Authorities'
  digests: match.
- v3 sha256 `260ed6e7f1d3b00347112a4a1b3224a2df7a9f0be41a9d977997426c5626d98b`;
  419 lines; diff stat 3 hunks / 9 deletions / 23 insertions
  (< 25-line target met).
- **Utah exhibit sentence (USER-GATE):** located exactly once in v2
  and v3; byte-compare of the v2 and v3 spans: identical. No repair
  touches it.
- **Deletion test:** with the Utah sentence removed from v3 in
  memory, the mandate-class definition ("A mandate of this class
  specifies … two properties at once") survives, as do all three
  repairs' sentences — no normative claim, including the new §2.7
  surface obligation and §2.8 confessions, loses ground. The
  exhibit carries comprehension only; substitution of any regime of
  the typed class leaves every repaired sentence unaltered (no
  repair names an instance).
- Grep `discharged by type`: 0 occurrences in v3.
- Grep `phone home`: 0 occurrences in v3 (the term does not survive
  in any form).
- Three-presentation distinction present at v3 §2.4 (line 196),
  citing the objects section, not restating it.
- §2.8 confession list grew by exactly two entries; no other §2.8
  byte changed.
- Exactly-once assertions: each of the three substitutions matched
  its v2 site exactly once; the script aborts on any other count.

## Scope statement

Three repairs applied; no others. No kernel-side text touched
(the optional GF-1 kernel-side scoping repair at §7/§15 routes
through the ordinary census, not this station). `staged-repos/custos/`
untouched (read-only).

## Re-graduation gate

This station's output is candidate successor bytes. The
re-graduation gate is the ratifying authority's read pass on
`weave/42-taxonomy-chapter-v3.md` (digest above), recorded by that
authority — not this station's own verification. Until that pass
is recorded, v2 remains the graduated seed of record and v3 is
its proposed successor (chain-not-tree).
