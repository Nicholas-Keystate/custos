VERDICT: REFUTED — **Correctness.** Exhibit: **Temporal Path T (counterexample, 2026)** destroys the clauses **“detection is exactly a comparison path connecting them,” “duplicity is detected iff the comparison graph … connects the deceived partition,”** and **“the equivocator’s only preserving strategy is maintaining a cut.”**

Let incomparable events \(x,y\) occupy one fiber. Initially observer \(A\) holds \(x\), observer \(D\) holds \(y\), and \(B,C\) hold neither. Every comparison performs a complete exchange of current holdings:

1. \(B\) compares with \(C\): neither has anything.
2. \(A\) compares with \(B\): \(B\) learns \(x\).
3. \(C\) compares with \(D\): \(C\) learns \(y\).

The aggregate comparison graph is the connected path \(A-B-C-D\), connecting the two deceived holder sets. Nevertheless, no observer ever holds both \(x\) and \(y\), so the antichain remains undetected. There is no graph cut in the aggregate graph; preservation resulted from temporal ordering and non-repeated communication.

Connectivity becomes sufficient only after adding assumptions absent from the theorem—such as persistent channels, fair repeated exchanges, eventual delivery, and transitive forwarding. Static spectral gap likewise says nothing about dissemination in an adversarial temporal schedule. Thus the stated “iff,” not merely its probability estimate, is false.

VERDICT: REFUTED — **Margin (i), ordered fibers.** Exhibit: **Samuel M. Smith, “Key Event Receipt Infrastructure (KERI),” 2019, arXiv:1907.02143**, especially the **key-event recovery / recovery rotation** mechanism, destroys the novelty clause **“Prior equivocation formalisms treat any divergence as a fork; here supersession makes some same-coordinate divergence lawful, and duplicity is specifically the incomparable pair.”**

KERI’s recovery rules give establishment/recovery rotations precedence over superseded interaction history: a recovery rotation can occupy the sequence position of the first superseded event and invalidate the abandoned continuation. Thus a rotation-versus-interaction divergence at the relevant sequence position is resolved by protocol precedence rather than treated as two permanently symmetric forks. By contrast, competing events without the required precedence—most importantly incompatible competing rotations—constitute duplicity. This is substantively the claimed distinction between comparable, lawfully superseded same-sequence claims and incomparable conflicting claims. Recasting that existing precedence relation as an “ordered fiber” is new notation, not the claimed mechanism.

VERDICT: NOT REFUTED — **Margin (ii), quantitative expansion/spectral-gap layer.**

1. **Giakkoupis, “Tight Bounds for Rumor Spreading in Graphs of a Given Conductance,” 2011, STACS.** This gives quantitative dissemination bounds in terms of graph conductance, closely anticipating the move from “number of watchers” to graph expansion. It falls short under the docket’s grading because it analyzes rumor spreading, not equivocation detection against an adversary explicitly paying a partition/cut budget.

2. **Sheng, Wang, Nayak, Kannan, and Viswanath, “BFT Protocol Forensics,” 2021.** Its forensic-support thresholds quantify how much honest transcript evidence is sufficient to identify Byzantine faults. It falls short because the bounds concern witness/transcript thresholds rather than spectral gap, conductance, or minimum cuts in a watcher comparison graph.

3. **Heilman et al., “Eclipse Attacks on Bitcoin’s Peer-to-Peer Network,” 2015, USENIX Security.** The attack explicitly preserves deception by isolating a victim’s network view, and defenses increase independent connectivity. It falls short because it does not supply the claimed expansion-based detection probability or a partition-budget optimization.

These are strong ingredients, but none verified here states the full claimed combination with substance.

VERDICT: NOT REFUTED — **Margin (iii), chart-relativity as a stated lemma.**

1. **Li, Krohn, Mazières, and Shasha, SUNDR, 2004, OSDI.** SUNDR shows that an equivocating server can maintain innocent-looking forked views until clients compare histories. This strongly anticipates the claim that equivocation is relational rather than locally evident in either view. It falls short because SUNDR still has operation histories and object-level consistency semantics; it does not prove that equivocation is undefinable in a genuinely coordinate-free content-addressed system.

2. **Bitcoin, Nakamoto, 2008.** Bitcoin has no KERI-style \((pre,sn)\) coordinates or rotation mechanism, yet two individually signed transactions spending the same UTXO define a double-spend conflict. This attacks any weaker reading equating “no sequence number” with “no equivocation.” It falls short against the exact claim because the consumed outpoint itself functions as a conflict coordinate: both transactions claim exclusive use of the same resource.

3. **RFC 6962, Certificate Transparency, 2013, §§4.4, 5, and 7.3.** Consistency proofs distinguish lawful append-only growth from incompatible log views, while split views require cross-client evidence. It falls short because tree size/log identity provide an explicit chart against which incompatible claims are compared; it is not a coordinate-free undefinability result.

I could not verify prior art that expressly states the docket’s exact undefinability corollary as a lemma.
