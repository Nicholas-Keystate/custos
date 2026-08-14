VERDICT: NOT REFUTED — strongest near-misses, ranked below; none satisfies §V.6’s exact clause: “No prior system holds P1, P2, P3, and P4 jointly — finding-grade evaluation of its own foundation, verification acts sealed attributably inside the system verified, as a standing organ, with the unverifiable residue as constitutional text.”

## Ranked near-misses

### 1. Certificate Transparency — RFC 6962, 2013  
**Exhibit:** Laurie, Langley, Kasper, *Certificate Transparency*, RFC 6962, IETF, June 2013. Specific mechanisms: Signed Certificate Timestamps (SCTs), append-only Merkle logs, signed tree heads, consistency proofs, and the normative gossip requirement. Relevant passages: RFC 6962 §5 (“All clients should gossip with each other, exchanging STHs at least…”) and §7.3 (“Violation of the append-only property is detected by global gossiping…”).

**Attack attempted.** This is the strongest candidate for upgrading the document’s own matrix row. One could argue:

- **P2**: strong — issuance receipts (SCTs) are signed, attributable, and entered into append-only logs.
- **P3**: strong — CT logs and monitors operated continuously at planetary scale.
- **P4**: arguably full — RFC 6962 explicitly confesses that a log cannot prove its own unforkedness to a lone client and that detection requires external gossip.
- **P1**: try to upgrade from partial to full by treating log-consistency proofs and conflicting signed tree heads as finding-grade verdicts against the log’s own foundation.

**Why it fails against the claim’s own grading discipline.** It fails on **P1**, exactly as Part 0 defines it.

Part 0 requires:

> “The system evaluates its own foundation to finding grade: not sentiment, not votes, but replayable verdicts against declared invariants, capable of convicting the foundation and of certifying its cure.”

CT does not do this. CT logs audit certificate authorities and provide cryptographic material by which external observers can detect log misbehavior. But the detection of a forked or split-view log is not an internal, standing, finding-grade evaluation of the log’s own validation foundation. RFC 6962 §7.3 makes the defect explicit: detection depends on **global gossiping**, i.e. comparison across external observers. A single client cannot self-verify unforkedness. There is no CT-internal organ that runs a conformance suite over the log’s own validation rules, convicts the foundation, and then certifies a cure with blast-radius control. Misbehavior is externally evidenced; the log is then distrusted or replaced, not cured under a replayable finding regime.

Even if one grants the aggressive upgrade of **P4** from “in normative text” to full constitutional confession, the conjunction still dies because **P1 remains partial at best**. This is not four properties jointly; it is three plus a partial.

**Failed clause:** P1 — “self-evaluation … to finding grade … capable of convicting the foundation and of certifying its cure.”

---

### 2. DNSSEC root-zone KSK ceremonies — ICANN, 2017–2018 rollover and continuing ceremonies  
**Exhibit:** ICANN DNSSEC Root Zone Key Signing Key ceremonies, especially the 2017–2018 root KSK rollover. Specific mechanisms: hardware security modules (HSMs), smart-card/key-holder procedures, Trusted Community Representatives, published ceremony scripts, witnessed key-generation and backup acts, audit residue, and public recordings. Exact citation to a particular ceremony-script version is **UNVERIFIED** in this pass; the existence of the root KSK ceremony practice and rollover is not in doubt, but I am not asserting a precise document title/version without verification.

**Attack attempted.** The docket names this direction, and it is intuitively dangerous for the claim. The DNSSEC root KSK ceremony looks like a recurring, witnessed, scripted, audited act governing the root of trust. One could try to grade it as:

- **P2**: signed key artifacts, ceremony attestations, audit residue.
- **P3**: recurring ceremonies and rollover cadence.
- **P4**: explicit reliance on human/physical trust and external community representatives.
- **P1**: attempt to treat ceremony validation steps as evaluation of the DNSSEC root foundation.

**Why it fails against the claim’s own grading discipline.** It fails primarily on **P1**, and also does not cleanly achieve **P2** at Part 0 grade.

On **P1**, the root KSK ceremony is a procedural attestation regime for key custody, key generation, backup, and rollover. It is not a replayable, finding-grade conformance evaluation of DNSSEC’s own validation foundation. It does not run declared invariants against the root validation layer in a way capable of convicting that foundation and certifying its cure. If a ceremony step fails, the ceremony can abort or be rescheduled; that is operational control, not a finding stream against the system’s own validation rules.

On **P2**, Part 0 requires:

> “verification runs are themselves attributable, sealed records inside the system under verification: who ran what, against which bytes, in what order — cryptographically committed, replayable by anyone.”

The DNSSEC root KSK regime produces signed DNSSEC artifacts and external ceremony residue: attestations, videos, audits, procedural records. But those are not, at least not on the face of the public ceremony model, sealed verification-run records **inside the DNSSEC system being verified**. They are ceremony and governance artifacts surrounding the root key. They do not make each verification run against the root foundation a cryptographically committed, replayable internal event.

On **P4**, the ceremony regime does appear to confess human and physical trust residue, but whether that confession has the required Löb-shaped constitutional form — “an axiom or an attestation of an external act, never a derived reflection theorem” — is **UNVERIFIED** here and not necessary to decide, because P1 already fails.

**Failed clauses:** P1 — “self-evaluation … to finding grade”; also P2 — “verification runs … sealed records inside the system under verification.”

---

### 3. Sarbanes-Oxley §404 / COSO internal-control regime — 2002 statute; COSO 2013 framework  
**Exhibit:** Sarbanes-Oxley Act of 2002, Pub. L. 107-204, §404, codified at 15 U.S.C. §7262; COSO, *Internal Control — Integrated Framework* (2013), with its explicit “inherent limitations” language. Specific mechanisms: management assessment of internal control over financial reporting, disclosure of material weaknesses, external auditor attestation, remediation/corrective action cycles. Exact COSO page for the inherent-limitations passage is **UNVERIFIED** here, but the concept is load-bearing in the framework.

**Attack attempted.** This is a non-cryptographic governance system that appears to get surprisingly close:

- **P1**: management tests and assesses its own internal-control foundation; material weaknesses can be found; remediation can be reported.
- **P3**: annual SOX 404 cycle plus continuous monitoring in many firms.
- **P4**: COSO explicitly states inherent limitations — human judgment, collusion, management override, reasonable assurance.
- **P2**: try to treat signed SOX certifications, audit opinions, and SEC EDGAR filings as sealed attributable acts.

**Why it fails against the claim’s own grading discipline.** It fails decisively on **P2**, and its **P1** is also below Part 0 grade.

Part 0’s P2 requires cryptographic commitment and replayability by anyone:

> “who ran what, against which bytes, in what order — cryptographically committed, replayable by anyone.”

SOX certifications, audit opinions, and EDGAR filings are legally attributable records, but they are not cryptographic sealed acts in the Part 0 sense. They are not replayable verification runs. They do not internally commit to the exact control tests, inputs, evidence set, order of operations, or evaluation logic in a manner that any third party can replay. They are legal attestations about an assessment, not sealed computational verification acts inside the system being verified.

On **P1**, SOX/COSO assessment is not finding-grade evaluation in the required sense. It is judgmental, sample-based, management-driven, and externally audited. It is not a replayable conformance suite against declared invariants capable of convicting the foundation and certifying cure with bounded blast radius. A material weakness is a finding, but not a replayable computational verdict over the system’s own foundation.

On **P4**, COSO’s inherent limitations are a strong prose confession, but they are not clearly a constitutional text in the Löb-shaped sense required by Part 0. Even if one upgraded P4 charitably, the conjunction still fails because P2 is absent and P1 is degraded.

**Failed clauses:** P2 — “verification acts sealed attributably inside the system verified”; also P1 — “finding-grade evaluation … replayable verdicts against declared invariants.”

---

### 4. Aviation safety management systems — ICAO Annex 19, 2013; FAA 14 CFR Part 5, 2015  
**Exhibit:** ICAO Annex 19, *Safety Management* (2013), and ICAO Doc 9859, *Safety Management Manual*; U.S. FAA Safety Management Systems, 14 CFR Part 5 (final rule effective 2015). Specific mechanisms: safety policy, safety risk management, safety assurance, internal audits, continuous monitoring, corrective action, management of change.

**Attack attempted.** Aviation SMS is a serious near-miss because it institutionalizes internal auditing of the safety system itself:

- **P1**: safety assurance audits evaluate whether the safety system, including audit organs, is functioning.
- **P3**: continuous safety monitoring and recurring audits.
- **P4**: residual risk is formally acknowledged in safety risk management.
- **P2**: try to treat audit reports, hazard reports, and corrective-action records as sealed attributable acts.

**Why it fails against the claim’s own grading discipline.** It fails on **P2** at the required grade, and its **P1** is not finding-grade in the computational/replayable sense.

SMS audit records are attributable in an organizational sense, but they are not cryptographically sealed, replayable records inside a self-certifying system. They are often confidential, procedural, and dependent on human judgment. Part 0’s P2 demands cryptographic commitment and replayability by anyone. SMS does not supply that.

SMS “findings” are audit observations and corrective actions, not replayable verdicts against declared invariants over the system’s own foundation. They can convict a process as deficient, but they do not constitute an executable conformance evaluation of the foundation itself, nor do they certify cure by replay with exact blast-radius control.

Residual risk is documented, but not as a Löb-shaped constitutional confession: “an axiom or an attestation of an external act, never a derived reflection theorem.” It is risk-management prose, not constitutional residue in the required form.

**Failed clauses:** P2 — “sealed records inside the system under verification”; P1 — “finding grade … replayable verdicts”; P4 — required constitutional/Löb form not established.

---

### 5. Tezos and post-2018 self-amending chains — Tezos white paper 2014; mainnet 2018  
**Exhibit:** L.M. Goodman, *Tezos — a self-amending crypto-ledger*, white paper, 2 September 2014; Tezos mainnet launched 17 September 2018; amendment cycle through recorded on-chain votes. Specific mechanism: protocol amendment proposals, exploration/promotion/adoption votes, on-chain sealed acts.

**Attack attempted.** Tezos is the document’s own conceded near-miss. One could attempt to upgrade:

- **P2**: amendment acts are signed, ordered, on-chain.
- **P3**: amendment process is standing and has operated repeatedly.
- **P1**: the chain amends its own protocol.
- **P4**: perhaps some governance documents or community norms confess limits.

**Why it fails against the claim’s own grading discipline.** It fails on **P1** and **P4**.

On **P1**, Tezos amendment is preference aggregation, not finding-grade evaluation. Stake voting can authorize a protocol change; it does not evaluate the candidate validation layer against declared invariants in a way capable of convicting the foundation or certifying a cure. There is no constitutionally bound conformance suite whose verdicts govern amendment by replay.

On **P4**, Tezos does not present the unverifiable residue as constitutional text in the Part 0 sense. It does not write the unforkedness/external-observation residue into its constitution as a first-class Löb-shaped confession. The document’s own grade — “P4 absent” — is not successfully attacked by primary-source evidence here.

I did not find a post-2018 self-amending chain whose amendment process includes pre-adoption conformance evaluation of the candidate protocol to finding grade, with sealed internal verification acts and constitutional residue. Polkadot OpenGov, Cardano Voltaire-style constitutional experiments, and similar systems may provide on-chain governance records, but I did not verify a finding-grade self-evaluation organ in any of them. Any such claim in this pass is **UNVERIFIED** and therefore not asserted.

**Failed clauses:** P1 — “finding-grade evaluation of its own foundation”; P4 — “unverifiable residue as constitutional text.”

---

### 6. Milawa / MetaCoq / mechanized-proof strand — Davis PhD 2009; Myreen & Davis JAR 2015; MetaCoq POPL 2020  
**Exhibit:** J.C. Davis, *A Self-Verifying Theorem Prover*, PhD dissertation, UT Austin, 2009; M.O. Myreen and J. Davis, “The Reflective Milawa Theorem Prover is Sound (Down to the Machine Code that Runs it),” ITP 2014, extended in *Journal of Automated Reasoning* 55 (2015); M. Sozeau et al., “Coq Coq Correct! Verification of Type Checking and Erasure for Coq, in Coq,” PACMPL 4(POPL), Art. 8, 2020.

**Attack attempted.** This strand is dangerous on P1 and P4:

- **P1**: Milawa’s tower admits higher-level checkers by proofs checked below; MetaCoq verifies Coq’s type checker inside Coq modulo axiomatized metatheory.
- **P4**: Harrison-style axiom deltas and MetaCoq’s explicit metatheoretic assumptions are strong confessions.

**Why it fails against the claim’s own grading discipline.** It fails on **P2** and **P3**.

The proof artifacts are not attributable sealed acts inside a live system under verification. They are one-shot evidence files, not records of who ran what, against which bytes, in what order, inside a standing polity log. The systems are not live organs that re-evaluate their foundations as the foundation changes. They are museum-grade achievements, not standing constitutional organs.

**Failed clauses:** P2 — “verification acts sealed attributably inside the system verified”; P3 — “standing organ.”

---

## Rule-1 upgrade attempt: no row yields three successful upgrades

The docket says three upgrades on one matrix row would be a refutation. I attempted that route and failed.

- **Certificate Transparency row**: the only plausible upgrades are P4 from “in normative text” to full confession, and perhaps P1 from partial to full. The P1 upgrade fails because RFC 6962’s own text assigns fork detection to external gossip, not internal finding-grade self-evaluation. No third upgrade available.
- **Tezos row**: P1 might be rhetorically upgraded because Tezos amends itself, but Part 0 requires finding-grade evaluation, not amendment-by-vote. P4 is absent. No three upgrades.
- **TPM/IMA row**: P4 is not upgradeable; the document correctly calls it inverted. The residue is not confessed; it is relocated silently to the vendor/root-of-trust.
- **Reproducible Builds row**: P1 cannot be upgraded. Reproducibility compares builds; it does not evaluate the system’s own validation foundation.
- **sigstore/SLSA row**: P1 cannot be upgraded. Rekor records signing acts; it does not evaluate its own validation layer to finding grade.
- **Milawa/MetaCoq rows**: P2/P3 cannot be upgraded. Proof files are not sealed live acts; one-shot proofs are not standing organs.

No row achieves the required conjunction.

---

## UNVERIFIED items encountered

1. **Exact DNSSEC root KSK ceremony-script citation.** I am not asserting a precise script title, version, or URL as verified in this pass. The ceremony practice is real, but the exact documentary form is UNVERIFIED here.
2. **Extent of production CT gossip deployment.** The status of gossip-related drafts as non-final/expired is consistent with the document, but the exact extent of production gossip deployment is UNVERIFIED here. In any event, even funded external monitoring would not satisfy P1 as an internal self-evaluation organ.
3. **Post-2018 chain conformance organs.** I did not verify any post-Tezos self-amending chain that requires finding-grade conformance evaluation of candidate protocols before adoption. Any assertion that such a chain exists is UNVERIFIED here.

---

## DRIFT

These points do not refute §V.6, but they may matter for document hygiene.

1. **Residue ledger item 7’s “RFC 6962’s gossip organ died unfunded” may be too blunt.** If read as “no funded CT monitoring ever existed,” it is vulnerable: browser root programs, log operators, and third-party CT monitoring have funded some watcher functions since the mid-2010s. The narrower claim — that RFC 6962’s universal gossip organ was not standardized/deployed as a constituted constitutional organ — appears safer. Exact production deployment remains UNVERIFIED here.

2. **vLEI QVI claim needs tightening.** The document uses the vLEI QVI regime as an existence proof of charter-and-fee-funded monitoring. I did not verify that QVIs perform the specific watcher/detection function required by the deterrence-wager entry. If QVIs mainly issue/validate legal-entity credentials rather than monitor duplicity or fork behavior, the analogy may be weaker than stated. This is UNVERIFIED here and does not affect §V.6.

3. **P4 ambiguity: text versus organ.** §V.6 requires residue as “constitutional text,” while V.3 and the residue ledger emphasize organs and attestation regimes. If P4 requires only text, CT becomes more dangerous. If P4 requires constitutional text plus a constituted attestation regime, CT is weaker. The document should state which grade is being claimed. This is not a refutation; it is a grading-discipline clarification.

4. **DNSSEC citation discipline.** If the DNSSEC root KSK ceremony is used as a near-miss in future versions, the companion should cite specific ICANN ceremony documents, RSSAC advisories, or rollover reports rather than relying on general knowledge. The current pass deliberately avoided asserting exact document titles where verification was not available.
