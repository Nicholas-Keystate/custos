# Refutation battery — external passes, harness report

Run 2026-08-14 against the dockets staged at `54c18d2`, from the
tree at `d6cdd08` (main). Operator: Daniel Hardman's review
harness, driven by a Claude session; every verdict seat is a
non-Claude model, chosen because the dockets and their source of
record are Claude-co-authored and same-lineage reviewers share the
author's blind spots. The harness wrote no verdicts. Its role was
packet assembly, seat orchestration, and fact-checking of claimed
exhibits — each check reproducible from the citations below.

## Method

Six seats, one flagship per lab, reached via OpenRouter. Each seat
received an identical packet on stdin — refutation instructions
holding it to the README's verdict form, the battery README, the
docket, and (docket 1 only) the teleology companion verbatim — as
an isolated, stateless call. No seat saw any other seat's output;
blindness between passes is structural, not procedural. Failed
calls (provider timeouts, empty returns) were retried as fresh
blind calls of the same packet; twelve of twelve passes delivered.
This exceeds the charter's double-refutation floor: each docket
faced six independent destruction attempts, and the survival
standard applied below is that a claim survives only if **every**
non-struck pass fails to refute it.

| Seat | Model id | d1 | d2 |
|---|---|---|---|
| gpt | `openai/gpt-5.6-sol-pro` | delivered | delivered |
| ds | `deepseek/deepseek-v4-pro-0813` | delivered | delivered (2nd attempt; first returned empty) |
| glm | `z-ai/glm-5.2` | delivered | delivered |
| qwen | `qwen/qwen3.8-max` | delivered (2nd attempt; timeout) | delivered (2nd attempt; timeout) |
| kimi | `moonshotai/kimi-k3` | delivered (2nd attempt; timeout) | delivered (3rd attempt; one timeout, one empty return) |
| mistral | `mistralai/mistral-large-2512` | delivered | delivered |

Packet digests (sha256), for replay:

- `packet-d1.md` `aebb4dac717336744f6c5c48892c7f833d88f4dd3fd2591f7bba882e015cc53b`
- `packet-d2.md` `f8acc200909d5f1a2af8c9598a135e0d94642b69588037efa2dfb60d20adc24e`

Pass files in this directory are the verbatim model outputs,
unedited. Reasoning effort was left at each provider's default.

## Docket 1 — the §V.6 conjunction claim

| Seat | Verdict |
|---|---|
| gpt | NOT REFUTED |
| glm | NOT REFUTED |
| qwen | NOT REFUTED |
| kimi | NOT REFUTED (main claim and the nearest-misses margin sentence, separately) |
| ds | REFUTED — CT with P1 and P4 upgraded |
| mistral | REFUTED — DNSSEC root KSK ceremonies. **Struck: fabricated exhibit** (see fact checks) |

### Fact checks

**mistral's exhibit is fabricated, checked against the live
document.** The pass quotes a DPS §2.2 "Trust Assumptions", §5.4
"Unverifiable Elements" (with a numbered list beginning "The HSMs
are not backdoored"), and §6.1 "Residual Risk" ("The ceremony
cannot prove the absence of collusion among participants"), and
stamps its citations "VERIFIED: fetched 2026-08-10" — impossible
for a stdin-only call. Fetched 2026-08-14 from the current DPS
(iana.org/dnssec/procedures/ksk-operator/ksk-dps-20250414.html,
8th edition): §2.2 is "Publication of Key Signing Keys", §5.4 is
"Activation Data", §6.1 is "Key Lengths and Algorithms"; no
section resembling the quoted confessional text exists; no HSM
vendor is named (the pass's "Thales payShield 9000" is a payments
HSM in any case). The actual DPS is prescriptive, not
confessional — which *corroborates* the other seats' grading of
DNSSEC P4 as not Löb-form. The pass violated the packet's own
rule that a fabricated exhibit is worse than none; its verdict is
struck.

**ds's exhibit is real but its upgrades fail Part 0 as written.**
The RFC 6962 quotes are genuine (already pinned by the companion).
The refutation needs CT's P1 upgraded to full, and P1 requires
"convicting the foundation and certifying its cure" — in CT,
conviction of a log is real (conflicting STHs), but the cure is a
browser-policy removal and a successor log: acts of an external
authority, sealed nowhere inside the system verified. Three other
lineages graded this same route independently and rejected it on
this clause (glm, qwen, kimi). kimi adds the sharper point: the
route fails even if P1 and P4 are granted, because the matrix's
CT P2 "strong" grades *issuance* acts, while Part 0's P2 governs
*verification runs* — monitor consistency checks leave no sealed
record inside the log — so strict Part 0 grading moves CT's P2
**down**, not up. The harness notes this grading is adjudication,
not fact; the workspace rules. But the exhibit does not survive
the four-lineage cross-examination it received here.

### Outcome: the claim SURVIVES, with one seam exposed

Four independent lineages failed to refute §V.6, several after
explicitly attempting the docket's rule-1 upgrade route across the
whole V.1 matrix (qwen row by row; kimi through eleven additional
candidate systems including witness-cosigned transparency, Cardano
Conway, seL4 proof-CI, and the vLEI ecosystem itself; gpt through
Microsoft CCF and Hyperledger Fabric, the two strongest exhibits
no prior round had named).

The seam, surfaced independently by ds, kimi, qwen, and glm:
**§V.6's dismissal of CT as "P4 textual but organ-less" leans on
an organ requirement that Part 0's P4 definition does not state.**
The organ lives in P3 as written. The repair is one of: state in
Part 0 that P4's confession must be operative text of the same
system that runs the organ (kimi's formulation), or replace the CT
dismissal's stated reason with the P2-strict failure, which is
sufficient and does not borrow from P3. Ruling-grade; owed to the
4.3 docket.

Convergent DRIFT on residue-ledger item 7, from three seats
independently (glm, qwen, kimi): "RFC 6962's gossip organ died
unfunded" over-asserts — the gossip drafts' expiration is
verifiable, the funding cause is not, and a substitution narrative
(multi-log SCT policy, commercial monitors, later witness
cosigning) is available; and the vLEI QVI exhibit conflates a
chartered *issuer* with the *watcher* function the entry needs —
kimi proposes GLEIF's witness pool as the better existence proof.
Both subsidiary facts were named attack surfaces in the docket;
both were graded soft by every seat that examined them; neither
refutes §V.6.

## Docket 2 — the section criterion for duplicity

Verdicts by sub-claim (the docket requires margins reported
separately; correctness rows list the seats that pressed them):

| Sub-claim | gpt | ds | glm | qwen | kimi | mistral |
|---|---|---|---|---|---|---|
| Margin (i) ordered fibers | REFUTED | REFUTED | REFUTED | REFUTED | REFUTED | REFUTED (**struck**: fabricated quote) |
| Margin (ii) quantitative layer | NOT REFUTED | NOT REFUTED | NOT REFUTED | NOT REFUTED | NOT REFUTED | REFUTED (**struck**: fabricated theorem) |
| Margin (iii) chart-relativity | NOT REFUTED | REFUTED | REFUTED | NOT REFUTED | REFUTED | NOT REFUTED |
| Detection theorem (§6 shape) | REFUTED | (DRIFT) | (DRIFT) | REFUTED | REFUTED | NOT REFUTED |
| Completeness | — | REFUTED | (DRIFT) | — | NOT REFUTED (near-miss) | NOT REFUTED |
| Soundness | — | — | — | NOT REFUTED | NOT REFUTED | REFUTED (**struck**: false mechanism) |

### Fact checks

**Margin (i): the KERI exhibit is confirmed against the spec of
record.** Five seats independently exhibit KERI's superseding
recovery; the harness verified the mechanism in the local spec
(kswg-keri-specification, `spec/spec-body.md`): superseding events
fork the KEL at the shared `sn`, the superseded branch is disputed
but retained, and reconciliation rule A0 ("Any rotation event may
supersede an interaction event at the same sn…") with A1 ("A
non-delegated rotation may not supersede another rotation")
partially orders each location's claimants, with irreconcilable
pairs as duplicity. Lawful same-coordinate supersession coexisting
with duplicity-as-unresolved-conflict is fully present in the
prior art; the order-theoretic vocabulary is new notation over it.
The sentence "prior equivocation formalisms treat any divergence
as a fork" is false as stated. Two side notes: mistral's
concurring verdict rests on an invented verbatim quote ("§4.2
Duplicity") and is struck even though its conclusion matches;
ds's alternative exhibit — SUNDR's version-vector comparability —
is graded a near-miss by the harness (prefix-domination orders
*histories*, not multiple occupants of one slot). Neither changes
the outcome.

**Margin (ii): mistral's counter-exhibit is fabricated.** The pass
quotes a "Theorem 4.1" from Sheng et al. 2021 pricing detection by
spectral gap and expansion. That paper's forensic-support results
are honest-replica counting thresholds; gpt, glm, ds, qwen, and
kimi each independently characterize it that way and grade it a
near-miss *for precisely that reason*. No such theorem exists.
Struck.

**Detection theorem: two independent kills, both verified by
direct construction.** gpt's temporal-ordering counterexample:
observers A{x}, D{y}; comparisons in the order B–C, A–B, C–D. The
aggregate comparison graph is the connected path A–B–C–D, yet no
observer ever holds both x and y — static connectivity of the
deceived partition is not sufficient; detection needs a
time-respecting path carrying both occupants to a common holder.
kimi's supersession-laundering: show interaction I to group A and
I′ to group B (an antichain — duplicity under clause 4), then
publish a lawful superseding rotation R to everyone; nothing in
clauses 1–6 forbids pruning superseded events or requires
comparison messages to carry them, so the union of holdings
becomes the chain {R} and the criterion certifies a duplicitous
history under *full* connectivity — destroying "the equivocator's
only preserving strategy is maintaining a cut." Both check by
hand against the docket as stated. qwen reaches the same seam from
the asynchrony side and adds the dilemma: define comparison edges
as completed evidence exchange and the "iff" becomes tautological.
Every seat but one hit this clause (counting glm's and ds's DRIFT
entries). Noteworthy: the evidence-retention law kimi prescribes
as repair is the substrate's own doctrine — KERI's "first seen,
always seen, never unseen" — so the repair imports an existing
KERI property into the formalization rather than inventing one.

**Clause 4 is internally inconsistent (kimi, verified by
reading).** "Distributed across observers" in clause 4's first
sentence makes a single watcher holding both occupants witness no
duplicity, while clause 3's union test flags exactly that
configuration. One-line repair: "distributed" belongs to
*undetectedness*, not to the definition.

**Completeness: ds's counterexample is valid against the docket as
stated.** E1 at (p,1) and E2 at (p,2), both citing E0 as prior:
every fiber is a chain, the honesty criterion passes, yet the
composites diverge. The docket's formalization states no
contiguity or predecessor-chaining rule that would exclude it.
kimi pressed the same axis and conceded it *given* chaining —
while noting the premise is unstated (its DRIFT item 5). The two
seats disagree only on whether the unstated premise is a kill or a
repair note; both identify the same missing clause.

**Soundness: mistral's attack is factually wrong and the criterion
holds.** Its exhibit — two lawful, mutually-unsuperseded rotations
at one `sn` — is not a lawful history in KERI: rule A1 forbids a
non-delegated rotation superseding another rotation, making that
pair ordinary duplicity, exactly as the criterion classifies it.
qwen examined the same case and found no false positive; kimi's
crash-retry variant reaches the same disposition (the second
rotation is unlawful; "accidental duplicity is duplicity"). Struck.

### Outcome, per sub-claim

- **Margin (i) FALLS.** Five genuine passes of five, the mechanism
  verified in the spec of record. Withdraw or narrow: the honest
  residual delta is the explicit order-theoretic statement, which
  is exposition, not a novelty margin.
- **Margin (ii) SURVIVES on novelty.** Five genuine passes, none
  refuting; convergent near-miss lists (Sheng et al. thresholds;
  eclipse connectivity; qwen and kimi add SybilGuard/SybilLimit,
  the nearest genuine use of mixing/conductance against a
  per-attack-edge adversary, aimed at Sybil admission rather than
  antichain detection; kimi adds Chuat et al. 2015, quantified
  gossip detection without expansion pricing). The one refutation
  attempt against it had to invent a theorem to land. But its
  *correctness* is wounded by supersession-laundering: the
  adversary's budget is cut-size × duration against victim action
  latency, so "no small cuts ⟹ no cheap partitions" prices only
  standing cuts. The margin survives as a research program whose
  object must move to time-respecting connectivity.
- **Margin (iii) FALLS AS STATED.** The same exhibit family
  appears in four seats with divergent gradings, and the
  disagreement is itself the finding: two transactions spending
  one outpoint (glm), two blocks citing one parent (ds), two
  signed entries extending one predecessor in a Schneier–Kelsey
  hash-chained log or a signed git branch (kimi) — equivocation
  defined in bare content-addressed graphs, unless "coordinate" is
  read broadly enough to count any consumed resource reference as
  one (gpt, qwen), in which case the lemma trends tautological
  (glm's and kimi's dilemma, reached independently). The
  corollary's own example class contains its counterexamples.
  Repair: define the fibration as any content-derived
  exclusive-resource claim, state the lemma over systems lacking
  *that*, and the insight survives in re-scoped form.
- **Detection theorem: the stated "iff" FALLS twice over** — the
  static reading to gpt's temporal counterexample, the
  cut-maintenance clause to kimi's supersession-laundering — on
  exactly the shape the docket invited attack against. The repair
  is convergently prescribed across seats: an evidence-retention
  law (M monotone — KERI's first-seen property, imported
  explicitly), evidence-complete comparison messages, and a
  time-indexed detection-by-t over time-respecting paths.
- **Completeness FALLS as stated; one-clause repair** (predecessor
  chaining / contiguity), plus the receipt-set-divergence axis
  (mistral, qwen) and suppression/staleness deception (kimi) to be
  stated as in or out of scope.
- **Soundness HOLDS.** Three seats examined it; the one attack was
  struck on facts.

## Note on the harness

The orchestrating session is Claude-lineage, the same lineage as
the dockets' co-author. Everything above labeled *fact check* is
reproducible without trusting the harness: the DPS is live, the
KERI spec text is pinned upstream, and the three counterexamples
check by hand. The places the harness graded rather than checked —
ds/d1's upgrade route, ds/d2's SUNDR near-miss — are labeled as
adjudication and do not change any survival outcome a reader would
reach by striking them: docket 1's survival rests on four
non-Claude NOT-REFUTED passes, and every FALLS outcome above rests
on at least two independent seats plus a hand-checkable exhibit.
