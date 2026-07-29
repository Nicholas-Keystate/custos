# Ruling docket — 2026-07-29

Thirteen open findings against Custos 4.1 (sha256
`ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05`)
are blocked on the same thing: two readings survive, each forced by
a different `SHALL`, and choosing between them from the text would
be legislating. `CONTRIBUTING.md` routes that decision to the
ratifying authority — `finding → triage → ruling → repairs executed
under rulings → next candidate edition`.

This document is triage output, not a ruling and not a repair. It
states each decision once, with the options and what each option
commits the standard to, so the thirteen can be worked as a batch
rather than as thirteen threads. **Recommendations are marked as
such and carry no force.** The drafting authority owns the wording;
the ratifying authority owns the ruling.

Nothing here proposes an edit to ratified text.

---

## Why a batch

Drafting is not the bottleneck. Of twenty-three actionable open
issues, thirteen are ruling-blocked, and they include every
BLOCKING finding on the tracker. No amount of further review moves
any of them.

The thirteen are also not independent. **Five rulings unblock the
other eight**, so the ordering below is not arbitrary:

| Rule first | Because it decides |
|---|---|
| **R1 — #7** position-indexed vs state-machine findings | R3 (#24) outright; constrains R4 (#6) |
| **R2 — #28** does the affirmation discipline bind `defeated` | whether #2's canonical-selection repair means anything |
| **R3 — #27** species in the requirement-set key | whether #3's repair is sufficient |
| **R4 — #20** which wall enumeration is canonical | may dissolve R7 (#21) entirely |
| **R5 — #9** which conformance predicate binds | unblocks #11, #14, #15 |

Two of these are preconditions for work already in flight: PR #26
repairs #2 and #3, and its repairs are only meaningful under a
particular resolution of R2 and only sufficient under a particular
resolution of R3. That PR says so in its own notes.

Four rulings touch spans inside §15's fixed walls (R1, R4, R6, and
the transition-system half of R4). Per `CONTRIBUTING.md` property
2, those return as **re-rulings** — the ratifying authority already
ruled on that wording, so it is not quietly patched.

---

## R1 — Are findings position-indexed, or state-machine valued?

**Issue:** #7 · **Severity:** BLOCKING · **Re-ruling:** yes (§7.3
transition system is a §15 fixed wall)

### The question

Does §7.3's transition table constrain the *relation between
findings at successive positions* on one question, or the
*mutation of a single stored value*?

### Why it must be answered

§7.3 forbids `affirmed → defeated` absolutely, and provides no
motion for the prospective termination of a grounding credential's
lifecycle. The §1.1 worked example — "may the holder of credential
X act in role Y?" — sits exactly on that gap: X's TEL emits `rev`,
which is evidence growth at a fixed law head, and the table has no
answer. Three conforming readings exist and they are neither equal
nor nested: the finding stays `affirmed` (force on a revoked
ground), moves to `defeated` (violating the wall), or every
revocable-grounded standing is perpetually `pending` (which guts
`affirmed`).

### Options

**A — Position-indexed.** A finding is an immutable function of a
closed triple (bundle, law head, position). "No flip" means no
finding at a fixed triple is ever rewritten; `affirmed@p` and
`defeated@p′` are two independent lawful findings. Cost: one
clarifying sentence, plus an explicit statement of how a standing
finding's dependence on revocable TEL state is expressed — whether
the cited registry state is part of the closed triple, so a later
position is simply a different triple.

**B — State-machine.** The table describes mutation of a live
value. Cost: a new lawful motion or current for prospective
lifecycle termination, reconciled with the `affirmed → defeated`
prohibition and the §15 wall.

### Recommendation

**A.** L1072's own second clause already points there — "new defeat
evidence yields a new finding at a new position" — and it matches
the case-1 framing in #1 (two views, same law, one having seen
less; `affirmed` vs `pending`, trivially resolved). B requires
opening a fixed wall to add an edge.

A is also the keystone. Under A, R3 (#24) resolves for free, and
R4's hardest sub-question (can antinomy be discovered after
affirmation?) becomes answerable without a new edge.

---

## R2 — Does the affirmation discipline bind `defeated`?

**Issue:** #28 · **Severity:** BLOCKING

### The question

May a fold return `defeated` while enumerated defeater-checks
remain unexamined?

### Why it must be answered

§7.3 L1113–1121 states the discharge discipline for `affirmed` and
names only `affirmed` ("never affirmed"). Read literally it does
not restrain `defeated`. But then the citation changes as the
bundle grows: `defeated(merit, M)` under `B1`, `defeated(crypto,
S)` under `B2 ⊃ B1`. Those are different grounds for one question,
and L1103 in the same paragraph says the larger bundle "refines and
never contradicts" the smaller. The forbidden table has no
`defeated → defeated` row, so the transition system — declared a
complete enumeration — does not reach the case.

### Options

**A — Literal.** The discipline binds `affirmed` only;
short-circuit defeat is lawful. Cost: L1103's monotonicity claim is
false as stated and must be weakened or scoped.

**B — Full discharge.** The discipline binds every terminal value;
an unexamined enumerated check yields `pending`. Cost: stating a
restriction §7.3 does not currently carry.

### Recommendation

**B**, and it is not close. Under A the monotonicity claim in the
same paragraph is falsified. More sharply: **A makes #2's canonical
selection meaningless.** Canonical selection ranges over "multiple
defeats simultaneously available," and under A an engine may return
the first defeat it finds without ever computing that set — so
there is no set to take the least of, and the total order PR #26
supplies has nothing to range over.

That dependency is worth stating plainly: **PR #26's repair to #2
is only meaningful under B.** If A is ruled, #2's repair needs
rethinking rather than merging.

A blind implementation pinned the literal reading, recorded that it
preferred the other, and wrote a regression test asserting the
non-monotonicity as an executable defect. That is the correct
posture for an implementer — reading a restriction into a ruled
span is legislating, which axiom 3 forbids — and it is why this
needs a ruling rather than a clarification.

---

## R3 — Does the species enter the requirement-set keys?

**Issue:** #27 · **Severity:** BLOCKING · **Status:** the only
*executed* cross-implementation divergence on the tracker

### The question

§7.2 (L1007) requires a pending finding to carry the **species** of
each requirement element. §7.3 (L1048–1051) states the dedup and
canonical-order key over subject, kind, and citing clauses — three
fields, not four. Is species in the keys or not?

### Why it must be answered

Two implementations written blind from the ratified bytes resolved
this in opposite directions and emit different `pending` findings
from one committed input: one names a single cure path, the other
names two. §7.3 L1038's byte-identity `SHALL` is falsified today,
in executed form, not in argument.

### Options

**A — Exclude species from the keys.** Forced by L1038: a field in
the element but not in the key makes the "canonical order" a
preorder and the bytes undetermined. Cost: two elements colliding
on the key must be merged and **the document says nothing about
how** — so A is incomplete until a merge rule names the survivor
from committed bytes. The implementer who pinned A had to invent
one and recorded the invention as itself an underdetermination.

**B — Include species in both keys**, appended as the final sort
tiebreak. Forced by §7.2's mandatory-field `SHALL` and by the cure
semantics of L997–1007. Cost: the canonical order as *stated* is
not total and must be explicitly extended.

### Recommendation

**B.** A's cost is not symmetric with B's. Under A a party is told
the cure is "the missing evidence arrives" and is never told a
recovery window is open — a materially different instruction about
what to do next, from the same record. §7.2 exists precisely so a
party can read the cure path off the finding; collapsing species
discards the document's own cure semantics to satisfy a key. B
costs one clause and yields a total order.

**Precondition status:** PR #26's repair to #3 settles direction,
comparison basis, and list semantics, and explicitly does *not*
settle the field set. Until R3 is ruled, that order is total over
three fields and not over the element, so L1038 stays unsatisfiable
for the colliding case regardless of the ordering fix.

---

## R4 — Which enumeration of the fixed walls is canonical?

**Issue:** #20 · **Severity:** MAJOR · **Re-ruling:** yes

### The question

§1.4 (L279–287) names five walls; §15 (L2052–2062) names six. Four
correspond; each list carries two the other omits. §15 also says
the six are "each carried by ratified text in this document," while
§1.4 says its walls are "imported whole rather than restated" from
the 4.0 kernel. Both the membership and the provenance disagree.

### Options

**A — One enumeration, in one place**, with every other mention
citing it rather than restating it. Includes one answer on
provenance: carried by 4.1's own text, imported by referent, or
explicitly split with each item assigned.

**B — Two lists with distinct declared subjects** — e.g. §15
enumerating openness-clause boundary commitments and §1.4
enumerating evaluator-conformance obligations — each naming its own
subject explicitly.

### Recommendation

**A.** A count in ratified prose ("These six are walls") is a
commitment, and a list restated in two places will drift again at
the next candidate — it already has. If B is ruled instead, each
list needs its subject named in ratified text, because on the
current bytes they read as two attempts at the same list.

**Knock-on:** if A resolves toward "carried by 4.1's own ratified
text," the §1.4 import disappears and **R7 (#21) dissolves**. Rule
R4 before spending effort on R7.

---

## R5 — Which conformance predicate binds?

**Issue:** #9 · **Severity:** MAJOR

### The question

§2 (L423–425) and §7.3 (L1038) make byte-identity the
class-defining obligation. §15 (L2069–2072) leaves the carriage
encoding an undesigned deliverable, so byte-identity has no
referent yet. §16 (L2141–2143) tests something else entirely —
equal corpus identities, admission sets, refusal grounds, and cited
law heads. Three predicates, one obligation.

### Options

**A — Pin the encoding now** to the substrate's canonical
composable form (insertion-ordered CESR + SAID). Byte-identity
becomes testable and §16 tightens to match §2. Cost: converts a
§15 openness deliverable into ratified law — a design act needing
its own review round, not an editorial one.

**B — Restate the obligation semantically** as §16's enumerated
equalities until the encoding lands. Cheaper and honest; weakens
the sentence that distinguishes Custos from improvised governance.

### Recommendation

**B now, A later.** B unblocks #14 and #15 immediately — a
differential harness cannot be built until it knows what it is
diffing — without committing the standard to an encoding under
time pressure. Either way, §2, §7.3 and §16 must end up using
**one** predicate; that unification is the ruling's real content.

---

## R6 — What does "contested standing" return?

**Issue:** #24 · **Severity:** BLOCKING · **Re-ruling:** yes
(§7.4's upward currents are an imported wall)

### The question

§7.4 (L1161) says a lower-tier self-conviction converts what was
affirmed above to "contested standing." The phrase appears exactly
once, is undefined, and is not a member of the four-valued
codomain that §15 fixes as the evaluator's return type "and nothing
else."

### Options

**A — Not a finding.** It is a lifecycle or operational state that
§7.5's separation rule excludes by construction. Cost: the "duplicity
taints upward" wall then returns nothing a verifier can consume,
and "converts" is the wrong verb for a finding that does not change.

**B — `pending` with the taint as its typed requirement.** Keeps
everything in-codomain. Cost: under a state-machine reading this is
the forbidden `affirmed → pending` edge.

**C — A fifth codomain value.** Breaks the §15 wall. Listed for
completeness; not viable.

### Recommendation

**Rule R1 first — this is downstream of it.** Under R1/A
(position-indexed), B becomes available and clean: the taint
produces a *new* `pending` finding at a *new* position, with the
taint as its typed requirement, and no forbidden edge is crossed
because nothing mutates. Under R1/B (state-machine), B is
unavailable and A is forced, along with an explanation of what
"converts" means for a value that cannot change.

That asymmetry is itself an argument for R1/A.

---

## R7 — How is §1.4's imported extent made computable?

**Issue:** #21 · **Severity:** MAJOR · **Read R4 first**

### The question

§1.4 imports "the evaluator sections" of the 4.0 kernel "whole
rather than restates." The phrase "evaluator sections" is defined
nowhere, no section numbers are given, and the five named walls are
not co-located: four sit in 4.0 §6, but the receipts wall sits in
4.0 §14 — the openness clause, whose other content is the explicit
enumeration of what the kernel does *not* design.

### Options

**A — Name the imported units by section number.**
Demonstrably impossible as stated: no section list yields exactly
the five named items and nothing else. Importing §6 whole omits the
receipts wall; importing §14 whole additionally imports "what is
open" and "what is unresolved," which are the opposite of walls.

**B — Pin by quoted span**, so a verifier can determine the
imported preimage exactly rather than inferring it from a
description.

### Recommendation

**B**, on the ground that A is not available. Plus one sentence on
the interaction between §16's whole supersession of the predecessor
and §1.4's partial re-incorporation of it — on current text a
reader can reasonably conclude either that the imported walls
survive supersession or that they were superseded and are merely
described.

**But rule R4 first.** If the walls end up carried by 4.1's own
text, there is no import and this question does not arise.

---

## R8 — What is the preimage of a whole-file pin?

**Issues:** #23 (BLOCKING) and #4 (OBSERVATION, corroborated) ·
**Recommend ruling as one**

### The question

`spec/custos-4.0-kernel-draft.md` opens with a 12-line header
declaring itself "scaffolding … stripped at ratification," and
4.1's appendix (L2350) agrees: "ruled: never ratified bytes." But
the digest pinned everywhere as the 4.0 edition of record —
`9cefdc5d5842…`, in `SUCCESSION.md` L12, in 4.1 at L5/L281/L2107/
L2317, and checked by `tools/verify_kernel.py` — is the digest of
the whole file, header included. The ratified extent hashes to
`f529388df9fc…` instead.

Separately, §3.2's reading rule states one pin discipline
(same-length placeholder in the digest's own field, 44-character
profile) which does not describe whole-file sha256 pins at all.
Two independent routes to the same gap: the pin form carrying the
document's most load-bearing commitments has no stated discipline.

### Options

**A — Re-pin to the ratified extent.** Cost: `9cefdc5d5842…` is
already anchored in the governance event log at sn 187/188 and
appears in five places. A correction is itself a succession-grade
act, not an errata edit.

**B — State that the pin is over the file-as-published**, with the
header inside the committed preimage though non-normative in
content. Cost: one clause, and the mild awkwardness of a preimage
containing bytes ruled non-normative.

### Recommendation

**B**, combined with a §3.2 repair covering both pin kinds — (a)
self-addressing SAID pins via same-length placeholder-in-field,
naming the placeholder character, and (b) external whole-file
digest pins, defining whether the preimage is the published file
or the ratified extent.

B makes the existing anchors correct without re-anchoring committed
history, and it is truer to the standard's own thesis: the
computation stands, and the ruling about normativity is a separate
statement from the ruling about the preimage. A asks the governance
log to correct a digest it already anchored, which is a much larger
act for the same end.

---

## R9 — Is survival ordered by committed bytes or by observation?

**Issue:** #25 · **Severity:** MAJOR

### The question

§1.4 imports "first-seen survival" as a binding wall. Its source
text (§7.4 L1159–1160) says "first-seen survives." But axiom 4
(L265–270) requires any order the fold consumes to be derivable
from committed bytes, §17 (L2207–2211) says an implementation whose
fold result depends on arrival order does not conform, and §7.3's
Inputs clause excludes ambient configuration entirely.

### Options

**A — Committed order.** Name the total order the survivor is
minimal under, derived only from committed bytes; if that is §17's
canonical consumption order, cite it. Retire or redefine
"first-seen," since the phrase names the one thing the fold may not
consult.

**B — Observation order.** Then axiom 4 and §17 need an explicit
stated exception rather than an inferred one.

### Recommendation

**A**, decisively. Both blind implementations pinned A independently
*and both recorded that they were overriding the clause's plain
words to do it*. A wall that every careful implementer must
silently reinterpret before it can be implemented is not yet
stated. B would gut axiom 4 for the sake of a phrase.

Worth noting for the record: this is a defect **4.1 created**. The
4.0 kernel carries the same §7.4 sentence but has neither axiom 4
nor §17 — the collision came into existence when 4.1 added them
around unchanged predecessor text. It is also one of the two items
§1.4 lists that §15's enumeration omits (R4), so it currently rests
on a single clause with no corroborating statement.

---

## R10 — Antinomy: payload, bearer, and reachability

**Issue:** #6 · **Severity:** BLOCKING · **Re-ruling:** yes ·
**Intent already signalled**

### Status

Unlike the rest of the docket, the direction here is already on the
record. The `pending → self-convicted` edge admits "a bearing
contradictory pair, **or** new governed-status evidence," while the
required payload (L1052–1053) is the contradictory pair's proof —
so the second trigger is reachable with no payload that satisfies
its own `SHALL`. In #1 the second trigger is identified as
**antinomy**: a contradiction sited in the committed law rather
than in the subject's bytes, indicting the GARD and its
administrators, with the checkbox "Update the `self-convicted` cell
with Antinomy type to go alongside Duplicity."

So the repair is **not** deleting the `or`. Three sub-questions
remain.

### The sub-questions

1. **Payload.** An antinomy has no "contradictory pair" in the
   duplicity sense, so it cannot borrow duplicity's payload clause.
   What must it carry — the proof object exhibiting the two
   grounded conclusions that cannot jointly stand, plus the
   enactment signatures that committed the producing clauses?
2. **Bearer.** An antinomy convicts the GARD and its
   administrators, not the subject. That is a different convicted
   party from every other path into this cell, and §7.4's
   law-relative force distinction does not currently cover it.
3. **Reachability.** The current table admits the second trigger on
   the `pending →` edge only. If an antinomy in the law can be
   discovered *after* a question was affirmed, there is no edge for
   it — the same shape of gap as R1.

### Recommendation

Sub-question 3 is the one that matters, and it is **downstream of
R1**. Under position-indexing it needs no new edge: the antinomy
produces a new terminal finding at a new position. Under a
state-machine reading it needs a new motion into a terminal value
from `affirmed`, which is a second opening of the same wall.

---

## R11 — Refusals: scope the claim, or commit a record?

**Issue:** #10 · **Severity:** MAJOR

### The question

The abstract (L29) promises a stranger recomputes "the same
refusals, byte for byte." The body classifies refusal as "not a
finding … recorded as an operational fact" (L1199–1201), excludes
it from the codomain (L967–972), and scopes §2's replay obligation
to "every judgment" (L424) — and a refusal is expressly not a
judgment. Whether a refusal is a committed replayable artifact is
openness-question 1 (L2079–2081).

### Options

**A — Scope the claim.** The stranger recomputes the same
Constitution and findings byte for byte; refusals replay as
*decisions* derivable from the same committed triple. Leaves
openness-question 1 open, which is where the document stands.

**B — Commit a refusal-record form**, resolving openness-question 1
in the same act. The abstract's current sentence then becomes true
as written.

### Recommendation

**A.** B decides a ratified openness question and is a
substantially larger act.

**Coupling to flag either way:** the abstract is not a free
surface. `README.md` L20 quotes this sentence byte-identically and
`tools/verify_kernel.py` check 3 enforces that the README quotes
rather than paraphrases. Any change to L29 is a three-artifact edit
that must move together, and the verifier is the guard that proves
it happened.

---

## R12 — Is "predicate congruence" worth renaming?

**Issue:** #5 · **Severity:** OBSERVATION

### The question

"Digest congruence" (SAID equality) is a true equivalence.
"Predicate congruence" — "rules of one Constitution that another's
committed rules satisfy" — is directional satisfaction, a
subsumption preorder. Is the shared noun a defect or a genus term?

### Options

**A — Rename** the directional relation to predicate *subsumption*
or *satisfaction*, reserving "congruence" for the symmetric digest
relation.

**B — Leave it**, declaring "congruence" a genus term meaning
overlap-at-a-grade, which is what §12's own framing already says
("the overlap is measurable at two grades").

### Recommendation

**B — rule it to close the thread, not to change text.** This is
the lowest-value item in the docket. §12 has already defused the
consequence: the comparison is computable only under a stated lens,
no canonical algorithm is committed, predicate congruence travels
at conjecture grade, and "congruence of either grade is evidence,
never force. It confers nothing." A reader who wrongly assumes
symmetry cannot cash the assumption into any machine consequence.
The blast radius is zero, and a rename costs a succession ceremony.

Recorded so the next reviewer who raises it finds the reasoning
rather than raising it again.

---

## Summary table

| # | Ruling | Issue | Sev | Re-ruling | Recommendation | Blocked by |
|---|---|---|---|---|---|---|
| R1 | Position-indexed vs state-machine findings | #7 | BLOCKING | yes | Position-indexed | — |
| R2 | Affirmation discipline binds `defeated`? | #28 | BLOCKING | no | Full discharge | — |
| R3 | Species in the requirement-set keys? | #27 | BLOCKING | no | Include | — |
| R4 | Which wall enumeration is canonical? | #20 | MAJOR | yes | One list, one place | — |
| R5 | Which conformance predicate binds? | #9 | MAJOR | no | Semantic now, bytes later | — |
| R6 | What does "contested standing" return? | #24 | BLOCKING | yes | New `pending` at a new position | R1 |
| R7 | §1.4's imported extent | #21 | MAJOR | no | Pin by span | R4 |
| R8 | Preimage of a whole-file pin | #23, #4 | BLOCKING | no | File-as-published + two-form §3.2 rule | — |
| R9 | Survival: committed order or observation? | #25 | MAJOR | no | Committed order | — |
| R10 | Antinomy payload, bearer, reachability | #6 | BLOCKING | yes | Own payload; reachability follows R1 | R1 |
| R11 | Refusals: scope or commit a record? | #10 | MAJOR | no | Scope the claim | — |
| R12 | Rename "predicate congruence"? | #5 | OBSERVATION | no | Leave it; close the thread | — |

Twelve rulings over thirteen issues — R8 covers #23 and #4 together.

## What is not in this docket

Nine open issues need no ruling and are drafting or program work:
#8 (warranty framing — aligning three sites to a grade the abstract
already ratifies), #11 (the ordering-semantics declaration), #12
(Spec-Up-T), #13 (projection vs ToIP's PR model), #14 (second
implementation), #15 (conformance vectors), #16 (warranty dispute
economics), #17 (deferred surfaces), #18 (working group), #19
(divergent-verdicts section).

Of those, #15 is the one worth starting before any ruling lands.
The discriminating inputs for R2, R3, R9 and #2 are already
described precisely enough to execute; written as vectors that
record both readings and assert only that two engines must agree,
they need no ruling to be valuable and become the regression suite
the moment rulings land. #27 is the proof of the method: an
executed divergence settled in minutes what argument had left open
across a full gauntlet round.
