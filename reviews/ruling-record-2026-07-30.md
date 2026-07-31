# Ruling record — 2026-07-30

Answers `reviews/ruling-docket-2026-07-29.md` (PR #31). Twelve
rulings and one dissolution, in the docket's own dependency order.
Issued by the ratifying authority after grounded review of each
question against the ratified bytes of `spec/custos-4.1.md`
(sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05`).

Nothing here edits ratified text. Every ruling lands as repair
instructions for the next candidate edition (4.2), entering its
committed input manifest; four rulings are re-rulings of fixed
walls and return through the front door with their findings as
evidence, per `CONTRIBUTING.md` property 2. Recommendations in the
docket were weighed as recommendations; where a ruling departs from
the docket's framing, the departure is stated and grounded.

One pattern, stated once because it recurs in most of the twelve:
nearly every blocker resolved to a **missing commitment made
explicit** — finding identity, discharge scope, key membership,
wall enumeration, pin discipline — not to new machinery. The
document's axioms already forced the answers; the text had not yet
said them. Two rulings (R9, R10) additionally found the docket's
own framing inside a frame the answer was outside of; both are
marked.

---

## R1 (#7) — RULED: A, position-indexed

A finding is an immutable fact of a closed triple, never a mutating
value: `finding = F(E, L, p)`.

- **E, the committed evidence bundle** — a set of committed log
  spans closed by citation, each (log identifier, coordinate range,
  digest): the GEL span, every cited KEL span, every cited TEL
  span. Registry state is INSIDE E (axiom 2's own sentence), so
  the revocation case dissolves: a `rev` event is a new span, a new
  E, a new finding at a new position. No edge crossed.
- **L, the committed law head** — the SAID of the Constitution
  state appraised under; E is typed by L: the law head commits the
  question's requirement space ex-ante, and the bundle inhabits
  the evidence-type the law declares.
- **p, the appraisal position** — a log coordinate (identifier,
  sequence number) in committed order; never wall-clock.

§7.3's transition table constrains the lawful succession of
findings across positions on one question, never the mutation of a
stored value. "Settled findings do not flip" = no coordinate's
fact is ever rewritten. The engine profile is NOT a triple member:
it is the lens-side citation whose inertness is what conformance
tests (the reversal condition).

Repair: one clarifying declaration in §7.3; the registry-state
membership sentence cited, not restated.

## R2 (#28) — RULED: B, full discharge binds every terminal value

No terminal finding while any enumerated check in the question's
committed requirement space is unexamined; an incomplete
examination yields `pending` with the unexamined check as its
typed requirement. The ratified "never affirmed" sentence named
only the seductive failure; this ruling states the dual.

Grounds: partial examination is a type error, not a smaller answer
— the requirement space is committed ex-ante (L1105–1109), so a
fold that stops early has computed something no one committed to.
Consequences: canonical selection's set is always computed (PR
#26's repair to #2 has its object and is meaningful); the defeated
citation is deterministic to the byte at a fixed triple; L1103's
monotonicity is true as written; the licensed-shortcut divergence
(two engines, different first defeat) is closed.

## R3 (#27) — RULED: B, species enters both keys

Species is appended to the requirement-set dedup key and the
canonical order as the final sort tiebreak — a four-field total
order (subject, kind, citing clauses, species). §7.2's
mandatory-field SHALL forces it: if the element must carry it, the
key must see it, or the canonical order is a preorder and the
bytes are undetermined.

A was rejected as incomplete (requires a merge rule the document
does not state) and lossy (a party told "the missing evidence
arrives" but never "a recovery window is open" has received a
materially different instruction from the same record — the merge
discards the cure semantics §7.2 exists to carry).

The shared doctrine with R2, for the record: the fold discharges
everything the law commits; the key sees everything the element
commits. Station obligation: the executed-divergence input becomes
a committed regression vector (expected = this ruling's reading).

## R4 (#20) — RULED: A, one enumeration, own-text provenance;
## membership adjudicated to SEVEN walls

One enumeration, in §15; §1.4 cites it and restates nothing.
Provenance ruled: every wall is carried by the current edition's
own ratified text — predecessor lineage is confessed history,
never a binding mechanism. The two §1.4-only walls were exactly
the two rotted sites (#2, #25): a wall imported by pointer can be
neither read nor repaired in-document, so it drifts unowned.

The walls, adjudicated item by item from the union of eight:

1. Codomain totality — kept as-is (convicted #24 in live fire).
2. Refusal at an uncommitted composition seam — kept as-is.
3. Transition system completely enumerated AND no backward edge —
   kept, merged into one wall (one commitment; an un-enumerated
   system cannot prove edge-absence).
4. The two currents, never merged — kept as-is.
5. Committed receipts for acts-as-grounds — kept as-is.
6. Canonical ordering — kept, reworded as the ambient-order
   declaration's constitutional hook; site rules descend from the
   declaration. RETYPED by R9 below.
7. First-seen survival — REMOVED from the evaluator wall list by
   R9 below; replaced by the no-fold-tier-selection wall.

Explicitly adjudicated OUT: R2's discharge discipline and R1's
position-indexing do not enter the wall list in this cycle — they
are §7.3 text; new walls enter through their own gauntlet, not as
riders on a drift repair.

Knock-ons: R7 dissolves; #23 loses its hardest case.

## R5 (#9) — RULED: one predicate — semantic now, byte at
## encoding; the encoding goes to a group design round

§2, §7.3, and §16 unify on ONE conformance predicate. Until the
carriage encoding ratifies, it is semantic FULL-PAYLOAD equality:
finding value + self-convicted kind + grounds in canonical order +
typed requirement set including species + refusal class where
refusal fires + cited law head + corpus identity. §16's ratified
list was short — it omits the findings themselves and would have
passed #27's executed divergence.

The byte-identity sentence survives as a forward commitment backed
by a convergence argument: R2, R3, and R4's ordering wall removed
every semantic source of byte variance, so the finding is unique
up to serialization, and byte-identity follows by construction the
moment an encoding lands. This is not a weakening; it is the same
predicate stated at the layer that exists.

The carriage encoding itself is NOT pinned by this ruling. It is
routed to its own design round in a group setting — Samuel Smith,
Daniel Hardman, and reviewers with KERI-systems design depth —
because the "one decision" is several (serialization kind; field
schemas still moving under R6/R8/R10 and the dossier question;
SAID coverage; versioning; genus composition with the ilk-table
seats), because §15's own ratified text routes this deliverable
through review-by-others entering as findings, and because two
live implementations exist whose authors' input is worth more
before ratification than after. Comparison-grade discipline in the
interim: same-engine comparisons are byte-grade under a pinned
fixture-local serialization; cross-engine comparisons are
semantic-grade; a divergence report states its grade.

Unblocked: #11, #14, #15.

## R6 (#24) — RULED: B under R1, refined

"Contested standing" is not a value; it is an evidence event with
a typed consequence. The lower-tier self-conviction enters the
record as new committed spans; at the next position the fold
returns `pending` with the taint as its typed requirement, species
= unresolved-conflict (no missing bytes cure a taint; no log
growth cures it; only a committed act by a named actor does —
"rehabilitation is an act, not a transition"). The affirmed at its
coordinate stands forever; no forbidden edge is crossed because
nothing mutates. Repair: "converts to contested standing" is
reworded to succession vocabulary; the codomain's totality wall
stands unbreached.

## R7 (#21) — DISSOLVED by R4

With walls carried in the current edition's own text, there is no
imported "evaluator sections" referent left to lack a computable
extent.

## R8 (#23, #4) — RULED: B, the pin commits to the file as
## published

A whole-file digest pin commits to the file as published — the
header inside the preimage, non-normative in content. The
separation law: the pin answers "which bytes?"; normativity
answers "which of those bytes bind?" — two rulings, never one.
`9cefdc5d…` stands correct as anchored; committed history is not
re-anchored. Repair: §3.2 gains the two-kind pin discipline —
(a) self-addressing SAID pins, same-length placeholder in the
digest's own field, placeholder character named; (b) external
whole-file digest pins, preimage = the published file.

## R9 (#25) — RULED: the defect is a LAYERING error; wall 6/7
## retyped [departs from the docket's A/B framing]

Both docket options lived inside a frame the answer is outside
of. §7.4's "first-seen survives" is a correct DESCRIPTION of
medium-tier behavior (KERI's observer-local acceptance policy;
comparing first-seens is how duplicity is detected) and it stays,
as description, in the taint passage. The defect is §1.4
importing that phrase as an EVALUATOR obligation — a category
error: first-seen is constitutively observational, the one thing
axiom 4 forbids the fold to consult. This is why both blind
implementations had to silently reinterpret the clause: the
correctly-typed rule is the only implementable one.

The evaluator wall is retyped: **no fold-tier selection.** The
fold consumes digest-cited committed spans; it never adjudicates
between competing versions of an event. Competitors at one
coordinate entering the bundle convict as duplicity — they are
never inputs to a choice. Survival is settled below the fold, at
bundle assembly, per holder, by the medium's own inherited policy,
reimplemented nowhere. (E cites spans by digest; there is no
"which version" question inside a fold.)

Also recorded: the defect class — collision-by-addition.
Unchanged predecessor text was made defective by the successor's
new commitments (4.0's sentence was innocent; 4.1 added axiom 4
and §17 around it). The regeneration method's census must check
survivals against new axioms, not merely re-derive them.

## R10 (#6) — RULED: the antinomy constructor is a CIRCUIT, not a
## pair [departs from the docket's pair framing]

- **Payload:** a jointly-unsatisfiable SET of grounded derivations
  — each derivation citing its evidence spans and clause SAIDs to
  its conclusion — plus the joint-unsatisfiability exhibit, plus
  the enactment signatures of every producing clause. A pair
  cannot express the decisive case: cardinality ≥ 3, pairwise
  consistent, jointly unsatisfiable. Irredundancy (no proper
  subset suffices) is SHOULD, not MUST: an honest non-minimal
  circuit still convicts; minimal-core extraction can be
  expensive.
- **Bearer:** the GARD's administrators, not the subject. Force is
  law-relative AND reflexive: the conviction binds maximally in
  the very frame whose law it convicts, and travels to other
  frames as evidence about that GARD.
- **Reachability:** dissolved by R1 — an antinomy discovered after
  affirmation is a new terminal finding at a new position; no new
  edge; the wall is not opened.

Station obligation: a cardinality-3 antinomy fixture (pairwise
consistent, jointly unsatisfiable) enters the conformance corpus —
it is the discriminating record that separates circuit-payload
engines from pair-payload engines.

## R11 (#10) — RULED: A, scope the claim

The stranger recomputes the same Constitution and the same
FINDINGS byte for byte; refusals replay as DECISIONS derivable
from the same committed triple. Openness-question 1 (a committed
refusal-record form) remains open — committing it by docket ruling
would decide a ratified openness question under ruling pressure,
the same class this record declined at R5. The three-artifact
coupling is honored in the repair: the abstract sentence, README
line 20's byte-identical quote, and verify_kernel check 3 move
together, and the verifier proves they moved.

## R12 (#5) — RULED: B, closed with no text change

"Congruence" is a genus term (overlap-at-a-grade, §12's own
framing). §12 already defuses every consequence: no committed
comparison algorithm, conjecture grade, stated lens, "evidence,
never force. It confers nothing." Blast radius zero; a rename
costs a succession ceremony. Recorded so the next reviewer finds
the reasoning instead of raising it again.

---

## Dispositions in flight

- **PR #26** (#2, #3 repairs): R2-B gives its canonical-selection
  repair its object; R3-B extends its three-field order to four.
  The two compose; neither subsumes. Merge path: update to the
  four-field order per R3, then merge as the ordering repair's
  first half, with the ambient-order declaration (the R4 wall-6
  hook) as the second half in the 4.2 candidate.
- **PR #30** (#29, Ground Axiom keyword force): not docketed;
  reviewed next as an ordinary finding repair under R4's
  own-text provenance.
- **PR #22** (review record): evidence-only; merge needs no ruling
  content.
- **#19** (convergence-not-consensus section): the geometry
  answer now exists — different evidence is a different bundle;
  different law is a different sheet of the manifold; the same
  triple on the same sheet must agree to the byte, and divergence
  there convicts the specification. Drafts into the 4.2 candidate.

## What this record binds

These rulings enter `weave/41-…/4.2` drafting as committed inputs:
the 4.2 input manifest cites this record by digest, and every
repair executes under a ruling named here. The carriage-encoding
group round is chartered separately and does not gate the 4.2
candidate. The five traveling conditions of the Chapter-1
graduation and the reversal condition continue to bind.
