# Disposition of the ruling record — 2026-07-31

The ratifying authority answered the docket on 2026-07-30 in
`reviews/ruling-record-2026-07-30.md` (commit `002e0b9`).

Both digests in the record's own frame verify:

| Claim | Stated | Computed | |
|---|---|---|---|
| the record | `45a6d720…` | `45a6d7208f0faca82946f2bfacb04799994b5cf2c9afdef53f24def9d8cf8552` | ✅ |
| 4.1 appraised against | `ff8b9e7a…` | `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` | ✅ |

This document is triage of the answer: what it covers, whether it
hangs together, and what to do next. It is not a repair and it
proposes no edit to ratified text.

---

## 1. Coverage

The record answers **the docket as filed on 2026-07-29** — R1–R12.
The second batch (R13–R18, sub-question 11a) and the third batch
(R19, R15a) are not addressed.

| Docket | Issue | Sev | Ruled | Disposition |
|---|---|---|---|---|
| R1 | #7 | BLOCKING | **A**, position-indexed | repair owed (§7.3) |
| R2 | #28 | BLOCKING | **B**, full discharge | repair owed (§7.3) |
| R3 | #27 | BLOCKING | **B**, species in both keys | repair owed; PR #26 |
| R4 | #20 | MAJOR | **A**, one list, **seven** walls | repair owed (§15/§1.4) |
| R5 | #9 | MAJOR | one predicate: semantic now | repair owed; encoding → group round |
| R6 | #24 | BLOCKING | **B** under R1, refined | repair owed (§7.4) |
| R7 | #21 | MAJOR | **dissolved** by R4 | closeable |
| R8 | #23, #4 | BLOCKING | **B**, file-as-published | repair owed (§3.2) |
| R9 | #25 | MAJOR | layering error; wall retyped | repair owed (§1.4/§7.4) |
| R10 | #6 | BLOCKING | antinomy = **circuit** | repair owed — **but see §2.1** |
| R11 | #10 | MAJOR | **A**, scope the claim | repair owed (3 artifacts) |
| R12 | #5 | OBSERVATION | **B**, no text change | closeable |
| **R13** | #32 | **BLOCKING** | — | **unruled** |
| **R14** | #33 | **BLOCKING** | — | **unruled** |
| **R15** | #35 | **BLOCKING** | — | **unruled** |
| **R16** | #38 | MAJOR | — | unruled |
| **R17** | #39 | MAJOR | — | unruled (docket carries no recommendation) |
| **R18** | #44 | MAJOR | — | unruled |
| **11a** | #41 | MAJOR | — | unruled |
| **R19** | #36 | MAJOR | — | unruled — blocked on #55, follows #56 |
| **R15a** | #35 | — | — | unruled |
| **R20** | #43 | **BLOCKING** | — | unruled — **added to the docket today** |
| **8a** | #8 | MAJOR | — | unruled — added to the docket today |

Two rulings arrive outside the docket's own framing and say so
(R9, R10). Both departures are improvements and are argued from
the bytes; neither is a defect. Four re-rulings were owed under
`CONTRIBUTING.md` property 2 — R1, R4, R6, R10 — and the record's
preamble accounts for exactly four. ✅

### The record's covering claim overstates its reach

The PR #31 comment states: *"Every BLOCKING finding on the tracker
now has its ruling."* On the tracker as it stands that is not so:

- **#32, #33, #35** — BLOCKING, on the docket (second batch,
  visible in the thread before the record was issued), unruled.
- **#43** — BLOCKING, **never docketed at all**. It is absent from
  the docket's numbered list *and* from its "what is not in this
  docket" list. That is our accounting gap, not the authority's.
  Fixed 2026-07-31: it is now **R20**, with the same two options
  its filing proposed and a recommendation of B (the enactment pins
  the companion), qualified by whether B is the mechanism or a
  bridge to A. R1/A sharpens it — a decision procedure that can
  change under the engine's feet is a hidden fourth input to a
  function the ruling has just declared closed.
- **#29** — BLOCKING, correctly dispositioned rather than ruled
  ("reviewed next as an ordinary finding repair under R4's own-text
  provenance"; PR #30 carries it). No objection; noting it because
  it is a fifth BLOCKING issue the sentence sweeps in.

Best reading: the record was drafted against the docket as
originally filed, and the covering sentence was written to that
scope. It needs one correction and a second sitting, not a
retraction.

---

## 2. Consistency check

### What holds — verified against the ratified bytes

- **R1's evidence bundle is axiom 2's own sentence.** L248–250:
  *"The log spans a fold reads — the GEL span, every cited
  key-event and registry span — are members of the evidence
  bundle."* Registry state is inside E, so #7's revocation case
  really does dissolve as succession. ✅
- **R4's arithmetic is right, and the docket's is too** — they
  count the same union differently and the record reconciles it.
  §1.4 (L281–287) names five; §15 (L2052–2062) names six; the
  transition pair (enumeration + no backward edge) is one item in
  §1.4 and two in §15. Union counted §15-style = **eight**; merged
  = **seven**. The two §1.4-only walls are canonical ordering and
  first-seen survival — which are exactly the two rotted sites
  (#2, #25), as the record claims. ✅ This is the sharpest single
  observation in the record.
- **R6's species is a ratified species.** §7.2 L1005–1006:
  *"unresolved-conflict is cured by an owned act of the party
  whose conflict it is."* R6 assigns exactly that, and its
  "rehabilitation is an act, not a transition" is the species'
  own cure clause restated. No new codomain value, no new species.
  ✅
- **R8 leaves committed history unrewritten** and answers #4 and
  #23 with one clause, as the docket recommended.
- **R12 closes a thread rather than changing text**, with the
  reasoning preserved — the disposition the docket asked for. ✅

### Discrepancies and gaps, ranked

**2.1 — R10 was ruled alone, and the docket said not to.**
The docket: *"Rule with R10: both concern what reaches
`self-convicted` and what it must carry, and rulings that disagree
would be worse than either alone."* R10 landed; R13 (#32) did not.
This is not cosmetic. R10's new constructor sits on the
`pending → self-convicted` edge at L1062 — and **"bearing" is the
gate on that edge**, defined only at the key tier. So the antinomy
circuit is a payload for a transition whose admission condition is,
at the governance tier, still undefined. R10 is under-determined
until R13 is ruled, and a repair drafted now would have to leave
the gate blank.

**2.2 — R1 presupposes R15.** R1 defines E as *"the GEL span,
every cited KEL span, every cited TEL span"* — following axiom 2,
which also says "the GEL span," singular. #35 (R15, BLOCKING) is
precisely the finding that **which anchored spans are the GEL is
underivable**. So the closed triple that R1 makes the foundation of
the whole scheme has one member whose extent is not yet derivable
from committed bytes. R1 is correct and R15 is still owed; the
dependency runs the direction the docket did not anticipate.

**2.3 — R14 does not dissolve as cleanly as the docket predicted.**
The docket said R2/B *"largely dissolves"* R14. On inspection it
dissolves only half. R2/B forecloses **short-circuit** defeat — a
`defeated` returned with an enumerated check unexamined. It does
nothing about **later-arriving** evidence that falsifies the cited
defeater's own enactment, where the check *was* examined and passed
against the then-bundle. In that case the trap is still built: R1/A
makes the growth a new finding, but L1103's *"refines and never
contradicts"* at a fixed law head still closes the `affirmed` exit,
`pending` is forbidden from `defeated`, and `self-convicted`
requires the subject's own contradiction. **#33 needs its own
ruling.** Our own recommendation was too optimistic and should be
corrected on the docket.

**2.4 — R9's scope is stated two ways.** R4's wall 6 (canonical
ordering) is annotated *"RETYPED by R9 below"*, and R4's wall 7
(first-seen) *"REMOVED … by R9 below"*. But R9's body retypes only
one wall — *"The evaluator wall is retyped: **no fold-tier
selection**"* — and never touches the ordering wall. This matters
because **R5's byte-identity convergence argument leans on it**:
R5 argues byte-identity follows by construction because "R2, R3,
and R4's ordering wall removed every semantic source of byte
variance." If the ordering wall is itself retyped by R9 in some
unstated way, that argument needs restating. One-sentence
clarification.

**2.5 — R5's unified predicate is not a superset of §16's.**
R5 enumerates: finding value, self-convicted kind, grounds in
canonical order, typed requirement set including species, refusal
class where refusal fires, cited law head, corpus identity.
§16 (L2140–2142) enumerates: corpus identities, **admission sets**,
**refusal grounds**, cited law heads. Two deltas:
- **"admission sets" is absent from R5's list.** Dropped, or
  subsumed under "grounds"? The whole content of R5 is that the
  three sites unify on *one* predicate, so the drafting pass cannot
  guess.
- **"refusal class" is a new term** — the spec has no "refusal
  class"; §16 says "refusal grounds" and §9 L1322–1325 names three
  refusal *kinds* by seal. Same commitment under a new name, or a
  new commitment?

**2.6 — The refusal component of R5 is the least-grounded part,
and 11a is why.** R5 makes refusal a compared component of the
conformance predicate. Sub-question 11a (#41) asks what a compound
result even *is* when one component refuses — and it is unruled.
Until it is, two engines can agree on every finding and still
differ on the object R5 tells them to compare. Note that R11/A
makes the cheap answer available: §7.5's own words are *"the
evaluator SHALL refuse **the invocation**"*, which is the docket's
suggested companion. It still has to be stated, because the ruled
text sits inside §7.5's quoted amendment block.

**2.7 — The new wall enters by the door the same ruling closes.**
R4 adjudicates R1's position-indexing and R2's discharge discipline
*out* of the wall list on the principle that *"new walls enter
through their own gauntlet, not as riders on a drift repair."*
R9's **no fold-tier selection** then enters the wall list as a
rider on that same drift repair. Defensible — it is a retype of an
existing wall, not a new commitment — but the record should say so
explicitly, because on the page the principle and the action point
opposite ways.

**2.8 — R11's coupling is described in the superseded form.**
The record says the repair moves "README line 20's byte-identical
quote" and that verify_kernel proves it. `tools/verify_kernel.py`
check 3 is an *excerpt* discipline — its own label is *"README
abstract excerpt discipline"* / *"README abstract is a byte-true
excerpt of the 4.1 edition."* Our 2026-07-30 correction said so and
the record repeats the original framing. Immaterial to the outcome
(R11/A rewords the abstract sentence, so the README quote almost
certainly changes anyway), but the repair instruction should name
the discipline that is actually enforced.

**2.9 — Count.** "Twelve rulings and one dissolution" is twelve
docket items: **eleven rulings and one dissolution** (R7 is the
dissolution). Trivial, but the record is going to be cited by
digest in the 4.2 input manifest.

**2.10 — The record cites a document that is not in the repo it
lives in.** Its first line answers `reviews/ruling-docket-2026-07-29.md`,
which exists only on PR #31's branch. Upstream `main` now carries a
ruling record whose subject is a dangling reference, and which cites
that subject by path rather than by digest — in a corpus whose whole
thesis is that commitments are pinned. **Merging PR #31 fixes it.**

### Our own defects, found in the same pass

- **The docket's R1 section mislabels two rulings.** The ordering
  table (L46) reads *"R3 (#24) outright; constrains R4 (#6)"* and
  the R1 recommendation repeats it (*"Under A, R3 (#24) resolves
  for free, and R4's hardest sub-question …"*). The issues are
  right and the R-numbers are stale: #24 is **R6** and #6 is
  **R10**. The record navigated it correctly, so no harm was done —
  but it must be fixed before PR #31 merges, since the record now
  cites this document.
- **#43 (BLOCKING) is on neither docket list.** Add it, or state
  why it needs no ruling.
- **R14's recommendation is too optimistic** (§2.3). Amend.
- **The third batch was published to the world before it was
  pushed.** The comments on #35, #36, #45, #47 and #49 cite
  "docket R19", "the R15 amendment", and
  `reviews/rounds/41-parsimony-2026-07-30/upstream-answer-1566.md`
  — all of which sat in unpushed local commits until 2026-07-31.
  Fixed by pushing `197be3b`; recorded because a record that cites
  what nobody can fetch is the exact failure the standard exists to
  prevent.

---

## 3. Next actions

> **Status, end of 2026-07-31.** Sections 3.0 through 3.3 are
> **done** and are kept as the record of what was decided and why.
> Do not re-execute them. What remains open is 3.4 (the station
> obligations, not yet started) and 3.5 (the second sitting, which
> is the ratifying authority's move, not ours).
>
> Executed: #21 and #5 closed; a disposition comment on every ruled
> finding; the maintainer's two dossier questions answered on #1;
> #57 opened for the carriage-encoding round; PR #26 updated to the
> four-field order; PR #49 split; and seven seed PRs opened —
> **#58** (R1, R6), **#59** (R2), **#60** (R4, R7, R9), **#61**
> (R8), **#62** (R5), **#63** (R11), and **#64** (R10, draft, held
> on #32 and carrying a marked `[BLANK]` — it must not merge until
> #32 is ruled).
>
> The live work queue is the repo's `tick` ledger (`tick ls`), not
> this section.

### 3.0 Immediate

1. **Merge PR #31.** It is the record's cited subject (§2.10).
   Before merging, land the three docket corrections in §2's last
   block: the R1 numbering slip, #43's placement, and the R14
   amendment — plus an "answered by" header pointing at
   `reviews/ruling-record-2026-07-30.md` and its digest.
2. **Answer the maintainer's two questions on #1** (posted
   2026-07-30, still unanswered): does the ToIP dossier spec's
   composition commitment cover the receipt-grain bundle preimage
   by inheritance, and does its issuer role admit the same party
   also carrying judgment liability in a distinct citing
   commitment? These were asked of the coiner, not of the reviewer,
   and they gate the maintainer's gate-1 decomposition.

### 3.1 Issues to close

| Issue | Why |
|---|---|
| **#21** | R7 dissolved by R4 — with own-text provenance there is no imported referent left to lack an extent. Close citing the record. |
| **#5** | R12/B, ruled with no text change and the reasoning preserved. Close citing the record. |

Nothing else should close yet: every other ruled finding owes a
4.2 repair, and closing on the ruling rather than the repair loses
the trace. Label them `ruled` and let the seed PRs close them.

### 3.2 Issues to keep open, retagged `ruled — repair owed`

#7, #28, #27, #20, #9, #24, #23, #4, #25, #6, #10 — each with a
one-line comment naming its ruling and the record's digest. (Standing
convention: one reply per finding, so the record reads 1-to-1.)

#8 stays open, re-scoped to the cross-reference residual; its
escalation question is unanswered and belongs on the next docket.

### 3.3 PRs to raise — 4.2 seeds, one per ruled surface

Ordered by readiness. Every one is `spec/4.2-seed-*`, none touches
ratified text of 4.1.

| # | Seed | Executes | Closes |
|---|---|---|---|
| 1 | **Update PR #26** — extend the order to R3's four fields, add the ambient-order declaration as the second half | R3, R2, R4 wall 6 | #2, #3, #27 |
| 2 | **Position-indexing and contested standing** — §7.3's closed-triple declaration; §7.4 "converts" → succession vocabulary | R1, R6 | #7, #24 |
| 3 | **Full discharge** — no terminal finding with an enumerated check unexamined | R2 | #28 |
| 4 | **One wall enumeration** — seven walls in §15, §1.4 cites; the 4.0 import retired; wall 7 retyped to no-fold-tier-selection; §7.4's first-seen sentence kept as description | R4, R9 | #20, #21, #25 |
| 5 | **Two-kind pin discipline** in §3.2 | R8 | #23, #4 |
| 6 | **One conformance predicate** — §2, §7.3, §16 unified | R5 | #9 |
| 7 | **Refusal claim scoped** — abstract L29 + README L20 + verify_kernel check 3, moving together | R11 | #10 |
| 8 | **Antinomy circuit** — §7.3 payload disjunction, §7.4 bearer and reflexive force | R10 | #6 — **hold for R13** |

Seeds 2 and 3 are both §7.3 and could ride together; keeping them
separate keeps each `Closes` line traceable to one ruling.

**Seed 8 should be drafted and held.** Its gate is R13's subject
(§2.1). Draft it, open it as a draft PR so the shape is on the
record, and do not ask for merge until #32 is ruled.

**PR #49** — execute the split already recommended on the PR: land
#46, #48 and the #40 partial now; hold #45 and #47 for R19. Nothing
in the record changes that analysis, and R19 is still unruled.

**PR #22** (review record) — the record says it needs no ruling
content. Merge.

**PR #30** (#29, Ground Axiom) — the record routes it as an
ordinary finding repair under R4's own-text provenance. Ready.

**PR #51** (node24 runtimes), **PR #50** (engagement companion) —
independent of all rulings.

### 3.4 Station obligations the record assigns to us

Two are explicit, and both are ours to build:

1. **R3** — the executed divergence from #27 becomes a committed
   regression vector, expected value = the ruled reading.
2. **R10** — a **cardinality-3** antinomy fixture (pairwise
   consistent, jointly unsatisfiable) joins the conformance corpus
   as the record that separates circuit-payload engines from
   pair-payload engines.

Both belong in **#15**, which the docket already identified as the
one item worth starting before any ruling lands. It is now worth
more: R2, R3, R9 and #2 all have ruled expected values, so vectors
written today are no longer "record both readings" — they assert
one. This is the highest-value unblocked work on the board.

**R5's carriage-encoding group round** is chartered by the
authority, not by us — tracked at **#57**, which carries its five
decisions, its inputs and their state, and the interim grade
discipline. Two of its named inputs are unruled:
R5 lists "genus composition with the ilk-table seats" among the
several decisions it defers — and under R19/A the ilk-table seats
do not exist. **R19 is an input to the group round.** Worth saying
when the charter arrives.

### 3.5 Back to the ratifying authority — a second sitting

One comment on PR #31, requesting the second sitting and correcting
the covering claim. The asks, in priority order:

1. **R13 (#32), R14 (#33), R15 (#35)** — three BLOCKING findings,
   unruled. R13 is the one that must move first: R10 is already
   ruled and is under-determined without it (§2.1).
2. **R19 (#36)** — *not* schedulable after all. The feasibility
   work filed later the same day establishes that #55 blocks it
   outright (nobody has exhibited a Custos enactment in the
   `(td, ts)` form, so the recommendation rests on the substrate's
   permissiveness rather than on the form carrying an edict, a
   warranty, a requirement element or a covenant seal) and that #56
   should precede it (retaining `upd` upstream removes option A's
   only substantial cost). It still gates PR #49's two held repairs
   and is still an input to R5's group round — which now makes
   **#55 and #56** the schedulable items, not R19.
3. **R15 (#35)** — additionally, R1 presupposes it (§2.2). Rule it
   with R19 per the R15a amendment; they are now one design.
4. **R14 (#33)** — flag our own correction: R2/B does not dissolve
   it (§2.3). It needs its own ruling.
5. **R16, R17, R18, 11a** — MAJOR, independent, no blockers. R17
   carries no recommendation by design; it is the one item on the
   docket that is pure intent.
6. **R20 (#43)** and **8a (#8)** — both now on the docket, both
   with no blockers and no dependencies. R20 is the fourth BLOCKING
   item outstanding; 8a may be a two-word confirmation. Together
   with R16, R17 and R18 they are what a second sitting can take in
   one pass.
7. **Four clarifications on the record itself**, each a sentence:
   R9's scope over wall 6 (§2.4); admission sets and "refusal
   class" in R5's predicate (§2.5); whether the no-fold-tier-selection
   wall is a retype rather than a new wall entering as a rider
   (§2.7); and the count (§2.9).

The tone that fits the record: it did the harder half. Eleven
rulings, two of them outside our framing and better for it, and one
pattern named that we had not seen — *nearly every blocker resolved
to a missing commitment made explicit*. What is owed is a second
sitting, not a revision.
