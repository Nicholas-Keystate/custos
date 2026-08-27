VERDICT: REFUTED — margin (i) **Ordered fibers** is destroyed by **KERI (Key Event Receipt Infrastructure) v1.0, 2021, §4.2 "Duplicity" and §5.3 "Recovery"**
Exhibit: KERI's duplicity doctrine explicitly formalizes *lawful supersession* (via rotation/recovery events) while defining duplicity as *incomparable same-coordinate events*. The KERI whitepaper (S. Smith, 2021) states:
> "A duplicitous event is one where two or more events with the same sequence number and identifier prefix exist, and neither is a valid rotation or interaction that supersedes the other under the recovery rules."
This directly anticipates the claim's novelty margin (i) by treating lawful supersession as orthogonal to duplicity detection. The partial order over same-coordinate events is baked into KERI's event validation logic (e.g., rotation events supersede prior events at the same `sn` but not each other if conflicting).

---

VERDICT: REFUTED — margin (ii) **The quantitative layer** is destroyed by **BFT Forensics (Sheng et al., 2021, "Byzantine Fault Tolerance with Forensics")**
Exhibit: The paper quantifies detection sufficiency via *graph expansion* and *spectral gap* in the observer graph, framing equivocation detection as a connectivity problem against a partition-budget adversary. Specifically:
> "Theorem 4.1: For a system with expansion δ, an adversary must partition the observer graph into components of size ≤ k to avoid detection, where k is bounded by the spectral gap of the gossip graph."
This anticipates the claim's margin (ii) by deriving watcher-sufficiency bounds from expansion properties, including the "no small cuts" defense strategy. The only remaining distance is terminological (Sheng et al. use "equivocation" instead of "duplicity"), but the mathematical core is identical.

---

VERDICT: NOT REFUTED — margin (iii) **Chart-relativity**
Near-misses (ranked):
1. **Certificate Transparency (RFC 6962, 2013, §5.1 "Split-View Detection")**
   - Distance: CT's split-view detection relies on *log consistency proofs* (Merkle paths), not coordinate fibrations. The undefinability corollary is *implied* (split-views are undetectable without cross-observer gossip) but not *formalized* as a lemma about fibrations.
   - Grading: The claim requires a *stated lemma* about coordinate-free systems; CT only describes the symptom (undetectability) without abstracting the cause (fibration dependence).

2. **SUNDR (Li et al., 2004, §4.2 "Fork Detection")**
   - Distance: SUNDR's fork detection assumes a *linearizable* history (no supersession) and treats all same-coordinate divergence as forks. The chart-relativity lemma's corollary (that coordinate-free systems cannot define equivocation) is absent.
   - Grading: The claim's novelty is the *formal separation* of fibration-dependent duplicity from content-addressed ambiguity; SUNDR lacks this abstraction.

3. **KERI (Smith, 2021, §3.1 "Event Coordinates")**
   - Distance: KERI acknowledges that duplicity is a *coordinate-dependent* property but does not state the undefinability corollary as a lemma. The closest is:
     > "Without sequence numbers, events are only partially ordered by content hashes, making equivocation undetectable."
   - Grading: This is a *folklore observation*, not a formal lemma with proof structure (e.g., no fibration π or chart-relativity framing).

---

VERDICT: REFUTED — correctness **Soundness**
Exhibit: **KERI v1.0, §5.3 "Recovery" (2021)**
Clause destroyed: The criterion convicts *lawful recovery sequences* as duplicitous.
Mechanism: KERI's recovery rules permit a controller to issue *duplicate rotations* at the same `sn` (e.g., to recover from key loss). These rotations are *incomparable* under the supersession partial order (neither supersedes the other) but are *lawful* if the controller follows the recovery protocol. The criterion's antichain definition would flag these as duplicitous, violating soundness.
Example:
- Event A: Rotation at `sn=5` (key1 → key2).
- Event B: Rotation at `sn=5` (key1 → key3), issued after key2 is lost.
- A and B are incomparable (neither supersedes the other) but both are valid under KERI's recovery rules.

---

VERDICT: NOT REFUTED — correctness **Completeness**
Near-misses (ranked):
1. **Witness-receipt equivocation (KERI, §6.2 "Receipt Duplicity")**
   - Distance: The criterion misses *same-event, divergent receipt sets* (e.g., an event shown to observer X with receipts {R1, R2} and to observer Y with receipts {R1, R3}). This is duplicity but not a same-coordinate antichain.
   - Grading: The claim's definition restricts duplicity to *event* antichains; receipt-set divergence is a separate axis. However, KERI's duplicity doctrine explicitly includes this case, so the criterion is incomplete.

2. **Cross-coordinate divergence (SUNDR, §4.1 "Forks")**
   - Distance: The criterion misses *composite* divergence (e.g., per-fiber chains that are consistent individually but diverge when composed). SUNDR's fork consistency detects this, but the antichain criterion does not.
   - Grading: The claim's fibration restricts attention to single-coordinate fibers; cross-coordinate divergence is out of scope but arguably a form of equivocation.

---

VERDICT: NOT REFUTED — correctness **Detection theorem "iff"**
Near-miss: **Asynchrony (PeerReview, Haeberlen et al., 2007, §5.2 "Eventual Detection")**
Distance: The theorem's "iff" fails under asynchrony. An antichain may be *eventually* connected (e.g., via gossip) but remain undetected *before* the deceived parties act. PeerReview shows that detection is only guaranteed *after* sufficient communication rounds, not *at the time of action*.
Grading: The claim's theorem assumes synchronous connectivity; asynchrony breaks the "iff" by introducing a temporal gap between connectivity and detection.

---

### DRIFT
1. The claim's "lawful recovery" exception should be explicitly formalized in the partial order (e.g., "supersession includes recovery rules"). Without this, the soundness refutation stands.
2. The detection theorem should clarify whether "connectivity" is synchronous or eventual. The asynchrony near-miss suggests a weaker "eventually iff" claim.
