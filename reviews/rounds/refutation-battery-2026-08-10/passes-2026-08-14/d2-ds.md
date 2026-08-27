`VERDICT: REFUTED — margin (i).` Exhibit: SUNDR, 2004 (Li, Krohn, Mazières, Shasha, OSDI). Mechanism: SUNDR’s fork consistency already uses version vectors; two observed histories are a fork only when the version vectors are **incomparable** under componentwise ordering. If one vector dominates the other, the divergence is treated as lawful/innocent partial visibility, not a fork. Destroyed clause: “Prior equivocation formalisms treat any divergence as a fork; here supersession makes some same-coordinate divergence lawful, and duplicity is specifically the incomparable pair.” SUNDR already has the comparability/incomparability split, so this margin is not novel.

`VERDICT: REFUTED — margin (iii) / chart-relativity corollary.` Exhibit: Bitcoin’s hash-chain fork definition, Nakamoto 2008. Mechanism: a Bitcoin block does not claim a `(pre, sn)` coordinate, but each block header contains `prev_block_hash`. Two distinct valid blocks with the same `prev_block_hash` are a fork/conflict defined purely from content-addressed graph structure. Destroyed clause: “systems without coordinates (no sn, no rotation — e.g. bare content-addressed event graphs) cannot define equivocation, only fail to detect it.” The parent-hash fiber already defines the conflict without a claimed coordinate.

`VERDICT: REFUTED — completeness of the antichain criterion.` Exhibit: counterexample constructed from the docket’s own stated validity conditions. Let `E0` be at `(p,0)`, `E1` at `(p,1)` with `prev = E0`, and `E2` at `(p,2)` with `prev = E0`, all validly signed and committed. Observer `O1` holds `{E0,E1}`; observer `O2` holds `{E0,E2}`. Then every fiber is a chain: `sn=1` has `{E1}`, `sn=2` has `{E2}`. There is no antichain of size ≥ 2 in any fiber, so the honesty criterion is satisfied. But `E1` and `E2` are competing successors of `E0`: the composites diverge. Destroyed clause: “Duplicity = an antichain of size ≥ 2 in some fiber, distributed across observers” as a complete criterion; also the honesty criterion as stated. This works because the docket does not state a contiguity validity rule such as `sn = prev.sn + 1`. If such a rule is added, the counterexample is excluded, but that is a repair to the formalization under attack.

`VERDICT: NOT REFUTED — margin (ii).` Strongest near-misses, ranked:

1. **BFT Forensics, Sheng et al., 2021** — quantifies honest-witness sufficiency for convicting equivocating replicas from transcripts, but does not price detection through observation-graph expansion or spectral gap against a cut-budget adversary.
2. **Eclipse-attack literature, Heilman et al., 2015 onward** — treats observer-graph cuts as an attack and connectivity as defense, with quantitative budget analysis, but it is not about duplicity detection or watcher-sufficiency via spectral gap.
3. **SUNDR, 2004** — requires client-to-client comparison/connectivity for fork detection, but stops at the qualitative connectivity requirement and does not provide the expansion/spectral-gap pricing layer.

Each lacks the specific combination: detection probability as a function of observation-graph expansion against a partition-budget adversary, with “how many watchers” reduced to spectral-gap sufficiency.

DRIFT

- If the antichain criterion is to survive the cross-coordinate counterexample above, the validity rules should explicitly include contiguity or some equivalent fiber-linking condition.
- The detection theorem’s “iff” is static; asynchrony/timing is not modeled. A comparison path may exist only after deceived parties have already acted, so any timely-detection claim would need a time bound.
- Receipt-set or signature-set equivocation is not represented in `M[coordinate, observer]` unless receipts/signatures are themselves made fiber occupants.
