# Tickets — parsimony review, round A (2026-07-30)

Drafted from the confirmed findings of the three-seat parsimony panel
(Skeptic, Spec-Precision, Relation-Algebra) against `spec/custos-4.1.md`
at sha256 `ff8b9e7a…b72b05`. Not yet filed.

Round B (Security, Governance, CESR/Wire, Privacy) is still running; its
tickets will follow as a second batch.

Ticket 1 is an upstream ask rather than a spec defect, and carries a
ready-to-adapt message for the KERI community.

---

## T1 — Ask the KERI community for an extension point for application-defined TEL event types

**Kind:** upstream ask, not a Custos defect
**Priority:** high — resolving it upstream removes work here

### What

The ACDC specification says TELs are meant to carry more than credential
state. keripy implements a closed set of registry event types — six under
KERI v1, three more for the ACDC v2 registry — each with a fixed field
list. So the extensibility exists on paper and not in code, and Custos
pays for that in §17 by offering two event-form tracks where one would
do.

If keripy grew a way to register an application-defined transaction event
type, most of track two's cost would go away — including, probably, the
need for Custos to reserve its own CESR genus.

### Why it matters here

Track one reuses the six existing forms, so governance content has to sit
behind an opaque SAID. Track two mints governance ilks, which the ACDC
spec explicitly permits, but no tooling anywhere has seen them. Custos
carries both, plus a genus reservation nobody upstream has recognized,
and §17 openly calls that "enacted, unrecognized". All of that is a
workaround for a missing extension point rather than anything Custos
wants.

### Evidence

- ACDC spec (trustoverip/kswg-acdc-specification @ `f96ef54`,
  `spec/spec-body.md:1918`, "Transaction event logs (TELs) as ACDC state
  registries"): "Any number of transaction event types can be constructed
  for different applications that may be securely attributed without
  complicating KEL semantics. The seals need no semantics beyond their
  secure attributability to the AID of the KEL controller."
- keripy @ `8e67f2e6a`, `src/keri/core/serdering.py:410-428` declares the
  KERI-v1 registry ilks `vcp`, `vrt`, `iss`, `rev`, `bis`, `brv` with
  fixed `alls` field dicts; the ACDC-v2 registry ilks `rip`, `bup`, `upd`
  at `:525-533` are likewise a closed set with fixed `alls`.
  `FieldDom.strict` defaults to `True` at `:118` and none of these nine
  overrides it, so an extra field raises `ExtraFieldError` (`:786`) on
  parse and `SerializeError` (`:1021`) on construction.

### Action

Take the message below to the KERI community — a WebOfTrust discussion,
the dev call, or Discord. It deliberately says nothing about Custos, so
it can be asked on its own merits. Re-verify both citations before
posting; keripy moves.

> The ACDC spec is explicit that TELs are meant to extend past credential
> state:
>
> > Any number of transaction event types can be constructed for
> > different applications that may be securely attributed without
> > complicating KEL semantics. The seals need no semantics beyond their
> > secure attributability to the AID of the KEL controller.
>
> I read that as an invitation: an application defines its own
> transaction event type and gets anchoring and attribution for free.
> Concretely, an application wanting an anchored, replayable log of
> something that isn't credential issuance — policy changes, device
> enrollment, membership in a group — and wanting those events to say
> what they are on the wire.
>
> In keripy the registry event types are a closed set: `vcp`, `vrt`,
> `iss`, `rev`, `bis`, `brv` under KERI v1, and `rip`, `bup`, `upd` for
> the ACDC v2 registry. Each has a fixed field list in `serdering.py`,
> `FieldDom` defaults to `strict=True`, and no registry entry overrides
> it, so an event carrying an extra field fails validation.
>
> That leaves an application defining its own type with two options. It
> can reuse an existing form and put everything behind the SAID, which
> parses everywhere and means nothing anywhere — the content is invisible
> even to the application's own tooling until it dereferences. Or it can
> fork the registry layer.
>
> My question is really about v2, since that's where the work is. Is the
> `rip`/`bup`/`upd` set meant to be closed the same way v1's is, or is
> there an extension path there I've missed? And if it is closed by
> design, what's the intended home for an application that wants its own
> anchored transaction event type — is the answer "carry your state in
> ACDCs instead", or something else?

---

## T2 — Founding law must name the governance registry

**Severity:** HIGH (blocking)
**Spec:** §17 tracks and bootstrap (`:2213-2240`), §4 genesis knot
(`:617-620`), §11 (`:1490-1494`)

### What

Under track one, a governance event and a credential issuance are the
same bytes in the same form. The spec expects a governed domain to
produce both. It commits a rule for what order to fold governance events
in, and no rule for which events are governance events. The bootstrap
commits the track a domain uses; it never commits which registry is the
governance registry.

### Why it matters

Two correct implementations holding identical bytes can compute different
constitutions, with no error raised. One folds every registry event under
the domain's identifier as governance, and the constitution acquires
clauses nobody enacted. Another looks for a designation, finds none, and
picks a rule — first registry created, or the one named in founding law,
or the one whose identifier appears in a given clause. Custos elsewhere
requires that two evaluations of the same inputs return byte-identical
findings. This breaks that silently.

Note the shape: the defect exists because the reduction of the GEL to a
TEL is so complete. Nothing distinguishes the two at the byte level, and
nothing is committed that would.

### Fix

Require the founding law to commit the governance registry's identifier
(or a span-selection predicate) at the same grade §17 already gives to
track choice. Add a must-reject boundary vector for a stream whose
governance registry cannot be derived.

### Note

§1.4's axiom 4 says "No ambient order". There is no matching "no ambient
membership" axiom, and that is the gap in one line.

---

## T3 — The pending-to-self-convicted edge can fire with no payload that satisfies its own rule

**Severity:** HIGH (blocking)
**Spec:** §7.3 (`:1062-1064` the edge, `:1052-1053` the payload rule),
§7.1 (`:953-957`), §7.4 (`:1165-1168`)
**Duplicates:** existing ruling docket R10 / issue #6

### What

A self-convicted finding must carry the identifier of the canonical proof
package for a contradictory pair. The `affirmed` and `defeated` edges into
that state both condition on a contradictory pair, so they can always
supply one. The `pending` edge adds a second trigger — "new governed-status
evidence" — which is not a pair.

### Why it matters

An implementation reading the second trigger literally must emit a
self-convicted finding with an empty or invented proof-package
identifier, which §7.1 says is not a member of the type. An
implementation treating it as redundant never fires it, leaving dead text
inside a section §15 calls completely enumerated. Self-conviction is
terminal and every backward edge out of it is forbidden, so the
divergence costs a permanently poisoned question in one implementation
against a live pending one in the other.

### Fix

Delete the second trigger, or re-route it to `defeated` with a stated
payload, or restate it in the contradictory-pair vocabulary the sibling
edges use.

### Note

The panel found this independently and then matched it to the docket.
Already known; recorded here so the batch is complete.

---

## T4 — Track two's ilk apparatus buys nothing at the fold

**Severity:** MEDIUM
**Spec:** §17 (`:2213-2230`, `:2262-2272`, `:2286-2292`) against §6 object
typing (`:898-908`)

### What

§6 types every committed object by schema identifier, reasoning that
"nothing here requires a bespoke parser". §17 then types GEL events by
ilk instead, with a two-track choice, a committed ilk table, and a CESR
genus reservation. But §17's own equivalence vectors require both tracks
to express one governance act with byte-identical fold results.

### Why it matters

If both tracks must fold identically, track two's only distinguishable
consumer is the governance-blind parser that track one already serves.
Two implementers can build disjoint lawful wire realizations of the same
standard, doubling the conformance surface for a distinction that
vanishes at the fold. The compact receipt form is gated on track two's
ilk seats, so track two also gates that work.

### Fix

Either exhibit a case where a conforming Gever must behave differently on
the two tracks, or collapse to one track. §17's own vector families
contain the right experiment. Outcome depends partly on T1.

---

## T5 — The comprehension gate is run in one section out of fifteen

**Severity:** MEDIUM
**Spec:** §1.7 (`:388-415`), complied with only at §17 (`:2176-2181`)

### What

§1.7 declares itself normative for the document itself and requires every
construct introduced after Chapter 1 to be stated as a named composition
of the seven primitives, in the introducing section's own prose. §17 does
this. No other section does. §1.7's own inventory omits edict, cone,
colored evidence, lens, covenant, availability charter and congruence.

### Why it matters

This is the document's own parsimony checker, and it is switched off in
fourteen of fifteen sections it governs. §6 introduces the four objects
that cross frames — exactly what a reduction argument targets — and
states no composition, so every reader reconstructs the argument, and
reconstruction is where readers diverge.

The panel argues one finding below (the lens question) would have been
caught at drafting time had §4 been made to write down what a lens is
composed of.

### Fix

Run the gate as a drafting pass: one sentence per introducing section, on
§17's model. Where a construct will not compose, apply §1.7's own
disjunction — repair Chapter 1 by succession, or remove the prescription.

Cheapest high-leverage item in the batch.

---

## T6 — Colored evidence has no user

**Severity:** MEDIUM
**Spec:** §2 (`:449-452`), §6 (`:844-846`, `:886-896`, `:898-908`)

### What

§6 says four object forms carry every crossing the document makes, and
lists colored evidence as one. The phrase appears exactly twice in 2471
lines — the §2 specifies-list and its own §6 bullet. No normative span
requires producing, consuming or verifying it. §6's object-typing clause
types the edict, the warranty and requirement elements, and types neither
colored evidence nor the cone. Its component "committed view echo"
appears once and is defined nowhere.

### Fix

Define the components and type it under §6's object-typing clause, or
remove it from §2's specifies-list and §6's four. By §1.7's gate, a
construct with no stated composition is a defect in the document's own
terms.

---

## T7 — The covenant seal's admissibility rule and verification are both undecidable

**Severity:** MEDIUM
**Spec:** §9 (`:1309-1327`), §15 carriage confession (`:2064-2072`); KERI
spec @ `71cb54e` seal count codes (`spec-body.md:405-422`), typed seal
(`:511-535`, with `:515` "The `t` field value is the versioned type of
the seal", `:522` fixing field order `[t, d]`, and the `-W`/`--W`
TypedDigestSealCouple rows at `:421-422`)

### What

Two problems in one clause. The seal is admissible "only where the
substrate's law makes lineage the invariant", but KERI's seal grammar
draws no such distinction, so the test resolves to nothing checkable
while its violation carries defect force. And verification is "neither
byte equality nor coordinate lookup" — the verifier evaluates whether a
successor satisfies the committed clause — with no clause language,
satisfaction relation, or successor relation given, so two verifiers can
lawfully differ.

Separately, §9 requires a seal to name its kind. KERI ships exactly that
facility in the typed seal, whose `t` field carries the seal's versioned
type. Custos acknowledges it without adopting it or reserving a `t`
value.

### Why it matters

This adjudicates the prior 4.0 review's KN-14: the typed-seal absorption
is nominal, not real. The covenant seal's carriage reduces to a typed
seal with a reserved `t` value and buys nothing new. Its one genuine
irreducible remainder — the verification procedure — is the part left
undesigned.

### Fix

Replace the admissibility side-condition with a decidable test or drop
its defect force; state the carriage as a typed seal with a reserved `t`
value; give the clause-satisfaction relation a committed language. Or
re-type the covenant seal honestly as a frame-local commitment whose
verification returns a finding rather than a seal verdict.

---

## T8 — The conviction-kind family doesn't cover everything the document rejects

**Severity:** MEDIUM
**Spec:** §14 (`:1973-1983`), §6 short cone (`:872-876`), §17 boundary
vectors (`:2288-2296`)

### What

§14 requires every conviction to name its kind, from a family of two:
canonical-form violation, or GARD-law violation. A conviction whose kind
can't be read "is not a conviction record". Two named rejections fall
outside both: a short cone (well-formed bytes violating no clause —
absent evidence, which the codomain types as pending), and §17's six
must-reject boundary conditions, which never say which output "reject"
is.

### Why it matters

Whoever writes §17's owed must-reject vectors has to legislate the
expected outcome, because the text doesn't determine it. Two implementers
write vectors expecting different values and both pass their own suites.

### Fix

Widen the family to cover evidence-absence and refusal explicitly, mark
those as non-convictions, reword §6's short-cone clause into the pending
vocabulary it actually describes, and annotate each §17 must-reject
vector with its expected value, defeater class and conviction kind.

---

## T9 — The compound-result product isn't closed over refusal

**Severity:** MEDIUM
**Spec:** §7.5 (`:1184-1207`), §8 composed evidence (`:1243-1267`)

### What

An evaluator's real result space is a finding or a refusal, and refusal is
explicitly not a codomain value. §7.5 mandates a product former over
components, defined only over findings. Nothing says what the product is
when one component refuses, and both readings conform: refuse the whole
invocation, discarding computed components; or return a product with a
refused coordinate, which is an object outside what §7.1 says the
evaluator returns.

### Why it matters

A compound standing question routinely contains both an unsatisfied slot
(pending) and an uncomposable one (refusal). Two implementers return
different things from the same bytes, neither in error.

### Fix

Candidate for the same ruling batch as R11 (refusal scope); either ruling
closes it.

---

## T10 — "A verifier that can evaluate a rotation can evaluate a quorum of endorsements" is half true

**Severity:** MEDIUM
**Spec:** §8 (`:1257-1267`); dossier spec (`spec-body.md:225`, `:353`,
`:358`); keripy `coring.py:4431`

### What

The threshold arithmetic does transfer — the dossier spec confirms its
operators use the same fractionally weighted threshold KERI uses for `kt`.
The slot-satisfaction predicate does not. KERI's `Tholder` decides one
question: did the signature at index `i` verify. A dossier slot counts as
endorsed only after a five-part cross-log check — a signed endorsement
ACDC with the right disposition and act, from the expected endorser,
anchored in that endorser's KEL, with a qualification proof validating
against a named schema.

### Why it matters

An implementer who reads the sentence, wires `Tholder` to an edge group
and concludes §8's composed-evidence obligation is discharged has
discharged the arithmetic and none of the slot dispositions. Unsatisfied
groups then produce pending findings whose requirement sets enumerate the
wrong slots — and requirement-set contents are exactly what the
byte-identity rule ranges over.

No m-ary or threshold edge-group operator exists in keripy today —
confirmed by grep against `upstream/main` @ `8e67f2e6a` for `MxN`,
`RMxN`, `MxQ`, `RMxQ`, `WAVG`, `NAND`, which returns nothing under
`src/keri`. The only edge-operator logic implemented is the unary set at
`src/keri/vdr/verifying.py:360` (`if op not in ['I2I', 'DI2I', 'NI2I',
'E1E']`). The dossier spec's named threshold operators are at
`dossier-spec-body.md:221`. So the claim is unexercised.

### Fix

Narrow the sentence to the algebra, or exercise slot-disposition
evaluation in a fixture before claiming the reuse.
