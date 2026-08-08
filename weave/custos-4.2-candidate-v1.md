# Custos 4.2 — Candidate

A standard for governed domains on KERI. Successor edition to
the ratified Custos 4.1 edition of record (sha256
ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05,
ratified at its authority KEL's sequence number 187, effective
at 188), which it consumes whole and supersedes at its own
effectuation coordinate. The ratified Custos 4.0 kernel (sha256
9cefdc5d584289ea8391d8069bca26ea38aa82a34f9ae973d80e4d1b7773f315)
and Custos 3.3 (sha256
18b0469e731db24f6bca45525828e4417751929306ea21e09977088e08a20ceb)
stand superseded through that lineage. Ratified text is never
edited: this edition was computed whole from a committed input
register — the 4.2 input manifest, sha256
74bdb8a0d950d8c7d8454cb7e015642636eae3d8944f954ba1d5e54d2ac950d9
— and every departure from its predecessor is accounted in the
appendix of record.

## Abstract

KERI detects; a GARD adjudicates. KERI ends
at a deliberately drawn line: an honest validator must not trust
duplicitous key state — and nothing follows. Detection without
consequence leaves every consumer of key state to improvise its
own governance above that line, and improvisation does not
compose. This standard specifies the layer that gives detected
facts their consequence under committed law: the governed domain
— a domain whose law is committed to a governance event log, the
GEL; whose judgment is computed from that log by a fold, the
Gever; and whose every act enters the record it is judged by.
The property this yields is replayable governance: any stranger
holding the logs computes the same Constitution and the same
findings, byte for byte, and re-derives every refusal as a
decision from the same committed triple. Through adjudication
a domain acts, and is held to account, by the same committed
judgments.

Replay is the receipt of performed governance — and receipting
by recomputation is work: recomputation proportional to the
record replayed, bandwidth and storage for the verification
cone that carries it. Verification cost is a mechanism property
of this design, stated in engineering units wherever a clause
depends on it. A warranty — a warrantor's committed backing for
a computed finding — stands in for re-folding until any
stranger holding the logs folds again, and one honest
recomputation convicts a false warranty on the warrantor's own
signature. That discipline is the design's claim, stated at the
design's grade: its deployment-scale record — an open replaying
population exercising the credible threat — is a committed,
unfinished deliverable of this standard's record, and no clause
below presumes it discharged.

## Introduction

This document is organized so that the smallest true statement
of the system arrives first. Chapter 1 types the governed domain
in seven primitives — five nouns, two verbs — and exhibits the
smallest domain that satisfies the type; every construct in the
sections that follow is introduced as a named composition of
those seven, and a construct that cannot state its composition
is a defect by this document's own rule. Chapter 2 types what
governed domains hold and exchange — the governed-object
taxonomy on three axes, of which the third, disclosure posture,
is this edition's new coordinate. Sections 3 through 17
regenerate the predecessor's machinery under that discipline:
scope, reading rules, definitions, the medium, the objects that
cross frames, the finding codomain, standing, seals, rotation,
the governed object classes, the transformation law, recourse,
federation, the openness clause, and succession. Section 18
specifies the GEL's committed event grammar, and section 19
specifies the compact receipt form and the three ordered gates
on its use. The appendix of record accounts every departure
from the predecessor edition in three censuses — each delta is
ruled, repaired, or confessed; every predecessor section is
dispositioned; and every carried span is re-examined against
this edition's new commitments. An unexplained entry in any of
the three is a defect in this document, not a liberty of its
drafting.

Normative force is carried by keyworded spans under the reading
rules of section 4. The reader who wants the obligations without
the derivations may read the two chapters, the keyworded spans,
and the appendix of record; the derivations exist so that no
obligation has to be taken on faith.

---

## 1.0 Where this document begins

KERI settles who speaks. An identifier, its key state, the
witnesses that receipt its events, and the duplicity evidence
that convicts a forked log. What KERI does
not settle is consequence: an honest validator must not trust
duplicitous key state, and there KERI stops. Everything beyond
that line — consequence made committed, computed, and replayable
— is what this document founds. KERI detects; a GARD
adjudicates. Adjudication names the office of the whole domain —
judgment by its fold, act by its constructors — never a license
for the one to do the other's work.


## 1.1 The smallest governed domain

Before any definition, the whole machine once, in plain
language.

A person incepts a KERI identifier and, in the inception event
itself, seals a one-page rule-set: who may hold a named role,
what a holder of that role may do, and what evidence a claim
must cite. That page is law. The log it enters is the domain's
governance record, and the identifier now speaks for a governed
domain — the smallest one there is: one key state, one page of
law, and the receipts.

A stranger arrives holding nothing but the logs. From bytes
alone she computes the law in force — not by asking anyone, but
by folding the governance record under the key state that
anchors it. Someone asks her: may the holder of credential X
act in role Y? Her computed answer testifies. It
cites the sealed page, the credential's registry state, and the
key events that authenticate both. Four answers are possible,
and each carries its ground or is no answer at all: affirmed,
when the committed evidence holds under the page; defeated, with
the citation of the clause or superseding act that defeats;
pending, when the evidence committed so far neither affirms nor
defeats — the finding names the typed requirement that would
discharge it; and self-convicted, when the subject's own
committed bytes contradict each other — the finding carries that
proof. And there is one thing her answer is never: where no
committed rule makes the question evaluable at all — not
missing evidence under a rule, but a missing rule — she refuses
the invocation. The refusal is not a fifth kind of finding; it
is her declining an ill-posed question, recorded as an
operational fact. She does not guess, and she does not
legislate.

Later, the person amends the page. The amendment is a committed
event like any other: it enters the same log, sealed under the
same key state. Every judgment after it folds under the amended
law; every judgment before it folds under the old — and both
remain recomputable by anyone holding the logs, forever. The
law changed lawfully, in the open, in the very record a judge
must read.

That is the whole standard. Five nouns — the log, the fold, the
finding, the seal, the succession — and two verbs. Everything
else in this document is composition.

## 1.2 The five nouns

**Log — committed evidence.** An append-only record of
committed events, anchored so that its integrity and authorship
are KERI's to prove. A governed domain reads three: the KEL,
which commits key state; the TEL, which commits registry state;
and the GEL, which commits law — constitution, amendment,
seating, enactment. The GEL is a TEL-shaped log with governance
semantics: its events are sealed into the anchoring KEL by the
same discipline KERI's registry layer uses, and this standard
introduces no new anchoring pattern. What the KEL is to keys
and the TEL is to credentials, the GEL is to law. A log asserts
nothing; it preserves. Evidence is its entire office.

**Fold — computed judgment.** A pure function from committed
log bytes to computed state. The Kever folds a KEL to current
key state; the Tever folds a TEL to current registry state; the
Gever folds a GEL — in the context of the KELs and TELs it
cites — to the Constitution: the law in force at a position,
and the standing every party holds under it. A fold writes
nothing, ever. Log and fold are one structure read twice: the
log is the committed evidence, the fold is the computed
judgment, and nothing in the judgment may exceed the evidence.

**Finding — the fold's ground-carrying values.** A fold does
not return opinions; it returns findings, and a finding carries
its ground or it is not a finding. The codomain has four
values: affirmed, defeated with the citation that defeats,
pending with the typed requirement that would discharge it, and
self-convicted with the proof from the subject's own committed
bytes. The ground is not an annotation on the value; it is a
component of the type, and a value arriving without it is not a
member. This is the same construction KERI applies to key
state, carried one tier up: judgment made replayable rather
than testimonial.

**Seal — a commitment planted in a log.** The instrument by
which one committed record binds itself to another. Three kinds
suffice for this standard, named beside KERI's own seal
grammar: the digest seal commits to exact bytes; the event seal
commits to an event at a log coordinate; the covenant seal
commits a subject to the domain's covenant set — its standing
law — so that every successor is checkable against the
committed clauses, and an unsatisfying successor is convictable
on the seal's own bytes. The covenant seal is
admissible only where exact bytes cannot be committed: where
byte equality is achievable, the digest seal is the honest kind
— the test is decidable — and a covenant seal over
digest-sealable content is itself a defect. A
seal names its kind, and a conviction sourced from a seal names
the kind it relied on. A fourth kind — a sealed verdict — is
named and deferred; its admissibility doctrine travels with the
seal chapter.

**Succession — the fold's law changing by enactment in the very
log the fold reads.** The reflexive loop, and the one place the
tower touches itself. The change is a constructor's act — an
enactment committed to the GEL like any other event; the fold
never writes, it reads the successor law the enactment left.
The Gever folds the GEL; an amendment to
the law is an event in the GEL; therefore the fold's own
transition rule is amended through the front door — as a
committed, sealed, replayable event in the record the fold
reads, subject to whatever the law in force requires of
amendments. Nothing about the loop is exempt from itself: a
ratification is an enactment, an enactment is judged under the
Constitution it amends, and the judgment is a finding like any
other. Succession is what makes a governed domain a living
order rather than a filed document.

## 1.3 The two verbs

Every actor in a governed domain performs exactly one of two
verbs, and no object in this standard performs both.

**Evaluate.** The fold's verb. An evaluator reads committed
bytes, computes state, and returns findings. Where committed
evidence runs short under a committed rule, its finding is
pending, naming the typed requirement that would discharge it.
Where no committed rule makes the invocation evaluable at all,
it refuses — and the refusal is not a finding but an
operational fact: the evaluator declining an ill-posed
question rather than legislating the missing rule. An
evaluator changes nothing: it holds no pen, and no degree of
conviction entitles it to one.

**Enact.** The constructor's verb. A constructor changes a
domain's state: it ratifies law, seats authorities, advances
lifecycle, commits acts. Every enactment is a committed event,
which is to say every exercise of the constructor's verb is
performed onto the record — a constructor cannot act except by
producing the evidence of its act.

The separation is KERI's own controller-validator division
carried up one tier: only a controller writes a KEL; any
validator verifies it; no validator, however convinced, may
write. Every later subtlety in this standard — organs,
warranties, adopted engine strata — resolves by asking which
verb an object performs. Anything that writes is on the
constructor's plane. Anything that judges is on the fold's.

## 1.4 The fold axioms

Five axioms bind every fold a governed domain runs. They are
gathered here as one floor; each is load-bearing elsewhere in
this standard, and none is new to this chapter.

1. **Ground.** A finding carries its ground — citation,
   requirement, or proof — or it is not a finding. The codomain
   admits no bare verdicts.

2. **Replay.** The same committed inputs yield the same computed
   state — and the inputs are exactly three, closed: the
   committed evidence bundle, the committed law head, and the
   appraisal position. No other input may influence the result.
   The log spans a fold reads — the GEL span, every cited
   key-event and registry span — are members of the evidence
   bundle, never a substitute for its completeness. The replay
   is the receipt of performed governance: an enactment's echo
   testifies, and every stranger who folds again has receipted
   that testimony — receipted in the governance-tier sense, the
   act of independent recomputation; replay mints no witness
   receipt and adds no authentication to the original enactment.
   Two domains holding identical committed triples hold
   identical Constitutions. A judgment no stranger can recompute
   is the judge testifying where the record should, and the
   judge's testimony is not a fold output.

3. **Refusal.** Where committed law runs out, the fold refuses
   rather than legislates. The refusal names what is missing.
   Discretion at evaluation time is exactly what replay
   eliminates; a fold that interprets has begun to enact.

4. **No ambient input.** Nothing a fold consumes may be
   underivable from committed bytes. The commitment has three
   faces, stated once here, each carrying its own discriminating
   refusal. Order: any order the fold consumes — of events, of
   clauses, of evidence — is derivable from committed bytes, or
   is proven irrelevant to the result. Membership: every span
   the fold consumes as its log is derivable from committed
   bytes — a stream whose membership cannot be derived is
   refused, never completed by convention. Semantics: every
   external rule-set whose meaning a finding consumes is pinned
   by committed digest — an unpinned semantics is refused, never
   assumed at whatever revision happens to be installed. An
   uncommitted input that affects a finding is a commitment
   without ground.

5. **Monotone layering.** Each fold consumes the output of the
   fold below it — the Gever presupposes registry state, which
   presupposes key state — and no fold writes into any log. The
   tower reads downward and never writes at all.

These five axioms are the common floor of every fold — and they
are a floor, not the whole house. The conforming evaluator
carries seven fixed walls, enumerated once in this edition's
own text — in the openness clause, section 16 — and restated
nowhere: this chapter cites that enumeration and imports
nothing by pointer, because a wall carried by reference into a
predecessor's bytes can be neither read nor repaired in this
document and drifts unowned. Those walls bind with full force;
a fold satisfying the five axioms alone is not yet a conforming
evaluator. Everything a particular domain adds above the walls
— the predicates its law evaluates, the grammar its events
speak, the strata it adopts — is what that domain chose. This
standard specifies the walls and declines to rank the choices:
it types the domain and leaves the taste to the governed.

## 1.5 The Gever's one discontinuity

The fold tower has exactly one discontinuity, and the Gever
sits on it.

The Kever and the Tever fold under law fixed by protocol. Their
transition rules — what a valid rotation is, what an issuance
does to registry state — are constants of KERI itself; no
domain chooses them, and no event can amend them. The Gever is
the first fold whose transition rule is committed data: the law
it folds under is itself in a log, enacted and amendable by the
domain it governs. One column changes in the taxonomy — whose
law? — and everything else is inherited unchanged: the same
anchoring discipline, the same fold purity, the same
ground-carrying codomain.

The consequence is a rule this standard applies to itself: the
standard never enlarges the Gever's public type. What is fixed
is the observable boundary — the codomain and its grounds, the
refusal discipline, the determinism of replay, the walls the
axiom floor names. Behind that boundary, implementations remain
free to grow in capability — scheduling, proof technique,
analysis — and such growth is lawful precisely because it is
unobservable at the boundary: two conforming engines, however
different their interiors, owe byte-identical agreement on the
same committed inputs. When extension pressure arrives at the
type itself, as it will, it is routed to one of two lawful
destinations: into the law, as committed content the existing
fold evaluates, or into an organ, a seated instrument on the
constructor's plane whose acts enter the GEL as events. The
boundary never moves; the interiors may.

Three tests separate the Gever from everything built above it,
and each is mechanical:

- **The write test.** No fold writes into any log. An engine
  that posts — that derives an artifact and commits it to the
  record — is an organ exercising the constructor's verb,
  however analytical its interior. Its outputs are enactments,
  and they acquire force the way all enactments do: by
  commitment, and then by fold.

- **The codomain test.** A component that returns
  ground-carrying findings by evaluating committed law sits
  inside the fold's type. A component that derives new objects
  for commitment — analyses, attestations, derived boundaries
  of any kind — produces evidence. Evidence has no standing
  until committed and folded.

- **The genus test.** The Gever belongs to the tower: it is the
  third fold, cousin to the two below it, and part of what a
  governed domain is. Engine strata a domain adopts belong to
  that domain's law: they sit inside what its Gever folds, not
  beside it in the tower. The tower is typed once, here. Law is
  chosen per domain, forever.

Bounds: this section constrains the standard, not the governed.
It does not forbid any domain any construction; it forbids this
document from absorbing constructions into the fold's type. The
openness clause governs what may be built above; this section
guarantees there is a stable thing to build on.

## 1.6 Color

A governed domain's color is its fold in force: the fold this
chapter types, configured by the committed law this domain
enacted, at this position of its record. Color belongs to the
domain, never to what it judges: evidence does not have a color
of its own — evidence is colored, by the judgment of a frame
that folded it, and the same receipt is lawfully colored
differently by every frame that judges it. Color is the
configured evaluator itself — what this domain can distinguish,
say, and judge — and the Constitution is that color's computed
state: run the fold in force over the committed record and the
Constitution is what returns. One configuration, one output;
the color is the instrument, the Constitution its reading. What
the law binds appears in the Constitution; what the law can
tell apart lives in the color.

Two consequences follow at once. Colors are compared
semantically, never by prose: the comparison runs over the
complete committed inputs of each fold — the committed evidence
bundle, the committed law head, the appraisal position, and the
pinned engine profile of the comparing lens — and asks what
distinctions each fold in force can draw, since syntactically
different clause sets may compute the same distinctions, and
identical law bytes over different committed contexts may not.
Where any such comparison binds a consequence, it is
fixture-work, not reading-work. And color is exactly as
replayable as everything else in the domain: a stranger holding
the logs computes what this domain is able to judge, before
ever asking it to judge anything.

## 1.7 The comprehension gate

This section is normative for this document itself.

The minimal case of §1.1 is expressible in the seven primitives
of this chapter — five nouns and two verbs, standing on the
presupposition that KERI settles who speaks; the presupposition
is ground, not a primitive — and in nothing else. Every
construct this standard introduces after this chapter is
introduced as a named composition of those seven, and the
introducing section states the composition in its own prose. A
warranty is an enactment binding its maker to a finding's
ground. An organ is a seated constructor. A tier is a bound on
which folds can see a structure. Consumption and federation are
relations between domains built from seals and enactments.
Adopted engine strata are law plus organs.

The gate tests two closures, and a failing section names which
it failed. Primitive closure: a section that requires an eighth
primitive has discovered a gap in this chapter's ontology, to
be repaired here by succession — or a prescription in that
section, to be removed there. Law closure: a section may need
no new primitive and still discover a missing axiom, invariant,
or composition rule among the seven; that too is this chapter's
defect, repaired here by succession, never patched silently in
place. What a governed domain is fits in this chapter. What a
governed domain ought to be does not appear in this standard at
all.

---

## Chapter 2 — The governed-object taxonomy

This chapter entered this edition by byte-exact extraction from
the graduated seed (weave/42-taxonomy-chapter-v2.md, sha256
dfd1ddc1a092225470d2e075c0ad7eec55a4d10e892f38501d763212fcd2bd9a,
graduated fit-for-candidate by the round of 2026-07-31): the
chapter body below is the seed's bytes unaltered; only the
seed's draft-status apparatus — its pin-closure header and its
closing status line — is replaced by this integration heading.
The chapter's quoted citations into "4.1" resolve, with their
line coordinates, into the predecessor edition of record, whose
bytes are pinned in section 17.

## 2.0 Where this chapter begins

A verifier confirms that a person is old enough — and learns
nothing else (not the birthdate, not the age itself, not which
authority vouched for the person, not whether the same person
was verified anywhere else yesterday). The confirming answer is
real evidence:
committed, replayable, carrying its ground. Everything the answer
was computed *from* stays undisclosed.

This shape is now a class of legal mandate. Legislatures have
begun to require, in prose, what no prose can deliver: that a
predicate be verifiable without disclosure of its evidence, and
that the authority issuing the underlying credential be barred
from watching it being used (such as Utah's enrolled
digital-identity statutes, which mandate age verification "without
revealing the individual's age or date of birth" and place the
endorsing department under an audit-checked bar on monitoring
presentations; register, byte-grade). A mandate of this class
specifies, without naming them, two properties at once: a
credential whose meaning is computable without being disclosed,
and an issuer structurally outside the computation.

This chapter types the family of objects that can satisfy that
class of mandate. The prior chapter of this standard typed the
governed domain — one identifier, one law, one adjudicating fold.
This chapter types what such domains *hold and exchange*:
credentials, registries, schemas, findings — and the one further
coordinate the mandate class forces into the open: who is
permitted to see the law that gives these objects their meaning.

## 2.1 The minimal case, one step further

The prior chapter's minimal case is one page of committed law
bound to one identifier. Take that founding page and ask a
question the prior chapter never asked: *who can read it?*

The founding page's digest is anchored in the identifier's key
event log — public, undeniable, ordered. But a digest is not the
bytes. Nothing in the anchoring act requires the page itself to
be published. The domain may hand the page to everyone, to a
named few, or to no one, and the anchor stays exactly as
verifiable in all three cases: whoever *does* hold the page can
prove it is the committed one, and no one — including the domain
— can swap it later. Commitment and disclosure were never one
act. They were one act *by default*, and the default was never
examined.

That unexamined default is this chapter's subject. 4.1 already
states the type: "The kernel commits the full-disclosure
baseline; confidentiality profiles are deployment law" (4.1,
920–922). This chapter gives that sentence its taxonomy.

The founding page has a standing name: it is committed law in
the GEL — "What the KEL is to keys and the TEL is to
credentials, the GEL is to law" (4.1, 144–145). Who can read the
page is a question about the bytes of a GEL.

## 2.2 The three axes

Every governed object in this standard is located by three
coordinates, each a fact about the object's relation to a GEL.

**Axis 1 — object class.** What the object is: identifier, log,
credential, registry, schema, finding, warranty — the nouns the
ratified editions already type (4.1 §5–§11), naming which kind
of thing stands in the GEL-relation.

**Axis 2 — governance grade.** How the object's GEL-relation is
grounded: born-governed — the relation sealed at inception (a
born-governed domain's "founding law is sealed at inception",
4.1, 2236–2237); adopted — acquired later, at a confessed lesser
grade (4.1, 2240–2241); or colorless — no relation, substrate
mechanics only. The grade is the mode of the binding, never a
score.

**Axis 3 — disclosure posture.** Who may read the bytes of the
GEL the object is bound to — who satisfies the antecedent of
replay. This axis is new, and the rest of this chapter is mostly
about it — because the first two axes locate an object's
*meaning*, and the third locates who can *compute* that meaning.

The three axes are orthogonal. A credential may be born-governed
and fully public; the same class of credential may be adopted and
disclosed only to admitted parties; nothing in one coordinate
constrains another. A consuming frame weighs all three, exactly
as it already weighs adopted against born-governed: the
coordinates are typed, visible facts about the object, never
grades of virtue. This chapter types the positions; it does not
rank them. Read together, the coordinates describe one
relation; §2.6 states what that convergence amounts to.

## 2.3 Why the third axis exists: color is the domain's, so
meaning has an address

The prior chapter settled where meaning lives. "Color belongs to
the domain, never to what it judges: evidence does not have a
color of its own — evidence is colored, by the judgment of a
frame that folded it" (4.1, 361–364). Under that ruling, a
credential on the wire is committed structure without meaning:
what it confers is computed by the consuming domain's fold, under
that domain's committed law.

That ruling has a consequence the prior chapter did not need to
state. If meaning lived in the object — if the credential carried
its own significance — then meaning would disclose wherever the
object traveled, to every intermediary and every observer,
unavoidably. Meaning that lives in committed law instead has an
*address*: a set of law bytes, identified by digest. And anything
with an address and a digest inherits KERI's oldest
maneuver — commit publicly, disclose selectively. The KEL anchors
the law's digest for the world; the law's bytes move under the
domain's own committed rules about who may hold them.
Verifiability on disclosure; confidentiality by default.

This is a lift of an existing discipline, and the lineage is
cited, not claimed: ACDC's graduated disclosure and chain-link
confidentiality (Smith) already deliver commit-then-disclose at
the credential tier — fields of an issued credential disclose
selectively against a committed schema. What this standard's
regime-side ruling makes possible is the same discipline one tier
up, applied to the law itself: not "which fields of the
credential are revealed" but "which clauses of the meaning-giving
law are revealed." The credential tier discloses *data*
selectively. The governance tier discloses *what the data means*
selectively. The second was not constructible while meaning rode
the object, because there was nothing law-side to withhold.

## 2.4 The disclosure postures

Three postures, named descriptively, typed by who can replay.

**Open.** The law's bytes are published. Any stranger holding the
logs recomputes every judgment — the posture every ratified
edition of this standard has exhibited, and the kernel's stated
baseline (4.1, 920–922). The jury is the world.

**Admitted.** The law's digests are anchored publicly; the bytes
disclose to parties the domain's own law admits. Admission is not
an informal courtesy: it is an enactment, committed in the GEL
like any other governance act, so the register of who may read
the law is itself governed law — amendable only by committed
amendment, replayable like everything else. (The loop is the
standard's signature one: the domain's disclosure rules are
inside the domain's law, so admission acts are adjudicated by the
very fold they grant access to.) An admitted party replays
exactly as a stranger would under the open posture; a
non-admitted party holds anchors, undeniable and meaningless.

**Clause-selective.** The narrowest posture, and the one the
no-disclosure mandate class of §2.0 requires. A finding "carries
its ground — citation, requirement, or proof — or it is not a
finding" (4.1, 240–241), and a ground cites clauses by digest.
Under the clause-selective posture the domain disclosing a
finding reveals *only the clauses its ground cites*: the verifier
checks the cited bytes against the committed digests, confirms
the computation, and never sees the remainder of the
Constitution. The Ground Axiom, ratified as an integrity rule,
turns out to be a disclosure protocol: because every finding
already names exactly the law it used, "reveal what the ground
names and nothing else" is a computable boundary, not a
negotiation.

The age answer of §2.0 is this posture at work. The finding
(affirmed: the age requirement is satisfied) travels with its
ground (the age-eligibility clause, by digest, plus the
computation). The birthdate — evidence consumed by the fold — is
not in the ground and does not travel. A finding is disclosed
*instead of* its evidence; a no-disclosure mandate is discharged
by construction rather than by promise.

## 2.5 Replay under posture: the conditional was always there

The replay obligation is stated in the ratified text as a
conditional: "any verifier holding the logs can recompute every
judgment to identical bytes" (4.1, 603–605). *Holding* is the
antecedent. The obligation binds the bytes — that recomputation
from them is deterministic — and was never a promise that every
party holds them. The open posture satisfies the antecedent for
everyone; the admitted posture satisfies it for a governed set;
the clause-selective posture satisfies it per-finding, for
exactly the span a ground names. No posture weakens the
conditional. What varies is possession, and possession was
always a fact about the audience, not a property of the proof.

Refusal to satisfy the antecedent is itself typed — provided the
asking is committed. A silence is not bytes; it enters evidence
only through the asker's own log: the disputant commits the
demand and its response horizon as an event in a log the fold
can cite, and what the fold then consumes is committed bytes — a
demand of record whose horizon closed unanswered — never an
ambient observation of quiet. A domain that declines to disclose
its law against such a demand has not escaped the system; the
committed, datable fact — this domain, asked at this coordinate,
withheld — stands in the asker's log, and the minimal case
already types such facts: the founding page commits what this
identifier's silence means. Non-disclosure under a committed
posture is lawful and legible; non-disclosure against one is
evidence. Both consequences are computable. Neither is a
prohibition.

One trade is confessed rather than minimized. The open posture's
jury is the world: any watcher can convict a domain of
self-inconsistency from public bytes. The admitted posture
narrows that jury to the admitted set — key-state duplicity
remains publicly convictable (KEL anchors are public in every
posture), but law-level inconsistency is convictable only by
parties holding the law. A narrowed jury is a real reduction in
who can catch a lie, and a consuming frame weighs it as it
weighs the adopted grade: a typed, visible coordinate, weighed
under the consumer's own law. Whether an admission check can be
consulted by the fold without contaminating its closed input
triple (evidence bundle, law head, position — the finding's three
committed inputs, 4.1 §7) is a question this chapter leaves under adversarial
attention, fixture-pending, rather than assuring.

## 2.6 The family, generated: the GEL as ur-element

The governed-X family is not an enumeration. It is generated:
one construction — place the substrate class's interpretive law
in a GEL — applied uniformly, class by class. The ratified edition
already states the move: governed X "adds committed law above an
untouched lifecycle" (4.1, 1459),
and its class roster closes on the matching confession — "These
classes are found by the criterion, not decreed by this section"
(4.1, 1536–1537). The family is the orbit of the substrate
classes under that one generator, and the grid of §2.2 is the
generator's coordinate system: axis 1 the class the construction
is applied to, axis 2 the mode of the binding it produces, axis
3 who may read the law it placed. Each member below is the
construction applied once.

**Governed credential.** An issuance event in a committed
registry, whose conferral is computed by the consuming domain's
fold under committed law, at a declared posture. The ratified
rule — "Registry state is evidence. Standing is judgment. The
committed covenant set is the function between them." (4.1,
1217–1218) — becomes, under the admitted posture, a
confidentiality mechanism: an observer of the public registry
sees that an issuance occurred and cannot compute what it
confers.

**Governed registry.** A TEL whose interpretive law lives in a
GEL: public events, posture-scoped meaning. Existence, ordering,
and integrity are world-checkable; what a registration *means*
is computed under law disclosed at the declared posture.

**Governed identifier.** The prior chapter's whole subject,
restated on axis 3: founding law anchored for everyone, readable
per posture.

**Governed schema.** A SAID-addressed schema (the ACDC
discipline, cited) placed under GEL succession: amendment becomes
enactment, and schema evolution acquires law's replayable
lineage.

**Governed finding.** The clause-selective posture's native
object, per §2.4: disclosed instead of its evidence, carrying
exactly the law it used.

One member of the family is unlike the others, and the
difference is the family's foundation. Every object above owes
its governedness to its GEL-relation; strike the relation and
what remains is the colorless substrate object. The GEL's own
governedness is not conferred by any further GEL — it is
grounded in the medium. The ratified bootstrap states it: the
derivation a verifier needs before admitting the first governance
event "grounds outside the GEL, in the genesis knot" (4.1, 2235)
— founding law sealed at inception under a KEL establishment
seal. The regress terminates there, and that termination is what
ur-element means: the GEL is the one member of the family whose
governedness is not produced by the construction, the element to
which every other member's governedness is a relation. The grid
does not merely use the GEL as one class among seven; the grid
is about the GEL — three coordinates of one relation, whose
fixed point is the relation's own object.

The fold tower carries the same structure, read as directions.
Grounding runs up: key state grounds registry state, and both
ground the law's log — "The tower reads downward and never
writes at all" (4.1, 274–275). Governing runs the other way: the
GEL confers meaning back down onto the registry and key events
the substrate admits without it. The GEL is the turning point,
and the ratified text marks it as the tower's one discontinuity:
"the first fold whose transition rule is committed data: the law
it folds under is itself in a log, enacted and amendable by the
domain it governs" (4.1, 303–306). Below that point, law is
protocol; above it, every governed object is generated.

One consequence is stated here because §2.8 relies on it: a
generated family cannot have been reverse-engineered from any
single instance or deployment — the generator is prior to every
cell it produces, and no cell is load-bearing for any other. The
deletion and substitution tests of §2.8 are a structural
property of the family; the generation theorem is itself the
defense of the taxonomy's neutrality.

Each cell of the grid either already has committed machinery in
the ratified editions or names its gate openly. Conferral-law
vectors and admission-enactment fixtures do not exist yet; the
claims above that depend on them are fixture-pending, and this
chapter marks them rather than presuming them discharged.

## 2.7 From prose regime to computable domain

The mandate class of §2.0 is one member of a wider class this
grid types: an external regime — a statute, a charter, a sectoral
framework — written in prose, enforced by its own authorities,
that already
specifies governed-object behavior without the machinery to
compute it. Any such regime becomes a computable domain at three
commitments, each already typed by the ratified editions:

1. **The regime's canonical text as founding law.** Where the
   text is public canonical bytes, a domain may be born-governed
   — incepted sealing the very instrument that authorizes it —
   and the regime's own authority relation survives the lift
   intact.
2. **The regime's registrable acts as registry events** —
   attestations, licenses, revocations on mature TEL machinery,
   under the ratified registry/standing split: a registration is
   evidence about a subject, never the subject — whatever act
   vocabulary the regime uses, the act records standing's
   evidence and does not constitute the subject — and conferral
   is the consuming fold's computation.
3. **The regime's decision rules as committed clauses** a fold
   evaluates — with any internal hierarchy of values rendered as
   a committed precedence order, so that where clauses conflict
   the evaluator refuses on a missing rule rather than
   improvising one.

The three commitments are the generator of §2.6 applied to a
regime that grew up outside the medium: each gives one class of
the regime's objects its GEL-relation, and the lifted objects
occupy the same grid as every other member.

Where a mandate of the §2.0 class additionally bars the issuing
authority from observing use, the bar is discharged by type
rather than by audit alone: under regime-side color a registered
act carries no meaning of its own, meaning is computed at
the consuming frame, and the issuer is structurally outside that
computation — there is nothing to phone home about. And where
several peer regimes must recognize one another — none above
another — the shape is the federation the inter-frame
transformation rule types (one frame's judgment is the next
frame's evidence, never its command):
bilateral recognition events on their own clocks, no global
chart, no root authority.

One enrolled statutory program is held in this corpus at
byte-grade as the exhibit of this section's class (the register;
the companion). The exhibit's depth — line-cited clause mappings,
its hierarchy-of-values as precedence, its reciprocity horizon,
and this corpus's prior contact with it (the ratified 3.3 carries
a bridge profile in its Annex A.3, recorded as derived from that
program — the mapping is a return visit, not first contact) —
lives in the companion document, which revs on the regime's own
clock, as a companion lawfully may and ratified text never does.

## 2.8 What this chapter does not claim

No deployed domain of the exhibited regime exists; its program is
statute and buildout, and nothing here asserts otherwise. No
conformance vectors yet exercise the admitted or clause-selective
postures; every equivalence claim involving them is
fixture-pending. The posture names are descriptive and may ripen.
The fold-purity question of §2.5 is open and under attack. The
narrowed-jury trade is confessed, not solved. The ur-element theorem of
§2.6 is a reading of ratified text, cited where it stands; it
introduces no new normative machinery. The exhibit is an
exhibit: every normative sentence in this chapter survives its
deletion, and any regime of the typed class substitutes without
altering one (the gauntlet exercises both tests). This chapter
types positions a governed object can occupy; whether any given
occupancy is wise is deployment law, and prescribing it would
violate the law this chapter is written under.

---

## 3. Scope and non-goals


The GARD's defining obligation is replay: a conforming domain
MUST make every judgment it issues recomputable by any verifier
holding its committed logs, equal under the one conformance
predicate of section 17 — semantic full-payload equality today,
byte identity as this standard's forward commitment the moment
a carriage encoding ratifies. That obligation is exercised
today at fixture scale — one implementation, one pinned
checkout — and cross-implementation equality is a confessed
open deliverable; the obligation, not its full discharge, is
what defines the class.

The governed domain and its seven primitives are typed once, in
Chapter 1; the governed-object taxonomy is typed once, in
Chapter 2; and no section below re-presents either: a section
that needs a type cites its chapter, and the boundary with KERI
— drawn in §1.0, detection below it, adjudication above it — is
owned there and redrawn nowhere. After the typing chapter the
document is built medium-first, because its subject is not one
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
  warranty) every crossing uses;
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
standard's record names general-relative, derived in section 12.
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



## 4. Normative language and reading rules

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

2. Digest pins name exact bytes, and this document uses two pin
   kinds, never blurred. A self-addressing pin names bytes that
   carry their own identifier: the pinned preimage is computed
   with the digest's own field holding a placeholder of the same
   length as the encoded digest — the placeholder character is
   the number sign, the substrate's own dummy convention — under
   the substrate's length-parametric rule by derivation code, of
   which forty-four characters, the 256-bit digest class, is
   this document's current profile, and verified by round trip
   before the pin travels. An external whole-file pin names
   bytes that do not carry their identifier: its preimage is the
   published file, whole, headers included. The pin answers
   which bytes; which of those bytes bind is answered by the
   normative-language rule above — two questions, two rulings,
   never one. A digest whose preimage is not stated is not a
   pin; it is decoration, and this document contains none.

3. This document derives; it does not allude. Every doctrine
   stated here either carries its grounds in the same section or
   cites the committed artifact that does. Terms of art from
   other communities appear with their coiner named. The
   predecessor document, the ratified Custos 4.0 kernel, is
   byte-immutable and is cited, never edited — as is Custos 3.3
   through it; this document replaces its predecessor whole, by
   the succession rule in its final section.

**The substrate of record.** The protocol layer this document
builds on is KERI, with ACDC as its credential layer and CESR
as its encoding layer, in the specifications stewarded by the
Trust Over IP Foundation's specification working group; the
same body's verifiable dossier specification is the substrate
of record for evidence carriage, consumed where the objects
section cites it; and keripy is the reference implementation
this standard's executable evidence was exercised against, at
the pinned checkout its record states. The revision of record
for each specification is pinned in the engagement companion
under this document's own pin discipline — a companion this
edition's ratification enactment SHALL pin beside this
document's own bytes — and within this document the substrate
is cited by name and never restated.



## 5. Definitions

**The minimal case.** This document's minimal case is stated
once, in Chapter 1 §1.1 — one key state, one page of law, one log
binding them — and it is not restated here: frame size is nowhere
a parameter of this document's law, nothing defined below
requires more of a domain than that section exhibits, and an
ecosystem-scale authority and a single person's identifier are
the same species at different masses.

The terms defined here do load-bearing work: each is defined
once, and every later use means exactly this. Terms inherited from the
substrate are marked as such and cite their origin; terms this
standard introduces are marked as extensions.

**GARD.** A Governed Autonomic Replayable Domain — the governed
domain Chapter 1 types, under its proper name: constitution,
evidence, and judgments committed bytes under one identifier,
such that lawfulness within the domain is decidable by replay.
"Governed": its law is committed and succeeds only by its own
committed rules. "Autonomic": its identity is self-certifying,
rooted in key state, borrowing no external authority.
"Replayable": the domain's conformance obligation that any
verifier holding the logs can recompute every judgment to
identical bytes — discharged today at the evidence scale the
federation section states.

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
(section 13) is the law of that space.

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
  event's self-addressing identifier — inheriting the KEL's
  duplicity evidence and establishment lineage. The typing
  itself — a TEL-shaped log with governance semantics, no new
  anchoring pattern, law's log as the KEL is keys' and the TEL
  credentials' — is Chapter 1 §1.2's; the GEL's committed event
  grammar — its event types, ilk discipline, and canonical order
  — is specified in section 18.

**The three folds.** Each log has a fold — the pure function
from committed log bytes to computed state that Chapter 1 §1.2
types. The specifications name the logs; the reference
implementation names the folds after the logs they fold, and
this standard adopts that naming convention and extends it by
one rung:

- **Kever** — folds a KEL to current key state (the reference
  implementation's class name, adopted).
- **Tever** — folds a TEL to current registry state (likewise the
  reference implementation's name, adopted).
- **Gever** (extension) — folds
  a GEL, in the context of the KELs
  and TELs it cites, to the Constitution: the answer to "what law
  governs this domain at this position, and what standing does
  this party hold under it."

**Constitution** (extension). The
constituted law-in-force of a GARD: the Gever's computed output,
as key state is the Kever's and registry state the Tever's. The
Constitution is a computed state, never a document: a ratified
text is an event in the GEL; the Constitution is what the fold
returns over all of them. Two GARDs holding identical committed
triples — evidence bundle, law head, appraisal position — hold
identical Constitutions; the GEL alone does not suffice, since
the Gever folds it in the context of the key events and registry
spans it cites (Chapter 1, axiom 2, states the closed triple).
That identity is the property that makes law replayable rather
than testimonial.

Log and fold are one structure read twice, and the tower reads
downward only; Chapter 1 states the structure (§1.2) and the
layering discipline (§1.4), once for every fold this section
names.

**Evaluator; constructor.** The two roles this standard separates
absolutely. A constructor changes a GARD's state: it ratifies
composition rules, seats authorities, advances lifecycle, commits
acts. An evaluator — the Gever's role — consumes a committed
regime and returns findings; it changes nothing, and where the
committed law runs out, it refuses rather than legislates. The
separation is the substrate's own controller-validator division
carried up to the governance layer: only a controller writes a
KEL; any validator verifies it; no validator, however convinced,
may write. "Appraisal" names the activity and the layer — the
fold-plane act of computing findings from committed evidence.
The office of the whole domain carries the stronger verb: KERI
detects; a GARD adjudicates — and appraisal is the adjudicating
domain's judging half, never its acting half. The verbs
themselves are typed in Chapter 1 §1.3; this entry names the
roles that perform them.

**Finding** (extension). The sole return type of the evaluator:
a judgment over a committed regime that carries its own ground —
the type Chapter 1 §1.2 exhibits with its four values, which the
codomain section specifies fully. A finding that does not carry
its ground is not a finding. Findings are judgments about
propositions, never states of processors, seats, or lifecycles —
that boundary is carried at keyword force by the codomain
section's ratified amendment text, which draws it exactly.

**Standing** (extension; the term in its jurisprudential sense).
A covenant-derived judgment of authority: whether a party, at a
position, holds a given power under the GARD's committed law.
Registry evidence is the input; standing is the computed output;
the committed covenant set is the function. The distinction is
load-bearing and the standing section specifies it.

**Predicate; clause; covenant** (the law ladder). Three tiers,
held apart throughout this document. A predicate is the atomic,
verifier-decidable test a clause evaluates — an evaluation-time
object, never separately addressed. A clause is the committed
unit of law: SAID-addressed bytes in the GEL, carrying one or
more predicates and their codomain mapping — the citable atom
that grounds cite and disclosure binds to. A covenant is the
enacted binding of a party to a set of clauses: a relation
created by enactment, carrying its administrators' signatures,
never a text. A clause is committed; a party covenants; a
covenant binds to clauses; clauses evaluate predicates. Clauses
and covenants constrain; they do not act. "Commitment" is
reserved throughout this document for the substrate act —
committing bytes to a log — and names no law object; where this
document says "covenant set" it means the enacted bindings in
force together with the clause sets they bind to.

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

**The seal kinds.** The three commitment kinds — the **digest
seal** committing to exact bytes, the **event seal** committing
to an event at a log coordinate, and the **covenant seal**
committing a subject to the GARD's covenant set, verified by a
fold — a standing question under the sealed clause set — are typed
in Chapter 1 §1.2, and the seal ladder of section 10 carries the
full discipline. Recorded here beside the typing: the kinds are
named beside the substrate's own seal grammar, the first two
subsuming kinds the substrate ships, the third this standard's
extension. The fourth kind Chapter 1 names and defers is the
**evaluation seal** — a committed verdict; its admissibility rule
appears in the seal section, and no construct in this document
uses it.

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


## 6. The medium

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
for whether a pair bears. Conviction in the medium, like every
conviction in this document, is observer-conditional: the
quantifier ranges over verifiers actually holding the pair, and
nothing promises that population is non-empty — the abstract
states this document's deployment-scale record at its own
grade. The medium is the substrate's
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

## 7. The objects that cross frames

What crosses a frame boundary is never judgment; it is committed
evidence in portable form. Three object forms carry every
crossing this document itself makes. They are this kernel's
forms, not a proven closure of the crossing space, and they
interrelate rather than partition — a warranty travels with the
cone spans its finding cites, and a cone is a collection over
the others:

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
  signature is a carriage commitment over the cone's composition
  — composition liability, never a warranty in this document's
  sense, for the warranty object of this section attests a
  computed finding, and carriage liability and content judgment
  never blur; the edict's identity remains the bare content SAID;
  and the judgment remains the consuming frame's computation. A frame
  presenting an edict across a boundary SHOULD present it as a
  dossier over its verification cone, and a dossier's threshold
  operators are the same committed composition grammar the
  standing section sanctions for composed evidence. The cone is
  closed transitively: it SHALL contain every log span the
  finding's replay reads, across every citation, to the depth
  replay actually touches — completeness is decidable by the
  replay itself, and a replay that reaches for a span the cone
  lacks convicts the cone as short. The cone carries the
  designation check of the grammar section: a finding's law
  head SHALL be derivable, from the cone's own spans, as the
  fold of the subject gAID's designated governance registry —
  genesis knot to founding law, founding law to designation,
  designation to registry, registry to fold to law head — and a
  warranty citing a law fold that no designation grounds is
  refused as law, however heavily receipted: recognition and
  receipt weight add force above the designation check, never
  in place of it. A fresh verifier needs
  exactly one entry point held in advance: the gAID. Everything
  else arrives as committed bytes verified against it.
- **Warranty** — a signed attestation of a computed finding,
  emitted under a pinned lens: evidence about a judgment, never
  the judgment. Replay-falsifiable by construction. Its substrate
  lineage is the endorsement — a non-controller signature
  attesting a view of committed bytes — refined by two
  obligations: the lens is pinned, and the attested finding is
  recomputable.

Where evidence itself travels for a stranger's judgment, it
travels in this same shape: the colorless base — valid to
every governance-blind consumer — with the warranty's lens
citation and, where claimed, the warranted finding. The
committed view echo such a crossing carries is nothing new:
it is the finding's own birth-committed declaration — the
evidence bundle's citation enumeration and its discharged
requirement space, committed before any question of bearing
arises. The predecessor edition typed a fourth object form,
colored evidence, for exactly this content; it is removed
here by identification, not retreat — its components resolve
to the warranted-receipt shape above, its color was always
participial and computed at the consumer, and the form may be
reinstated under its own name on exhibited need.

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

**The blinding mandate.** Any object whose self-addressing
identifier is committed in advance of its intended disclosure
SHALL carry a substrate-grade blinding factor, in the
credential layer's own salt-field discipline — cited, not
reinvented; born-disclosed objects are exempt. Governance
preimages are narrow — a roster, an act kind, a coordinate —
and a committed digest over a guessable preimage is fail-silent
confidentiality, the class the grammar section's fail-loud law
must-rejects. The mandate guards the preimage, never the
traffic pattern: anchor existence and anchor grade remain
visible, and that is the medium being honest.



## 8. The finding codomain

### 8.1 The type and its values

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
section 8.5 excludes them by construction rather than by
enumeration.

### 8.2 Pending species and cure

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

### 8.3 The transition system

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
the third rung of the ladder of section 8.4, as T1 is the key
tier and T2 the registry tier.)

**Inputs.** A finding is an immutable fact of a closed triple,
never a mutating value: a function of exactly three inputs — the
committed evidence bundle, the committed law head under which it
is appraised, and the appraisal position. The bundle is a set of
committed log spans closed by citation, each named by log
identifier, coordinate range, and digest: the GEL span, every
cited key-event span, every cited registry span — registry state
is inside the bundle, per the second axiom's own sentence. The
bundle is typed by the law head: the law commits the question's
requirement space ex-ante, and the bundle inhabits the evidence
type the law declares — which is what makes completeness
decidable and affirmation reachable. A whole-log span is lawful
where a committed predicate needs one, and it closes at a
committed coordinate, never at "the log as of now." The position
is a log coordinate in committed order, never wall-clock. The
engine profile is not a triple member: it is the lens-side
citation of the comparing frame, and its inertness — that no
conforming profile changes a public finding at a fixed triple —
is what conformance tests. No other input — wall clocks, local
state, operator discretion, ambient configuration — may
influence a finding. Two evaluations of the same triple SHALL
return findings equal under the one conformance predicate of
section 17: semantic full-payload equality today, byte identity
by construction the moment a carriage encoding ratifies. The
transition tables below constrain the lawful succession of
findings across positions on one question, never the mutation
of a stored value: no coordinate's fact is ever rewritten.

**Required payloads.**

- A defeated finding SHALL carry its defeater class and its
  citation: the violated or superseding clause's identifier, or,
  for cryptographic defeat, the identifier of the failed
  verification subject. Neither is reconstructible from a bare
  verdict; both MUST be explicit or uniquely re-derivable from a
  committed referent.
- A pending finding SHALL carry its typed requirement set:
  deduplicated elements, each carrying requirement kind, subject
  identifier, the list of citing clauses, and its discharge
  species, in the canonical four-field total order — subject,
  then kind, then citing-clause bytes, then species. The
  deduplication key sees every field the element carries:
  elements differing only in species do not merge, for a party
  told that missing evidence would cure and a party told that a
  recovery window stands open have received materially different
  instructions from the same record. The fold discharges
  everything the law commits; the key sees everything the
  element commits.
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

**Bearing.** A finding declares what it stands on at birth —
the evidence bundle's citation enumeration and the requirement
space it discharged — and a conviction bears on a finding
exactly when it is conviction-grade and pertinent: the pair
convicts under the tier's committed rules (at the key tier, the
substrate's superseding-recovery calculus; at the registry and
governance tiers, only within frames that committed the
violated predicate — no committed predicate, no conviction, and
the pair is ordinary evidence to consume), and the convicted
party's artifact is a member of one of the finding's two
birth-committed enumerations. Membership is flat, in a finite
committed list — the bundle is closed by citation, so
everything the finding leans on is enumerated flatly; no
transitivity, no ambient input, no declaration: pertinence is
derived, never declared. The convict's role dispatches the
edge: a convicted subject fires the edge into self-convicted; a
convicted cited third party fires the taint succession of the
duplicity section — the finding's voice is poisoned, not the
question. Both halves of the check were committed before the
question ever arose.

**Forbidden transitions.** Seven edges, absolute:

| From | To | Why forbidden |
|---|---|---|
| affirmed | defeated | settled findings do not flip; new defeat evidence yields a new finding at a new position |
| defeated | affirmed | no transition reverses a defeat; reversal is lawful only as a new finding at a new position whose grown bundle falsifies the cited defeat, per the succession rule below — otherwise rehabilitation is an act, not a transition; taint-cure and ground-evaporation are different phenomena, and neither is an edge |
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
growth, and the monotonicity is over the knowledge order:
growth refines the record — no finding is erased, no citation
un-happens, every coordinate's fact stands forever — at a fixed
law head, never over wall time. Verdicts across successions on
one question may lawfully reverse, under exactly one condition:
a successor finding may reverse a terminal value only where its
grown bundle contains committed evidence falsifying a ground
the prior finding cites — an undercut, computable through the
bearing rule, since the falsified artifact is in the prior
finding's cited ground — and never on added contrary weight
alone. With a cited defeat falsified, the defeat no longer
discharges, and the fold returns what the requirement space now
yields; the prior finding stands at its coordinate, and the
reversal is a new fact, not a rewrite. This document ranks
defeat by class and gives undercut no priority machinery: an
undercut acts only through this reversal condition, and the
divergence from defeasible-argumentation practice is stated
rather than hidden. Defeating evidence is ex-ante enumerable:
everything that could defeat a question is in that question's
committed requirement space before appraisal begins, which is
what makes defeat a citation rather than a surprise.
Contradictory pairs convict only where they bear on the
question — duplicity elsewhere in a subject's history taints
that history's standing, but it does not convert this
question's finding. The ordering forces a discipline on every
terminal value, stated here so no reader must derive it: no
finding is terminal while any enumerated check in the
question's committed requirement space is unexamined. An
evaluator holding a bundle that leaves any enumerated check
unexamined returns pending with that check as its typed
requirement — never affirmed, and never defeated either, for a
fold that stops at its first defeat has computed something no
one committed to: the canonical-selection set below is always
the computed set, and partial examination is a type error, not
a smaller answer.

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

### 8.4 The duplicity ladder and the two currents

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
  monotonic — first-seen survival is the medium's own
  observer-local acceptance policy, described here as the
  mechanism by which duplicity is detected, never an evaluator
  rule — and what was affirmed above stands at its coordinate
  forever. The taint's consequence is a succession: at the next
  position the fold returns pending with the taint as its typed
  requirement, species unresolved-conflict — no missing bytes
  cure a taint, no log growth cures it; only a committed act
  owned by the party whose conflict it is, for rehabilitation
  is an act, not a transition. The subject's voice is poisoned
  going forward; the record it already made remains a record.

**The conviction ladder.** The duplicity ladder rises through
record tiers; a second ladder rises through authorship layers —
evidence author, law author, specification author — and the two
axes never blur. Duplicity is exhibited: two voices, convicted
by comparison of a pair of the author's own committed bytes.
Antinomy is derived: one voice whose committed law is jointly
unsatisfiable — a set of grounded derivations over consistent
evidence, each individually clean, no contradictory pair
anywhere, the contradiction reachable only by the fold that
derives it. An antinomy conviction's proof object is a circuit,
never merely a pair: the jointly-unsatisfiable set of grounded
derivations, each citing its evidence spans and clause
identifiers to its conclusion, together with the
joint-unsatisfiability exhibit and the enactment signatures of
every producing clause — a pair cannot express the decisive
case, cardinality three or more, pairwise consistent, jointly
unsatisfiable. Irredundancy — that no proper subset suffices —
is a SHOULD, never a MUST: an honest non-minimal circuit still
convicts, and extracting a minimal core is work this standard
does not compel. The
bearer is the domain's administrators, never the subject, and
the force is law-relative and reflexive: the conviction binds
maximally in the very frame whose law it convicts, and travels
to every other frame as evidence about that domain. An antinomy
discovered after affirmation is a new terminal finding at a new
position; no forbidden edge opens. Self-conviction's typed
inhabitants are therefore two — duplicity and antinomy — and
one conviction lives above the codomain entirely: divergence,
two conforming engines returning different public findings on
one committed triple, convicts the specification itself, on its
own conformance records and the divergence transcript. No fold
returns it; it is not a finding but this standard held to
account by its own discipline, and a differential harness over
independently conformant engines is the only instrument that
detects it.

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

### 8.5 The separation rule

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

The product closes under refusal: where any component of a
compound invocation refuses, the invocation refuses — the
refusal remains an operational outcome about the composition
seam, its ground named under the seal ladder's three-kind
discipline — and the refusal record cites the components
already computed, which stand as ordinary findings at their own
coordinates: facts once computed, for a sibling's refusal
un-happens nothing. No product object ever contains a refused
coordinate — refusal answers about the seam, findings answer
about the subject — and no computed finding is discarded. An
unsatisfied component discharges as pending inside the product;
an uncomposable product refuses whole.

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


## 9. Standing

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
section 8: a standing question returns affirmed, defeated with
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
8.5 read constructively: refusal fires where composition is
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


## 10. The seal ladder

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
the GARD's covenant set — to standing law, not to another
object. Its verification splits into three layers at three
epistemic grades, and the layers never blur. Carriage is medium
physics, tier-uniform: the covenant seal is carried as the
substrate's own generic typed seal with a reserved type value,
its seal data the self-addressing identifier of the sealed
clause set — no substrate extension is claimed, and a
governance-blind consumer parses the seal unharmed. Attachment
is medium physics, likewise tier-uniform: coordinate lookup and
lineage walk, the event-seal machinery reused. Satisfaction is
governance-tier computation, and it is a fold: whether a
successor satisfies the sealed clause set is a standing
question under that set, returning the four-valued finding —
warrantable, contestable, position-indexed, inheriting the
codomain's full machinery. A seal joined to a defeated
satisfaction finding is breach with a committed anchor. What
the seal irreducibly does is name the clause set a successor is
answerable to, forward, at a committed coordinate — the promise
survives amendment; the seal carries the question, and the fold
supplies the answer. A covenant seal on a governance corpus
thereby commits its future: every successor is checkable
against the sealed clause set, and an unsatisfying successor is
convictable on the seal's own bytes. Admissibility is the
decidable test: where byte equality is achievable, the digest
seal is the honest kind, and a covenant seal over
digest-sealable content is itself a defect. The sealed set
names clause identifiers into the sealing domain's designated
governance registry; a portable clause language — sealing a
subject to another domain's law — is chartered to the encoding
round and not designed here.

Two disciplines bind all three kinds. A seal names its kind:
consumers MUST NOT be left to infer commitment semantics from
context. And a conviction sourced from a seal names the seal kind
it convicts under — a digest mismatch, a coordinate mismatch, and
a clause violation are three different refusals, and a record
that blurs them is unauditable (the conviction-family rule of
section 15 carries this forward; where this document requires a
refusal to name its ground, this three-kind discipline is the
naming rule).

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


**Anchor grade.** Where a seal lands is itself a committed choice
with committed consequences, and this standard names the grades
rather than leaving them ambient. A seal carried in an
interaction event is erasable in principle: superseding recovery
at the key tier can displace the event that carried it, and the
seal's survival is then a promise of the recovery policy rather
than a property of the log. A seal carried in an establishment
event is physics: displacing it forks the establishment lineage
itself, and the fork is duplicity evident to any watcher holding
both branches. Neither grade is forbidden — the difference is
computable, and a consuming frame weighs it. Designated act
classes — charter, revocation of a seat, enactment amending law,
and the succession acts of section 17 — SHALL anchor in
establishment events; a domain whose law designates further
classes commits that designation in its GEL. The difference
between the two grades is the difference between promise and
physics, and this standard does not let the two wear one name.

## 11. Rotation policy

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
medium — it grounds recourse under section 14.

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
  until exercised, each such pre-disclosure commitment carrying
  the blinding factor the objects section mandates;
- **on what evidence** — from none to a committed ground with
  attestations, in which case the recovery rotation is a grounded
  enactment and inherits all of section 14.1: its ground replays
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
recourse machinery of section 14 enacted in key state itself —
the frame answering compromise of its own authority with a
grounded, contestable, replayable act. Rotation policy is where
the temporal and the judicial reflexes of an autonomic frame
meet. These are illustrations, not a registry: the axes are the
law; the uses are what Constitutions do with them.


## 12. The governed object classes

This section states no new law. It derives, from the sections that
do, the generative rule the frame interior instantiates — stated
once, so that a builder can see the move whole and derive the next
instance without asking.

**The one move.** Every governed object in this document is the
two-layer joint of section 11 pointed at a different substrate
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
section 9, which names the schemas its standing law consumes —
and schema succession (an amendment in the GEL).

**The relation axis.** The move instantiates across relations as
well as objects: law over the frame's own lifecycle
(self-directed); law over a seated organ's (the seat); law over
evidence consumed from strangers (adoption); law under a
federation envelope (peer). The columns are one law at four
distances from the frame's own keys, and computed congruence
(section 13) is the medium-grade measure of the passage from
stranger to peer.

**The classes this document exercises.**

- **Governed key state** — KEL events; its law is rotation policy
  (section 11).
- **Governed seats** — delegated establishment events; its law is
  a Constitution's seating clauses and this document's
  delegated-organ rule (sections 9 and 11).
- **Governed registries** — registry inception and management;
  its law is the covenants of section 9 naming which registries,
  under which semantics, confer what.
- **Governed credentials** — issuance and revocation; its law is
  the standing covenants of section 9.
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
judged: the knot in section 5's gAID definition — founding law
computed first, sealed at inception, the identifier excluded from
every pre-identity byte — closes the cycle exactly where no prior
Constitution exists, and the law in force at the first event is
the substrate's own admission rules: the degenerate law every
frame has because the substrate imposes it, in the pattern of
section 11's degenerate policy. Every later event is judged inside
the positional recursion. The forward commitment at the far end
is the same discipline at a confessed lesser grade: as
pre-rotation commits key state to its successor's digest before
the successor exists, the succession rule of section 17 commits
this document to its successor's criterion — criterion, not
digest, and the difference in strength is stated rather than
blurred. Self-description without self-application, at either
end.

**The enumeration is open.** These classes are found by the
criterion, not decreed by this section: a Constitution that
commits law over a further substrate lifecycle has derived the
next instance, not extended this standard. The rows are
illustrations at the grain of section 11's axes: the criterion is
what generalizes; the classes are what this document did with
it.


## 13. The transformation law

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


### 13.1 The two relations


**Consumption — unilateral.** Frame B consumes frame A's edicts as
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

**Federation — bilateral.** Frames A and B grant each other's
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

### 13.2 The transformation


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
   verification. A dossier whose carriage commitment fails
   to recompute convicts its curator without touching the
   edict's own standing: carriage liability and content
   judgment never blur.
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
   whatever B's law says the evidence, as B's own fold colors
   it, confers.

Steps 1-2 are the invariant half: every frame computes them
identically or the medium itself is broken. Steps 3-4 are the
covariant half: they differ by frame lawfully, and the same edict
is lawfully colored differently by every frame that judges it,
simultaneously — many dyers, one object, no possession.


### 13.3 The verification regimes

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

Color is computed, never asserted — and it belongs to the
domain, never to what the domain judges. A governed domain's
color is its fold in force: its committed law configuring the
evaluator this standard types, at a position of its record. A
receipt, an attestation, or any evidence object is colored by
that fold's judgment — the coloring is the output of a committed
rule-set evaluated over committed bytes at a committed position
— and an issuer's asserted coloring is merely more evidence for
that computation to judge, including evidence of the assertion's
own falsity. The colorless base
remains valid to every consumer that ignores governance entirely:
a validator that knows nothing of GARDs parses and verifies the
same bytes unharmed. Adoption of a coloring regime is a committed
act of the adopting party — no threshold of attestations makes a
coloring ambient, and no party is subject to a regime it never
committed to.

The deployment-scale questions of these regimes — when
warranted consumption is necessary rather than convenient, what
work replay demands at deployment scale — are stated in this
standard's record as open questions with committed fixture
obligations, and this document claims nothing about them. The
construction stands on its own: replay disciplines warranty
whether or not the warranted path is ever the necessary one.

One further compaction is admitted without being delivered. A
zero-knowledge proof of a fold — a proof that a finding was
computed under committed law from committed evidence,
disclosing neither — would extend this consumption ladder one
rung past the warranty, toward verification whose work no
longer grows with the record replayed; the compact receipt form
of section 19 is the nearer rung, gated there. No clause of
this standard depends on such a proof, and no gate for one is
stated here: the admitted future is recorded so that its
arrival would be an extension, never a surprise.


### 13.4 The discipline


No authority ranks frames. The discipline between them is mutual
convictability over the shared medium:

- **Cross-frame duplicity.** A frame that speaks with two voices —
  to two counterparties, at one committed coordinate — is
  convictable by anyone holding both logs. The conviction is
  frame-invariant: it is computed in the medium, not under any
  frame's law — and it is observer-conditional, per the
  abstract's stated grade: the quantifier ranges over verifiers
  holding both logs and never promises that population is
  non-empty. Watchers make conviction likely; nothing makes it
  guaranteed.
- **False-warranty conviction.** A warrantor whose attested
  finding diverges from replay is convicted on its own signature
  by any verifier that recomputes. Warranted consumption is
  disciplined exactly because replay-native consumption never
  closes.
- **Envelope breach.** A federated frame that confers force
  outside the shared rule-object's commitment, or withholds what
  it committed, has produced committed evidence of its own breach
  — liability under its counterparty's law and its own.


### 13.5 Engine independence


Nothing in this law requires a constructed governance engine.
Steps 1-2 bind to the substrate's own machinery; steps 3-4 bind to
the evaluator's type boundary — its return type, its refusal rule,
its determinism — which any conforming implementation satisfies.
The composed joint — substrate admission and governance appraisal
over the same committed bytes — is exercised at fixture scale
against one implementation at one pinned checkout, and nothing
wider is claimed, while the engine interior remains open by
confession. Agreement between engines is geometry, never
consensus: different evidence is a different bundle; different
law is a different sheet; and the same committed triple on the
same sheet must agree — under the conformance predicate of
section 17 — for every conforming engine, however different the
interiors. Divergence there convicts neither engine but this
specification, per the conviction ladder of the codomain
section, and the differential harness is standing
instrumentation of this standard's record, not an optional
courtesy. The transformation law
is the reason the open interior does not leak: everything that
crosses frames is defined at the boundary.


## 14. Recourse

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

### 14.1 The grounded enactment

Recourse is an act, and acts belong to constructors: a recourse
act is an enactment in the GEL, subject to everything section 9
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
at an uncommitted seam are open surfaces of the section 16
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

### 14.2 The recourse ladder

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
  medium section; observer-conditional, per the abstract's
  stated grade — the verifiers holding the pair are never
  promised to exist). This rung is not recourse but its evidentiary
  floor: the medium convicts and never sentences, and every act
  taken on that conviction is frame-local and grounded like any
  other.

### 14.3 The final rung: recourse against the frame

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
federation duties (section 15). A sovereign cannot be imprisoned, but it can be left —
and in this architecture, leaving takes the proof along.

### 14.4 What this section does not design

This section commits the grounded-enactment profile: what makes
a consequence lawful, what grounds it, how its abuse convicts.
It does not claim the profile exhausts recourse semantics.
Recourse procedure is constructor interior, open by the
confession of section 16: who may initiate, how questions are
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

## 15. Federation duties

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
governed protocol, as defined in section 5.


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
substrate's own law is silent. A federated GARD SHALL state
which latitude it has closed by committed profile and which it
inherits open — and the closure instrument is committed, never
ambient: a Constitution SHALL commit, as a functional-dependency
declaration, the revision digests of every external
specification whose semantics its fold consumes, naming the
predicate set consumed — the substrate's superseding-recovery
calculus rule by rule, each consumed or expressly excluded,
never in silence, and the carriage threshold semantics where
used — with the whole-file digest standing where those
predicates currently live, confessed as pin granularity rather
than design; where a consumed rule set later exists as its own
self-addressed artifact, re-pinning coarse to fine is an
ordinary migration. Semantics-version is thereby a governed
object by the criterion of section 12, and a substrate upgrade
is a migration enactment at a committed coordinate: replay
before and after the move is deterministic, and the move itself
is replayable. Pinning does not pretend the upstream is static;
it makes when the domain moves a committed, visible act.

**Travel posture.** This duty's forcing ground is standing, not
a transformation step: a claim traveling as a defect report or an
allocation request borrows an authority over the receiving corpus
that the traveler does not hold. Nothing in this document SHALL
travel as a defect report, an allocation request, a custody
selection, or an extension proposal against any substrate or
ecosystem corpus before an authoritative answer from that
corpus's own custodians. Questions travel as questions.



## 16. The openness clause

This document tells the reader where its own design ends. The clause carries keyword force: prose anywhere in this
document or its companions that implies design beyond the
boundary stated here SHALL be treated as a defect of that prose,
reviewable and repairable as such.

**What is fixed.** Seven commitments bound the governance
evaluator. They are enumerated here, once, in this edition's
own text — every wall binds as this document's text, never by
pointer into a predecessor, for an imported wall can be neither
read nor repaired in-document and drifts unowned — and every
other section that needs them cites this list:

1. **Codomain totality.** The evaluator's return type is the
   four-valued finding codomain and nothing else.
2. **Refusal at the seam.** At an uncommitted composition seam
   the evaluator refuses rather than legislates.
3. **Complete enumeration, no backward edge.** The transition
   system is explicitly and completely enumerated, and no
   backward edge exists in it — one commitment, for an
   un-enumerated system cannot prove the absence of an edge.
4. **The two currents.** Defeat annihilates upward while
   duplicity taints upward, and the two currents never merge.
5. **Committed receipts for acts as grounds.** An unreceipted
   operational drop is never a finding.
6. **Canonical ordering.** Every order a fold consumes MUST be
   derivable from committed bytes: at every site where an order
   can affect a finding, this standard names the canonical
   order, and the canonical order is total — lexicographic over
   the encoded self-addressing identifiers at the site unless
   the site's clause commits a different derivable order; at
   every site where an order cannot affect a finding, the claim
   of irrelevance is a conformance obligation, exhibited by
   confluence vectors under permuted arrival. This wall is the
   constitutional hook of the fourth axiom's order face; site
   rules descend from it.
7. **No fold-tier selection.** The fold consumes digest-cited
   committed spans; it never adjudicates between competing
   versions of an event. Competitors at one coordinate entering
   the bundle convict as duplicity — they are never inputs to a
   choice; survival is settled below the fold, at bundle
   assembly, per holder, by the medium's own inherited
   acceptance policy, reimplemented nowhere.

These seven are walls: evidence-ruled, fixture-exercised, and
binding. Membership is conserved from the predecessor's
ratified lists — the seventh is the retype of a wall whose
stated obligation was a category error, its commitment already
carried by the fourth axiom, not a new commitment; a genuinely
new wall enters only through its own gauntlet, never as a rider
on a repair.

**What is open.** The interior they bound is undesigned, and this
document does not design it: evaluator scheduling, constructor
architecture, composition-rule authorship, seating procedure, the
act-registry design, receipt transport, the deployment
realization of observation, and the general algebra connecting
these parts, together with the carriage encoding of this
document's object classes — a committed deliverable whose default
posture is the substrate's native composable attachment grammar
rather than document envelopes, chartered to a design round
convened with the substrate's own stewards and this standard's
implementers, expressly not gating this edition. The interior is
assigned to review by others, entering as findings, never as
edits. A reader who infers a completed construction from the
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


## 17. Succession and ratification

The ratified Custos 4.1 edition is the document of record this
document supersedes, and its bytes are pinned as an external
whole-file pin under the reading rules' two-kind discipline:
sha256
ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05,
computed over the predecessor's complete published byte stream
(whole-file preimage, no placeholder, verified by round trip at
this document's assembly), ratified at its authority KEL's
sequence number 187 and effective at 188. The ratified Custos
4.0 kernel (sha256
9cefdc5d584289ea8391d8069bca26ea38aa82a34f9ae973d80e4d1b7773f315)
and Custos 3.3 (sha256
18b0469e731db24f6bca45525828e4417751929306ea21e09977088e08a20ceb)
stand superseded through that lineage. The predecessor remains
byte-immutable: nothing in
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
discharged here: cross-implementation interoperability — two
independent implementations deriving, from one committed corpus
in both presentation orders, results equal under this
document's one conformance predicate, stated once here and
cited by the scope and codomain sections: semantic full-payload
equality — finding value with its self-convicted kind, grounds
in canonical order, typed requirement sets including species,
refusal grounds with the seal kind named per the seal ladder's
three-kind discipline wherever refusal fires, cited law heads,
and corpus identities together with their admission sets, the
admission set a constituent of corpus identity and named
explicitly for the avoidance of drafting doubt — with byte
identity following by construction, as this standard's forward
commitment, the moment a ratified carriage encoding removes the
last serialization freedom; and the authority-lineage
materialization above. Both are debts of the
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


## 18. The GEL grammar

Section 5 defines the GEL and its anchoring discipline; this
section commits its event grammar. Composition, per the
comprehension gate: a GEL event is a log entry (log) carrying an
enactment or its evidence (enact), committed by seal into the
gAID's KEL (seal), read by exactly one fold (fold, finding), and
subject to the law in force at its position (succession).
Nothing here requires an eighth primitive.

**The spine.** The GEL is a thin, single-signature spine. The
only utterances a gAID makes unilaterally into its own GEL are
anchorings: commitments of acts to coordinates. Everything
multi-party — co-signed enactments, seated organs' acts,
federation envelopes — enters as evidence the spine anchors,
never as spine events with interior authority structure. A GEL
event whose lawfulness depends on authority beyond the gAID's
key state at its coordinate is committed by the spine and judged
by the fold; the spine carries, the law decides.

**Event identity.** Every GEL event SHALL carry a self-addressing
identifier in its own field, computed under the reading rules'
pin discipline: the identifier field carries a placeholder of
the encoded digest's length during computation, and the digest
ranges over the event's complete canonical bytes. A GEL event
whose identifier field is not self-addressing is not a GEL event
of this standard. Receipts and attachments addressing a GEL
event address these bytes; a coordinate tuple is a location,
never an identity.

**Canonical order.** This paragraph is a site rule descending
from the canonical-ordering wall of section 16. A fold consumes
its log in exactly one
order, and that order derives from committed bytes: KEL
anchoring order first, intra-anchor order as the anchoring
event's seal list states, and no tiebreak that consults
anything uncommitted. An implementation whose fold result
depends on arrival order, storage order, or any ambient
sequence does not conform; the conformance vectors for this
paragraph include streams presented in permuted arrival order
that SHALL fold to byte-identical Constitutions.

**The two tracks.** Two event-form tracks are lawful, and a
domain's choice between them is committed law, not convention:

- **Track one — registry-form reuse.** GEL events use the
  substrate's registry event forms under their existing ilks,
  with governance semantics carried entirely by the committed
  law that interprets them. This track is the colorless base:
  any registry-capable consumer parses the events unharmed, and
  the governance reading is the adopting domain's committed act.
- **Track two — governance ilks.** GEL events use ilks minted
  for governance semantics. The ilk registry for this track is
  itself committed data in the GEL — the table of event types a
  domain's law recognizes is law, enacted and amended under
  succession like any other clause, so the grammar a domain
  speaks is born governed rather than assumed. A consumer
  encountering an unrecognized governance ilk holds committed
  evidence of exactly that; recognition is a computed judgment
  under the consumer's own law.

**The bootstrap.** Track choice and, for track two, the initial
ilk table are committed law — and a verifier must derive them
before it can admit the first event they govern. That derivation
grounds outside the GEL, in the genesis knot Chapter 1 and the
definitions section already commit: a born-governed domain's
founding law is sealed at inception, and the initial track
placement and initial ilk table are clauses of that founding
law, readable from the inception-sealed bytes before any GEL
event is consumed. An adopted domain's later-anchored founding
law grounds the same commitments at its confessed lesser grade.
Migration — a change of track or of ilk table — is an enactment
judged under the grammar previously in force: the event that
changes the grammar is itself admitted under the grammar it
changes, exactly as an amendment is judged under the law it
amends. Where a verifier cannot derive the initial placement or
table from the applicable committed founding-law referent — the
inception-sealed founding law of a born-governed domain, or the
later-anchored founding law of an adopted domain, at its
confessed grade — it refuses the
stream — a missing rule, not missing evidence — and the refusal
names the underivable commitment.

**Designation and membership.** A domain's founding law SHALL
commit the identifier of the governance registry it designates
as its GEL, at inception grade, sealed by the genesis knot; an
adopted domain's later-anchored founding law grounds the same
designation at its confessed lesser grade, and registry
migration is an enactment like any other. No positional default
exists: a convention that reads the first-anchored registry as
law fails silent on inception-order accidents and cannot
express migration, and this grammar commits no such reading.
The membership face of the fourth axiom binds here concretely:
every span the fold consumes as GEL SHALL be derivable from
committed bytes, and a stream whose governance registry or
whose membership cannot be so derived fires the bootstrap
refusal above, extended from placement to membership. The
designation is the domain's GEL-singleness declaration, and its
enforcement is inherited from the knot's own physics: a second
designation requires either a second founding-law byte-set
against one anchored identifier — digest-impossible — or a
second KEL, which is key-tier duplicity; singleness of law is
thereby grounded, and every other singleness is conferred by
clause and adjudicated by the designated fold. The check enters
the verification cone, per the objects section: a finding's law
head SHALL be derivable as the fold of the subject gAID's
designated GEL, and a warranty citing a non-designated law fold
is refused as law — recognition and receipt weight add force
above the designation check, never in place of it, however
heavily warranted the stranger. Two disciplines complete the
rule. Fail-loud: law content MAY blind per the disclosure
postures Chapter 2 types; designation and membership fail loud
or not at all, and any membership rule that can yield a proper
subset of the GEL without a refusal is a must-reject. And a
confessed bound, stated plainly: one entity operating two
domains with clean faces is beyond byte-conviction by
construction — this standard convicts identifiers, never
entities; a founding law MAY carry a sole-authority clause
converting surfaced linkage evidence into ordinary clause
breach, and authority singleness is thereby clause-grade, never
physics-grade.

The two tracks do not manufacture duplicity: an event is on the
track its domain's committed law places it on, the choice is
readable from the domain's committed record — the founding-law
referent for the initial placement, the GEL it governs for every
migration since — and a domain that speaks both
tracks at one coordinate without committed placement law has
produced inconsistency its own fold convicts.

**Genus.** The encoding substrate's genus namespace admits
reservation, and a reservation of a governance genus is itself
an enactment: committed in the GEL of the domain that reserves
it, carrying the reserved coordinates and their intended
grammar, judged and superseded under that domain's law.
Recognition of the reservation by the substrate's stewards is a
distinct, later, bilateral event — a federation-shaped
recognition, not a precondition. The reservation this standard's
own record commits is Exhibit-class evidence for section 16's
confessed frontier: enacted, unrecognized, and honest about the
difference.

**The compact form gate.** The compact, count-code-framed
receipt form — the wire shape by which a warrantor's backing
travels per-receipt — is specified, with the three ordered
gates on its use and the envelope rule that holds until they
stand, in section 19; premature compact-form use is a
must-reject of this grammar, enumerated below.

**Vectors.** Each committed obligation of this section owes a
discriminating record before any implementation claims it:
equivalence vectors (both tracks expressing one governance act;
byte-identical fold results); boundary vectors (must-reject:
non-saidive event identity; designated-class act anchored in an
interaction event; both-track placement without committed
placement law; a stream whose initial track or ilk table cannot
be derived from the applicable founding-law referent; a stream
whose designated governance registry, or whose GEL membership,
cannot be derived from committed bytes; a well-formed warranty
citing a law fold no designation grounds, however heavily
receipted; a membership rule yielding a proper subset of the
GEL without a refusal; a grammar
migration not
admitted under the grammar previously in force; compact-form use
while any of the ordered gates of section 19 remains unstood); refusal-boundary
vectors (an unrecognized governance ilk yielding committed
evidence and a rule-governed judgment, against the refusal fired
by an underivable grammar — the pending/refusal line drawn at
the grammar grain); recognition vectors (a genus reservation
enacted and consumed as committed evidence, distinguished from
external recognition, which no vector may presume); and order
vectors (permuted arrival, identical Constitutions). A guard
that has never been shown failing is not yet a guard; the
vectors are the exhibit that every wall in
this section can actually refuse.

## 19. The compact receipt form and its gates

The grammar section commits the compact, count-code-framed
receipt form — the wire shape by which a warrantor's backing
travels per-receipt — as a deliverable behind three ordered
gates. This section specifies the gates, the rule the first
gate turns on, and the ground the whole construction stands on.
Composition, per the comprehension gate: the compact form is a
carriage shape for a warranty (an enactment binding its maker
to a finding's ground) over a receipt and its attachments,
committed by seal and judged like any other evidence; nothing
here requires an eighth primitive. Compaction is a change of
carriage over a meaning already committed, and each gate closes
one way a lighter wire form could silently become a different
commitment: the first closes identity drift — what bytes the
one digest speaks for; the second closes authority drift — what
law governs the form's event types; the third closes order
drift — whether arrival order can change the fold. Until every
gate stands, warranted receipts travel in the heavyweight
envelope form — the substrate's own receipt bytes unmodified,
with the backing carried in attachment groups — which is
complete and lawful today; the compact form changes cost, never meaning.
The consumption ladder of section 13.3 is this section's
governing frame, and this section is that ladder's nearer rung,
cited downward from it.

**Gate one — the bundle-commitment rule.** The defect this gate
closes is verified from the substrate's reference
implementation at the pinned checkout: the substrate's receipt
form is the one event form whose identifier field is not
self-addressing — a receipt's identifier names the receipted
event, not the receipt's own bytes — and nothing in the
substrate today lets one digest address a receipt together with
its attachment groups. A compact form whose one identifier
cannot speak for its whole bundle is an identity without a
committed preimage: a commitment without ground. The rule, a
candidate design bound to its own gauntlet leg:

> **Bundle identifier.** The bundle identifier of a warranted
> receipt is the self-addressing digest, in the substrate's
> encoding, of the canonical bundle preimage: the concatenation,
> in this committed order, of the receipt serialization bytes
> exactly as receipted — the substrate form unmodified, wrapped
> and never altered — followed by each attachment group's framed
> bytes, count code included, the groups ordered
> lexicographically over the encoded form of each group's
> primary identifier; where a group's own grammar commits an
> internal order, that order is preserved within the group, and
> only the between-group order is imposed. The bundle identifier
> is computed over the preimage, never over any presentation:
> two presentations of one bundle SHALL re-derive the same
> bundle identifier, or the bundle is not the same bundle.
>
> **Two liability layers, never blurred.** The bundle identifier
> is a carriage commitment: its signer attests the composition
> and integrity of the collection, never the veracity of any
> claim within it — the objects section's carriage division,
> applied at the receipt grain. The warrantor's judgment
> commitment is a separate object — the warranty of the objects
> section, schema-typed, registry-bound, its lens cited — that
> cites the bundle identifier and never signs the bundle
> directly. Two signatures over two preimages: a carriage
> conviction (the preimage fails to recompute) and a judgment
> conviction (replay of the cited triple contradicts the
> finding) are distinct by construction, even when one party
> holds both roles.

Three properties of the rule are each a vector obligation:
presentation independence — the preimage is derived by
canonical reassembly, so arrival order is provably inert, by
construction rather than by discipline; substrate
non-interference — the receipt bytes travel unmodified, so
every existing consumer parses them unharmed; and tamper
totality — any byte change in the receipt or any attachment
group changes the preimage, hence the identifier, hence defeats
the backing. One dependency is confessed rather than resolved:
whether the receipt-grain carriage commitment stated here is
the special case of the dossier specification's own composition
commitment, inheritable by citation rather than restated, is a
question pending with that specification's author; the
two-layer structure above stands on this document's own
never-blur division either way, and the answer changes the
citation, not the structure. Gate one stands when the rule's
text has survived its gauntlet leg, a reference implementation
recomputes bundle identifiers against receipts produced by the
substrate's reference implementation at a pinned checkout, and
the must-reject vectors of gate three's family are green.

**Gate two — the governed ilk-table seats.** The compact form
introduces wire shapes whose event types must be governed
types: rows of a track-two ilk table that is itself committed
law under the grammar section, or the form's grammar floats
free of any authority. The genus reservation already stands as
an enactment — enacted, unrecognized, and honest about the
difference, per the grammar section — and what does not yet
stand are the seat enactments: one committed event per seated
row, each carrying the row's complete field domain, including
where the bundle identifier sits; its placement law, naming
which anchor grades may carry it under the seal ladder; and the
grammar coordinate it extends, the table version it seats into,
cited by identifier. Gate two's discharge is pure enactment —
the machinery is committed law already; the acts are simply not
yet performed — and gate two stands when every track-two ilk
the compact form speaks has its seat enactment anchored at
establishment grade and the resulting table round-trips through
the grammar section's genesis-derivation requirement: a
stranger derives the table from committed bytes alone. One
contingency is held open rather than designed against: whether
the ilk seats take their currently drafted shape is an open
question of this standard's record, and nothing in this section
presumes its answer.

**Gate three — conformance vectors, both presentation orders.**
The residual risk after the first two gates is an
implementation faithful to rule and seats but sensitive to
arrival; gate three is not design but the discriminating record
for the other two gates' claims — a guard never shown failing
is not yet a guard. Three vector families are committed. The
equivalence family: one warranted receipt bundle, both
presentation orders, identical bundle identifier and identical
fold consequence. The must-reject family: bundle tamper, one
byte in any group; forged group identity, a between-group
permutation canonical reassembly does not cure; digest-preimage
confusion, the bundle identifier offered where the receipted
event's identifier is required or conversely — the two digests
are different types, and a conforming consumer SHALL refuse the
confusion; an unseated ilk; compact-form use while any gate
remains unstood; and route isolation, below. And the
vanilla-passthrough family, gate-grade: a warranted heavyweight
envelope fed to an ungoverned substrate node at the pinned
checkout — the receipt MUST verify and the stream MUST survive
the extra attachment groups, and an envelope grouping that
fails this vector is redesigned until it passes: compatibility
is a gate, not a hope. Gate three stands when all three
families are green under the committed station harness; a
single-implementation green is lawful at its confessed grade,
and cross-implementation green is the deliverable the
succession section already carries.

**The one-way-coverage ground.** The bundle rule is not a
workaround for a substrate gap; it is the only geometry the
signature law permits, and the reasoning is committed here so
the question does not reopen. Self-addressing works because a
digest is a public, deterministic, keyless function of bytes:
the identifier's own field is filled with a placeholder of the
digest's length, the bytes are hashed, and any verifier
re-derives the value by the same committed convention — the
circularity is defined away by a public rule about the hole. A
hole in a preimage is lawful only for a value anyone can
recompute from the rest of the bytes. A signature never
qualifies: verification checks it, only the private key
produces it — so an endorsement can never live inside the
identity of the thing it endorses. Sign before addressing, and
the endorsement covers bytes in which the identity was a dummy,
liftable onto any content with the same dummied form; address
before signing, and the identity fails to cover the signature,
leaving a mutable interior region — two byte-different objects
with one identifier, a blind spot exactly where the medium's
duplicity comparison must see; and a genuine fixpoint, each
covering the other, is what the hash function exists to make
infeasible. At most one coverage can be interior, and the
substrate chose: identity covers all content, with no holes,
and endorsement stands outside as attachments. The historical
record corroborates the choice — the enveloped-signature
tradition of the web's first signature standard put endorsement
interior to the artifact, excluded at verification by
canonicalization, and its mutable interior became two decades
of exclusion and canonicalization exploits; the register of
external influences carries the citation as this standard's
negative exhibit. The receipt form's non-self-addressing
identifier is that same choice, honest at the receipt grain: a
receipt is a pointer plus endorsements, its content is
elsewhere, and no in-form digest could ever cover attachments
that must stand outside the bytes they endorse. The lawful
replacement for self-endorsement is endorsement by enclosure
from outside, one layer up: event bytes under the event's
identifier; witness endorsements beside them; the two together
under the bundle identifier; the warrantor's backing citing the
bundle identifier from outside, content for a next layer out if
one is ever needed. Each layer's identity covers everything
inside it; each layer's endorsement stands just outside; every
floor stands on completed bytes, and nowhere is there a circle.

**The transport stratum.** Self-framing is genus-relative: a
count code's size semantics come from its genus's code table,
so a parser that does not hold a genus cannot size an
unrecognized group, and the substrate's reference parser raises
on unexpected count codes rather than skipping them — verified
from its primary bytes at the pinned checkout. Skippability is
a property of the outer frame's genus, never of the encoding
layer globally. The consequence binds as a must-reject:
compact-form bytes, which travel in this standard's own genus,
SHALL NOT ride in streams consumed by parties that never
committed the regime — a foreign-genus segment is mechanically
fatal to every consumer not holding the genus, not merely
unlawful — and compact-form bytes arriving on such a route are
refused at the genus boundary. The compact form is spoken only
where both endpoints committed it. Three voices result, one
invariant. Anchors: governance commitments as seals in the
substrate's own events, parsed, replicated, witnessed, and
duplicity-guarded by every ungoverned node natively — the
governance tier's security inherited by anchoring, reimplemented
nowhere. The heavyweight envelope: substrate receipt bytes
unmodified plus backing in attachment groups the ungoverned
parser accepts in position, bound by the gate-one bundle
identifier — the vanilla-passthrough vector is that claim's
discriminating record. The compact form: this standard's genus,
track-two ilks, spoken only on committed routes. Every voice
binds the same committed bytes through their identifiers;
adoption stays a committed act of the adopting party; cost
falls as commitment deepens; meaning never moves; and the
substrate's protections hold undiminished at every rung,
because every rung anchors into the KEL.

---

## Appendix of record — regeneration accounting (three censuses)

Method authority: the consume-and-regenerate ruling. Input
authority: the committed 4.2 input manifest (sha256
74bdb8a0d950d8c7d8454cb7e015642636eae3d8944f954ba1d5e54d2ac950d9),
whose Amendment 4 makes this appendix a three-census register:
the delta census accounts every change from the predecessor
under its governing ruling; the structure census dispositions
every predecessor section; and the collision-by-addition census
re-examines every carried span against this edition's new
commitments, so that unchanged text made defective by new law
is a first-class finding, never a silent survival. Predecessor:
the ratified Custos 4.1 edition of record (sha256
ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05).
The rulings cited below live in the ruling record of 2026-07-30
and its two supplements (2026-07-31; 2026-08-01), cited
together always, and in the 4.1-cycle rulings the manifest
carries forward. One confession, stated plainly: the committed
census generator for this edition (the census-is-a-program law)
is a deliverable of this candidate's gauntlet, not of this
assembly pass — the censuses below are the regeneration's own
register, verified span by span in the assembly report, and the
generator run against final-form bytes is a ceremony gate that
no prose census substitutes for. Every predecessor sentence not
named below was re-derived and survives verbatim — verbatim
survival is re-derivation that confirmed the sentence under the
rulings in force, never inertia.

### Delta census

Every departure from the predecessor, each under its governing
ruling. Sites are named in this edition's numbering.

1. Head — superseded: new lineage pins (4.1 by whole-file
   digest as predecessor of record; 4.0 and 3.3 through it) and
   the input-manifest pin (succession law; R8's two-kind pin
   discipline).
2. Abstract, replay sentence — repaired under R11: findings
   replay byte for byte; refusals re-derive as decisions from
   the same committed triple; the claim is scoped to what the
   evidence rules.
3. Abstract, second paragraph — regenerated under C-13: the
   verification-cost register (mechanism property, engineering
   units) replaces the predecessor's economic register; the
   deployment-scale confession carries with force intact.
4. Introduction — superseded: recomposed for the two-chapter
   architecture, the three-census appendix, and sections 18–19.
5. §1.2, covenant-seal entry — repaired under R17: the
   undecidable lineage-invariant admissibility condition is
   replaced by the decidable digest-precedence test.
6. §1.4, axiom 4 — repaired under supplement 2's generalized
   commitment: no ambient input, three faces (order, membership,
   semantics), stated once where the axiom lives, each face with
   its discriminating refusal.
7. §1.4, wall paragraph — repaired under R4 (own-text
   provenance) with E-1/C-2: the import-by-referent of the 4.0
   kernel's evaluator walls is replaced by a citation of this
   edition's own enumeration in section 16; first-seen survival
   no longer appears as an evaluator wall (R9).
8. Chapter 2 — added whole: the graduated seed, byte-exact
   (structure census, additions).
9. §3, replay obligation — repaired under R5/R11: the
   conformance predicate of section 17 is cited; byte identity
   becomes the stated forward commitment.
10. §3, typed-once paragraph — seam repair: Chapter 2 joins
    Chapter 1 as a typing chapter no later section re-presents.
11. §3, specifies-list — repaired under R16: colored evidence
    leaves the portable-forms list.
12. §4, pin rule — repaired under R8: the two pin kinds
    (self-addressing; external whole-file) with the
    which-bytes/which-bind separation.
13. §4, substrate of record — repaired under R20 (edition
    layer): the verifiable dossier specification is admitted to
    the substrate of record; the engagement companion is bound
    to the ratification enactment's pin.
14. §5, covenant entry — repaired under C-14: the four-tier law
    ladder (predicate < clause < covenant; commitment reserved
    for the substrate act), with the covenant-set double-duty
    reading resolved explicitly at the definition.
15. §5, seal-kinds entry — repaired under R17: covenant-seal
    verification named as a fold.
16. §6 — repaired under 8a: conviction in the medium stated
    observer-conditional (first of the three cross-references).
17. §7, object forms — repaired under R16 (removal by
    identification): three portable forms; the
    colored-evidence entry resolves into the warranted-receipt
    shape, its view echo identified as the finding's
    birth-committed declaration (R13); reinstatement on
    exhibited need stands.
18. §7, cone — repaired under R15: the designation check enters
    the verification cone, with the weight guard.
19. §7, dossier division — repaired under the terminology sweep
    (predecessor line 865): the dossier issuer's signature is a
    carriage commitment, never a warranty; never-blur stated at
    the site.
20. §7, end — added under R18: the conditional blinding mandate.
21. §8.3, inputs — repaired under R1 with R5: the closed triple
    enumerated (bundle as citation-closed span set, registry
    state inside; law head typing the bundle; position;
    whole-log spans closing at committed coordinates; the
    engine profile as lens-side citation whose inertness
    conformance tests); equality under the one conformance
    predicate; findings as immutable facts of positions.
22. §8.3, pending payload — repaired under R3: species enters
    the deduplication key and the canonical order as the fourth
    field; the shared doctrine sentence carried.
23. §8.3, bearing — added under R13: bearing = conviction ∧
    pertinence, flat membership in birth-committed enumerations,
    role dispatch.
24. §8.3, forbidden-table reason — repaired under R14:
    defeated→affirmed lawful only as succession under the
    reversal condition; taint-cure and ground-evaporation
    distinguished.
25. §8.3, evidence ordering — repaired under R14 and R2:
    monotonicity re-scoped to the knowledge order with the typed
    reversal condition (undercut, never rebuttal); full
    discharge stated for every terminal value, partial
    examination a type error.
26. §8.4, taint current — repaired under R6 and R9: first-seen
    survival marked as medium-tier description; contested
    standing succeeded by tainted pending, species
    unresolved-conflict, cured only by an owned act.
27. §8.4 — added under R10 with C-17 §F and C-15: the
    conviction ladder (exhibited/derived axes; the antinomy
    circuit constructor with its payload, bearer, and force; the
    divergence conviction above the codomain).
28. §8.5 — repaired under 11a: the compound product closes
    under refusal; computed components stand; refusal answers
    about the seam.
29. §10, covenant seal — repaired under R17: the three-layer
    split (typed-seal carriage with reserved type; event-seal
    attachment; satisfaction as a fold), the decidable
    admissibility test, portable clause language chartered out.
30. §10, conviction kinds — clarified under C-1: the three-kind
    refusal-ground discipline named as the naming rule this
    document's refusal requirements cite.
31. §11, invoke axis — repaired under R18: pre-disclosure
    custodian commitments carry the blinding factor.
32. §13.2, step 4 — terminology sweep: conferral wording made
    explicitly participial (C-15).
33. §13.2, step 2 — terminology sweep (line-865 kin): the
    dossier's failed composition commitment convicts the
    curator; carriage vocabulary aligned.
34. §13.3 — regenerated under C-13: deployment-scale questions
    stated without the economic register; the
    admitted-not-delivered zero-knowledge paragraph added,
    citing section 19 as the nearer rung.
35. §13.4 — repaired under 8a (second cross-reference).
36. §13.5 — added under C-15 (#19): convergence as geometry —
    different evidence is a different bundle, different law a
    different sheet, same triple same sheet agrees under the
    section-17 predicate; divergence convicts the specification.
37. §14.2 — repaired under 8a (third cross-reference).
38. §15, interpretive latitude — repaired under R20 (domain
    layer): functional-dependency declarations of consumed
    semantics; migration enactments; pin-granularity confession.
39. §16, what is fixed — repaired under R4 with E-1/C-2/R9: the
    seven walls enumerated once in this edition's own text,
    wall 6 as the ambient-order declaration's constitutional
    hook, wall 7 the no-fold-tier-selection retype; membership
    conserved at seven.
40. §16, what is open — repaired under R5: the carriage
    encoding chartered to the group design round, expressly
    non-gating.
41. §17, pins — repaired under succession law and R8: 4.1
    pinned as predecessor of record at its KEL coordinates; 4.0
    and 3.3 superseded through it.
42. §17, cross-implementation deliverable — repaired under R5
    with C-1: the one conformance predicate stated in full
    (semantic full-payload equality, refusal grounds per the
    three-kind discipline, admission sets named through corpus
    identity), byte identity as forward commitment.
43. §18, canonical order — seam repair: the paragraph named as
    a site rule descending from wall 6 (R4; C-17 §E).
44. §18 — added under R15: designation and membership (the
    designation rule at inception grade, the membership face's
    bootstrap refusal, knot-physics singleness, the cone check,
    fail-loud, the sole-authority confession).
45. §18, compact-form gate — superseded by pointer: the gate
    paragraph moves whole into section 19 (seam-rule 2); the
    envelope sentence appears once, there.
46. §18, vectors — repaired under R15: designation and
    membership must-rejects join the boundary family.
47. §19 — added under C-16 with the F-amendment: the compact
    receipt form and its three gates, recomposed from the
    committed gates breakdown — the bundle-commitment rule with
    its two liability layers, the seat-enactment shapes with
    the R19 contingency held open, the vector families, the
    one-way-coverage ground with the register's negative
    exhibit, the transport stratum.
48. Predecessor appendix — superseded by this appendix: the 4.1
    appendix was that edition's own accounting and stands in the
    predecessor's ratified bytes; nothing of it carries forward
    as live apparatus.

### Structure census

Every predecessor section dispositioned; zero unexplained.
"Carried" = re-derived intact (verbatim); "repaired" = carried
with the named ruling's repair; "superseded" = replaced by
named successor text; "dropped" = removed with grounds.

| 4.1 section | Disposition |
|---|---|
| Head | superseded(this edition's head): lineage re-pinned |
| Abstract | repaired(Abstract): R11; C-13 |
| Introduction | superseded(Introduction): two-chapter architecture |
| 1.0 Where this document begins | carried(1.0) |
| 1.1 The smallest governed domain | carried(1.1) |
| 1.2 The five nouns | repaired(1.2): R17 seal admissibility |
| 1.3 The two verbs | carried(1.3) |
| 1.4 The fold axioms | repaired(1.4): generalized commitment; R4/E-1/C-2 wall citation |
| 1.5 The Gever's one discontinuity | carried(1.5) |
| 1.6 Color | carried(1.6) |
| 1.7 The comprehension gate | carried(1.7) |
| 2. Scope and non-goals | repaired(3): R5/R11 predicate; R16 list; Chapter-2 seam |
| 3. Normative language and reading rules | repaired(4): R8 pin kinds; R20 substrate of record |
| 4. Definitions | repaired(5): C-14 law ladder; R17 seal entry |
| 5. The medium | repaired(6): 8a |
| 6. The objects that cross frames | repaired(7): R16, R13, R15, R18, line-865 sweep |
| 7. The finding codomain | repaired(8): R1, R2, R3, R5, R6, R9, R10, R13, R14, 11a |
| 8. Standing | carried(9): covenant-set double duty resolved at the §5 ladder definition, not at the sites |
| 9. The seal ladder | repaired(10): R17 three-layer split; C-1 |
| 10. Rotation policy | repaired(11): R18 |
| 11. The governed object classes | carried(12): seam-rule check run — zero enumeration-over-generation assertions found; the open-enumeration paragraph is the seed's own cited ground |
| 12. The transformation law | repaired(13): C-13; C-15; 8a; sweep; the admitted-not-delivered paragraph; the section-19 pointer |
| 13. Recourse | repaired(14): 8a |
| 14. Federation duties | repaired(15): R20 |
| 15. The openness clause | repaired(16): R4 seven walls; R5 charter |
| 16. Succession and ratification | repaired(17): lineage pins; R5/C-1 predicate |
| 17. The GEL grammar | repaired(18): R15 designation block; wall-6 hook; gate paragraph superseded into 19; vectors extended |
| Appendix of record (D-3) | superseded(this appendix): predecessor accounting stands in ratified bytes; three-census law replaces two-census law per Amendment 4 |

Additions with no predecessor counterpart: this edition's head
and introduction (recomposed); Chapter 2 whole, extracted
byte-exact from the graduated seed (sha256
dfd1ddc1a092225470d2e075c0ad7eec55a4d10e892f38501d763212fcd2bd9a,
its body carried unaltered under its integration heading); the
blinding mandate (§7, R18); the bearing rule (§8.3, R13); the
conviction ladder (§8.4, R10/C-17/C-15); the compound-refusal
closure (§8.5, 11a); the convergence-geometry passage (§13.5,
C-15); the designation-and-membership block (§18, R15); section
19 whole (C-16); this appendix. Zero predecessor sections
unaccounted; zero additions unaccounted.

### Collision-by-addition census

Every carried span re-examined against the nine second-sitting
rulings and the generalized ambient commitment; every span
found defective under new law was repaired and appears in the
delta census; spans examined and found consistent are logged
here so their retention is a decision, never an accident.

Repaired on collision (cross-referenced to delta entries): the
§1.2 seal admissibility (R17 → entry 5); the §1.4 wall import
(R4 provenance → entry 7); the abstract's replay quantifier
(R11 → entry 2); first-seen survival as evaluator vocabulary
(R9 → entries 7, 26); the monotonicity sentence and the
forbidden table's defeated→affirmed reason (R14 → entries 24,
25); "converts to contested standing" (R6 → entry 26); the
discharge-test enumeration (R5/C-1 → entry 42); the custodian
digest-hiding axis (R18 → entry 31); the cone's missing
designation check (R15 → entry 18); the specifies-list and
object forms (R16 → entries 11, 17); line 865's composition
warranty (sweep → entry 19).

Examined and retained, with grounds:

- §6's "cryptographic rather than negotiated" — consistent with
  R17: the medium's three computations are carriage-and-
  attachment-layer objects; satisfaction is typed as a fold in
  the seal ladder, and the medium section never claimed it.
- §13.1's join-reached rule and its "discovery order is
  observer-relative and consulted by nothing" — already
  conforming to the generalized commitment: the bond derives
  from two committed anchors.
- §8.2's pending-species rule — consistent with R3: species is
  already mandatory per element; the key repair lands in §8.3.
- §14.1's grounded-enactment replay ("returns the claimed
  finding") — predicate-neutral; equality reads through
  section 17's predicate wherever findings are compared.
- §15's stated-evidence-scale duty — consistent with the
  divergence tier: a claim naming its scale is what the
  differential instrument audits.
- §18's genus-reservation paragraph — retained unchanged; the
  R19 seat-shape question is expressly held open and nothing
  here closes it.
- §1.1's refusal prose — consistent with 11a: refusal was
  already an operational fact about an ill-posed question, and
  the compound closure composes with it.
- §10's anchor-grade doctrine — consistent with R18: the
  blinding mandate confesses that anchor existence and grade
  stay visible; the two commitments compose.
- §1.6's color and §13's coloring prose — consistent with C-15
  and R16: every retained use is participial or names the
  domain's own fold; no object owns a color anywhere in this
  edition, and no receipt noun anywhere takes color as a
  possession.

Zero carried spans retained defective; zero collisions
unexamined.

Standing obligations this appendix leaves open, named: the
committed census generator against final-form bytes (ceremony
gate); the R11 three-artifact coupling (the abstract's replay
sentence, the public repository's quotation of it, and the
verifier's check move together at publication); the station
obligations of the record and supplements (the R3 regression
vector, the cardinality-3 antinomy circuit, the bearing,
membership, reinstatement, semantics-pin, satisfaction-fold,
and compound-refusal vectors, and the compact-form families of
section 19); the carriage encoding (group round, non-gating);
the R19 seat-shape contingency; the dossier-inheritance answer
at gate one; and the engagement companion's writing and pinning
at ratification (R20). None of these is presumed discharged by
any clause of this document.
