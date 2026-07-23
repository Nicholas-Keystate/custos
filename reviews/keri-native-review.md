# KERI-native review — Custos 4.0 kernel, assembled draft v1
# Round: reviews/rounds/40-drafting-2026-07-22/
# Reviewer: substrate-native leg (third leg; firewalled from
#   sol-kernel-review.md, fable-kernel-review.md, and all
#   k40-*-response* files — none read)
# Subject: custos-4.0-kernel-draft.md
#   (sha256 e5cef68cc0f736540d73e454c11ed96494fac0e801ef2d93475d8f3d4130ec0b)
# Date: 2026-07-22
#
# Corpus paths abbreviated throughout:
#   KERI  = trustoverip/tswg-keri-specification, spec/spec-body.md (main)
#   ACDC  = trustoverip/tswg-acdc-specification, spec/spec-body.md (main)
#   CESR  = trustoverip/tswg-cesr-specification, spec/spec-body.md (main)
#   KRAM  = SmithSamuelM/Papers, whitepapers/kram.md
#   SPAC  = SmithSamuelM/Papers, whitepapers/SPAC_Message.md
#   IPEX  = SmithSamuelM/Papers, whitepapers/ACDC_IPEX_Negotiation.md
#   DOSS  = ToIP dossier specification (cite the canonical ToIP source)
#   keripy = WebOfTrust/keripy (pinned @ 79e31cc8)
# Kernel cites are section + draft line number (draft:NNN).

## 1. Verdict

**SOUND-WITH-FINDINGS.** The kernel's seam architecture — evidence
crosses, judgment never does; substrate cited, never restated;
openness confessed — is genuinely substrate-respecting and in
several places better-mannered toward the substrate than most work
this community receives; but the draft misstates the substrate's
reconciliation machinery at its foundation (the opening claim, the
medium's conviction rule, and the window-cure rule all
over-generalize past superseding recovery), elevates reference-
implementation vocabulary into protocol law, and leaves the
request-authentication (KRAM) and disclosure-posture (SPAC)
obligations of its own outward face unstated.

No BLOCKING findings. Seven MAJOR, six MINOR, two OBSERVATION.

---

## 2. N1 — Substrate fidelity findings

### KN-01 · MAJOR · The opening overstates the substrate's silence

Kernel cite: §1, "KERI makes duplicity evident and remains silent
about recourse. When a validator detects two conflicting key
events from one authority, the protocol's remedy is private: the
validator decides whether to cease trusting said authority, and
further recourse is left to the rest of the network to decide"
(draft:15-19).

Substrate cite: KERI:53 — "An honest validator MUST trust when
there is no evidence of duplicity and MUST NOT trust when there is
any evidence of duplicity unless and until the duplicity has been
reconciled. KERI provides mechanisms for duplicity reconciliation.
These include key compromise recovery mechanisms." Also
KERI:1784-1827 (Superseding Recovery and Reconciliation, a fully
normative recourse mechanism at the key layer) and KERI:51-53
(Juror/Jury/Judge machinery for duplicity evidence evaluation).

The spec bytes contradict the framing on two points. First, the
validator's response is not discretionary: the spec legislates it
with a MUST/MUST NOT pair. Second, the protocol is not silent
about recourse at its own tier: superseding recovery is committed,
rule-enumerated recourse for key compromise (KERI:1802-1823), and
reconciliation is a named, provided-for process. What the
substrate is genuinely silent about is *governance consequence
beyond key-state trust decisions* — which is the kernel's actual
subject and a stronger, truer premise. The current wording hands a
KERI spec author a refutation in the document's first paragraph.
Repair: re-ground §1 on KERI:53's own words; claim the silence
that is actually there.

### KN-02 · MAJOR · The medium's conviction rule ignores superseding recovery

Kernel cite: §4, "two committed voices at one coordinate convict
their author in every frame at once, under no frame's law"
(draft:298-300); repeated at §10.4, "at one committed coordinate —
is convictable by anyone holding both logs" (draft:933-936).

Substrate cite: KERI:1799 ("after an event has already been
accepted as first seen into a KEL, a different event at the same
location (same sequence number) is accepted that supersedes that
pre-existing event"); KERI:1806 (rule A0: a rotation MAY supersede
an interaction at the same sn); KERI:1856 ("The exception to this
general rule is that a rotation event may provide a superseding
recovery"); KERI:53 ("unless and until the duplicity has been
reconciled").

The substrate lawfully admits a second verifiable event at one
coordinate: superseding recovery. A rotation superseding a
compromised interaction is reconciliation, not conviction — the
spec's whole recovery design depends on the pair NOT poisoning the
author. The kernel's medium section states unconditional
conviction; its own §6.2 window-open species shows the drafters
know recovery windows exist, but the medium's conviction relation
is never scoped by the substrate's reconciliation rules. As
written, the kernel's tier-1 self-conviction predicate and the
substrate's superseding rules disagree on the same bytes. Repair:
the medium's conviction predicate must be stated modulo
KERI:1802-1823 — a same-location pair convicts only where no
superseding rule reconciles it — and the tier-1 instantiation of
self-convicted (§6.1, draft:390-394) must cite those rules as the
committed decision procedure for whether a pair bears.

### KN-03 · MAJOR · Kever/Tever are implementation names, not substrate names

Kernel cite: §3, "The substrate names its folds after the logs
they fold" (draft:190-191); "**Kever** — folds a KEL to current
key state. Substrate-native. **Tever** — folds a TEL to current
registry state. Substrate-native." (draft:194-196).

Substrate cite: the strings "Kever" and "Tever" appear zero times
in KERI, ACDC, or CESR spec bodies (content search over all three,
2026-07-22, 0 matches). They are keripy class names:
keripy/src/keri/core/eventing.py:1812 (`class Kever:`) and
keripy/src/keri/vdr/eventing.py:650 (`class Tever:`).

The specifications name no folds; the *reference implementation*
does. Presenting Kever/Tever as "substrate-native" and the naming
grammar as "the substrate's own" is precisely the
over-generalization of implementation behavior into protocol law
this review lane exists to catch — and it matters doubly here
because the kernel mints "Gever" as the third rung of that
grammar. The extension is fine; the attribution is wrong. Repair:
attribute the fold-naming grammar to the reference implementation
at its pinned checkout (cite the two class paths), keep
"substrate-native" for KEL/TEL only, and mark Gever as an
extension of an implementation convention, not of the
specifications.

### KN-04 · MAJOR · The window-cure rule over-generalizes the non-delegated superseding rules

Kernel cite: §6.2, "**window-open** is cured by the closing of the
committed window (the next establishment event fossilizes the
suffix — recovery windows are typed by this species, not by a new
value)" (draft:421-424).

Substrate cite: KERI:1806-1808 (non-delegated: a rotation may
supersede an interaction; a non-delegated rotation may NOT
supersede another rotation — so for non-delegated KELs the next
rotation does fossilize the prior suffix); but KERI:1813-1819
(rules B1-B3: a delegated rotation MAY supersede the latest-seen
delegated rotation) and KERI:1825 ("recovery can not happen for
any compromise of pre-rotated keys, only the latest-seen" —
i.e. the window on a delegated establishment event stays open
until a *subsequent non-superseding* rotation lands, not until the
next establishment event as such).

"The next establishment event fossilizes the suffix" is true only
for non-delegated KELs. The kernel's own organs live in
"delegation strata" (§3 draft:280-284; §12 draft:1140-1149), which
is exactly the regime where the claim fails: a delegated rotation
is itself supersedable under B1-B3. Repair: type the window-close
condition per KEL class — non-delegated: next rotation
(KERI:1806-1808); delegated: next non-superseding rotation
accepted under B/C recursion (KERI:1813-1825) — or state the cure
as "the substrate's superseding rules no longer admit a
superseding event at the position," which is class-neutral and
cites one place.

### KN-05 · MAJOR · The duplicity ladder borrows the medium's conviction force for frame-local crimes

Kernel cite: §3, "**Duplicity** (substrate term, extended by
tier)" (draft:271-278); §6.4, "At the registry tier, it is two
registries where committed law demands one chain … At the
governance tier, it is contradictory enactments under one
committed predicate" (draft:536-541).

Substrate cite: KERI:1744 — "A duplicitous event is defined as a
verified but different version of an event at the same location."

The spec's duplicity is location-relative and law-free: it
convicts in the medium, for every observer, with no committed
covenant anywhere in the predicate — which is exactly the property
the kernel's own §4 celebrates. The tier-2 and tier-3 extensions
are *law-relative*: "where committed law demands one chain,"
"under one committed predicate." A frame that never adopted the
covenant computes no crime from the same bytes. Reusing the word
"duplicity" for both erases the frame-invariant/frame-local
boundary the kernel elsewhere enforces as its central discipline
(§10, draft:793-803). The extension is marked, which is honest;
but the marking does not state the force downgrade. Repair: one
normative sentence in §6.4 — tier-1 duplicity convicts in the
medium; tier-2/tier-3 "duplicity" convicts only within frames that
committed the violated predicate, and travels to other frames as
evidence, never as conviction. (This is the kernel's own
transformation law applied to its own vocabulary.)

### KN-06 · MINOR · "The substrate ships the first two" undercounts the substrate's seal grammar

Kernel cite: §3, "named in the substrate's own seal grammar (the
substrate ships the first two; the third is this standard's
extension)" (draft:252-254); §8, "the first two are the
substrate's own, cited" (draft:673-675).

Substrate cite: KERI:405-422 (seal count-code table: digest,
Merkle-root, source-couple, source-triple, last-establishment,
backer-registrar, typed — seven kinds); KERI:424 (digest seal);
KERI:448-469 (source event and key event seals); KERI:480-484
(latest establishment event seal); KERI:511-518 (typed seal).

The substrate ships seven seal kinds, not two. The kernel's
digest/event dichotomy absorbs most of them, but not all: the
latest-establishment-event seal (KERI:480) commits to *current key
state of an AID*, not to bytes and not to a coordinate — it
answers a third question the kernel's ladder has no rung for, and
one a governance layer plausibly wants (an edict endorsing a seat
holder's key state as-of-now). Repair: cite the full table, state
which substrate kinds the kernel's two categories subsume, and
either admit or expressly exclude the latest-establishment kind.
See also KN-14 (the typed seal as the covenant seal's carrier).

### KN-07 · MINOR · The threshold-operator grammar is a dossier-spec profile, not ACDC-native

Kernel cite: §7, "it MAY be expressed in the substrate's native
edge-operator grammar: ACDC edge groups whose operator field
carries a weighted threshold over slotted references, each slot
naming the schema its evidence must satisfy (the ACDC operator
conventions, as profiled in the dossier specification; cited, not
restated)" (draft:631-636); "the operator grammar is the
substrate's own way of committing it" (draft:639-640).

Substrate cite: ACDC:1101-1110 — the native m-ary operator set is
`AND`, `OR`, `NAND`, `NOR`, `AVG`, `WAVG`; no threshold-to-unity
operator exists in the ACDC spec. The `MxN`/`RMxN`/`MxQ`/`RMxQ`
threshold operators and the slot/weight/unity mechanics are
constructions of the dossier spec (DOSS:353, DOSS:358-362,
DOSS:371-374), described there as "following ACDC operator
conventions."

The kernel's parenthetical does say "as profiled in the dossier
specification," which saves it from misstatement — but "the
substrate's native edge-operator grammar" and "the substrate's own
way" promote a ToIP extension profile to substrate status in the
same sentence. The threshold-algebra unification claim itself is
well grounded (DOSS:353: "This is the same fractionally weighted
threshold KERI uses for key-event…"). Repair: say "the ACDC edge
grammar as profiled by the dossier specification's threshold
operators" and drop "native" for the threshold part.

### KN-08 · MINOR · The 44-character pin rule hardcodes one digest class against the kernel's own migration clause

Kernel cite: §2 rule 2, "computed with the digest's own field
carrying a placeholder of forty-four '#' characters"
(draft:127-133).

Substrate cite: CESR:1197-1199 — the dummy is "a dummy string of
the same length" as the final encoded SAID, algorithm given by the
SAID's own derivation code; CESR:1265 ties 44 characters to the
Blake3-256 case specifically.

CESR's rule is length-parametric by derivation code; 44 is the
256-bit digest class profile, not the rule. The kernel's own §9
commits to cryptographic migration by committed schedule
(draft:777-780) — a suite migration to a larger digest class
changes the placeholder length and would falsify reading rule 2 as
written. Repair: state the CESR rule (same length as the derived
SAID, per its code) and note 44 as this document's current
profile.

### KN-09 · OBSERVATION · Witness/watcher vocabulary is used at spec grain — praise

Kernel §3/§12 use "witness" strictly as the controller-designated,
KEL-managed availability/receipt mechanism and refuse to enumerate
observers. This matches the spec bytes exactly: witnesses are
controller-chosen and KEL-managed (KERI:43), watchers are
validator-controlled, deliberately not KEL-managed, and kept
confidential precisely so attackers cannot enumerate them
(KERI:45); ambient verifiability is the unenumerated-population
property (KERI:1882-1884). The availability charter's
"never a roster" doctrine (draft:284-288, 1154-1158) is the spec's
own design logic carried up a layer, correctly. Sound.

---

## 3. N2 — Seam findings

Lane (a), demanded properties: sound, one line — the kernel
nowhere requires ordering, finality, availability, or a global
view the substrate does not provide; the availability charter is a
committed floor rather than a presumption, appraisal time is log
positions, and the observation premise (§13, draft:1227-1235)
disclaims omniscience explicitly.

Lane (b), duplicated machinery: substantively clean at the log
layer; the one near-duplication (warranty vs. the spec's own
Endorsement/Judge vocabulary) is filed as opportunity KN-16 rather
than defect because the kernel's warranty carries strictly more
structure (pinned lens, replay-falsifiability).

### KN-10 · MAJOR · Lane (c): the GEL's anchoring discipline is asserted, not specified

Kernel cite: §3, "GEL (extension) — … each event anchored through
the gAID's key state" (draft:183-186); §5, "sealed by a GEL event
at a coordinate, authenticated through the gAID's key state"
(draft:324-325).

Substrate cite: ACDC:1918 — "Events in the TEL are sealed
(anchored) in a Key Event Log (KEL) using seals. A seal can be as
simple as the event's SAID"; KERI:395 (seals bind a commitment to
the key state of a KEL at the seal's location); KERI:448-454
(source event seals for registry/transaction endorsement).

"Anchored through the gAID's key state" names an outcome, not a
mechanism. The substrate has an exact, normative pattern for
third-log anchoring — the TEL discipline: log events are sealed
into the KEL via seals in the anchor list, inheriting the KEL's
duplicity evidence and establishment lineage. If the GEL follows
that pattern, the kernel should say so in one sentence with the
ACDC:1918 cite, and the GEL needs no new substrate blessing — it
is a TEL-shaped log with governance semantics, which is the
strongest possible position before this audience. If the GEL does
NOT follow that pattern (e.g., GEL events carry their own
signatures without KEL seals), that is a new anchoring pattern and
must be confessed as an extension requiring review. The draft
currently lets the reader assume either. This is the highest-value
one-sentence repair in the document.

### KN-11 · MAJOR · Lane (d): the outward face has a KRAM-shaped hole

Kernel cite: §12, the availability charter — "a committed
obligation that the key state and evidence its judgments depend on
remain available and receipt-consistent" (draft:1140-1143); §10.2
step 2, "B fetches E's verification cone" (draft:850-851); §13
lists "receipt transport" as open interior (draft:1204).

Substrate cite: KRAM:9-13 (authentication types for requests:
attached signature single/multi-key, anchoring-seal reference);
KRAM:29-33 (gap replay and gap first-play attacks against hosts
that serve authenticated requests under datetime windows); KRAM:37
(KRAM assumes the sender's KEL is already held by the receiver);
KRAM:40 (query `qry` and all non-key-event message types pass
through KRAM before message-specific processing).

The charter obligates a serving surface: strangers fetch cones,
consumers query registries, federates exchange recognition
evidence. Every one of those consumption paths is a request at a
host, and the substrate's own design answer for authenticating
requests at hosts — with its cache windows, replay-attack
taxonomy, and KEL-availability assumption — is KRAM. The kernel
says nothing about whether cone-fetch requests are authenticated,
rate-disciplined, or anonymous, and the openness clause's "receipt
transport" confession does not cover it, because the *charter* is
normative kernel law while transport is confessed open — the
charter thus commits an obligation whose discharge posture is
undesigned without saying so. Additionally, KRAM timeliness is
wall-clock-windowed (KRAM:25, 29-33) while the kernel bans wall
clocks from findings (§6.3, draft:448-453); these are compatible —
transport admission is not appraisal — but the kernel should say
that in one sentence, or a hostile reader will claim the outward
face smuggles wall-clock time into the evidence path. Repair: add
a federation duty naming request authentication at charter
endpoints as a committed deliverable, citing KRAM as the substrate
mechanism, and one boundary sentence separating transport
timeliness from appraisal position.

### KN-12 · MAJOR · Lane (e): the cone's disclosure posture is an unconfessed PAC trade

Kernel cite: §5, the verification cone "the minimal committed log
spans (GEL, KEL, TEL as cited)" with the charter as "the committed
guarantee that the cone is fetchable" (draft:327-331); §7,
registry evidence as standing input (draft:602-614).

Substrate cite: SPAC:11-17 (the PAC trilemma: authenticity,
confidentiality, privacy — pick two at the highest level; ToIP
order: authenticity, then confidentiality, then privacy);
ACDC:1783-1790 (contractually protected disclosure and chain-link
confidentiality as core ACDC machinery); DOSS:458 (dossiers MAY
use graduated disclosure), DOSS:464 (correlation-vector analysis
for dossier-based protocols), DOSS:509 (the Redacted Dossier
pattern reconciling public verification with confidential
sources).

The kernel maximizes authenticity and replayability — every
judgment public, every cone fetchable by strangers. That is a
lawful corner of the PAC trade space, but it is a *trade*: the
standing evidence in a cone is registry evidence about persons
(seat qualifications, endorsements, custodial identities), the
exact material the substrate's graduated-disclosure and chain-link
machinery exists to protect, and the dossier spec the kernel
adopts as carriage form carries both a correlation analysis and a
redaction pattern the kernel never mentions. One elegant privacy
touch exists (§9: custodian identities "hidden in digest until
exercised," draft:753-755) and proves the drafters can do this
when they look. What the kernel owes the transport layer, per this
lane's question, is a stated posture: either "cones are
full-disclosure and this document trades privacy for
auditability" (confessed, PAC-cited), or an adoption of the
dossier spec's graduated/redacted disclosure with the standing
machinery told how to appraise partially disclosed evidence
(pending species already fits: an undisclosed span is a typed
requirement). Silence is the only wrong option.

### KN-13 · MINOR · "Join-reached" is phrased temporally where no shared time exists

Kernel cite: §10.1, "The bond binds at join-reached: when the
second anchor lands, computed by any verifier, decided by no one"
(draft:825-826).

Substrate cite: no committed cross-KEL ordering exists anywhere in
the corpus (content search over KERI/ACDC/CESR spec bodies,
2026-07-22 — sequence numbers and first-seen ordinals are
per-KEL: KERI:323, KERI:1799). Grounded as absence at search
grain.

"When the second anchor lands" has no verifier-invariant referent:
landing is observer-relative, and two verifiers discover the pair
of anchors in different orders. The property is monotone — once
both anchors exist in both committed logs every verifier computes
the bond — so the construction is sound; only the temporal
phrasing is wrong, and it is wrong by the kernel's own
no-ambient-order law. Repair: bind the bond at a coordinate pair
(A's recognition event coordinate, B's recognition event
coordinate), existing for any verifier holding both spans; delete
"when."

---

## 4. N3 — Missed opportunities

### KN-14 · The typed seal as the covenant seal's carriage

- **What:** The kernel introduces the covenant seal as a new
  commitment kind (§8, draft:687-697) with no statement of how it
  is carried in a log event.
- **Where in corpus:** KERI:511-518 — the typed seal: a versioned
  type field plus digest, expressly "a generic facility for seals"
  with CESR count codes already allocated (`-W`/`--W`, KERI:421-422).
- **Adoption cost:** Low. Define a covenant-seal type/version
  value under the typed-seal `t` field grammar; the digest commits
  to the covenant-set SAID; verification semantics remain the
  kernel's.
- **Recommendation:** Adopt. It converts the covenant seal from
  "new seal kind needing substrate blessing" into "profile of the
  substrate's own extension point," which is both technically
  cheaper and rhetorically the difference between an allocation
  request and a citation. (The kernel's travel posture,
  draft:1175-1179, forbids allocation requests before custodial
  answer — the typed seal is how to not need one.)

### KN-15 · Delegation (dip/drt) for seating, strata, and custodial recovery

- **What:** The kernel's organs are "seated" via GEL events and sit
  in "delegation strata" (§3 draft:280-284, §9 draft:769-772, §12
  draft:1140-1149), but the draft never says whether an organ
  identifier is a KERI delegated AID, and its §9 rotation-policy
  axes re-derive machinery the substrate already ships for
  delegated identifiers.
- **Where in corpus:** KERI:287-288 (`dip`/`drt` event types);
  KERI:623 (dip's `di` delegator field); KERI:1813-1825 (B1-B3:
  delegator-mediated superseding recovery of a delegated rotation
  — substrate-native custodial recovery); KERI:379 (the `DND`
  config trait — committed control of delegation depth, i.e.
  stratum bounding).
- **Adoption cost:** Moderate — a normative sentence per organ
  class plus cites; no new machinery.
- **Recommendation:** Adopt at least the citation: state that
  seated organs SHOULD be delegated AIDs of the gAID, at which
  point (i) "who may invoke" and "what defeats it" (§9 axes,
  draft:749-763) are partially discharged by delegator approval
  and B-rule recovery in the medium itself, (ii) the availability
  charter's "delegation strata" acquire the substrate's own
  delegation semantics rather than a metaphor, and (iii) the §9
  claim that bare pre-rotation is "defeasible by nothing"
  (draft:743-746) gets its needed exception — for delegated AIDs
  the substrate already imposes a richer policy than the
  degenerate one.

### KN-16 · The spec's Endorsement/Juror/Judge vocabulary as the warranty's lineage

- **What:** The kernel's warranty ("a signed attestation of a
  computed finding," §5 draft:345-347) and warrantor discipline
  (§10.3-10.4) are presented without substrate lineage.
- **Where in corpus:** KERI:1276 — non-controller, non-witness
  signatures on events "can be called Endorsements," the watcher
  endorsing its first-seen version being the worked example;
  KERI:51-53 — Juror (records and provides duplicity evidence),
  Jury, Judge (evaluates key events on that evidence) as named
  ecosystem roles.
- **Adoption cost:** Trivial — two citations.
- **Recommendation:** Cite. The warranty is a strict refinement of
  the spec's Endorsement (adds pinned lens and
  replay-falsifiability), and the warrantor is the kernel-layer
  Judge whose verdicts are disciplined by replay. Naming the
  lineage converts an apparent parallel invention into a visible
  strengthening of the substrate's own roles — exactly the
  reception this audience rewards.

### KN-17 · IPEX for cone and dossier exchange

- **What:** The kernel specifies what crosses frames (§5) and the
  duties before travel (§12) but no exchange protocol by which a
  consumer requests, negotiates, and receives a cone or dossier —
  a gap that becomes acute if KN-12's graduated-disclosure repair
  is adopted.
- **Where in corpus:** IPEX:3-7 (negotiation of graduated
  disclosure via schema-as-type plus attribute path lists);
  IPEX:52-56 (the apply/offer/agree/grant chain); IPEX:58-70
  (multi-ACDC path dicts for chained disclosure — a cone is such a
  chain).
- **Adoption cost:** Low as citation (name IPEX as the negotiation
  layer for warranted or contractually protected cone disclosure);
  the full profile is companion-grade work.
- **Recommendation:** Cite in §12 as the substrate's exchange
  machinery for the consumption paths that are not bare
  charter-floor fetches; do not profile it in the kernel.

### KN-18 · ACDC schema machinery for the kernel's committed-object typing

- **What:** The kernel's four crossing objects (edict, cone,
  warranty, colored evidence) and its typed requirement sets are
  committed objects with no stated typing discipline — are they
  ACDCs, bespoke SADs, or unconstrained?
- **Where in corpus:** ACDC:132 and ACDC:236-248 (composable JSON
  Schema, schema-as-SAID typing, `oneOf` compaction); ACDC:168
  (metadata ACDC — commitment to a not-yet-disclosed object, which
  is the pending species' natural evidence form); ACDC:85 and
  ACDC:1914-1918 (`rd` registry binding, giving warranties
  revocable state for free).
- **Adoption cost:** Moderate; but note the kernel already
  half-commits — §5's edict is expressly "never an issuer-bearing
  container" (draft:322-324), so the edict is deliberately NOT an
  ACDC, while the warranty ("signed attestation … emitted under a
  pinned lens by a warrantor staking its own committed identity,"
  draft:892-898) is the textbook ACDC attestation.
- **Recommendation:** One normative sentence per object kind:
  edict = bare SAD (stated, with the existing rationale); warranty
  = ACDC (schema-typed, registry-bound, hence revocable and
  edge-linkable to its lens); requirement elements = schema SAIDs
  in the ACDC sense. This is the difference between the KERI
  toolchain consuming kernel objects on day one and every
  implementer inventing a parser.

### KN-19 · CESR carriage posture — say something

- **What:** The kernel commits SAID discipline (its §2 rule 2 is a
  correct CESR SAID computation per CESR:1197-1234, KN-08 aside)
  but never states a serialization or attachment posture for its
  own object classes — no committed answer to "what does a GEL
  event, an edict, or a warranty look like on the wire."
- **Where in corpus:** KERI:399-422 (seals as CESR count-code
  groups, native attachment grammar); CESR:1197-1234 (SAID
  round-trip); the substrate's whole attachment design assumes
  composable native groups rather than enveloped documents.
- **Adoption cost:** Low to confess, moderate to profile.
- **Recommendation:** At kernel grade, one openness-clause line:
  carriage encoding of kernel object classes is a committed
  deliverable (companion), with CESR-native attachment groups the
  default posture per bedrock law 9's own "CESR-grade commitments"
  standing check. Silence here reads to a CESR author as
  document-envelope thinking.

### KN-20 · OOBI for the one-hop resolution duty

- **What:** §12 Naming requires the traveling vocabulary to
  resolve "one-hop through its notation register" (draft:1090-1094)
  and the charter promises fetchable logs, but discovery — how a
  stranger finds the charter's endpoints at all — is unnamed.
- **Where in corpus:** KERI:2676-2683 (OOBI URLs binding AIDs to
  roles and service endpoints); KERI:2853 (`iurls` resolution
  yielding KEL and endpoint-authorization proofs); KERI:2944
  (BADA-RUN for securely managed endpoint discovery data).
- **Adoption cost:** Trivial citation.
- **Recommendation:** Cite OOBI/BADA-RUN as the discovery
  substrate under the availability charter. OBSERVATION-weight;
  include if §12 is touched for KN-11.

---

## 5. N4 — The audience message

The primary external audience is the KERI community's engineers
and spec authors, and the honest summary is: this document will
survive that audience's immune system almost everywhere except its
first page — and the places it survives, it survives unusually
well.

**What earns trust.** The custody posture is close to exemplary.
"Everything below it belongs to the substrate and is cited, never
restated" (draft:36-37) is the right covenant, and the draft
mostly keeps it. The travel posture — "Questions travel as
questions" (draft:1175-1179) — is a sentence spec custodians
should want framed; it renounces in advance the allocation-request
and defect-report postures that make outside governance work
obnoxious. Stated evidence scale (draft:1096-1112), with its
explicit confession that every executable claim rests on one
implementation at one pinned checkout, is the kind of honesty spec
authors extend credit for; likewise the openness clause's walls/
open/unresolved trichotomy and the §14 admission that
authority-lineage materialization follows the document. The
watcher doctrine is the spec's own ambient-verifiability logic
(KERI:45, 1882-1884) carried up a layer with the reasoning intact
— a substrate reader will recognize their own design instincts
honored rather than paraphrased (KN-09). And the core offer is
real: the substrate community has no committed judgment layer, the
"KERI detects; a GARD appraises" boundary is drawn where the
substrate's own controller/validator division points (draft:
217-227), and the transformation law's evidence-only crossing is
the correct generalization of end-verifiability to judgments.

**What triggers the immune system.** Three things, in descending
order. First, the opening paragraph (KN-01): it tells this
community their protocol "remains silent about recourse" and
leaves the validator's response discretionary, when the spec bytes
legislate the response (KERI:53) and enumerate a recovery calculus
(KERI:1784-1827) the community regards as one of its hardest-won
achievements. A reviewer named Smith reads that paragraph as
evidence the authors have not read the reconciliation sections —
and then reads the rest of the document looking for confirmation.
That is a catastrophic discount rate to buy with one paragraph,
and it is unnecessary: the kernel's true premise — the substrate
committedly refuses to legislate *what the evidence means for
governance* — is stronger and is actually in the spec's own words
("there is no requirement for shared governance over any of the
infrastructure components," KERI:61). Second, the naming custody
slip (KN-03): "the substrate names its folds" claims the
specifications say something they nowhere say; minting "Gever"
inside what is actually keripy's class-naming convention will read
to an implementer as charming and to a spec editor as an outside
document asserting how the substrate's naming grammar extends.
Attributed correctly — "the reference implementation's fold names,
extended by one rung" — the same move becomes a compliment.
Third, the small over-attributions that pattern-match to land
grab even where substance is fine: "the substrate ships the first
two" seal kinds (KN-06), "the substrate's native edge-operator
grammar" for a dossier-spec profile (KN-07). Each is a
one-clause fix; together they decide whether §7 and §8 read as
consumption or annexation.

**Contribution or land grab, by section.** §4 (the medium), §6
(the codomain), §10 (the transformation law), §11 (recourse), and
§13 (openness) read as contributions — they add a layer the specs
deliberately do not have, and they keep citing downward correctly.
§7 reads as contribution once KN-07's attribution is fixed; its
threshold-algebra unification sentence is the single best bridge
in the document because the dossier spec itself asserts the same
identity (DOSS:353). §8 currently reads closest to land grab: it
renames the substrate's seal taxonomy into a two-kind ladder,
undercounts it, and then plants an extension on top; fixed per
KN-06 plus KN-14 (covenant seal as typed-seal profile), it becomes
a model citizen. §3's fold grammar is the annexation risk (KN-03).
§12 and §14 read as contributions and, frankly, as better
federation-duty discipline than most substrate-adjacent documents
impose on themselves.

**The single highest-leverage change.** Re-ground the document's
relationship to the substrate's reconciliation machinery, in one
coordinated repair: rewrite §1's silence claim on KERI:53's own
words, scope §4's conviction rule by the superseding rules
(KN-02), and type §6.2's window-cure per KEL class (KN-04). It is
one repair because it is one error surfacing three times — the
draft treats the key tier as detection-only, when the substrate's
key tier already contains a committed reconciliation calculus, and
the kernel's whole value proposition ("the substrate stops at
detection; we commit judgment") is *strengthened*, not weakened,
by stating exactly where the substrate's own recourse ends: at key
state, by rule, with reconciliation — and never above it. Make
that repair and the document's first page recruits the reader the
rest of the document deserves.

---

## 6. QA register — training-prior claims and grounding limits

Per the brief's discipline, every claim I could not ground in
committed corpus bytes, or grounded only as absence-at-search-
grain:

1. **"Kever"/"Tever" absent from spec bodies** (KN-03): grounded
   as absence by content search over all three TSWG spec bodies
   (0 matches, 2026-07-22). Absence claims are search-grain, not
   proof-grain; the positive claim (keripy class names) is
   byte-grounded at the cited paths.
2. **No committed cross-KEL ordering in the corpus** (KN-13):
   grounded as absence at search grain (per-KEL `sn` at KERI:323,
   per-KEL first-seen ordinal `fn` at KERI:1799; no cross-KEL
   order construct found). Marked as such in the finding.
3. **512-bit digest SAIDs encode longer than 44 characters in
   CESR** (background to KN-08): training-prior claim, no corpus
   cite — the committed corpus shows the length-parametric rule
   (CESR:1197-1199) and the 44↔Blake3-256 association (CESR:1265)
   but I did not locate a corpus byte stating the 88-character
   encoding of larger digests. KN-08 as written depends only on
   the corpus-grounded length-parametric rule, not on this prior.
4. **"IPEX" as the settled name of the apply/offer/agree/grant
   protocol with normative standing in the ACDC spec**: the held
   corpus grounds the mechanics and message chain
   (IPEX:3-7, 52-56) but the held IPEX paper is a design note, not
   a ratified spec body; whether IPEX is normatively specified
   elsewhere in the TSWG corpus is a training-prior claim, no
   corpus cite. KN-17's recommendation (cite as substrate
   exchange machinery) is phrased against the held bytes only.
5. **KRAM datetime windows are wall-clock**: grounded at
   KRAM:25-33 (datetime stamps, accept/prune window lags); the
   further prior that these datetimes are UTC ISO-8601 per KERI
   message convention is training-prior, no corpus cite, and is
   not load-bearing in KN-11.
6. **Reception predictions in §5 (N4)** — how named individuals
   or the community "will read" passages — are reviewer judgment,
   not corpus-groundable, offered as the brief's lane N4 requires
   and marked here once for the whole section.

No other prior-knowledge assertions are made without a corpus
cite; every KERI/ACDC/CESR/KRAM/SPAC/dossier behavior claim above
carries its path:line.

— end of review —
