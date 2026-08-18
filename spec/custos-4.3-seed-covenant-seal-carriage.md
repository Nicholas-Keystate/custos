# Custos 4.3 seed — the covenant seal's carriage, moved off the seal

> DRAFT — repair seed for the 4.3 cycle. Unpinned until declared
> final. Enters the successor by succession; the ratified Custos
> 4.2 bytes (sha256 68cc5c9b7164b33dffcf7b705a0d1301fe108c647d356
> 38fec61d52d29b2775a) are untouched by this file. Discharges
> finding #80 only. **Executed under no numbered ruling**, and
> one is owed: R17.1 of supplement 2 of 2026-08-01 (sha256
> 7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea267
> 0) ruled the typed-seal carriage this seed replaces, so a
> superseding ruling is the vehicle and this file is its input.
> Offered to the drafting authority, which owns the wording.
>
> R17's three-layer split is **not reopened**. Layers 2 and 3
> stand exactly as ruled and as ratified. Only layer 1 changes,
> and only in where the type is written.

---

## What this seed carries

One substitution. The covenant seal stops naming its kind in a
field of the seal and starts naming it in the artifact the seal
commits to — which is where the substrate has always put it.

Everything the ratified text says the covenant seal *is* survives
unaltered. It still binds a subject to standing law rather than
to another object. Its verification still splits into three
layers at three epistemic grades. Attachment is still coordinate
lookup and lineage walk; satisfaction is still a fold. What the
seal irreducibly does — name the clause set a successor is
answerable to, forward, at a committed coordinate — is untouched.
The repair is about carriage, and carriage only.

## The defect

Finding #80 carries the evidence; the argument compresses to
this.

The substrate's typed seal types the *digest*, not the
commitment. Its `t` field answers "what procedure verifies this
digest" — the hash algorithm is already carried by the CESR code
of `d`, and `t` carries the derivation above it, the substrate's
own worked example being the Merkle-tree family, where the type
decides how an inclusion proof is checked (KERI `71cb54e`,
`spec-body.md:515`). The covenant seal puts an ordinary
self-addressing identifier of a clause set in `d`, derived the
ordinary way. There is nothing about its derivation for `t` to
say, so under the substrate's own reading the honest value would
name an ordinary digest and the type field would be vacuous.

The reference implementation reads the field a third way, as a
protocol-and-version primitive drawn from a two-member table
(keripy `7da1e64a1`, `structing.py:67-71`, `kering.py:21`), which
makes the reservation an application to join the substrate's
protocol table rather than to allocate a seal type — a larger
act, and still not an expression of commitment semantics.

And §17's premise is false. It places the reserved seal type
"in a namespace of the same kind" as the CESR genus, "the typed
seal structure's type table, externally stewarded" (L3214-3219).
The genus namespace is specified, sized and built for other
protocol stacks. The seal-type namespace has no table: the
substrate registers the *count code* that frames the couple and
never the values that fill it. A recognition question was stated
for an addressee that does not exist.

Underneath all three sits a doctrinal collision the ratified text
does not acknowledge. §10 forbids consumers from inferring
commitment semantics from context (L2047-2048); the substrate
states that seal semantics *are* modified by the context in which
the seal appears (`spec-body.md:399`). The typed seal was reached
for as the escape from that collision. It is not one — and the
repair below does not need one.

## Repair — layer 1, carriage

> **Carriage.** A covenant seal is a commitment to a covenant
> event committed in the sealing domain's designated governance
> event log. The event names its own kind in its type field,
> under this standard's grammar, and carries the clause
> identifiers of the sealed set. The seal itself is the
> substrate's ordinary source or event seal, taken unmodified:
> the commitment travels in a form every conforming substrate
> implementation already parses, and no substrate extension is
> claimed, requested or required.
>
> **Admissibility.** A covenant seal is inadmissible over content
> whose exact bytes can be committed. Where byte equality is
> achievable the digest seal is mandatory, and a covenant seal
> over digest-sealable content is the defect.

Admissibility is carried forward verbatim from the ratified text
and is not the subject of this seed. It is reproduced only
because a carriage clause that dropped it would read as
repealing it.

The substitution is shaped by the substrate's own precedent, and
the precedent is exact. A credential issuance is anchored by an
untyped event seal, and whether the anchored act is a registry
inception, an issuance or a revocation is read off the anchored
event's type field (keripy `7da1e64a1`, `vdr/eventing.py:337`;
the type vocabulary at `kering.py:360`). Nobody proposed a
revocation seal type, because the seal was never the place the
kind was written.

This standard is better positioned for that shape than the
substrate is, not worse. The sealed set is already clause
identifiers into the designated governance event log, and R15
already makes *which* registry that is a committed fact rather
than an assertion. The covenant event has a home before the
repair asks for one.

The consequence worth stating plainly: the type now lives in a
table this standard stewards. There is no reservation, no
recognition question, and no dependency on another project's
custodians for the construct to be well-formed. The absorption
KN-14 asked for is finally real — not because a value was
reserved in someone else's namespace, but because nothing needed
to be.

## The naming discipline, one dereference out

> A seal names its kind. For the first two kinds the seal's own
> shape is the name; for the covenant seal the name is the type
> field of the committed event the seal resolves to. Consumers
> are never left to infer commitment semantics from context, and
> a conviction sourced from a seal names the seal kind it
> convicts under.

The discipline is preserved, not weakened, and the reason is
worth writing down because it is the objection a careful reader
raises first.

A consumer that cannot resolve the committed event cannot
evaluate the covenant. Satisfaction is a fold over the sealed
clause set; a verifier holding the seal alone holds no clause
set, no law head and no candidate successor, and has nothing to
compute. So the class of consumers that loses wire-visible
discrimination is exactly the class that could never have acted
on it. Nothing that could evaluate a covenant seal before can
fail to identify one now.

The document's own §12.4 posture already says this in the general
case: the quantifiers range over verifiers holding the bytes,
and never promise that set is non-empty.

## What is unchanged

Layers 2 and 3 are untouched by this seed and are not restated
here, which is deliberate — a repair that recites the layers it
does not change invites the reading that it changed them.

Attachment remains coordinate lookup and lineage walk over the
committed log, the event-seal machinery reused. Satisfaction
remains a fold: a standing question under the sealed set,
appraised at a position, returning the four-valued finding with
its ground, inheriting bearing, succession under re-discharge,
the designated law head and full discharge by being a fold. A
seal joined to a defeated satisfaction finding is still breach
with a committed anchor.

§5's claim survives on the same scoping R17 gave it, and gains a
little: layers 1 and 2 are cryptographic, and layer 1 is now
cryptographic in a form the substrate's own parsers agree with
rather than in a form awaiting a steward's answer.

## The cost, stated

One thing is genuinely lost, and one apparent loss is a gain.

Lost: a consumer holding the seal but not the committed event
cannot tell from the seal alone that the commitment is a
covenant. The section above argues no consumer that mattered is
in that class, but the loss is real and should be confessed
rather than argued away.

Not lost — improved: the governance-blind consumer. §10's
carriage clause claimed a typed seal with a reserved value lets
"a governance-blind consumer parse the seal unharmed." The
opposite is nearer the truth. An ordinary source or event seal is
parsed by every conforming substrate implementation. An
unrecognized type value is precisely the input a fail-loud parser
is entitled to reject, and this standard's own §17 praises the
substrate for rejecting unallocated codes rather than guessing at
them. The colorless base §17's track one names, and the evidence
posture §12.3 states, are both better served by the ordinary seal
than by the typed one.

If the drafting authority nevertheless wants discrimination on
the wire without dereference, the substrate-shaped mechanism is
the anchoring context — a seal into the designated governance
event log is already discriminable as governance work — and not
a seal type. That route needs no reservation either.

## Notes for the drafting authority

Things surfaced in drafting that finding #80 did not name.

1. **§17 loses a reservation, and the paragraph is better for
   it.** The genus reservation stands: CESR's genus namespace is
   real, admits reservation, and was disposed on its own terms at
   #45. Striking the seal-type sentence (L3214-3219) leaves one
   reservation with one steward and one recognition question,
   which is a cleaner confession than two reservations of which
   one had no addressee. The "answered together, never separately
   by accident" clause goes with it; there is no longer a second
   thing to answer.

2. **The covenant event needs a type value, and this standard
   has never minted one.** The repair moves the naming problem
   rather than dissolving it: something must be written in the
   covenant event's type field, in a grammar this document
   specifies. That is a small act and an owned one, but it is not
   nothing, and it lands in the encoding round's territory (#57)
   if the round convenes before the successor edition closes. The
   seed deliberately does not mint the value, for the same reason
   R17's seed declined to name a reserved seal type: naming it
   here would legislate a decision surface the round owns.

3. **The station obligations R17 left behind need one
   adjustment.** The satisfaction-as-fold and breach-composition
   vectors are unaffected. The digest-precedence vector — a
   covenant seal over content whose exact bytes were committable,
   expected must-reject — must now exhibit the governance-event
   form rather than a typed seal, or it will encode the defect
   this seed removes into the corpus that is supposed to
   discriminate against it.

4. **The doctrinal collision deserves a sentence somewhere, not
   silence.** §10's "consumers MUST NOT be left to infer
   commitment semantics from context" reads, against the
   substrate's `spec-body.md:399`, as a rebuke of the substrate.
   After this repair the two are reconcilable and the
   reconciliation is interesting: the substrate says context
   modifies seal semantics, this standard says the *committed
   event* carries them, and a committed event resolved through a
   seal is the disciplined form of what the substrate loosely
   calls context. Saying so once converts an apparent
   disagreement into an alignment, which is worth more than the
   sentence costs.

5. **This is a carriage repair inside a re-rooting cycle.** The
   4.3 docket's framing is a cleaner root rather than another
   accretion pass. This seed is compatible with either: it
   removes a construct-specific extension claim, so a re-rooting
   that subsumes §10 into a smaller seal treatment inherits a
   simpler thing to subsume. It should not be held for the
   re-rooting decision, because the falsified §17 span is
   independent of how the root is drawn.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.2, sha256 `68cc5c9b7164b33dffcf7b705a0d1301fe108c647d35638fec61d52d29b2775a` |
| Executed under | No numbered ruling; a superseding ruling for R17.1 is owed |
| Supersedes | R17.1 (carriage) of ruling record supplement 2, 2026-08-01, sha256 `7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670` — layers 2 and 3 stand |
| Finding discharged | #80 (wrong axis typed; reservation into a table that does not exist) |
| Spans repaired | §10 carriage L2016-2023; §10 naming discipline L2047-2055; §17 reservation L3214-3219 (struck) |
| External citations verified | 2026-08-18 against upstream main — KERI spec `71cb54e`, CESR spec `7a6adca`, keripy `7da1e64a1` |
| Depends on | R15 (the designated governance event log is committed) |
| Charter input, not designed here | the covenant event's type value → #57 |
| Re-ruling | Yes — R17.1 only |
| Station obligations, adjusted | digest-precedence vector re-expressed in the governance-event form → #15 |
| Ratified bytes altered | None |
