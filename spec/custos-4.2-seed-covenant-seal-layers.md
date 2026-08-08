# Custos 4.2 seed — the covenant seal in three layers

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges finding #39 only. Executed under ruling R17 of the
> ruling record supplement 2 of 2026-08-01 (sha256 7c5f6491976bd5
> fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670). Offered to
> the drafting authority, which owns the wording.
>
> A portable clause language — sealing against another domain's
> law — is **expressly not designed here**. R17 routes it to the
> encoding round's charter inputs (#57), and a seed that drafted
> it would be legislating a decision surface the charter owns.

---

## What this seed carries

One split, and everything else follows from it.

"Verification" of a covenant seal was three questions at three
different epistemic grades, asked in one word. The section's
defect was stating a governance-tier computation in medium-tier
vocabulary — which is why its admissibility side-condition
resolved to nothing checkable, and why two frames holding the
same seal and the same candidate successor could lawfully reach
opposite verdicts inside a section asserting that two disciplines
bind all three kinds.

R17 splits the word. Carriage and attachment are medium physics
and tier-uniform. Satisfaction is a fold.

## Repair — the split

**Ratified spans.** Cited, not edited. The covenant seal
(L1309–1319):

> **Covenant seal** (extension). A commitment binding a subject
> to the GARD's covenant set — to standing law, not to another
> object. Verification is neither byte equality nor coordinate
> lookup: the verifier evaluates whether the successor satisfies
> the committed clause. … The covenant seal is admissible only
> where the substrate's law makes lineage the invariant; where
> byte equality is achievable, the digest seal is the honest
> kind, and substituting the weaker kind is itself a defect.

The same admissibility condition appears in the typing chapter
(L178–181). The substrate's seal grammar, acknowledged and not
adopted (L1288–1293):

> The substrate's seal grammar ships more kinds than this section
> names — digest seals, Merkle-root seals, event and source
> couples, a latest-establishment seal, a generic typed seal —
> and this standard's first two categories subsume the
> byte-shaped and coordinate-shaped members of that table, cited,
> never renamed.

The naming discipline (L1321–1327), which requires a seal to name
its kind and a conviction to name the kind it convicts under. And
the medium's claim the split has to survive (L809–814):

> the three things every verifier in every frame computes
> identically from the same committed inputs under the
> substrate's pinned semantics, because their agreement is
> cryptographic rather than negotiated.

**The defect.** The admissibility side-condition is uncheckable:
the substrate's seal grammar draws no distinction between a
"lineage invariant" and a "byte-identity invariant" as substrate
law, so the test resolves to nothing while its violation carries
defect force — a rule found by nobody and assertable by anybody.
And the verification procedure is unstated: no clause language,
no satisfaction relation, no successor relation.

## Layer 1 — carriage (medium physics, tier-uniform)

> **Carriage.** The covenant seal is carried as the substrate's
> typed seal with a reserved type value, and its seal data is the
> self-addressing identifier of the sealed clause set. No
> substrate extension is claimed and none is required.
>
> **Admissibility.** A covenant seal is inadmissible over content
> whose exact bytes can be committed. Where byte equality is
> achievable the digest seal is mandatory, and a covenant seal
> over digest-sealable content is the defect.

Two things happen here, and the second is the repair.

The carriage makes real an absorption that was nominal. The prior
substrate review's KN-14 raised the typed seal as the covenant
seal's carriage; section 9 acknowledges the typed seal without
adopting it or reserving a value, so the absorption existed in
prose and not in bytes. Reserving the value is cheap under any
branch of R17 and buys the naming discipline its mechanism: a
seal that names its kind in a field a governance-blind consumer
can read.

The admissibility condition is **replaced by section 9's own
decidable test**, which was sitting in the next clause the whole
time. "Where byte equality is achievable, the digest seal is the
honest kind" is checkable — a verifier asks whether the sealed
content has determinate bytes at seal time — where "the
substrate's law makes lineage the invariant" is not. The defect
force stays and acquires a subject: the defect is *substituting a
covenant seal for an available digest seal*, which is what the
original clause was reaching for and could not say.

## Layer 2 — attachment (medium physics, tier-uniform)

> **Attachment.** Whether a seal is attached to a subject is
> decided by coordinate lookup and lineage walk over the
> committed log — the event-seal machinery, reused unchanged.

Nothing is designed here; the layer exists to be named, because
it was the half of "verification" that really is coordinate work
and was being carried by the same word as the half that is not.

Layers 1 and 2 are **log-kind-uniform**: they hold identically
over a KEL, a TEL and a GEL, and neither consults governance
semantics. That uniformity is what keeps a covenant seal
checkable *as a seal* by a consumer that knows nothing of GARDs —
the same property section 17's track one calls the colorless base
and section 12.3 states for evidence generally.

## Layer 3 — satisfaction (governance tier)

> **Satisfaction.** Whether a successor satisfies the sealed
> clause set **is a fold**: a standing question under the sealed
> set, appraised at a position, returning a finding of the
> four-valued codomain with its ground. It is warrantable and
> contestable like any other finding; it is position-indexed; and
> it inherits the full machinery — bearing, succession under
> re-discharge, the designated law head, and full discharge of
> the question's committed requirement space.
>
> A covenant seal together with a `defeated` satisfaction-finding
> is a breach with a committed anchor.

This is the answer the section could not give because it was
looking for a verdict rather than for a fold. "Does the successor
satisfy the sealed clauses" has exactly the shape every other
governance question has: committed evidence, committed law head,
a position, and a ground-carrying value. Two frames reaching
opposite verdicts is no longer lawful for the reason it is not
lawful anywhere else — they would be folding different triples,
and the divergence convicts one of them.

Everything the satisfaction fold inherits, it inherits by being
a fold, not by a clause enumerating inheritances:

- **Bearing** (R13) decides whether a contradictory pair reaches
  the satisfaction question at all.
- **Succession under re-discharge** (R14) is what happens when
  committed growth falsifies a ground the satisfaction-finding
  cited — the seal does not re-verify, the question is appraised
  afresh at a new position.
- **The designated law head** (R15) is what makes "the sealed
  clause set" derivable rather than asserted, since the clauses
  are SAIDs into a GEL and which registry is the GEL is now
  committed.
- **Full discharge** (R2) is why a satisfaction-finding cannot be
  `affirmed` while any enumerated check on the sealed set sits
  unexamined.

## Section 5's claim, correctly scoped

The medium says agreement is "cryptographic rather than
negotiated", and finding #39 is right that the ratified covenant
seal contradicts it: a verification that two frames can lawfully
decide differently is negotiated by any honest reading.

The split repairs the contradiction without weakening the medium.

> Layers 1 and 2 are cryptographic — byte and coordinate work,
> identical for every verifier. Layer 3 is computed and
> replayable: not byte equality, and not negotiation either. The
> third grade between them is what a fold is.

That third grade is the standard's whole thesis stated at the
seal ladder. Judgment that is neither a byte comparison nor a
matter of opinion, because it is a pure function of committed
inputs, is what the document exists to specify — so the covenant
seal's satisfaction layer is not an embarrassing exception to
section 5. It is section 5's own sentence read at the tier where
folds live.

## What the seal irreducibly does

> A covenant seal names the clause set a successor is answerable
> to, forward, at a committed coordinate.

That is the irreducible content, and it is worth stating in the
text because the three-layer split can otherwise read as
dissolving the construct into machinery that already existed. It
does not. A digest seal commits bytes; an event seal commits a
coordinate; neither can commit a *subject* to *standing law* such
that the commitment survives the law's own amendment. The promise
survives amendment because what was sealed is the clause set at
its coordinate, and the fold that appraises satisfaction runs
under the law head the question names.

The seal carries the question; the fold supplies the answer.

## Clause language, and what is not designed here

> The sealed set is a set of clause self-addressing identifiers
> into the domain's designated governance event log, and
> satisfaction semantics are the existing discharge semantics of
> section 7.3. No new language is introduced.

In-domain sealing needs nothing more than this: the clauses are
already SAID-addressed, the discharge machinery already exists,
and the fold already knows how to appraise a requirement space.

A **portable** clause language — sealing against another domain's
law — is a different question and a real design surface, because
a clause citation that travels must survive leaving the log that
minted it. R17 routes it to the encoding round's charter inputs
(#57), where it is already listed as the fourth input. This seed
neither designs it nor presumes its outcome; the in-domain form
above stands whichever way the round goes.

## Notes for the drafting authority

Things surfaced in drafting that R17 did not name.

1. **The admissibility condition appears twice and must move
   twice.** Chapter 1's seal noun carries it at L178–181 and
   section 9 carries it at L1316–1319. Chapter 1's version is the
   one that reaches a reader first, and it is also the one inside
   the typing chapter, which section 2 says is owned there and
   redrawn nowhere (L431–435). If only section 9's copy is
   repaired, the document states an uncheckable admissibility
   test in the chapter that types the primitives and a decidable
   one in the chapter that details them.

2. **Section 16's succession story now runs through a fold, and
   that is a stronger claim than it looks.** L2165–2169 says
   "The seal a successor plants is checkable against this
   document's covenant set — that is what the covenant seal is
   for — and a successor that cannot satisfy the committed
   succession clauses is convictable on its own enactment bytes."
   Under the split, "checkable" at layer 3 means a fold over this
   document's own succession clauses, which makes the standard's
   self-application concrete: the covenant set is the sealed
   clause set, and the satisfaction fold is an ordinary
   governance question about the standard itself. Worth stating
   at the site, because a reader who takes "checkable" as
   medium-grade will expect a verdict the layer cannot give.

3. **A reserved type value is a substrate-facing act, and the
   document has a discipline for those.** Section 17's genus
   paragraph rules that reserving coordinates in the encoding
   substrate's namespace is itself an enactment, committed in the
   GEL of the domain that reserves it, and that recognition by
   the substrate's stewards is a distinct, later, bilateral event
   (L2262–2272). The same shape applies to a reserved seal type
   value, and section 14's travel posture (L2034–2041) forbids
   this document travelling as an extension proposal against a
   substrate corpus before an authoritative answer from that
   corpus's custodians. The seed therefore says "a reserved type
   value" and does not name one.

4. **The four-valued codomain over a satisfaction question needs
   its `pending` story told once.** A successor that has not yet
   done what the sealed clauses require is not in breach — the
   satisfaction-finding is `pending` with the unmet clause as its
   typed requirement, and the seal's forward promise is exactly
   the state in which that pending is the correct answer for a
   long time. A drafting pass that only exhibits the `defeated`
   case invites the reading that a covenant seal is a breach
   detector, which is half of what it is.

5. **Station obligations: three vectors, routed to #15.**
   Satisfaction-as-fold — a sealed clause set, a candidate
   successor, and a four-valued finding with its ground.
   Digest-precedence defect — a covenant seal over content whose
   exact bytes were committable, expected must-reject. And breach
   composition — a seal plus a `defeated` satisfaction-finding
   yielding a breach with a committed anchor. They belong in #15.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Executed under | Ruling record supplement 2, 2026-08-01, sha256 `7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670` — R17 |
| Finding discharged | #39 (an uncheckable admissibility condition and an unstated verification procedure) |
| Adjudicates | KN-14 — the typed-seal absorption becomes real rather than nominal |
| Depends on | R2, R13, R14, R15 — the satisfaction fold inherits them by being a fold |
| Charter input, not designed here | portable clause language → #57 |
| Re-ruling | No — §9 is not a §15 fixed wall; §5's claim is scoped rather than reworded |
| Station obligations, elsewhere | satisfaction-as-fold; digest-precedence defect; breach composition → #15 |
| Ratified bytes altered | None |
