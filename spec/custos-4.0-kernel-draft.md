# Custos 4.0 — kernel, assembled draft v1 


---

## 1. Scope and non-goals

**Abstract** — A governance layer for KERI-based identifier
infrastructure is presented. KERI settles who speaks for an
identifier: key state committed to witnessed, end-verifiable
logs; duplicity — two voices at one coordinate — evident to any
observer holding both; recovery provided at the key tier; the
trust decision ruled in KERI's own words (an honest validator
MUST NOT trust key state carrying unreconciled evidence of
duplicity). There KERI deliberately stops. Whether a duplicitous
authority keeps its seat, whether acts it signed retain standing,
what a counterparty is owed once trust is withdrawn — these are
law above key state, and KERI imposes none; every consuming
system improvises its consequences, and improvisation does not
compose. This document presents the GARD — Governed Autonomic
Replayable Domain — which extends end-verifiability from control
provenance to governance provenance: law, evidence, and judgment
as committed bytes under one identifier, every judgment
recomputable by any verifier holding the logs. Ambient
verifiability, carried from key state to judgment. KERI detects;
a GARD appraises. The boundary between those two verbs is the
boundary of this document: everything below it belongs to the
substrate and is cited, never restated; everything above it is
specified here.

The GARD's defining obligation is replay: a conforming domain
MUST make every judgment it issues recomputable,
byte-identically, by any verifier holding its committed logs.
That obligation is exercised today at fixture scale — one
implementation, one pinned checkout — and cross-implementation
equality is a confessed open deliverable; the obligation, not its
full discharge, is what defines the class.

The document is built medium-first, because its subject is not one
domain but the composition of many: first the invariant medium
every frame already shares, then the objects that cross between
frames, then the interior machinery of a single frame, and then
the transformation law — how one frame's edicts are consumed and
federated by another, mediated by key state. A GARD in this
document is a frame of appraisal among frames, never an authority
over them; whatever a section says about one GARD's interior is
subordinate to what the whole document says about the space
between them.

This document specifies:

- the medium and the objects that cross it — the frame-invariant
  substrate, and the portable forms (edict, verification cone,
  warranty, colored evidence) every crossing uses;
- the finding — the sole return type of governance appraisal —
  with its four values, its evidence ordering, its complete
  transition system, and the pending species that describe cure;
- standing — how committed registry evidence becomes a judgment
  of authority under committed covenants, and why the two are
  never the same thing;
- the seal ladder — the three commitment kinds this standard's
  anchors use, and the admissibility rule for a deferred fourth;
- rotation policy — the frame's committed relationship to time:
  who may rotate its identifiers, on what evidence, effective
  when, defeasible by what;
- the governed object classes — the criterion and the relation
  axis by which the frame's one move generalizes, and the
  reflexive class that makes the domain autonomic;
- the transformation law — how edicts cross frames: unilateral
  consumption, bilateral federation, and the discipline that
  replaces a judge above;
- recourse — the grounded enactment, by which judgment becomes
  lawful, replayable consequence, and the ladder of what that
  consequence may be at each relation;
- the federation duties — what a frame owes before its judgments
  travel, including the availability charter;
- the openness clause — the exact boundary of what this document
  has and has not designed; and
- succession — how this document lawfully replaces its
  predecessor and how it may itself be replaced.

This document does not specify:

- a complete construction of the Gever, the governance evaluator.
  This document fixes the evaluator's type boundary — what it
  consumes, what it returns, when it must refuse — and confesses
  its interior undesigned. The openness clause states this
  boundary exactly.
- a deployed watcher infrastructure. The judgments specified here
  are decidable over the evidence actually surfaced; the
  availability charter commits a floor under that evidence, and
  no clause of this document presumes an observer who sees
  everything.
- cross-implementation interoperability. Every executable claim
  in this document's evidence trail was exercised against one
  implementation at one pinned checkout. Agreement between
  independent implementations is a committed, unfinished
  deliverable, and no clause here claims it.
- a complete registry of governance acts. Where this document
  names acts (enactment, seating, recovery, reconciliation), it
  binds their evidence requirements; it does not enumerate the
  act universe.

Two commitments of posture shape the design, stated once here as
aims. Law in this document is dynamical: a frame's own law is
among the objects the frame governs, and every change to it is
judged under the law in force before it — the posture this
standard's record names general-relative, derived in section 10.
And composition carries no global frame: sovereign frames compose
as local charts compose an atlas — local appraisal, committed
transport, overlap measured where committed law shares a fragment
— with no chart of the whole anywhere, as design rather than
lack: agreement between frames is built relation by committed
relation from the ground up, and no authority owns the
comparison.

The reader this document assumes is adversarial: a reviewer
looking for the sentence that promises more than its evidence.
Sections are ordered so that each claim's grounds precede it
(two confessed exceptions: rotation policy precedes the recourse
profile it invokes, and the governed object classes precede the
transformation law whose congruence measure they cite; each
forward reference is explicit where it occurs), and
the openness clause exists so that the frontier of the design is a
published surface rather than a discovery.


## 2. Normative language and reading rules

The key words MUST, MUST NOT, SHALL, SHALL NOT, SHOULD, SHOULD
NOT, MAY, REQUIRED, RECOMMENDED, and OPTIONAL in this document are
to be interpreted as described in BCP 14 (RFC 2119, RFC 8174)
when, and only when, they appear in all capitals.

Three reading rules govern the whole text:

1. Keyword-marked sentences are ruled spans. Every sentence
   carrying a BCP 14 keyword is a normative commitment of this
   document, individually extractable and individually testable.
   The set of ruled spans is the document's normative content;
   prose between them motivates and derives but binds nothing on
   its own. Keyworded text quoted from another corpus and
   attributed to it where it appears remains that corpus's
   commitment, cited here; quotation enters nothing into this
   document's ruled spans. This convention is shared with the governance corpora
   a GARD is built to consume — a framework that marks its
   requirements in the same defined-force grammar can be lifted,
   span by span, into committed predicates.

2. Digest pins name exact bytes. Where this document pins a
   digest, the pinned preimage is defined in the text beside the
   pin, computed with the digest's own field carrying a
   placeholder of the same length as the encoded digest — the
   substrate's rule is length-parametric by derivation code, and
   forty-four characters is this document's current profile, the
   256-bit digest class — and verified by
   round trip before the pin travels. A digest whose preimage is
   not stated is not a pin; it is decoration, and this document
   contains none.

3. This document derives; it does not allude. Every doctrine
   stated here either carries its grounds in the same section or
   cites the committed artifact that does. Terms of art from
   other communities appear with their coiner named. The
   predecessor document, Custos 3.3, is byte-immutable and is
   cited, never edited; this document replaces it whole, by the
   succession rule in its final section.

**The substrate of record.** The protocol layer this document
builds on is KERI, with ACDC as its credential layer and CESR as
its encoding layer, in the specifications stewarded by the Trust
Over IP Foundation's specification working group, and with keripy
as the reference implementation this standard's executable
evidence was exercised against, at the pinned checkout its record
states. The revision of record for each specification is pinned
in the engagement companion under this document's own pin
discipline; within this document the substrate is cited by name
and never restated.


## 3. Definitions

**The minimal case, before any definition.** The smallest GARD
is one identifier that has committed how it will behave and keeps
the receipts. A person incepts an identifier, sealing into the
inception a founding law of a single page: who may rotate these
keys and on what evidence, what this identifier's silence means,
which credentials it honors and what they confer. From then on,
every act the identifier takes is either lawful under that page
or committed evidence that it was not — and any stranger holding
the logs reaches the same verdict, because the page is bytes and
the verdict is a computation. No members, no organs, no
committee, no second party: one key state, one page of law, one
log binding them. That object, whole, is a GARD; frame size is
nowhere a parameter of this document's law, and nothing defined
below requires more of a domain than this paragraph exhibits. An
ecosystem-scale authority and a single person's identifier are
the same species at different masses, and everything that
follows — the finding, standing, recourse, the transformation
law — is what this one object does, written out in full.

The terms defined here do load-bearing work: each is defined
once, and every later use means exactly this. Terms inherited from the
substrate are marked as such and cite their origin; terms this
standard introduces are marked as extensions.

**GARD.** A Governed Autonomic Replayable Domain: a governed
domain whose constitution, evidence, and judgments are committed
bytes under one identifier, such that lawfulness within the domain
is decidable by replay. "Governed": its law is committed and
succeeds only by its own committed rules. "Autonomic": its
identity is self-certifying, rooted in key state, borrowing no
external authority. "Replayable": the domain's conformance
obligation that any verifier holding the logs can recompute every
judgment to identical bytes — discharged today at the evidence
scale the federation section states.

**gAID** (extension). The autonomic identifier of a GARD itself:
the identifier whose key event log anchors the domain's
governance events. A GARD's identity is its genesis, and the
genesis is a constructed knot rather than a judged act. A
born-governed GARD's genesis is the pair (K0, C): an inception
event and a founding Constitution text. C is computed first — its
authors pre-exist the domain — and refers to the domain's
authority only through a reserved sentinel resolved at
verification; the sentinel binds to whichever prefix's inception
seals C. K0 SHALL seal C's self-addressing identifier among its
anchoring seals, and the gAID is K0's self-addressed prefix: the
founding law lies inside the bytes the identity digest ranges
over, so the same keys under a different founding law name a
different domain, and two domains sealing one founding text are
distinguished by their inceptions, never by C's identifier. The
gAID SHALL NOT appear in C or in any body C cites, transitively —
the sentinel, the seal, and this exclusion are the cuts that
close the genesis cycle, and their conformance vectors are a
committed deliverable of this standard's record. A domain MAY
instead incept bare and anchor its founding law later: the
adopted construction is lawful at a confessed lesser grade — its
identity ranges over keys alone, and its founding law is as
displaceable as any later anchor — and a consuming frame may
weigh the difference. A GARD's current law is a computed state,
never a new identity.

**Frame.** A GARD regarded from between domains: a sovereign
locus of appraisal whose judgments are valid in its own frame,
computed under its own Constitution, and carry no force elsewhere
by existing. "GARD" and "frame" name one object; "frame" is used
where the emphasis is the space between domains — no frame is
preferred, and force is frame-local. The transformation law
(section 11) is the law of that space.

**The three logs.** Substrate vocabulary, cited (KERI and its
credential-registry layer), except the third, which this standard
introduces in the substrate's own naming grammar:

- **KEL** — key event log. The committed, append-only record of
  an identifier's key state: who may sign, established by what
  succession. Substrate-native.
- **TEL** — transaction event log. The committed record of
  registry state: issuance, revocation, and their successors,
  anchored to a KEL. Substrate-native.
- **GEL** (extension) — governance event log. The committed
  record of a GARD's law: constitution, amendment, seating,
  enactment. GEL events are sealed into the gAID's KEL by the
  same anchoring discipline the substrate's registry layer uses
  for TELs — a seal in the anchoring event carrying the GEL
  event's self-addressing identifier — so the GEL is a TEL-shaped
  log with governance semantics, inheriting the KEL's duplicity
  evidence and establishment lineage; this standard introduces no
  new anchoring pattern. What the KEL is to keys and the TEL is
  to credentials, the GEL is to law.

**The three folds.** Each log has a fold: a pure function from
committed log bytes to computed state. The specifications name
the logs; the reference implementation names the folds after the
logs they fold, and this standard adopts that naming convention
and extends it by one rung:

- **Kever** — folds a KEL to current key state (the reference
  implementation's class name, adopted).
- **Tever** — folds a TEL to current registry state (likewise the
  reference implementation's name, adopted).
- **Gever** (extension of the implementation convention) — folds
  a GEL, in the context of the KELs
  and TELs it cites, to the Constitution: the answer to "what law
  governs this domain at this position, and what standing does
  this party hold under it."

**Constitution** (extension). The
constituted law-in-force of a GARD: the Gever's computed output,
as key state is the Kever's and registry state the Tever's. The
Constitution is a computed state, never a document: a ratified
text is an event in the GEL; the Constitution is what the fold
returns over all of them. Two GARDs holding identical GELs hold
identical Constitutions — the property that makes law replayable
rather than testimonial.

Log and fold are one structure read twice: the log is the
committed evidence; the fold is the computed judgment; nothing in
the judgment may exceed the evidence. Each fold consumes the
output of the fold below it — the Gever presupposes Tever-state,
which presupposes Kever-state — and no fold writes into any log.

**Evaluator; constructor.** The two roles this standard separates
absolutely. A constructor changes a GARD's state: it ratifies
composition rules, seats authorities, advances lifecycle, commits
acts. An evaluator — the Gever's role — consumes a committed
regime and returns findings; it changes nothing, and where the
committed law runs out, it refuses rather than legislates. The
separation is the substrate's own controller-validator division
carried up to the governance layer: only a controller writes a
KEL; any validator verifies it; no validator, however convinced,
may write. "Appraisal" names the activity and the layer: KERI
detects; a GARD appraises.

**Finding** (extension). The sole return type of the evaluator: a
judgment over a committed regime that carries its own ground. A
finding that does not carry its ground is not a finding. The four
values, specified fully in the codomain section: affirmed;
defeated, carrying the citation that defeats; pending, carrying
the typed requirement that would discharge it; and
self-convicted, carrying the canonical proof package that
identifies the contradictory pair. Findings are judgments
about propositions, never states of processors, seats, or
lifecycles — that boundary is carried at keyword
force by the codomain section's ratified amendment text, which
draws it exactly.

**Standing** (extension; the term in its jurisprudential sense).
A covenant-derived judgment of authority: whether a party, at a
position, holds a given power under the GARD's committed law.
Registry evidence is the input; standing is the computed output;
the committed covenant set is the function. The distinction is
load-bearing and the standing section specifies it.

**Covenant.** A committed, verifier-decidable constraint over a
domain's transitions or evidence, carried in the GARD's law and
evaluated by replay. Covenants constrain; they do not act.

**Committed.** Bytes are committed when they are signed into a
log under an identifier's key state and anchored so that the
medium's duplicity relation ranges over them. Committal is what
converts data into evidence: a committed artifact can convict its
author; an uncommitted one cannot. Availability and receipt
discipline over committed bytes are the charter's subject, not
part of this definition.

**Law head; position.** A law head is the self-addressing
identifier of the committed law an appraisal runs under — the
Constitution state, at a coordinate, that a finding cites as its
rule-set. A position is a log coordinate (identifier, sequence
number) in the committed order of the log it names; this document
never measures position in wall-clock time.

**Lens.** The committed coordinates of an appraisal semantics:
which rule-set, which engine profile, which predicate set a
finding or warranty was computed under, cited by identifier. A
pinned lens is a lens cited immutably in the committing artifact.

**Organ; seat.** An organ is an identifier seated by the GARD to
act in a named role, whose acts enter the GEL as acts of the
domain. A seat is the committed grant of that role: an
establishment act citing the role's clause. This document uses
both words at exactly this grain and designs neither seating
procedure nor organ architecture — the openness clause holds
them open.

**The seal kinds.** Three commitment kinds, named beside the
substrate's own seal grammar (the first two subsume kinds the
substrate ships; the third is this standard's extension): the **digest seal**
commits to exact bytes; the **event seal** commits to an event at
a log coordinate; the **covenant seal** commits a subject to the
GARD's covenant set — verified not by byte equality nor by
coordinate lookup but by whether the successor satisfies the
committed clause. A fourth kind, the **evaluation seal** — a
committed verdict — is named here and deferred: its admissibility
rule appears in the seal section, and no construct in this
document uses it.

**Governed protocol** (ratified species name). A protocol whose
rules of interpretation are themselves under committed,
verifiable succession — the governance extension of a
verifiable algorithm: a computation any verifier can recompute
from committed inputs to the identical result. A GARD whose
governed corpus is a protocol specification is the reference
case; the federation section states its conditions.

**Duplicity** (substrate term, extended by tier). Two voices
where the constitution of a tier demands one, proven by the
author's own committed bytes. The voice unit rises with the tier:
at the key tier, two events at one coordinate; at the registry
tier, two registries where committed law demands one chain; at
the governance tier, contradictory enactments under one committed
predicate. Each tier's duplicity is invisible to the machinery of
the tier below — the codomain section carries the ladder.

**Availability charter** (extension). A committed obligation,
propagated down a GARD's delegation strata, that the key state
and evidence a stratum's judgments depend on remain available and
receipt-consistent: each stratum's witnesses discharge it; its
scope and floor are specified in the federation section. The
charter commits obligations over logs, never a roster of
observers — an enumerated observer set is a witness set by
definition, and the deterrence value of unenumerated observation
survives only while it is unenumerated.


## 4. The medium

Between frames there is no shared judge. There is a shared medium:
key state, SAID-addressed bytes, and the duplicity relation —
the three things every verifier in every frame computes
identically from the same committed inputs under the substrate's
pinned semantics, because their agreement is cryptographic rather
than negotiated. A KEL folds to the same key state everywhere; a
SAID resolves to the same bytes or convicts the presenter; and a
pair of committed voices at one coordinate that no committed
superseding rule reconciles convicts its author for every
verifier holding the pair, under no frame's law. The scoping is
the substrate's own: its superseding-recovery rules lawfully
admit a second event at a coordinate as reconciliation — a
rotation recovering a compromised log is repair, cited, not
duplicity — and the medium's conviction predicate is stated
modulo those rules, which are the committed decision procedure
for whether a pair bears. The medium is the substrate's
achievement, cited here and added to nowhere: this document builds
on key state; it does not extend it.

Two properties of the medium carry the whole architecture. First,
authentication is frame-invariant: whether an event is admitted
by an identifier's key state is decided by the substrate's own
machinery, identically for every observer — so the first half of
every cross-frame computation needs no agreement between the
frames at all. Second, nothing in the medium ranks frames: there
is no privileged vantage, no root registry, no frame whose
judgments are the medium's own. The medium carries evidence and
convicts duplicity; it never judges. Judgment begins only inside
a frame, under committed law — which is what the rest of this
document specifies.

## 5. The objects that cross frames

What crosses a frame boundary is never judgment; it is committed
evidence in portable form. Four object forms carry every crossing
this document itself makes. They are this kernel's forms, not a
proven closure of the crossing space, and they interrelate rather
than partition — a warranty may travel as a component of colored
evidence, and a cone is a collection over the others:

- **Edict** — a committed governance act of one frame: a bare
  SAID-addressed content (never an issuer-bearing container; the
  center is the SAID), sealed by a GEL event at a coordinate,
  authenticated through the gAID's key state, citing the law head
  under which it was enacted.
- **Verification cone** (of an edict) — the minimal committed log
  spans (GEL, KEL, TEL as cited) from which a fresh verifier
  authenticates the enacting voice, resolves the coordinate, and
  recomputes the enactor's standing. The availability charter is
  the committed guarantee that the cone is fetchable. The cone's
  portable carriage form is the verifiable dossier (the Trust
  Over IP dossier specification; cited, consumed, not restated):
  a container whose payload is a graph of references to external
  evidence, whose issuer attests to the integrity and composition
  of the collection — never to the veracity of the claims within
  it. That division is exactly this law's: the dossier issuer's
  signature is a composition warranty over the cone's carriage;
  the edict's identity remains the bare content SAID; and the
  judgment remains the consuming frame's computation. A frame
  presenting an edict across a boundary SHOULD present it as a
  dossier over its verification cone, and a dossier's threshold
  operators are the same committed composition grammar the
  standing section sanctions for composed evidence. The cone is
  closed transitively: it SHALL contain every log span the
  finding's replay reads, across every citation, to the depth
  replay actually touches — completeness is decidable by the
  replay itself, and a replay that reaches for a span the cone
  lacks convicts the cone as short. A fresh verifier needs
  exactly one entry point held in advance: the gAID. Everything
  else arrives as committed bytes verified against it.
- **Warranty** — a signed attestation of a computed finding,
  emitted under a pinned lens: evidence about a judgment, never
  the judgment. Replay-falsifiable by construction. Its substrate
  lineage is the endorsement — a non-controller signature
  attesting a view of committed bytes — refined by two
  obligations: the lens is pinned, and the attested finding is
  recomputable.
- **Colored evidence** — any committed evidence object traveling
  with its color-computation inputs: the colorless base (valid to
  every governance-blind consumer), a committed view echo, and a
  lens citation; optionally a claimed color as warranty. The color
  itself never travels: it is computed at each consumer under that
  consumer's committed rule-set — one object, many lawful colors,
  colorless in the commons.

**Object typing.** An edict's content SHALL be a bare
self-addressed data item, never an issuer-bearing credential
container — an issuer field smuggles a spine, and authority lives
in the anchors. A warranty SHALL be a schema-typed, registry-bound
attestation in the substrate's credential discipline — typed by
schema identifier, revocable through its registry, its lens cited
by edge. Requirement elements in typed requirement sets SHALL
name their required schemas by schema identifier in the same
discipline. Object forms typed this way are consumable by the
substrate's existing toolchain; nothing here requires a bespoke
parser.

**Disclosure posture, confessed.** The cone maximizes
authenticity and auditability at privacy's expense: a fetchable
cone discloses the registry evidence it carries, including
evidence about persons. This is a committed trade, made openly —
of the three properties no protocol maximizes at once,
authenticity ranks first here — and it is scoped: nothing in this
document forbids a deployment profile from adopting the graduated
and redacted disclosure machinery the carriage specification
provides, and a cone span withheld under such a profile is
appraised by the ordinary pending species — an undisclosed span
is a typed requirement, not a defect. The kernel commits the
full-disclosure baseline; confidentiality profiles are deployment
law.


## 6. The finding codomain

### 6.1 The type and its values

Governance appraisal in a GARD returns exactly one type: the
finding. A finding is a judgment over a committed regime that
carries its own ground — the citation, requirement, or proof that
justifies it. A value that does not carry its ground is not a
member of this type, whatever else it may be. This is the Ground
Axiom applied as a typing rule, and it is the load-bearing
decision of this document: because every finding carries its
ground, every finding is checkable by replay, and because every
finding is checkable by replay, judgment composes across parties
that share evidence.

The codomain has four values:

- **affirmed** — the proposition holds over the committed
  evidence. Ground: the evidence bundle and the clause set under
  which it was appraised.
- **defeated(citation)** — the proposition is defeated by
  committed evidence. Ground: the citation of the defeating
  clause or superseding act, together with the defeater's class.
- **pending(typed-requirement)** — the evidence committed so far
  neither affirms nor defeats; the finding names what is missing.
  Ground: the typed requirement set — each element naming its
  requirement kind, its subject, and the clauses that make it
  required.
- **self-convicted(proof)** — the subject's own committed bytes
  contain a contradiction: two voices where its constitution
  demands one. Ground: the canonical proof package identifying
  the contradictory pair. At the key tier, whether a pair bears
  is decided by the substrate's own superseding-recovery rules —
  a lawfully superseding event reconciles rather than convicts.

The same four-valued scheme is instantiated at every tier of the
fold tower: the Kever's acceptance machinery realizes it over key
events, the Tever over registry events, and the Gever over
governance events. The evidence ordering below is stated once and
holds per tier.

This codomain is total over findings returned by an evaluator. It
is not total over everything a governance system may persist:
lifecycle states, seating states, operational conditions, and
evaluator incapacity are not findings, and the separation rule in
section 6.5 excludes them by construction rather than by
enumeration.

### 6.2 Pending species and cure

The pending value is not one state but a family of discharge
species, and their assignment is governed by the following
ratified rule:

> Pending discharge species are assigned to processor branch
> states, not indiscriminately to stores or escrow classes. The
> species are absent, window-open, unresolved-conflict, and
> expired/abandoned. Expired/abandoned means that an operational
> processor has discharged its retained work and re-presentation
> is required. Pending species describe cure paths and are not
> additional terminal findings. Where an eviction receipt
> exists, it supplies the committed ground for the discharge; an
> unreceipted drop remains an operational observation rather
> than a consumable finding value.

(The amendment's operational vocabulary — processor branch
states, stores, escrow classes — is the evaluator-implementation
grain: a processor is whatever machinery retains work between
appraisals. The amendment's point is that species classify the
committed cure path, never the machinery's private state.)

Each species names its cure: **absent** is cured by the arrival
of the missing evidence; **window-open** is cured when the
substrate's superseding rules no longer admit a superseding event
at the position — for a non-delegated log, the next rotation
fossilizes the suffix; for a delegated log the window closes only
when no lawful superseding rotation remains admissible under the
substrate's delegated-recovery rules, which stay open longer (the
substrate's own recovery calculus is the decision procedure;
recovery windows are typed by this species, not by a new value); **unresolved-conflict** is cured by an owned act of
the party whose conflict it is; **expired/abandoned** is cured by
re-presentation. A pending finding SHALL carry the species of
each of its requirement elements. A processor's silent disposal
of retained work MUST NOT be represented as a finding: until a
committed receipt of the eviction exists, the drop is an
operational observation, and a verifier that cannot distinguish
"judged absent" from "silently dropped" holds no judgment at all.

### 6.3 The transition system

The finding type is a state machine, and this section is its
complete enumeration — states, payloads, permitted transitions
with conditions, forbidden transitions, and terminality. The
governing rule is ratified verbatim:

> The finding type SHALL enumerate its constructors, required
> payloads, permitted transitions with their conditions,
> forbidden transitions, and terminality. The 3.3 transition
> system embeds without normative alteration at T3. A defeated
> finding SHALL preserve the defeater class and its citation,
> either as explicit fields or through a uniquely re-derivable
> committed referent.

(T3, in the amendment's tier labeling, is the governance tier —
the third rung of the ladder of section 6.4, as T1 is the key
tier and T2 the registry tier.)

**Inputs.** A finding is a function of exactly three inputs: the
committed evidence bundle, the committed law head under which it
is appraised, and the appraisal position. No other input — wall
clocks, local state, operator discretion, ambient configuration —
may influence a finding. Two evaluations of the same triple
SHALL return byte-identical findings.

**Required payloads.**

- A defeated finding SHALL carry its defeater class and its
  citation: the violated or superseding clause's identifier, or,
  for cryptographic defeat, the identifier of the failed
  verification subject. Neither is reconstructible from a bare
  verdict; both MUST be explicit or uniquely re-derivable from a
  committed referent.
- A pending finding SHALL carry its typed requirement set:
  deduplicated elements, each carrying requirement kind, subject
  identifier, and the list of citing clauses, in canonical order
  (subject, then kind, then citing-clause bytes).
- A self-convicted finding SHALL carry the identifier of the
  canonical proof package for the contradictory pair.

**Permitted transitions.** Five edges, each conditioned on
evidence growth:

| From | To | Condition |
|---|---|---|
| pending | affirmed | the requirement set discharges affirmatively |
| pending | defeated | the requirement set discharges by defeat |
| pending | self-convicted | a bearing contradictory pair, or new governed-status evidence (committed
evidence newly bearing on the subject's status under the
governance tier's committed predicates), enters the bundle |
| affirmed | self-convicted | a contradictory pair bearing on the question enters the bundle |
| defeated | self-convicted | a contradictory pair bearing on the question enters the bundle |

**Forbidden transitions.** Seven edges, absolute:

| From | To | Why forbidden |
|---|---|---|
| affirmed | defeated | settled findings do not flip; new defeat evidence yields a new finding at a new position |
| defeated | affirmed | defeat is not un-cited; rehabilitation is an act, not a transition |
| affirmed | pending | evidence does not un-arrive |
| defeated | pending | evidence does not un-arrive |
| self-convicted | pending | a poisoned question does not reopen |
| self-convicted | affirmed | self-conviction is terminal for its question |
| self-convicted | defeated | self-conviction is terminal for its question |

No backward edge exists anywhere in the system: findings move
only in the direction of evidence growth. This is the within-tier
form of the same law that orders the tiers themselves.

**Terminality.** Affirmed and defeated are final except for one
event: the arrival of a contradictory pair bearing on the same
question, which moves either to self-convicted. Pending is the
non-terminal bottom. Self-convicted is terminal for its question
— the question is poisoned, and no further evidence rehabilitates
it.

**The graph form.** Two derivations, stated for the reader who
works graph-wise rather than log-wise; neither adds law. At the
type level, the permitted edges form a directed acyclic graph: no
backward edge exists, so no cycle is constructible, and every
path terminates. At the instance level, a GARD's governance
history — its findings at their positions, with the key-state and
registry-state anchors each finding cites — forms a directed
acyclic graph over the KEL and TEL spine; the GEL is that graph
in log presentation, and the fold is its traversal.

**The evidence ordering.** Findings are ordered by evidence
growth: where one committed bundle is a subset of another,
appraisal under the larger bundle refines and never contradicts
appraisal under the smaller — monotonicity is over the subset
order on bundles at a fixed law head and position, never over
wall time. Defeating evidence is ex-ante enumerable: everything
that could defeat a question is in that question's committed
requirement space before appraisal begins, which is what makes
defeat a citation rather than a surprise. Contradictory pairs
convict only where they bear on the question — duplicity
elsewhere in a subject's history taints that history's standing,
but it does not convert this question's finding. The ordering
forces a discipline on affirmation, stated here so no reader must
derive it: affirmed is reachable only over a bundle that
discharges the question's entire committed requirement space. An
evaluator holding a bundle that leaves any enumerated
defeater-check unexamined returns pending with that check as its
typed requirement, never affirmed — which is exactly what makes
the ordering monotone, since a bundle that could still grow a
defeater is, by construction, a bundle that has not discharged
the space.

**Canonical selection.** Where multiple defeats are simultaneously
available for one question, the finding SHALL cite the
lexicographic minimum of (defeater-class rank, citation
identifier, subcode). Two verifiers holding the same bundle
SHALL emit the same defeated finding down to the byte. The
defeater classes are enumerated and ranked, in this order,
carried from the predecessor unchanged: **crypto** (a
cryptographic verification failed), **authority** (the actor
lacked the invoked power), **merit** (the content violates a
committed clause), **superseded** (a later lawful act displaced
the subject). The subcode is the defeat's discriminator within
its citation, assigned by the cited clause's own committed
enumeration; where the clause defines none, the subcode is empty
and orders last.

### 6.4 The duplicity ladder and the two currents

Duplicity is one crime with a rising voice unit. At the key tier,
it is two events at one coordinate of one KEL. At the registry
tier, it is two registries where committed law demands one chain
— no fork appears anywhere; the crime is visible only to a fold
that reads the KEL as a registry of registries. At the governance
tier, it is contradictory enactments under one committed
predicate — visible only to a Gever evaluating the corpus. Each
tier's duplicity is structurally invisible to the machinery of
the tier below, which is why the tower has three rungs and not
one.

Findings cascade between tiers in two distinct currents, and a conforming evaluator SHALL NOT merge them:

- **Defeat annihilates upward.** A defeated finding at a lower
  tier voids what was built on it: an invalid seal voids the
  issuance that cited it, which voids the enactment that
  consumed the issuance. The dependents were never valid;
  annihilation is discovery, not change.
- **Duplicity taints upward.** A self-conviction at a lower tier
  does not un-happen the history above it: committed history is
  monotonic, first-seen survives, and what was affirmed above
  converts to contested standing rather than to nothing. The
  subject's voice is poisoned going forward; the record it
  already made remains a record.

Breach and duplicity remain distinct crimes at every tier:
defeated is conviction by another's citation; self-convicted is
conviction by one's own committed pair. No clause of this
document blurs them. One force distinction likewise binds:
key-tier duplicity convicts in the medium, for every verifier,
under no frame's law. Registry-tier and governance-tier
duplicity are law-relative — they convict only within frames
that committed the violated predicate, and a frame that never
committed the predicate SHALL consume them as evidence, never as
conviction. Extending the
substrate's word up the tiers does not extend the substrate's
force.

### 6.5 The separation rule

The codomain's totality claim survives contact with real
governance machinery only because of the following ratified
separation:

> A Gever evaluator returns findings over a committed regime. It
> does not ratify composition rules, seat or re-seat
> authorities, advance governance lifecycle, or supply missing
> acts. Those are constructor operations. Where evaluation would
> require an uncommitted ordering or composition rule, the
> evaluator SHALL refuse the invocation and SHALL NOT legislate
> the missing seam. Lifecycle, seating, evaluator-incapacity,
> operational, and mixed constructor states are not members of
> the finding codomain merely because they are persisted judgment
> machinery. Compound evaluator results SHALL preserve their
> component propositions and grounds as a product rather than
> collapse them into a fifth scalar shape.

The refusal clause deserves its plain statement: when two
committed authorities meet with no committed rule for composing
them, the evaluator refuses the invocation. Refusal is not a
fifth finding value — it is the evaluator declining to answer an
ill-posed question, recorded as an operational fact. An evaluator
that invents an ordering to avoid refusing has legislated, and an
evaluator that legislates is a constructor wearing the wrong
name. The amendment's compound-product rule, restated as
derivation: each component of a compound question preserves its
own proposition, ground, and transition system in the product;
the amendment's SHALL, quoted above, is the binding form.


## 7. Standing

Standing is the judgment of authority: whether a party, at a
position, holds a given power under a GARD's Constitution. This
section commits the one rule from which every standing judgment
derives.

**Registry state is evidence. Standing is judgment. The committed
covenant set is the function between them.**

A TEL answers exactly one question: what is the committed state
of this registry — issued, revoked, superseded, at which
positions. It does not answer whether the credential's holder may
act. That answer exists only under a committed covenant: the
GARD's Constitution names which schemas, issued by which
registries, under which expiry and supersession semantics, confer
which powers. Issuance status alone — the registry says issued —
is never standing; it is the evidence over which the standing
covenant computes. A relying party that treats registry state as
authority has skipped the law and trusted the ledger.

In the vocabulary of institutional fact (Searle's construction,
cited): committed registry state counts as standing only within
the context the covenant constitutes. The formula is the whole
doctrine — the "counts as" is computed, the context is committed,
and both are replayable.

Standing judgments are findings and inherit the full machinery of
section 6: a standing question returns affirmed, defeated with
citation, pending with typed requirement, or self-convicted; its
transitions obey the same edges; window-open standing during a
recovery window is the pending species doing its ordinary work.

**Composed evidence.** Where a standing covenant requires
compound evidence — endorsements from several seats, a quorum of
qualified issuers, nested any-of and all-of conditions — the
composition rule MUST itself be committed, and it MAY be
expressed in the ACDC edge grammar as profiled by the dossier
specification's threshold operators: edge groups whose operator
field carries a weighted threshold
over slotted references, each slot naming the schema its evidence
must satisfy (the ACDC operator conventions, as profiled in the
dossier specification; cited, not restated). A committed edge
operator is a composition rule the evaluator consumes; the
evaluator supplies none — this is the refusal clause of section
6.5 read constructively: refusal fires where composition is
uncommitted, and the operator grammar is the ecosystem's
committed way of expressing it. The threshold algebra is one algebra at both
ends of the system — the same weighted-threshold satisfaction
that governs key-event signing governs evidence sufficiency —
so a verifier that can evaluate a rotation can evaluate a quorum
of endorsements (a derivation from the substrate's design, not
new law). An unsatisfied operator group is not a defect and not
a defeat: it discharges as a pending finding whose typed
requirement set enumerates exactly the unfilled slots — each
element naming the slot's required schema, its expected issuer,
and the citing clause — so the cure path for insufficient
composed evidence is readable off the finding itself.

The vocabulary of consequence within a GARD is evidence,
liability, and standing (the jural correlatives, Hohfeld cited):
a power held is a liability borne by its counterparty; a standing
withdrawn is evidence preserved. This document specifies no monetary consequence for breach.

The Gever consumes standing when appraising enactments: an
enactment is lawful only if its author held the enacting power at
the enactment's position under the Constitution then in force.
The chain is explicit — key state authenticates the voice
(Kever), registry state evidences the qualification (Tever), the
Constitution confers the power, and the finding records the
judgment with its ground. Every link is committed; every link
replays.


## 8. The seal ladder

A seal is a commitment planted in a committed log. The kinds
differ by what they commit to, and a verifier that confuses the
kinds verifies nothing. The substrate's seal grammar ships more
kinds than this section names — digest seals, Merkle-root seals,
event and source couples, a latest-establishment seal, a generic
typed seal — and this standard's first two categories subsume
the byte-shaped and coordinate-shaped members of that table,
cited, never renamed. One substrate kind is expressly out of
scope: the latest-establishment seal, which commits to current
key state as such; no construct of this document consumes it,
and its adoption is future work, not implied. The third kind is
this standard's extension; a fourth is deferred by rule.

**Digest seal** (substrate vocabulary). A commitment to exact
bytes. Verification: recompute the digest over the presented
bytes; equality or failure. The digest seal answers "are these
the bytes" and nothing else.

**Event seal** (substrate vocabulary). A commitment to an event
at a log coordinate. Verification: resolve the coordinate in the
committed log; compare identifiers. The event seal answers "is
this the event at this coordinate" and nothing else.

**Covenant seal** (extension). A commitment binding a subject to
the GARD's covenant set — to standing law, not to another object.
Verification is neither byte equality nor coordinate lookup: the
verifier evaluates whether the successor satisfies the committed
clause. A covenant seal on a governance corpus commits its future
— every successor is checkable against the sealed clause set, and
an unsatisfying successor is convictable on the seal's own bytes.
The covenant seal is admissible only where the substrate's law
makes lineage the invariant; where byte equality is achievable,
the digest seal is the honest kind, and substituting the weaker
kind is itself a defect.

Two disciplines bind all three kinds. A seal names its kind:
consumers MUST NOT be left to infer commitment semantics from
context. And a conviction sourced from a seal names the seal kind
it convicts under — a digest mismatch, a coordinate mismatch, and
a clause violation are three different refusals, and a record
that blurs them is unauditable (the conviction-family rule of
section 13 carries this forward).

**Evaluation seal — named and deferred.** A fourth kind is
constructible: a commitment to a verdict — "we ran clause C
against subject X; result R." This document names it and defers
it. No discriminating fixture exists, and a sealed verdict raises
the oracle problem in seal form: the seal is only as good as its
evaluator, and a consumer who trusts the seal has trusted the
evaluator it cannot see. The admissibility rule travels now, as
committed doctrine, so that the deferral cannot drift into
silent adoption:

An evaluation seal is admissible only over verifiable
algorithms: computations any verifier can recompute from
committed inputs to the identical result. Commit
predicates, never verdicts. A sealed verdict a stranger cannot
recompute is smuggled authority, and no construct of this
document consumes one.


## 9. Rotation policy

The medium admits any validly signed rotation; nothing in this
section changes that. What a frame adds is committed law about
which admitted rotations are lawful: a rotation policy is a
SAID-addressed rule-set over the rotations of the frame's own
identifiers — the authority gAID and its seated organs —
committed in the Constitution before the positions it governs —
a rotation policy SHALL be committed before any position it
judges. Policy is commitment, never configuration: a rule adopted after
the position it judges is no rule at all, and a rotation
appraised under law committed before it is the two-layer joint —
substrate admission below, frame appraisal above, one set of
bytes — pointed at the frame's own keys: the substrate admits the
rotation; the frame appraises it; an unlawful rotation is valid
key state and a convictable governance event on the same bytes.
Appraisal of rotations, like all appraisal, returns findings:
a rotation the policy convicts is not thereby unwound in the
medium — it grounds recourse under section 12.

**The degenerate species.** Bare pre-rotation — the substrate's
own next-key digest — is the degenerate rotation policy: one
successor, self-invoked, on no evidence, effective immediately,
defeasible by nothing. Every frame has at least this policy,
because the substrate imposes it.

**The four committed axes.** A Constitution MAY customize
rotation policy along four axes, each a committed clause. These
are the axes this document commits; the design space is not
claimed closed:

- **who may invoke** — from the holder alone to a custodian
  threshold set, the custodians' identities hidden in digest
  until exercised;
- **on what evidence** — from none to a committed ground with
  attestations, in which case the recovery rotation is a grounded
  enactment and inherits all of section 12.1: its ground replays
  or the rotation convicts its invokers;
- **when effective** — from immediately to after a contest window
  measured in log positions, never in wall-clock time;
- **what defeats it** — from nothing to veto by the live keys
  within the window.

Each axis is independently committable, and the policy a frame
adopts is readable from its Constitution by any stranger holding
the cone. Seated organs SHOULD be delegated identifiers of the
gAID: delegation dual-anchors the seat's key events (the organ
signs; the delegator seals), places custodial recovery of a
compromised organ inside the substrate's own delegated-recovery
rules, and gives the charter's delegation strata the substrate's
delegation semantics rather than a metaphor. Where an organ is a
delegated identifier, the who-may-invoke and what-defeats-it axes
are partially discharged by the substrate itself — and the
degenerate policy's "defeasible by nothing" acquires its
exception, since the substrate already imposes a richer policy on
delegated identifiers than on sovereign ones.

**What rotation policy reaches.** Committed rotation clauses give
the frame its relationship to time. Tenure is rotation policy:
seat terms are establishment rotations on organ identifiers, and
a term limit is a clause any verifier can check. Liveness is
rotation policy: a committed cadence turns silence into
committed, dateable absence — and a cadence breach composed with
a recovery clause is the dead-man construction, in which the
missed positions are themselves the terminal procedural finding
that grounds custodial succession. Cryptographic migration is
rotation policy: a clause that by a named position all successor
digests commit to a named suite makes the frame's algorithm
transition a checkable schedule rather than an operational hope.
And recourse
reaches through this section as much as time does: a recovery
rotation invoked by custodians on committed evidence is the
recourse machinery of section 12 enacted in key state itself —
the frame answering compromise of its own authority with a
grounded, contestable, replayable act. Rotation policy is where
the temporal and the judicial reflexes of an autonomic frame
meet. These are illustrations, not a registry: the axes are the
law; the uses are what Constitutions do with them.

## 10. The governed object classes

This section states no new law. It derives, from the sections that
do, the generative rule the frame interior instantiates — stated
once, so that a builder can see the move whole and derive the next
instance without asking.

**The one move.** Every governed object in this document is the
two-layer joint of section 9 pointed at a different substrate
object: the substrate admits X-events by its own mechanics; the
frame commits law, before the positions that law judges, over
which admitted X-events are lawful; appraisal returns findings;
findings ground recourse. "Governed X" never modifies X's
substrate mechanics and never requires the substrate's permission
— it adds committed law above an untouched lifecycle, and the
whole finding and recourse machinery arrives with it.

**The criterion.** X is governable in this document's sense
exactly when three things hold: X has a substrate lifecycle —
committed events with the substrate's own admission mechanics; X's
events authenticate through key state, so admission is
frame-invariant; and X's events have positions, so law committed
before a position can judge it. The criterion excludes as well as
admits: a schema — immutable content under a self-addressing
identifier, with no lifecycle — is not a governable object; what a
frame governs is schema adoption — the covenant content of
section 7, which names the schemas its standing law consumes —
and schema succession (an amendment in the GEL).

**The relation axis.** The move instantiates across relations as
well as objects: law over the frame's own lifecycle
(self-directed); law over a seated organ's (the seat); law over
evidence consumed from strangers (adoption); law under a
federation envelope (peer). The columns are one law at four
distances from the frame's own keys, and computed congruence
(section 11) is the medium-grade measure of the passage from
stranger to peer.

**The classes this document exercises.**

- **Governed key state** — KEL events; its law is rotation policy
  (section 9).
- **Governed seats** — delegated establishment events; its law is
  a Constitution's seating clauses and this document's
  delegated-organ rule (sections 7 and 9).
- **Governed registries** — registry inception and management;
  its law is the covenants of section 7 naming which registries,
  under which semantics, confer what.
- **Governed credentials** — issuance and revocation; its law is
  the standing covenants of section 7.
- **Governed law** — GEL events; the reflexive class, below.
- **Governed attestation** — receipts and warranties; the
  partitioned class, below.

**Governed attestation** is one class with a partitioned interior,
and the availability charter is the partition. Obligated
attestation — witness receipts — is speech the charter binds
before the fact: the duty to speak is committed, propagated down
the delegation strata, and silence against a committed cadence is
itself appraisable evidence. Voluntary attestation — warranties —
is speech no law compels, disciplined after the fact by
replay-falsifiability. Duty-to-speak is governed ex ante;
freedom-to-speak is convictable ex post; the charter is the
committed boundary between the regimes.

**Governed law** is the reflexive class — the facet of the
autonomic property this class supplies: a domain whose law is
administered from outside may be governed; it is not autonomic. The GEL passes the
criterion using itself: amendments and ratifications are committed
events, anchored through the gAID, judged under the Constitution
in force before them. The frame's law is dynamical — the measure
of lawfulness is itself among the objects measured — and the
construction is not paradoxical, because it is positional: law
never applies to itself at a coordinate, only to its successor at
the next, and succession is never retroactive. The recursion's base case is genesis, constructed rather than
judged: the knot in section 3's gAID definition — founding law
computed first, sealed at inception, the identifier excluded from
every pre-identity byte — closes the cycle exactly where no prior
Constitution exists, and the law in force at the first event is
the substrate's own admission rules: the degenerate law every
frame has because the substrate imposes it, in the pattern of
section 9's degenerate policy. Every later event is judged inside
the positional recursion. The forward commitment at the far end
is the same discipline at a confessed lesser grade: as
pre-rotation commits key state to its successor's digest before
the successor exists, the succession rule of section 15 commits
this document to its successor's criterion — criterion, not
digest, and the difference in strength is stated rather than
blurred. Self-description without self-application, at either
end.

**The enumeration is open.** These classes are found by the
criterion, not decreed by this section: a Constitution that
commits law over a further substrate lifecycle has derived the
next instance, not extended this standard. The rows are
illustrations at the grain of section 9's axes: the criterion is
what generalizes; the classes are what this document did with
it.


## 11. The transformation law

Judgment never crosses frames; evidence does. A GARD is a frame of
appraisal, not an authority over others: its findings are valid in
its frame, computed under its Constitution, and carry no force
anywhere else by existing. What is invariant between frames is the
medium — key state, committed bytes, and duplicity, which every
verifier in every frame computes identically. What crosses frames
is committed evidence: log spans whose authentication is
frame-invariant. What the receiving frame does is compute its own
judgment over that evidence under its own committed law. Force is
frame-local; evidence is frame-invariant; recognition is the
committed act that connects them.


### 11.1 The two relations


**CONSUMPTION — unilateral.** Frame B consumes frame A's edicts as
evidence under B's law. Adoption SHALL be committed: B's
recognition of any regime of A's is an event in B's own GEL,
naming what of A it recognizes (which registries, which schemas,
which law heads) and under which lens; thereafter B's
evaluator computes findings over A's artifacts exactly as over any
committed evidence — A's Kever-state authenticates A's voice; B's
Constitution decides what the authenticated evidence confers in B.
A cannot prevent consumption and need not know of it. No threshold
of consumption by others binds any frame that never committed to
it. Consumption confers evidence-weight, never force.

**FEDERATION — bilateral.** Frames A and B grant each other's
edicts standing-conferring force inside their own frames. Type:
the matched-anchor envelope — A's GEL commits a recognition event
citing a shared rule-object SAID; B's GEL commits the same
rule-object SAID; the bond exists iff both anchors verify and cite
the same object. The bond binds at join-reached: it exists
exactly at the coordinate pair — A's recognition event at its
coordinate, B's at its own — computed by any verifier holding
both spans, decided by no one; discovery order is
observer-relative and consulted by nothing. Either
side exits unilaterally by its own committed act; neither can
fabricate the other's consent. Force crosses only through the
envelope, and only as far as the shared rule-object commits.

One alternative is disposed of on the record: the substrate can
express a joint commitment as a group identifier — one
multi-signature identifier whose single committed event both
parties sign. For federation it is rejected on the stated
constraints: a group identifier is a new authority whose key
state sits above both parties, which is the super-frame this law
forbids, and exit from it is a key-state operation a counterparty
can contest rather than a unilateral committed act. The envelope
keeps sovereignty where the constraints demand: two anchors, two
logs, no shared spine.

**Larger figures.** A federation of n frames is n(n-1)/2 bilateral
envelopes citing one shared committed instrument — the instrument,
never any collective act, is what makes it one federation (the
composition shape; conjecture-with-fixtures, cited at grade). No
super-frame exists; no envelope creates an authority above its two
parties.


**Computed congruence.** Where two frames' committed law shares a
fragment, the overlap is measurable at two grades, and the grades
never blur. Digest congruence — clauses equal by self-addressing
identifier — is medium-grade: any verifier holding both
Constitutions derives it from committed bytes by the medium's own
machinery. Predicate congruence — rules of one Constitution that
another's committed rules satisfy — is an evaluation, not a
medium fact: it is computable only under a stated lens, this
document commits no canonical comparison algorithm, and a
verifier asked to compare at a seam its lens leaves uncommitted
refuses rather than legislates. No fixture yet exercises either
computation; predicate congruence in particular travels at
conjecture grade in this standard's record, its fixture
obligation attached. Congruence of either grade is evidence,
never force. It confers nothing — no standing, no adoption, no
recognition follows from overlap by existing — and it operates
only at the margins of the relations above: it informs whom a
frame adopts, where an envelope is worth its ceremony, and what
shared rule-object already lies latent as the measured overlap.
It enters no ceremony and waives no committed act. Envelopes
crystallize along congruence; diplomacy starts from a measurement
rather than a blank page.

### 11.2 The transformation


Given an edict E of frame A and a consuming frame B with a
committed adoption of A's relevant regime:

1. **Authenticate** (medium, frame-invariant): B MUST verify E's
   anchoring event against A's key state — signatures, coordinate,
   witness receipts per A's availability charter. This step is
   identical in every frame; it is the substrate's own admission
   machinery, and its verdict does not depend on B's law.
2. **Resolve** (medium): B MUST fetch E's verification cone —
   presented as a verifiable dossier where the producing frame
   carries it across the boundary — and MUST verify every SAID it
   cites. Wrong bytes convict on arrival; the name is the
   verification. A dossier whose composition warranty fails
   convicts its curator without touching the edict's own
   standing: carriage liability and content judgment never
   blur.
3. **Appraise** (frame-local): B's evaluator SHALL compute its
   finding over E as evidence under B's own Constitution and
   committed adoption lens, and under nothing else: affirmed, defeated with citation, pending with typed
   requirement, or self-convicted. Composed-evidence requirements
   in B's adoption covenant may be expressed in the substrate's
   edge-operator grammar; an unsatisfied group discharges as
   pending, its requirement set enumerating the unfilled slots.
4. **Confer** (frame-local): what the finding confers in B —
   standing, admissibility, nothing — is B's Constitution's
   decision alone. Under a federation envelope, conferral follows
   the shared rule-object; under bare consumption, conferral is
   whatever B's law says evidence of this color confers.

Steps 1-2 are the invariant half: every frame computes them
identically or the medium itself is broken. Steps 3-4 are the
covariant half: they differ by frame lawfully, and the same edict
lawfully carries different colors in different frames
simultaneously.


### 11.3 The verification regimes

Both relations resolve, at the consumer, into one of two ways of
checking — one discipline between them:

**Replay-native consumption.** A verifier holding the committed
logs and the committed rule-set recomputes the finding: same
evidence bundle, same law head, same position, byte-identical
result. This regime needs no trust in the producing GARD at all —
the finding is checked, not believed. Replay-native verification
is always available to any party the availability charter
reaches, and its permanent availability is what disciplines
everything else.

**Warranted consumption.** A consumer MAY instead rely on a
signed attestation of a fold-finding — a warranty that the
computation was run and returned this result, emitted under a
pinned lens by a warrantor staking its own committed identity.
A warranty is evidence about a judgment, never the judgment: the
finding remains the computed object, and the warranty adds only
the warrantor's liability for its accuracy. A false warranty is
replay-falsifiable by construction: one honest verifier
recomputing from committed bytes convicts the warrantor on the
warrantor's own signature, in the manner of a confessed judgment.
A false warranty is therefore always falsifiable in principle;
whether the open replaying population effectively disciplines
deployed warranted supply — access, publication, standing, and
consequence operating as a system — is a pending claim of this
standard's record, held to its fixture conditions, and this
document does not assert it.

Color is computed, never asserted. A receipt, an attestation, or
any evidence object acquires its governance meaning — its color —
as the output of a committed rule-set evaluated over committed
bytes at a committed position, and an issuer's asserted color is
merely more evidence for that computation to judge, including
evidence of the assertion's own falsity. The colorless base
remains valid to every consumer that ignores governance entirely:
a validator that knows nothing of GARDs parses and verifies the
same bytes unharmed. Adoption of a coloring regime is a committed
act of the adopting party — no threshold of attestations makes a
coloring ambient, and no party is subject to a regime it never
committed to.

The scale economics of these regimes — when warranted consumption
is necessary rather than convenient, what replay costs at
deployment scale — are stated in this standard's record as
open questions with committed fixture obligations, and this
document claims nothing about them. The construction stands on
its own: replay disciplines warranty whether or not warranty is
ever economically necessary.


### 11.4 The discipline


No authority ranks frames. The discipline between them is mutual
convictability over the shared medium:

- **Cross-frame duplicity.** A frame that speaks with two voices —
  to two counterparties, at one committed coordinate — is
  convictable by anyone holding both logs. The conviction is
  frame-invariant: it is computed in the medium, not under any
  frame's law.
- **False-warranty conviction.** A warrantor whose attested
  finding diverges from replay is convicted on its own signature
  by any verifier that recomputes. Warranted consumption is
  disciplined exactly because replay-native consumption never
  closes.
- **Envelope breach.** A federated frame that confers force
  outside the shared rule-object's commitment, or withholds what
  it committed, has produced committed evidence of its own breach
  — liability under its counterparty's law and its own.


### 11.5 Engine independence


Nothing in this law requires a constructed governance engine.
Steps 1-2 bind to the substrate's own machinery; steps 3-4 bind to
the evaluator's type boundary — its return type, its refusal rule,
its determinism — which any conforming implementation satisfies.
The composed joint — substrate admission and governance appraisal
over the same committed bytes — is exercised at fixture scale
against one implementation at one pinned checkout, and nothing
wider is claimed, while the engine interior remains open by
confession. The transformation law
is the reason the open interior does not leak: everything that
crosses frames is defined at the boundary.


## 12. Recourse

A finding is a judgment; recourse is what a frame lawfully does
about one. This section closes the arc the first section opened.
The substrate commits detection and its own key-layer recovery,
and is silent above them — and a framework that adds judgment but not
consequence has only moved the silence one layer up: evidence
committed, findings computed, and the act that answers them still
improvised. What converts a governance framework into an
autonomic one is exactly this capability. Within its perimeter,
an autonomic frame detects, judges, acts, and incorporates the
act into its own law, with no external enforcer anywhere in the
loop — the facet of the autonomic property recourse supplies:
without this loop, judgment is computed but consequence remains
administered.

Stated concretely before any machinery, because the word
"recourse" carries courtroom weight it does not need: recourse is
consequence as computation. Issuance and revocation become
programmable — not in the sense that software fires them, but in
the sense that their lawfulness is a function any verifier can
run. A credential is issued because its covenant's requirement
set discharged, and the issuance carries that ground; a standing
is revoked because its ground failed replay, and the revocation
carries the failure; a seat expires because its committed term
reached its position, with no one deciding anything; an adoption
is withdrawn citing the finding that defeated it. Each of these
is the same object — a committed act carrying the terminal
finding that grounds it — and this section specifies that one
object and the ladder of relations it may travel. What a GARD
enables is exactly this: consequence that explains itself, in
bytes, to strangers.

### 12.1 The grounded enactment

Recourse is an act, and acts belong to constructors: a recourse
act is an enactment in the GEL, subject to everything section 7
requires of enactments. What distinguishes it is its ground. A
grounded enactment SHALL commit, within its own content: the
evidence bundle it rests on, pinned as a set of digests; the law
head it invokes; the position at which it speaks; and the
terminal finding it claims, stated with that finding's citation.
An enactment presented as recourse that omits any of the four is
not a grounded enactment and confers nothing under this profile.
In committed bytes, the enactment asserts: the fold over exactly
these inputs returns exactly this finding.

Lawful recourse is then two replays, and both are computable by
any verifier holding the verification cone. The ground replays:
an evaluator given the pinned bundle, the cited law head, and the
named position returns the claimed finding. And the enactor was
empowered: the acting party held the invoked power at that
position under the Constitution then in force. An enactment whose
ground fails replay is defeated on its own bytes: the replay
assertion is a committed proposition, this profile makes its
truth a validity condition of the act under an explicit clause,
and one recomputation defeats the act with citation — computable
in every frame that can fetch the cone. Self-conviction keeps its
ratified meaning and is not borrowed here: an enactor whose own
committed bytes contain a bearing contradictory pair
self-convicts; a false ground and a forked voice are different
crimes, and this profile blurs neither. An enactment whose ground
replays but whose enactor lacked the power is convicted by the
ordinary standing machinery. These are the failure modes this
profile models; the enumeration is not claimed exhaustive —
unavailable grounds, malformed ground sets, and evaluator refusal
at an uncommitted seam are open surfaces of the section 14
interior.

Recourse SHALL be grounded only on terminal findings. A pending
finding is a non-terminal judgment carrying its typed
requirement; it cannot ground final recourse, and force applied
to a question still pending is the improvised justice this
document exists to end. Interim measures are not an exception: a lawful
suspension while a question pends is grounded on a terminal
finding about a procedural proposition — that a contradictory
pair exists, that a recovery window stands open — which is
affirmable while the substantive question is not yet judged.

Grounds do not rot. The ground pins its evidence subset and its
position; evidence arriving later may ground a later act but
never rewrites the replay of the claim as made, and because
succession is never retroactive, a recourse act lawful under the
Constitution then in force remains lawful in the record even
after the law that authorized it is superseded.

### 12.2 The recourse ladder

Consequence is graduated by relation, and each rung uses only the
force that relation actually carries.

- **Within the frame** — withdrawal of standing, revocation of
  empowerment, expulsion from a seat: grounded enactments with
  real force, because the perimeter is real. This is the only
  rung where prevention operates.
- **Across a federation envelope** — exit: the envelope binds
  bilaterally and dissolves unilaterally, so recourse against a
  breaching federate is a grounded dissolution event, the bond
  dying with the breach finding attached. No enforcement crosses
  the boundary; none is needed for the bond to end examinably.
- **Under bare consumption** — revocation of adoption, the same
  shape: a committed act citing its recomputable ground.
- **Into the commons** — testimony: warranted convictions emitted
  as evidence, colorless in the commons, colored by whoever
  adopts a lens. Beyond every perimeter, recourse is conversion,
  never prevention.
- **In the medium** — cross-frame duplicity convicts its author
  for every verifier holding the pair, under no frame's law
  (modulo the substrate's superseding reconciliation, per the
  medium section). This rung is not recourse but its evidentiary
  floor: the medium convicts and never sentences, and every act
  taken on that conviction is frame-local and grounded like any
  other.

### 12.3 The final rung: recourse against the frame

The remaining case is the frame itself gone wrong: an authority
that equivocates, enacts without ground, or seals its members out
of the law they are governed by. The architecture's answer is its
own succession machinery taken at face value. The logs are held
by those the frame governs; an authority that speaks with two
voices is convictable in the medium by anyone holding both; and
the remedy is the fork — a successor frame incepted on committed
evidence, citing the predecessor's records and the conviction
grounds for leaving them. The freezability criterion's disclosed fork residue is this
rung's bookkeeping; the criterion itself lives with the
federation duties (section 13). A sovereign cannot be imprisoned, but it can be left —
and in this architecture, leaving takes the proof along.

### 12.4 What this section does not design

This section commits the grounded-enactment profile: what makes
a consequence lawful, what grounds it, how its abuse convicts.
It does not claim the profile exhausts recourse semantics.
Recourse procedure is constructor interior, open by the
confession of section 14: who may initiate, how questions are
scheduled, what hearing or appeal structure a Constitution
adopts — and with them rehabilitation, reliance protection for
parties who consumed a later-defeated act in good faith, and the
deployed effectiveness of consequence, none of which this
document establishes. And the fully
seamless form of the loop — a frame whose entire membership
administers by mutual watching, with no organs at all — is an
open research question this document registers and does not
answer. The loop this section commits is the autonomic minimum:
evidence to finding, finding to grounded act, act to law, law to
the next finding — each step committed, each step replayable.
Within a GARD, evidence is committed and justice is replayable:
the act that punishes carries the proof that it may.

## 13. Federation duties

A frame's judgments travel only as far as strangers can compute
them, and each duty in this section either exists
because a step of the transformation law fails without it, or
states its own forcing ground where it derives from standing or
the charter's serving surface: names must resolve in one
hop or resolution stalls; evidence scale must be stated or a
claim borrows credibility it never earned; the availability
charter must hold or the verification cone is unfetchable;
conviction kinds must be named or the discipline cannot tell a
format refusal from a law conviction; interpretive latitude must
be confessed or two conformant verifiers diverge in silence; and
custody and freezability must be committed or the frame's own
continuity is ambient. The reference case throughout is the
governed protocol, as defined in section 3.


**Naming.** A federated GARD's traveling vocabulary is its
committed vocabulary: the names this document ratifies. Each name
resolves one hop to its minting artifact through the notation
register — a companion artifact whose digest the ratification
enactment SHALL pin beside this document's own. Open names SHALL
NOT travel as settled terminology; a name still under co-ripening
is confessed as such wherever it appears.

**Stated evidence scale.** Every claim in a governed corpus rests
on evidence that was gathered at some scale, and the scale is
part of the claim. A transition law exercised in a fixture — a
purpose-built world of test identifiers, one implementation, one
pinned checkout — is proven exactly there and nowhere larger.
The same law running under production custody, real witnesses,
and adversarial load is a different claim, resting on evidence
that does not yet exist. The federation obligation is honesty
about which of these a traveling claim carries: a claim SHALL
name the scale of the evidence behind it, and a claim that
borrows the credibility of a scale it was never exercised at is
a defect of this document, reviewable as such. Concretely, for
this document itself: every executable claim herein was
exercised against one implementation at one pinned checkout,
with purpose-built identifiers; no claim herein about witness
behavior, deployed operation, or independent implementations
carries a discriminating record, and none is made.

**Custody plurality.** Custody of a GARD's authority keys is
profile-plural: this document ratifies no default custody
posture. The custody profile a GARD adopts SHALL be committed in
its Constitution, and no single-custodian profile is presumed —
however convenient — as the unmarked case.

**Freezability.** A GARD MAY freeze — close its succession — only
under the five-part criterion, all parts satisfied: its promised
acts are completed or decidably dischargeable; its domain or its
successor is closed; no unresolved horizon of same-identity
questions remains; its fork residue is disclosed; and its
succession latency is acceptable to the parties its freeze binds.
Decidable-completeness alone is not freezability.

**Conviction kinds.** Every conviction a federated GARD emits
SHALL name its kind within the governance canon violation family:
a canonical-form violation (the bytes fail the committed corpus
form — ordering, corpus identity) or a GARD-law violation
(well-formed bytes whose content violates a committed clause).
The two kinds never blur: a form conviction is not a law
conviction, a law conviction is not a parse failure, and every
finding retains its position, its defeated clause, its
verification grain, and its committed law head. A conviction
record from which the kind cannot be read is unauditable and
therefore not a conviction record.

**The availability charter.** A federated GARD SHALL carry an
availability charter: a committed obligation that the key state
and evidence its judgments depend on remain available and
receipt-consistent, at every stratum of its delegation tree. The
charter binds obligations over logs — availability of the KELs,
TELs, and GEL a fold must read; receipted consistency of what has
been made available — and each stratum's witnesses are the
mechanism that discharges it. Delegated authority carries the
charter down with it: a stratum that sheds its availability
obligation sheds its delegated standing with it. The charter's temporal half is
cadence: where the Constitution commits a rotation cadence for
the frame's identifiers, the charter's guarantee extends from
fetchable logs to a dateable frame — silence against a committed
cadence is not absence of news but committed, positionable
evidence, appraisable like any other. The charter
never enumerates observers beyond the witness sets it obligates:
an enumerated observer set is a witness set by definition, and
the deterrence value of unenumerated observation survives only
while the observers are unenumerated. The admissibility profile
for evidence arriving from unenumerated observers is a committed
deliverable of the deployment lane, and no clause of this
document presumes it settled.

**Request authentication.** The charter obligates a serving
surface — strangers fetch cones, consumers query registries,
federates exchange recognition evidence — and every consumption
path is a request at a host. Authentication of those requests,
with its replay-attack taxonomy and cache-window discipline, is a
committed deliverable of the deployment lane, and the substrate's
own request-authentication mechanism is the design of record for
it, cited, not restated. One boundary binds here:
transport admission MAY be wall-clock-windowed; appraisal
position MUST NOT be — the timeliness of a request and the
position of a finding are different layers, and no clause of this
document reads transport time into evidence. Discovery of the
charter's endpoints rides the substrate's out-of-band
introduction machinery, cited at the same grain.

**Interpretive latitude.** Where the substrate's behavior was
never committed as law, two conformant verifiers can diverge
without either lying. This uncommitted interpretive latitude —
the ambient freedom this standard's record names and scopes — is
confessed, not cured, by this document: the encoding layer is
closed (a serialization either parses canonically or fails), but
semantic latitude above it (threshold derivation defaults,
receipt-race edges, escrow retention) remains open wherever the
substrate's own law is silent. A federated GARD SHALL state which latitude it has closed by
committed profile and which it inherits open.

**Travel posture.** This duty's forcing ground is standing, not
a transformation step: a claim traveling as a defect report or an
allocation request borrows an authority over the receiving corpus
that the traveler does not hold. Nothing in this document SHALL
travel as a defect report, an allocation request, a custody
selection, or an extension proposal against any substrate or
ecosystem corpus before an authoritative answer from that
corpus's own custodians. Questions travel as questions.


## 14. The openness clause

This document tells the reader where its own design ends. The clause carries keyword force: prose anywhere in this
document or its companions that implies design beyond the
boundary stated here SHALL be treated as a defect of that prose,
reviewable and repairable as such.

**What is fixed.** Six commitments bound the governance
evaluator, each carried by ratified text in this document: the
evaluator's return type is the four-valued finding codomain and
nothing else; at an uncommitted composition seam the evaluator
refuses rather than legislates; no backward edge exists in the
transition system; defeat annihilates upward while duplicity
taints upward, and the two currents never merge; acts consumed as
grounds require committed receipts — an unreceipted operational
drop is never a finding; and the transition system is explicitly
and completely enumerated. These six are walls: evidence-ruled,
fixture-exercised, and binding.

**What is open.** The interior they bound is undesigned, and this
document does not design it: evaluator scheduling, constructor
architecture, composition-rule authorship, seating procedure, the
act-registry design, receipt transport, the deployment
realization of observation, and the general algebra connecting
these parts, together with the carriage encoding of this
document's object classes — a committed deliverable whose default
posture is the substrate's native composable attachment grammar
rather than document envelopes. The interior is assigned to
review by others, entering as findings, never as edits. A reader who infers a completed construction from the
six walls has inferred more than this document states, and the
inference is the reader's.

**What is unresolved.** Three questions this standard's record
raises are explicitly unresolved, stated here with what would
resolve each. Whether a committed finding of undecidability is
itself a finding or a record of evaluator incapacity — resolved
by a fixed proposition, a named bearer, a committed ground, and
an explicit terminality rule. Whether cross-order proof export
generalizes beyond the refusal rule — resolved by a committed
composition rule naming the proof consumer and bearer, or by a
committed refusal record showing no well-formed invocation
exists. And whether a contradictory pair combined with a
recoverable processor state splits cleanly into its evidentiary
and operational components — resolved by exhibiting the split on
committed bytes. Drafting that implies closure of any of these
three is defective by this clause.

**The observation premise.** Completeness of view is never a
committed property of any enumerable party. What a fold decides,
it decides over the evidence actually surfaced: the availability
charter commits a floor under that evidence, and whatever
unenumerated observers surface arrives as surplus above the
floor. The total view is a join no single party holds — the
ordinary condition of a distributed system, stated here once so
that no decidability claim in this document reads as a claim
about omniscience.


## 15. Succession and ratification

Custos 3.3 is the document of record this document supersedes,
and its bytes are pinned: sha256
18b0469e731db24f6bca45525828e4417751929306ea21e09977088e08a20ceb,
computed over the predecessor's complete committed byte stream
(whole-file preimage, no placeholder, verified by round trip at
this document's assembly). It remains byte-immutable: nothing in
it is edited, and its ratified findings retain their positions
and their grounds. This document replaces it whole, by succession
— the same discipline this standard imposes on every governed
corpus, applied to itself.

Ratification of this document SHALL be an enactment: an event in
the GEL, anchored through the authority gAID's key state, citing this
document's exact bytes by digest. The ceremony's operational
sequence — assembly, ratification, effectuation — produces
committed events; the ceremony's circumstances remain outside the
ratified bytes. On effectuation, this document's clauses are the GARD's law for every position at
and after the effectuation coordinate, and SHALL bind no position
before it: succession is never retroactive.

The ratification anchoring is stated at its true grain:
ratification is anchored in a device-held key event log, and the
materialization of the authority identifier's establishment
lineage — the committed local bytes from which a fresh verifier
reconstructs the gAID's key state with no ambient store history —
is a committed deliverable that follows this document rather than
preceding it. Until that reconstruction replays, locally
re-derivable authority establishment remains unverified, and this
document says so rather than presuming it.

Two further committed deliverables are acknowledged and not
discharged here: cross-implementation interoperability (two
independent implementations deriving equal corpus identities,
admission sets, refusal grounds, and cited law heads from one
committed corpus in both presentation orders) and the
authority-lineage materialization above. Both are debts of the
program, on the record, with their discharge criteria stated;
neither blocks this document's ratification, and this document
makes no claim that either is done.

This document MAY itself be superseded, and only by its own
rule: the successor SHALL be ratified as an enactment under the
Constitution then in force, citing these bytes as predecessor.
Succession carries its own integrity controls. The succession
record — predecessor digest, ratifying enactment, and
effectuation coordinate — SHALL be derivable from the GEL as a
detached record, replayable by a stranger holding neither
edition's bytes. Eligibility is latest-unsuperseded: an
enactment is a lawful succession only under the Constitution in
force at its own coordinate, and a ratification whose cited
predecessor was already superseded at that coordinate confers
nothing, however well signed. Where two enactments claim the
same predecessor, the GEL's committed order rules: the earlier
lawful enactment is the succession, and the later travels as
evidence — of error or of duplicity — under the force
distinction of the transformation law. A repository or mirror
of these bytes preserves history; which bytes are law is
computed from the GEL, never read off any mirror. The seal a successor
plants is checkable against this document's covenant set — that
is what the covenant seal is for — and a successor that cannot
satisfy the committed succession clauses is convictable on its
own enactment bytes. What this document does for its subject
domains, it accepts for itself.

