# Spec-Precision & Language Designer (SPC) Review: Custos 4.1 — the parsimony round

**Date:** 2026-07-30
**Target(s):** `/home/daniel/code/3GR/custos/spec/custos-4.1.md` (sha256 `ff8b9e7a…b72b05`, 2471 lines — preflight verified against the pin); cross-referenced against `kswg-keri-specification`, `kswg-acdc-specification`, `kswg-cesr-specification`, `kswg-dossier-specification`, `keripy`
**Effort:** deep  **Objective lens:** survivability
**Sources used:** `keri-doctrine.md`, `review-house-style.md`, `orchestrating-reviews.md`, bible `01`/`04`/`07`, plus live re-anchored substrate sources (every line number below was re-grepped today; none is copied from the doctrine)

---

## Executive summary

Custos 4.1 is a serious specification with an unusually honest frontier, and its central move — make governance judgment a pure function of committed bytes so a stranger recomputes rather than trusts — is KERI's own move applied one tier up. My lens does not fault that move. It faults the fact that the document's **class-defining obligation** ("a conforming domain MUST make every judgment it issues recomputable, byte-identically", `:423-426`) is contradicted, at ruled-span force, by the document's own supporting vocabulary — and that several of its most load-bearing predicates are not decidable from the spec text alone.

The single biggest finding is **F1**: axiom 2 and §7.3 close the fold's inputs to exactly three and explicitly exclude "ambient configuration" (`:245-247`, `:1033-1038`), while the `lens` definition (`:752-755`), the color-comparison clause (`:378`), and §12.2 step 3's SHALL (`:1650-1652`) each make a **pinned engine profile** an input a finding "was computed under". Two ruled spans cannot both be satisfied. On the reduction test this is also the answer to the charge's question (b): the warranty *does* reduce to an ACDC — §6's own SHALL says so — and of its two claimed remainders, "recomputable" is axiom 2 restated and "the lens is pinned" is the one that does not reduce *and* is the one that breaks replay. The remainder that earns the warranty its name is the same clause that costs the standard its headline property.

Close behind, **F2** is the parsimony charge's question (a) answered from my side of the table: the GEL does not reduce cleanly to "a TEL plus a schema" — not because the spec argues it cannot, but because the spec never says how a verifier tells GEL spans from TEL spans under its own track one. That is not a reason to keep the type; it is a hole where the reduction argument should be.

"Nothing in my lens" would have been a dishonest report here. Eight findings follow, five HIGH.

---

## Steelman

The strongest reading of Custos 4.1, in KERI's terms:

KERI relocated the root of trust from an administrator to a replayable log, and then stopped at a deliberately drawn line — an honest validator must not trust duplicitous key state, and nothing follows. Everything above that line (who was entitled to issue, under what rules, what a relying party owes when evidence goes bad) is today improvised, and improvisation does not compose. Custos proposes to apply KERI's *own* method to that layer: take a thing currently asserted by an administrator and make it a pure function of committed bytes, so that judgment becomes checkable rather than testimonial. That is the correct method, and the document is disciplined about it in ways that matter to my lens specifically:

- It **adds no anchoring pattern** and says so (`:139-146`, `:652-658`). The GEL is TEL-shaped and sealed by the substrate's existing registry discipline. This is not a new trust root; it is a third fold, and the spec names the *fold*, not the log, as the novelty (§1.5).
- It **identifies its one discontinuity honestly**. The Kever's and Tever's transition rules are protocol constants; the Gever's is committed data. The reflexivity is bounded positionally — "law never applies to itself at a coordinate, only to its successor at the next" (`:1517-1519`) — which is the structural analogue of pre-rotation: commit forward, never rewrite backward.
- The **refusal discipline** is exactly the guard that keeps the evaluator on the validator side of KERI's controller/validator line. "An evaluator that legislates is a constructor wearing the wrong name" (`:1201-1203`) is the right instinct, and it is the same instinct as "a watcher observes; the relying party enforces."
- §14's **stated-evidence-scale** duty and §15's openness clause are the kind of assumption-naming KERI's own corpus models. A specification that says "every executable claim herein was exercised against one implementation at one pinned checkout" (`:1952-1957`) has earned the right to be read charitably about what it has *not* claimed.
- §17 is a genuine attempt at **conformance-vector thinking** — must-reject vectors, permuted-arrival-order vectors, "a guard that has never been shown failing is not yet a guard" (`:2303-2304`). Most governance specifications never get this far, and I am grading against a bar the document set for itself.

I also want to record two constructs that **reduce cleanly and honestly, with the spec saying so**, so that nothing below reads as a reflex to shrink:

- **Edict.** §6's SHALL — "a bare self-addressed data item, never an issuer-bearing credential container" (`:898-901`) — *is* the reduction. An edict is a plain SAD plus a prohibition. No new type is claimed and none is needed; the reasoning ("an issuer field smuggles a spine, and authority lives in the anchors") is correct in KERI's terms and I have no quarrel with it.
- **Cone.** The carriage reduces to the ToIP verifiable dossier and the spec says so (`:859-868`). The one thing that does *not* reduce — the transitive-closure obligation, "it SHALL contain every log span the finding's replay reads… completeness is decidable by the replay itself" (`:872-876`) — is a real remainder and, rarer, a **decidable** one. That clause is the best-specified obligation in the document. (Its rejection outcome is untyped; see F6. The obligation itself is sound.)

---

## Top findings

### F1: The fold's inputs are closed to three at ruled-span force and opened to four at ruled-span force — the `lens` cannot be both inert and load-bearing

- **Severity:** HIGH · **Confidence:** CONFIRMED · **dedupe_key:** `fold-inputs-closed-triple-vs-pinned-lens` · **Objective function:** survivability · **Layer:** governance · **Bucket:** spec-gap
- **Location:** `custos-4.1.md:245-247` (axiom 2), `:1033-1038` (§7.3 Inputs), `:752-755` (§4 Lens), `:378-381` (§1.6), `:1650-1652` (§12.2 step 3), `:901-904` (§6 warranty), `:1684-1690` (§12.3)

**Finding.** Four ruled or definitional spans disagree about how many inputs a finding has.

Closing side (two of them keyworded or axiomatic):

> "the inputs are exactly three, closed: the committed evidence bundle, the committed law head, and the appraisal position. **No other input may influence the result.**" (`:245-247`)

> "A finding is a function of exactly three inputs… No other input — wall clocks, local state, operator discretion, **ambient configuration** — may influence a finding. Two evaluations of the same triple SHALL return byte-identical findings." (`:1033-1038`)

Opening side:

> "**Lens.** The committed coordinates of an appraisal semantics: which rule-set, **which engine profile**, which predicate set a finding or warranty **was computed under**, cited by identifier." (`:752-755`)

> "the comparison runs over **the complete committed inputs of each fold** — the committed evidence bundle, the committed law head, the appraisal position, **and the pinned engine profile of the comparing lens**" (`:378-381`)

> "B's evaluator **SHALL** compute its finding over E as evidence under B's own Constitution **and committed adoption lens, and under nothing else**" (`:1650-1652`)

An engine profile is ambient configuration by any reading an implementer will apply. So §12.2's SHALL names a fourth input that §7.3's SHALL forbids. There is no reconciling clause anywhere in the document.

**The two implementations this permits.** Team A reads the closed triple as governing: the lens is redundant metadata, its engine-profile component is inert, and a warranty's "pinned lens" adds nothing the law head does not already carry. Team A therefore ignores the engine-profile component entirely when recomputing a warranted finding, and treats a warranty citing an unknown engine profile as verifiable. Team B reads §12.2 and §4 as governing: the engine profile is semantically load-bearing (that is the only reason to pin it immutably), so a finding computed under profile P is not comparable to one computed under profile Q, and Team B **refuses to falsify a warranty whose pinned profile it does not run**. Team B has just destroyed the replay-falsifiability that §12.3 and §12.4 make the entire discipline of warranted consumption ("a false warranty is replay-falsifiable by construction… one honest verifier recomputing from committed bytes convicts the warrantor", `:1690-1693`). Team A has just read three ruled spans out of the document.

Worse, the failure is silent in exactly the shape my lens hunts. Both teams emit well-formed findings. The divergence appears only when someone byte-compares, which is precisely the operation §7.3's SHALL exists to guarantee will succeed.

**Compounding: the `lens` has no committed form.** §6 requires a warranty to carry "its lens cited by edge" (`:901-904`). An ACDC edge's far node is another ACDC referenced by SAID (ACDC spec `spec/spec-body.md:114`, "The top-level Edge section `e` field value makes a cryptographically verifiable commitment to other ACDCs via references to their SAIDs"; operator field `o` at `:51`). So the lens must be an ACDC — but the document never says it is one, names no schema for it, no edge label, no operator, and no encoding for "engine profile". §15 confesses the engine *interior* undesigned (`:2064-2072`), which is legitimate; what is not legitimate is requiring a normative citation of a profile of that undesigned interior. I cannot write a conformance vector for "the same warranty under a different pinned lens" from the spec text.

**Why it matters (in KERI's terms).** §2 makes replay the class-defining obligation. Doctrine claim 9 makes the spec, not any one implementation, the interop invariant; two conforming Custos engines that disagree about whether the engine profile is an input do not agree on the one property the class is named for. This is not a PKI prior — it is the same discipline as "a Kever folds a KEL to the same key state everywhere."

**Recommendation (proposed).** Pick one, in text. The cheap repair, which is also the parsimonious one: redefine `lens` as a *projection of the law head* — rule-set identifier plus predicate-set identifier, both already inside the committed law — and **delete the engine profile from it**, stating explicitly that a pinned lens is a convenience citation that adds no input and that a finding recomputed under any conforming engine must match. Then amend §1.6's comparison-input list to the three, and §12.2 step 3's "and under nothing else" to name the triple. If instead the engine profile *is* meant to be load-bearing, axiom 2 must be amended by succession per §1.7's law-closure rule, and §12.3's falsifiability claim must be re-graded, because it no longer holds unconditionally.

---

### F2: Under track one, no committed rule lets a verifier decide which anchored spans constitute the GEL

- **Severity:** HIGH · **Confidence:** CONFIRMED · **dedupe_key:** `gel-span-membership-underivable` · **Objective function:** survivability · **Layer:** governance · **Bucket:** spec-gap
- **Location:** `custos-4.1.md:2216-2222` (track one), `:2232-2252` (the bootstrap), `:2203-2211` (canonical order), `:652-663` (§4 GEL), `:1490-1494` (§11 governed registries/credentials); keripy `src/keri/vdr/eventing.py` `issue()` at `:227` and `revoke()` at `:267` (re-read today)

**Finding.** §17 commits a canonical order — "KEL anchoring order first, intra-anchor order as the anchoring event's seal list states, and no tiebreak that consults anything uncommitted" (`:2203-2207`) — but never commits a **membership** rule. Under track two the ilk distinguishes governance events. Under **track one** it cannot:

> "**Track one — registry-form reuse.** GEL events use the substrate's registry event forms under their existing ilks, with governance semantics carried entirely by the committed law that interprets them." (`:2216-2219`)

A gAID's KEL anchors more than its GEL. §11 explicitly types **governed registries** ("registry inception and management") and **governed credentials** ("issuance and revocation") as classes the same domain exercises (`:1490-1494`). So the same KEL carries registry-form seals for ordinary TELs *and*, on track one, for the GEL — in the substrate's own identical forms. I re-read the reference forms: an `iss` event is `{v, t, d, i, s, ri, dt}` where `i` is the credential SAID and `ri` the registry (keripy `vdr/eventing.py:227`), and `rev` likewise (`:267`). Nothing in those bytes says "law."

The bootstrap clause is the place this would be fixed, and it enumerates exactly two committed items:

> "**The bootstrap.** **Track choice** and, for track two, the **initial ilk table** are committed law — and a verifier must derive them before it can admit the first event they govern." (`:2232-2235`)

Registry designation is not among them, and "placement" plainly means track placement — §17's own boundary vector says "both-track **placement** without committed placement law" (`:2291-2292`). §4's gAID genesis knot seals only C's SAID at inception (`:617-620`); it commits no GEL registry identifier.

**The two implementations this permits.** Team A folds every registry-form event anchored in the gAID's KEL as a GEL event — so an ordinary credential issuance by the domain becomes a governance event, and the Constitution grows clauses nobody enacted. Team B requires an explicitly designated registry and, finding no designation rule in the text, invents one (first `vcp` anchored after the inception seal? the registry named in C? the registry whose `ri` appears in the founding law?) — three plausible inventions, three different Constitutions. Both teams return a well-formed Constitution from identical bytes. §7.3's byte-identity SHALL is violated with no diagnostic anywhere.

**Why it matters.** This is the seam where the charge's question (a) actually lives. The spec's own concession is that the GEL "is a TEL-shaped log with governance semantics… this standard introduces no new anchoring pattern" (`:139-146`). If the GEL genuinely reduces to a governance-schema'd registry, then *the registry identifier is the reduction* and it must be committed at genesis, exactly as the substrate commits a registry's identity in its `vcp`. The document takes the reduction's benefit (no new anchoring pattern, "colorless base", "any registry-capable consumer parses the events unharmed") without paying its one price. My lens does not adjudicate whether the third log type is needed — that is SKP's — but I can say that **as written, the reduction is neither performed nor blocked; it is left underivable**, and §17's own refusal clause ("Where a verifier cannot derive the initial placement or table… it refuses the stream", `:2246-2252`) does not fire, because track placement *is* derivable; only membership is not.

**Recommendation (proposed).** Add the GEL's registry identifier to the bootstrap's committed set: the founding law SHALL commit the identifier of the registry (or the explicit span-selection predicate) whose events constitute the GEL, readable from the inception-sealed founding law before any GEL event is consumed — the same grade §17 already assigns to track choice. Add a must-reject boundary vector for a stream whose GEL registry designation is underivable, alongside the existing track/ilk-table vector.

---

### F3: The refusal boundary is stated at two incompatible widths, and refusal sits outside every determinism SHALL in the document

- **Severity:** HIGH · **Confidence:** CONFIRMED · **dedupe_key:** `evaluator-refusal-boundary-underspecified` · **Objective function:** survivability · **Layer:** governance · **Bucket:** spec-gap
- **Location:** `custos-4.1.md:114-120` (§1.1), `:210-216` (§1.3 Evaluate), `:261-264` (axiom 3), `:1188-1195` (§7.5 ratified text), `:1197-1203` (§7.5 plain statement), `:2052-2062` (§15 wall list), `:2246-2252` (§17 bootstrap), `:1033-1038` (§7.3 Inputs)

**Finding — two widths.** The document gives the refusal trigger twice, at two different widths, and the wider one carries no keyword.

*Broad* (Chapter 1, which §1.7 declares "normative for this document itself", `:390`): "Where **no committed rule** makes the invocation evaluable at all, it refuses" (`:212-214`); "Where committed law **runs out**, the fold refuses rather than legislates" (axiom 3, `:261-262`); "not missing evidence under a rule, but **a missing rule** — she refuses the invocation" (`:114-117`).

*Narrow* (the ruled span, and the §15 wall): "Where evaluation would require **an uncommitted ordering or composition rule**, the evaluator **SHALL** refuse the invocation" (`:1191-1193`); §15's wall list reduces it further to "at an **uncommitted composition seam** the evaluator refuses rather than legislates" (`:2055-2056`); §7.5's plain statement likewise: "when **two committed authorities meet with no committed rule for composing them**, the evaluator refuses" (`:1197-1199`).

Under §3's own reading rule 1 — "Keyword-marked sentences are ruled spans… prose between them motivates and derives but **binds nothing on its own**" (`:535-540`) — the *narrow* trigger is the normative one and the broad Chapter 1 statements bind nothing. That is almost certainly not what the author intends, because Chapter 1 is declared normative for the document and §17's bootstrap refusal is a *missing-rule* refusal, not a composition-seam refusal: "it refuses the stream — **a missing rule, not missing evidence**" (`:2250-2252`) — a sentence that also carries no keyword, so §17's own refusal path is not a ruled span either, while §17 nonetheless owes "refusal-boundary vectors" testing it (`:2296-2300`).

**The two implementations this permits.** Ask a domain's Gever whether party P holds power Y, where the Constitution contains no clause conferring Y on anyone. Team A (broad): no committed rule makes the question evaluable → refuse. Team B (narrow): no *composition or ordering* rule is required, so refusal does not fire; the requirement space contains "a clause conferring Y", which has not arrived, so return **pending(absent)** — whose cure per §7.2 is "the arrival of the missing evidence" (`:996-997`), i.e. the enactment of a clause. Team B has silently converted "this question is ill-posed" into "this question is one enactment away from affirmable", which is the exact confusion §1.1's "she does not guess, and she does not legislate" was written to prevent — and it is the friendlier answer, so it will be the one that ships.

**Finding — refusal is outside every determinism guarantee.** Refusal is emphatically *not* a finding: "Refusal is not a fifth finding value — it is the evaluator declining to answer an ill-posed question, **recorded as an operational fact**" (`:1199-1201`). But every determinism obligation in the document is scoped to *findings*: "Two evaluations of the same triple SHALL return byte-identical **findings**" (`:1037-1038`); axiom 2's replay is over "computed state". No ruled span requires that two evaluators on the same triple **both** refuse, nor that their refusals be byte-comparable, nor that a refusal be committed at all. "Recorded as an operational fact" pins no form: no required fields, no ground obligation, no anchoring duty. §15's unresolved list even contemplates "a **committed refusal record**" (`:2084-2085`) as something that would resolve a *different* open question — confirming that a committed refusal record is not, today, a thing this document defines.

**Why it matters.** Refusal is the load-bearing anti-legislation guard — the thing that keeps the Gever a validator rather than a controller (doctrine claim: only a controller writes; no validator, however convinced, may write). A guard whose trigger has two widths and whose output falls outside the byte-identity obligation is a guard two implementations will fire at different times and report incomparably. And because refusal is where the fold *declines* rather than errs, the divergence produces no exception, no rejection, no diagnostic — the quiet failure shape, not the loud one.

**Recommendation (proposed).** (a) Choose one width and put it in a keyworded span; if the broad width is intended, amend §7.5's ratified text by succession rather than leaving Chapter 1 to carry it in unruled prose. (b) Add a ruled span extending byte-identity to refusal: two evaluators on the same triple SHALL either both refuse or both return the same finding, and a refusal SHALL carry the identifier of the underivable commitment (§17 already gestures at this: "the refusal names the underivable commitment", `:2252`) in a committed form. (c) State whether a refusal must be committed to be consumable across a frame boundary.

---

### F4: The pending species family is not total over the composed-evidence grammar the document itself adopts — a declined slot has no conforming species

- **Severity:** HIGH · **Confidence:** CONFIRMED · **dedupe_key:** `pending-species-not-total-over-composed-evidence` · **Objective function:** survivability · **Layer:** acdc · **Bucket:** spec-gap
- **Location:** `custos-4.1.md:978-1012` (§7.2, especially `:982` and the SHALL at `:1007`), `:1243-1267` (§8 Composed evidence), `:1653-1656` (§12.2 step 3); dossier spec `spec/dossier-spec-body.md:352-362` (threshold mechanics and slot dispositions), `:366-376` (the four operators)

**Finding.** §7.2's ratified rule enumerates the pending species exhaustively — "The species are **absent, window-open, unresolved-conflict, and expired/abandoned**" (`:982-983`) — and §7.2 makes carrying one mandatory: "A pending finding **SHALL** carry the species of each of its requirement elements" (`:1007-1008`).

§8 then adopts the dossier specification's threshold-operator grammar for composed evidence and commits a mapping:

> "An unsatisfied operator group is not a defect and not a defeat: it discharges as a **pending** finding whose typed requirement set enumerates exactly **the unfilled slots** — each element naming the slot's required schema, its expected issuer, and the citing clause" (`:1262-1267`; repeated at §12.2 step 3, `:1653-1656`).

But the cited grammar has **three** slot dispositions, not two. Re-anchored in the live dossier spec:

> "A slot is in exactly one of three dispositions: **Pending**… **Endorsed**… **Declined**: the slot references the same signed endorsement ACDC issued by the candidate, but with a `disp` of `"decline"` — a declination. This is an **authenticated refusal**. Its weight is not added to the threshold sum, but, unlike a pending slot, **it records attributable dissent** — distinguishing a candidate who was asked and refused from one who has not yet acted." (`dossier-spec-body.md:358-362`)

A **Declined** slot is unfilled — so §8 sweeps it into "the unfilled slots" — but it fits none of the four species. It is not `absent` ("cured by the arrival of the missing evidence", `:996-997`): the evidence arrived, signed, and says no. It is not `window-open` (no substrate superseding window is involved). It is not `unresolved-conflict` ("cured by an owned act of the party whose conflict it is", `:1005-1006`) — there is no conflict; there is a settled, attributable refusal, and the party has already acted. It is not `expired/abandoned` (nothing was retained and dropped).

**The two implementations this permits.** Team A assigns `absent` and emits a cure path — "await this endorser's evidence" — that the committed bytes already foreclose; a consumer reading the finding's cure path is told to wait for something that has definitively not happened, which is precisely the "verifier that cannot distinguish 'judged absent' from…" confusion §7.2's own last sentence warns against (`:1009-1012`). Team B assigns `unresolved-conflict` and emits a cure path pointing at the wrong party. Team C, holding the SHALL strictly, finds no assignable species and **refuses** — converting a perfectly well-posed composed-evidence question into an ill-posed one. Three conforming readings, three different outputs from identical committed bytes, on the single most likely composed-evidence path in the ecosystem (an *m*-of-*n* endorsement group where one endorser declined).

**Why it matters.** §8's threshold-algebra paragraph is the document's strongest reuse argument — "the same weighted-threshold satisfaction that governs key-event signing governs evidence sufficiency… a verifier that can evaluate a rotation can evaluate a quorum of endorsements" (`:1257-1261`), which is accurate against the live dossier text (`:353`, "This is the same fractionally weighted threshold KERI uses for key-event signing thresholds (`kt`)"). Answering the charge's absorption question for KN-18/KN-17: the absorption here is **real, not nominal** — Custos genuinely consumes the operator grammar rather than restating it. But the absorption is *partial in a way the document does not notice*: it adopted the operators and the slot weights and missed the third disposition. That is the characteristic failure of a real absorption, and it is exactly what a mapping table would have caught.

**Recommendation (proposed).** Add a fifth species — `declined` (or `refused`), whose cure is a substitute qualifying endorsement rather than the named party's act — by succession under §1.7's law-closure rule, and state the mapping from the dossier's three slot dispositions onto the species explicitly in §8. Add a conformance vector: an `MxN` group with one Endorsed, one Pending and one Declined slot, and the byte-exact pending finding it must produce.

---

### F5: The `pending → self-convicted` edge admits evidence that cannot satisfy the required payload of the state it enters

- **Severity:** HIGH · **Confidence:** CONFIRMED · **dedupe_key:** `self-conviction-edge-condition-contradicts-required-payload` · **Objective function:** survivability · **Layer:** governance · **Bucket:** spec-gap
- **Location:** `custos-4.1.md:1062-1064` (the edge), `:1065-1066` (the sibling edges), `:1052-1053` (the payload SHALL), `:953-959` (§7.1 self-convicted), `:2052-2062` (§15 wall: "the transition system is explicitly and completely enumerated")

**Finding.** The type's own definition of `self-convicted` is a contradictory pair and nothing else:

> "**self-convicted(proof)** — the subject's own committed bytes contain a contradiction: two voices where its constitution demands one. Ground: **the canonical proof package identifying the contradictory pair**." (`:953-957`)

> "A self-convicted finding **SHALL** carry the identifier of the canonical proof package **for the contradictory pair**." (`:1052-1053`)

Two of the three edges into that state say exactly that: "a contradictory pair bearing on the question enters the bundle" (`:1065`, `:1066`). The third does not:

> `| pending | self-convicted |` "a bearing contradictory pair, **or new governed-status evidence** (committed evidence newly bearing on the subject's status under the governance tier's committed predicates), enters the bundle" (`:1062-1064`)

The disjunct's second arm admits evidence that is *not* a contradictory pair. The parenthetical gloss says "bearing on the subject's **status**", not "contradiction". So the edge permits a transition into a state whose ruled payload can only be satisfied by an object the triggering evidence does not contain — and by the Ground Axiom, "a value arriving without it is not a member" (`:164-167`).

**The two implementations this permits.** Team A reads the second arm as redundant with the first (governance-tier duplicity *is* "contradictory enactments under one committed predicate", §7.4 `:1144-1146`), and never fires it independently — in which case the clause is dead text in a section §15 lists as a completely-enumerated **wall**. Team B reads it literally, fires the edge on new governed-status evidence, and must then either (i) emit a self-convicted finding with an empty or synthesized proof-package identifier — a bare verdict, which §7.1 says is not a member of the type — or (ii) manufacture a "canonical proof package" for a pair that does not exist. Team B's output is terminal and unrecoverable: "Self-convicted is terminal for its question — the question is poisoned, and **no further evidence rehabilitates it**" (`:1086-1089`), and every backward edge out of it is forbidden absolutely (`:1076-1078`). So the ambiguity's cost is not a re-computation; it is an irreversibly poisoned question in one implementation and a live pending one in another.

This also crosses §7.4's own force distinction, which the document says a conforming evaluator SHALL NOT merge: "Breach and duplicity remain distinct crimes at every tier: defeated is conviction by another's citation; **self-convicted is conviction by one's own committed pair**. No clause of this document blurs them." (`:1165-1168`). The `pending → self-convicted` edge's second arm blurs them.

**Recommendation (proposed).** Delete the second disjunct, or — if a governance-tier status change genuinely must move a pending finding — route it to `defeated(citation)` where a citation exists, and state the required payload for the new path. If the arm is meant to name governance-tier duplicity specifically, say so in the contradictory-pair vocabulary the other two edges use, so the three edges are orthogonal and the payload SHALL is satisfiable on all of them.

---

### F6: The mandated conviction-kind family is not total over the rejections the document itself names

- **Severity:** MEDIUM · **Confidence:** CONFIRMED · **dedupe_key:** `conviction-kind-family-not-total` · **Objective function:** survivability · **Layer:** governance · **Bucket:** spec-gap
- **Location:** `custos-4.1.md:1973-1983` (§14 Conviction kinds), `:872-876` (§6 short cone), `:2288-2300` (§17 boundary vectors), `:1321-1327` (§9 seal-kind conviction discipline)

**Finding.** §14 makes the taxonomy exhaustive and mandatory:

> "Every conviction a federated GARD emits **SHALL** name its kind within the governance canon violation family: a **canonical-form violation** (the bytes fail the committed corpus form — ordering, corpus identity) or a **GARD-law violation** (well-formed bytes whose content violates a committed clause). The two kinds never blur… **A conviction record from which the kind cannot be read is unauditable and therefore not a conviction record.**" (`:1973-1983`)

Two rejections the document names elsewhere fall outside both kinds:

1. **The short cone.** "a replay that reaches for a span the cone lacks **convicts the cone as short**" (`:875-876`). The bytes are well-formed and violate no clause — evidence is simply *absent*. That is neither a canonical-form violation nor a GARD-law violation. Nor is it obviously a conviction at all: absent evidence is what `pending(absent)` exists for. The document uses conviction language for what its own codomain types as pending, and §14 then demands a kind that does not exist.

2. **The §17 must-reject vectors.** The boundary family lists six must-reject conditions (`:2288-2296`) — non-saidive event identity; a designated-class act anchored in an interaction event; both-track placement without committed placement law; an underivable initial track/ilk table; a grammar migration not admitted under the prior grammar; compact-form use while a gate stands — and never says, for any of them, which output "reject" is: `defeated(class, citation)` with which defeater class, `self-convicted`, a refusal, or a parse failure. Two of the six are plainly form-shaped (non-saidive identity) and two are plainly law-shaped (interaction-event anchoring of a designated class), but the underivable-grammar case is §17's own *refusal*, which is not a conviction at all and therefore has no kind to name.

**Why it matters.** This is a conformance-testability defect in my strict sense: I cannot write a vector whose pass/fail is decidable from the spec text, because the expected output is not determined. §17 owes these vectors as committed deliverables, and whoever writes them will have to legislate the outcome — which is the document's own named failure mode ("An evaluator that invents an ordering to avoid refusing has legislated", `:1201-1202`) displaced onto the vector author. §9's parallel discipline shows the author knows the shape of the fix: "a conviction sourced from a seal names the seal kind it convicts under — a digest mismatch, a coordinate mismatch, and a clause violation are three different refusals" (`:1322-1326`). §14 needs the same treatment one tier up.

**Recommendation (proposed).** Either widen the family to cover absence and refusal explicitly (a three- or four-member family: form violation, law violation, evidence-absence, refusal-of-invocation — the last two not being convictions, and said so), or re-word §6's short-cone clause to the pending vocabulary it actually describes. Then annotate each §17 must-reject vector with its expected codomain value, defeater class, and conviction kind, so the vector is decidable from the text.

---

### F7: The covenant seal's admissibility side-condition and its verification procedure are both undecidable from the text

- **Severity:** MEDIUM · **Confidence:** CONFIRMED · **dedupe_key:** `covenant-seal-verification-undecidable` · **Objective function:** survivability · **Layer:** keri-core · **Bucket:** spec-gap
- **Location:** `custos-4.1.md:1309-1319` (§9 Covenant seal), `:176-181` (§1.2), `:1321-1323` (the naming MUST), `:2064-2072` (§15 carriage confession); KERI spec `spec/spec-body.md:405-422` (seal count-code table), `:511-518` (Typed seal), `:480-484` (Latest establishment event seal) — all re-read today

**Finding.** §9 defines the covenant seal's verification as an open predicate:

> "Verification is neither byte equality nor coordinate lookup: **the verifier evaluates whether the successor satisfies the committed clause**… The covenant seal is admissible only where **the substrate's law makes lineage the invariant**; where byte equality is achievable, the digest seal is the honest kind, and **substituting the weaker kind is itself a defect**." (`:1312-1319`)

Three things are not decidable here.

(a) **"Where the substrate's law makes lineage the invariant"** names no substrate clause and resolves to nothing checkable. I re-read KERI's seal grammar: the substrate ships digest (`-Q`), Merkle-root (`-R`), source-event couples (`-S`), key-event triples (`-T`), latest-establishment (`-U`), backer (`-V`) and typed (`-W`) seals (`spec-body.md:405-422`). Nothing in that table, or in the surrounding §Seals text, distinguishes a "lineage invariant" from a "byte-identity invariant" as a *substrate law*. Custos §9 is accurate about what the table contains (I verified the enumeration at `:1288-1296`, including the latest-establishment seal it puts expressly out of scope) — but the admissibility test it then states cannot be run against it. Meanwhile the document declares violating that untestable test "itself a defect" (`:181`, `:1318-1319`). A defect condition whose test is undecidable will be found by nobody and asserted by anybody.

(b) **"Whether the successor satisfies the committed clause"** names no clause language, no satisfaction relation, and no "successor" relation. Two verifiers holding the same seal and the same successor can reach different verdicts by construction — which is the one thing §5 says never happens in the medium ("their agreement is cryptographic rather than negotiated", `:812-813`). A covenant seal is therefore not a medium object at all; it is a frame-local evaluation wearing a medium object's name, in a section whose other two kinds are strictly medium-computable. That non-orthogonality is the finding: the seal ladder's three rungs are not the same kind of thing, and the text asserts they are ("Two disciplines bind **all three kinds**", `:1321`).

(c) **The naming MUST is not testable.** "A seal names its kind: consumers **MUST NOT** be left to infer commitment semantics from context" (`:1321-1323`). The substrate ships the exact facility — the typed seal, `-W`/`--W` `TypedDigestSealCouples`, whose `t` field is "the **versioned type** of the seal… so that various types of digests with different semantics and derivations may be used" (`spec-body.md:511-517`), a 7-character CESR primitive (code `Y`) carrying 4 type + 3 version characters. Custos acknowledges the substrate ships "a generic typed seal" (`:1291-1292`) and then never says whether the covenant seal is carried as one, nor reserves a `t` value for it. §15 confesses carriage encoding open (`:2068-2072`), which covers the *bytes* — but a MUST about naming that cannot be tested until the confessed-open thing is designed is a MUST written ahead of its own decidability.

**Why it matters.** This is my answer to the charge's KN-14 adjudication: **the absorption of the typed seal is nominal, not real.** 4.1 correctly cites the substrate's table and correctly scopes out the latest-establishment seal, but it does not adopt the typed-seal mechanism for its own extension; it names a third kind whose carriage is deferred and whose verification is an open predicate. The parsimony verdict from my lens is narrow but clean: the covenant seal's **carriage** reduces to `-W` with a reserved `t` value and buys nothing new; what does not reduce is the *verification procedure* — and that is precisely the part the document leaves undesigned. A construct whose only irreducible remainder is undesigned has not yet earned its rung on a ladder whose other two rungs are decidable in three lines each.

**Recommendation (proposed).** (i) Replace "where the substrate's law makes lineage the invariant" with a decidable test, or drop the admissibility side-condition and its "itself a defect" force until one exists. (ii) State the covenant seal's carriage as a typed seal with a reserved `t` value (this costs one reservation and discharges the naming MUST immediately). (iii) Either give the clause-satisfaction relation a committed language, or re-type the covenant seal honestly as a *frame-local* commitment whose verification is an appraisal returning a finding — not a medium-grade seal — and say so in §5's terms.

---

### F8: The comprehension gate — the document's own normative closure rule — is satisfied in exactly one of the fifteen sections it governs

- **Severity:** MEDIUM · **Confidence:** CONFIRMED · **dedupe_key:** `comprehension-gate-unmet-in-introducing-sections` · **Objective function:** survivability · **Layer:** governance · **Bucket:** spec-gap
- **Location:** `custos-4.1.md:388-415` (§1.7), `:2176-2181` (§17's compliant statement), and the non-compliant introducing sections: §4 (`:752-755` lens, `:733-735` covenant, `:757-763` organ/seat, `:796-804` availability charter), §6 (`:840-896` edict, cone, warranty, colored evidence), §9 (`:1347-1363` anchor grade), §12 (`:1575-1598` envelope, `:1608-1629` congruence), §14 (`:1965-1971` freezability)

**Finding.** §1.7 is declared "normative for this document itself" (`:390`) and states the obligation in two parts:

> "Every construct this standard introduces after this chapter **is introduced as a named composition of those seven, and the introducing section states the composition in its own prose**." (`:396-398`)

> "Primitive closure: a section that requires an eighth primitive has discovered a gap in this chapter's ontology, to be repaired here by succession — **or a prescription in that section, to be removed there.**" (`:405-409`)

§17 complies exactly, and shows what compliance looks like:

> "Composition, per the comprehension gate: a GEL event is a log entry (log) carrying an enactment or its evidence (enact), committed by seal into the gAID's KEL (seal), read by exactly one fold (fold, finding), and subject to the law in force at its position (succession). Nothing here requires an eighth primitive." (`:2176-2181`)

No other section does. §6 introduces the four objects that cross frames — the objects the charge asks the reduction test to be run on — and states no composition for any of them. §4 introduces `lens`, `covenant`, `organ`/`seat`, `availability charter`, `law head`, `position` with no composition. §9 introduces anchor grade, §12 the matched-anchor envelope and computed congruence, §14 freezability — none states one. §1.7's own inventory (`:399-404`) covers warranty, organ, tier, consumption, federation and adopted engine strata, and omits edict, cone, colored evidence, lens, covenant, availability charter and congruence entirely.

**Why it matters, and why it is not a style note.** The gate is the mechanism by which the standard makes its own parsimony *checkable* rather than asserted. Its absence at §6 is precisely why the charge's reduction test has to be reconstructed by a reviewer instead of read off the text — and reconstruction is where two readers, like two implementers, diverge. Concretely: **F1 exists because no section ever states the lens's composition.** Had §4 been required to write "a lens is a citation of a committed law head plus a predicate set (log, seal)", the engine-profile component would have had nowhere to hide, and the contradiction with axiom 2 would have been visible at drafting time. The gate is not decoration; it is the document's own static type-checker, and it is switched off almost everywhere.

I hold this to my own calibration line: this is not "I would have organized it differently." It is a keyworded self-imposed rule, declared normative for this document, unmet in fourteen of fifteen governed sections, with a remedy the document itself prescribes.

**Recommendation (proposed).** Run the gate as a drafting pass and add the one-sentence composition statement to each introducing section, on §17's model. Where a construct will not compose (my candidates: `lens`'s engine profile, per F1; the covenant seal's satisfaction relation, per F7), §1.7's own disjunction applies — repair Chapter 1 by succession, or remove the prescription there. The appendix of record already has the machinery to account such a pass line by line.

---

## Additional patterns noted

**Defeated-finding citation and canonical selection — raised, then held below finding grade.** §7.1 says the ground is "the citation of the defeating clause **or superseding act**" (`:946-948`); §7.3's SHALL says "the violated or superseding **clause's** identifier, or, for cryptographic defeat, the identifier of the failed verification subject" (`:1042-1046`). Under §3's reading rule 1 the SHALL governs and the ambiguity resolves — so I do **not** raise it as a divergence finding. The residual worth noting: for the `superseded` defeater class the required payload then identifies only the authorizing clause, not the displacing act, so a consumer cannot locate the act from the finding — an arguable Ground-Axiom thinness rather than a divergence. Separately, "the finding SHALL cite the **lexicographic minimum** of (defeater-class rank, citation identifier, subcode)" (`:1123-1126`) is followed by "where the clause defines none, the subcode is empty and **orders last**" (`:1134-1136`); an empty string is the lexicographic *minimum*, not the maximum, so the two sentences disagree. I traced reachability and could not construct a case where the tiebreak actually decides (equal rank *and* equal citation identifier forces the same clause, hence the same enumeration policy), so the clause is either contradictory or dead. Either way an implementer must guess; I record it here rather than spend a finding on a possibly-unreachable branch. The comparison's collation is also unpinned (byte order vs code-point order — harmless for qb64's ASCII alphabet today, not harmless if a citation identifier is ever a non-qb64 string).

**The SAID placeholder character is inherited, not stated — and that is fine.** §3 rule 2 describes the pin discipline as "the digest's own field carrying a placeholder of the same length as the encoded digest — the substrate's rule is length-parametric by derivation code" (`:548-556`) without naming the fill character. CESR pins it normatively: "The SAID verification protocol **MUST** be implemented as follows: … replace the SAID field value in the serialization with a dummy string of the same length. **The dummy character is `#`**, that is, ASCII 35 decimal" (`kswg-cesr-specification/spec/spec-body.md:1200-1205`). Because §3 attributes the rule to the substrate and §3's "substrate of record" paragraph names CESR (`:568-577`), an implementer inherits `#`. I checked this specifically because it is the shape of defect I hunt, and it is not one. Recording the negative result so the panel does not re-derive it.

**Track one satisfies the event-identity SHALL.** I checked whether §17's "Every GEL event SHALL carry a self-addressing identifier in its own field" (`:2193-2198`) is satisfiable on track one, since the substrate's registry forms use `i` for the *subject* (credential SAID), not the event. It is: the reference forms carry a separate `d` field which is the event's own SAID (keripy `vdr/eventing.py` `issue()`/`revoke()`, `:227`/`:267`, both built through `SerderKERI(sad=ked, makify=True)`). No finding. Worth stating because §17's compact-form gate correctly flags the *receipt* form as the one whose identifier field is not self-addressing (`:2274-2281`) — that distinction is accurate.

**The threshold-algebra reuse claim is accurate.** §8's "the same weighted-threshold satisfaction that governs key-event signing governs evidence sufficiency" (`:1257-1261`) is confirmed by the dossier spec's own framing: "This is the same fractionally weighted threshold KERI uses for key-event signing thresholds (`kt`): the threshold itself is the fixed constant 1, so there is no separate count field" (`dossier-spec-body.md:353`). Custos's description of the operator grammar (edge groups, `o` operator field, weighted slots each naming a required schema) matches `:353-358` clause for clause. This is real absorption, and it is why F4's gap — the missed third disposition — is a fixable omission rather than a wrong model.

**Establishment-anchoring of designated classes has an unstated operational consequence.** §9's SHALL requires charter, seat revocation, law-amending enactments and succession acts to anchor in establishment events (`:1357-1361`). Because KERI establishment events consume the pre-rotated next-key commitment, this makes every law amendment a key rotation of the gAID. That may well be intended ("the difference between promise and physics", `:1362-1363`) and it is a defensible trade in KERI's terms. It is not a spec-precision defect and I raise no finding; I flag it for GOV/SEC as a lifecycle-cost consequence the text does not surface, under any shared key those lenses choose.

---

## Residual unknowns

- **Whether the lens's engine profile is intended to be load-bearing.** F1 is robust either way — one reading kills replay, the other makes three ruled spans dead letters — but which repair is correct is an author-intent question I cannot close from the text. Flagged as `needs-info` in spirit; reported as `recommend-revise` because *some* repair is required regardless.
- **Whether a Declined dossier slot is meant to be inside Custos's composed-evidence scope at all.** §8 adopts the operator grammar "as profiled by the dossier specification" (`:1246-1252`); if the profile is meant to be narrower than the whole operator family, saying so would dissolve F4. It does not currently say so.
- **The prior-art adjudication I could not complete.** I adjudicated KN-14 (F7: nominal absorption), KN-16/KN-18 (§6's object-typing clause is a real adoption — a warranty *is* an ACDC by the document's own SHALL) and KN-17 (real, per §6's dossier carriage and the accurate threshold profile). KN-15 (delegation for seating), KN-19 (CESR carriage) and KN-20 (OOBI) are treated at gesture grade in §10, §15 and §14 respectively (`:1410-1420`, `:2068-2072`, `:2019-2021`); whether those gestures are real absorptions cannot be judged until the confessed carriage deliverable lands, and I decline to grade them as findings against a confessed-open surface.
- **Cross-implementation divergence is confessed, so I did not grade it.** §2 and §16 both state that cross-implementation agreement is an undischarged deliverable. Every divergence I report above is therefore a divergence *the spec text permits*, not a divergence anyone has observed — which is the only claim my lens is entitled to make and the only one I have made.

---

## Pre-ship self-check

For each finding I asked: *would a KERI core contributor recognize this as reasoning in KERI's own terms, or dismiss it as an outsider importing a PKI/IAM/blockchain/SD-JWT prior?*

- None of the eight assumes an **invulnerability** objective. Every one is scored against **survivability**: a divergence that leaves two honest verifiers with different answers degrades recoverability of judgment, which is the property this class is named for.
- None rests on a generic "a good spec would define X" appeal. Each exhibits either **two concrete implementations** the text permits (F1, F2, F3, F4, F5) or an **undecidable predicate the document itself gives normative force** (F6, F7, F8).
- None faults Custos for a property that lives in a lower layer. I did not fault the medium, key state, or duplicity semantics; §5's account of them is accurate and I checked it against KERI's own §Seals and superseding-recovery framing.
- I explicitly declined three candidate findings (defeated-citation divergence, SAID placeholder, track-one event identity) after verifying they resolve — the calibration line my persona names: a coherent-but-terse notation I would have drawn differently is not a finding.
- The charge warned that a parsimony critique is the shape most likely to smuggle a prior. I have not argued "just use a TEL" (F2 argues the opposite: the reduction is neither performed nor blocked, and the missing piece is a *designation*, not a type collapse) and I have not argued "just use an ACDC" (the spec already does, at SHALL force). Where I did reach for a substrate mechanism — the typed seal in F7 — I named what breaks without the covenant seal's remainder, and found that the remainder is the undesigned part.
