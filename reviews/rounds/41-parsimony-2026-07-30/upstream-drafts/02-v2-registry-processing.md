# Draft 02 — a processing layer for the v2 registry

**Home:** new issue on WebOfTrust/keripy.
**Custos tracker:** #54. **Post after draft 01**, and do not take up the
implementation offer until Custos #55 reports — if a governance enactment
does not fit the `(td, ts)` form, this would be built against the wrong
shape. Posting it as a design question earlier is fine and probably good.

**Suggested title:** Is anyone working on processing for the v2 registry
(`rip`/`bup`/`upd`), and should anchoring be separable from state
interpretation?

---

## What I think the current state is

As of `8e67f2e6a`, the ACDC v2 registry exists as **construction and
encoding** but not as **processing**:

- Builders — `src/keri/acdc/messaging.py`: `registryIncept` (`rip`),
  `blindate` (`bup`), `update` (`upd`).
- Field domains — `SerderACDC` at `serdering.py:525-533`.
- CESR structures for blinded state — `BlindState` and `BoundState`
  (`structing.py:82`, `:96`), count codes `-a`/`--a` and `-b`/`--b`
  (`counting.py:264-267`), parser support (`parsing.py:2393`, `:2434`).

What I can't find is a v2 `Tever` — anything that accumulates state,
verifies an event's anchor in the issuer's KEL, escrows events arriving
before their anchor, or replays a registry. `src/keri/vdr/eventing.py` is
the v1 registry (`vcp`/`vrt`/`iss`/`rev`/`bis`/`brv`), with the
`issued`/`revoked` state machine.

I looked at open PRs and issues before writing this and didn't see it in
flight — the nearest are #1479 (`Baser.cloneMsg` is v1-only) and my own
#1558. Please correct me if I've missed something; I'd rather join work
than duplicate it.

## The question underneath

I'd like to build on the v2 registry, and I'll need processing to do it.
Before writing anything I want to ask about a structural choice, because
getting it wrong would be expensive to undo.

The v1 `Tever` **fuses** two concerns:

1. **Substrate mechanics** — is this event anchored by a seal in the
   issuer's KEL, is it in order, does it escrow correctly if its anchor
   hasn't arrived, can the registry be replayed deterministically.
2. **State interpretation** — what the event *means*, i.e. the
   `issued`/`revoked` machine.

(1) is generic over any transaction event type. (2) is specific to
credential issuance.

Would you be open to a v2 processing layer that keeps those separate —
anchoring, ordering, escrow and replay implemented once, parameterised by
an application-supplied interpretation of the state string?

## Why I think this is worth the seam

It connects to the answer you gave me in #1566. I'd asked whether there
was an extension point for application-defined transaction event types,
and the answer was essentially no, with the observation that the state
string's vocabulary is unconstrained and `td` needn't address an ACDC —
so use those.

Taking that seriously: what an application like mine actually needs isn't
a registry of new ilks, and it isn't a new genus. It's **anchoring,
ordering and replay for events whose meaning the application owns**. That
is exactly (1) without (2). If (1) is generic in the implementation, the
extensibility you described becomes usable without anyone minting an ilk,
reserving a code point, or coordinating anything — which seems more in
the spirit of "the seals need no semantics beyond their secure
attributability" than a type registry would have been.

It also means the second, third and fourth applications to want this
don't each reimplement escrow.

## What I'm offering

I'm willing to do the work, and I'd rather do it in the open in keripy
than carry a fork. What would help before I start:

- Is a v2 `Tever` already designed, or in progress somewhere I haven't
  looked?
- Is the fused-vs-separated question already settled by a constraint I
  can't see from the outside?
- Does the planned `xfr` event change the shape of the state accumulator
  enough that this should wait for it?

Related: #1558, on whether `Tever.verifyAnchor`'s single-seal requirement
is normative or an implementation simplification — the answer bears on
what a v2 anchor check should do.
