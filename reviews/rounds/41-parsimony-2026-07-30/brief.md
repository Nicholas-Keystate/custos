# Charge: the parsimony review of Custos 4.1

## Subject of record

The subject of this review is the full text of:

    /home/daniel/code/3GR/custos/spec/custos-4.1.md
    sha256 ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05
    2471 lines

**Read that file in full before reviewing.** This charge is an
orientation and an index, never a substitute for the spec. Where this
charge and the spec disagree, the spec governs, and the disagreement is
itself a finding. Quotes below are given with line numbers as of the
pinned sha256; re-anchor them, and every substrate citation, against
live sources per `orchestrating-reviews.md` §6.

Supporting context in the same repository, readable but not the subject:

- `custos-for-keri-practitioners.md` — a plain-language on-ramp.
- `companions/philosophy.md`, `companions/gleif-egf-mapping.md`,
  `companions/confidentiality-and-anchored-delivery.md`.
- `reviews/keri-native-review.md` — a prior substrate-fidelity review of
  the **4.0** kernel, discussed under "Prior art" below.
- `reviews/ruling-docket-2026-07-29.md` — thirteen open ruling-blocked
  findings.

## What Custos claims to be

Custos specifies a governance layer above KERI and names the class it
defines: the GARD, a Governed Autonomic Replayable Domain. Its thesis is
that KERI makes duplicity evident and then stops, on purpose — detection
without consequence — and that everything above that line (who was
entitled to issue, under which rules, and what a relying party owes when
evidence goes bad) is currently improvised and does not compose.

Its central structural move is a third log and a third fold. Keys get the
KEL and the Kever; credentials get the TEL and the Tever; law gets the
**GEL**, a governance event log, and the **Gever** that folds it. A
Constitution is not a document but what the fold returns at a position.

The standard types itself in seven primitives — five nouns (log, fold,
finding, seal, succession) and two verbs (evaluate, enact) — and binds
itself to a closure rule (§1.7, the comprehension gate, which is
"normative for this document itself"):

> Every construct this standard introduces after this chapter is
> introduced as a named composition of those seven, and the introducing
> section states the composition in its own prose. A warranty is an
> enactment binding its maker to a finding's ground. An organ is a seated
> constructor. […] Primitive closure: a section that requires an eighth
> primitive has discovered a gap in this chapter's ontology, to be
> repaired here by succession — or a prescription in that section, to be
> removed there. (`:396-409`)

That self-imposed budget is the lever this review pulls on.

## The charge — the reduction test

For **every construct Custos introduces** — GEL, Gever, fold, finding,
warranty, cone, edict, organ, tier, color / colored evidence, covenant
seal, grounded enactment, frame, consumption, federation, engine stratum —
answer four questions:

1. **Nearest substrate equivalent.** What does KERI, ACDC, CESR, or the
   dossier profile already provide that occupies this role or most nearly
   does?
2. **Does it reduce?** Can the construct be expressed as that existing
   thing plus a schema, a convention, or a profile — with no new type?
3. **What is the irreducible remainder?** If something genuinely does not
   reduce, name it precisely. A construct with a real remainder earns its
   name; one without is ontological inflation, and by the spec's own §1.7
   that is a defect in the spec's terms, not merely in yours.
4. **What does the new type cost?** In tooling, wire format, verifier
   complexity, interop surface, and implementer burden.

A construct that fully reduces and buys nothing is a finding. So is a
construct whose stated composition in the spec's own prose does not
actually hold.

### Two worked examples that seed the test

These are the reviewer's two burning questions. They are given here **with
the spec's own partial answers**, so that the review tests the spec's
argument rather than a strawman. Neither is pre-judged; both may be
resolved in the spec's favor.

**(a) Why a GEL and not a TEL?** A TEL already exists for anchoring events
that do not evolve key state. Governance events appear to fall in that
class. Does Custos need a third log type, or a third *fold* over an
existing log type?

The spec concedes the structural point outright in §1.2:

> the GEL, which commits law — constitution, amendment, seating,
> enactment. The GEL is a TEL-shaped log with governance semantics: its
> events are sealed into the anchoring KEL by the same discipline KERI's
> registry layer uses, and this standard introduces no new anchoring
> pattern. What the KEL is to keys and the TEL is to credentials, the GEL
> is to law. (`:139-146`)

§4 types it as "**GEL** (extension) — governance event log […] sealed
into the gAID's KEL by […] the same [discipline] for TELs" (`:652-656`).

What appears genuinely new is not the log but the fold. §1.5 ("The
Gever's one discontinuity") argues that the Kever's and Tever's transition
rules are protocol constants, while the Gever's transition rule is
committed data living in the log it reads, amendable by the domain it
governs, resolved positionally so that law never applies to itself.

So the strongest form of the question is: *if the GEL is TEL-shaped, uses
the TEL's anchoring discipline, and introduces no new wire pattern, does
the standard need a new log type at all — or does it need only a new fold
over a governance-schema'd registry?* Note that a search of the pinned
text finds **no passage anywhere in 4.1 that argues the GEL-vs-TEL
question directly**. Whether or not the conclusion is right, the argument
is absent. Consider also the interleaving question the spec does not
reach: would committing governance evolution and credential evolution
into one log be harmful, or beneficial, or neither?

**(b) Why a warranty and not an ACDC?** Is a warranty anything more than
an ACDC schema? The spec's §6 object-typing clause says:

> A warranty SHALL be a schema-typed, registry-bound attestation in the
> substrate's credential discipline — typed by schema identifier,
> revocable through its registry, its lens cited by edge. […] Object forms
> typed this way are consumable by the substrate's existing toolchain;
> nothing here requires a bespoke parser. (`:901-908`)

and gives its lineage as the substrate's endorsement, "refined by two
obligations: the lens is pinned, and the attested finding is recomputable"
(`:879-885`). So the spec appears to already answer *yes, it is an ACDC* —
which relocates the question to whether "warranty" earns a name in a
seven-primitive budget, or whether it is a schema plus two obligations
wearing the costume of a construct. Weigh the two obligations honestly:
are they doing real work that an ACDC schema alone could not express?

This is live, not settled: the ruling docket lists open issues #8
("warranty framing — aligning three sites to a grade the abstract already
ratifies") and #16 ("warranty dispute economics").

### Generalize past the two examples

The two above are the reviewer's questions. The panel's value is the ones
nobody asked. Apply the reduction test across the whole vocabulary, and in
particular consider:

- **The cone** against the dossier specification's existing composition
  and disclosure machinery.
- **The covenant seal** against KERI's own seal grammar — the spec claims
  three seal kinds "named beside KERI's own seal grammar" (`:1284`ff) and
  defers a fourth.
- **The organ / seating** against KERI delegation (`dip`/`drt`).
- **Colored evidence** against graduated and selective disclosure.
- **The edict** — required to be "a bare self-addressed data item, never
  an issuer-bearing credential container" (`:898-901`) — against a plain
  SAD.
- **The finding codomain** (§7) against what a verifier already computes.
- **Typed requirement sets** against ACDC schema and edge machinery.

### The mirror question

`keri-doctrine.md` exists to stop a *reviewer* importing priors KERI
rejects. Ask the mirror question of the subject: does **Custos** reintroduce
what KERI deliberately deleted? Specifically — does the GEL acquire ledger
shape; does "the Constitution" recreate an administrative root of trust;
does positional law require an ordering KERI refuses to provide across
identifiers; does any part of the federation or frame machinery
manufacture an authority above the parties? The spec claims it rejects
super-frames and root registries and that a joint multi-signature
identifier "would be simpler and is rejected on principle." Test that.

### A caution that cuts against the charge

A parsimony critique is precisely the shape most likely to be a smuggled
prior. "Just use a TEL" can itself be a category error if the TEL's
transition rule is a protocol constant and the Gever's cannot be. Steelman
each construct before reducing it, per `review-house-style.md`. Name which
objective function your criticism assumes. A finding that Custos is
"unnecessarily complex" without naming what breaks when the construct is
deleted is not a finding.

## Prior art — do not rediscover, check absorption

`reviews/keri-native-review.md` reviewed the **4.0** kernel from the
substrate-native lens and returned SOUND-WITH-FINDINGS (7 MAJOR, 6 MINOR,
2 OBSERVATION, 0 BLOCKING). Its §4 "N3 — Missed opportunities" register
already made reuse arguments of exactly this shape:

- **KN-14** the typed seal as the covenant seal's carriage
- **KN-15** delegation (`dip`/`drt`) for seating, strata, custodial recovery
- **KN-16** the spec's Endorsement/Juror/Judge vocabulary as the warranty's
  lineage
- **KN-17** IPEX for cone and dossier exchange
- **KN-18** ACDC schema machinery for committed-object typing
- **KN-19** CESR carriage posture
- **KN-20** OOBI for the one-hop resolution duty

4.1 appears to have absorbed several of these at least nominally — the
warranty's endorsement lineage and the §6 object-typing clause read as
direct responses to KN-16 and KN-18. **The question for this review is
whether the absorption is real or nominal**: did 4.1 adopt the substrate
mechanism, or adopt its vocabulary while keeping the bespoke construct?
Do not re-derive KN-14 through KN-20; adjudicate them against 4.1.

Its §2 substrate-fidelity findings (KN-01 through KN-13) concerned
misstatements of KERI's reconciliation machinery — superseding recovery,
the conviction rule, Kever/Tever as implementation rather than protocol
names. Those were against 4.0. If any survive into 4.1, that is a finding.

## What the spec already confesses

Do not spend findings on what the spec concedes. §2 (scope and non-goals)
fixes six commitments and confesses the interior they bound — evaluator
scheduling, seating procedure, constructor architecture — as undesigned.
§6 confesses that the cone "maximizes authenticity and auditability at
privacy's expense" as a committed, open trade. Agreement between
independent implementations is stated on the record as an open debt.
A confessed non-goal is not a gap. A confessed gap presented elsewhere in
the document as settled, however, is.

## Addendum — what round A already settled (2026-07-30)

A first panel (Skeptic, Spec-Precision, Relation-Algebra) has run this
same charge. **Do not re-derive these.** Check them from your own lens
only where your lens touches them, and say so if you disagree.

**Confirmed and standing** (two HIGH, seven MEDIUM):

- Under track one, no committed rule says which anchored spans constitute
  the GEL — the bootstrap commits track *placement*, never *membership*,
  so two conforming implementations derive different Constitutions from
  identical bytes. This is the round's top repair.
- The `pending → self-convicted` edge fires on "new governed-status
  evidence," which is not a contradictory pair and cannot satisfy the
  proof-package payload §7.3 requires of the state it enters. (Matches the
  repo's own ruling docket R10 / issue #6.)
- §17 types GEL events by ilk while §6 types every other committed object
  by schema identifier; and since §17's own equivalence vectors require
  both tracks to fold byte-identically, track two's ilk table and CESR
  genus reservation buy nothing at the fold boundary.
- The threshold *arithmetic* transfers from KERI's `kt` to a quorum of
  endorsements; the *slot-satisfaction predicate* does not.
- The compound-result product is not closed over refusal.
- The conviction-kind family is not total over the rejections the document
  itself names.
- The covenant seal's admissibility side-condition and verification
  procedure are both undecidable from the text; its carriage reduces to
  KERI's typed seal (`-W`) with a reserved `t` value, so KN-14 is
  nominally absorbed rather than really absorbed.
- §1.7's comprehension gate — normative for the document itself — is
  satisfied in exactly one of the fifteen sections it governs.
- Colored evidence is a crossing object with no emitter, no consumer, no
  typing clause, no stated composition, and an undefined component
  ("committed view echo", used once, defined nowhere).

**Refuted — do not repeat these mistakes.** Each was adversarially
checked and failed:

- *"The warranty pins its lens but not the replay triple."* It pins the
  triple: ground is a component of the type, and "the attested finding is
  recomputable" closes over bundle and position.
- *"The covenant seal has no irreducible remainder — it is a digest
  commitment plus a fold."* The same test dissolves KERI's own
  delegating-event and TEL source seals; a seal *is* a digest commitment
  anchoring data to an event, with evaluation always exogenous.
- *"Track two is unexercised surface."* keripy's registry schemas are
  closed (`strict=True`, fixed `alls`), so track one can express only what
  an opaque digest plus a coordinate determines; and ACDC's own spec
  authorizes minting new transaction event types.
- *"The pending species family is not total"* — species are
  requirement-kinds (what is missing), not slot dispositions.
- *"Fold inputs are opened to four at ruled-span force"* — the cited spans
  carry no BCP 14 keyword, so under §3 they bind nothing.
- *"The refusal boundary is stated at two incompatible widths"* — the
  narrow SHALL is a floor, not a ceiling.
- *"Optional delegation keeps a second seating construction lawful"* —
  event seals already supply cross-log order without delegation.

The two general traps: (1) a reduction test that would equally dissolve a
construct KERI itself ships is proving too much; (2) demanding a property
the design never claimed, where survivability rather than invulnerability
is the objective.

## Disposition

Report per `orchestrating-reviews.md`: severity as adoption-obligation,
`dedupe_key` naming the issue rather than the lens, objective function and
layer named, and the pre-ship self-check run. "Nothing in my lens" is a
valid and respected answer.
