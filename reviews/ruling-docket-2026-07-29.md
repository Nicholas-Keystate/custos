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

**Second batch appended 2026-07-30.** Six further rulings, R13–R18,
were added a day after this docket was assembled, from findings the
parsimony review round filed on 2026-07-30 (#32, #33, #35, #38, #39,
#44). Three are BLOCKING. R11 also gains a named sub-question (#41)
rather than being assumed to cover it. R1–R12 are unchanged; the
second batch begins after R12 and the summary table carries both.

---

## Why a batch

Drafting is not the bottleneck. Of twenty-three actionable open
issues, thirteen are ruling-blocked, and they include every
BLOCKING finding on the tracker. No amount of further review moves
any of them.

*Updated 2026-07-30:* the tracker has since grown. Of forty-four
open issues, twenty are ruling-blocked, and the ratio held —
further review produced six more rulings and closed none. That is
the argument for batching restated as evidence.

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

*Correction, 2026-07-30:* the coupling is looser than stated above.
Check 3 is an **excerpt** discipline, not a byte-identity one — its
own comment reads "Trimming is lawful; paraphrase is not", and it
passes when the README's quoted span is a contiguous substring of
the edition's abstract. So the README may lawfully quote a shorter
span and stay green, which lowers the cost of B. The three-artifact
framing overstates it.

### Sub-question 11a — what does a compound result return when one component refuses? (#41)

Named here rather than assumed covered. §7.5 (L1184–1195) mandates
a product former over components, defined only over findings, while
refusal is expressly not a codomain value. Nothing states the
product's value when one component refuses, and both readings
conform: refuse the whole invocation, discarding components already
computed; or return a product with a refused coordinate, which is
an object outside what §7.1 says the evaluator returns.

This is reachable in ordinary use — a compound standing question
routinely contains an unsatisfied slot (pending) and an
uncomposable one (refusal) at once. Whichever way R11 goes, this
needs an explicit answer, and the ruled text sits inside §7.5's
quoted amendment block, which is less free than ordinary ratified
prose.

**Recommendation:** decide it with R11 in the same sitting. If R11
takes A (scope the claim), the natural companion is that a refusing
component refuses the invocation, and the partial components are
not returned — but that should be stated, not inferred.

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

# Second batch — appended 2026-07-30

Six rulings from the parsimony review round of 2026-07-30, which
closed a day after this docket was assembled. Three are BLOCKING.
They are ruling-blocked for the same reason the first twelve are:
in each, two readings survive and choosing between them from the
text would be legislating.

Two carry over into the first batch's ordering:

| Rule first | Because it decides |
|---|---|
| **R2 — #28** does the affirmation discipline bind `defeated` | largely dissolves R14 (#33); rule R2 first |
| **R10 — #6** antinomy payload and bearer | shares its subject matter with R13 (#32); rule them together |

The other four are independent of the first batch and of each
other.

---

## R13 — What does "bearing" mean at the registry and governance tiers?

**Issue:** #32 · **Severity:** BLOCKING · **Read with R10**

### The question

"Bearing" gates every edge into `self-convicted` (L1062, L1065,
L1066), terminality (L1085), and §13.1's recourse trigger (L1824).
It is given a decision procedure at exactly one tier — the key
tier, where §7.1 (L957–959) defers to the substrate's
superseding-recovery rules. The four-valued scheme is instantiated
at all three tiers (L961–965). Nothing states how a verifier
decides bearing at T2 or T3, including for the Gever — the
evaluator this standard exists to specify. "Bearing" is not among
§4's defined terms.

### Why it must be answered

`self-convicted` is terminal and unrehabilitatable (L1087–1089).
Two verifiers who resolve bearing differently reach permanently
different terminal states from identical committed evidence, and no
later evidence reconciles them. That is the most expensive class of
divergence the standard admits.

The natural reading — bearing is a matter for the domain's own law
— makes it worse rather than better, because it collides with a
second rule. If law is silent on *bearing*, axiom 3 says refuse. If
law is silent on the *violated predicate*, §7.4 says consume as
evidence and do not refuse. **From inside the fold the two are
indistinguishable**: in both, committed law fails to speak to the
pair in front of you. The dispositions are opposites. A blind
implementation hit exactly this and pinned a refusal it was not
confident in.

Both available moves violate a ruled span, which is what makes this
BLOCKING rather than a clarification request.

### Options

**A — Bearing is substrate-deferred at every tier.** Extend §7.1's
key-tier procedure downward: a pair bears unless a committed
superseding rule reconciles it, at T2 and T3 as at T1. Cost: the
governance tier has no analogue of superseding recovery, so the
rule would have to say what plays that role, or say that nothing
does and every governance-tier pair therefore bears.

**B — Bearing is a committed predicate of the domain's law.** The
domain names it; a fold that cannot locate it refuses. Cost: a
stated rule distinguishing law-silent-on-bearing (refuse) from
law-silent-on-the-violated-predicate (consume), which is the
distinction currently unavailable from inside the fold. Without
that, B does not close the finding.

**C — Bearing is definitional, not evaluative.** Add it to §4 with
a procedure that makes it decidable from committed bytes at every
tier, so no per-domain latitude arises.

### Recommendation

**B, and only with its second half.** A is cheapest but pushes the
problem into an analogue the governance tier does not have. C is
the largest act. B matches §1.4's framing that the predicates a
domain's law evaluates are what that domain chose — but B is not a
repair unless the refuse/consume boundary is drawn in the same
ruling, because that boundary, not the definition, is what the
blind implementation could not resolve.

Rule with R10: both concern what reaches `self-convicted` and what
it must carry, and rulings that disagree would be worse than either
alone.

---

## R14 — Where does a finding go when evidence falsifies the cited defeat?

**Issue:** #33 · **Severity:** BLOCKING · **Sequence after R2**

### The question

A finding is `defeated(merit, M)`. At the same law head and
position, the bundle grows to include evidence that clause `M`'s
own enactment failed cryptographic verification, or was made by an
actor lacking the invoked power. Where does the finding go?

### Why it must be answered

Every destination is closed by ratified text. Staying
`defeated(merit, M)` cites a defeat the committed bundle falsifies,
against the Ground Axiom. `affirmed` is a forbidden edge and
contradicts rather than refines the smaller bundle's appraisal.
`pending` is forbidden from `defeated`. `self-convicted` requires a
bearing contradictory pair from the *subject's* own bytes, and the
defeater's invalidity is not the subject's contradiction. An act is
the table's own escape hatch, but no act occurred — only evidence
arrived.

The case is not hypothetical: two of the four ratified defeater
classes are undercutter-shaped (L1129–1132) — `crypto` and
`authority` — and both can apply to the defeating clause's own
enactment.

§7.3's answer to reinstatement is that it happens as an act at a
new position, which is coherent and is scoped to match (L1104–1106,
monotonicity at a fixed law head and position). But an act changes
the law head and so escapes that scope. Evidence does not. The
answer covers rehabilitation by act and leaves invalidity
established by evidence alone with nowhere to go.

### Options

**A — Defeat is indefeasible by evidence.** A defeater's own
invalidity is reachable only through an act. Cost: one sentence,
plus the admission that this is a substantial expressiveness limit
a reader will not infer. State it explicitly or it will be
rediscovered.

**B — The requirement space includes the defeater's own validity
checks.** Then the affirmation discipline must bind `defeated` too,
not only `affirmed` — which is precisely R2/#28's repair, and this
finding becomes a consequence of it rather than an independent
defect.

**C — Name a lawful destination** for evidence-established
defeater invalidity, which means opening the forbidden table.

### Recommendation

**Rule R2 first, then revisit.** Under R2/B (full discharge), this
largely dissolves into option B here: short-circuiting to
`defeated` with the defeater's own validity unexamined would no
longer be reachable, so the trap state would not be manufactured in
the first place. If R2 goes the other way, R14 needs its own
ruling, and A is then the cheapest honest answer.

Worth deciding alongside: whether undercutters are a distinct
category. `crypto` and `authority` attack applicability rather than
content, and the literature holds such attacks succeed irrespective
of priority, while this document adjudicates all defeat by class
rank — modelling them as high-ranked rebuttals. If that is
intended, the divergence is worth stating on the record.
`self-convicted` already looks like one undercutter promoted to its
own value.

---

## R15 — How is GEL span membership derived under track one?

**Issue:** #35 · **Severity:** BLOCKING

### The question

Under §17's track one, GEL events use the substrate's registry
event forms under their existing ilks, so a governance event and a
credential issuance are the same bytes in the same form, anchored
the same way — and §11 types the same domain as producing both.
§17 commits a canonical *order* for folding GEL events (L2203–2207)
and no rule for *membership*. Which anchored spans are the GEL?

### Why it must be answered

The bootstrap commits exactly two things: track choice and, for
track two, the initial ilk table (L2232–2235). That is track
*placement*, and §17's own must-reject vector list confirms the
reading by naming "both-track placement without committed placement
law". §4's genesis knot seals only the founding law's SAID.
Nothing designates a governance registry.

Three plausible inventions were exhibited — the first `vcp` after
the inception seal, the registry named in C, the registry whose
`ri` appears in founding law — yielding three different
Constitutions from identical committed bytes, each well-formed,
with no diagnostic. §7.3's byte-identity SHALL is violated and
§17's bootstrap refusal does not fire, because placement *is*
derivable and only membership is not.

Note the shape of the gap: §1.4 axiom 4 says "No ambient order".
There is no matching "no ambient membership".

### Options

**A — Founding law commits the governance registry's identifier**,
at the same grade §17 gives track choice, with a must-reject
boundary vector for a stream whose governance registry cannot be
derived. Cost: one clause plus one vector.

**B — Founding law commits a span-selection predicate** rather than
an identifier, admitting more than one governance registry. More
expressive, larger surface, and the predicate's own evaluation
becomes a fold input.

**C — An ambient rule** — for example, the first registry incepted
under the gAID is the GEL. Cheapest to write and the worst fit: it
is exactly the ambient derivation axiom 4's sibling would forbid,
and it silently breaks for any domain that incepts a credential
registry first.

### Recommendation

**A.** It matches the grade §17 already assigns to track choice,
it is derivable before the first governed event is admitted (which
is what the bootstrap requires), and it leaves B available later
without rework. C should be rejected on the record so it is not
rediscovered as the obvious shortcut.

Consider ruling in the same sitting whether an axiom naming
"no ambient membership" belongs beside axiom 4, since the absence
of that axiom is what let the gap through drafting.

---

## R16 — Define colored evidence, or remove it?

**Issue:** #38 · **Severity:** MAJOR

### The question

§6 says four object forms carry every crossing this document makes
and lists colored evidence as one. The term occurs three times in
2471 lines — §2's specifies-list and twice in §6, its intro and its
own bullet. No normative span requires producing, consuming, or
verifying it. §6's object-typing clause types the edict, the
warranty and requirement elements, and types neither colored
evidence nor the cone. Its component "committed view echo" occurs
once and is defined nowhere.

### Why it must be answered

An implementer told the crossing space is carried by four object
forms must build a form whose components are undefined, whose
typing clause omits it, and for which no fixture, vector, or
consuming clause exists. Two implementers build two different
objects, or neither builds it, and §2's "this document specifies"
list is false at its fourth item. By §1.7's own gate, a construct
with no stated composition is a defect in this document's terms.

This also blocks half of #37: the comprehension-gate drafting pass
cannot state colored evidence's composition while its components
are undefined.

### Options

**A — Define it.** Give "committed view echo" a definition, type
colored evidence under §6's object-typing clause, and state its
composition from the seven primitives. Cost: real design, because
the object has never been exercised.

**B — Remove it** from §2's specifies-list and from §6's four
object forms, reinstating it when a crossing is exhibited that
genuinely requires transporting a colorless base plus a view echo
plus a lens citation as one object.

### Recommendation

**B, unless a consumer exists.** The steelman for A is real —
naming the object makes the participial doctrine concrete and
pre-commits a wire shape a later multi-lens or confidentiality
profile will need. But a form with no emitter, no consumer, no
typing and no fixture is a promise the document cannot keep, and
"four object forms carry every crossing" is falsified today by its
own §6. If the drafting authority knows of a consuming case, A; if
the honest answer is "not yet", B costs nothing and can be undone.

---

## R17 — The covenant seal: decidable test, or re-type it?

**Issue:** #39 · **Severity:** MAJOR

### The question

§9 makes the covenant seal admissible "only where the substrate's
law makes lineage the invariant", and says verification "is neither
byte equality nor coordinate lookup" — the verifier evaluates
whether the successor satisfies the committed clause. Neither is
decidable from the text.

### Why it must be answered

The substrate's seal grammar ships digest, Merkle-root,
source-event, key-event, latest-establishment, backer and typed
seals, and draws no distinction between a "lineage invariant" and a
"byte-identity invariant" as substrate law. So the admissibility
side-condition resolves to nothing checkable while its violation
carries defect force — a rule found by nobody and assertable by
anybody.

And no clause language, satisfaction relation, or successor
relation is given, so two frames holding the same seal and the same
candidate successor can lawfully reach opposite verdicts — inside a
section asserting "Two disciplines bind all three kinds", and
against §5's "their agreement is cryptographic rather than
negotiated".

Separately: §9 requires a seal to name its kind, and the substrate
ships exactly that facility in the typed seal, whose `t` field is
"the versioned type of the seal". §9 acknowledges the typed seal
without adopting it or reserving a `t` value. This adjudicates the
prior 4.0 review's KN-14 — the absorption is nominal, not real. The
carriage reduces to a typed seal with a reserved `t`; the one
genuine irreducible remainder is the verification procedure, which
is the part left undesigned.

### Options

**A — Make it decidable.** Replace the admissibility side-condition
with a checkable test (or drop it along with its defect force),
state the carriage as a typed seal with a reserved `t` value, and
give clause-satisfaction a committed language. Cost: the committed
language is a real design surface.

**B — Re-type the seal.** Make it a frame-local commitment whose
verification returns a *finding* rather than a medium-grade seal
verdict. This is honest about what it can deliver and removes the
conflict with §5, at the cost of weakening what the covenant seal
was introduced to do.

### Recommendation

**No recommendation — this one is genuinely open.** A preserves the
construct and owes a language nobody has drafted; B preserves
decidability and demotes a construct the document leans on in §16's
succession story ("the seal a successor plants is checkable against
this document's covenant set — that is what the covenant seal is
for"). The choice turns on whether covenant satisfaction is
intended to be medium-grade, and that is exactly the sort of intent
the text cannot settle.

Whichever way it goes, the carriage half is separable and cheap:
reserving a `t` value for the covenant seal is worth doing under
either branch.

---

## R18 — Mandate a blinding factor, or confess the leak?

**Issue:** #44 · **Severity:** MAJOR

### The question

This document designs commit-now/disclose-later in several places —
an edict's identity is its bare SAID, digest seals commit bytes
that need not travel, §10 opens contest windows measured in log
positions, §6 contemplates undisclosed cone spans — and never
requires a blinding factor. A case-insensitive search for
`entropy`, `nonce`, `uuid`, `salt` or `blinding` across all 2471
lines returns zero matches.

### Why it must be answered

The substrate is explicit that a SAID conceals only when the
content carries entropy: without the `u` field "an adversary may be
able to reconstruct the block contents merely from the SAID of the
block and the Schema of the block using a rainbow or dictionary
attack".

Governance content is near the worst case. The seat roster is
public in the GEL, act kinds come from a closed §17 ilk table, and
the coordinate is public — so the search space is roster ×
act-kind × coordinate, trivially small against a Blake3-256 digest.

Concretely: a domain commits a 40-position contest window on seat
revocations. A revocation edict is anchored and, per §9's anchor
grade, lands in an establishment event — maximally visible and
non-erasable. Its SAID is public immediately while the pre-image is
withheld. The target grinds the space, recovers the content, and
spends the full contest window acting on it while the frame
believes the act is committed-but-undisclosed.

Two conforming implementations — one blinding, one not — both
satisfy §6's typing SHALL, so the divergence is silent uncommitted
latitude under §14's own interpretive-latitude duty.

### Options

**A — Mandate a blinding factor** on any object whose SAID is
committed before its content is disclosed. The typing clause does
not forbid a `u` field today, so this is an omission rather than a
structural bar. Cost: one ruled span; interacts with #48, since a
`u` field on a bare SAD is exactly the shape.

**B — Confess the leak** and scope the commit-now/disclose-later
claims to content whose disclosure is not adverse. Cheaper, and
consistent with the document's confessed authenticity-first
ranking, but it leaves contest windows advertising their own
subjects.

### Recommendation

**A, scoped to the withheld case.** Most governance evidence is
meant to be public and needs nothing. The finding bites only where
the design has *already chosen* to withhold — contest windows,
undisclosed spans, seals over untraveled bytes — and in exactly
those places the hash is being asked to do concealment work it
cannot do unaided. A ruled span scoped to that case is small and
does not disturb the public baseline.

Note the existing `confidentiality-and-anchored-delivery.md`
companion is informative and therefore cannot discharge a normative
gap, however well it describes the terrain.

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
| **R13** | "Bearing" at the registry and governance tiers | #32 | BLOCKING | no | Committed predicate **plus** the refuse/consume boundary | Rule with R10 |
| **R14** | Where a finding goes when evidence falsifies the defeat | #33 | BLOCKING | no | Revisit after R2; else defeat is evidence-indefeasible | R2 |
| **R15** | GEL span membership under track one | #35 | BLOCKING | no | Founding law commits the registry identifier | — |
| **R16** | Define colored evidence, or remove it? | #38 | MAJOR | no | Remove unless a consumer exists | — |
| **R17** | Covenant seal: decidable test, or re-type it? | #39 | MAJOR | no | *No recommendation — genuinely open* | — |
| **R18** | Mandate a blinding factor, or confess the leak? | #44 | MAJOR | no | Mandate, scoped to the withheld case | — |
| **11a** | Compound result when one component refuses | #41 | MAJOR | no | Decide with R11 | R11 |

Eighteen rulings and one sub-question over twenty issues — R8
covers #23 and #4 together; R13–R18 and 11a are the second batch,
appended 2026-07-30.

Both batches together: **six BLOCKING** (R1, R2, R3, R6, R8, R10)
in the first, **three more** (R13, R14, R15) in the second.

## What is not in this docket

These open issues need no ruling and are drafting or program work:
#11 (the ordering-semantics declaration), #12 (Spec-Up-T), #13
(projection vs ToIP's PR model), #14 (second implementation), #15
(conformance vectors), #16 (warranty dispute economics), #17
(deferred surfaces), #18 (working group), #19 (divergent-verdicts
section), #34 (upstream ask: application-defined TEL event types),
#36 (whether track two buys anything at the fold boundary), #37
(run §1.7's comprehension gate across the introducing sections),
#40, #42, #45, #46, #47, #48 (editorial repairs, seeded by PR #49).

**#8 moved.** It was listed here as drafting work — "aligning three
sites to a grade the abstract already ratifies". Re-checked against
the ratified bytes on 2026-07-30: all three sites already carry the
observational condition ("from the same committed inputs", "for
every verifier holding the pair", "by any verifier that
recomputes"), so the finding as filed does not hold and the
residual is one cross-reference per site. But the issue's
*escalation* question is a genuine ruling and is not covered
anywhere in this docket: **are §12.4's mutual convictability and
§13.2's cross-frame duplicity floor intended as guaranteed
properties, or as observer-conditional ones?** The bytes read as
observer-conditional, which is the survivability-correct posture,
but intent is the ratifying authority's to state. Docket it if the
answer is not obvious to the authority; it is left off the numbered
list because it may be a two-word confirmation rather than a
decision.

Of those, #15 is the one worth starting before any ruling lands.
The discriminating inputs for R2, R3, R9 and #2 are already
described precisely enough to execute; written as vectors that
record both readings and assert only that two engines must agree,
they need no ruling to be valuable and become the regression suite
the moment rulings land. #27 is the proof of the method: an
executed divergence settled in minutes what argument had left open
across a full gauntlet round.
