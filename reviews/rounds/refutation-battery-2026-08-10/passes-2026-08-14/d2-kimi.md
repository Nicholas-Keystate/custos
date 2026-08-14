VERDICT: REFUTED — core claim (clause 6, detection-theorem shape): the "supersession-laundering" history below destroys the clause "The equivocator's only preserving strategy is maintaining a cut" and the sufficiency direction of "duplicity is detected iff the comparison graph … connects the deceived partition."

VERDICT: REFUTED — margin (i): KERI's own published recovery rule and duplicity doctrine state lawful same-coordinate supersession coexisting with equivocation detection.

VERDICT: NOT REFUTED — margin (ii): ranked near-misses in §4.

VERDICT: REFUTED — margin (iii): the undefinability corollary is false as stated (hash-chained logs) or vacuous; either reading voids the margin.

---

## 1. Exhibit A (core): supersession-laundering

The docket's own superseding rule — "rotation recovers over interaction at the same sn" — gives the equivocator a strategy that is not cut-maintenance:

1. Controller creates ixn **I** at (pre, n), validly signed; shows it to observer group A only.
2. Controller creates ixn **I′** ≠ I at (pre, n); shows it to group B only. (Antichain {I, I′} exists; a cut is needed only from this moment.)
3. Controller creates rot **R** at (pre, n) — lawful recovery, validly signed, pre-rotation commitment satisfied, chained to the same predecessor — and publishes R to *everyone*, no cut.
4. Every observer lawfully supersedes its ixn with R. Standing occupant at (pre, n) is R for all.

**Clause destroyed (a):** "The equivocator's only preserving strategy is maintaining a cut." False as stated: the adversary needs a cut only for the window between first disclosure and R's publication, which it controls and can size to the victims' action latency. Thereafter, permanent evasion with *full* connectivity.

**Clause destroyed (b):** "detection is exactly a comparison path connecting them" (⟸). Two readings of M, both lose:

- *M = current holdings* (the text's present tense: "what each observer holds"). Nothing in clauses 1–6 forbids pruning a lawfully superseded, non-standing event. If A and B prune I, I′ on accepting R, the union of holdings is {R} — a chain — and no connected comparison graph of any expansion can ever detect {I, I′}: the evidence no longer exists in anyone's holdings. The honesty criterion (clause 3) certifies a duplicitous history.
- *M = ever-held* (the repair reading). Detection still fails unless the comparison protocol *transmits superseded events*. Standing-state comparison — exchange of current occupants/receipts, which is what efficient gossip and watcher protocols actually exchange — shows A and B in agreement on R. Clause 6 nowhere requires evidence-complete gossip, and margin (i) itself argues against it: superseded events are lawfully non-standing, so a protocol that carries them forever is precisely what the ordered-fiber design is meant to make unnecessary.

Note the mechanism: margin (i)'s feature *creates* the attack on clause 6. Lawful supersession is an evidence-laundering primitive. This also wounds margin (ii)'s correctness (charged here, not to its novelty verdict): the adversary's budget is cut-size × *duration*, and "no small cuts ⟹ no cheap partitions" prices only standing cuts. Detection probability is a race against victim action latency, not against a maintained partition.

**Repair distance:** (1) an evidence-retention law making M monotone; (2) a stated requirement that comparison messages carry full fiber contents including superseded and duplicitous events; (3) temporal indexing of the iff. With all three, the shape is restorable — which is why this refutes the claim *as stated*, not the research program. If the grader rules M was always intended monotone and comparison always evidence-complete, this degrades to a near-miss at distance "three unstated premises"; I see no textual basis for that ruling.

## 2. Secondary defect: clause 4 is internally inconsistent

Sentence 1: "Duplicity = an antichain … *distributed across observers*." Sentence 2: "Two committed occupants of one coordinate, neither superseding the other." Under sentence 1, a single watcher holding both rotations R₁, R₂ at (pre, n) witnesses *no duplicity* — yet clause 3's union test flags exactly that configuration (union not a chain). Clauses 3 and 4 give contradictory classifications of the same configuration; clause 4 conflates duplicity with *undetected* duplicity. Repair distance: one line (move "distributed" into the undetectedness condition). Reported, not pressed as the kill.

## 3. Exhibit B (margin i): KERI's published doctrine

Margin (i) asserts: "Prior equivocation formalisms treat any divergence as a fork," and claims as new that lawful supersession coexists with duplicity = the incomparable pair. Counterexhibit: **S. M. Smith, KERI white paper / KERI specification and KAWA (KERI Agreement Algorithm for Witness Agreement), 2019–2024**. KERI's stated validation rules: a rotation event at sequence number n *recovers over* (supersedes) an interaction event at n — lawful same-coordinate divergence — while same-ilk conflicting events at (pre, sn) are duplicity, detected via first-seen policy and watcher/witness agreement. That is lawful supersession coexisting with equivocation detection, stated with substance (specified, implemented in keripy). The docket's own illustrative rule ("rotation recovers over interaction at the same sn") is quoted from this source, and the docket's grading says a margin falls if "a source states it with substance." Exact section/page loci: UNVERIFIED; existence of the recovery rule and first-seen duplicity doctrine: high confidence.

Corroboration (partial): **SPORC** (Feldman, Zeller, Freedman, Felten, OSDI 2010) and **Depot** (Mahajan et al., OSDI 2010) detect same-(client, seqno) forks *and* lawfully absorb them via join operations dominating both branches — supersession coexisting with fork detection, though the forked pair itself stays flagged (distance from (i): same-coordinate divergence never becomes lawful; KERI closes that gap).

Distance remaining for (i): the general poset/antichain *notation*. If the margin is read as claiming only the notation, it is unkillable and substance-free; read as claiming the substance, it is KERI's doctrine.

## 4. Margin (ii): NOT REFUTED — near-misses, ranked

Grading discipline: the margin falls to "a quantified watcher-sufficiency bound via graph expansion" or equivalent substance.

1. **SybilGuard / SybilLimit** (Yu, Kaminsky, Gibbons, Flaxman, SIGCOMM 2006; Yu, Gibbons, Kaminsky, Xiao, IEEE S&P 2008). The pricing *structure* is present with substance: adversary pays per attack edge (cut budget); fast mixing of the honest region bounds the adversary's yield per cut edge. Falls short: the deliverable is Sybil-identity admission, not equivocation detection; no antichain, no comparison-path iff, no watcher-sufficiency statement. Distance: the entire detection semantics.
2. **Chuat, Szalachowski, Perrig, Laurie, Messeri, "Efficient Gossip Protocols for Verifying the Consistency of Certificate Logs," IPCCC 2015** (authors/venue high-confidence; title UNVERIFIED to the word). Quantified gossip-based split-view detection: detection latency/probability vs gossip parameters — literally detection-as-connectivity, quantified. Falls short: epidemic-dissemination analysis, not expansion/spectral gap; no partition-budget adversary choosing cuts. Distance: the pricing functional.
3. **BFT forensics** (Sheng, Wang, Nayak, Kannan, Viswanath, CCS 2021). Quantified sufficiency: how many honest transcripts convict equivocating replicas, per protocol. Falls short: quorum-count combinatorics; no observer graph, no cuts, no expansion. Distance: graph topology entirely absent.
4. **Eclipse/partition attacks** (Heilman, Kendler, Zohar, Goldberg, USENIX Security 2015; Marcus, Heilman, Goldberg 2018; Tran et al., IEEE S&P 2020). Partition-as-attack, connectivity-as-defense. Falls short: no equivocation semantics, no quantified detection-vs-expansion bound. Distance: the whole quantitative theorem.
5. **Fraud/data-availability proofs** (Al-Bassam, Sønnino, Buterin, 2018). "How many light clients suffice" under network assumptions. Falls short: count-based sufficiency assuming connectivity; no cut budget, no spectral gap. (Distant sixth: King–Saia, PODC 2010, use samplers/expanders against adaptive adversaries — for BA bit complexity, not detection.)

No verifiable source states the composition: detection probability as a function of observation-graph expansion against an adversary paying per cut edge, with watcher sufficiency as a spectral-gap question. (ii) survives on novelty; its correctness is separately damaged by Exhibit A.

## 5. Exhibit C (margin iii): the corollary is false or vacuous

Clause destroyed: "systems without coordinates (no sn, no rotation — e.g. bare content-addressed event graphs) cannot define equivocation." Counterexample: **hash-chained signed logs** — Schneier & Kelsey, "Secure Audit Logs to Support Computer Forensics," ACM TISSEC 1999; equally, a signed git branch. Entries are content-addressed, chained by predecessor digest; no sequence numbers, no rotation. Two signed entries extending the same predecessor constitute equivocation, definable and detectable from content alone: the predecessor digest *is* the slot-claim. An "event graph" minimally has edges; with edges, same-parent pairs are definable. The corollary's own example class therefore contains systems that define equivocation. Escape hatch: if "bare" means edgeless blobs, the lemma reduces to "with no equivalence structure, no conflict relation is definable" — a tautology whose statement-as-lemma carries no substance, voiding the margin the other way. Prior-art near-misses (insufficient alone): PBFT/Tendermint/Casper define equivocation only coordinate-wise, and SUNDR (Li, Krohn, Mazières, Shasha, OSDI 2004) states that fork detection requires cross-client comparison — the lemma's substance as embedded folklore, which the docket concedes; none states the undefinability corollary, so if the lemma is read vacuously, "first to state a tautology" is the only residue.

## 6. Other attacks prosecuted, with dispositions

- **Cycle hunt (fiber order):** conceded. Under the actual rule (rot > ixn at same sn; same-ilk pairs incomparable), the fiber is a two-level poset; no cycle constructible. Caveat: if any deployment folds KERI's observer-relative *first-seen* tie-break into the order, the fiber order becomes observer-relative and clause 3's union test is ill-defined (see DRIFT).
- **Completeness via cross-coordinate composites:** conceded, via first-divergence over hash-chaining (note: predecessor commitment is *not stated* in clause 1; without it, divergence still reduces to antichain-or-staleness). Residual gap: suppression/staleness deception (withholding a superseding R from a victim) yields divergent key-state beliefs with a chain union — but staleness is excluded from equivocation by the docket's definition, matching SUNDR/fork-linearizability scope. Near-miss, distance: requires redefining equivocation to include non-disclosure.
- **Soundness via crash-retry double rotation:** near-miss. An honest controller that rotates, crashes, restores from backup, and re-rotates with fresh next-key entropy produces a convicted antichain at one sn. But the docket's law permits one standing occupant; the second rotation is unlawful (KERI doctrine agrees: accidental duplicity is duplicity). The criterion is sound w.r.t. the law; only the *label* "honesty criterion" fails. Distance: one terminological repair.
- **Asynchrony/timing of the iff:** near-miss. The iff is tenseless; under asynchrony only an eventual, time-indexed version survives, and "detection probability" is undefined absent a stated gossip process and adversary model. Distance: restatement; the docket flags the theorem as unproven shape, so this is damage it half-concedes.
- **Nominal vs honest expansion:** near-miss. If the adversary controls relay *vertices* (Sybils), connectivity of the nominal comparison graph does not yield detection; expansion must be measured on the honest-induced subgraph, which is unobservable. Distance: requires a vertex-adversary model the docket omits.

## DRIFT

Repairs that would strengthen the document without refuting its intent: (1) state M as monotone (ever-held) or add an explicit evidence-retention law for superseded/duplicitous events; (2) specify comparison-message content (full fiber vs standing state) — clause 6's ⟸ depends on it; (3) time-index the detection iff and define the probability space (gossip process, adversary's temporal budget); (4) fix clause 4 by relocating "distributed across observers" into the undetectedness condition; (5) state the predecessor-chaining assumption in clause 1; (6) replace "honesty criterion" with "non-duplicity criterion"; (7) bar first-seen tie-breaks from the fiber order or make the order explicitly per-observer; (8) address vertex adversaries before pricing expansion.
