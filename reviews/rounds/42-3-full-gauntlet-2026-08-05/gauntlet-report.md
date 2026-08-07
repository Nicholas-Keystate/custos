# 4.2 full-document gauntlet report (2026-08-05)

Round: `reviews/rounds/42-3-full-gauntlet-2026-08-05/`.
Subject: `weave/custos-4.2-candidate-v2.md`, 3,863 lines.
Subject digest verified before reading: sha256
`a11f2902c6e18404ba22c9468681e8a92b57af01fe1de53b08dbabb2d5c786f0`
(matches the round design's pin; no mismatch).

Reviewer: fresh-context adversarial gauntlet leg, read-only on all
inputs, sole output this file. Inputs consumed: the round design;
`reviews/rounds/42-2-integration-review-2026-08-03/sol-leg-findings.md`
(the nine named attacks' original text); `weave/42-repair-report.md`
(repair census / ruling→site map); `reviews/ruling-record-supplement-3-2026-08-03.md`
(the rulings the repairs execute); `weave/42-taxonomy-chapter-v2.md`
(seed-block comparison source). Findings never edits. Seed-block
content findings are flagged for the seed's own station.

Report is written incrementally, part by part (process note: prior
delegations died of infrastructure loss mid-run; partial progress
must survive).

---

## Part I — the nine named attacks (per ruling S3-2)

Method per row: original finding restated from
`42-2 .../sol-leg-findings.md`; repair located from the candidate's
own repair census (appendix, fourth census) and confirmed against
the v1→v2 byte diff (83 hunks, all mapped, none inside the seed
block 469–844); score with byte-grounds.

### N1 (was A4) — clause-selective disclosure vs the undisclosed computation — REPAIRED (with a flagged seed-station residue)

Original: revealing the cited clause proves commitment, not that
hidden evidence satisfies it; the prose conflated three
presentation forms and overclaimed the mandate.

Repair located: (a) the aggregate-Constitution construction at
the commitment-form site, §7 lines 1461–1477 (census B7):
clause-set head SHALL be an aggregate commitment over per-clause
u-salted, SAID-addressed sub-blocks; membership recomputed;
"revealing a clause against [a monolithic digest] proves only
that the clause was committed somewhere, never its membership in
the law in force" (1472–1474) — the exact defect named. (b) The
routing note at the Chapter 2 integration heading, lines 454–467
(census L1), confessing the S3-3 repair enters the seed only
through the seed's own station. (c) The three-form triple exists
in kernel text as the consumption ladder: replay-native
consumption (2413–2420), warranted consumption (2422–2437), and
the proof rung admitted-not-delivered (2464–2473, "admitted
without being delivered ... zero-knowledge proof of a fold").

Score: REPAIRED. Residue flagged for the seed's own station,
never as an in-place edit: seed §2.4 lines 632–638 still carries
the convicted conflation verbatim ("A finding is disclosed
*instead of* its evidence; a no-disclosure mandate is discharged
by construction rather than by promise") — the S3-3 residue
ruling ("the conflation is the defect") must land at seed
regeneration, and the routing note (454–467) names only the
aggregate half of S3-3 explicitly, not the presentation-form
residue. See SF-1/GF-13.

### N2 (was A5) — issuer non-observation "by type" — UNREPAIRED

Original (BLOCKING): local appraisal prevents a semantic
phone-home requirement but does not structurally prevent issuer
observation — TEL queries, OOBI resolution, correlatable
identifiers, issuer-observable presentation registries; the bar
must be tested at the transport and resolution surfaces.

Byte-grounds for UNREPAIRED:
- The attacked sentence stands byte-identically in v2 at lines
  805–810 (seed §2.7): "the bar is discharged by type rather
  than by audit alone: ... the issuer is structurally outside
  that computation — there is nothing to phone home about."
- The seed block is byte-identical across the repair pass
  (verified: v2 lines 469–844 are an exact substring of
  `weave/42-taxonomy-chapter-v2.md`; zero diff hunks in range).
- The repair census (3783–3858) contains no entry citing SOL A5
  — census finding columns cite SOL A1, A3, A4, A9, A10, A12,
  A16, A17, A19, A20, A21, A23, A24, A25, B1–B8, and the
  same-family A-n series; A5 is absent. No supplement-3 ruling
  orders an A5-specific repair (S3-3 covers disclosure of law,
  not issuer observation of use).
- No kernel-side scoping landed: nothing in §6, §7, §13, or §15
  tests the observation bar at transport/resolution surfaces or
  scopes the seed's by-type claim. The §15 KRAM/OOBI repairs
  (2803–2820) concern the serving domain's request surface, not
  issuer observation of credential use.
- The confessed-openness defense is unavailable: seed §2.8's
  confession list (828–844) confesses fixture-pending postures,
  the narrowed jury, and the fold-purity question — it does not
  confess the observation-surface gap. An attack on a confessed
  boundary must show the confession false or incomplete: here
  the by-type discharge is asserted, not confessed open, and the
  §2.8 enumeration is incomplete with respect to it.

Score: UNREPAIRED. Severity BLOCKING (a named attack under
S3-2's must-survive rule). Repair routes lawfully through the
seed's own regeneration station (the site is graduated bytes);
a kernel-side scoping sentence at the §7 disclosure-posture or
§15 serving-surface sites would additionally be an ordinary
census-accounted repair. Flagged, not edited. See GF-1/SF-2/SF-3.

### N3 (was A9) — universal "credential-layer salt-field discipline" — REPAIRED (minor residue)

Original (BLOCKING): a universal salt-field discipline naming
nothing — location, entropy, disclosure, canonicalization
undefined; not an ACDC rule.

Repair located: §7 blinding mandate, lines 1447–1459 (census
B6): the blinding factor is named as "ACDC's own discipline for
exactly this — the high-entropy UUID field, the u-field ...
cited, not reinvented"; scope narrowed to objects whose
self-addressing identifier is committed in advance of intended
disclosure, born-disclosed objects exempt; preimage-not-traffic
scoping stated (1457–1459). The §11 custodian axis carries the
mandate by reference (2106–2109, census entry 31). The
per-clause use composes with the aggregate (1464–1468).

Score: REPAIRED. Minor residue (GF-7): "ACDC's own discipline"
is applied by mandate to *any* pre-committed self-addressed
object class, including non-ACDC objects (GEL events, rosters),
where field placement and preimage inclusion are not derivable
from the cited discipline; carriage is chartered to the encoding
round, which bounds the exposure.

### N4 (was A10) — Kever/Tever claimed to instantiate the codomain — REPAIRED

Original (BLOCKING): acceptance machinery does not return the
four-valued, ground-carrying finding type.

Repair located: the adapter sentence, §8.1 lines 1516–1524
(census C2): "instantiated, never returned: KERI's and the
registry layer's acceptance machinery do not return this
document's finding type, and their operational outcomes
(acceptance, escrow, validation failure, missing receipts) enter
appraisal as typed evidence facts; the fold computes findings
over those facts." Reinforced at §13.2 step 1 (2375–2378, census
G1): admission outcome "enters appraisal as a typed admission
fact, never as a finding of this document's codomain."

Score: REPAIRED. The residual "realizes it over key events"
(1517) is directly bounded by the adjacent adapter clause; no
site elsewhere claims the lower folds return findings (checked:
1963–1964 assigns them evidence roles only).

### N5 (was A12) — edge thresholds equated with signing thresholds — REPAIRED

Original (BLOCKING): "one algebra" false generality.

Repair located: §9 composed evidence, lines 1938–1948 (census
D1), executing S3-1 verbatim in substance: "analogous — the same
satisfaction shape over differently typed slot judgments, never
one algebra: a KERI signing slot asks whether a key signed; an
edge slot here asks whether a credential stands, and that is
this document's own fold question — schema, issuer
qualification, registry state, disclosure state — never the
substrate's," plus the forward mint clause (1944–1948: shared
predicate as committed artifact upstream → cite by digest →
declared shared dependency by ordinary migration). The dossier
threshold-operator sentence at 1354–1356 equates only
dossier-with-standing composition grammar (both ACDC-side) and
does not reintroduce the cross-end equation.

Score: REPAIRED.

### N6 (was A19) — authentication flattened to one admission step — REPAIRED

Original (BLOCKING): signatures, coordinates, receipts treated
as one context-free verdict.

Repair located: (a) cone-root typed authentication grade of four
components, §7 lines 1370–1377 (census B2): controller threshold
verified; witness roster identified from the applicable
establishment state; receipt threshold satisfied; establishment
coordinate cited; unmet receipt threshold discharges as pending
enumerating the missing receipt indices — the S3-5 ruled shape
exactly. (b) §13.2 step 1's typed admission fact (2372–2378).
(c) KRAM named with the cache-window boundary, §15 lines
2803–2817 (census I2): transport admission MAY be
wall-clock-windowed (the window is KRAM's cache window);
appraisal position MUST NOT be. (d) Observer-relative acceptance
vs deterministic fold distinguished at §6 (1279–1285, census A8).

Score: REPAIRED. Noted, not scored down: the grade's four ruled
components omit delegation state and BADA/first-seen grade,
which the original finding also named — that narrowing is the
ruling's own choice (S3-5), recorded here for the station's
vector work.

### N7 (was A20) — witnesses claimed to discharge availability — REPAIRED

Original (BLOCKING): receipts do not guarantee retrievability of
TEL/GEL/schema/clause payloads.

Repair located: §15 availability charter, lines 2769–2801
(census I1): "witness receipts prove receipt, never serving; the
charter binds what the medium commits, and its discharge is
appraised like any clause, never presumed from the witnesses'
existence" (2784–2787); the per-stratum floor over KERI's
committed witness fields with the floor-violating establishment
event convictable on the same KEL bytes (2776–2783); mirrored at
the §5 charter definition (1259–1269, census A7) and admitted as
a governed object class in §12 (2227–2232, census F4).

Score: REPAIRED. No residual discharge-by-existence claim found
by independent grep.

### N8 (was A24) — track-one registry reuse claimed neutral — REPAIRED

Original (BLOCKING): reused TEL ilks carry native transition
semantics; registry-capable consumers may act on them.

Repair located: §18 track one, lines 3094–3100 (census K1): "One
confession binds the election: reuse is semantically loaded for
governance-blind consumers — the reused ilks carry their native
registry semantics, and a registry-capable consumer may act on
them as registry state — so the colorless-base claim is scoped
to parseability, never to meaning-neutrality, and a domain
electing this track owns that load as committed law." Scope
verified against the other colorless-base sites (1389–1391,
2448–2451, 3091–3093): each is parse/verify-scoped and
consistent with the confession.

Score: REPAIRED.

### N9 (was A25) — genus reservation as unilateral GEL law — REPAIRED

Original (BLOCKING): a GEL enactment cannot reserve CESR code
points for interoperable interpretation.

Repair located: §18 genus paragraph, lines 3180–3201 (census
K2): the genus namespace named as "CESR's ... externally
stewarded table"; "The enactment binds the reserving domain's
own profile and nothing wider: it is a reservation in a table
someone else stewards, and it cannot by itself create
interoperable CESR meaning"; recognition a distinct, later,
bilateral event and "the interoperability gate for everything
beyond it"; the covenant seal's reserved type value stated
beside it as a namespace of the same kind, answered together
(3196–3201). Gate two's residual "pure enactment" (3340) now
refers to seat enactments in the domain's *own* track-two ilk
table — genuinely local law — with the reservation's
non-recognition confessed in the same paragraph (3332–3334);
the original conflation does not survive the K2 scoping.

Score: REPAIRED.

### Part I scorecard

| # | was | attack | score |
|---|---|---|---|
| N1 | A4 | clause-selective disclosure without a presentation construction | REPAIRED (seed-station residue flagged) |
| N2 | A5 | issuer non-observation asserted by type | **UNREPAIRED** |
| N3 | A9 | universal salt-field discipline naming nothing | REPAIRED (minor residue) |
| N4 | A10 | Kever/Tever instantiate the codomain | REPAIRED |
| N5 | A12 | one algebra across threshold ends | REPAIRED |
| N6 | A19 | authentication flattened to one step | REPAIRED |
| N7 | A20 | witnesses discharge availability | REPAIRED |
| N8 | A24 | track-one reuse semantically neutral | REPAIRED |
| N9 | A25 | genus reservation as unilateral law | REPAIRED |

---

## Part II — the standing gauntlet batteries

### Battery 1 — register

**BCP 14 force.** Independent keyword scan: every ALL-CAPS
keyword instance sits in a ruled span; the only lowercase
"must not" instances (lines 22, 93) state KERI's own validator
maxim in reported prose, deliberately unkeyworded — lawful under
reading rule 1. The seed block (469–844) contains zero BCP 14
keywords (verified by scan), consistent with its typing-chapter
charter. No stray ALL-CAPS emphasis found outside keywords and
established initialisms (KERI, ACDC, CESR, GARD, KEL/TEL/GEL,
SAID, OOBI, KRAM, DI2I, UUID, KSN, BCP/RFC).

**Economics vocabulary.** One hit outside census meta-text: line
1958 "This document specifies no monetary consequence for
breach" — an exclusion, not an economic register; lawful. Census
mentions of "economic register" (3499, 3600) are accounting
meta-text. PASS.

**Pulpit anaphora.** Sentence-start frequency scan: no repeated
rhetorical opener above noise (top repeats are list numerals).
PASS.

**Participle discipline.** "colored receipt" absent (scan). All
nine "colored"/"colorless" kernel uses are participial or name
the judging frame's act (385–386, 2404, 2443, 2448–2451, 2650);
census entries 3522/3541 are meta. PASS.

**Direct-naming law.** Independent grep of the generic register
outside the seed. The repair claim ("zero unlawful generic sites
outside three enumerated residuals — 1092, 1944, 3529") tests as
follows:
- The three claimed residuals: 1092 ("the substrate's own naming
  grammar", the three-logs entry) — lawful, the A-10 exemplar;
  1944 ("never the substrate's") — lawful, the S3-1 ruled
  sentence's deliberate contrast; the third is mispinned: v2
  line 3529 is delta-census meta-text; the definitional site
  minting "the substrate of record" is line 1007. The
  lawfulness claim itself holds at 1007 (it is the license
  site); the pin is wrong. See GF-6.
- Additional role-abstract residuals the enumeration does not
  carry: 882 ("the frame-invariant substrate", §3
  specifies-list apposition to the medium); 1041 ("terms
  inherited from the substrate"); 1090/1096/1099 ("Substrate
  vocabulary, cited", "Substrate-native" — the A-10 three-logs
  exemption); 1195 ("the substrate act" — a reserved term
  minted at the law-ladder definition); 2324 ("the substrate
  can express a joint commitment as a group identifier" — the
  A-10 group-identifier-rejection exemption); 2844 ("a
  substrate upgrade is a migration enactment"); 2855 ("any
  substrate or ecosystem corpus" — travel posture, genuine
  generality). Each site individually survives the §4 license
  ("lawful only where the claim genuinely holds for any
  conformant substrate of this class") or is definitional/
  exempted — no site was found where a KERI-specific mechanism
  hides behind the generic noun. The direct-naming LAW holds;
  the repair report's residual COUNT is inaccurate. GF-6, MINOR
  (round-artifact accounting, not candidate text).
- "the medium": 34 kernel uses, all resolving to the §6 defined
  term (KERI's key state, SAID-addressed bytes, duplicity
  relation — "The medium is KERI's achievement, cited," 1304).
  Lawful as a defined term of art.

**Conversion artifacts (young repair prose).** Four sites where
the S3-8 sweep produced ungrammatical "the KERI's": 1558–1559
("cured when the / KERI's superseding rules"), 1562–1563
("under the / KERI's delegated-recovery rules"), 1661–1662
("the / KERI's superseding-recovery calculus"), 3450–3451 ("the
/ KERI's protections hold undiminished"). Mechanical residue of
"the substrate's" → "KERI's" substitutions that left the
article. GF-5, MINOR.

### Battery 2 — sacrosanct and provenance

All verified from disk bytes by independent scan:
- `KERI detects; a GARD adjudicates.` — count 1 (line 21; the
  §1.0 site at 96–97 line-wraps across "GARD\nadjudicates",
  same bytes modulo the wrap, as in the predecessor). PASS.
- `Her computed answer testifies.` — count 1 (line 119). PASS.
- `acts, and is held to account, by the same committed` — count
  1 (line 35, continuing "judgments." on line 36). PASS.
- `receipt of performed governance` — count 2 (lines 38, 267),
  matching the predecessor's span-4 count. PASS.
- `the compact form changes cost, never meaning` — count 1
  (line 3258). PASS.
- Abstract line 21 reads "KERI detects; a GARD adjudicates. KERI
  ends" — the ratifying-authority edit stands. PASS.
- Seed block byte-identity: v2 lines 469–844 are an exact
  substring of `weave/42-taxonomy-chapter-v2.md` (file digest
  dfd1ddc1… as pinned at line 445); the only material outside
  the block is the seed's draft-status apparatus, replaced by
  the integration heading exactly as the heading confesses
  (443–453). The v1→v2 diff has zero hunks in 469–844. PASS.
- Predecessor digest: the cited 4.1 pin (ff8b9e7a…, lines 4–5
  and 2961–2962) verifies against
  `staged-repos/custos/spec/custos-4.1.md` (independent hash:
  match). The 4.0 (9cefdc5d…) and 3.3 (18b0469e…) pins match
  the succession record's lineage. PASS.

### Battery 3 — census

**Delta census sample (10 entries, verified against text):**
entry 2 (abstract replay sentence — 31–34, refusals re-derived
as decisions ✓); entry 3 (verification-cost register — 38–51,
engineering units, no economic vocabulary ✓); entry 5 (§1.2
covenant-seal digest-precedence test — 193–197 ✓); entry 12 (§4
two pin kinds — 980–996 ✓); entry 20 (§7 blinding mandate —
1447–1459 ✓); entry 23 (§8.3 bearing — 1657–1676 ✓); entry 27
(§8.4 conviction ladder — 1797–1831 ✓); entry 39 (§16 seven
walls own-text — 2868–2912 ✓); entry 44 (§18 designation and
membership — 3133–3170 ✓); entry 47 (§19 whole — 3237–3452 ✓).
All ten verify.

**Repair census sample (10 entries, verified against the v1→v2
byte diff):** A8 (1279–1285 observer-relative vs deterministic
✓); B2 (1370–1377 four-component grade ✓); B6 (1449–1452
u-field ✓); B7 (1460–1477 aggregate insertion ✓); C2
(1519–1524 adapter ✓); D1 (1938–1948 analogous + mint clause
✓); E5 (2137–2149 delegated-gAID MAY profile ✓); I1 (2775–2787
floor + receipts-prove-receipt ✓); K1 (3094–3100 track-one
confession ✓); N3 (3276–3286 Blake3-256, qb64, per-group
enumeration ✓). All ten verify.

**Census-escape check (v1→v2).** The full diff (83 hunks) was
mapped hunk-by-hunk against the 74 repair-census entries: every
hunk is attributable to a census entry (multi-line entries span
adjacent hunks; the final append block is the census itself).
Zero hunks inside the seed block. No unaccounted change found.
PASS as to changes.

**Collision escape found (carried text vs new text).** Line 2927
reads "A reader who infers a completed construction from the
six walls has inferred more than this document states." The
walls are SEVEN in this edition (2868 "Seven commitments"; 2906
"These seven are walls"; delta entry 39 "membership conserved
at seven"; §1.4 line 304 "seven fixed walls"). "six walls" is
the predecessor's count (4.1 enumerates "Six commitments"),
carried stale into a section whose enumeration the same edition
changed. The collision-by-addition census asserts "Zero carried
spans retained defective; zero collisions unexamined" (3755–
3756) — this span falsifies that assertion. GF-2, MAJOR:
internal inconsistency in the walls enumeration (battery 4's
exact target) plus a false census totality claim.

**Structure census vs section inventory.** All 4.1 sections
dispositioned against the actual v2 inventory (Head, Abstract,
Introduction, Ch.1 §1.0–1.7, Ch.2 §2.0–2.8, §3–§19, appendix);
the renumbering map (4.1 §n → v2 §n+1 from §2 on) is consistent
across all rows; additions list matches the text. The
"carried(12)"-style rows are stale relative to v2's repairs
lawfully — the fourth census's header states it supersedes as
the v1→v2 accounting while the assembly censuses stand
append-never. PASS.

### Battery 4 — internal consistency

- **§-cross-references:** every "section n"/"§n.m" reference
  spot-resolved against the inventory (17 succession ✓, 16
  openness ✓, 19 gates ✓, 18 grammar ✓, 14 recourse ✓, 15
  federation ✓, 13.x transformation ✓, 12 classes ✓, 11
  rotation ✓, 10 seals ✓, 9 standing ✓, 8.5 separation ✓, 7
  objects ✓, 5 definitions ✓, 4 reading rules ✓, Chapter 1/2
  cites ✓). No dangling reference found.
- **Walls enumeration:** §16 enumerates seven, internally
  complete (each wall one commitment; wall 3 explicitly fuses
  enumeration + no-backward-edge as one; wall 6 names its
  descent to the §18 site rule, and 3073–3074 cites back
  correctly; wall 7 carried with its retype provenance). Wall
  mentions elsewhere: 304 (seven ✓), 336 ✓, 2870–2871 ✓, 2895 ✓,
  3074 ✓, 3234 ✓ — and ONE defect: 2927 "six walls" (GF-2,
  above).
- **Codomain identity:** the four values + refusal-outside are
  stated at §1.1 (121–135), §1.2 (173–183), §1.4 wall cite,
  §8.1 (1496–1510), §8.5 (1878–1884), §10 satisfaction fold
  (2008–2012), §13.2 step 3 (2387–2390), §16 wall 1
  (2875–2876). Identical at every site; no fifth value anywhere;
  refusal consistently an operational fact, never a finding;
  the §8.5 compound-product rule preserves components as a
  product, not a fifth shape. PASS.
- **Two currents / no backward edge:** stated at §8.4
  (1778–1795), §16 walls 3–4 (2879–2884); the §8.3 forbidden
  table (1678–1699) enumerates seven forbidden edges with no
  backward edge; the evidence-ordering reversal condition
  (1711–1732) is explicitly a NEW finding at a new position,
  not an edge — consistent with "no backward edge" at 1690 and
  with the forbidden-table's defeated→affirmed reason. PASS.
- **Three-tier fold vocabulary:** Kever/Tever/Gever used at
  §1.2 (163–171), §5 (1113–1128), §8.1 (1516–1524), §9
  (1963–1966). Every use assigns the lower folds evidence-
  producing roles consistent with the C2 adapter sentence
  ("instantiated, never returned"); no site has a lower fold
  returning findings. PASS.

### Battery 5 — deletion and substitution (exhibit law)

- **Utah** (sole named instance in the document; SEDI absent by
  scan): the naming lives in one parenthetical, seed lines
  483–487. Deletion test: the surrounding sentence ("This shape
  is now a class of legal mandate. Legislatures have begun to
  require, in prose, what no prose can deliver...") stands with
  the parenthetical deleted; the seed carries zero BCP 14
  keywords, so no ruled span exists in the chapter to lose
  ground; the kernel's ruled spans nowhere cite the instance
  (grep: no kernel Utah/SEDI reference). §2.7's exhibit
  paragraph (818–827) already holds the enrolled program
  unnamed, routed to the companion on its own clock. PASS.
- **Substitution test:** replacing the instance with a
  counterfactual regime of the typed class (public canonical
  text, registrable acts, decision rules) alters no ruled span:
  the three commitments of §2.7 (782–798) quantify over "any
  such regime," and §2.8 (838–841) commits exactly this
  deletion/substitution survivability, which this battery
  exercises and confirms. PASS.

### Battery 6 — fresh-implementer attack

**Mechanism (a): the bundle-preimage rule (3275–3304).**
Implementable from the text: preimage = receipt bytes exactly
as receipted, then each attachment group's framed bytes (count
code included), between-group order lexicographic over the qb64
of each group's primary identifier, intra-group order per the
group's own grammar; digest = Blake3-256 SAID, qb64. Guesses
required:
1. "Primary identifier" is enumerated for exactly two group
   shapes ("for an indexed-signature group, the signer's
   prefix; for a couple, the coupled identifier"). CESR receipt
   attachment streams admit further group classes (transferable
   indexed signature groups carrying prefix+sn+digest,
   quadruples/sextuples, pathed material). For any group
   outside the two named shapes, two conformant implementers
   can select different primary identifiers, deriving different
   bundle identifiers for one bundle. The divergence is
   fail-loud at consumption (identifier mismatch → carriage
   conviction), not silent acceptance of different content
   under one identifier. Grade: MAJOR (GF-3). The census claims
   the enumeration was "restored verbatim from the gates
   doctrine" — restoration is confirmed as text, but the
   restored enumeration is exemplar-shaped, not total, and gate
   one's vector families do not enumerate a per-group-class
   coverage obligation.
2. Tiebreak for two groups sharing one primary identifier:
   undefined. Grade: MINOR (cosmetic until a real stream
   exhibits it; the must-reject family would surface it).
3. Everything else — dummy convention, digest class, wrapping,
   two liability layers — is determined. The gate structure
   (compact form unusable until gates stand) bounds field
   exposure.

**Mechanism (b): the aggregate-Constitution commitment
(1461–1477).** Determined from the text: per-clause sub-blocks,
independently SAID-addressed (§5 clause definition composes,
1186–1189), each carrying a u-field blinding factor;
clause-selective disclosure reveals cited clauses + salts;
verifier "recomputes membership in the anchored aggregate."
Guess required: the aggregate function itself — Merkle tree,
sorted digest concatenation, ACDC's aggregate construction? —
and with it the membership-proof object shape (does a proof
carry siblings? positions? the whole digest list?). The text
routes "the construction's carriage" to the encoding round
(1475–1477). Membership-verification semantics are not
carriage: whether a forged sibling is refused, and what bytes a
membership proof needs, depend on the aggregate function, and
S3-3's must-affirm/must-refuse pair cannot even be fixtured
without choosing it. The confession as written labels a
semantic openness with a carriage word. Grade: MAJOR (GF-4) —
underdetermined; divergence is fail-loud between implementers
(head mismatch) but the confession is incomplete in scope-
naming, which is the round law's test for attacking confessed
openness.

**Mechanism (c): the availability floor (2769–2801, with
1259–1269 and 2227–2232).** Implementable from the text: read
the witness set and threshold fields of each stratum's
establishment events; compare against the chartered per-stratum
minimum threshold; an establishment event below floor is a
convictable governance event on the same KEL bytes. The
conviction path is fully derivable. One guess: the "set-
stability rule" names a clause slot without typing its
predicate language (churn bound? intersection minimum?) — the
domain's committed clause supplies the content, so the openness
is the ordinary law-side openness of every clause slot in this
document. Grade: MINOR (GF-10) — a one-sentence typing of what
a set-stability clause must commit (its comparator and its two
event coordinates) would close it; no silent divergence,
because the clause bytes themselves carry the rule.

### Battery 7 — over-generalization recheck (young prose)

Every inserted/repaired span from the census was re-read
against the mechanism-as-role test:
- The eight insertions (L1, A5a, B2, B7, E5, F4, G5, and the §19
  restorations) name their mechanisms: u-field, DI2I, KRAM,
  OOBI, Blake3-256/qb64, keripy@79e31cc8, watcher discrepancy
  report, key-state-notice comparison package, KERI delegation
  physics. No new generic-register site found in young prose.
- Residual generic phrasing in young prose: none found beyond
  the four grammar artifacts (GF-5). The G5 insertion's "the
  observation roles upstream" (2518) is a lawful role reference
  — the roles are named two sentences earlier.
- One young-prose site checked for overclaim rather than
  generality: B2's grade omits delegation state and BADA/
  first-seen grade relative to the original A19 enumeration —
  recorded at N6 (Part I) as the ruling's own scoping, NOTE
  (GF-11), for the station's vector work, not a defect of the
  repair against its ruling.

---

## Part III — supplement-3 vector obligations (spot-check tier)

Text-supports-discrimination checks only; the 42-7 station owes
the fixtures.

**S3-1 (edge slots fed to a signing-threshold evaluator without
per-slot standing appraisal).** REFUTABLE from the ruled
sentence alone: lines 1938–1944 commit that "an edge slot here
asks whether a credential stands, and that is this document's
own fold question — schema, issuer qualification, registry
state, disclosure state — never the substrate's." An
implementer treating an edge slot as a signature-presence test
contradicts the ruled span directly. SUPPORTED.

**S3-3 (membership-proof semantics).** Half-supported. The
must-affirm direction (valid clause + salt recomputes into the
anchored aggregate) is derivable from 1468–1471. The
must-refuse direction (forged sibling refuses) is derivable in
principle from "recomputes membership" — but WHAT recomputation
refuses a forged sibling depends on the unchosen aggregate
function (GF-4, battery 6b). The vector pair is statable
against the text but not fixturable from the text alone.
PARTIALLY SUPPORTED; blocked on the encoding-round choice, and
the text should confess that dependency as semantics, not
carriage.

**S3-4 (unseated warrantor fails credential verification, not
governance appraisal).** UNAMBIGUOUS: lines 1409–1420 — the
DI2I edge is "checked by edge validation in the existing
toolchain before any fold runs, and an unseated warrantor's
warranty fails credential verification. That check is evidence
the fold consumes, never a verdict: the two currents stay
unmerged." The failure mode's layer (credential verification)
is explicit. SUPPORTED.

**S3-5 (floor-violating establishment event convictable from
KEL bytes alone).** DERIVABLE: lines 2776–2783 — the floor
binds "the witness set and threshold an establishment event
carries — so that an establishment event whose new witness
state falls below the chartered floor is a convictable
governance event on the same KEL bytes, derivable by any
holder"; restated at 2227–2232 and 1259–1269. The
missing-receipt-indices pending vector is likewise derivable
from 1374–1377. SUPPORTED.

**S3-6 (delegated-gAID MAY grade and confessed cost).**
PRESENT: lines 2137–2149 — headed "(an OPTIONAL profile)",
verbed "MAY adopt", cost confessed in the same breath
(delegator-as-infrastructure; sole-authority extension to the
custodial quorum; two-identifier shadow re-run), and "Some
domains will rightly refuse the dependency." No reading as
mandatory survives the span. SUPPORTED.

**S3-7 (two typed evidence objects; acquisition openness
stated).** PRESENT: lines 2501–2519 — watcher discrepancy
report and key-state-notice comparison package "both
schema-typed evidence admissible in an evidence bundle like any
other," with the KSN package carrying the paired notices so
divergence is "recomputable from the package rather than
believed from the report"; judges/jurors constructor-plane,
determinations "replayable evidence ... never fold
replacements"; and "The acquisition procedure ... is expressly
confessed open, pending maturation of the observation roles
upstream." Openness stated, not implied. SUPPORTED.

---

## Findings register (severity-ordered)

- **GF-1 — BLOCKING.** N2/A5 unrepaired: the issuer
  non-observation "discharged by type" claim stands
  byte-identical at seed lines 805–810; no repair-census entry,
  no supplement-3 ruling, no kernel-side scoping, and the seed's
  §2.8 confession list does not confess the observation-surface
  gap (confession incomplete — the lawful-openness defense
  fails). Attack: Part I named-attack replay. Route: the seed's
  own regeneration station (graduated bytes; flagged, not
  edited), plus an optional kernel-side scoping repair at §7/§15
  through the ordinary census. As a named attack under S3-2's
  must-survive rule, one UNREPAIRED row blocks by construction.
- **GF-2 — MAJOR.** Line 2927 "six walls" vs the seven-wall
  enumeration this edition commits (2868, 2906, 304; delta
  entry 39). A carried span made defective by this edition's
  own change, exactly the collision-by-addition census's
  charter — and that census asserts "Zero carried spans
  retained defective; zero collisions unexamined" (3755–3756),
  which this span falsifies. Attack: battery 4 walls sweep +
  battery 3 census audit. One-word repair through the ordinary
  delta census; the census correction is append-grade.
- **GF-3 — MAJOR.** Bundle-preimage rule (3282–3286): the
  per-group primary-identifier enumeration covers two group
  shapes; other lawful CESR attachment-group classes leave the
  primary identifier implementer-chosen, so two conformant
  implementers can derive different bundle identifiers for one
  bundle (fail-loud divergence, not silent). Attack: battery 6
  fresh-implementer. Repair shape: total enumeration or a
  committed derivation rule per group class, plus a coverage
  obligation in gate three's vector families. Gate-one's
  unstood status bounds exposure — nothing lawful ships on the
  rule today.
- **GF-4 — MAJOR.** Aggregate-Constitution commitment
  (1461–1477): the aggregate function and membership-proof
  object are undetermined by the text, but the openness is
  confessed as "carriage ... chartered to the encoding round"
  — membership-verification semantics are not carriage, and
  S3-3's ruled must-affirm/must-refuse pair is unfixturable
  until the function is chosen. The confession is real but
  mislabels its scope (incomplete confession under the round's
  own confessed-openness law). Attack: battery 6
  fresh-implementer + Part III S3-3. Repair shape: one sentence
  naming the aggregate function as an open semantic commitment
  of the encoding round, or committing it.
- **GF-5 — MINOR.** Four grammar artifacts of the naming sweep:
  "the / KERI's" at 1558–1559, 1562–1563, 1661–1662, 3450–3451
  (article left behind by "the substrate's" → "KERI's"
  substitution). Attack: battery 1 register scan of young
  prose. Mechanical repair through the ordinary census.
- **GF-6 — MINOR (round artifact, not candidate text).** The
  repair report's sweep-audit line mispins the third lawful
  residual: "line 3529" is census meta-text; the definitional
  site minting "the substrate of record" is line 1007. The
  lawfulness claim holds at the correct site; the enumeration
  "three residuals" also undercounts lawful role-abstract
  sites (882, 1041, 1195, 2324, 2844, 2855 — each individually
  lawful under the §4 license or A-10 exemptions). No unlawful
  site found; the accounting, not the law, is off.
- **GF-7 — MINOR.** Blinding mandate (1447–1459) applies
  "ACDC's own discipline" by mandate to non-ACDC pre-committed
  object classes (GEL events, custodian rosters) where u-field
  placement and preimage inclusion are not derivable from the
  cited discipline; carriage round bounds exposure. Attack:
  Part I N3 residue probe.
- **GF-8 — MINOR.** §19's gate-one text asserts
  "verified from keripy ... at the pinned checkout 79e31cc8"
  (3264–3265) and "keripy's parser raises on unexpected count
  codes ... verified from keripy's primary bytes at the pinned
  checkout" (3426–3428) without citing the round artifact
  where the verification lives; the stated-evidence-scale duty
  (2725–2741) demands the scale be named, which it is, but not
  the record's address. Attack: battery 4 + register. A
  one-hop citation (per the naming duty, 2717–2723) closes it.
- **GF-9 — NOTE.** "the KERI specification's
  superseding-recovery section" (1291–1292) names a section of
  an external specification whose revision is pinned only via
  the engagement companion, which "this edition's ratification
  enactment SHALL pin" (1017–1019) — until that pin exists the
  named-section reference floats. Confessed shape (pin
  granularity confession at 2839–2843 covers the class);
  recorded for the ratification checklist.
- **GF-10 — NOTE.** The availability floor's "set-stability
  rule" (2777–2778) names a clause slot without typing its
  comparator; the domain's clause bytes carry the content, so
  no silent divergence. Attack: battery 6c.
- **GF-11 — NOTE.** The cone-root authentication grade's four
  components omit delegation state and BADA/first-seen grade
  relative to the original A19 enumeration — the ruling's own
  scoping (S3-5), recorded for the station's vector work.
- **SF-1 — flagged for the seed's own station (content finding,
  no edit proposed).** Seed §2.4 lines 632–638 carry the S3-3
  conflation ("A finding is disclosed *instead of* its
  evidence; a no-disclosure mandate is discharged by
  construction rather than by promise") that the ruling
  convicts ("the conflation is the defect"); the ruled
  three-presentation-form distinction exists kernel-side only.
  The integration heading's routing note names the aggregate
  half of S3-3 but not this residue half.
- **SF-2 — flagged for the seed's own station.** The GF-1/N2
  site itself (805–810): by-type discharge of the observation
  bar.
- **SF-3 — flagged for the seed's own station.** Seed §2.8's
  confession enumeration (828–844) is incomplete: it should
  carry the observation-surface openness (SF-2) once ruled.

## Verdict

**DEFECTS-FOUND.**

Severity order: GF-1 (BLOCKING); GF-2, GF-3, GF-4 (MAJOR);
GF-5, GF-6, GF-7, GF-8 (MINOR); GF-9, GF-10, GF-11 (NOTE);
seed-station flags SF-1–SF-3 (routed, not scored against the
kernel).

Scorecard: N1 REPAIRED (seed residue flagged) · N2 **UNREPAIRED**
· N3 REPAIRED · N4 REPAIRED · N5 REPAIRED · N6 REPAIRED ·
N7 REPAIRED · N8 REPAIRED · N9 REPAIRED.

**Disposition.** The repair pass held: eight of the nine named
attacks are repaired with byte-grounds, all 74 census entries
sampled or diff-mapped verify, the seed block is byte-identical,
every sacrosanct span and lineage pin checks, and the young
repair prose introduced no new generic-register site. What
blocks is narrow and precisely located: N2/A5 was never assigned
a ruling or a repair entry, and its site sits in graduated seed
bytes whose confession list does not cover it — the candidate
cannot claim survival of a named attack that no artifact ever
engaged. The lawful discharge path does not require reopening
the kernel: (1) rule the N2 repair and route it through the
seed's regeneration station together with SF-1/SF-3 (all three
land in the same seed sitting), with an optional one-sentence
kernel-side scoping at §7/§15 through the ordinary census;
(2) take the one-word GF-2 repair and the GF-5 grammar sweep
through the ordinary delta census with an appended collision-
census correction; (3) disposition GF-3/GF-4 either as repairs
now or as named openness — each needs only a sentence to
convert an implementer guess into a confessed open commitment.
With those dispositioned, nothing found by this gauntlet stands
between the candidate and FIT-FOR-FREEZE-LIFT; the freeze-lift
decision itself is the ratifying authority's.

---

Report complete. All three parts run: nine named attacks
scored; seven standing batteries run; six supplement-3 vectors
spot-checked. Subject digest at close re-verified:
a11f2902c6e18404ba22c9468681e8a92b57af01fe1de53b08dbabb2d5c786f0.
