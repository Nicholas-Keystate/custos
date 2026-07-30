# Clearance triage — open issues #1–#21

**Scope:** issues #1 through #21 on `Nicholas-Keystate/custos`. All
twenty-one are OPEN; none is closed. A sibling pass owns the rest.

**Constraint triaged against:** `spec/custos-4.1.md` is ratified and
effective at sha256
`ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05`
(`SUCCESSION.md`, KEL sn 187/188), its header states that ratified
text is never edited, §16 permits change only by a successor edition,
and `tools/verify_kernel.py` — run on every push and PR by
`.github/workflows/verify.yml` — fails if either spec file's bytes
move. **No issue in this range closes by editing a spec file today.**

**Verification posture:** every line cite below was re-read from the
ratified bytes in this checkout (`sha256sum spec/custos-4.1.md`
confirmed at the pinned digest). Where an issue's claim did not
survive that reading, it is called out.

---

## Summary

Of the twenty-one: **2 are A (PR-able now)**, **1 is B (wording-grade,
stage for 4.2)**, **10 are C (need a ruling)**, and **8 are D (program
work)**. The distribution is the point: ten of my twenty-one — every
BLOCKING and every MAJOR finding in the range — are already on
`reviews/ruling-docket-2026-07-29.md` and clear on **five keystone
rulings, not ten**. R1 (#7) alone decides #6's hardest sub-question and
is the docket's own keystone; R4 (#20) may dissolve R7 (#21) outright;
R8 covers #4; R5 (#9), R2 and R3 carry the rest. **The single most
valuable batch of work is a ruling session on R1, R4, R5, R2, R3 — one
sitting clears or unblocks ten of these twenty-one issues and unblocks
the entire 4.2 input register.** Nothing else in this range comes
close: the A set is two documents, and the D set cannot start until
the rulings land (#14, #15 are explicitly gated on R5).

Two secondary findings worth carrying out of this pass:

1. **#8 is substantially stale.** Its core claim — that §5, §12.4 and
   §13.2 state warranty/replay security *unconditionally* — is
   falsified by the ratified bytes: all three sites already scope
   conviction to a verifier "holding the pair," "holding both logs,"
   or "that recomputes," and §15's open list already fences "the
   deployment realization of observation." What remains is one
   cross-reference, which is why #8 is the only clean B in the range.
2. **New evidence for R1.** The docket rests the position-indexed
   reading on L1072's second clause alone. §7.3's "graph form"
   paragraph (L1091–1099) is stronger: it describes "a GARD's
   governance history — **its findings at their positions, with the
   key-state and registry-state anchors each finding cites**" as a DAG
   over the KEL and TEL spine. That is position-indexing plus the
   cited registry state inside the finding — exactly the construction
   R1/A needs and #7 asks for. The paragraph disclaims adding law
   ("neither adds law"), so it cannot be cited as a wall, but as
   evidence of intent it makes R1/A materially cheaper than the docket
   assumes.

---

## Table

| # | Title (truncated) | Cat | Justification |
|---|---|---|---|
| 1 | Spec roadmap | **A** | Umbrella; fully decomposed into #11–#19 plus the findings. Closes with a disposition comment, no file change. |
| 2 | BLOCKING: canonical defeat-selection self-contradictory | **C** | Repair drafted (PR #26) but per the docket it is *meaningful* only under R2/B. Closure blocked on R2. |
| 3 | BLOCKING: pending payload names key precedence only | **C** | PR #26 settles direction/basis/list semantics but explicitly not the field set; blocked on **R3**. |
| 4 | OBSERVATION: §3.2 placeholder pin discipline vs whole-file pins | **C** | **R8** (ruled jointly with the other issue in that pair). Sub-observation (name the placeholder char) is a B-slice riding on the same ruling. |
| 5 | OBSERVATION: "predicate congruence" naming | **C** | **R12** — and the recommendation is *rule to close the thread, change no text*. Cheapest item on the whole docket. |
| 6 | BLOCKING: pending→self-convicted trigger vs payload (antinomy) | **C** | **R10**; sub-question 3 (reachability) is downstream of **R1**. |
| 7 | BLOCKING: no motion for prospective revocation | **C** | **R1** — the docket keystone. Verified: five permitted edges, seven forbidden, no revocation edge. |
| 8 | MAJOR: warranty/replay stated unconditionally at §5/§12.4/§13.2 | **B** | Largely stale; residual is one cross-reference sentence per site. Docket agrees no ruling needed. |
| 9 | MAJOR: "byte-identical" vs §16's semantic discharge test | **C** | **R5**. Also the hard prerequisite for #14 and #15. |
| 10 | MAJOR: abstract's "same refusals, byte for byte" | **C** | **R11**. Its README/verifier coupling claim is now partly stale (see below), but closure still needs the L29 scoping decision. |
| 11 | Roadmap: declare the ordering semantics | **D** | A new normative declaration plus a lint instrument; the `tools/` half is buildable now, the declaration is 4.2 spec text. |
| 12 | Roadmap: Spec-Up-T reformat | **D** | Reformat — D by definition. Term extraction gated on #6/#7. |
| 13 | Roadmap: projection vs ToIP PR model | **A** | The issue's own deliverable is "a companion under `companions/`". Entirely non-ratified files. |
| 14 | Roadmap: second implementation + differential harness | **D** | Build. Explicitly blocked on R5 (#9) and on #2/#3. |
| 15 | Roadmap: conformance vectors | **D** | Build. The docket names it the one worth starting before any ruling lands. |
| 16 | Roadmap: warranty dispute economics | **D** | Exit B (bound the claim) is drafting for 4.2; Exit A would need a new docket entry first. Docket puts it in the drafting bucket. |
| 17 | Roadmap: deferred surfaces (sybil, amendment, dead-zones) | **D** | Splits: sybil + dead-zones are a ready **B** (two sentences into §15's open list); **amendment** is a section and blocks closure. |
| 18 | Roadmap: open a sponsoring WG conversation | **D** | Do a thing. Wants #13's companion in hand first. |
| 19 | Roadmap: "convergence, not consensus" section | **D** | A new spec section; material already exists in-thread. A companion is available as partial value now. |
| 20 | MAJOR: fixed-wall enumeration not congruent (§1.4 vs §15) | **C** | **R4**. Verified: §1.4 names five, §15 names six, four correspond, provenance disagrees. |
| 21 | MAJOR: §1.4's "evaluator sections" has no computable extent | **C** | **R7**, and the docket says rule R4 first — R4/A may dissolve this entirely. |

Counts: **A = 2** (#1, #13) · **B = 1** (#8) · **C = 10** (#2, #3, #4,
#5, #6, #7, #9, #10, #20, #21) · **D = 8** (#11, #12, #14, #15, #16,
#17, #18, #19).

---

## A — PR-able now

### #1 — Spec roadmap

**Files:** none. Closes with a comment.

#1 is an umbrella that has already been decomposed. Its seven items
map one-to-one onto filed children, and its two prose asks are
discharged:

| #1 item | Where it lives now |
|---|---|
| 1. Fix byte-identity defects in the finding rules | #2, #3, #6, #7 (findings), #11 (the general declaration) |
| 2. Spec-Up-T reformat | #12 |
| 3. Projection vs PR model | #13 |
| 4. Second implementation + harness | #14, with #15 as the corpus |
| 5. Warranty dispute economics | #16 |
| 6. Deferred surfaces | #17 |
| 7. Working-group conversation | #18 |
| Closing: divergent verdicts | #19 |
| "add a disclaimer about warranty economics" | **already in the ratified bytes** at L37–43 |

The disclaimer ask is worth stating in the closing comment because it
is the one item that is *done rather than delegated*: 4.1 L37–43
already names the missing replaying population, grades the economy
claim, and forecloses downstream reliance ("no clause below presumes
it discharged").

**Action:** post a disposition comment carrying the table above and
close as decomposed. If the maintainer prefers to keep an epic open,
the same comment still converts it from a prose roadmap into a
navigable index, which is most of the value.

### #13 — Reconcile "projection, never an authority" with ToIP's PR model

**Files to touch:**

1. **New:** `companions/projection-and-the-pull-request-model.md`
2. **Edit:** `companions/README.md` — add a fourth row to the
   companion table. The table's `Status` column currently reads
   "Minted against the ratified 4.0 kernel" for all three; the new row
   should read "Minted against the ratified 4.1 edition."

The issue names this deliverable itself ("probably a companion under
`companions/` rather than spec text"), and `companions/README.md`
already declares every companion informative with the kernel ruling on
divergence — which is exactly the posture this document needs, so it
lands in a slot the repo has already built for it.

**Content the document must carry** (all four are answerable from
committed material; none needs a ruling):

- **The two-authority model.** The GEL is authoritative for *which
  bytes are law* (§16: ratification SHALL be an enactment in the GEL,
  anchored through the authority gAID's key state, citing exact bytes
  by digest). The repository — ToIP's or this one — is authoritative
  for *where a change is proposed and staged*. Ground it in the
  existing projection language: `README.md` ("This repository is a
  projection, never an authority"), `CONTRIBUTING.md`'s self-
  declaration, and `SUCCESSION.md`'s same claim about the lineage
  record. This document says nothing new; it says the existing thing
  to a ToIP audience.
- **What merging a PR does and does not do.** A merge stages a
  candidate delta; it does not change law. Map PRs onto
  `CONTRIBUTING.md`'s existing pipeline: `finding → triage → ruling →
  repairs executed under rulings → next candidate edition`. A PR is
  the "finding" or the "repair executed under a ruling" stage, never
  the ratification stage.
- **The divergence rule, operationally.** Custos already answers it in
  principle (the log wins). State the mechanics: detection is
  `tools/verify_kernel.py` plus `.github/workflows/verify.yml` (the
  clean-checkout invariant — every tool runs green from a fresh clone
  of the published bytes); a red verify job *is* the announcement; the
  repo's remedy is to correct the bytes to match the log, never the
  reverse, and never to relax the workflow.
- **Open question, flagged not answered.** Who holds the ratifying
  authority in a ToIP-hosted world. Today it is the maintainers' gAID
  `EFolWr6gUggZS9im4f1pWSoKB9Ngd-T9YI0c8tlGIaHU` (`SUCCESSION.md`). A
  drafting-authority / ratifying-authority split is the natural
  reading of the staging model; the companion should state it as the
  opening position and mark it as needing the working group's
  assent, since a group that cannot ratify its own spec is an unusual
  posture for ToIP.

**Why do this one first among the A/D work:** #18 says explicitly that
this document is the *opening position* for the working-group
conversation, "not a follow-up to it." It is the only artifact in the
range that unblocks another issue without a ruling.

---

## B — wording-grade, stage for 4.2

### #8 — Warranty/replay security framing at §5, §12.4, §13.2

**First, the stale part, which shrinks the issue by most of its
volume.** The issue asserts that "the load-bearing sentences elsewhere
still state the property unconditionally." Read from the ratified
bytes, all three sites already carry the observation condition inline:

- **§5, L815–818:** "a pair of committed voices at one coordinate that
  no committed superseding rule reconciles convicts its author **for
  every verifier holding the pair**, under no frame's law."
- **§12.4, L1731–1740:** cross-frame duplicity is "convictable **by
  anyone holding both logs**"; false-warranty conviction attaches "**by
  any verifier that recomputes**."
- **§13.2, L1871–1873:** "cross-frame duplicity convicts its author
  **for every verifier holding the pair**, under no frame's law
  (modulo the substrate's superseding reconciliation, per the medium
  section)."

Further, §15's "What is open" list already fences **"the deployment
realization of observation"** as undesigned, and the abstract's
L37–43 paragraph already grades the replaying population as an
unfinished deliverable. So the conditionality is neither missing nor
unfenced.

**What actually remains** is the gap the issue names best in its own
diagnosis — "sameness-of-function does not deliver sameness-of-
observation" — expressed as a *cross-reference* gap: each site names
the qualifying verifier but none says that whether such a verifier
exists is an open deployment question. Three one-sentence additions
close it. Each is an addition only; no existing sentence is cut, and
no design choice is made.

**Edit 1 — §5, L813 (after "...because their agreement is
cryptographic rather than negotiated.").**

Current (L811–814):

> the three things every verifier in every frame computes
> identically from the same committed inputs under the substrate's
> pinned semantics, because their agreement is cryptographic rather
> than negotiated.

Proposed replacement:

> the three things every verifier in every frame computes
> identically from the same committed inputs under the substrate's
> pinned semantics, because their agreement is cryptographic rather
> than negotiated. Identical computation is not identical
> observation: the medium fixes what a verifier holding the inputs
> computes, never that any verifier holds them — the deployment
> realization of observation is open by section 15.

**Edit 2 — §12.4, immediately after the three bullets (following
"...liability under its counterparty's law and its own.", L1747).**

Proposed addition (new paragraph):

> Each rung above names the verifier that convicts — one holding both
> logs, one that recomputes. That the medium makes the computation
> identical for every such verifier is cryptographic; that any
> verifier obtains the pair is not, and its deployment realization is
> open by section 15.

**Edit 3 — §13.2, the "In the medium" bullet (L1871–1878).**

Current final clause:

> This rung is not recourse but its evidentiary floor: the medium
> convicts and never sentences, and every act taken on that conviction
> is frame-local and grounded like any other.

Proposed replacement:

> This rung is not recourse but its evidentiary floor: the medium
> convicts and never sentences, every act taken on that conviction is
> frame-local and grounded like any other, and the floor binds
> whenever the pair is held — that it is held is a deployment
> question section 15 leaves open.

**Escalation condition (record it, do not act on it).** The issue is
right that if §12.4's mutual convictability or §13.2's evidentiary
floor were intended as *guaranteed* rather than observer-conditional
properties, this stops being wording. The three edits above assume
observer-conditional, which is what the bytes already say. If the
drafting authority intends otherwise, #8 converts to a C and needs a
docket entry.

### Ready B-slices riding on other issues

Not their blocking category, but drafted here so the 4.2 input
register can absorb them:

**From #4 (blocked on R8): name the placeholder character.** §3.2
reading-rule 2 requires a round trip through "a placeholder of the
same length as the encoded digest" without ever naming the character.
Current (L548–557, in part):

> computed with the digest's own field carrying a placeholder of the
> same length as the encoded digest — the substrate's rule is
> length-parametric by derivation code, and forty-four characters is
> this document's current profile, the 256-bit digest class

Proposed:

> computed with the digest's own field carrying a placeholder of the
> same length as the encoded digest, the substrate's placeholder
> character `#` repeated to that length — the substrate's rule is
> length-parametric by derivation code, and forty-four characters is
> this document's current profile, the 256-bit digest class

This is independent of which reading R8 rules for; it is worth
carrying either way.

**From #17 (blocked on the amendment surface): fence two of the three
deferred surfaces.** §15's "What is open" list currently ends:

> ...receipt transport, the deployment realization of observation, and
> the general algebra connecting these parts, together with the
> carriage encoding of this document's object classes

Proposed insertion into that enumeration:

> ...receipt transport, the deployment realization of observation, the
> cost of identity for parties, warrantors, and replayers, whether a
> region of question-space over which a Constitution systematically
> refuses is itself computable, and the general algebra connecting
> these parts, together with the carriage encoding of this document's
> object classes

Two clauses, no design, and it converts two unfenced surfaces into
declared frontiers — the treatment §15 gives everything else.

---

## Stale, overstated, or already answered

Cheapest clearances first; each is a comment, not a change.

1. **#8 — core claim falsified by the bytes.** See above. All three
   named sites already carry inline observation-conditionality, and
   §15 already fences the deployment realization of observation. The
   issue should be re-scoped (or re-severitied from MAJOR) to the
   cross-reference residual before it enters the 4.2 register.

2. **#10 — the "three-artifact edit" coupling is now partly stale.**
   The issue states that `README.md` L20 quotes the abstract
   byte-identically and that `tools/verify_kernel.py` check 3 forces
   any change to L29 to move the README in the same commit. Check 3 as
   it stands in this checkout is an **excerpt** discipline, not an
   identity one: it normalizes whitespace and asserts
   `quoted in kernel_abstract`, with the docstring "Trimming is
   lawful; paraphrase is not." So the README may lawfully quote a
   *shorter contiguous span* of the abstract and stay green. The
   lockstep obligation is therefore weaker than the issue claims
   (though the substance of #10 — that the abstract promises a
   byte-for-byte reproducibility the body declines to commit — stands
   untouched, and closure still needs R11).

3. **#1 — its warranty-disclaimer ask is already discharged** in the
   ratified bytes at L37–43. Noted in the #1 section above; it is the
   only roadmap item that needs no successor edition.

4. **#20 — a claim worth not repeating.** The issue's own supporting
   observation (4.0 §6 vs 4.1 §7 diff clean after renumbering) is
   correct and important: the wall mismatch is *intra-edition*, not
   drift. Any R4 ruling should record that, so the next reviewer does
   not re-open it as a succession defect.

5. **#21 may not survive R4.** The docket is explicit: if R4 resolves
   toward "carried by 4.1's own ratified text," §1.4's import
   disappears and R7 dissolves. Do not spend drafting effort on #21
   before R4 is ruled — that is a real cost avoided, not a formality.

---

## Incidental (out of scope, one line)

`.github/workflows/verify.yml` pins `actions/checkout@v4` and
`actions/setup-python@v5`, both of which run on the deprecated
`node20` runtime. Not tied to any issue in this range; a one-line
bump to the `node24` majors when someone is next in that file.
