VERDICT: NOT REFUTED

The claim in §V.6 is that no prior system (pre-2026) holds P1–P4 jointly at the grades defined in Part 0. I searched for a single system exhibiting all four and found none. Below are the strongest near-misses, ranked, each with the reason it falls short stated against the claim's own grading discipline.

---

**Near-miss #1: Certificate Transparency (RFC 6962, 2013)**

Closest overall. P2 strong (issuance acts sealed as SCTs in append-only Merkle logs, attributable, replayable). P3 strong (planetary-scale, live, adversarial). P4 in normative text — RFC 6962 §5 and §7.3 confess the split-view residue: "Violation of the append-only property is detected by global gossiping... As soon as two conflicting Signed Tree Heads for the same log are detected, this is cryptographic proof of that log's misbehavior."

Why it falls short:
- **P1 stays at "~" (partial), not "yes."** Part 0 defines P1 as "replayable verdicts against declared invariants, capable of convicting the foundation and of certifying its cure." CT can convict a log — conflicting STHs are cryptographic proof of misbehavior. But it cannot *certify a cure*: there is no mechanism inside CT for a convicted log to amend itself and be re-certified by the same system. A compromised log is abandoned; a new log is created. The "certifying its cure" half of P1 is absent. Moreover, CT cannot detect split-views from inside a single client's view — the property the document grades as P1's core ("evaluates its own foundation") is not self-verifiable by CT; it requires an external act of comparison. This is precisely the document's row-11 residue. P1 cannot be upgraded to "yes" under the document's own definitions.
- **P4 stays at "in normative text," not constitutional with organ.** Part 0's P4 requires the residue to be "a named, first-class object — with the form Löb's theorem forces: an axiom or an attestation of an external act." RFC 6962's gossip clause is attestation-shaped (external comparison required), which is correct Löb form. But the document's §V.3 distinguishes Custos's P4 by having an *organ attached* to the confession — the watcher role. CT's gossip organ was never deployed (draft-ietf-trans-gossip never became an RFC; browsers and monitors provide monitoring but not the split-view gossip mechanism specified in §5/§7.3). A confession in text without a working organ is the document's own distinction between CT's P4 ("in normative text") and Custos's P4 ("constitutional Ω-row"). The document grades this fairly; an upgrade to full P4 would require a deployed gossip organ, which does not exist.

Two upgrades needed (P1 ~→yes, P4 text→constitutional-with-organ). Both fail against the document's own grading.

---

**Near-miss #2: Tezos (2014 / 2018)**

P2 real (amendment acts are attributable, sealed, ordered, on-chain). P3 real (live, continuous, many protocol upgrades without hard forks).

Why it falls short:
- **P1 stays "nominal," not "yes."** The document grades P1 as nominal because "Voting establishes that stakeholders assented, never that the proposed validation layer is correct; there is no conformance suite that can return a finding against the reference implementation." This is accurate per the Tezos white paper (Goodman 2014), which specifies stake-weighted voting on proposals — preference aggregation, not finding-grade evaluation. To upgrade P1, I would need to exhibit a Tezos mechanism that evaluates candidate protocols against declared invariants to finding grade before adoption. No such mechanism exists in Tezos's amendment cycle (exploration → promotion → cooldown → adoption), which is entirely vote-based.
- **P4 stays "absent," not "yes."** The document notes Tezos "defines away" non-forkedness by consensus rather than confessing it as residue — "the one property our telos insists must be confessed is the one a blockchain claims to have abolished." There is no constitutional text in Tezos's protocol or governance documentation that confesses what the protocol cannot verify about itself, in Löb form or otherwise. To upgrade P4, I would need to find such text. It does not exist.

Two upgrades needed (P1 nominal→yes, P4 absent→yes). Both fail.

---

**Near-miss #3: Milawa / Jitawa (Davis 2009; Myreen & Davis 2014/2015)**

P1 strongest in the entire matrix — the tower is admission-by-replay: Level 1 checks Level 2's fidelity claim, Level 2 checks Level 3, and so on to Level 11, carried down to verified x86 machine code.

Why it falls short:
- **P2 stays "absent."** Part 0 defines P2 as "verification runs are themselves attributable, sealed records inside the system under verification: who ran what, against which bytes, in what order — cryptographically committed, replayable by anyone." Milawa produces proof files (8.4 GB of them). These are artifacts, not acts by identified parties. There is no actor who performs a verification, no cryptographic seal of that act, no record of *who* ran *what*. The tower's admissions are proof-theoretic, not governance acts. To upgrade P2, I would need to show that Milawa records its verification runs as attributable, sealed events. It does not.
- **P3 stays "absent."** Part 0 defines P3 as "a standing organ, not a one-shot proof... it re-runs as the foundation changes, and a foundation change is itself a governed act admitted by replay." Milawa was proved once over ~4 person-years and then frozen. The document grades this accurately: "proved once, then frozen." There is no standing organ that re-runs as the foundation changes. To upgrade P3, I would need to show that Milawa's verification is continuous and that changes to its foundation are admitted by replay. Neither is true.
- **P4 stays partial ("skeptic's list"), not "yes."** The four-avenue skeptic's list (HOL4/ML/compiler/OS/hardware; x86 model vs. silicon; OS-mediated I/O; semantics mis-definition) is a prose confession, not "constitutional text" as Part 0 requires — "a named, first-class object" with Löb form. It is a research-paper caveat, not a constitutional article with an organ attached.

Three upgrades needed (P2 absent→yes, P3 absent→yes, P4 partial→yes). All fail.

---

**Near-miss #4: DNSSEC Root KSK Ceremonies (IANA/ICANN, recurring)**

P3 present — ceremonies recur on a regular cadence (KSK rollovers: 2018, 2024, scheduled future). P2 partial — ceremonies are scripted, video-recorded, witnessed, and audited. P1 weak — procedural attestation by human witnesses, not finding-grade conformance against declared invariants. P4 weak — operational documentation, not Löb-form constitutional text.

Why it falls short:
- **P1 is not finding-grade.** The ceremony verifies that KSK generation proceeds per script, but this is witnessed procedural compliance, not "replayable verdicts against declared invariants, capable of convicting the foundation and of certifying its cure." There is no conformance suite that returns a finding against the DNSSEC root's own validation layer.
- **P2 is not sealed inside the system.** Ceremony records (videos, audit reports, published scripts) are external artifacts held by IANA and auditors. They are not "cryptographically committed, replayable by anyone" records *inside the DNSSEC system under verification.* The DNSSEC system (DNS with validation) does not contain the ceremony's verification acts as committed records.
- **P4 is not constitutional text.** ICANN bylaws and the KSK Rollover Operational Practice Statement document procedural requirements, but do not contain a Löb-form confession of what the DNSSEC root cannot self-verify (e.g., that the root zone's own unforkedness requires external observation). The residue is handled operationally, not constitutionally.

Three upgrades needed (P1 weak→yes, P2 partial→yes, P4 weak→yes). All fail.

---

**Near-miss #5: MetaCoq (Sozeau et al., POPL 2020 + JAR 2020)**

P1 strong — first verified type checker for the Coq kernel, proven correct in Coq against PCUIC. P4 best-in-class for explicitness — the residue is machine-locatable (literal `Axiom` declarations in the development for fix-guard, ind-guard, strong normalization).

Why it falls short:
- **P2 absent.** No attributable sealed acts. The verification produces proof terms, not governance acts by identified parties.
- **P3 absent.** One-shot verification, frozen. No standing organ re-runs as the foundation changes.

Two upgrades needed (P2 absent→yes, P3 absent→yes). Both fail. P4, while best-in-class for explicitness (machine-locatable axioms), is still axiom-file text, not "constitutional text" with an organ attached — the document's own distinction.

---

**Cross-check of UNVERIFIED items that could change a grade:**

- **F* self-certification** (marked UNVERIFIED in Part III, item 8): Even if F* has self-certified its typechecker, this would at best add another Milawa-like near-miss (P1 strong, P2/P3 absent). It cannot upgrade any row to all four. Not a refutation even if true.

- **CT gossip deployment extent** (marked UNVERIFIED in Part II, item 6): The document says "I do not assert" deployment extent. If gossip were fully deployed with a working organ, it could upgrade CT's P4 from "in normative text" to constitutional-with-organ. But P1 would remain partial (CT can convict via consistency proofs but cannot self-verify unforkedness from inside a single client, and cannot certify a cure). One upgrade at most, insufficient for refutation.

- **Hart page citation** (marked UNVERIFIED for page number): Does not affect any grade.

---

**Paraphrase checks:**

- **Elster retraction paraphrase** (Part IV.V): The document paraphrases *Ulysses Unbound* (2000) as taking apart the precommitment analogy in three moves (societies aren't selves; founding moments aren't sober; enforcement regress — mast has no anchor). This is a fair paraphrase of Elster's well-known argument, though not directly quotable. Even if the paraphrase were inaccurate, it would affect the Elster entry's placement, not §V.6's conjunction claim.

- **Ostrom 1992 paraphrase** (Part IV.X): The document paraphrases "Covenants with and without a Sword" as showing communication alone improves but doesn't hold cooperation, while communication plus endogenous sanctioning sustains it. This is the well-established finding from Ostrom, Walker & Gardner (1992). Accurate. Does not affect §V.6.

---

DRIFT

1. **Residue ledger item 7 — vLEI QVI as monitoring-organ proof.** The document cites "the vLEI's QVI regime is the standing proof that charter-and-fee suffices, without bonds or slashing" for funding a monitoring organ. QVIs (Qualified vLEI Issuers, under GLEIF) are credential *issuers* operating under a charter-and-fee model, but their function is identity credential issuance, not duplicity *monitoring* or *watching* in the CT sense. Using QVIs as proof that charter-and-fee funds a *watcher* function conflates credential issuance with adversarial monitoring. The claim may still hold (charter-and-fee can fund monitors in principle), but the specific vLEI exhibit is weaker than the text suggests. This does not affect §V.6.

2. **Residue ledger item 7 — RFC 6962 gossip "died unfunded" vs. "never needed."** The document states the gossip organ "died unfunded." The more precise characterization is that gossip was *never deployed* — browsers implemented CT enforcement requiring SCTs (Chrome, 2018) and monitors/auditors exist (Cloudflare, Google, Facebook), but the specific client-to-client STH-gossip mechanism specified in RFC 6962 §5 and drafted in draft-ietf-trans-gossip was never implemented at scale. Whether it "died unfunded" or "was never needed" is debatable — split-view attacks were not observed in practice, so the organ may have been judged unnecessary rather than unfunded. This nuance does not affect §V.6 but sharpens the CT near-miss analysis.

3. **Matrix row for Harrison (2006) — P1 grade.** The document grades Harrison's HOL Light self-verification as "~" (partial) for P1. Harrison verified "an imperfect but quite detailed model" of the HOL Light kernel — without definitional mechanisms — and added an explicit axiom I (weak large-cardinal hypothesis). This is arguably stronger than "~" suggests: Harrison achieved genuine internal verification of a substantial kernel fragment, with the residue honestly priced as two axiom deltas. A case could be made for P1 = "yes (modulo named axioms)." However, even at P1 = yes, Harrison still lacks P2, P3, and has only partial P4 (axiom deltas, not constitutional text). Three more upgrades would be needed; none are available. Not a path to refutation.
