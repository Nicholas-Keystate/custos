# Custos 4.2 seed — full discharge binds every terminal value

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges finding #28 only; every other span of section 7.3
> stands as ratified. Executed under ruling R2 of the ruling
> record of 2026-07-30 (sha256 45a6d7208f0faca82946f2bfacb0479999
> 4b5cf2c9afdef53f24def9d8cf8552), and read against ruling R14 of
> supplement 2 of 2026-08-01 (sha256 7c5f6491976bd5fb12dcbab4c152
> 0002f9f5a1cdf9bf94dc2f0964bb1aea2670), whose succession re-runs
> this discipline at the new position. Offered to the drafting
> authority, which owns the wording.

---

## What this seed carries

One paragraph of section 7.3 is replaced. It states the discharge
discipline for `affirmed` and names only `affirmed`; the
replacement binds every terminal value.

The paragraph is short and the repair is shorter, but it is the
most load-bearing of the ordering repairs. Three other clauses in
the same section depend on it and none of them says so.

## Repair — the discharge discipline

**Ratified span (4.1 L1113–1121).** Cited, not edited.

> The ordering forces a discipline on affirmation, stated here so
> no reader must derive it: affirmed is reachable only over a
> bundle that discharges the question's entire committed
> requirement space. An evaluator holding a bundle that leaves any
> enumerated defeater-check unexamined returns pending with that
> check as its typed requirement, never affirmed — which is
> exactly what makes the ordering monotone, since a bundle that
> could still grow a defeater is, by construction, a bundle that
> has not discharged the space.

**The defect.** Read literally, the discipline restrains
`affirmed` and nothing else. A fold may then return `defeated`
while enumerated defeater-checks remain unexamined — and the
citation changes as the bundle grows. `defeated(merit, M)` under
`B1` becomes `defeated(crypto, S)` under `B2 ⊃ B1`: two different
grounds for one question, from bundles in the subset order.

Three consequences, and each is a live contradiction rather than
an inelegance:

- L1103, four paragraphs later, says appraisal under the larger
  bundle "refines and never contradicts" appraisal under the
  smaller. Two different defeat citations for one question are
  not a refinement.
- The forbidden table has no `defeated → defeated` row, and the
  transition system is declared an explicit and complete
  enumeration. So the system does not reach the case at all.
- Canonical selection ranges over "multiple defeats simultaneously
  available". Under the literal reading an engine may return the
  first defeat it finds without ever computing that set — so there
  is no set to take the least of, and the total order in the
  canonical-order seed has nothing to range over.

A blind implementation pinned the literal reading, recorded that
it preferred the other, and wrote a regression test asserting the
non-monotonicity as an executable defect. That is the correct
posture for an implementer — reading a restriction into a ruled
span is legislating, which axiom 3 forbids — and it is why this
needed a ruling rather than a clarification.

**Replacement.**

> The ordering forces a discipline on every terminal value, stated
> here so no reader must derive it: **a terminal finding is
> reachable only over a bundle that discharges the question's
> entire committed requirement space.** An evaluator holding a
> bundle that leaves any enumerated check unexamined returns
> pending with that check as its typed requirement, and returns
> neither affirmed nor defeated nor self-convicted.
>
> The discipline is symmetric because the requirement space is
> committed ex-ante. Everything that could bear on the question —
> affirmatively or by defeat — is enumerated in that space before
> appraisal begins, so a fold that stops early has not computed a
> smaller answer. It has computed something no one committed to,
> which is a type error rather than an economy.
>
> This is what makes the ordering monotone in both directions. A
> bundle that could still grow a defeater is, by construction, a
> bundle that has not discharged the space; so is a bundle that
> could still grow the evidence that falsifies the defeat it
> currently cites. Neither yields a terminal value.

**Ground.** The ratified sentence named the seductive failure and
not its dual. Returning `affirmed` while a defeater-check sits
unexamined is the error a reader expects, so the document warned
about it; returning `defeated` on the first defeat found looks
like thrift rather than error, which is why it went unwarned and
why an implementer pinned it in good faith.

The symmetry argument is section 7.3's own. L1104–1106 already
says defeating evidence is ex-ante enumerable — "everything that
could defeat a question is in that question's committed
requirement space before appraisal begins, which is what makes
defeat a citation rather than a surprise." A citation drawn from
an unexamined space is a surprise wearing a citation's clothes.

## What this repair unblocks

Recorded because four clauses depend on it, three of them
silently, and a candidate that lands them without this one lands
them broken.

- **Canonical selection has an object.** The set of
  simultaneously-available defeats is always computed, so the
  total order in `custos-4.2-seed-canonical-order.md` has
  something to be least of, and the defeated citation is
  deterministic to the byte at a fixed triple.
- **L1103's monotonicity claim becomes true as written**, with no
  weakening and no scoping clause.
- **The licensed-shortcut divergence closes.** Two engines
  examining a requirement space in different orders can no longer
  return different first defeats, because neither may stop at the
  first.
- **R14's succession consumes it.** Supplement 2 rules that
  committed evidence falsifying a cited defeat yields an ordinary
  succession, computed fresh by full discharge at the new
  position. That ruling names this discipline as the computation
  it re-runs, and its reversal condition is stated over the
  ground the prior finding cites — which is determinate only
  because nothing was left unexamined when the prior finding was
  computed. The dependency runs one way: R14 needs this seed;
  this seed does not need R14.

## Notes for the drafting authority

Some things surfaced in drafting that finding #28 did not name.

1. **`self-convicted` is inside the discipline, and that is worth
   confirming rather than assuming.** The replacement says "a
   terminal finding", and section 7.3 makes self-convicted
   terminal. The reading is that a bearing contradictory pair
   discharges the space by exhibiting it, so nothing is left
   unexamined — but self-conviction arrives by a different route
   from the other two terminal values, and the ruling's phrase is
   "every enumerated check in the question's committed requirement
   space". If a contradictory pair can convict while an unrelated
   enumerated check sits unexamined, the sentence above overreaches
   and should say "neither affirmed nor defeated".

2. **The repair does not reach finding #33, and the candidate
   should not read as though it does.** This discipline
   forecloses returning `defeated` while a check sits unexamined
   at appraisal time. It says nothing about evidence arriving
   *later* that falsifies a defeater whose validity check was
   examined and passed against the bundle as it then stood.

   The docket originally predicted that R2 would largely dissolve
   #33. It dissolves the short-circuit half. The later-arrival
   half is the half #33 was about, and it survived — until
   supplement 2, which rules it R14/C: the destination is an
   ordinary succession, `F(E′, L, p′)` computed fresh by the
   discipline this seed states, with the prior `defeated`
   standing at its own coordinate and L1103's monotonicity
   re-scoped to the knowledge order. So the gap this note was
   written to keep open is closed, by its own ruling and its own
   seed, not by this one. What this note now records is the
   boundary: the two repairs compose and neither subsumes the
   other.

3. **"Enumerated check" is doing work the document defines
   loosely.** The ratified sentence says "enumerated
   defeater-check"; the replacement widens it to "enumerated
   check" so it covers the affirmative side too. Whether the
   committed requirement space enumerates affirmative checks as
   first-class members, or only defeater-checks with affirmation
   as the residue, is not stated anywhere I could find. Under the
   residue reading the widening is harmless; under the
   first-class reading it is the substance. Worth pinning, since
   the seed's symmetry argument assumes the first-class reading.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Executed under | Ruling record 2026-07-30, sha256 `45a6d7208f0faca82946f2bfacb04799994b5cf2c9afdef53f24def9d8cf8552` — R2 |
| Findings discharged | #28 (the affirmation discipline binds only `affirmed`) |
| Re-ruling | No |
| Unblocks | #2 and #3's repairs (canonical selection acquires its object); R14's succession-under-re-discharge, which re-runs this discipline at the new position |
| Explicitly not discharged | #33 (evidence falsifying the cited defeat) — ruled R14/C by supplement 2, sha256 `7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670`, and seeded separately; see note 2 |
| Status | Unpinned draft; enters the 4.2 candidate by succession |
| Ratified bytes altered | None |
