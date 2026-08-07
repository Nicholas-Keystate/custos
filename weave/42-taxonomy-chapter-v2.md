# The governed-object taxonomy — chapter draft v2 (4.2 cycle, seed candidate)

Status: DRAFT v2 for the 42 cycle; not graduated; not ratified.
Re-derived 2026-07-30 under the exhibit/warrant split (named
instances carry comprehension only, never normative ground;
deletion and substitution tests bind). v2, 2026-07-31:
regenerated whole under the GEL-ur-element ruling (2026-07-30);
predecessor weave/42-taxonomy-chapter-draft.md (sha256
2af4c76b39489bc5bd699de2e37e9408be7902b624c5d7f2801c317475bb65df)
superseded whole (chain-not-tree). Inputs
(pin-closure): Custos 4.1 edition of record (sha256
ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05,
ratified KEL sn 187/188) — cited below as "4.1" with line
coordinates into spec/custos-4.1.md; the SEDI source register
ops/held/sedi-register.md (sha256 1bc46ff5…) — the exhibit's
citations resolve to its committed bytes, never to live URLs; the
depth treatment lives in the companion (weave/42-sedi-companion-
draft.md, staging for companions/sedi-alignment.md per shelf 42-3);
ruled arc: threads/gel-wire-grammar.md, GOVERNED-CREDENTIAL
TAXONOMY ARC block. Drafting laws in force: prescription law (this
chapter types, never prescribes), minimal-case-first, computable
consequences never prohibitions, exhibit-never-warrant.

---

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

*End of chapter draft v2. Gauntlet: not dispatched. Graduation: not earned.*
