# The Verifiable Dossier as a Committed Gluing

**Status:** informative companion, draft v0.2 (2026-07-31),
against the ratified 4.1 kernel. Not normative — for Custos, for
the ToIP *Verifiable Dossiers* specification, or for anyone else.
Written for that specification's author and for any implementer
of dossier verification.

**v0.2 supersedes v0.1, which mis-drew the central object:** it
described a dossier as a "path of splices" carrying a fact from
issuer to verifier — that is a credential *chain*, the very
object the dossier specification exists to be distinguished
from. A verifiable dossier is issuer-centric, has no issuee
("affidavit, not passport"), and is a *curated evidence graph*
verified by recursive traversal at a reference time. The
correction is on the record because it strengthens the thesis:
the graph reading is where the mathematics actually lives.

**Citations** are to the ToIP KSWG *Verifiable Dossiers* draft
(Hardman/Provenant), by section name with the version pinned to
our held copy (v0.6 build 2026-05-22) — the draft moves, section
names travel better than numbers. Prior contact between that
specification and this program: the twelve-touchpoint comparison
of 2026-06-12, which this companion extends in one direction
only. Per the kernel's travel discipline, nothing here proposes
text for another community's specification; where this document
raises a question, the question travels as a question.

---

## 1. The claim in one paragraph

A verifiable dossier is a *proposed gluing*: a curator assembles
evidence born in many sovereign worlds — credentials from
issuers, wrapped foreign artifacts, oracle observations,
jointly-endorsed instruments — into one graph that purports to
support one account of the facts. No single authority ever
decided that account; each piece was decided only in its own
world, by its own logs. What the curator asserts, and what the
verifier checks, is that the pieces *cohere*: that the graph's
edges compose, that each cited identification was live at the
reference time, that locally decided facts assemble into one
globally decided account. Verification-by-recursive-traversal is
exactly a composition check. This reading changes nothing about
what the specification already does — it explains *why* its
mechanisms have the shapes they have, and it predicts the one
place assemblies will fail that no current verifier tests: where
the trust graph between ecosystems stops being a tree.

## 2. The vocabulary, grounded in the specification's own objects

**A committed fact** is anything a stranger recomputes from
logs: key state at an event, a TEL issuance not revoked, a SAID
matching its bytes. Inside one authority's cone such facts are
*decided* — replay settles them; two honest verifiers cannot
disagree.

**A splice** is a committed identification that connects
sovereign worlds — signed, anchored, citable, and carrying
state. The specification already has a taxonomy of splices,
richer than plain credential edges, and each entry earns its
seat in this reading:

- an **ACDC edge** is the ordinary splice: this entry's subject
  IS that identifier's controller;
- a **bridge wrapper** is a splice into a foreign estate — a
  bridging party verifies an X.509 / W3C VC / mDL artifact under
  declared policy and commits the identification as an
  attestation; the two revocation lifecycles stay decoupled
  unless a governance framework links them (the specification's
  own caveat, which is precisely where a cascade covenant
  belongs);
- an **observation attestation** is a splice onto dynamic state
  — an oracle binds an observed fact at a time to a committed
  artifact; time itself enters evidence only this way;
- **joint issuance** (the M / RM / Q / FIN edge operators) is a
  *multi-party* splice — one identification committed under a
  threshold of endorsers, with revocation lawfully asymmetric;
- an **annotation edge** (`admitted`, `stricken`) is a splice
  *state transition*: the original artifact is preserved and the
  identification's standing changes prospectively, with a
  receipt. This is the same discipline a TEL applies to
  credentials — issuance opens an identification, revocation
  closes it on the record, nothing is erased — executed at
  document granularity. The two mechanisms were specified
  independently and converge exactly (a fact already on record
  in the touchpoint comparison); in this companion's terms, both
  are ledgers of *which identifications an authority currently
  maintains*.

**An assembly** is the dossier itself: a graph of splices plus
the evidence to replay each one. The fact that arrives at the
verifier — "this brand may originate calls under that number,"
"this officer may sign for that entity" — was decided in *no*
single world. It is decided only by the assembly, at a reference
time, or it is not decided at all.

## 3. What verification is

Per splice: replay the source world to the anchoring coordinate
(keys valid then?), replay the identification's state ledger
(open then? open now, if currency is required?), check schema
and binding. Per assembly: traverse the graph and check that the
ends meet and the composition holds — that the account the
curator proposes actually *descends* from the locally decided
pieces.

Two structurally different kinds of connection hide inside that
traversal, and the distinction pays:

- **Delegation is not a splice.** A delegated identifier's
  establishment is anchored *inside* the delegator's log: one
  composite complex, one replay, and the question "is this
  delegation real" is decided the way in-log facts are decided.
  Failures here are ordinary verification failures.
- **Everything in §2's taxonomy is a splice**: an identification
  *between* worlds neither of which contains the other,
  defeasible over time, carried by its own committed state.
  Failures here are evidence about an edge — revoked but
  presented, stricken but relied upon, wrapper current but
  foreign credential dead.

The issuer-centric, no-issuee design is this distinction taken
seriously: an affidavit is a *local section sworn by its
author* — it never pretends to be the global account. The
dossier never claims the gluing succeeded; it *proposes* the
gluing, and the verifier computes, at the reference time,
whether the proposal holds. That is why reference time belongs
to the verifier, not the curator — and why it wants to be
expressible as a log coordinate (a first-seen position) rather
than only as civil time, with civil time entering through the
specification's own oracle pattern. A gluing check keyed to a
coordinate is replayable arithmetic; keyed only to a clock, it
is testimony about a clock.

## 4. The ledger lineage — why this is the next entry in an old book

Single-entry bookkeeping is a bare log: a list, no check.
Double-entry added the first conservation law — every
transaction posted twice *within one entity's books*, so one
ledger carries an internal coherence test, the trial balance.
Triple-entry (Grigg's construction — the signed receipt shared
between counterparties, "the receipt is the transaction") moved
the check *between* books: the receipt is a committed
reconciliation between two parties' records. Note what that is
in this companion's vocabulary: a splice. KERI's receipts,
seals, and anchors are triple-entry bookkeeping generalized from
money to key state; the dossier specification generalizes it
again, from key state to arbitrary evidence — wrappers,
observations, joint endorsements are all receipt-shaped.

Now the question this lineage teaches you to ask: **what is the
trial balance of the receipt layer itself?** Double-entry's
genius was not the two entries — it was the balance check.
Triple-entry as deployed never built its check: receipts are
pairwise, and nothing anywhere asks whether the receipts
*themselves* cohere when composed around a cycle. Blockchains
escaped the question by force: one global ledger, one total
order, majority-selected, every local view that loses the fork
race orphaned. One book needs no reconciliation — at the price
of a consensus regime and the deletion of losing truths.
Ecosystems of sovereign authorities cannot pay that price. They
keep many books and hold receipts — which means they owe the
balance check that one-book systems abolished. That check does
not exist today, in any specification, ours included.

## 5. Where assemblies will fail: trees, cycles, and the third book

Today's deployed trust graphs are trees. The vLEI ecosystem has
one root; authority flows outward; two distinct paths between
the same endpoints do not exist. In a tree, if every splice
checks, the assembly checks — composition can never fail
independently. Every current verifier silently relies on this,
and rightly so. It is not a flaw; it is an unstated assumption
with an expiry date.

The expiry arrives with cross-recognition. The moment ecosystems
recognize each other — a mobile-network consortium recognizes a
healthcare trust community recognizes a state trust list
recognizes the consortium — the graph acquires cycles, and two
facts hold simultaneously:

1. every bilateral recognition can be individually valid,
   current, honestly maintained; and
2. carrying an identification around the loop — translating it
   A→B, B→C, C→A under the committed instruments — can fail to
   return what it started with.

No splice is broken. No party is dishonest. No pairwise audit
can find the defect, because it does not live in any pair — it
lives in the triangle. Conflict-of-laws has known this failure
for centuries as *renvoi*, and its standing lesson is that the
cure is never another bilateral instrument; it is a multilateral
one that closes the triangle explicitly. Dossiers will be where
this bites first, because a dossier is precisely the artifact
that *walks* the trust graph: an assembly curated in one
ecosystem and consumed in another, through a recognition edge
that sits on a cycle, is a proposed gluing whose composition
check is no longer covered by the tree assumption — and no
verifier performs any other.

## 6. The loop test — implementable today, out of the specification's own parts

1. From the assembly's citations, enumerate the recognition and
   bridge edges it relies on (the wrapper attestations and
   recognition instruments, by SAID).
2. If the relied-upon edges lie on a cycle of the recognition
   graph, walk the cycle: apply each committed translation, in
   order, to the assembly's binding claims.
3. Byte-compare arrival against departure. SAIDs make the
   comparison exact rather than interpretive; a reference time
   expressed as a log coordinate makes the walk replayable
   rather than testimonial.
4. A mismatch is a **loop finding**: evidence that the cycle's
   instruments do not compose, attributable to the cycle as a
   whole, prior to any assignment of fault. And the finding has
   a natural carrier *already in the specification*: it is an
   observation attestation — an oracle observed a computable
   fact about dynamic state (the cycle's composition, at a
   time) and committed it. A federation's trial balance can
   travel as evidence inside the very dossiers that depend on
   it.

This is a conformance test for *federations*, not credentials —
a class of test that exists nowhere in the stack today. An
accountant recognizes it instantly: pairwise receipts are
entries; the loop test is the trial balance.

## 7. Four MAY-grade thoughts, offered for digestion

1. **The governance coordinate.** The `gov` metadata field
   already motivates procedural legitimacy; a bare SAID or URI
   has no *as-of*. The coordinate form — registry SAID plus log
   position — was proposed in the touchpoint exchange and
   matters doubly here: it stamps each splice with the law-chart
   it was committed under, which is what makes cross-chart
   composition a checkable claim instead of an assumption.
2. **Relied-edge enumerability.** The citation model already
   carries what an assembly cites; making the recognition and
   bridge edges *enumerable as a set* from the assembly alone
   turns step 1 of the loop test into computation rather than
   reconstruction.
3. **Cycle disclosure.** A curator who knows the assembly's
   edges touch a recognition cycle can say so — a one-bit
   confession that tells the verifier the tree assumption does
   not hold here, exactly parallel to the specification's
   existing instinct that redaction, wrapping, and observation
   must each announce themselves.
4. **Loop findings as first-class evidence.** If a loop finding
   is an observation attestation, then annotation edges give it
   a lifecycle (admitted into a federation's record, stricken
   when the cycle is repaired) and dossiers give it
   distribution. The trial balance becomes self-carrying: the
   evidence layer transporting the evidence of its own limits.

None of these changes what a dossier asserts. They make the
composition check — the one check that today rests on an
expiring assumption — computable by strangers, the standard
every other layer of the stack already meets.

## 8. The ladder, for readers who want the mathematics

The picture has a standard home. Facts decided in one world are
*local sections*; splices are *identifications on overlaps*;
whether local data assembles into one global account is the
*gluing* problem; the obstructions are graded:

| Degree | Object here | Decided by | Characteristic failure |
|---|---|---|---|
| H⁰ | one world's committed facts; delegation | replay of one complex | in-log duplicity — the pair convicts |
| H¹ | splices: edges, wrappers, observations, annotations; the TEL as their state ledger | pairwise coherence at a reference coordinate | revoked-but-presented; stricken-but-relied-upon |
| H² | cycles of recognition and bridge instruments | loop replay — the trial balance | bilaterally clean, triangle open: no pair convicts, only the loop reveals |

One constant runs up the ladder: the incriminating object is
always *a pair that cannot cohere* — two events at one
coordinate, a revocation and a presentation, a departure and an
arrival that differ. Each degree only widens where the pair can
hide, and each degree's instrument is replay over a wider cover.
The relevant classical statement for two worlds is the
Mayer–Vietoris principle; everything used here is finite, exact
at this scale, and computable by replay — no infinities, no
conjectures. The reason to say this at all: sixty years of
theorems about when local consistency does and does not imply
global consistency come along free, and they say the triangle
level is not optional — it is the first level at which honest
parts can make a dishonest whole. (References: any standard
treatment of sheaves and Čech cohomology, e.g. Mac Lane &
Moerdijk; the governance-side derivation lives in the program's
annealing record and travels here as companions mature.)

## 9. Status and custody

Draft for one reader's digestion; v0.2 corrects v0.1's central
object on the record (chain → curated graph), per the program's
supersession-not-erasure discipline. Claims about KERI/ACDC/TEL
mechanics are replayable against keripy at the program's pinned
checkout. "Verifiable dossier" and the mechanism vocabulary
(bridge wrapper, observation attestation, annotation edge, joint
issuance operators, evidence curator) are the dossier
specification's own, cited never retitled; "renvoi" is standard
conflict-of-laws vocabulary; "trial balance" is standard
accounting vocabulary; triple-entry is Grigg's construction
(Ijiri's momentum accounting is an unrelated homonym). The tree
observation about vLEI describes the current deployment and is
not a criticism. The loop test claims novelty only as *deployed
practice* — the mathematics is classical, which is a feature:
the test's authority should rest on replay, not on us.
