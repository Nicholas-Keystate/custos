# 4.2 targeted re-gauntlet report (2026-08-06)

Round: `reviews/rounds/42-5-targeted-regauntlet-2026-08-06/`.
Subject: `weave/custos-4.2-candidate-v4.md`, 3,928 lines.
Subject digest verified before reading: sha256
`a9ac1ed5adf0d0ce85c993b7ecb6d459e4192c0d60efc09a93dccb8f91439c89`
(matches the brief's pin; no mismatch).

Reviewer: fresh-context targeted re-gauntlet leg. This is NOT a
full gauntlet: the full round (42-3) ran against candidate v2 and
this leg verifies only that the three repair acts discharge its
findings — six checks plus the young-prose battery. Findings never
edits; seed-body content findings are flagged for the seed's own
station (SF-n continuation), never proposed as in-place edits.

Inputs consumed, digests verified before reading:
- `reviews/rounds/42-3-full-gauntlet-2026-08-05/gauntlet-report.md`
  sha256 `f5220ca6e5868d4dc58f1102af7cb92fce2824bcb81464b89f08bd61aec4e2f1`
  (matches the 42-4 station record's own pin of it).
- `reviews/rounds/42-4-seed-station-2026-08-06/station-record.md`.
- `weave/42-taxonomy-chapter-v3.md` sha256
  `870a4d7cb998bb890241c80297a4991d57da71afe8ab9f7e852eab69b692f406`
  (matches the brief and the v4 seed-succession census).
- Chain predecessors hashed for the census check:
  v2 `a11f2902c6e18404ba22c9468681e8a92b57af01fe1de53b08dbabb2d5c786f0`,
  v3 `cd16f4ba46c861713a2bfc201ae2424f54809de4f8c0173a37410a95ca04a705`,
  seed v2 `dfd1ddc1a092225470d2e075c0ad7eec55a4d10e892f38501d763212fcd2bd9a`
  — each matching the pins the censuses and records cite.

Report written incrementally, check by check (provider-infra law).
New findings carry this round's namespace `RG-n` (42-5/RG-n
qualified outside this round); the notation.md row for RG-n is an
obligation of the session that ratifies this report, recorded here.

---

## Part I — the six checks

### Check 1 — N2/GF-1 replay (SOL A5 against the repaired §2.7) — REPAIRED

Original attack (42-3 report lines 63–103, BLOCKING): local
appraisal prevents a semantic phone-home requirement but does not
structurally prevent issuer observation — TEL queries, OOBI
resolution, correlatable identifiers, issuer-observable
presentation registries; the bar must be tested at the transport
and resolution surfaces.

The repaired site, v4 lines 807–818 (seed §2.7, entered via the
42-4 station's R-1 and the v4 splice):

> "the type argument proves exactly what it proves: under
> regime-side color meaning is computed at the consuming frame, so
> no clause of committed law can require issuer contact. The bar
> on observation is discharged only where the verification path
> itself avoids issuer-observable surfaces — evidence acquired
> from non-issuer witnesses or caches, no resolution through
> issuer-published endpoints during appraisal, presentation
> registries, where used, holder-controlled. Transport-surface
> observation is a deployment property, testable at the
> acquisition path; a mandate of this class binds the path, not
> just the semantics."

Replaying the A5 attack surface by surface:

- **TEL queries.** The convicted "by type" discharge is dead
  (grep `discharged by type`: 0 occurrences in v4; grep
  `phone home`: 0). The type argument is now scoped to exactly
  what it proves — no clause of committed law can *require*
  issuer contact — and the discharge condition is a surface
  predicate: "evidence acquired from non-issuer witnesses or
  caches." A TEL query to an issuer-operated witness fails the
  "only where" condition; the bar is then not discharged. The
  attack no longer has a type-level claim to attack.
- **OOBI resolution.** Named directly: "no resolution through
  issuer-published endpoints during appraisal." The resolution
  surface is inside the obligation.
- **Issuer-observable presentation registries.** Named directly:
  "presentation registries, where used, holder-controlled."
- **Correlatable identifiers.** Not named as a fourth list item.
  The general predicate ("the verification path itself avoids
  issuer-observable surfaces") quantifies over the class, and the
  42-4 station record's R-1 drafting note names "correlatable
  acquisition identifiers" as part of the conviction it repairs —
  but the candidate text itself carries only the three-surface
  enumeration plus the general predicate. Because the discharge
  condition is written as a necessary condition ("discharged
  ONLY where ... avoids issuer-observable surfaces"), a
  correlatable acquisition identifier that makes a surface
  issuer-observable falls under the predicate; the residue is an
  enumeration-completeness nit, not an escape. Recorded as RG-5
  (NOTE), for the fixture round's vector work.
- **Tested at the transport/resolution surfaces.** The
  confession-with-force lands the testability claim:
  "Transport-surface observation is a deployment property,
  testable at the acquisition path; a mandate of this class binds
  the path, not just the semantics." The obligation is now a
  path-binding, deployment-testable claim, exactly the grade the
  attack demanded.
- **Confession completeness (the 42-3 lawful-openness failure).**
  Seed §2.8 now carries the entry (v4 lines 844–847): "This
  chapter does not claim that type-level locality closes
  transport-level observation; the surface obligation a mandate
  of the §2.0 class carries is stated where §2.7 defines the
  posture." The confession that 42-3 found incomplete (SF-3) is
  complete with respect to this gap.

Score: **REPAIRED** (with RG-5 NOTE residue). The surface
obligation answers all four A5 observation channels; the by-type
overclaim does not survive anywhere in v4.

### Check 2 — GF-2 (walls count and census totality) — REPAIRED

Original (MAJOR): v2 line 2927 "six walls" against this edition's
seven-wall enumeration; and the collision-by-addition census's
totality claim "Zero carried spans retained defective; zero
collisions unexamined" falsified by that span.

- The site (now v4 line 2945, §16 The openness clause): "A reader
  who infers a completed construction from the seven walls has
  inferred more than this document states" — the one-word repair
  landed (V3-5).
- Independent walls sweep over the whole file: every count-bearing
  wall mention reads seven (304 "seven fixed walls"; 2886 "Seven
  commitments"; 2924 "These seven are walls"; 2945; delta-census
  3636; structure-census 3707). Grep "six walls": 0 occurrences.
- The census-totality rescope (V3-6), v4 lines 3778–3782: "Zero
  collisions unexamined at assembly. One carried span was found
  stale by the 42-3 gauntlet after this census closed (the walls
  count of section 17, repaired in the v3 pass under its census
  below) - the totality claim is scoped to the assembly pass, and
  later rounds convict later." The falsified absolute claim is
  withdrawn, the convicting round is cited, the repairing census
  is pointed to, and the surviving claim ("zero collisions
  unexamined AT ASSEMBLY") is scoped to what the assembly pass
  could actually attest. Honest in substance.
- Rescope accuracy nit: the parenthesis says "the walls count of
  section 17"; the repaired span sits in §16 (The openness
  clause) — heading at v4 line 2879, the span at 2945; §17 is
  Succession and ratification. Same mispin appears in the v3
  micro-pass census row V3-5 ("s17 walls count") and V3-3
  ("s8.4 force distinction" for a span at line 1679, inside §8.3).
  Recorded as RG-2 (MINOR, census meta-text accounting).
- Register-honesty note: the rescope EDITS the collision census's
  closing lines in place rather than appending a correction block
  (42-3's disposition suggested "an appended collision-census
  correction"), and the repair census's header line "the assembly
  censuses stand untouched" (3802) is true only of its own pass.
  Lawful: the withdrawn claim survives verbatim in the committed
  predecessor files (v2 3755–3756, chain-not-tree across candidate
  versions), and V3-6 accounts the edit. Recorded as RG-8 (NOTE).

Score: **REPAIRED** (RG-2 MINOR + RG-8 NOTE adjacent, neither
flips the hold).

### Check 3 — GF-3 (bundle rule closed-or-refuse) — REPAIRED

Original (MAJOR): the per-group primary-identifier enumeration
covered two group shapes; for any other lawful CESR
attachment-group class two conformant implementers could select
different primary identifiers and derive different bundle
identifiers for one bundle.

The repaired rule, v4 lines 3301–3307 (V3-7):

> "(for an indexed-signature group, the signer's prefix; for a
> couple, the coupled identifier; and for any other CESR
> attachment-group class, the group's primary identifier as fixed
> by the encoding round's carriage profile before that class may
> appear in a bundle - a bundler meeting a group class the profile
> does not enumerate refuses, it never chooses);"

Two-implementer derivation test, by case over lawful inputs:
(a) indexed-signature group → signer's prefix: determined by rule.
(b) couple → coupled identifier: determined by rule.
(c) any other class the (future) carriage profile enumerates →
identifier fixed by one committed enumeration both implementers
read: determined.
(d) any other class the profile does not enumerate → "refuses, it
never chooses": no bundle identifier exists for either
implementer; refusal is the determined outcome.
No lawful input remains on which two conformant implementers can
derive different bundle identifiers — the under-determination is
closed by closure-or-refusal, exactly the ordered shape. The rule
no longer chooses silently and no longer lets the implementer
choose.

Residue, recorded not scored against the repair:
- The 42-3 battery-6a item 2 tiebreak (two groups sharing one
  primary identifier) was graded MINOR in 42-3, was never given a
  GF label or a repair order, and is unchanged in v4 (RG-7, NOTE —
  carried residue, not new).
- The deferral target is named "the encoding round's carriage
  profile," yet what the profile fixes (the primary identifier
  entering the between-group ordering of the bundle-identifier
  preimage) is commitment-form semantics under the document's own
  GF-4 distinction — the choice decides must-affirm/must-refuse
  recomputation vectors. Divergence is impossible either way
  (refuse-not-choose pre-profile; one committed enumeration
  post-profile), so this is a scope-naming tension, not an
  under-determination: RG-6, NOTE.

Score: **REPAIRED**.

### Check 4 — GF-4 (aggregate-head confession) — REPAIRED

Original (MAJOR): the aggregate function and membership-proof
object were undetermined, and the openness was confessed under a
carriage label ("the construction's carriage is chartered to the
encoding round") — membership-verification semantics are not
carriage; the confession was real but mislabeled in scope.

The repaired head, v4 lines 1477–1482 (V3-8):

> "that head SHALL be an aggregate commitment over per-clause
> sub-blocks (the aggregate's digest function and concatenation
> order are semantics this document owes and the encoding round
> pins - an openness of commitment form, confessed here, not a
> carriage detail): each clause independently SAID-addressed ..."

Completeness of the confession, tested against the 42-3 grounds:
- The scope label is corrected in the exact terms the finding
  demanded: "semantics ... an openness of commitment form ...
  not a carriage detail." The mislabel does not survive.
- The two open parameters named — digest function and
  concatenation order — jointly determine the membership-proof
  object shape (what a proof carries — siblings, positions, or
  the digest list — is a function of the aggregate construction
  once those two are pinned), so the 42-3 "membership-proof
  object shape" gap is inside the confessed openness, not outside
  it. The confession is complete with respect to the finding's
  enumeration.
- Ownership and venue are committed: "this document owes and the
  encoding round pins" — the 42-3 disposition offered exactly
  this ("one sentence naming the aggregate function as an open
  semantic commitment of the encoding round, or committing it");
  the first branch is taken.
- The retained sentence "The construction's carriage is chartered
  to the encoding round" (1493–1495) is now consistent: the same
  round owns both halves, but the halves are named apart —
  semantics confessed as commitment-form openness, carriage
  chartered as carriage. No contradiction between the two spans.
- Part III S3-3 consequence: the must-affirm/must-refuse pair
  remains unfixturable until the encoding round pins the function
  — which is now what the text says out loud. Confessed openness,
  neither false nor incomplete: lawful under the round's own
  confessed-openness law.

Score: **REPAIRED**.

### Check 5 — SF-1/S3-3 (the §2.4 three-form sentence) — REPAIRED (with an RG-1 seed-station flag)

Original (SF-1, carrying the S3-3 seed-side ruling): seed §2.4
carried the conflation "A finding is disclosed *instead of* its
evidence; a no-disclosure mandate is discharged by construction
rather than by promise" — the conflation is the defect; the
three-presentation-form distinction existed kernel-side only.

The repaired sentence, v4 lines 636–640 (seed §2.4 via the 42-4
station's R-2 and the v4 splice):

> "A finding disclosed in place of its evidence is lawful under
> one of the three presentation forms the objects section of this
> standard types — replayed, warranted, or proven — and which
> form a no-disclosure mandate accepts is the mandate's own
> committed choice."

- The convicted conflation is gone (the "discharged by
  construction rather than by promise" claim does not survive
  anywhere in v4). The sentence now carries the distinction by
  lift — disclosure-of-finding is lawful only UNDER a typed
  presentation form, and the form choice is the mandate's
  committed choice — which is the ruled shape ("cites the
  kernel-side machinery; does not restate it," station R-2).
- Kernel-site consistency check (the check the brief orders): the
  kernel's three-presentation typing is the §13.3 consumption
  ladder — replay-native consumption (2431–2438), warranted
  consumption (2440–2455), and the proof rung admitted without
  being delivered (2482–2491). The seed's triple "replayed,
  warranted, or proven" names those three forms consistently —
  same three, same order of ascent, no fourth form invented, no
  form dropped.
- One inconsistency in the citation, flagged for the seed's own
  station (RG-1, MINOR): the sentence attributes the typing to
  "the objects section," and v4's uniform usage binds that phrase
  to §7 (the blinding-factor cite at 2127, the seat-credential
  cite at 2145, the carriage-division cite at 3318 all resolve
  "the objects section" to §7). §7 types three object forms —
  edict, verification cone, warranty (1338–1400) — a different
  triple: "warranted" and "replayed" have §7 anchors (warranty;
  cone-as-replay-evidence), but no §7 text types a "proven"
  presentation form; the proof rung is typed only at §13.3, and
  there as admitted-not-delivered ("No clause of this standard
  depends on such a proof," 2488–2489). The new §2.8 entry
  repeats the same pointer ("the presentation machinery the
  objects section types," 848). The distinction the ruling
  ordered is present and correct; its kernel address is
  imprecise, and "types" mildly overclaims the proof rung's
  admitted-not-delivered status. Comprehension-grade, no
  implementer divergence; seed bytes, so flagged, never edited.

Score: **REPAIRED** (RG-1 MINOR flagged to the seed station).

### Check 6 — census chain (v1 → v4 complete accounting) — PASS

The six census sections exist in v4's appendix in chain order:
delta census (3507), structure census (3674),
collision-by-addition census (3724) — the three assembly censuses
— then repair census (3799, v1→v2), v3 micro-pass census (3891,
v2→v3), v4 seed-succession census (3917, v3→v4). Chain-not-tree:
each later census appends; the assembly censuses stand.

**Digest chain, independently recomputed.** Every pin cited by
the two new censuses verifies against the committed files:
v2 `a11f2902…` ✓, 42-3 report `f5220ca6…` ✓ (v3 census, 3894/3897);
v3 `cd16f4ba…` ✓, seed-v2 `dfd1ddc1…` ✓, seed-v3 `870a4d7c…` ✓
(v4 census, 3919–3921). The 42-4 station record's pins (seed-v2,
seed-v3, gauntlet report, supplement 3) also verify.

**Exhaustive hunk mapping, v2→v3** (independent diff: 9 change
hunks + the census append):
1464 → V3-8; 1558 → V3-1; 1562 → V3-2; 1661 → V3-3; 2927 → V3-5;
3284 → V3-7; 3450 → V3-4; 3755–3756 → V3-6; the final append is
the v3 census itself. Eight rows, eight substantive hunks,
one-to-one; zero unmapped. The census's own summary line
("Entries: 8") is accurate.

**Exhaustive hunk mapping, v3→v4** (independent diff: 4 hunks):
636–640, 808–818, 844–850 — exactly the three seed hunks the v4
census names (§2.4 / §2.7 / §2.8), all inside the Chapter 2 body;
3916–3928 is the v4 census append itself. Zero unmapped.

**Seed splice integrity.** The v4 Chapter 2 body (§2.0 through
§2.8, up to the section separator) is an exact substring of
`weave/42-taxonomy-chapter-v3.md`; the seed file's residue
outside the match is only its pin-closure header block (before)
and its closing status line (after) — exactly the draft-status
apparatus the integration heading (443–453) confesses replacing.
The station record's own verification block (three hunks, 9 v2
lines → 23 v3 lines, exactly-once substitutions, Utah exhibit
sentence byte-identical and located once) is consistent with the
independent diffs run here.

**Composite closure.** Independent v2→v4 diff: 12 hunks — the 8
V3 rows + the 3 seed hunks + the appended census blocks. Every
v2→v4 change is accounted by exactly one census row (or is a
census block accounting itself). **No census-escape found; the
BLOCKING condition is not met.**

**Entry sample (5 sampled across the three post-assembly
censuses, verified against text):**
- Repair census K1 (§18 track-one confession) → v4 3116
  "colorless-base claim is scoped to parseability" ✓.
- Repair census C2 (§8.1 adapter) → v4 1537 "instantiated, never
  returned" ✓.
- Repair census I2 (§15 KRAM) → v4 2826 ✓.
- v3 census V3-5 (walls count) → v4 2945 "seven walls" ✓.
- v3 census V3-8 (aggregate head) → v4 1478–1482 confession ✓.
- (v4 census's single entry verified above by splice test.)

Two accounting nits, neither an escape (both changes ARE
censused; the meta-text mispins their sites): RG-2 covers the
V3-5 "s17"/V3-3 "s8.4" section mispins; RG-3 (NOTE) covers the
v4 census's closing claim "everything outside the seed body
byte-identical to v3," which is true of everything except the
census block's own append — the standing
appended-census-accounts-itself convention, harmless but
imprecise as worded.

Score: **PASS** (complete accounting; RG-2 MINOR, RG-3 NOTE).

---

## Part II — young-prose battery

Perimeter: every line the v3 micro-pass inserted (the 8 V3 sites:
v4 lines 1478–1482, 1576, 1580, 1679, 2945, 3302–3307, 3473,
3778–3782, and the v3 census block 3891–3915) and every line the
seed station's three hunks inserted (v4 lines 636–640, 808–818,
844–850, and the v4 census block 3916–3928). All are
never-before-reviewed text.

**Register check.**
- BCP 14 force: zero BCP 14 keywords inside the young insertions
  themselves (scan). The GF-3 insertion extends a pre-existing
  SHALL-ruled blockquote without adding keywords; the GF-4
  parenthesis sits inside a pre-existing SHALL sentence; the seed
  hunks keep the seed's zero-keyword charter (full-seed scan: 0
  keywords). No force regression, no unruled new obligation
  smuggled keyword-free — the §2.7 "is discharged only where"
  is definitional posture prose in the seed's established
  keywordless register, matching the sentence it replaced.
- Economics vocabulary: zero hits in young prose (scan).
- Declarative voice / ALL-CAPS: no stray emphasis; the only
  ALL-CAPS tokens are initialisms (CESR) and census meta-text
  citing finding labels (GF, SF, "the gauntlet's BLOCKING
  finding" — accounting register, lawful as in the prior
  censuses' own practice).
- One typographic register drift, RG-4 (MINOR): four young-prose
  sites use an ASCII hyphen as a spaced dash (" - ") where the
  document's register is the em-dash (618 em-dash lines):
  1480 (GF-4 parenthesis), 3305 (GF-3 rule), 3781 (census
  rescope), 3913 (v3 census summary). Mechanical repair through
  the ordinary census.

**Over-generalization check** (mechanism-as-role test on every
young span): the §2.7 repair names its surfaces (non-issuer
witnesses, caches, issuer-published endpoints, presentation
registries) rather than gesturing at "the transport layer"; the
GF-3 completion names the deferral venue (the encoding round's
carriage profile) and the refusal behavior; the GF-4 parenthesis
names the two open parameters (digest function, concatenation
order) and their owner; "issuer-observable surfaces" is a
predicate the same sentence's enumeration instantiates — general
but not generic. Zero occurrences of "the KERI's"/"the CESR's"/
"the ACDC's" by cross-line whitespace-tolerant regex over the
whole file (the GF-5 class is extinct). No "substrate"-register
regression in any young span. PASS.

**Internal consistency with adjacent text.**
- §2.4: the repaired sentence's triple (replayed, warranted,
  proven) is consistent with the §13.3 ladder; adjacent
  ground/consequence prose unbroken. The "objects section"
  address imprecision is RG-1 (check 5).
- §2.7: the retained type argument and the new surface obligation
  compose without contradiction (the type argument is scoped to
  "no clause can require issuer contact"; the surface obligation
  covers what the type argument no longer claims); the following
  federation sentence ("And where several peer regimes…")
  connects grammatically and semantically.
- §2.8: the two new confessions are true of the chapter as
  repaired (§2.7 does state the surface obligation; the chapter
  does defer proof machinery to the kernel) — confessions
  neither false nor incomplete with respect to the 42-3 record.
- §7 aggregate head: the parenthesis agrees with the retained
  carriage sentence at 1493–1495 (check 4).
- §19 bundle rule: the refuse-not-choose clause is consistent
  with the adjacent fail-loud doctrine (identifier mismatch
  convicts carriage) and strengthens it (no identifier is ever
  derived for an unenumerated class).
- §16/appendix: the walls-count word and the census rescope are
  consistent with every other walls mention (independent
  seven-sweep) and with the v3 census's V3-5/V3-6 rows.
- The four GF-5 cure sites (1576, 1580, 1679, 3473) read
  grammatically with their carried possessives ("cured when
  KERI's superseding rules…", "admissible under KERI's
  delegated-recovery rules", "at the key tier, KERI's
  superseding-recovery calculus", "and KERI's protections hold
  undiminished") — the dangling articles are gone, no new
  artifact introduced.

Battery verdict: PASS (RG-4 MINOR typography; no register, force,
generality, or consistency defect of substance).

---

## Findings register (severity-ordered; namespace 42-5/RG-n)

No BLOCKING. No MAJOR.

- **RG-1 — MINOR (flagged for the seed's own station; seed
  bytes, no edit proposed).** Seed §2.4 (v4 638) and §2.8 (848)
  attribute the three presentation forms to "the objects
  section," the phrase v4 elsewhere uniformly binds to §7
  (2127, 2145, 3318); the replayed/warranted/proven triple is
  actually typed at §13.3 (2431–2491), and the proof rung is
  admitted-not-delivered there, so "types" mildly overclaims it.
  Comprehension-grade; no implementer divergence.
- **RG-2 — MINOR (census meta-text accounting).** Section
  mispins in the v3 micro-pass census and the collision rescope:
  V3-5 "s17 walls count" and the rescope's "the walls count of
  section 17" — the span lives in §16 (2945, heading 2879);
  V3-3 "s8.4 force distinction" — the span lives in §8.3 (1679,
  §8.4 begins 1781). The changes themselves are correctly
  accounted; the site labels are off by one section.
- **RG-3 — NOTE.** The v4 seed-succession census's closing claim
  "everything outside the seed body byte-identical to v3" is
  exact except for the census block's own append — the standing
  self-accounting convention, imprecise as worded.
- **RG-4 — MINOR.** Four young-prose ASCII spaced hyphens where
  the document register is the em-dash: 1480, 3305, 3781, 3913.
  Mechanical repair through the ordinary census.
- **RG-5 — NOTE.** §2.7's discharge enumeration names three of
  A5's four observation channels explicitly; correlatable
  acquisition identifiers are covered only by the general
  "issuer-observable surfaces" predicate (which the necessary-
  condition form does reach). For the fixture round's vector
  work.
- **RG-6 — NOTE.** GF-3's deferral venue is labeled "the
  encoding round's carriage profile," yet what the profile fixes
  (the primary identifier entering the bundle-identifier
  preimage ordering) is commitment-form semantics under the
  document's own GF-4 distinction. No divergence is possible
  either way (refuse pre-profile, one committed enumeration
  post-profile); scope-naming tension only.
- **RG-7 — NOTE (carried, not new).** The 42-3 battery-6a
  tiebreak residue (two groups sharing one primary identifier)
  was graded MINOR there, never assigned a GF label or a repair,
  and is unchanged in v4. Surfaces in the must-reject vector
  family when fixtured.
- **RG-8 — NOTE (register honesty, resolved lawful).** The GF-2
  rescope edits the collision census's closing lines in place
  rather than appending a correction block. Append-never is
  satisfied at the artifact-chain grain — the withdrawn absolute
  claim survives verbatim in committed v2 (3755–3756) and the
  edit is accounted by V3-6 — but the repair census's standing
  header "the assembly censuses stand untouched" (3802) is now
  true only of its own pass. Recorded for the ratifying
  authority's reading.

---

## Verdict

**REPAIRS-HOLD.**

| # | finding (42-3) | repair act | score |
|---|---|---|---|
| 1 | GF-1 / N2 (A5) — BLOCKING, issuer non-observation by type | seed station R-1 + v4 splice | **REPAIRED** (RG-5 NOTE) |
| 2 | GF-2 — MAJOR, six-walls + census totality | V3-5 + V3-6 | **REPAIRED** (RG-2, RG-8) |
| 3 | GF-3 — MAJOR, bundle-rule under-determination | V3-7 closed-or-refuse | **REPAIRED** (RG-6, RG-7 NOTES) |
| 4 | GF-4 — MAJOR, aggregate-head confession mislabeled | V3-8 semantics confession | **REPAIRED** |
| 5 | SF-1 / S3-3 — §2.4 conflation | seed station R-2 + v4 splice | **REPAIRED** (RG-1 flagged) |
| 6 | census chain v1→v4 | six censuses, chain-not-tree | **PASS** (no escape) |
| 7 | young-prose battery | all v3 + station insertions | **PASS** (RG-4 MINOR) |

GF-5 verified extinct in passing (four cure sites read clean;
cross-line regex zero). SF-3 verified discharged inside check 1
(the §2.8 confession completions). No new finding rises above
MINOR; the three MINORs are one seed-station comprehension nit,
one census-label nit, and four typography characters. Nothing
found by this re-gauntlet stands between candidate v4 and the
ratifying authority's freeze-lift decision, which is that
authority's alone — never this leg's.

Disposition, one sitting: (a) RG-2/RG-3/RG-4 through the
ordinary census as mechanical corrections whenever next opened;
(b) RG-1 to the seed station's ledger for its next sitting (no
urgency — comprehension-grade); (c) RG-5/RG-6/RG-7 to the
fixture round's vector obligations; (d) RG-8 needs no repair,
only the authority's awareness while reading the appendix.

---

Report complete. Six checks run, one battery run. Subject digest
re-verified at close: sha256
a9ac1ed5adf0d0ce85c993b7ecb6d459e4192c0d60efc09a93dccb8f91439c89
(match: no drift during the round).
