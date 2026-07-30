# Practitioner explainer vs. Custos 4.1 — divergence audit

| Field | Value |
|---|---|
| Explainer (audited) | `custos-for-keri-practitioners.md`, 307 lines |
| Spec (authority) | `spec/custos-4.1.md`, 2471 lines |
| Spec sha256 | `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Date | 2026-07-30 |
| Method | claim inventory → per-claim adjudication against spec text; every cited line read, not estimated |

**Verdict counts** — 86 checkable claims:

| Verdict | Count |
|---|---|
| holds | 70 |
| overstated | 8 |
| understated | 3 |
| unsupported | 2 |
| contradicted | 0 |
| confessed-as-settled | 3 |

Note on the `overstated` convention used here: it covers both *the explainer
claims more than the spec* and *the explainer drops a restriction the spec
imposes*, since both make the explainer's implied commitment broader than the
spec's. Rows of the second kind are marked "(dropped restriction)".

---

## Executive summary

The explainer is a faithful projection of Custos 4.1 in the large. Its typing
chapter — seven primitives, five nouns, two verbs, the fold axioms, the
Gever's one discontinuity, the genesis knot, the four finding values with
their grounds, standing, the grounded enactment, the transformation law's four
steps — tracks the spec closely enough that most sentences are recognizable
paraphrases or verbatim lifts of spec text, and the numeric claims all check
out (seven primitives, five nouns, four values, three seal kinds, six fixed
commitments, four transformation steps). Notably, the explainer does **not**
repeat the 4.0-era framing that finding KN-01 attacked: its opening ("an
honest validator must not trust duplicitous key state — and nothing follows")
is 4.1's own corrected wording at spec:18-20 and spec:77-81, which grounds on
KERI:53's MUST NOT rather than on discretion.

The most serious divergence is at explainer:60-61 — "no new wire pattern,
nothing an existing verifier cannot parse" — which enlarges the spec's narrow
"introduces no new anchoring pattern" (spec:144) into a universal wire-format
claim that §17 flatly does not support: track two mints governance ilks an
existing verifier cannot read (spec:2222-2230), the standard's own record
enacts a CESR genus reservation the substrate's stewards have not recognized
(spec:2262-2272), and the compact receipt form is gated behind an owed
bundle-commitment rule (spec:2274-2284). A practitioner who believed that
sentence would size a Custos integration wrongly.

Second: the explainer's opening sentence about duplicity (explainer:11-12)
drops the superseding-recovery scoping the spec carries in three places — this
is finding KN-02 re-entering through the explainer after the spec repaired it.
Third: the seal paragraph presents a closed three-kind ladder and omits both
the covenant seal's admissibility restriction (a *defect* to substitute it
where a digest seal is achievable) and the deferred fourth kind with its
"commit predicates, never verdicts" doctrine — the doctrine that keeps the
whole design from collapsing into trusted oracles.

Would a practitioner reading only the explainer be misled about anything
load-bearing? Yes, on three counts: wire compatibility, the unconditional
force of key-tier duplicity conviction, and the warranty's normative container
form (spec:901-903 makes it a SHALL; the explainer implies any signed
attestation qualifies). Everything else is legitimate compression.

---

## Divergence table

`E` = explainer line(s); `S` = spec line(s).

| E | Explainer quote | S | Spec quote | Verdict | Why it matters |
|---|---|---|---|---|---|
| 60-61 | "no new wire pattern, nothing an existing verifier cannot parse" | 144; 2219-2230; 2262-2272; 2274-2284 | "introduces no new anchoring pattern"; "**Track two — governance ilks.** GEL events use ilks minted for governance semantics"; "a reservation of a governance genus is itself an enactment"; the compact form is "a committed deliverable gated" | overstated | a reader sizes integration as drop-in when track two, the genus reservation, and the compact form are all new wire surface |
| 11-12 | "a forked log convicts its author for anyone holding the pair" | 816-824 | "a pair of committed voices at one coordinate **that no committed superseding rule reconciles** convicts its author… the medium's conviction predicate is stated modulo those rules" | overstated | reintroduces KN-02: a KERI reader knows superseding recovery reconciles rather than convicts, and the unscoped claim invites the refutation the spec spent a repair to avoid |
| 222-225 | "self-convicted: the subject's own committed bytes contradict each other… This one is terminal." | 954-959 | "At the key tier, whether a pair bears is decided by the substrate's own superseding-recovery rules — a lawfully superseding event reconciles rather than convicts." | overstated | same omission at the codomain grain; an implementer would build a tier-1 self-conviction predicate that convicts lawful recoveries |
| 127-129 | "A covenant seal commits a subject to the domain's standing law, so that a successor failing the sealed clauses is convictable on the seal's own bytes." | 178-181; 1316-1319 | "admissible only where lineage, not byte identity, is the invariant; where exact bytes can be committed, the digest seal is the honest kind, and substituting the weaker for the stronger is **itself a defect**" | overstated (dropped restriction) | the three kinds read as freely choosable; substituting covenant for digest is a defect, not a design option |
| 125-126 | "Three kinds carry the standard." | 183-185; 774-777; 1329-1344 | "A fourth kind — a sealed verdict — is named and deferred"; "**Commit predicates, never verdicts.** A sealed verdict a stranger cannot recompute is smuggled authority" | confessed-as-settled | the ladder reads closed where the spec publishes an open frontier item *and* the anti-oracle doctrine that governs it — the doctrine most load-bearing against sealed-verdict drift |
| 283-284 | "a signed attestation that a finding was computed under a pinned lens" | 898-904 | "A warranty **SHALL** be a schema-typed, registry-bound attestation in the substrate's credential discipline — typed by schema identifier, revocable through its registry, its lens cited by edge" | overstated (dropped restriction) | a builder would ship a bare CESR-signed blob and be non-conforming; revocability and schema typing are normative, not incidental |
| 288-289 | "Judgment stays cheap to verify because it is expensive to fake." | 37-43; 1693-1699; 1718-1724 | "That economy is the design's claim, stated at the design's grade: its deployment-scale record… is a committed, unfinished deliverable… and no clause below presumes it discharged"; "this document does not assert it" | confessed-as-settled | the spec's most carefully graded claim is repeated without its grade; the explainer's own "what it refuses to claim" section never restores it |
| 197-199 | "That is what autonomic means here: the domain detects, judges, acts, and files the act… with no external enforcer anywhere in the loop." | 600-602; 1774-1777 | "'Autonomic': its identity is self-certifying, rooted in key state, borrowing no external authority"; "**Within its perimeter**, an autonomic frame detects, judges, acts…" | overstated | promotes one facet to the definition and drops the perimeter scope; §13.2:1857,1869-1870 make prevention available only within the frame |
| 106-108 | "A section that needs an eighth primitive has found a gap in the ontology, repairable **only** by amending the typing chapter through succession." | 405-412 | "to be repaired here by succession — **or a prescription in that section, to be removed there**"; the gate tests **two** closures, primitive and law | overstated | the gate has two dispositions and two closures; "only" makes the ontology look more brittle than the spec's own rule |
| 52-54 | "KERI already solved this shape twice. Keys get a log, the KEL, and a fold, the Kever." | 665-675 | "The specifications name the logs; **the reference implementation names the folds** after the logs they fold, and this standard adopts that naming convention" | overstated (attribution) | KN-03's naming-custody slip in miniature: attributing Kever/Tever to KERI-the-specification is exactly the over-attribution 4.1 repaired |
| 96-97 | "GLEIF's root identifier is adopted grade, exactly." | — | (spec names no real-world entity anywhere; grep for GLEIF/ICAO/vLEI returns nothing) | unsupported | applies the spec's taxonomy to a named third party as settled fact; the spec classifies no deployed identifier |
| 28-34 | "ICAO governs passports; GLEIF's vLEI framework governs qualified issuers…" | — | (no counterpart) | unsupported | imported motivational apparatus; harmless as framing, but it is not spec content and should not be read back as such |
| 36-42 | blockchains "supply the two things prose lacks — a total order… and a completeness surface… The price is sovereignty" | 486-490; 2092-2100 | "no clause of this document presumes an observer who sees everything"; "Completeness of view is never a committed property of any enumerable party. …The total view is a join no single party holds" | confessed-as-settled | by rhetorical implication Custos pays only the sovereignty price; the spec confesses a second one — it never claims completeness of view |

### Understated (noted for completeness, not corrections)

| E | What is thinner than the spec | S |
|---|---|---|
| 293-296 | The open frontier is given as three items ("evaluator scheduling, seating procedure, constructor architecture"). §15 lists eight open interior items plus **three explicitly unresolved questions**; §13.4 adds recourse procedure, rehabilitation, reliance protection, and deployed effectiveness. | 2064-2075; 2077-2090; 1894-1909 |
| 218-221 | Pending is given without its four discharge species (absent, window-open, unresolved-conflict, expired/abandoned) and without the SHALL that a pending finding carry each element's species. | 974-1012, esp. 1007 |
| 124-131 | The seal paragraph omits the two disciplines binding all three kinds: a seal names its kind (consumers MUST NOT infer semantics from context), and a conviction sourced from a seal names the kind it convicted under. | 182-183; 1321-1327 |

---

## Serious divergences

### D-1 · "No new wire pattern" (explainer:59-61)

**Explainer, 59-61:**

> GEL events seal into the domain's KEL by the same anchoring discipline TELs
> already use — no new wire pattern, nothing an existing verifier cannot
> parse.

**Spec, 141-145 (§1.2):**

> The GEL is a TEL-shaped log with governance semantics: its events are sealed
> into the anchoring KEL by the same discipline KERI's registry layer uses,
> and this standard introduces no new *anchoring* pattern.

The spec's commitment is scoped to *anchoring*. Three places in §17 make the
wider claim false:

**Spec, 2216-2230 (§17, the two tracks):**

> **Track one — registry-form reuse.** … This track is the colorless base: any
> registry-capable consumer parses the events unharmed…
> **Track two — governance ilks.** GEL events use ilks minted for governance
> semantics. … A consumer encountering an unrecognized governance ilk holds
> committed evidence of exactly that.

**Spec, 2262-2272 (§17, genus):**

> The encoding substrate's genus namespace admits reservation, and a
> reservation of a governance genus is itself an enactment… Recognition of the
> reservation by the substrate's stewards is a distinct, later, bilateral
> event… enacted, unrecognized, and honest about the difference.

**Spec, 2274-2284 (§17, the compact form gate):**

> A compact, count-code-framed receipt form — the wire shape by which a
> warrantor's backing travels per-receipt — is a committed deliverable gated,
> in order, on: the bundle-commitment rule (… owed because the substrate's
> receipt form does not make its identifier field self-addressing)…

Also relevant: spec:2193-2198 requires every GEL event to carry a
self-addressing identifier *in its own field*, which the substrate's receipt
form does not do (spec:2278-2280).

**Proposed minimal correction (not applied):** replace the em-dash clause with
the spec's own scope, and name track one as the condition under which the
parse claim holds. E.g.:

> GEL events seal into the domain's KEL by the same anchoring discipline TELs
> already use — no new anchoring pattern. A domain may go further and keep its
> GEL in registry event forms, the colorless base any registry-capable
> consumer parses unharmed; or it may mint governance ilks, which existing
> verifiers read as committed evidence they do not recognize. Which track a
> domain speaks is committed law, not convention.

### D-2 · Duplicity conviction stated unconditionally (explainer:11-12, 222-225)

**Explainer, 10-12:**

> A KEL folds identically for every honest validator, and a forked log
> convicts its author for anyone holding the pair.

**Spec, 814-824 (§5):**

> A KEL folds to the same key state everywhere; a SAID resolves to the same
> bytes or convicts the presenter; and a pair of committed voices at one
> coordinate **that no committed superseding rule reconciles** convicts its
> author for every verifier holding the pair, under no frame's law. The
> scoping is the substrate's own: its superseding-recovery rules lawfully
> admit a second event at a coordinate as reconciliation — a rotation
> recovering a compromised log is repair, cited, not duplicity — and the
> medium's conviction predicate is stated modulo those rules…

Repeated at the codomain grain, **spec:954-959:**

> **self-convicted(proof)** … At the key tier, whether a pair bears is decided
> by the substrate's own superseding-recovery rules — a lawfully superseding
> event reconciles rather than convicts.

and at the recourse ladder, **spec:1871-1877**: "modulo the substrate's
superseding reconciliation, per the medium section."

This is exactly the KN-02 finding (`reviews/keri-native-review.md`:72-101),
which the 4.1 text repaired in all three places. The explainer's first
paragraph re-opens it. Note that the explainer's *adjacent* framing —
"an honest validator must not trust duplicitous key state — and nothing
follows" (explainer:12-14) — is 4.1's own corrected wording (spec:18-20,
77-81) and is **not** a KN-01 repeat; the problem is the sentence before it,
not the one KN-01 named.

**Proposed minimal correction (not applied):** one clause, at explainer:11.

> …and a forked log its author cannot reconcile under the substrate's own
> superseding rules convicts him for anyone holding the pair.

and, at explainer:223, append to the self-convicted bullet: "At the key tier,
whether a pair bears is the substrate's superseding-recovery rules to decide —
a lawful recovery reconciles rather than convicts."

### D-3 · The seal ladder reads closed and unrestricted (explainer:124-131)

**Explainer, 124-131:**

> A **seal** is a commitment planted in a log… Three kinds carry the standard.
> A digest seal commits to exact bytes. An event seal commits to the event at
> a log coordinate. A covenant seal commits a subject to the domain's standing
> law, so that a successor failing the sealed clauses is convictable on the
> seal's own bytes.

**Spec, 172-185 (§1.2)** — the same three kinds, plus two things the explainer
drops:

> The covenant seal is admissible **only** where lineage, not byte identity, is
> the invariant; where exact bytes can be committed, the digest seal is the
> honest kind, and substituting the weaker for the stronger is itself a
> defect. A seal names its kind, and a conviction sourced from a seal names
> the kind it relied on. A fourth kind — a sealed verdict — is named and
> deferred; its admissibility doctrine travels with the seal chapter.

**Spec, 1329-1344 (§9)** carries the deferred kind's doctrine at full weight:

> **Evaluation seal — named and deferred.** … a sealed verdict raises the
> oracle problem in seal form: the seal is only as good as its evaluator, and
> a consumer who trusts the seal has trusted the evaluator it cannot see. …
> An evaluation seal is admissible only over verifiable algorithms… Commit
> predicates, never verdicts. A sealed verdict a stranger cannot recompute is
> smuggled authority, and no construct of this document consumes one.

§2:465 lists what the document specifies as "the three commitment kinds this
standard's anchors use, **and the admissibility rule for a deferred fourth**"
— so the fourth is specified content, not a footnote. In a document whose
thesis is "law you can replay," the sentence that forbids sealing verdicts is
arguably the single doctrine most worth carrying to a practitioner audience:
it is the rule that keeps a Custos deployment from degenerating into signed
oracle output.

**Proposed minimal correction (not applied):** two sentences appended to the
seal paragraph.

> The covenant seal is the weaker instrument and is admissible only where
> lineage, not byte identity, is the invariant; where exact bytes can be
> committed, using it instead of a digest seal is itself a defect. A fourth
> kind is constructible and deliberately refused: a seal over a verdict.
> Commit predicates, never verdicts — a sealed verdict a stranger cannot
> recompute is smuggled authority, and no construct of Custos consumes one.

### D-4 · The warranty's normative container form is dropped (explainer:283-284)

**Explainer, 283-285:**

> Warranties amortize it: a signed attestation that a finding was computed
> under a pinned lens. A warranty is evidence about a judgment, never the
> judgment…

**Spec, 898-904 (§6, Object typing):**

> A warranty **SHALL** be a schema-typed, registry-bound attestation in the
> substrate's credential discipline — typed by schema identifier, revocable
> through its registry, its lens cited by edge. … Object forms typed this way
> are consumable by the substrate's existing toolchain; nothing here requires
> a bespoke parser.

On the brief's question — is the explainer's "a warranty is an enactment
binding its maker to a finding's ground" (explainer:103-104) consistent with
§6's SHALL as stated to a practitioner? The *sentence* is fine: it is
spec:399 verbatim, from the comprehension gate, which is a composition claim
(warranty = enact + finding-ground), not a wire-form claim. The two are
consistent — one types the object in primitives, the other types its carriage.
The gap is that the explainer never carries the carriage type anywhere, so a
practitioner is left with "signed attestation + pinned lens" as the whole
specification of a warranty. That is under-specified in exactly the direction
that produces non-conforming implementations: no schema identifier, no
registry, no revocability, no edge-cited lens.

**Proposed minimal correction (not applied):** extend explainer:283-284.

> Warranties amortize it: an ACDC-discipline attestation of a computed
> finding — schema-typed, registry-bound so it can be revoked, its lens cited
> by edge. A warranty is evidence about a judgment, never the judgment…

### D-5 · The economics claim without its grade (explainer:288-289)

**Explainer, 286-289:**

> …one honest verifier recomputing from committed bytes convicts the warrantor
> on its own signature. Judgment stays cheap to verify because it is expensive
> to fake.

**Spec, 33-43 (Abstract)** — the same sentence, immediately graded:

> Judgment stays cheap to verify precisely because it is expensive to fake.
> **That economy is the design's claim, stated at the design's grade: its
> deployment-scale record — an open replaying population exercising the
> credible threat — is a committed, unfinished deliverable of this standard's
> record, and no clause below presumes it discharged.**

**Spec, 1693-1699 (§12.3):**

> A false warranty is therefore always falsifiable in principle; whether the
> open replaying population effectively disciplines deployed warranted supply
> — access, publication, standing, and consequence operating as a system — is
> a pending claim of this standard's record, held to its fixture conditions,
> and **this document does not assert it**.

The explainer's "what it refuses to claim" section (explainer:291-299)
confesses the fixture scale and the cross-implementation debt but never
returns to the economics. So the one place the spec is most insistent about
grading its own claim is the one place the explainer states it flat.

**Proposed minimal correction (not applied):** one clause at explainer:289, or
one sentence added to the closing section.

> Judgment stays cheap to verify because it is expensive to fake — the
> design's claim, at the design's grade: whether an open replaying population
> actually exercises the threat is an unfinished deliverable, and Custos does
> not assert it.

---

## Claims that hold

Explainer line → spec line. 70 entries.

| E | Claim | S |
|---|---|---|
| 10-11 | a KEL folds identically for every honest validator | 814 |
| 12-14 | KERI stops; honest validator must not trust duplicitous key state; detection, no consequence | 17-20, 77-81 |
| 16-21 | consumers improvise above the line; improvisation does not compose | 20-22 |
| 23-25 | Custos specifies the layer above; GARD named; KERI detects, a GARD adjudicates | 17, 81, 596-599 |
| 44-49 | integrity self-certifying, authority not; registry evidence ≠ authority | 1217-1229 |
| 54-57 | fold = walk committed events and accumulate implied state | 148-153 |
| 57-59 | Custos adds the third rung: the GEL and the Gever | 654-663, 676-681 |
| 59-60 | GEL events seal into the KEL by the discipline TELs use | 141-145, 654-658 |
| 62-63 | what the KEL is to keys and the TEL to credentials, the GEL is to law | 144-146 |
| 65-67 | a Constitution is not a document; a ratified text is an event in the GEL | 682-688 |
| 67-69 | identical committed inputs → identical law by computation | 688-693 |
| 73-76 | Kever/Tever transition rules are constants of the protocol | 300-303 |
| 76-78 | the Gever is the first fold whose transition rule is committed data | 303-306 |
| 80-85 | not circular but positional; succession never retroactive | 1516-1519, 2124-2126 |
| 87-91 | founding law computed first, SAID sealed at inception, prefix = identifier | 610-620 |
| 91-94 | law must not mention the identifier; reserved sentinel; exclusion closes the cycle | 614-616, 622-626 |
| 94-96 | incept bare and anchor later = adopted grade, lawful and weaker | 626-632 |
| 101-103 | seven primitives; every later construct is a composition of them | 392-400 |
| 103-104 | a warranty is an enactment binding its maker to a finding's ground | 399 |
| 104 | an organ is a seated constructor | 400 |
| 104-105 | federation is a relation between domains built from seals and enactments | 401-402 |
| 108 | the seven are a budget, not a glossary (primitive closure) | 405-410 |
| 110 | five are nouns | 130-132 |
| 112-113 | log = committed evidence, anchored so KERI proves integrity and authorship | 136-138 |
| 114 | a log asserts nothing; preserving is its entire office | 146 |
| 114-115 | a domain reads three: KEL, TEL, GEL | 138-141 |
| 117-118 | fold = pure function from committed bytes to implied state | 148-150 |
| 119 | log and fold are one structure read twice; no fold ever writes | 154-156, 274-275 |
| 121-122 | a finding is what a fold returns, carrying its ground | 158-165 |
| 124-125 | a seal is a commitment planted in a log binding one record to another | 170-172 |
| 126-127 | digest seal commits to exact bytes; event seal to an event at a coordinate | 172-175, 1299-1307 |
| 129-131 | seals hang the GEL off the KEL and put founding law inside the identifier | 654-658, 616-620 |
| 133-135 | succession = law changing by enactment inside the log the fold reads | 187-201 |
| 137 | two verbs, and no object performs both | 205-206 |
| 139-141 | evaluate: read bytes, compute state, return findings, refuse where no rule makes it evaluable | 208-215 |
| 141-142 | an evaluator holds no pen, and no conviction earns it one | 216-217 |
| 144-147 | enact: ratify, seat, issue, commit; every enactment is a committed event | 219-224 |
| 149-152 | KERI's controller/validator division carried up one tier | 226-229 |
| 155-158 | evaluate(evidence_bundle, law_head, position); no clock, config, network, discretion | 1033-1038 |
| 160-162 | enact produces a committed event and judges nothing | 219-224 |
| 165 | two evaluations of the same triple return byte-identical findings | 1038 |
| 173-175 | genesis: one key state, one page of law, one log binding them | 92-98 |
| 176-178 | seating: an establishment act citing the clause that creates the role | 760-764 |
| 179-180 | issuance: registry state moves in a TEL, anchored to key state | 649-651, 1493-1494 |
| 181-184 | a stranger holding nothing but the logs asks the question | 100-104 |
| 184-186 | the Gever folds the GEL in the context of the KEL/TEL spans it cites | 149-153, 676-681 |
| 187-190 | consequence grounded on a terminal adverse finding; act commits its ground | 1802-1810, 1834-1836 |
| 191-194 | amendment is an ordinary GEL event, judged under the law in force before it | 1512-1519, 122-128 |
| 196-197 | steps 5 and 6 land in the GEL, the log step 4 reads | 654-656, 1909-1911 |
| 201-206 | four answers; ground is a component of the value, not an annotation; no bare verdicts | 930-941, 158-165 |
| 207-209 | affirmed: evidence discharges the clause; ground = bundle + clause set | 943-945 |
| 210-214 | defeated: citation of defeating clause or superseding act, plus defeat class (crypto, authority, merit, superseded) | 946-948, 1129-1136 |
| 214-217 | lexicographic minimum where several defeats are available; same defeat down to the byte | 1123-1128 |
| 218-221 | pending: typed requirement set naming what would settle it; a cure path | 949-953, 1048-1051 |
| 223-225 | self-convicted is terminal; the question is poisoned; no later evidence rehabilitates | 1084-1089 |
| 227-231 | the ground requirement is the load-bearing decision; judgment composes across parties sharing evidence | 934-939 |
| 233-236 | a fifth outcome is not a value; a missing rule, not missing evidence; refusal is an operational fact | 114-120, 1197-1201 |
| 236-238 | an evaluator that invents an ordering has legislated; a legislating evaluator is a constructor wearing the wrong name | 1201-1204 |
| 240-242 | transitions run only toward evidence growth; no backward edge; new finding at a new position | 1068-1082 |
| 246-249 | registry state is evidence, standing is judgment, the covenant set is the function | 1217-1224 |
| 249-252 | a relying party reading authority off the registry has trusted the ledger | 1224-1229 |
| 254-258 | a grounded enactment commits bundle, law head, position, and the terminal finding it claims | 1798-1810 |
| 258-261 | checked twice: the ground replays and the enactor held the power; failure is defeat on its own bytes | 1812-1822 |
| 266-267 | judgment never crosses a frame boundary; evidence does | 1547-1552 |
| 268-272 | four steps; authenticate and resolve invariant, appraise and confer frame-local | 1637-1665 |
| 272 | the same act is lawfully judged differently by every frame, at the same time | 1665-1667 |
| 274-275 | no super-frame and no root registry | 833-836, 1600-1605 |
| 275-276 | domains compose as local charts compose an atlas | 507-512 |
| 276-278 | consumption is unilateral; B commits the recognition; A need not know | 1563-1573 |
| 278-279 | federation is bilateral: two anchors, one shared rule object, unilateral exit | 1575-1587 |
| 279-281 | a joint multi-signature identifier is rejected: it manufactures an authority above both parties | 1589-1598 |
| 283 | warranties amortize replay | 33-36, 1684-1688 |
| 285-288 | a warranty is evidence about a judgment, never the judgment; replay-falsifiable; convicts on its own signature | 1688-1693, 1738-1741 |
| 293-295 | six commitments are fixed | 2052-2062 |
| 295-296 | the interior they bound is confessed undesigned | 2064-2073 |
| 296-299 | one implementation, one pinned checkout; independent implementations an open debt on the record | 491-495, 1952-1957, 2138-2146 |
| 301-303 | the repository is a projection, never an authority; which bytes are law is computed from the GEL | 2163-2165 (and `README.md`:59-63) |

---

## Notes on the brief's named pressure points

1. **KN-01 / "detection, no consequence."** The explainer does *not* repeat the
   framing KN-01 attacked. 4.0 said the protocol "remains silent about
   recourse" and left the validator's response discretionary; 4.1 says "an
   honest validator must not trust duplicitous key state — and nothing
   follows" (spec:18-20, 77-81), which is KERI:53's own MUST NOT, and the
   explainer copies the corrected form. The residual tension — §13:1769-1770
   concedes "the substrate commits detection **and its own key-layer
   recovery**, and is silent above them" — lives in the spec, not in the
   explainer. The genuine regression is KN-02, at explainer:11-12 (see D-2).
2. **Warranty = enactment binding its maker to a finding's ground, vs §6's
   SHALL.** Consistent; different layers (composition vs. carriage). The
   defect is omission, not contradiction — see D-4.
3. **"No new wire pattern."** Not supported; see D-1.
4. **Numeric claims.** All verified: seven primitives (spec:392), five nouns
   (spec:130-132), two verbs (spec:203-206), four finding values (spec:941),
   three seal kinds (spec:171-172, with a fourth deferred at 183-185), six
   fixed commitments (spec:2052-2061, enumerated and counted), four
   transformation steps (spec:1637-1661). The only enumerative problem is the
   silent drop of the deferred fourth seal kind — see D-3.
5. **"A projection, never an authority."** Holds, and the attribution to "the
   repository" is right: `README.md`:59-63 says it in those words, quoting
   spec:2163-2165.
