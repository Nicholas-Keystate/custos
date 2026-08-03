# Protocol Security & Verifier Realist (SEC) Review: Custos 4.1 — parsimony round B

**Date:** 2026-07-30
**Target(s):** `/home/daniel/code/3GR/custos/spec/custos-4.1.md` (sha256 `ff8b9e7a…b72b05`, 2471 lines, pin verified at preflight); cross-referenced against `/home/daniel/code/wot/kswg-keri-specification`, `/home/daniel/code/wot/keripy` (HEAD `5ba9b473`, branch `feat-di2i-direct-delegates`; every code citation re-confirmed against `origin/main` as well), `/home/daniel/code/me/kswg-acdc-specification`, `/home/daniel/code/me/kswg-dossier-specification`
**Effort:** deep **Objective lens:** survivability
**Sources used:** `keri-doctrine.md`, `review-house-style.md`, `orchestrating-reviews.md`, bible §§02, 03, 07; live re-anchored: KERI spec-body `:1690`, `:1799`, `:1806-1825`, `:1872`; keripy `src/keri/vdr/eventing.py:1345-1390`

---

## Executive summary

The security surface of Custos 4.1 is, in the main, KERI-native: it declines prevention, it keeps judgment local, it refuses a super-frame, it puts authority in anchors rather than issuer fields, and it confesses its observer dependence in the two places (§2, §15) where a lesser document would have assumed it. My lens finds no category error at the architecture level.

It finds four grounded defects at the seam where Custos's prose meets the substrate's actual machinery. Ranked: (F1) §13.1 lets a grounded enactment **declare its own appraisal position in its own content**, and runs both of the act's validity replays at that self-declared position — a governance-tier retrograde attack that the substrate's as-of-anchor discipline exists to defeat, and that §8 and §16 already close correctly with an anchor-derived rule; (F2) §9's anchor-grade doctrine asserts that an establishment-anchored seal is **"physics"**, which is false for delegated identifiers — the class §10 SHOULDs organs into — and which converts an observer-dependent detection property into a prevention claim; (F3) §12.2 step 1 takes the **witness-receipt threshold off the producing frame's own charter** and calls the verdict frame-invariant, inverting the substrate's explicit validator-selects-M self-protection control; (F4) §4's "same anchoring discipline as TELs" plus §17's seal-list intra-anchor ordering plus §6's "consumable by the existing toolchain" are **jointly falsified by the reference registry anchor check**, which requires a full event-seal triple, a back-pointing source couple, and exactly one seal in the anchoring event.

The single biggest is F1: it is the only one that lets an actor who has lawfully lost a power exercise it anyway with a replay that passes clean.

---

## Steelman

Stated at its strongest, in KERI's terms:

KERI settles authenticity and stops. Everything above the line — who was entitled to issue, under what rules, what a relying party owes when evidence goes bad — is presently improvised, and improvisation does not compose across trust domains. Custos's move is to take the one construction KERI already proved (a committed append-only log plus a pure fold from log bytes to computed state, with the fold's output carrying its own ground) and instantiate it a third time over law. That is not ontological inflation; it is the *same* construction, and the document says so: the GEL introduces no new anchoring pattern (§1.2 `:141-146`), and the only genuine discontinuity is that the Gever's transition rule is committed data rather than a protocol constant (§1.5).

Three of the document's specifically security-shaped choices are, from this lens, correct and worth defending against a reduction test:

- **The edict as a bare SAD, not an issuer-bearing container** (§6 `:898-901`). "An issuer field smuggles a spine, and authority lives in the anchors" is exactly the ACDC §Binding-to-Key-State argument: a paired signature binds to container context and the current moment; an anchored commitment binds to key state as of a coordinate. Custos got the KERI answer, not the W3C-VC answer.
- **The warranty's two obligations** (§6 `:879-885`). A reduction test that says "it's just an ACDC schema" misses that the *lens pin* is what makes false-warranty conviction well-defined. Without a pinned rule-set/engine profile, a warrantor accused of a divergent finding can always answer "different lens," and the conviction dissolves. The pin is the load-bearing anti-repudiation guard, not decoration. It reduces to an ACDC *schema* only in the sense that the pre-rotation `n` field reduces to "just a hash."
- **The rejection of the joint multisig identifier for federation** (§12.1 `:1589-1598`). A group identifier is a new authority above both parties, and exit becomes a contestable key-state operation. That is the federation-recentralizes shibboleth caught correctly, in the substrate's own terms.

And the refusal discipline (§7.5) is the right *shape* of guard: at an uncommitted composition seam, fail closed and do not legislate. My criticism below is never that these guards are unnecessary. It is that four of them are stated at a strength the substrate does not supply, or are described in terms the reference verifier does not implement.

---

## Top findings

### F1: A grounded enactment's appraisal position is content-declared, not anchor-derived — the retrograde attack, one tier up

- **Severity:** HIGH · **Confidence:** CONFIRMED · **dedupe_key:** `enactment-position-not-bound-to-anchor-coordinate` · **Objective function:** survivability · **Layer:** governance · **Bucket:** deployment-gap
- **Location:** proposal §13.1 `:1803-1808`, `:1812-1817`, `:1844-1849`; contrast §8 `:1274-1277` and §16 `:2155-2158`. Substrate ground: keripy `src/keri/vdr/eventing.py:1365-1388` (`Tever.verifyAnchor`), re-confirmed at `origin/main:1392`; keripy invariant H1; bible 07 §11.

**Finding.** §13.1 requires a grounded enactment to commit, *within its own content*, four things: the pinned evidence bundle, "the law head it invokes", "the position at which it speaks", and the claimed terminal finding (`:1803-1808`). It then makes both validity conditions run at that content-supplied coordinate: "an evaluator given the pinned bundle, the cited law head, and **the named position** returns the claimed finding. And the enactor was empowered: the acting party held the invoked power **at that position** under the Constitution then in force" (`:1813-1817`).

No span anywhere in the document requires the named position to equal the coordinate of the GEL event that carries the enactment. I grepped every occurrence of `position` and `coordinate` in the pinned text; there is none. All three inputs to both replays are therefore chosen by the party whose act is being checked.

This is not a uniform reading — it is a divergence *inside* the document. §8 uses the anchor-derived rule: "an enactment is lawful only if its author held the enacting power at **the enactment's position**" (`:1276`), where §4 `:748-750` defines a position as a coordinate "in the committed order of the log it names". §16 uses it explicitly: "an enactment is a lawful succession only under the Constitution in force at **its own coordinate**" (`:2157`). Two sites derive the position from the anchor; the one site that governs recourse — the sharp end, where force is applied — takes it from the actor's own content.

**Why it matters.** The substrate's answer to exactly this problem is anchor-relative validation. `Tever.verifyAnchor` does not accept a claimed position: it resolves `db.kels.getLast(keys=self.pre, on=seqner.sn)`, requires `eserder.said == saider.qb64`, and then requires the anchoring seal's own `s` field to equal the anchored event's `s` (`vdr/eventing.py:1365-1388`). The position is *derived from committed bytes on both sides*, never asserted. That is invariant H1, and it exists because "an attacker who ever obtains a key can forge evidence that looks like it originated in the past, forever" (`was.md` §Retrograde attack, via bible 07 §11).

Concrete failure: organ O holds power P under law head L1. At GEL coordinate 40 the domain enacts an amendment; the successor law head L2 strips O of P. At coordinate 50, O commits a grounded enactment — a revocation, a seat action, an adoption withdrawal — declaring **position 30**, **law head L1**, and an evidence bundle of digests all committed at or before 30, claiming the terminal finding "affirmed: O holds P." Both §13.1 replays pass by construction: the fold over (that bundle, L1, 30) returns that finding, and O did hold P at 30 under L1. The act is anchored at 50 and takes effect at 50. §13.1 `:1844-1849` then actively blesses the outcome — "Grounds do not rot… a recourse act lawful under the Constitution then in force remains lawful in the record even after the law that authorized it is superseded."

Nothing in the document convicts this. It is not self-conviction (no contradictory pair), not a failed ground replay (the ground replays), and not a standing defeat (the standing held at the declared position). A frame that has lawfully stripped an organ of a power cannot, under §13.1 as written, stop that organ from exercising it with a clean receipt.

Note the interaction with the repo's own open ruling R1: if R1 resolves position-indexed (the recommended option), *everything* hinges on which position a finding is indexed at — which makes the missing binding between declared position and anchor coordinate strictly more load-bearing, not less. R1 does not close this; it sharpens it.

**Recommendation.** One ruled span in §13.1, plus a must-reject vector. Smallest form: *the position a grounded enactment names SHALL be the coordinate of the GEL event that carries it, and the evidence bundle it pins SHALL be committed at or before that coordinate; an enactment whose named position differs from its anchoring coordinate is not a grounded enactment and confers nothing.* Add to §17's boundary must-reject family: "grounded enactment whose named position differs from its anchoring coordinate." If the drafters' intent was always that the two coincide, the clause costs nothing and removes the divergence with §8/§16; if it was not, the divergence is the finding.

---

### F2: §9's "establishment anchoring is physics" is false for delegated identifiers, and overstates detection as prevention even where it holds

- **Severity:** HIGH · **Confidence:** CONFIRMED · **dedupe_key:** `anchor-grade-physics-claim-overstated` · **Objective function:** survivability · **Layer:** keri-core · **Bucket:** proof-scope
- **Location:** proposal §9 `:1349-1363` (esp. `:1353-1356`, `:1358-1360`), against §10 `:1410-1420` and §14 `:1988-1993`. Substrate ground: KERI spec-body `:1690`, `:1799`, `:1806-1825` (rules A0/A1/A2/B1/B2/B3/C), re-anchored in `/home/daniel/code/wot/kswg-keri-specification/spec/spec-body.md`.

**Finding.** §9 states the anchor-grade doctrine unconditionally:

> A seal carried in an establishment event is physics: displacing it forks the establishment lineage itself, and the fork is duplicity evident to any watcher holding both branches. (`:1353-1356`)

and rests a SHALL on it: "Designated act classes — charter, revocation of a seat, enactment amending law, and the succession acts of section 16 — SHALL anchor in establishment events" (`:1358-1361`).

Both halves of the sentence fail, in different ways, and the failure is worst on exactly the identifier class §10 recommends.

**(a) For delegated identifiers the claim is simply false, and the substrate says so on purpose.** KERI's superseding rule set (spec-body `:1806-1825`) forbids rot-supersedes-rot only for *non-delegated* identifiers (rule A1, `:1808`). Rule B (`:1813-1819`) expressly permits a delegated rotation to supersede the latest-seen delegated rotation at the same `sn`, under B1/B2/B3 conditions keyed to the delegator's KEL ordering. The spec presents this as a *feature*:

> anytime the sealing (anchoring) event in the delegator's KEL may be superseded by another event, then the delegator and Delegatee may execute a superseding recovery of an establishment event in the Delegatee's KEL and thereby recover from the establishment Live-attack. **This is not possible with an establishment Live-attack on a non-delegated event.** (spec-body `:1690`)

So an establishment-anchored seal on a delegated KEL is displaceable, lawfully, and the displacement is *reconciliation, not duplicity* — a point Custos's own §5 concedes: "a rotation recovering a compromised log is repair, cited, not duplicity" (`:820-822`). §10 `:1410-1415` SHOULDs seated organs into delegated identifiers, and §14 `:1988-1993` propagates the charter "at every stratum of its delegation tree", contemplating a GARD as a delegated stratum — i.e., a gAID that is itself delegated. Under §10's own recommendation, the acts §9's SHALL most wants protected (revocation of a seat; seating) land on precisely the identifiers where the grade evaporates.

**(b) Even for non-delegated identifiers, "the fork is duplicity evident" misdescribes the mechanics.** Under A1 the second rotation at the same `sn` cannot supersede, and the KERI spec is explicit about the consequence: "an event that may not supersede… another event at the same location **cannot be first seen at all** by that KEL" (`:1799`). There is no branch in the validator's KEL; the second version is dropped. Evidence of the attempt exists only for a party that *independently received both versions* — which is the observer layer: A5 (observer presence, "optional in practice and MUST NOT be silently assumed") and A8-A11 ("None of A8-A11 are enforced by KERI"). Custos elsewhere refuses to grant exactly this (§2 `:487-490`, §15 `:2092-2100`). §9 grants it in one word.

This is the smoke-detector inversion in a document that otherwise avoids it: a detection property, conditional on unenumerated observers, restated as a physical guarantee.

**Why it matters.** §9 tells a consuming frame that "the difference is computable, and a consuming frame weighs it" (`:1356-1358`) — but the difference it is told to weigh is stated wrong, and the document supplies no procedure for computing the *actual* difference (is the anchoring identifier delegated? is its delegator's anchoring event still superseidable? has the latest-seen delegated rotation moved?). §7.2's window-open species (`:998-1005`) shows the drafters hold the correct fact — "for a delegated log the window closes only when no lawful superseding rotation remains admissible under the substrate's delegated-recovery rules, which stay open longer." §9 contradicts §7.2.

Concrete failure: a domain designates seat revocation as an establishment-anchored class per §9's SHALL, materializes seat tenure as establishment rotations on a delegated organ identifier per §10's SHOULD (`:1423-1425`), and then — via a delegator-side signing-key compromise, or a colluding gAID — a superseding delegated rotation at the same `sn` restores the seat under B1. A fresh verifier replaying the organ's KEL sees only the trunk: the revocation is on the disputed branch, and no duplicity is convictable anywhere in the medium. The frame's own §13.3 recourse-against-the-frame story ("an authority that speaks with two voices is convictable in the medium by anyone holding both", `:1885-1887`) does not fire, because under KERI's rules the authority did not speak with two voices — it performed a lawful recovery.

**Recommendation.** Replace the unconditional grade with a conditional one, in ruled form: *an establishment-anchored seal is undisplaceable only on a non-delegated identifier whose superseding-rotation prohibition (substrate rule A1) applies; on a delegated identifier the grade is bounded by the substrate's delegated-recovery window, and a frame committing a designated act class SHALL state which grade its anchoring identifier supplies.* Drop or qualify "the fork is duplicity evident to any watcher holding both branches" — the detection is observer-conditional, and §2/§15 already say so. Cross-reference §7.2's window-open species, which already carries the correct calculus.

---

### F3: The consuming frame's witness-receipt threshold is read off the producing frame's own charter, inverting the substrate's validator-selects-M control

- **Severity:** HIGH · **Confidence:** CONFIRMED · **dedupe_key:** `receipt-threshold-taken-from-producer-not-consumer` · **Objective function:** survivability · **Layer:** governance · **Bucket:** proof-scope
- **Location:** proposal §12.2 step 1 `:1637-1641`; §5 `:828-834`; §14 `:1985-2006`. Substrate ground: KERI spec-body `:1872` (Annex A, §Security Properties), re-anchored; `background.md` §5.8 via bible 02 §4.

**Finding.** The transformation law's first step reads:

> **Authenticate** (medium, frame-invariant): B MUST verify E's anchoring event against A's key state — signatures, coordinate, **witness receipts per A's availability charter**. This step is identical in every frame; it is the substrate's own admission machinery, and **its verdict does not depend on B's law**. (`:1637-1641`)

The substrate assigns that threshold to the opposite party. KERI spec-body `:1872`:

> When the controller is responsive but dishonest, the Controller may create inconsistent versions of an event that are first seen by different subsets of its witnesses. In the case where only F of the witnesses is faulty despite a dishonest controller, **the validator may protect itself by requiring a large enough sufficient agreement or threshold of accountable duplicity, M**, that guarantees that either only one satisfying agreement or none at all… **To restate, the validator may select its M to ensure that the service is immune** such that the service will either provide one and only one KERL or none at all. **This protects the validator.**

M is a validator-side self-protection knob, named as such. Custos's step 1 sources it from the producer's committed charter and then forecloses B from raising it, by declaring the verdict frame-invariant and independent of B's law. A frame A that is dishonest and runs its own witnesses (`background.md` §5.8: "a malicious controller can simply run its own witnesses"; "Witness thresholding alone does not prevent this") chooses both the witness set and the floor B checks against.

There is a charitable reading — "per A's availability charter" describes which receipts are *fetchable*, not B's threshold. It does not rescue the clause: under that reading, B's own immunity threshold is nowhere provided for in the entire crossing path, and the "verdict does not depend on B's law" sentence still forecloses it. Either way, the consuming frame is given no committed license to protect itself the way the substrate says a validator must.

**Why it matters.** §12.4's whole discipline rests on cross-frame convictability: "A frame that speaks with two voices — to two counterparties, at one committed coordinate — is convictable by anyone holding both logs" (`:1733-1737`). That conviction requires the two counterparties to be presented with *divergent-but-properly-receipted* versions and then to meet. The immunity constraint is the mechanism that stops A from producing two proper agreements at all — and it works only if the *consumers* set M. Handing M to A removes the one lever the substrate gives B, on the path where B is checking A.

Concrete failure: frame A commits a charter naming toad = 1 over three witnesses A controls. It issues edict E at coordinate n to frame B and edict E′ at coordinate n to frame C, each with one receipt from a different A-controlled witness. Both B and C execute step 1 exactly as written and both accept — the receipts satisfy A's charter, and neither is licensed to demand more. Custos's own §5 frame-invariance claim (`:828-834`, "whether an event is admitted by an identifier's key state is decided by the substrate's own machinery, identically for every observer") is true for signature admission and false for agreement immunity, which is per-validator by construction.

**Recommendation.** Split the two facts and make the second B's. Ruled form: *A's availability charter commits A's floor and grounds a breach finding against A; B's admission threshold for A's events is B's own committed law, and B SHALL apply the greater of the two.* And narrow the frame-invariance claim in §5 and §12.2 to signature/coordinate admission, stating explicitly that duplicity-immunity is validator-selected and therefore frame-relative. This is a scope repair, not a new mechanism — it is what the substrate already says.

---

### F4: "Same anchoring discipline as TELs" plus seal-list intra-anchor ordering plus "existing toolchain" are jointly falsified by the reference registry anchor check

- **Severity:** HIGH · **Confidence:** CONFIRMED · **dedupe_key:** `gel-anchoring-discipline-not-what-registry-layer-enforces` · **Objective function:** survivability · **Layer:** wire · **Bucket:** deployment-gap
- **Location:** proposal §4 `:652-658`, §6 `:906-908`, §17 `:2203-2211`, §17 track one `:2216-2221`. Substrate ground: keripy `src/keri/vdr/eventing.py:1345-1390` (`Tever.verifyAnchor`), call sites `:1083`, `:1157`, `:1321`; re-confirmed at `origin/main` (same check at `:1392`).

**Finding.** Three claims are made about the GEL's carriage:

1. §4 `:653-658`: "GEL events are sealed into the gAID's KEL by **the same anchoring discipline the substrate's registry layer uses for TELs** — a seal in the anchoring event carrying the GEL event's self-addressing identifier."
2. §6 `:906-908`: "Object forms typed this way are consumable by the substrate's existing toolchain; nothing here requires a bespoke parser."
3. §17 `:2203-2208`: "A fold consumes its log in exactly one order… KEL anchoring order first, **intra-anchor order as the anchoring event's seal list states**."

Read the actual registry anchor check at HEAD (`vdr/eventing.py:1345-1390`):

```python
dig = self.db.kels.getLast(keys=self.pre, on=seqner.sn)    # :1365  back-pointer required
...
if eserder.said != saider.qb64: return False               # :1374
seal = eserder.ked["a"]
if seal is None or len(seal) != 1: return False            # :1378-1379  EXACTLY ONE SEAL
seal = seal[0]
spre = seal["i"]; ssn = seal["s"]; sdig = seal["d"]        # :1381-1384  full event-seal triple
if spre == serder.ked["i"] and ssn == serder.ked["s"] \
        and serder.said == sdig: return True               # :1387-1388
```

Three divergences, each material:

- **The seal is an event-seal triple `(i, s, d)`, not a digest of the anchored event.** The anchoring seal must carry the anchored event's *own identifier and sequence number*, and both are checked. §4's description — "a seal in the anchoring event carrying the GEL event's self-addressing identifier" — describes a digest seal, which this code rejects at `:1387`.
- **A back-pointing source couple `(seqner, saider)` is required.** Without it the check returns False at `:1362-1363`. The couple names the exact KEL coordinate and the anchoring event's SAID; it is what makes the anchor check as-of-position rather than a KEL scan. Custos mandates no such back-pointer on a GEL event — §17 `:2199-2201` goes the other way ("a coordinate tuple is a location, never an identity").
- **The anchoring KEL event must carry exactly one seal** (`:1378-1379`). §17's canonical-order rule — "intra-anchor order as the anchoring event's seal list states" — is only meaningful when one anchoring event carries two or more GEL-event seals, and that is precisely the case the reference registry path refuses.

Track one (`:2216-2221`) is defined as "GEL events use the substrate's registry event forms under their existing ilks" — i.e., events processed by `Tever`/`Tevery`, through this exact code path.

**Why it matters.** §14's stated-evidence-scale duty (`:1941-1957`) commits that "every executable claim herein was exercised against one implementation at one pinned checkout." A track-one GEL with two governance events sealed into one KEL anchoring event does not verify at that implementation, so §17's order vectors ("permuted arrival, identical Constitutions", `:2302-2303`) cannot be discharged for the multi-seal case that gives the intra-anchor rule its content. And the §6 toolchain claim — the parsimony argument's strongest card, since it is what makes "no new type" cheap — is falsified for track one at the reference verifier.

Fairness note, because it matters for the repair: the *KERI spec* does contemplate multi-seal anchoring events — rule B2 (spec-body `:1817`) turns on "the anchoring seal of the superseding rotation's delegated event appears later in the seal list". So the seal-list ordering rule is spec-legal; it is the reference implementation's registry path that is stricter. That makes this a genuine gloss-vs-enforced gap of exactly the shape bible 07 §12 warns about, not a spec error — but a standard whose evidence trail is one implementation cannot claim toolchain consumability that the implementation refuses.

**Recommendation.** Three small repairs: (i) restate §4's discipline in the substrate's actual terms — an event-seal triple committing the GEL event's identifier, sequence number, and SAID, accompanied by a source couple naming the anchoring coordinate; (ii) either drop the multi-seal intra-anchor ordering rule for track one, or state that track one is constrained to one governance seal per anchoring event and reserve seal-list ordering to track two; (iii) qualify §6's toolchain claim to the forms actually exercised, and add a boundary must-reject vector for "track-one GEL event whose anchoring event carries more than one seal." Note that repair (i) also supplies the anchor back-pointer that F1 needs.

---

## Additional patterns noted

- **§12.2 step 1 says "against A's key state" without an as-of qualifier** (`:1637-1638`). Any implementation that verifies by replaying A's KEL gets this right for free, so this is a precision nit rather than a finding — but it is the same looseness as F1: the document names a key state and a position without saying *at which coordinate the key state is taken*. Worth one word ("as of the anchoring event's coordinate") in the same edit as F1.

- **Ruling docket R11 (issue #10) — refusal auditability.** I do not re-emit this as a finding; it is docketed. But I disagree with the docket's recommendation of option A ("scope the claim") from this lens, and record the reason. Refusal is the fail-closed output — §15 lists it as one of six binding walls (`:2055-2056`) — and under option A it is the only output of the system that carries neither a determinism SHALL (the §7.3 SHALL at `:1037-1038` is scoped to *findings*) nor a committed-record obligation (§7.5 `:1197-1201` classifies it as "an operational fact"). The document already applies precisely the opposite discipline to a sibling operational fact: §7.2 `:1009-1012` requires a committed eviction receipt because "a verifier that cannot distinguish 'judged absent' from 'silently dropped' holds no judgment at all." The same sentence is true verbatim of refusal. Under option A, a frame that declines to act can answer "the evaluator refused" and no stranger can falsify it — the false-warranty conviction machinery of §12.4 cannot reach it, because a refusal is definitionally not a finding and therefore not warrantable. A wall no one can prove you climbed over is not a wall. Option B costs more; it is the one that keeps the fail-closed path inside the discipline the rest of the document enforces.

- **Track one makes governance events *also* real registry events.** On track one a GEL event is a `vcp`/`iss`/`rev`-shaped event processed by a live `Tever`, which will compute genuine registry state from it independent of the Gever's law. §17 calls this "the colorless base: any registry-capable consumer parses the events unharmed" (`:2218-2220`). Parsing unharmed is not the same as *state-computing consistently*: a governance-blind registry consumer will hold a TEL state for the domain's law that the Gever may read differently. I could not close this into a failure scenario from the text — the interaction depends on which registry ilks a domain elects — so I flag it as a residual rather than a finding, and hand it to KRT/SPC.

- **Where the reduction test lands, from this lens.** The covenant seal, the cone, and colored evidence I leave to the sibling lenses that already adjudicated them in round A; I have nothing to add and do not dispute their findings. On the two seeded questions: the **warranty** does not reduce to a bare ACDC schema, because the pinned lens is what makes false-warranty conviction well-defined (see Steelman) — a schema constrains shape, not the rule-set under which a claim can later be falsified. On the **GEL vs TEL** question, my lens is agnostic about the log type but not about the description: F4 shows that the "TEL-shaped, no new anchoring pattern" claim is not yet accurate as stated, which cuts *against* the parsimony case, not for it — the reuse argument is only as strong as the fidelity of the reuse.

- **What I checked and found clean.** The availability charter is not a phone-home (§6 `:857-858`, §12.2 step 2): the fetched cone is self-verifying committed bytes — "Wrong bytes convict on arrival; the name is the verification" (`:1645-1646`) — which is data-not-authority, the correct KERI posture (`00-lens.md` claim 1). No construct in the document consumes a latest-establishment seal (§9 `:1293-1297`) or the deferred evaluation seal, and the evaluation seal's admissibility rule ("Commit predicates, never verdicts", `:1341-1343`) is the right guard against smuggled authority. §12.1's rejection of the group identifier and §12.1's "No super-frame exists" (`:1600-1605`) hold up. I found no reintroduced verification-time authority, no witness-as-voucher, and no place where the document weakens the pre-rotation firewall.

## Residual unknowns

- Whether §13.1's named position was *intended* to be the anchoring coordinate. If yes, F1 is a one-sentence repair and a missing vector; if no, it is a design hole. I could not resolve it from the text, and both readings are conformant — which is itself the defect.
- Whether any Custos fixture has ever exercised a multi-seal anchoring event on track one. I read the pinned spec and the reference verifier, not the repo's fixture tree; if such a vector exists and passes, F4's third divergence needs re-examination (the first two stand regardless).
- The delegated-recovery window calculus F2 asks for is genuinely non-trivial to state (it recurses up the delegation chain per rule C, spec-body `:1821-1825`). I have not attempted to draft it; §7.2 already cites the substrate's calculus by reference, which may be the right grain for §9 too.
