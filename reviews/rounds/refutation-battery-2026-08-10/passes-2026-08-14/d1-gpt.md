VERDICT: NOT REFUTED — No pre-2026 system I can verify satisfies the full conjunction at Part 0’s grades. The strongest near-misses, ranked:

1. **Microsoft Confidential Consortium Framework (CCF) — strongest near-miss.**  
   **Sources:** Microsoft Research, *CCF: A Framework for Building Confidential Verifiable Replicated Services* (2019 technical report); Microsoft CCF documentation, “Governance,” “Constitution,” and “Transaction Receipts” (2023–2024).  
   **Mechanism:** CCF stores signed governance proposals and ballots in its replicated Merkle ledger; its JavaScript “constitution” contains proposal-validation and application rules and can itself be replaced through governance. Ledger transactions can receive cryptographic receipts, and approved code identities are tied to hardware-attested measurements. This gives a serious P2/P3 combination and a replayable rule-governed check over proposed changes to constitutional machinery.  
   **Why it falls short:**  
   - Against **“evaluates its own foundation to finding grade … capable of convicting the foundation and of certifying its cure”**, CCF validates *candidate governance actions* under the current constitution. I found no primary-source mechanism that periodically tests the currently seated constitution or CCF implementation against declared invariants, emits a finding that the existing foundation is defective, and then certifies a repair. It is admission control, not the docket’s stronger diagnostic loop.  
   - Against **“the unverifiable residue as constitutional text”**, CCF documents trust in enclave attestation, hardware, service operators, recovery members, and ledger availability, but I could not verify that those limits are represented *in the service constitution itself* as named unverifiable axioms or external-attestation obligations. Treating approved code measurements or recovery thresholds as P4 would weaken “confessed residue” into ordinary configuration.  
   **Status:** The claim that current CCF constitutions can encode stronger invariant tests is plausible but **UNVERIFIED** and still would not establish that a deployed pre-2026 system actually did so.

2. **Hyperledger Fabric channel configuration and MSP governance.**  
   **Sources:** Hyperledger Fabric documentation, “Channel Configuration (configtx)” and “Membership Service Provider (MSP)” (Fabric 1.4 documentation, 2019; Fabric 2.2 documentation, 2020).  
   **Mechanism:** A configuration update carries a read set, write set, and signatures. Peers compute the configuration delta and check authorization under the existing `mod_policy`; accepted updates alter the very policies and MSP trust roots used for later validation. Channel blocks preserve ordered configuration transactions, while MSP configuration explicitly contains root and intermediate certificates. This is substantially stronger than Tezos-style preference aggregation: there is executable conformance and authorization checking over changes to the validation foundation.  
   **Why it falls short:**  
   - Against **P1’s finding grade**, Fabric can reject an unauthorized or structurally invalid *proposed update*, but it does not thereby inspect and convict the already-installed validation foundation. A human or external tool must first diagnose a bad policy or MSP configuration.  
   - Against **“who ran what … sealed attributably”**, the submitted signatures identify proposers and authorizers, not each peer execution of the validation procedure. Invalid ordinary transactions can remain marked invalid in a block, but I could not verify an equivalent attributable, cryptographically sealed record of every failed configuration-validation run.  
   - MSP roots are first-class trust anchors, but the documentation does not characterize their unverifiability as constitutional residue in P4’s Löbian sense. A configured root certificate is not by itself a confession that its external issuance or custody cannot be derived internally.

3. **DNSSEC root KSK ceremonies.**  
   **Sources:** ICANN, *DNSSEC Practice Statement for the Root Zone KSK Operator*, version 2.1 (2016) and version 2.2 (2017); ICANN, published Root KSK Ceremony Scripts and ceremony materials (recurring since 2010); ICANN annual SysTrust audit reports.  
   **Mechanism:** Root-key operations follow published scripts, use designated Crypto Officers and Trusted Community Representatives, require witnessed quorum-controlled physical steps, and generate signed logs, audit materials, and video records. The ceremonies recur as a standing operational organ, and the Practice Statement expressly allocates physical, personnel, hardware-security-module, and external-audit dependencies.  
   **Why it falls short:**  
   - Against **“replayable verdicts against declared invariants”**, a later observer can replay the video and documentary evidence only as an evidentiary review, not cryptographically replay the physical acts or regenerate a deterministic verdict from committed inputs.  
   - Against **“records inside the system under verification”**, ceremony records are published by ICANN and auditors; they are not DNSSEC records authenticated and ordered by the root-zone validation state whose foundation is being evaluated. Publishing them on a DNSSEC-protected domain would still not make them acts inside the root DNSSEC state machine.  
   - Audits assess compliance with ceremony controls; they do not establish a conformance suite capable of convicting the DNSSEC validation foundation itself and certifying its cure.

4. **Cardano on-chain governance and constitution (CIP-1694 era).**  
   **Sources:** Cardano Improvement Proposal CIP-1694, “A First Step Towards On-Chain Decentralized Governance” (2022–2023); Cardano interim constitutional materials and governance deployment associated with the Chang/Plomin upgrades (2024–2025).  
   **Mechanism:** Governance actions and attributable votes are recorded on-chain; protocol-parameter and hard-fork actions alter the system’s validation foundation; a Constitutional Committee votes on whether actions conform to the constitution; protocol parameter guardrails can impose executable bounds.  
   **Why it falls short:**  
   - Committee determinations are signed constitutional judgments but not **“replayable verdicts against declared invariants”** where they depend on interpretation and voting. Executable parameter bounds cover only a subset of constitutional review.  
   - I found no verified pre-2026 mechanism that runs finding-grade conformance over the currently executing ledger foundation, convicts that implementation, and certifies a cure.  
   - Any claim that the constitution names chain identity, social consensus, implementation correctness, and observer availability as P4-grade residue is **UNVERIFIED**.

5. **Certificate Transparency after RFC 6962.**  
   **Sources:** Laurie, Langley, and Kasper, RFC 6962 (2013), §§5 and 7.3; Laurie et al., RFC 9162, *Certificate Transparency Version 2.0* (2021); Google Chrome, *Certificate Transparency Log Policy* (2022–2024 revisions).  
   **Mechanism:** SCTs, signed tree heads, inclusion proofs, and consistency proofs are cryptographically replayable; monitors continuously inspect certificates; browser log policies can disqualify logs for noncompliance. RFC 6962 expressly identifies cross-observer comparison as necessary to expose split views.  
   **Why it falls short:**  
   - CT evaluates CAs and append-only log behavior, not the CT validation foundation itself. Consistency proofs establish a relation between tree states under fixed rules; they do not test whether those rules or their implementation are defective.  
   - Browser log qualification and disqualification are external governance acts, not acts sealed inside the particular log being evaluated.  
   - RFC 6962’s gossip language is a protocol requirement and security limitation, but it does not constitute the residue as an article of a self-governing system with an attached standing organ. RFC 9162 does not close that gap.

None of these systems clears the two hardest clauses simultaneously: **current-foundation diagnosis rather than candidate-update validation**, and **the unverifiable remainder represented as constitutional text rather than merely documented trust assumptions**. Consequently, no verified exhibit destroys §V.6’s conjunction claim.
