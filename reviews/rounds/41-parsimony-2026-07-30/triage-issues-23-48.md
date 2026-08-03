# Clearance triage — open issues #23–#48

**Scope:** the twenty-three open issues numbered 23–48. #22, #26, #30 and
#31 are pull requests, not issues; there is no issue at those numbers.
No issue in the range is closed.

**Constraint this triage is run against.** `spec/custos-4.1.md` is
ratified and effective, pinned at sha256 `ff8b9e7a…b72b05` in
`SUCCESSION.md`, anchored at KEL sn 187/188, and enforced byte-for-byte
by `tools/verify_kernel.py` under `.github/workflows/verify.yml`. The
same holds for `spec/custos-4.0-kernel-draft.md` at `9cefdc5d…773f315`.
Ratified text is never edited (`CONTRIBUTING.md` property 1). **No issue
below can be closed by editing either spec file today.**

## Summary

Of the twenty-three, **one is PR-able now (A)**, **eight are
wording-grade and stage for 4.2 (B)**, **twelve need a ruling (C)**, and
**two are program work (D)**. Twelve of the twenty-three are
ruling-blocked — but only five of those are already on
`reviews/ruling-docket-2026-07-29.md` (#23→R8, #24→R6, #25→R9, #27→R3,
#28→R2). **Seven issues in this range need rulings that the docket does
not yet cover** (#32, #33, #35, #38, #39, #41, #44) — three of them
BLOCKING. That gap is the most important structural finding here: the
docket was assembled on 2026-07-29 and the parsimony round filed #34–#48
on 2026-07-30, so the docket is one round stale.

**The single most valuable batch of work** is the eight **B** items,
assembled as one or two 4.2 seed documents in the shape PRs #26 and #30
already established (`spec/custos-4.2-seed-<topic>.md` — a *new,
unpinned* file that quotes each ratified span, states the defect, and
supplies replacement text; both verifiers stay green). Six of the eight
are single-sentence edits whose replacement text is written out below,
and five of those six (#40, #45, #46, #47, #48) form one coherent seam —
**carriage, confession and the §17 gate lists** — so they can travel as a
single seed PR closing five MAJOR findings without a ruling, without
touching ratified bytes, and without waiting on anything. #29 is already
in flight as PR #30. That leaves #37 (a mechanical drafting pass) and
#42 as their own small seeds.

The one **A** item (#43) is the highest-value *repo* work in the range:
a BLOCKING finding whose dominant cause is that a companion artifact the
ratified text names does not exist in `companions/`. Writing it is a
plain file addition.

## Table

| Issue | Title (truncated) | Cat | Justification |
|---|---|---|---|
| 23 | 4.0 kernel's pinned digest covers 12 lines ruled "never ratified bytes" | C | Docket **R8** (with #4). Re-pin vs. declare the preimage file-as-published; either way a governance act. |
| 24 | §7.4 "converts to contested standing" returns a value the codomain lacks | C | Docket **R6**, itself blocked on **R1**. Verified: "contested standing" occurs exactly once (L1161). |
| 25 | "first-seen survival" stated in arrival vocabulary axiom 4 forbids | C | Docket **R9**. Verified: "first-seen" at L285 and L1160 only. |
| 27 | two blind impls emit different pending findings — species not in the key | C | Docket **R3**. Executed divergence; species in/out of the key is a fork. |
| 28 | affirmation discipline binds only `affirmed` | C | Docket **R2**. Literal vs. full-discharge reading. |
| 29 | Ground Axiom carries no BCP 14 keyword; `affirmed` has no ruled payload | B | Two keyword edits, both restating text already in the document. **Already drafted — PR #30.** |
| 32 | "bearing" gates every edge into `self-convicted`, defined only at T1 | C | **Not on the docket.** BLOCKING fork: define bearing vs. delegate to domain law, plus where the refusal boundary falls. |
| 33 | evidence that the defeater was invalid has no lawful destination | C | **Not on the docket.** BLOCKING fork: name a destination vs. declare defeat indefeasible by evidence. Largely downstream of R2. |
| 34 | ask KERI community for an application-defined TEL event-type extension point | D | Upstream conversation. Closure is the community's answer, not a file. |
| 35 | founding law never names the governance registry — GEL membership underivable | C | **Not on the docket.** BLOCKING fork: registry identifier vs. span-selection predicate vs. "all gAID-anchored registry events". |
| 36 | track two's ilk apparatus buys nothing at the fold boundary | D | Next action is an experiment: exhibit a discriminating case from §17's own vector families, or the finding stands and a collapse ruling follows. |
| 37 | §1.7's comprehension gate is satisfied in one of fifteen sections | B | Verified: `Composition, per the comprehension gate` occurs once, at L2176. One composition sentence per introducing section; mechanical. |
| 38 | colored evidence has no emitter, consumer, typing clause, or composition | C | Fork: define the object (incl. "committed view echo", L892, defined nowhere) vs. remove it from §2's specifies-list and §6's four. |
| 39 | covenant seal's admissibility rule and verification procedure undecidable | C | Fork: decidable admissibility test + committed clause-satisfaction language vs. re-typing the seal as a frame-local commitment returning a finding. |
| 40 | conviction-kind family not total over the rejections the document names | B | Scoping edit: the family is total over convictions and nothing else. Plus a short-cone reword into pending vocabulary. |
| 41 | compound-result product not closed over refusal | C | Docket **R11**-adjacent (issue says either ruling closes it), but distinct: the ruled span sits inside §7.5's *quoted amendment*, so it is not free surface. |
| 42 | threshold arithmetic transfers from `kt`, the slot predicate does not | B | Narrow one sentence to the algebra. Alternative closure: exercise slot disposition in a fixture (D, ties to #14/#15). |
| 43 | replay triple depends on unpinned external specs; the companion doesn't exist | **A** | `companions/engagement-companion.md` is named at §3 L575 and absent from the repo. Writing it is a plain file addition. Residual B noted below. |
| 44 | committed SAIDs over low-cardinality governance content carry no blinding factor | C | Fork: mandate a blinding factor (new obligation on object forms, interacts with #48) vs. confess and scope the commit-now/disclose-later claims. |
| 45 | a domain may emit CESR streams under an unrecognized governance genus | B | The suggested repair *is* a drafted sentence, narrow and unopposed; the broader attack was already refuted in the filing. |
| 46 | "the encoding layer is closed" exempts the two producer choices | B | Scope an over-broad claim to the consumer direction and widen an enumeration by two items. |
| 47 | compact-form gate omits the domain and the counter-table version | B | Add two commitments to a gate list for an already-undischarged deliverable. |
| 48 | the edict's bare-SAD form is not a framable stream element | B | Minimal closure is scoping §6's "no bespoke parser" claim to the at-rest case and deferring carriage to §15. (Committing carriage is a separate design act, R5-shaped.) |

---

# A — PR-able now

## #43 — the engagement companion does not exist

**Primary category A**, with a residual B and a governance act. Stated
plainly: the A work does not close the issue by itself, but it removes
the dominant cause, converts the BLOCKING grade to a MAJOR residual, and
is executable today with no ruling.

**Verified in the tree:** `companions/` contains exactly `README.md`,
`confidentiality-and-anchored-delivery.md`, `gleif-egf-mapping.md`,
`philosophy.md`. `spec/custos-4.1.md` L574–575 says "The revision of
record for each specification is pinned in the engagement companion under
this document's own pin discipline." That artifact is absent. (So is the
**notation register** of §14 L1935–1938 — the same class of gap, likewise
A-able, and worth the same pass.)

### Files to touch

1. **Create `companions/engagement-companion.md`** — informative
   companion, same header posture as the other three ("the kernel rules
   on any divergence"). Content: the revision of record for each
   specification the fold's semantics dereference, at the checkouts the
   4.1 record was exercised against and re-verified 2026-07-30 in #34,
   #43, #45–#48:

   | Specification / implementation | Revision of record |
   |---|---|
   | KERI specification (ToIP) | `71cb54e` |
   | ACDC specification (ToIP) | `f96ef54` |
   | CESR specification (ToIP) | `7a6adca` |
   | ToIP verifiable dossier specification | `c2d261c` |
   | keripy (reference implementation) | `8e67f2e6a` |

   Name the specific dereferenced spans so the pin is auditable rather
   than decorative: KERI's superseding-recovery rules A0/A1/A2 and
   B1/B2/B3 (`spec-body.md:1802–1825`), which decide `self-convicted` and
   the `window-open` species; and the dossier threshold-operator
   semantics (`dossier-spec-body.md:225`, `:373–374`), which decide which
   slots a pending requirement set enumerates. Record the two the
   document does **not** mention (the C1 recursive-delegation case at
   `:1823` and the latest-seen constraint at `:1825`) as known
   divergences.

2. **`companions/README.md`** — add a fourth row to the companion table
   and change "Three companions travel beside the ratified kernel" to
   "Four companions…". Status column: "Minted against the ratified 4.1
   edition".

3. **`tools/verify_kernel.py`** — add a check (call it check 5) that
   every companion the ratified text names by role exists in
   `companions/`: grep the edition of record for the companion names it
   uses (`engagement companion`, `notation register`) and assert a
   matching file is present. This is the guard that would have caught
   both absences, it runs green from a clean checkout, and it fits the
   file's stated contract ("proves bytes, not authority"). Keep it
   non-fatal only if the maintainers want the notation register out of
   scope for this pass; otherwise let it fail loudly.

### What remains after the A work

- **Residual B (see below):** the dossier specification is not in §3's
  substrate of record at all (L568–572 names KERI, ACDC, CESR only), so
  even a perfect companion does not reach it under §3's pin discipline.
- **Governance act:** §14 L1936 makes the *notation register*'s digest
  the one the ratification enactment SHALL pin. Pinning the engagement
  companion's digest beside it is an enactment, not a repo change.
- The alternative branch the filing offers — the Constitution commits the
  specification digests it folds under, making semantics-version a
  governed object under §11 — is a design act and would be **C**.

---

# B — wording-grade, stage for 4.2

Each item below gives the exact current bytes and the exact proposed
replacement, so a 4.2 seed document can be assembled directly from this
section. Line numbers are against `spec/custos-4.1.md` @ `ff8b9e7a…`.

## #29 — Ground Axiom keyword force (already in flight as PR #30)

**Edit 1 — §7.1, L933–935.** Current:

> A value that does not carry its ground is not a
> member of this type, whatever else it may be.

Proposed:

> A finding SHALL carry its ground; a value that does not carry its
> ground is not a member of this type, whatever else it may be.

**Edit 1′ (alternative site) — §1.4 axiom 1, L240–242.** Current:

> 1. **Ground.** A finding carries its ground — citation,
>    requirement, or proof — or it is not a finding. The codomain
>    admits no bare verdicts.

Proposed:

> 1. **Ground.** A finding SHALL carry its ground — citation,
>    requirement, or proof — or it is not a finding. The codomain
>    admits no bare verdicts.

**Edit 2 — §7.3 Required payloads, insert as the first bullet at L1042**
(codomain order), mirroring the `defeated` bullet's re-derivability
clause. The payload text is not new: it restates §7.1 L943–945 verbatim.

> - An affirmed finding SHALL carry its ground: the identity of the
>   committed evidence bundle and of the clause set under which it was
>   appraised. Both MUST be explicit or uniquely re-derivable from a
>   committed referent.

**Note.** The broader question the filing raises — whether §3 rule 1
needs a second class of normative content for definitions, axioms and
typing rules — is a genuine **C** and is *not* on the ruling docket. PR
#30 deliberately declines to decide it. Recommend it be added to the
docket as a new ruling; otherwise the keyword patches will be applied one
at a time forever (§15's six walls and all five axioms are unkeyworded
prose today).

## #37 — run §1.7's comprehension gate across the introducing sections

**Verified:** `Composition, per the comprehension gate` occurs exactly
once in 2471 lines, at L2176. §17 L2176–2181 is the model:

> Composition, per the
> comprehension gate: a GEL event is a log entry (log) carrying an
> enactment or its evidence (enact), committed by seal into the
> gAID's KEL (seal), read by exactly one fold (fold, finding), and
> subject to the law in force at its position (succession).
> Nothing here requires an eighth primitive.

The edit is one such sentence per introducing section. It is mechanical
and each is short; exemplars for the load-bearing cases, in §17's exact
form:

- **§4, Lens (L752–755):** "Composition, per the comprehension gate: a
  lens is a citation of a committed law head (log, succession) together
  with the predicate set a fold applies under it (fold, finding).
  Nothing here requires an eighth primitive." *(This is the one the
  filing calls out: had it been written, the "lens is a fourth fold
  input" argument would have had nowhere to hide.)*
- **§4, Covenant (L733–735):** "…a covenant is an enactment (enact)
  binding a subject to a clause set committed in a log (log) and
  checkable by fold. Nothing here requires an eighth primitive."
- **§4, Availability charter (L796–804):** "…an availability charter is
  an enactment obligating the fetchability of the log spans a fold
  reads. Nothing here requires an eighth primitive."
- **§6, Edict (L849–853):** "…an edict is an enactment committed by seal
  into a log at a coordinate and read by a fold."
- **§6, Verification cone:** "…a cone is the set of log spans one fold
  reads, closed transitively."
- **§9, Anchor grade (L1347–1363)**, **§12, Envelope (L1575–1598)**,
  **§12, Congruence (L1608–1629)**, **§14, Freezability (L1965–1971)**:
  same treatment.
- **§4, Organ/seat (L757–763)** and **§6, Warranty (L878–884)**: §1.7's
  own inventory already supplies the compositions ("An organ is a seated
  constructor"; "A warranty is an enactment binding its maker to a
  finding's ground") — the introducing sections must restate them in
  their own prose, per L397–398.

**One case will fail the gate, and that is the point:** §6's **colored
evidence** cannot state a composition while its component "a committed
view echo" (L892) is defined nowhere — see #38. §1.7 L405–409 supplies
the remedy for exactly that: repair Chapter 1 by succession, "or a
prescription in that section, to be removed there." So #37's pass is B
right up to the point where it meets #38, which is C.

## #40 — the conviction-kind family is not total

**Edit 1 — §6, L874–876.** Current:

> completeness is decidable by the
> replay itself, and a replay that reaches for a span the cone
> lacks convicts the cone as short.

Proposed:

> completeness is decidable by the
> replay itself, and a replay that reaches for a span the cone lacks
> yields a pending finding whose typed requirement set names the missing
> span; the cone is short, which is a defect of carriage and not a
> conviction.

**Edit 2 — §14, append one sentence after L1983.** Current paragraph ends:

> A conviction
> record from which the kind cannot be read is unauditable and
> therefore not a conviction record.

Proposed addition:

> The family is total over convictions and over nothing else: absence of
> committed evidence discharges as a pending finding, and refusal of an
> invocation is an operational fact under the separation rule of section
> 7.5 — neither is a conviction, and neither carries a kind.

**Residual, flagged:** the filing's third repair item — annotate each of
§17's six must-reject boundary vectors (L2289–2296) with its expected
codomain value, defeater class and conviction kind — is more than a
sentence and is the seam where this meets the vector work of #15 (**D**).
Recommend it travel with the vectors, not with this seed.

## #42 — the threshold reuse claim

**Edit — §8, L1257–1262.** Current:

> The threshold algebra is one algebra at both
> ends of the system — the same weighted-threshold satisfaction
> that governs key-event signing governs evidence sufficiency —
> so a verifier that can evaluate a rotation can evaluate a quorum
> of endorsements (a derivation from the substrate's design, not
> new law).

Proposed:

> The threshold arithmetic is one arithmetic at both ends of the system —
> the same weighted-threshold satisfaction that governs key-event signing
> governs evidence sufficiency (a derivation from the substrate's design,
> not new law). The slot-satisfaction predicate is not shared: a
> key-event slot is satisfied by a verified signature at an index, while
> an evidence slot is satisfied by the composed-evidence discipline this
> section states, so a verifier that can evaluate a rotation inherits the
> arithmetic and not the predicate.

**Alternative closure (D):** exercise slot-disposition evaluation in a
fixture, which discharges §14's stated-evidence-scale duty without a spec
edit. That is real program work and ties to #14 / #15.

## #45 — emission under an unrecognized governance genus

**Edit — §17, append to the Genus paragraph after L2272.** The current
paragraph (L2262–2272) ends "…enacted, unrecognized, and honest about the
difference." Proposed addition:

> Until recognition, a domain SHALL NOT emit CESR streams under an
> unrecognized governance genus on any interoperable surface: governance
> events travel in the recognized KERI/ACDC genus, and the reservation
> travels as committed evidence of its own enactment, never as a wire
> claim.

This is the filing's own drafted sentence. It is unopposed — the broader
attack on the paragraph was raised and refuted in the same review — and
it is consistent with §14's travel posture (L2034–2041), which already
forbids this document travelling as an allocation request.

## #46 — "the encoding layer is closed"

**Edit — §14, L2026–2032.** Current:

> is
> confessed, not cured, by this document: the encoding layer is
> closed (a serialization either parses canonically or fails), but
> semantic latitude above it (threshold derivation defaults,
> receipt-race edges, escrow retention) remains open wherever the
> substrate's own law is silent. A federated GARD SHALL state which latitude it has closed by
> committed profile and which it inherits open.

Proposed:

> is
> confessed, not cured, by this document: the encoding layer admits no
> interpretive latitude in the consumer direction (a serialization either
> parses canonically or fails), but the producer direction is open where
> the substrate leaves it open — serialization kind and digest derivation
> code are the producer's choice — as is semantic latitude above it
> (threshold derivation defaults, receipt-race edges, escrow retention),
> wherever the substrate's own law is silent. A federated GARD SHALL
> state which latitude it has closed by committed profile — including its
> serialization kind and its digest derivation code — and which it
> inherits open.

## #47 — the compact-form gate list

**Edit — §17, L2276–2281.** Current:

> is a committed deliverable gated, in order, on:
> the bundle-commitment rule (a committed preimage recipe by which
> one digest addresses a receipt together with its attachments;
> owed because the substrate's receipt form does not make its
> identifier field self-addressing), the governed ilk-table seats
> of track two, and conformance vectors exercising both
> presentation orders.

Proposed:

> is a committed deliverable gated, in order, on:
> the bundle-commitment rule (a committed preimage recipe by which one
> digest addresses a receipt together with its attachments — naming the
> domain, text or binary, over which the preimage is taken, and the
> counter-table genus and version under which its framing is read; owed
> because the substrate's receipt form does not make its identifier field
> self-addressing), the governed ilk-table seats of track two, and
> conformance vectors exercising both presentation orders.

Adding to a gate list for an already-undischarged deliverable commits
nothing new; it makes an existing gate satisfiable.

## #48 — the edict's carriage claim

**Edit — §6 Object typing, L905–908.** Current:

> Object forms typed this way are consumable by the
> substrate's existing toolchain; nothing here requires a bespoke
> parser.

Proposed:

> Object forms typed this way are consumable by the substrate's existing
> toolchain at rest: computing and verifying the SAID of a bare
> self-addressed data item requires no bespoke parser. Their carriage as
> stream elements is a different question and remains an undesigned
> deliverable under section 15; nothing in this paragraph settles whether
> an edict travels as sealed data or inside the substrate's wrapper for
> non-native serializations.

This is the *minimal* closure: it removes the contradiction with §15
L2069–2072 (§6 asserting as settled what §15 confesses as undesigned)
without deciding the carriage. **Deciding the carriage is a separate
design act** — the same shape as docket R5 option A, which the docket
itself calls "a design act needing its own review round, not an editorial
one." If the maintainers prefer to decide it now, #48 becomes **C**.

---

# C — needs a ruling

Five are already docketed; **seven are not**, and the docket should be
extended before the next round of drafting effort is spent.

| Issue | Docket | Note |
|---|---|---|
| #23 | **R8** (with #4) | Recommendation on record: file-as-published + a two-form §3.2 pin rule. |
| #24 | **R6** | Downstream of **R1**; the docket says rule R1 first. |
| #25 | **R9** | Recommendation on record: committed order, decisively. |
| #27 | **R3** | The only *executed* cross-implementation divergence. |
| #28 | **R2** | Precondition for PR #26's repair of #2 being meaningful. |
| #41 | R11-adjacent | The filing says either R11 ruling closes it; it is a distinct sub-question (product closure over refusal) and the ruled text sits inside §7.5's **quoted amendment block** (L1184–1195), which is even less free than ordinary ratified prose. Recommend it be added to R11 as a named sub-question rather than assumed covered. |
| **#32** | *none* | BLOCKING. Define "bearing" at T2/T3, or state it is a committed predicate and how a verifier locates it; and draw the refusal boundary between "law silent on bearing" (refuse, axiom 3) and "law silent on the violated predicate" (consume, §7.4), which are currently indistinguishable from inside the fold. |
| **#33** | *none* | BLOCKING. Where does a finding go when committed evidence falsifies the cited defeat at a fixed law head and position? Largely dissolves under R2/B (full discharge), so **sequence it after R2** — but if R2 goes the other way it needs its own ruling. |
| **#35** | *none* | BLOCKING. How is GEL span *membership* derived under track one? Three plausible inventions were exhibited. Note the shape: there is an axiom 4 ("no ambient order") and no matching "no ambient membership". |
| **#38** | *none* | MAJOR. Define colored evidence (starting with "committed view echo", L892) and type it under §6's object-typing clause, or remove it from §2's specifies-list and from §6's "four object forms". Blocks the colored-evidence half of #37. |
| **#39** | *none* | MAJOR. Replace the covenant seal's admissibility side-condition with a decidable test or drop its defect force; and give clause-satisfaction a committed language — or re-type the seal as a frame-local commitment returning a finding. Large design surface behind either branch. |
| **#44** | *none* | MAJOR. Mandate a blinding factor on objects whose SAID is committed before disclosure, or confess the leak and scope the commit-now/disclose-later claims. Interacts with #48 (a `u` field on a bare SAD) and with the existing `confidentiality-and-anchored-delivery.md` companion, which is informative and therefore cannot discharge a normative gap. |

---

# D — program work

## #34 — upstream ask: application-defined TEL event types

Closure is the KERI community's answer, not an artifact in this repo.
**The A-able half:** draft the question as a file under `upstream/`
(which today holds only `x509-trust-route-assumptions-note.md`) so it
travels as a question, per §14's travel posture at L2034–2041 — "Nothing
in this document SHALL travel as a defect report, an allocation request,
a custody selection, or an extension proposal … Questions travel as
questions." The evidence is already assembled in the issue (ACDC
`f96ef54` `spec-body.md:1918`; keripy `8e67f2e6a`
`serdering.py:410-428`, `:525-533`, `FieldDom.strict` at `:118`). The
conversation itself — WebOfTrust discussion, dev call, or Discord —
remains the blocker. Distinct from #18, and narrow enough to go first.

## #36 — does track two buy anything at the fold boundary?

The next action is an experiment, not an edit: work §17's own equivalence
and boundary vector families (L2286–2306) and try to exhibit a
conforming Gever that must behave differently on the two tracks. If one
exists, the finding is withdrawn and the issue closes with a comment and
no spec change — the cheapest possible clearance. If none exists,
collapsing to one track is a **C** ruling with a large blast radius: §17's
bootstrap, the ilk table, the genus reservation (#45), and the compact
form gate (#47, gated on "the governed ilk-table seats of track two")
all hang off track two's existence. Also partly dependent on #34's
upstream answer.

---

# Stale or already answered

**None.** Every line citation in #23–#48 that I checked resolves against
the ratified bytes at `ff8b9e7a…b72b05`. Specifically re-verified:

- #23 — `sha256sum spec/custos-4.1.md` reproduces the pinned digest;
  `spec/custos-4.0-kernel-draft.md`'s whole-file digest is what
  `verify_kernel.py` checks.
- #24 — "contested standing" occurs **once** in 2471 lines (L1161).
- #25 — "first-seen" occurs at L285 and L1160 only, exactly as cited.
- #27 — §7.3 L1048–1051 names the key as `(subject, kind,
  citing-clause bytes)`, three fields; §7.2's species field is not
  among them.
- #29 — §7.1 L930–939 and §1.4 L240–242 carry no BCP 14 keyword; §7.3
  Required payloads (L1040–1053) has exactly three bullets and no
  `affirmed` bullet.
- #37 — `Composition, per the comprehension gate` occurs once, at L2176.
- #38 — "colored evidence" appears in §2's specifies-list (L451), in
  §6's intro (L846–847, wrapped) and in its own bullet (L886); §6's
  object-typing clause (L898–908) types the edict, the warranty and
  requirement elements, and neither colored evidence nor the cone.
  "view echo" occurs once, at L892, undefined.
- #40 — §14 L1973–1983 and §6 L875–876 are verbatim as quoted.
- #41 — §7.5 L1184–1195 is a quoted ratified amendment block; the
  compound-product SHALL is inside it.
- #43 — `companions/` does not contain an engagement companion (nor a
  notation register); §3 L574–575 says the revisions are pinned there;
  §3 L568–572's substrate of record names KERI, ACDC and CESR only, and
  the dossier specification is not in it.
- #44 — a case-insensitive grep for `entropy|nonce|uuid|salt|blinding`
  over `spec/custos-4.1.md` returns **0**.
- #45, #46, #47, #48 — §17 L2262–2272, §14 L2023–2032, §17 L2274–2284
  and §6 L898–908 are verbatim as quoted.

One correction worth recording rather than a staleness: #38 says "colored
evidence" occurs "exactly twice"; it occurs three times, the third being
the §6 introduction at L846–847 where a warranty is said to travel "as a
component of colored evidence". The substance of the finding is
unaffected — that mention is not a normative user either.
