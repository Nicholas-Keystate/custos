VERDICT: REFUTED — Margin (i). Exhibit: KERI (S. M. Smith, Key Event Receipt Infrastructure whitepaper/specification, 2021; exact section/passage from memory, so pinpoint citation UNVERIFIED). KERI’s same-prefix/same-sequence-number “supercession”/lawful-recovery mechanism allows an establishment event (rotation) to supersede a non-establishment event (interaction) at the same sequence number, while treating only conflicting same-coordinate events not related by that rule as duplicity. This destroys the exact clause: “(i) Ordered fibers. Prior equivocation formalisms treat any divergence as a fork; here supersession makes some same-coordinate divergence lawful, and duplicity is specifically the incomparable pair.” KERI already contains the substance: lawful same-coordinate supersession coexisting with a duplicity doctrine based on unresolved same-coordinate conflict.

VERDICT: REFUTED — Correctness of §6 detection clause. Counterexample T1 (asynchrony / coarse comparison graph) destroys the exact clause: “duplicity is detected iff the comparison graph (gossip, watchers, receipt exchange) connects the deceived partition.” Let coordinate c have incomparable committed occupants x and y. Observer A holds only x; observer B holds only y; observer C is an intermediate comparator. If the comparison graph is a potential or partially specified communication graph, edges A–C and C–B can exist while messages carrying x and y are delayed, lost, or restricted to other coordinates. The graph connects the deceived partition, but no honest observer obtains both x and y before acting, or ever if losses persist. If instead the graph is defined so that an edge means “full, coordinate-specific evidence exchange sufficient to transmit the conflicting occupants,” then the “iff” is tautological and does not establish the claimed asynchronous detection theorem; it merely restates that detection requires completed evidence transfer. As written, connectivity is not sufficient for detection.

VERDICT: NOT REFUTED — Margin (ii). Strongest near-misses, ranked:

1. SybilGuard (Yu, Kaminsky, Gibbons, Abraham, 2006). It uses fast-mixing random walks on a social graph, explicitly relying on conductance/spectral gap, and bounds malicious acceptance against an adversary paying a limited number of “attack edges” into the honest region. It falls short of margin (ii) because it prices Sybil-identity acceptance, not detection of a same-coordinate antichain or watcher-sufficiency for equivocating claims. There is no duplicity fiber, no conflicting event antichain, and no comparison-graph theorem for equivocation detection.

2. Eclipse-attack literature, especially Heilman et al., 2015, Eclipse Attacks on Bitcoin’s peer-to-peer network. It identifies observer-graph partitioning as the attack and connectivity/degree increases as defense. It falls short because it is qualitative and system-specific: no spectral-gap sufficiency bound, no watcher-count threshold, and no formal detection probability against a cut-budget adversary for duplicity.

3. PeerReview (Haeberlen, Kouznetsov, Druschel, 2007) and BFT forensics (Sheng et al., 2021; full bibliographic details as named by docket, UNVERIFIED). These give witness/reviewer/forensic sufficiency ideas and eventual exposure or conviction thresholds. They fall short because their quantitative or threshold structure is protocol/quorum/replica-based, not observation-graph expansion or spectral gap against paid cuts. They do not state detection-as-connectivity for a distributed antichain.

4. Certificate Transparency split-view/gossip material (RFC 6962, 2013; later gossip drafts, exact draft details UNVERIFIED). It establishes that split-view misbehavior requires cross-observer comparison/monitor gossip. It falls short because it does not provide an expansion/spectral-gap pricing of detection probability or a watcher-sufficiency bound against a partition-budget adversary.

VERDICT: NOT REFUTED — Margin (iii). Strongest near-misses, ranked:

1. SUNDR / fork consistency (Li, Krohn, Mazières, Shasha, OSDI 2004). It shows that untrusted-server equivocation/forks become detectable only through client-to-client comparison and that isolated views can masquerade as partial visibility. It falls short because SUNDR still defines forks using client/server state and sequence/version coordinates; it does not state the docket’s stronger coordinate-free undefinability lemma: that bare content-addressed event graphs cannot define equivocation at all.

2. Certificate Transparency split-view detection (RFC 6962, 2013; monitor/gossip folklore). It recognizes that a single observer cannot distinguish malicious split-view from innocent partial visibility without comparison. It falls short because CT logs have coordinates (log identity, tree size, signed tree heads) and the literature frames detection operationally, not as a lemma that the criterion is undefinable absent coordinates.

3. Content-addressed Merkle-DAG/version-control branching folklore (e.g., Git, 2005 onward). Branches are internally valid content-addressed histories; conflict appears only through names/refs/coordination points. It falls short because it is folklore without a formal equivocation lemma, proof, or corollary, and it does not treat equivocation as a security detection criterion.

VERDICT: NOT REFUTED — Correctness of the fiber-order / soundness core. Strongest near-misses, ranked:

1. Duplicate rotations at one sn. If a real recovery rule allowed two same-sn rotations to be lawful but mutually unsuperseded, §4 would convict an honest history. It falls short because the docket stipulates that the superseding rule partially orders claimants; absent a concrete lawful rule that makes two same-sn rotations comparable without duplicity, the example is either ordinary duplicity or an incomplete specification, not a demonstrated false positive.

2. Transient recovery pairs. A rotation/interaction pair at the same sn can look conflicting before recovery metadata is known. It falls short because once the superseding rule is applied, the pair is comparable; the criterion’s honesty test is over the union of committed valid claimants, not over an observer’s temporary ignorance. No cycle in the fiber order was exhibited.

DRIFT

- The detection theorem should be time-indexed. Define a comparison graph G_t whose edges are actual, coordinate-specific evidence exchanges completed by time t, and state detection-by-t separately from eventual exposure. Distinguish potential communication topology, actual comparison edges, and evidence-flooding semantics.

- The formalization should state whether signatures, witness receipts, and quorum bundles are part of the content-addressed event object or separate proof objects. If separate, either add proof-bundle fibers or specify a cross-coordinate composition rule; otherwise receipt-set divergence is outside the criterion.

- The supersession relation needs an explicit antisymmetry/transitivity argument, including duplicate rotations, recovery races, and any rule that depends on later receipts or witness thresholds.

- Margin (i) should either cite KERI’s supercession/duplicity doctrine and narrow the claimed delta, or withdraw the “prior formalisms treat any divergence as a fork” formulation.

- Margin (ii), if retained, should explicitly differentiate the proposed expansion/spectral-gap account from SybilGuard-style mixing bounds and eclipse/connectivity literature, ideally by proving a watcher-sufficiency theorem tied to antichain detection rather than identity limiting or generic partition resistance.
