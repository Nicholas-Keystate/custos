# Fable leg — over-generalization audit and integration survey
# Custos 4.2 candidate v1 (2026-08-03)

Reviewer: fresh-context adversarial leg (Fable), one of two parallel
independent legs. Inputs: review-brief.md; weave/custos-4.2-candidate-v1.md;
staged-repos/custos/spec/custos-4.1.md (comparison); weave/42-compact-form-gates.md;
keripy @ 79e31cc8 (read-only); specs/tswg-acdc-specification (read-only).

## Input-integrity note (report before findings)

The brief pins the candidate at sha256 c62c1dde…; the on-disk file
hashes 8b4f701a4446c4e3899f0f6ed113ce480153c03f541e22b0e773a67bc27c6c8d.
I did not re-pin blind: I re-ran the committed assembly engine
(ops/held/42-assemble-engine.py (held copy), output redirected to staging) and reproduced the
pinned bytes exactly (digest match), then diffed staging against disk.
The entire delta is one line — line 21, "Key state infrastructure ends"
→ "KERI ends" — a post-acceptance direct-naming edit, in exactly the
register this round exists to enforce (presumably the ratifying
authority's own hand; matches the catch class that ordered this round).
Findings below are against the on-disk bytes (8b4f701a…); line numbers
are identical in both states except line 21. Staging file deleted after
use. The orchestrator should attribute the edit and update the round's
pin of record.

Baseline counts that frame everything below (on-disk bytes, 3,596
lines): "CESR" appears exactly once (line 992). "ACDC" six times (four
of them in the byte-frozen Chapter 2 seed and §9). "keripy" once (997).
"substrate" ~70 times; "the medium" ~25 times. OOBI, BADA, KRAM,
witness thresholds, watcher roles, key-state notices: zero by name.

---

## PART A — site audit

### A-1. BLOCKING — §4 "The substrate of record" is the license for every other site, and its promise is inverted. Lines 991–1004.

The one naming block names KERI/ACDC/CESR correctly, then rules:
"within this document the substrate is cited by name and never
restated." The document then does the opposite: after line 997 the
names essentially vanish and "the substrate" / "the medium" / "the
encoding layer" / "the credential layer" become the working names —
CESR is never written again in 2,600 subsequent lines that specify a
CESR wire form. Classification: FALSE GENERALITY at the charter grain —
this clause is where the generic register is laundered into apparent
lawfulness. Repair is one sentence plus a sweep: rule that the
substrate components are cited by their proper names (KERI, ACDC,
CESR, and the named mechanism) at every load-bearing use, reserving
"the substrate"/"the medium" for the genuinely role-abstract sites
(A-13 below lists which those are). The banked register law (direct
naming; "KERI" never "the substrate" in reader-first text) already
rules this; the candidate text predates the enforcement.

### A-2. BLOCKING — "The encoding substrate's genus namespace" (§18 Genus). Lines 3019–3029.

The authority's own catch, confirmed and sharpened: genus namespaces
are not a property of encoding layers in general — they are CESR's
specific architecture (GenusCodex, keripy counting.py:41; the
genus-version grammar of the CESR spec's count-code tables; the
`-_AAA`-style genus codes). An implementer told "the encoding
substrate's genus namespace admits reservation" cannot locate the
mechanism, the reservation grammar, or the stewards to address.
FALSE GENERALITY: the whole paragraph's design (reservation as
enactment; recognition by "the substrate's stewards" as later
bilateral event) is meaningless except against CESR's actual
genus/count-code tables and the ToIP working group that stewards
them. Repair: name CESR, name the genus table, cite the count-code
section of the CESR specification.

### A-3. BLOCKING — Section 19's bundle rule genericized its own committed input into under-specification. Lines 3103–3116, 3248–3261.

The gates document (42-compact-form-gates.md, a named input to the
assembly) states the rule concretely: "the Blake3-256 SAID, qb64, of
the canonical bundle preimage… the groups ordered lexicographically
over the qb64 of each group's primary identifier (for an
indexed-signature group, the signer's prefix; for a couple, the
coupled identifier…)". The candidate abstracted this in transit to
"the self-addressing digest, in the substrate's encoding… ordered
lexicographically over the encoded form of each group's primary
identifier" — and DROPPED the per-group-type definition of "primary
identifier" entirely. Two consequences, both implementer-misleading:
(1) "the encoded form" no longer pins qb64 vs qb2 — the two CESR
domains give different byte orders under lexicographic comparison,
so two conforming implementers can derive different bundle
identifiers from one bundle; (2) with "primary identifier" undefined
per group type, the between-group order is not derivable from the
document at all. This is a canonical-preimage rule — exactness is its
entire office; the genericization re-opened the identity drift gate
one exists to close. Same defect class at 3092–3094 ("verified from
the substrate's reference implementation at the pinned checkout" —
which implementation? which checkout? keripy serdering.py:393
rct FieldDom, no saids entry — checkable in one hop if named) and
3251–3252 (the raise-not-skip fact, keripy parsing.py:1251/1298,
cited namelessly). Repair: restore the gates document's specificity —
Blake3-256, qb64, the per-group primary-identifier enumeration, keripy
at 79e31cc8 by name.

### A-4. MAJOR — The pin rule's dummy convention is CESR mechanics written namelessly. Lines 965–980.

"the number sign, the substrate's own dummy convention — under the
substrate's length-parametric rule by derivation code, of which
forty-four characters, the 256-bit digest class" — this is the CESR
SAID derivation exactly (keripy coring.py saidify: 44 '#' dummy
chars, qb64 Blake3-256, one-char derivation code 'E'). A reader
outside the family cannot recompute a self-addressing pin from this
text: "forty-four characters" is only derivable if you already know
qb64 and the CESR code table. FALSE GENERALITY on a rule whose whole
purpose is that strangers recompute it. Name CESR and the derivation
code table.

### A-5. MAJOR — "The substrate's superseding-recovery rules/calculus" is load-bearing at four sites and never named or located. Lines 1259–1264, 1431–1433, 1471–1479, 2682–2684.

The medium's conviction predicate is stated "modulo those rules"
(1262–1264); the window-open pending species' CURE is decided by
them (1471–1479: non-delegated fossilization at next rotation,
delegated windows staying open); §15 even obligates domains to pin
them "rule by rule, each consumed or expressly excluded" (2682–2684).
So the fold's decidability at the key tier hangs on a rule set the
document never names (KERI's superseding recovery — the KERI
specification's superseding-recovery section; keripy eventing
acceptance logic) and never states even in summary. An implementer
cannot compute when window-open cures without independently knowing
which KERI rules are meant. FALSE GENERALITY: the design depends on
KERI's specific recovery table; the prose claims a portability
("the substrate's own recovery calculus is the decision procedure")
the design does not have. Repair: name the mechanism and its spec
section at first use; the §15 functional-dependency clause then has a
referent.

### A-6. MAJOR — Two "citations" that name nothing: request authentication and out-of-band introduction. Lines 2653–2666.

"the substrate's own request-authentication mechanism is the design
of record for it, cited, not restated" — the mechanism is KRAM
(KERI Request Authentication Mechanism, keripy kraming.py: monotonic
timed cache, replay-attack and clock-retrograde protection — exactly
the "replay-attack taxonomy and cache-window discipline" the sentence
gestures at). "the substrate's out-of-band introduction machinery" —
OOBI. Neither name appears. By the candidate's own rule (line
979–980: "A digest whose preimage is not stated is not a pin; it is
decoration"), a citation that names no citable artifact is
decoration. These are the document's own best evidence that generic
prose hides real machinery: KRAM's wall-clock window is precisely the
"transport admission MAY be wall-clock-windowed" boundary the
paragraph draws — naming it would let the boundary cite KRAM's
actual cache-window semantics instead of restating them vaguely.

### A-7. MAJOR — The warranty is an ACDC and the blinding factor is the ACDC UUID field; neither is named. Lines 1360–1370, 1386–1396.

"A warranty SHALL be a schema-typed, registry-bound attestation in
the substrate's credential discipline — typed by schema identifier,
revocable through its registry, its lens cited by edge" — every
clause of this is ACDC-specific (SAID-addressed schema, TEL registry
vcp/iss/rev, edge section), and "the substrate's credential
discipline" is the only name given. Worse at 1388–1389: "a
substrate-grade blinding factor, in the credential layer's own
salt-field discipline — cited, not reinvented." No spec calls it a
"salt-field discipline"; the mechanism is ACDC's UUID `u` field
(tswg-acdc spec-body.md ~line 164: high-entropy `u` field defeats
rainbow-table discovery of a committed SAID's preimage). A reader
sent to find "salt-field discipline" in the ACDC spec will not find
those words. The citation form defeats its own checkability. Name
ACDC; name the `u` field.

### A-8. MAJOR — The covenant seal's carriage names "the substrate's own generic typed seal" but not the actual structure. Lines 1904–1934.

The carriage is KERI's SealKind (t, d) — keripy structing.py SealKind
namedtuple — traveling under the TypedDigestSealCouples count code
('-W', counting.py:255). Naming it does two things the generic prose
cannot: makes "a governance-blind consumer parses the seal unharmed"
checkable against the actual parser, and exposes a real coordination
surface — the reserved `t` value lives in a type namespace someone
stewards, which is the same recognition question as the genus
reservation (A-2) and should be stated beside it, not hidden.

### A-9. MAJOR — Chapter 2's disclosure postures cite ACDC's lineage but not its machinery, leaving the edition's new axis without a mechanism. Lines 569–580, 591–615 (seed; repairs route to the seed's own station, not in-place edit).

The chapter does name ACDC once, correctly, at lineage grade
(569–571: "ACDC's graduated disclosure and chain-link confidentiality
(Smith) already deliver commit-then-disclose at the credential tier")
— and then delivers the lift ("the same discipline one tier up") as
prose only. The admitted posture (591–601) specifies WHO may read
but no disclosure mechanism; the clause-selective posture (603–615)
says "reveal what the ground names and nothing else" with no way for
the verifier to check that a revealed clause is a member of the
anchored Constitution without seeing the rest. Both problems are
solved machinery in the cited lineage — see B-1. Classification:
MISSED INTEGRATION, the round's central class. (Because the chapter
is a byte-frozen graduated seed, the repair enters through the seed's
regeneration station or a 4.2-gauntlet finding, never an in-place
edit — flagged so the orchestrator routes it.)

### A-10. NOTE — Sites where the generic register is TRUE generality; keep, with grounds.

- Lines 1247–1283 (the medium's two properties: frame-invariant
  authentication; no ranking of frames) — genuinely holds for any
  conformant KERI-class substrate; the abstraction is the point.
  Keep "the medium" here; it is the document's one earned abstraction.
- Lines 1069–1090 (three logs) and 1092–1107 (three folds) — model
  sites: substrate vocabulary cited by name (KEL, TEL, Kever, Tever,
  "the reference implementation's class name, adopted"), extension
  marked. This is what every other site should look like.
- Lines 1838–1862 (§9 composed evidence) — names the ACDC edge
  grammar, the dossier threshold operators, and the one-algebra
  observation (weighted-threshold satisfaction = keripy Tholder at
  both ends). Second model site.
- Lines 2207–2216 (group-identifier alternative disposed of on the
  record) — a specific KERI mechanism (multisig group AID) engaged
  specifically and rejected with grounds. This is the correct form
  for a considered-and-declined integration.
- Lines 2934–2939 (track one, registry-form reuse under existing
  ilks) — correctly generic-by-design: the colorless base is the
  claim.

### A-11. NOTE — "Key state infrastructure" (pre-edit line 21) and residual abstract-register kin.

The accepted bytes' abstract opened "KERI detects; a GARD
adjudicates. Key state infrastructure ends at a deliberately drawn
line" — the euphemism in the sentence that exists to name KERI. The
on-disk edit ("KERI ends") already repairs it; recorded here so the
census carries the site and the collator checks for kin (grep found
no other "key state infrastructure"; "the protocol layer this
document builds on" at 991 is the definition site and lawful).

### A-12. NOTE — Chapter 2 seed's "substrate" sites. Lines 526, 673–684, 717–741.

"substrate mechanics only," "the substrate class's interpretive
law," "the colorless substrate object," "grounded in the medium" —
inside the seed these are layer-role uses under Chapter 1's binding
definitions and mostly lawful under the directness ruling
(layer-role uses stay lawful once a binding block defines them). But
the binding block (§4, line 991) sits AFTER the seed in reading
order, so a linear reader meets ~15 "substrate" uses before the word
is bound. Worth one repair at the Chapter 2 integration heading or an
earlier binding sentence; not worth reopening the seed.

### A-13. NOTE — The scale of the sweep, quantified for the repair program.

Sites where "the substrate('s)" should become a proper name or a
named mechanism, by section: §4 pin rule (2 sites), §5 definitions
(6), §6 medium (4 — keep "the medium" itself per A-10), §7 objects
(4), §8 codomain (5), §9–§10 seals (5), §11 rotation (7), §12
classes (9), §13 (4), §15 (6), §16 (2), §18 (6), §19 (12). Roughly
70 total; my read is ~50 convert to names (KERI / CESR / ACDC / the
named mechanism), ~20 are lawful layer-role abstraction. The naming
sweep is mechanical once A-1's rule is adopted; the missed
integrations (Part B) are the substantive work.

---

## PART B — innovation survey, ranked by leverage

The archetype for this class: CESR genus reservation → a
governance-native wire form (section 19). Each entry names the
mechanism with its checkable surface, the Custos surface it serves,
and what the integration enables that the current design cannot do.

### B-1. ACDC selective disclosure + chain-link confidentiality → the disclosure postures get their machinery. LEVERAGE: HIGHEST.

Mechanism (tswg-acdc spec-body.md): (a) selective disclosure — the
aggregate `A` field is a digest of the concatenation of SAIDs of
blinded (per-block `u`-salted) attribute sub-blocks, so one committed
top-level digest admits per-block disclosure WITH proof of membership
and zero leakage of siblings (~lines 110, 164, 680); (b) chain-link
confidentiality — offer/accept against a metadata ACDC (empty `u`)
whose rules section carries terms of use, full disclosure only after
committed acceptance (~lines 168–172, 256); (c) contractually
protected disclosure generally.

Custos surface: Chapter 2's clause-selective and admitted postures
(A-9).

The integration: structure the committed Constitution (or its
clause-set head) as an aggregate over per-clause blinded sub-blocks —
each clause SAID-addressed (already ratified, line 1163–1166) plus a
per-clause blinding factor (the §7 blinding mandate at 1386–1396
already REQUIRES this for pre-disclosure commitments — the two
clauses compose and nobody has noticed). Then clause-selective
disclosure is literally ACDC selective disclosure one tier up: reveal
the ground-cited clauses + their salts; the verifier recomputes
membership in the anchored aggregate; the remainder stays blind AND
provably present. This closes the gap the chapter currently bridges
with prose ("reveal what the ground names" — but against what
commitment?). For the admitted posture, admission enactments grant
disclosure under a chain-link exchange: the law travels as a
contractually protected disclosure whose rules section carries the
admission terms, so unpermissioned re-disclosure by an admitted
party becomes breach with committed evidence — which materially
softens the narrowed-jury confession (655–668): the jury is narrow,
but leaks out of it are convictable. Cannot be done against a
generic "credential layer"; it is Sam's exact machinery, and the
chapter's own lineage paragraph promises the lift without delivering
it.

### B-2. CESR native field maps + canonical order → discharge the byte-identity forward commitment. LEVERAGE: HIGH (routed to the chartered encoding round).

Mechanism: CESR-native serialization kind — fixed field order, typed
primitives, no JSON serialization freedom (CESR spec, native message
serialization; keripy Serder kinds). The conformance predicate is
semantic-only today explicitly because "a carriage encoding removes
the last serialization freedom" (2855–2858); the candidate never
says that the substrate family already ships the encoding with that
property. Custos surface: the one conformance predicate (§17), the
GEL event grammar (§18 — track-two events in CESR-native form get
canonical order BY CONSTRUCTION, collapsing part of wall 6's site
rules into physics). What it enables: byte-identity stops being a
forward commitment and becomes a selection among existing substrate
serializations. Routing honesty: the carriage encoding is chartered
to the group design round and expressly non-gating (2765–2770); this
entry is INPUT to that charter naming the family-native candidate,
not a repair to this edition.

### B-3. ACDC edge operators (I2I / NI2I / DI2I) → warranty-to-seat chains checked by the substrate toolchain. LEVERAGE: HIGH.

Mechanism: edge operators (tswg-acdc spec-body.md 1192–1207): I2I
requires this ACDC's issuer to be the pointed-to node's issuee; DI2I
admits a DELEGATED AID of the issuee. Custos surface: the warranty
object (1360–1370) and seats (2028–2038). The candidate already
rules warranties are edge-citing credentials and seated organs
SHOULD be delegated identifiers of the gAID — but never connects
them. The integration: a warranty's edge to the warrantor's seat
credential carries DI2I — then "the warrantor holds the seat it
claims" is checked by ACDC edge validation in the existing
toolchain, before any Gever runs; an unseated warrantor's warranty
fails credential verification, not just governance appraisal. DI2I
exists for exactly the delegated-organ shape the candidate chose;
the generic register ("its lens cited by edge") hid that the edge
grammar carries typed CONSTRAINTS, not just references. Enables:
standing-chain pre-checks with zero new machinery; the composed
§9/§11 design becomes executable today.

### B-4. KERI witness configuration (wits/toad in establishment events) → the availability charter becomes a computed obligation. LEVERAGE: HIGH.

Mechanism: witness designation and threshold are COMMITTED KEY
STATE — `b`/`bt` at inception, `ba`/`br` cuts-and-adds at rotation
(KERI spec witness sections; keripy eventing Kever); witness
receipts are couples with committed cadence possibilities. Custos
surface: the availability charter (1236–1244, 2630–2651) and the
obligated-attestation partition (2117–2126). Today the charter is a
separate committed obligation whose discharge is prose ("each
stratum's witnesses discharge it"). The integration: charter clauses
bind the ALREADY-COMMITTED witness fields — a charter commits per
stratum a minimum toad and a witness-set stability rule; then "a
stratum that sheds its availability obligation sheds its delegated
standing" (2637–2639) stops being a sentence and becomes a fold
predicate: a rotation whose new toad/wits fall below the chartered
floor is a convictable governance event on the same bytes — the §11
two-layer joint pointed at witness state, a governed object class
the §12 criterion already admits (witness config has lifecycle,
authenticates through key state, has positions). Enables: charter
breach detectable by any stranger holding the KEL, no audit organ
required.

### B-5. Superseding recovery consumed by name, and the recovery window as a first-class governed object. LEVERAGE: MEDIUM-HIGH.

Complement to A-5: beyond naming, there is an unused design move.
The candidate's window-open species and §11's contest windows both
lean on KERI's recovery windows; KERI's delegated recovery
(dip/drt: delegator approval required, windows open longer) means a
domain can CHOOSE its recovery-window shape by choosing delegation
depth — the candidate says this for organs (2028–2038) but not for
the gAID itself: a born-governed domain whose gAID is itself a
delegated identifier of a custodial quorum gets constitutional
recovery windows enforced by substrate physics rather than by
committed policy the fold appraises after the fact. That is the
§11 "what defeats it" axis partially discharged by the medium —
the same claim the candidate makes for organs, one level up, unmade.
Sketch: one paragraph in §11 stating the gAID-as-delegated-identifier
construction and its confessed cost (the delegator becomes
infrastructure the domain's autonomy must account for).

### B-6. CESR streams as the verification cone's native carriage. LEVERAGE: MEDIUM.

Mechanism: CESR is a streaming protocol — count-code-framed groups,
pipelining, cold-start stream parsing (CESR spec framing/ops
sections); a KEL/TEL replay IS a CESR stream in the reference
implementation. Custos surface: the verification cone (1300–1336),
whose carriage is currently the dossier (document envelope) with
"the substrate's native composable attachment grammar" named as the
default posture for the future encoding (2766–2767). The
integration: specify the cone's log spans as canonically ordered
CESR stream segments under a bundle-rule-style composition
identifier (section 19's own construction, one grain up). Enables:
cone presentation-independence and tamper-totality by the same
machinery as compact receipts, and a cone that any vanilla parser
can consume span-by-span (the anchors voice of the transport
stratum, applied to cones). Also gives "completeness is decidable by
the replay itself" (1323) a wire-level counterpart. Routed with B-2
to the encoding round.

### B-7. Duplicity proof packages typed as CESR event pairs. LEVERAGE: MEDIUM.

Mechanism: key-tier duplicity is concretely two verifiable
CESR-framed events at one (i, s) — the medium's crime has an exact
wire shape, and keripy's first-seen/duplicity machinery consumes
it. Custos surface: self-convicted's "canonical proof package
identifying the contradictory pair" (1428–1431, 1555–1556) — never
given a shape. The integration: type the key-tier proof package as
the pair of framed signed events plus their receipt sets; registry-
and governance-tier packages then extend the same shape (pair of
anchored events + the committed predicate cited). Enables: proof
packages that any KERI-native consumer can verify mechanically at
the key tier before any governance machinery engages, and a
concrete fixture family for the 42-7 station. The generic "canonical
proof package" hid that the base tier already has a native format.

### B-8. BADA/RUN and key-state notices → freshness discipline for warranted consumption. LEVERAGE: MEDIUM-LOW.

Mechanism: BADA (Best Available Data Acceptance; keripy
routing.py:175ff) — monotonic acceptance for signed, non-KEL
assertions keyed on key state and datetime; KSN (key-state notice
rpy) rides it. Custos surface: warranted consumption (2303–2318) and
the transport-time boundary (2660–2664). A warranty is exactly the
object class BADA governs: a signed latest-view assertion outside
any log the consumer folds. Unaddressed today: at which key state a
warranty's signature verifies when the warrantor rotates between
emission and consumption — registry binding (issuance anchoring)
covers issuance-time, but presentation-cache behavior is the BADA
question, and naming BADA imports its answer (including retrograde-
clock protection) instead of leaving the cache discipline to the
deployment lane unnamed. One sentence plus a citation.

### B-9. ACDC bulk issuance → unlinkable warranties and presentations. LEVERAGE: LOW (companion-grade).

Mechanism: bulk-issued private ACDCs (spec-body.md bulk-issuance
section: one issuance commitment, many uncorrelatable instances,
nested `rd` for contractually protected registry disclosure). Custos
surface: Chapter 2's presentation-unlinkability posture (the §2.0
mandate class bars issuers from watching use). A warrantor or
endorser issuing bulk-blinded instances lets a holder present to N
consumers without cross-consumer correlation — the statutory
no-phone-home property extended from the issuer to the warrantor
tier. Companion/SEDI material, not kernel text; recorded so the
survey is honest about the mechanism's existence.

---

## The pattern, stated once

Every BLOCKING and most MAJORs share one mechanism: the candidate
writes the ROLE where its own design consumed the MECHANISM. Where
the document engaged a mechanism by name (three logs, edge-operator
algebra, the group-identifier rejection), the engagement is specific,
checkable, and in two cases generative; where it wrote "the
substrate's own X," the specificity that produced the design decayed
in transit (A-3 is the proof case: the committed input named
Blake3/qb64/per-group identifiers and the candidate un-named them,
re-opening the drift its gate closes). The missed integrations
cluster where the generic word sits: "credential layer" hid the
u-field, the edge operators, and selective disclosure (B-1, B-3);
"encoding layer" hid native field maps and streams (B-2, B-6);
"the substrate's machinery" hid wits/toad, KRAM, BADA, and the
recovery calculus (B-4, B-5, B-8, A-5, A-6). The repair program is
therefore two-track exactly as the brief suspects: a mechanical
naming sweep (A-1's rule, ~50 sites per A-13), and adoption
decisions on B-1 through B-5, of which B-1 is the one that
strengthens this edition's own new axis rather than its inheritance.

— end of leg findings —
