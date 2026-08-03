# Upstream answer — WebOfTrust/keripy discussion #1566

**Asked:** 2026-07-30 (dhh1128), per issue #34 / ticket T1.
**Answered:** 2026-07-30T23:26Z by SmithSamuelM.
**Verified against:** keripy `upstream/main` @ `8e67f2e6a` (2026-07-29), the
same checkout the parsimony round cited. All code claims below re-checked
today.

---

## What Sam said, decomposed

**1. The v2 registry ilk set is closed *and* actively curated.** Two
changes are planned: deprecate `upd` (a blindable update can be unblinded
by attaching the unblinded attribute block, so the unblinded variant is
redundant), and add `xfr` — a **doubly-anchored transfer of registry
control** from the issuer AID named in `rip` to a new controller named in
`xfr`. Motivated by SEDI and asset-transfer use cases.

**2. The direct answer on an extension point: no.** Verbatim — "The TEL
concept is meant to be general to accommodate any future applications. One
can define it how one wants. The seals in the associated KEL don't
differentiate what they are sealing so there could be any number of TEL
types. But like anything, defining one's own TEL type with its own set of
events then means one has to get buy in for it to be widely adopted. But
as they say its a free country."

That is the status quo T1 already described, confirmed by the maintainer:
permitted at the specification layer, unimplemented at the reference layer,
and the adoption cost is the application's to carry. **No registration
mechanism is planned.** The contingency issue #36 named — "if
application-defined transaction event types become registrable, track two
stops being exotic" — resolves against track two.

**3. The recommended path, which is new information.** The v2 blindable
state registry's attribute block links an ACDC SAID and a **state string**,
and "the set of state strings and the semantics of those is not limited."
So an application whose transaction state is representable as a string
already has a home. Further: it is not limited to ACDCs — "the ACDC said
field could be a SAID (or merkle tree root) of something else." Precedent
already on their roadmap: anchoring the IPEX **Grant message SAID** instead
of an ACDC, so the registry event's state includes the grant contents, not
merely the state string. Extension by layering two ACDCs — the top-level
one carries the extended state, the second-level one is the subject of that
state — which is exactly what the Grant anchor does.

**4. Two attachment primitives.** The BAB (blinded attribute block) has a
group code letting it attach to any message. The **BBAB** (bound blinded
attribute block) adds two fields — the `sn` and SAID of an event in the
**issuee's** KEL — cross-anchoring the state change to the issuee's key
state as well as the issuer's. Purpose Sam gave: broken delegation chains
break and repair more intelligently.

---

## Verification against `8e67f2e6a`

| Claim | Status | Evidence |
|---|---|---|
| State string vocabulary unconstrained | **confirmed** | `structing.py:80` — `ts` = "state as string text (Labeler)"; `Labeler` (`coring.py:3342`) is a generic textual field value with no vocabulary. `messaging.py:97` docstring: "state (str): transaction event state string". |
| `td` need not be an ACDC SAID | **confirmed structurally** | `structing.py:79` documents `td` as the ACDC top-level `d`, but the cast is `Castage(Noncer, 'nonce')` (`structing.py:291`) — any qb64 digest fits. No validator constrains it. |
| BAB shipped | **confirmed** | `BlindState(d,u,td,ts)` at `structing.py:82`; count codes `-a` / `--a` (`BlindedStateQuadruples`) at `counting.py:264-265`; parser at `parsing.py:2393`. |
| BAB attachable to any message | **confirmed** | It is a count-code group in the v2 attachment table, not bound to a message type. |
| BBAB shipped | **confirmed** | `BoundState(d,u,td,ts,bn,bd)` at `structing.py:96`; count codes `-b` / `--b` (`BoundStateSextuples`) at `counting.py:266-267`; parser at `parsing.py:2434`. Its own source comment states Sam's delegation rationale: "cross anchors the issuees key state to the issuers key state ... so that downstream issuances by issuee can be verified against the delegated entitlements". |
| `bup` commits to the BAB | **confirmed** | `messaging.py:72` — `b=blid`, "qb64 blindable state attribute block said". The event's SAID therefore covers a digest over `(d,u,td,ts)`. |
| `xfr` | **roadmap only** | No occurrence of `xfr` anywhere under `src/keri`. Not in `Ilkage` (`kering.py:353-362`). |
| `upd` deprecation | **roadmap only** | `upd` present in `Ilkage`, in the `SerderACDC` field dom (`serdering.py:531`), and as a builder (`messaging.py:78`). |
| **v2 registry has no fold** | **new, and load-bearing** | `rip`/`bup`/`upd` appear only as *message builders* in `src/keri/acdc/messaging.py`. There is no v2 `Tever`. The `issued`/`revoked` state machine in `vdr/eventing.py` is the **v1** registry. |

That last row is not something Sam said, and it matters: **there is no
incumbent v2 registry fold whose semantics a Gever would collide with.**
Custos would be defining the first one. The parsimony round's premise —
that the extension point exists on paper and not in code — is true of the
v2 *fold* even more completely than of the v2 *events*.

---

## Disposition of the open issues

### #34 — **closed by this answer.**

The issue's action was "take a message to the KERI community and find out
what's possible," and triage recorded that "closure is the community's
answer, not a file." The maintainer answered. Record the answer and close.

Note what the answer does, though: it **does not remove Custos work — it
redirects it.** T1 predicted that a positive answer would delete most of
track two's cost. The answer is negative on the mechanism and positive on a
path neither track describes. So the saving is available, but only if
Custos takes the third path deliberately.

### #36 — **not closed; decisively re-weighted, and a third disposition opens.**

The issue offers two exits: exhibit a case where a conforming Gever must
behave differently on the two tracks, or collapse to one track. Sam's
answer supplies neither directly, but it does two things:

1. **Its stated contingency resolves against track two.** No registration
   mechanism is coming; minting governance ilks means forking the registry
   layer and buying adoption, indefinitely. Track two's cost is now known to
   be permanent rather than transitional.
2. **It exposes a third form that dominates both tracks as §17 describes
   them.** Use `rip` + `bup`/`upd` unchanged, and carry the governance act's
   kind in `ts` and its content SAID in `td`. This is *not* track one as §17
   frames it (`:2216-2222`: governance semantics "carried entirely by the
   committed law that interprets them", content behind an opaque SAID) —
   the act's kind is on the wire, in a field the substrate parses, with
   **no minted ilk and no genus reservation**. And it is not track two.

So #36's likely repair is now: **collapse to track one, and amend track
one's own description to name the `(td, ts)` extension surface**, so it
stops being the "parses everywhere and means nothing anywhere" option the
review correctly attacked.

**One caveat before Custos leans on this.** With `upd` deprecated, `ts`
lives inside the *blinded* attribute block on `bup`, not in the event body.
On-wire legibility becomes disclosure-gated rather than public-by-default:
a governance-blind consumer sees a blind SAID until the unblinded BAB is
attached. Cryptographic commitment is intact (`bup.b` covers the BAB SAID),
and for a public governance log you simply always attach the unblinded
block — but the legibility claim needs that qualification, and §17 would
have to say so. This is a design decision, not a free win. (It is also,
separately, a **privacy gain** worth weighing against the round-B
correlation findings.)

### #45 — **not closed; unanswered, and its cause becomes removable.**

Sam said nothing about CESR genus allocation — the genus question was never
put to him. Two consequences:

- The recommended path needs **no genus at all**. If Custos collapses to
  the `(td, ts)` form, the reservation loses its justification and #45
  dissolves by deletion rather than by ruled span. Note the CESR reviewer
  already established the genus is separable from track two anyway
  (F3: "ilks are `t`-field string values, not CESR codes ... the paragraph's
  defect is that it treats a code-table selector as though it were an ilk").
- **The genus-allocation question should now be asked directly**, and Sam is
  the right person to ask. That is the missing half of the upstream
  conversation, and it is the one that would close #45 outright rather than
  by removal. See the follow-up below.

#45's own recommended repair (a domain SHALL NOT emit under an unrecognized
governance genus on an interoperable surface) stands regardless of which
way Custos goes.

### #47 — **touched, not closed.**

The compact-form gate (`:2274-2284`) lists "the governed ilk-table seats of
track two" as its second ordered gate. If track two collapses, that gate
item is void and the list must be restated.

**Correction to this entry as first drafted.** It said "do not draft the
seed until #36 is ruled." The seed is already drafted and open as **PR
#49**, which carries `Closes #45` and `Closes #47`. So the advice was
issued too late to be taken, and the live question is not whether to draft
but whether to *land*. That is the most schedulable consequence of this
whole answer and it was nearly missed. See the execution log.

### #35 — **untouched, and slightly sharpened.**

Founding law still never names the governance registry. If anything the
`(td, ts)` path makes the gap worse: a GEL becomes even more
indistinguishable from a credential registry when it is literally a `rip`
registry differing only by the state strings inside it. `rip`'s field set
(`v,t,d,u,i,n,dt` — `serdering.py:525`) offers no purpose field to hang a
designation on, so the designation has to come from founding law exactly as
the issue says.

### The ruling docket

**No existing ruling is unblocked, but the docket grew.** As first drafted
this entry read "R1–R13: unaffected," which was wrong twice — the docket
ran to R18 plus sub-question 11a at the time, and the answer did not leave
it untouched. Corrected:

- **R1–R14, R16–R18, 11a — genuinely unaffected.** Each is an
  internal-semantics fork (finding codomain, transition system, refusal
  scope, requirement-set keys, colored evidence, the covenant seal,
  blinding). None depends on substrate event grammar. Nothing here
  unblocks any of them, and in particular none of the six BLOCKING
  rulings moves.
- **R15 (#35) — amended.** A fourth membership option is now on the
  record as **R15a**: membership by committed state vocabulary. Recorded,
  not adopted; it does not displace option A, because under a deprecated
  `upd` the state string sits in the blinded block and membership becomes
  disclosure-dependent.
- **R19 (#36) — new.** #36 was triage category D (program work) and is now
  a ruling, because the answer resolved its contingency and disclosed a
  third option. It is the only docket item that gates work already in
  flight.

Both were appended to `reviews/ruling-docket-2026-07-29.md` as a third
batch on 2026-07-30.

---

## Capabilities disclosed, and the work they generate

**The heading here first read "New work Sam volunteered," which was
ambiguous and wrong in both readings.** Nothing below is work the
maintainer volunteered *to do for Custos*. `xfr` and the `upd` deprecation
are keripy roadmap items that upstream will build for upstream reasons
(SEDI, asset transfer); the BBAB is already shipped. What was volunteered
is *information*. The work these generate for this repository is
**reaction** — deciding how the Gever treats a capability someone else
owns — and that is #52 and #53.

The genuinely new *Custos* work is in the section after this one, and it
is larger than the reaction work.

These bear on ratified text:

1. **`xfr` — registry control transfer.** A substrate event that moves
   control of a registry from the `rip` issuer to a new controller,
   doubly anchored. Custos §4 GEL anchoring, §10 rotation policy and §16
   succession all assume the gAID controls its GEL. This is either an
   opportunity (a substrate-native mechanism for transferring governance
   authority, with the double anchor doing exactly the work Custos's seal
   ladder wants) or a hazard (a substrate-level transfer the Gever has no
   rule for, capable of moving a GEL out from under its founding law).
   Worth an issue either way; roadmap, so there is time.

2. **BBAB / `BoundState` — binding a state change to the issuee's key
   state.** Shipped today (`-b` / `--b`). §7.4's duplicity ladder and §13's
   recourse ladder both turn on "which key state was in force at this
   coordinate." This is a substrate primitive that may discharge some of
   what Custos specifies by hand. Worth an evaluation pass.

3. **`upd` deprecation** — any Custos text or conformance vector that
   presumes `upd` is on a deprecation path.

   **Swept 2026-07-31: clean, no issue filed.** `upd` occurs nowhere in
   `spec/`, `companions/`, `tools/`, or any root artifact. The only
   occurrences in the repository are review prose and this document. §17
   speaks of ilks abstractly and names no specific v2 event type, so no
   ratified span and no owed vector inherits the deprecation. Nothing to
   do — recorded so the check is not repeated.

   The residual is indirect and belongs to **R19**: if §17 collapses to
   the `(td, ts)` form, the amended track description will be the first
   ratified text to depend on a specific v2 event's field list, and *that*
   text would inherit the deprecation. Which is an argument for describing
   the surface (a SAID and a state string) rather than naming `bup`.

---

## Custos feasibility work this answer generates

Filed 2026-07-31, a day after the rest, when an audit asked what work the
answer creates that nobody is tracking. Both had been *stated* in this
document and neither had been *filed* — the first as a one-line
observation under the verification table, the second not at all.

**#54 — the ACDC v2 registry has no fold upstream.** `rip`/`bup`/`upd`
exist as message builders and CESR structures; there is no v2 `Tever`, so
no state accumulation, anchor verification, escrow or replay. The reuse
posture holds at the encoding layer and not at the processing layer. Not
a defect in ratified text — 4.1 names no protocol version — but it becomes
load-bearing the moment R19 rules toward the v2 form. Two-sided: the
opportunity (no incumbent fold to contradict, and the v1 Tever's
`issued`/`revoked` codomain would have fought the design anyway) is as
real as the cost. #14 and #15 both inherit it: a v2 GEL fixture cannot be
produced by driving keripy alone.

**#55 — nobody has shown a Custos enactment fits the `(td, ts)` form.**
This is the one that undercuts a recommendation this repository has
already made. R19 recommends collapsing to that form on the strength of
the substrate's *permissiveness* — `ts` has no vocabulary, `td` takes any
digest — which establishes only that the substrate will not reject it. It
does not establish that the form carries an edict, a warranty, a
requirement element, or a covenant seal. Those are different claims and
only the first was checked. If everything needs the layered-ACDC
arrangement the maintainer described, the collapsed track is not the
simple thing R19 sells, and the ratifying authority should not be asked
to rule until that is known.

**#55 blocks R19.** The docket has been updated to say so. It is also the
experiment #36 originally asked for, re-pointed: #36 wanted a
discriminating case between the two existing tracks, and the better
question is now whether the track we would collapse *to* holds the
payload.

---

## Upstream work nobody is doing, that Custos needs

The framing "upstream will build this" is wrong, and worth correcting
because it licenses waiting. keripy's maintainer group is the community,
and this project's author is in it. "It's a free country" is not a
deferral to someone else; it is a statement that whoever needs the
capability builds it. Custos is the party that needs it.

**Checked 2026-07-31, so this is not speculation about the queue:**
keripy has 25 open pull requests and none touches a v2 registry fold.
The nearest adjacent open issues are #1479 (`Baser.cloneMsg` is v1-only)
and #1558 (this project's own `Tever.verifyAnchor` single-seal question).
Recent commit traffic under `src/keri/acdc/` and `src/keri/vdr/` is IPEX
verbs, edge operators and Serder conventions. **Nobody is building the
processing layer.**

Three pieces, very different in size and leverage:

1. **Argue against the `upd` deprecation.** Cheapest by far — a
   discussion post — and the highest leverage for this standard. R19's
   entire central caveat exists *because* `upd` is slated for removal: it
   is the unblinded update that carries `td`/`ts` in the event body, and
   without it the state string retreats into the blinded block and
   governance legibility becomes a disclosure act. The upstream rationale
   for deprecating it ("a blindable update can be unblinded by merely
   attaching the unblinded attribute block") is sound for credential
   state, where blinding is the default and disclosure is the exception.
   **A public governance log inverts that.** That is a real, specific,
   community-facing argument that nobody but this project is positioned
   to make, and if it lands, R19 option A gets materially cleaner.

2. **Write the v2 registry processing layer** — the substance of #54, and
   the one worth thinking about structurally rather than just doing. The
   v1 `Tever` **fuses** two concerns: verifying that an event is anchored,
   ordered and escrowed correctly, and interpreting what its state
   *means* (`issued`/`revoked`). A v2 processing layer written with that
   seam open — anchoring, escrow and ordering generic over an
   application-supplied state interpretation — would give Custos exactly
   the substrate half it needs while leaving the Gever to supply the
   governance half.

   Note what that would also be: **it is the extension point the ask in
   #34 requested, arriving by a different door.** Sam declined to build a
   registry of application-defined *event types*. But the need underneath
   that ask was never really new ilks; it was anchoring, ordering and
   replay for events whose meaning the application owns. A generic
   processing layer supplies that without any new ilk, any new genus, or
   any coordination — which is consistent with everything he said, and
   with "as they say its a free country."

3. **`xfr`.** Described upstream with a design constraint already stated
   (doubly anchored, `rip` issuer to new controller) and no implementation
   behind it. Medium-sized, and directly relevant to the governance
   authority-transfer question in #52.

**Sequencing.** 1 before 2 — the argument is nearly free and it changes
what 2 has to accomplish. And 2 should wait on #55, because if a Custos
enactment does not fit the `(td, ts)` form at all, the processing layer
is being written against the wrong shape.

These are recorded here rather than filed as issues on this tracker
because they are keripy work, and `CONTRIBUTING.md` is explicit that
reviews of adjacent communities' work "travel as questions to them, never
as defect reports about them." They belong in keripy's tracker, opened by
a community member, on their own merits.

---

## Follow-up ask — posted

The genus question was never posed in the original ask. Posted to the same
thread on 2026-07-31 by dhh1128. **Awaiting answer; #45 stays open on it.**
Drafted as:

> That mostly answers it — the `(td, ts)` pair is a bigger extension surface
> than I'd read it as, and an unconstrained state string plus a `td` that
> can be any SAID covers the merkle-root case directly.
>
> One thing I didn't ask and should have. Separate from event types: what's
> the process for a CESR protocol genus? The spec says the genus/version
> table is the one table all protocols must hold identically, and Annex A
> describes entry as "first needed first-entered", but I can't tell whether
> that means an application coordinates a code point with you before
> emitting under it, or reserves one and seeks recognition afterward. I'd
> rather not emit streams under three characters nobody has agreed I hold.
>
> Also — is `xfr` far enough along to be worth tracking? A doubly-anchored
> transfer of registry control is directly relevant to what I'm doing with
> Nico, more so than the event-type question was.

---

## Execution log

Every recommendation above, and where it went. Added 2026-07-31 because
the document as first written was a list of recommendations with no record
of which had been acted on — which is the failure mode a provenance
artifact exists to prevent.

| Recommendation | Status | Where |
|---|---|---|
| Close #34, recording the answer | **done** 2026-07-30 | issue #34 comment + closed |
| #36: promote to a ruling | **done** | docket **R19**; issue #36 comment |
| #35: record the fourth option | **done** | docket **R15a**; issue #35 comment |
| #45: note the two consequences | **done** | issue #45 comment |
| #47: note the gate dependency | **done** | issue #47 comment |
| File `xfr` | **done** | issue **#52** |
| File BBAB | **done** | issue **#53** |
| Sweep Custos text for `upd` | **done** 2026-07-31 | clean; no issue filed (see above) |
| Ask the genus question | **done** 2026-07-31 | posted to discussion #1566 by dhh1128 |
| Revise `why-a-gel-and-not-a-tel.md` | **done** | it argued for an ask that has now been answered, and carried §17's understatement of track one |
| Commit the round and this answer | **done** | `75f46bf`, `eaeeef1`, `197be3b` on `docket/rulings-2026-07-29` (PR #31) |

### Open, and owned by someone else

These are not oversights. Each needs a decision this document has no
standing to make.

1. **PR #49 — land, split, or hold.** It carries `Closes #45` and
   `Closes #47`, and R19's recommended option removes the text both
   repairs amend. The sequencing note is posted on the PR recommending a
   **split** — land #46, #48 and the #40 partial now (none depends on
   §17's track structure), hold #45 and #47 for R19. **Not executed.**
   Splitting a PR is a drafting act, and `CONTRIBUTING.md` gives the
   drafting authority the wording.
2. **R19 and R15a await ruling.** Recommendations on the docket carry no
   force. Until R19 is ruled, §17's two tracks stand as ratified text and
   nothing about the `(td, ts)` form is committed.
3. **#45 awaits Sam.** The genus question is posted and unanswered. Two
   exits remain: steward recognition, or R19 removing the paragraph's
   subject.
4. **#52 and #53 are evaluation passes, unscheduled.** #53 in particular
   carries a marked-speculative claim (that the BBAB may discharge §7.4
   and §13 work) that no vector exercises. It should not be relied on
   until someone tries to express a recourse scenario with it.

### Known limitation of this document

Its verification column is a snapshot of keripy `8e67f2e6a` taken
2026-07-30. Two of the rows it depends on most — the `upd` deprecation and
`xfr` — are **roadmap, not code**, sourced from one maintainer's message
rather than from bytes. Per `CONTRIBUTING.md`'s speculation rule, any
Custos text that comes to rest on them must say so. R19's option A rests
on the `upd` deprecation for its central caveat about disclosure-gating,
which is the single largest unverified dependency in this whole analysis.
