# Custos 4.1 — Chapter 1: What a Governed Domain Is

> DRAFT — expansion of weave/41-taxonomy-chapter-skeleton.md
> (station 1). Ruling trail: threads/gel-wire-grammar.md.
> Unpinned until declared final. Enters the 4.1 candidate by
> succession; the 4.0 ratified bytes are untouched by this file.
> Sacrosanct-span provenance is recorded in the skeleton; this
> text derives from the banked rulings and carries no drafting
> apparatus in its own bytes.

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
on the seal's own bytes. The covenant seal is admissible only
where lineage, not byte identity, is the invariant; where exact
bytes can be committed, the digest seal is the honest kind, and
substituting the weaker for the stronger is itself a defect. A
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
   state — and the inputs are a committed tuple, never the GEL
   alone: the GEL span, every cited key-event and registry span,
   the law head, and the appraisal position. The replay is the
   receipt of performed governance: an enactment's echo
   testifies, and every stranger who folds again has receipted
   that testimony — receipted in the governance-tier sense, the
   act of independent recomputation; replay mints no witness
   receipt and adds no authentication to the original enactment.
   Two domains holding identical committed tuples hold identical
   Constitutions. A judgment no stranger can recompute is the
   judge testifying where the record should, and the judge's
   testimony is not a fold output.

3. **Refusal.** Where committed law runs out, the fold refuses
   rather than legislates. The refusal names what is missing.
   Discretion at evaluation time is exactly what replay
   eliminates; a fold that interprets has begun to enact.

4. **No ambient order.** Any order the fold consumes — of
   events, of clauses, of evidence — is derivable from
   committed bytes, or is proven irrelevant to the result. An
   uncommitted order that affects a finding is a commitment
   without ground.

5. **Monotone layering.** Each fold consumes the output of the
   fold below it — the Gever presupposes registry state, which
   presupposes key state — and no fold writes into any log. The
   tower reads downward and never writes at all.

These five axioms are the common floor of every fold — and they
are a floor, not the whole house. The ratified evaluator carries
further fixed walls this chapter imports whole rather than
restates: the complete transition system among the four finding
values and its refusal of backward edges, the canonical ordering
and selection of evidence, the distinct upward currents of
defeat and duplicity, first-seen survival, and the rule that
acts consumed as grounds require committed receipts. Those walls
bind by citation with full force; a fold satisfying the five
axioms alone is not yet a conforming evaluator. Everything a
particular domain adds above the ratified walls — the predicates
its law evaluates, the grammar its events speak, the strata it
adopts — is what that domain chose. This standard specifies the
walls and declines to rank the choices: it types the domain and
leaves the taste to the governed.

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
enacted, at this position of its record. Color is the
configured evaluator itself — what this domain can distinguish,
say, and judge — and the Constitution is that color's computed
state: run the fold in force over the committed record and the
Constitution is what returns. One configuration, one output;
the color is the instrument, the Constitution its reading. What
the law binds appears in the Constitution; what the law can
tell apart lives in the color.

Two consequences follow at once. Colors are compared
semantically, never by prose: the comparison runs over the
complete committed inputs — law, cited spans, position — and
asks what distinctions each fold in force can draw, since
syntactically different clause sets may compute the same
distinctions, and identical law bytes over different committed
contexts may not. Where any such comparison binds a
consequence, it is fixture-work, not reading-work. And color is
exactly as replayable as everything else in the domain: a
stranger holding the logs computes what this domain is able to
judge, before ever asking it to judge anything.

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
