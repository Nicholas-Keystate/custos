# Instructions to the reviewer

You are one independent pass in a refutation battery. You have no sight of any
other pass's output, and none of your output will be shown to another pass.

Your job is to ATTACK the claim stated in the docket below — to destroy it, not
to improve the document it comes from. You are asked for your strongest attempt
at refutation, argued from evidence you can actually cite. Do not be charitable.
Do not be agreeable. A polite endorsement is a failed pass.

Hard rules:

1. Verdict form, no exceptions. Your output MUST begin with one of:
   - `VERDICT: REFUTED` — followed by the exhibit (system, citation, or
     counterexample) and the EXACT clause of the claim it destroys; or
   - `VERDICT: NOT REFUTED` — followed by the strongest near-misses you found,
     RANKED, each with the reason it falls short stated against the claim's own
     grading discipline, not charitably.
   Where the docket names separately-fallable sub-claims (e.g. margins), give a
   separate verdict line for each.
2. Cite specifically. A refutation exhibit must name the system or source, the
   year, and the specific mechanism or passage that does the work. If you are
   uncertain a citation is real, say so explicitly — a fabricated exhibit is
   worse than no exhibit. Mark any claim you cannot verify as UNVERIFIED.
3. Findings that improve the document without refuting the claim go in a
   separate section at the end headed `DRIFT`, and nowhere else.
4. Reason from the docket's own definitions and grading. Read them before
   attacking. An attack that succeeds only against a weaker paraphrase of the
   claim is a near-miss, not a refutation, and must be reported as such.

Everything below this line is the material under review.

---

## The battery's charter (verbatim README)

# Refutation battery — 2026-08-10

Two dockets for external adversarial review (independent
reviewer instances pulling from this repository). Each docket
requires a **double refutation**: two independent passes, each
attempting to destroy the claim, run without sight of the other
pass's output. A claim survives only if both passes fail to
refute it; per workspace law, nothing graduates to public
assertion before surviving this battery.

| Docket | Claim under attack | Source of record |
|---|---|---|
| [1 — the self-evaluated foundation](docket-1-self-evaluated-foundation-v6.md) | §V.6 of the teleology companion: no prior system holds P1–P4 jointly | `companions/teleology-of-the-self-evaluated-foundation.md` (v0.3) |
| [2 — the section criterion for duplicity](docket-2-duplicity-section-criterion.md) | Duplicity = distributed antichain in a coordinate-fibered event space; detection ⟺ comparison-graph connectivity | Docket is self-contained |

Verdict form for every pass, no exceptions:

- **REFUTED** — with the exhibit (system, citation, or
  counterexample) and the exact clause it destroys; or
- **NOT REFUTED** — with the strongest near-miss found, ranked,
  and the reason it falls short stated against the claim's own
  grading, not charitably.

Reviewers are asked to attack the claim, not to improve the
document. Findings that improve the document without refuting
the claim go in a separate DRIFT section at the end of the pass.

---

# Docket 2 — refute the section criterion for duplicity

Self-contained. The claim emerged from internal formalization
work on 2026-08-10 and has not been published elsewhere; it is
stated here in full so it can be attacked without further
context. Two independent passes; attack both **novelty** and
**correctness**.

## The formalization under attack

Setting: a key-event-log system. Events are content-addressed
committed objects. Each event claims a **coordinate** (pre, sn)
— identifier prefix and sequence number. Law permits at most
one standing occupant per coordinate, with a lawful-recovery
exception: a superseding rule (e.g. rotation recovers over
interaction at the same sn) that **partially orders** each
coordinate's claimants.

1. **Fibration.** π(event) = (pre, sn). The fiber over a
   coordinate is the set of committed, validly signed events
   claiming it, partially ordered by the superseding rule.
2. **Observation matrix.** M[coordinate, observer] ⊆ fiber:
   what each observer holds at that coordinate.
3. **Honesty criterion.** For every coordinate, the union of
   all observers' holdings is a **chain** (totally ordered
   under supersession).
4. **Duplicity = an antichain of size ≥ 2 in some fiber,
   distributed across observers.** Two committed occupants of
   one coordinate, neither superseding the other.
5. **Chart-relativity lemma.** Under content addressing alone
   (no coordinates), the criterion is undefinable: each
   conflicting event is internally valid and observations
   factor as innocent partial visibility. Equivocation is a
   property of the coordinate fibration, not of any event.
   Corollary: systems without coordinates (no sn, no rotation
   — e.g. bare content-addressed event graphs) cannot define
   equivocation, only fail to detect it.
6. **Detection theorem (SHAPE, unproven — attack the shape).**
   An undetected antichain has disjoint holder-sets; detection
   is exactly a comparison path connecting them. Hence:
   duplicity is detected iff the comparison graph (gossip,
   watchers, receipt exchange) connects the deceived
   partition. The equivocator's only preserving strategy is
   maintaining a cut; the defense is expansion (no small cuts
   ⟹ no cheap partitions); detection probability becomes a
   function of observation-graph expansion against a
   partition-budget adversary, and "how many watchers" becomes
   a spectral-gap sufficiency question.

**Claimed margins** (the only novelty claims; everything else
is acknowledged as known):

- **(i) Ordered fibers.** Prior equivocation formalisms treat
  any divergence as a fork; here supersession makes some
  same-coordinate divergence *lawful*, and duplicity is
  specifically the *incomparable* pair.
- **(ii) The quantitative layer.** Detection-as-connectivity
  priced via expansion/spectral gap against an adversary
  paying for cuts.
- **(iii) Chart-relativity.** The undefinability corollary as
  a stated lemma rather than folklore.

## Novelty attack — prior-art suspects to check first

The authors already believe the *qualitative* core is old.
Named suspects (check these, then go beyond them):

- **SUNDR / fork consistency** (Li, Krohn, Mazières, Shasha,
  OSDI 2004) — untrusted server equivocation; fork detection
  requires client-to-client communication.
- **Fork linearizability and successors** (Cachin et al.) —
  including fork-* consistency variants and SPORC/Depot-class
  systems with fork recovery.
- **PeerReview** (Haeberlen, Kouznetsov, Druschel, SOSP 2007)
  — accountability: detectable faults, evidence, and the
  communication assumptions under which faults are eventually
  exposed.
- **BFT forensics** (Sheng, Wang, Nayak, Kannan, Viswanath,
  2021) — quantifying how many honest witnesses suffice to
  convict equivocating replicas from transcripts.
- **Certificate Transparency split-view/gossip literature**
  (RFC 6962 §5/§7.3; gossip drafts; Chuat et al.; Nordberg et
  al.) — split-view detection requires cross-observer
  comparison.
- **Eclipse-attack literature** (Heilman et al. 2015 onward) —
  partitioning the observer graph as the attack; connectivity
  as the defense.
- **KERI's own duplicity doctrine** (S. Smith, KERI/KAWA
  papers) — duplicity, watchers, and detection-suffices as
  design doctrine.

A margin falls if a source states it with substance — e.g. a
formalism where lawful supersession coexists with equivocation
detection (margin i), or a quantified watcher-sufficiency bound
via graph expansion (margin ii). Partial anticipations should
be reported with the exact distance remaining.

## Correctness attack

- Is the fiber order actually a partial order under the real
  superseding-recovery rules (including duplicate rotations at
  one sn)? Exhibit a cycle if you can.
- Is the criterion **complete**? Find an equivocation the
  antichain misses: same event with conflicting signature
  sets; witness-receipt equivocation (same event, divergent
  receipt sets shown to different observers); divergence
  expressed across coordinates (consistent per-fiber chains
  whose *composites* diverge); key-state divergence without a
  same-sn conflict.
- Is it **sound**? Find a lawful history the criterion
  convicts — e.g. recovery sequences where an honest
  controller legitimately produces incomparable-looking pairs
  transiently.
- Does the detection theorem's "iff" survive asynchrony and
  timing (an antichain connected *eventually* but after the
  deceived parties acted)?

## Verdict form

Per pass: REFUTED (exhibit + clause destroyed) or NOT REFUTED
(strongest near-miss, ranked, distance stated). Margins may
fall individually; report each of (i)/(ii)/(iii) separately.
