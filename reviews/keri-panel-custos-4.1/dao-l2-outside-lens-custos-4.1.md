# DAO / L2-governance outside-lens review — custos-4.1

- **Reviewer:** Codex (gpt-5.5), high reasoning effort, prompted as a senior DAO/Ethereum/L2-governance adversary
- **Date:** 2026-07-27
- **Target:** `spec/custos-4.1.md` (full text)
- **Purpose:** deliberately import the blockchain/DAO/L2 priors that `keri-doctrine.md` instructs the KERI-native panel to *refuse* — the complementary axis. Raw run: `/tmp/custos-dao-review.log`.

## Verdict

> Custos has a strong auditability idea: governance acts should be replayable from committed evidence, and evaluators should refuse when law is missing. But as a governance architecture, it mostly specifies **evidence discipline, not a complete dispute or enforcement system**. The warranty economy is effectively an optimistic verification system without the parts that make optimistic systems survivable: bonds, challenge windows, slashing rules, challenger incentives, data-availability enforcement, and a canonical dispute result.
>
> The biggest risk is that Custos treats "recomputable if you have the logs" as close to "governance has converged." Those are not the same. In blockchain/DAO terms, **Custos has validity rules but no settlement layer.**

## Ranked findings

| # | Severity | Title | Prior art |
|---|----------|-------|-----------|
| 1 | BLOCKING | Warranty economics recreate optimistic rollups without the dispute game (no bond, challenge window, slashing, challenge venue, challenger reward, griefing budget) | Optimism/Arbitrum fault proofs, UMA optimistic oracle |
| 2 | BLOCKING | Verifier's dilemma unanswered — replay is costly, so no rational stranger re-folds; false warranties persist | TrueBit verification games, rollup watchtower economics, DAS incentives |
| 3 | BLOCKING | No global consensus → no canonical verdict; two honest parties with different bundles replay correctly to *different* findings | Canonical-chain selection & finality; optimistic rollups settle to L1 |
| 4 | MAJOR | Data availability is a *charter*, not enforcement — a party withholding spans shapes practical truth without falsifying bytes | Validium/DA failures, Celestia/EigenDA sampling, blob windows |
| 5 | MAJOR | Replay determinism ≠ oracle — self-conviction catches internal contradiction, not consistent lying about external reality | UMA optimistic oracle, Kleros, Augur |
| 6 | MAJOR | Sybil resistance externalized — KERI AIDs are cheap; "N independent attestations" is forgeable | Gitcoin Passport, BrightID, proof-of-humanity, token weight |
| 7 | MAJOR | Amendment governance underspecified — no quorum/timelock/veto → "the rules can lawfully destroy themselves" | Governor Bravo, timelocks, veto councils, emergency guardians |
| 8 | MAJOR | Low-quorum & last-minute governance attacks open (late content swap via referenced bytes / law-head substitution) | Beanstalk exploit, Compound proposal mechanics, Snapshot manipulation |
| 9 | MAJOR | "Refusal" can be weaponized — a captured drafter engineers accountability dead-zones ("no rule, no verdict" → "no accountability") | Ambiguous DAO emergency clauses, jurisdiction-avoidance games |
| 10 | MAJOR | Recourse is mostly exit, not enforcement — conviction is reputational; no slash/freeze/compensation | Moloch ragequit, restaking slashing, optimistic-bridge failures |
| 11 | MAJOR | Gever correctness = a trusted single-implementation problem (one pinned checkout carries the whole replay claim) | Ethereum client diversity, Parity multisig, rollup prover bugs |
| 12 | MAJOR | "Code is law" risks preserved, not removed — a flawed committed rule is faithfully, replayably applied | The DAO, Compound governance bugs, Mango Markets |
| 13 | MINOR | Federation doesn't scale cleanly — pairwise envelopes get brittle at n frames | IBC zones, bridge networks, D2D agreements |
| 14 | OBSERVATION | Privacy tradeoff is severe — verification cones disclose credential/registry evidence about people | MACI, Semaphore, ZK/selective-disclosure creds |

## Most likely KERI-native blind spots (reviewer's own summary)

1. The warranty model is an optimistic-rollup fraud-proof system in substance, and needs the full dispute-game economics.
2. Deterministic replay over identical inputs is **not settlement**. Without shared DA and finality, honest parties can remain permanently divergent.
3. Self-conviction solves equivocation, not lying about external reality. The oracle problem remains the hard part.
4. KERI identifiers are not sybil resistance. Any rule counting identifiers/attestations/warrantors needs an independent scarcity or personhood model.
5. "The log guards the guardian" only works against violations of *already-authored* law. It does not protect against captured authors, bad amendment rules, low quorum, bribery, or lawful self-destruction.

## Caveat on this lens

Every finding here is stated from *outside* KERI's objective function. Several (esp. #3 non-convergence, #10 recourse-is-exit, #14 privacy) fault Custos for properties KERI **deliberately declines to provide** (global consensus, on-chain enforcement, unlinkability). Those are not bugs in KERI's frame — they are the frame. Their value is that they mark exactly where Custos must make an *explicit, defended* choice for a ToIP audience that will include people carrying these blockchain priors. See the reconciliation for which findings survive translation into KERI's terms and which are frame-conflicts to be answered rather than fixed.
