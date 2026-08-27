# Docket 2, v2 — the section criterion for duplicity, repaired per the external battery

Successor to `docket-2-duplicity-section-criterion.md` (v1 stands
as committed; this document supersedes its claims, chain-not-tree).
Every repair below transcribes a convergent prescription from the
sealed external passes (`passes-2026-08-14/harness-report.md`);
none is new invention. Verdict provenance is cited per clause.

## Status of the v1 claims, one line each

| v1 claim | Verdict (battery) | Disposition here |
|---|---|---|
| Margin (i) ordered fibers | FALLS, 5/5 genuine passes | withdrawn as novelty; kept as exposition (§1) |
| Margin (ii) quantitative layer | SURVIVES novelty; wounded on correctness | restated over time-respecting connectivity (§4) |
| Margin (iii) chart-relativity | FALLS as stated | re-scoped (§3) |
| Detection theorem "iff" | FALLS twice | time-indexed restatement (§4) |
| Completeness | FALLS, one-clause gap | chaining premise stated (§2) |
| Soundness | HOLDS, attack struck on facts | unchanged (§2) |

## 1. The formalization (repaired) — with the novelty confession

Setting as in v1: content-addressed committed events, coordinate
π(event) = (pre, sn), fibers partially ordered by the committed
superseding rule.

**Novelty confession (executes the margin-(i) withdrawal).** The
qualitative structure — lawful same-coordinate supersession
coexisting with duplicity-as-incomparable-pair — is KERI's own
superseding-recovery doctrine, verified in the spec of record
(reconciliation rules A0/A1 partially order each coordinate's
claimants; irreconcilable pairs are duplicity). Five external
seats exhibited this independently; the harness confirmed it
against `kswg-keri-specification` spec text. What this document
contributes at the qualitative layer is *notation only*: the
order-theoretic statement of an existing doctrine. The sentence
"prior equivocation formalisms treat any divergence as a fork"
was false and is retracted.

1. **Fibration.** As v1, with the scope repair from the battery:
   the fibration is defined over any **content-derived
   exclusive-resource claim** — a committed reference that at
   most one standing event may lawfully consume (a coordinate
   (pre, sn); a UTXO outpoint; a predecessor link in a
   hash-chained log). The chart-relativity lemma (v1 margin iii)
   is restated in this scope: equivocation is definable exactly
   where such a claim exists, and undefinable in graphs whose
   references carry no exclusivity. (The v1 statement fell to its
   own example class — double-spends and forked chained logs are
   equivocation in bare content-addressed graphs; the exclusivity
   of the consumed reference, not the presence of (pre, sn)
   coordinates, is the load-bearing property. Four seats, two
   convergent counterexample families.)
2. **Observation matrix, time-indexed.** M_t[claim, observer] ⊆
   fiber: what each observer holds at time t. **Evidence
   retention is a law of the model, imported explicitly: M is
   monotone in t** — holdings are never pruned (KERI's own
   first-seen-always-seen property, stated here as a premise
   rather than assumed silently). Comparison messages are
   **evidence-complete**: a comparison carries the sender's full
   holding for the compared claim, superseded events included.
   (Without these two clauses the criterion certifies laundered
   histories; see §5.)
3. **Honesty criterion.** For every exclusive claim, the union of
   all observers' holdings is a chain under the supersession
   order.
4. **Duplicity.** An antichain of size ≥ 2 in some fiber — two
   committed occupants of one exclusive claim, neither
   superseding the other. *(Repair, one word moved: v1's
   "distributed across observers" belonged to undetectedness,
   not to the definition — as written it made a single watcher
   holding both occupants witness no duplicity while clause 3
   flagged exactly that configuration. Duplicity is a property
   of the fiber; distribution is a property of its detection
   state.)*

## 2. Completeness and soundness, restated

**Chaining premise (the v1 gap, now stated).** Events carry
committed predecessor references, and a lawful history's events
at successive positions of one identifier chain contiguously:
the event at (pre, n+1) cites the standing event at (pre, n).
Composite divergence — per-fiber chains whose compositions
diverge — is then a supersession conflict at the first position
where the cited predecessors differ, and the antichain criterion
catches it. (v1 claimed completeness without this premise and
fell to the two-events-one-prior counterexample; two seats
identified the same missing clause, disagreeing only on whether
it was a kill or a repair.)

**Scope confession.** Receipt-set equivocation (same event,
divergent witness-receipt sets shown to different observers) and
suppression/staleness deception (withholding rather than forking)
are real deceptions outside this criterion's object; they are
detected by receipt-completeness and freshness machinery
respectively, not by fiber antichains. Stated as out of scope,
not solved.

**Soundness (held; unchanged).** A lawful history is never
convicted: the superseding rules order every lawful
same-coordinate pair, and pairs the rules refuse to order (two
non-delegated rotations at one sn, under A1) are duplicity by
that refusal — including the crash-retry case. Accidental
duplicity is duplicity. The battery's one soundness attack
required a pair the medium's own rules forbid, and was struck.

## 3. Chart-relativity, re-scoped (formerly margin iii)

The lemma survives in exclusive-resource form: **equivocation is
a property of consumed exclusive references, not of content
addressing** — definable wherever a committed reference admits at
most one lawful consumer, undefinable where references are
non-exclusive citations. The dilemma that killed the v1 form
(read "coordinate" narrowly and the counterexamples land; read it
broadly and the lemma is tautological) is resolved by naming the
property instead of the instance: the claim is now that systems
*lacking any exclusivity discipline* cannot define equivocation —
and that the discipline itself is therefore the constitutive
choice, which is the point the v1 lemma was reaching for.

## 4. The detection claim, time-indexed (formerly the theorem-shape and margin ii)

The static form is dead — twice. (Temporal counterexample:
aggregate comparison connectivity without any time-respecting
path carrying both occupants to a common holder; laundering
counterexample: §5.) The repaired object:

**Detection-by-t.** Duplicity at fiber F is detected by time t
iff there exists a **time-respecting comparison path** under
monotone M and evidence-complete messages that brings two
incomparable occupants of F into one observer's holding by t.
This is a definition-with-consequences, not an "iff" theorem
about static graph connectivity; connectivity of the deceived
partition is necessary but not sufficient, and sufficiency is
exactly what the time-respecting qualifier adds.

**The quantitative margin (survives; restated; research
program).** The adversary's resource is now correctly priced:
maintaining the deceived partition costs **cut-size × duration
against the victims' action latency** — a standing cut is
expensive, a transient cut before victims act may be cheap. The
open program: price detection-by-t on dynamic comparison graphs
(temporal expansion / dynamic spectral methods) against an
adversary paying for cuts over time windows, with the watcher-
sufficiency question restated as a temporal-connectivity budget.
The battery found no prior art stating this object (nearest
misses, converged across five seats: BFT-forensics honest-replica
counting; eclipse-attack connectivity; SybilGuard/SybilLimit
mixing against Sybil admission; Chuat et al. gossip detection
without adversarial pricing) — the one refutation attempt against
its novelty required a fabricated theorem and was struck.

## 5. The laundering bound — what detection cannot promise

The battery's sharpest exhibit, kept as a standing confession:
without monotone M and evidence-complete comparison, an
equivocator can show incomparable events to disjoint groups, then
publish a lawful superseding event to everyone and rely on
pruning to make the union a chain — **full connectivity then
certifies a duplicitous history**. The v1 sentence "the
equivocator's only preserving strategy is maintaining a cut" is
therefore false in general and true exactly under the two
retention clauses of §1.2. Those clauses are the criterion's real
price: detection is a property of *evidence discipline*, not of
connectivity alone. Systems that prune superseded evidence have
chosen undetectability, and the choice is legible in their
retention law. (This is the substrate's first-seen doctrine
arriving as a theorem's premise — the formalization is honest
about what the doctrine was always for.)

## 6. Standing

The v1 verdict form and refutation invitation carry over to this
document. Margins now claimed: the re-scoped relativity lemma
(§3) and the temporal pricing program (§4) — the second wounded-
but-standing, confessed as a program rather than a result.
Everything in §1–§2 is exposition or repair of record, claimed as
neither novel nor final.
