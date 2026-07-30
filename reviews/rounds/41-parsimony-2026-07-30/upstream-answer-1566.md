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
item is void and the list must be restated. Add the dependency; do not
draft the seed until #36 is ruled.

### #35 — **untouched, and slightly sharpened.**

Founding law still never names the governance registry. If anything the
`(td, ts)` path makes the gap worse: a GEL becomes even more
indistinguishable from a credential registry when it is literally a `rip`
registry differing only by the state strings inside it. `rip`'s field set
(`v,t,d,u,i,n,dt` — `serdering.py:525`) offers no purpose field to hang a
designation on, so the designation has to come from founding law exactly as
the issue says.

### The ruling docket (R1–R13)

**Unaffected.** Every docket item is an internal-semantics fork — finding
codomain, transition system, refusal scope, requirement-set keys. None
depends on substrate event grammar. Nothing here unblocks any of the
thirteen.

---

## New work Sam volunteered, worth filing

These were unprompted and bear on ratified text:

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

---

## Follow-up ask, recommended

The genus question was never posed. Suggested narrow follow-up on the same
thread, after the thank-you:

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
