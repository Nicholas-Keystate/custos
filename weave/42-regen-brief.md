# Regeneration brief — Custos 4.2 candidate v1 (2026-08-01)

**For a fresh-context drafting agent. Workdir:
/Users/hun-magnon/Documents/KERI/standard-annealing/. This brief
plus the files it pins are your entire world. Do not consult
thread files, GitHub, or any artifact not named here.**

## Step 0 — verify every input digest before reading anything

Run `shasum -a 256` on each; on ANY mismatch, STOP and report the
mismatch. Do not proceed on drifted bytes.

| Input | Path | sha256 |
|---|---|---|
| The frozen manifest (your law) | `weave/42-input-manifest.md` | `74bdb8a0d950d8c7d8454cb7e015642636eae3d8944f954ba1d5e54d2ac950d9` |
| Predecessor (consumed whole) | `staged-repos/custos/spec/custos-4.1.md` | `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| The graduated seed (extracted byte-exact) | `weave/42-taxonomy-chapter-v2.md` | `dfd1ddc1a092225470d2e075c0ad7eec55a4d10e892f38501d763212fcd2bd9a` |
| Ruling record | `reviews/ruling-record-2026-07-30.md` | `45a6d7208f0faca82946f2bfacb04799994b5cf2c9afdef53f24def9d8cf8552` |
| Supplement 1 (errata bind) | `reviews/ruling-record-supplement-1-2026-07-31.md` | `e7ca111120e04163822bf098855662f163dc3f6de87a3ca71c2a093d7bc01d2d` |
| Supplement 2 (nine rulings) | `reviews/ruling-record-supplement-2-2026-08-01.md` | `7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670` |
| Compact-form gates (new body content) | `weave/42-compact-form-gates.md` | `0572afd9a55e3bc07ef2144e93fe0d6847f11e90f8de3e7b6e977631d358e45a` |
| External-findings scaffold (§E, §F) | `weave/42-external-findings-scaffold.md` | `e21a0392928c6d0df516f7b3a8fccc1c5b738be8b6b46911d9e40c0ccca92e8b` |
| External influences register | `weave/external-influences.md` | `ff19fb11998ab77fbbf769f2be0b1d684a06fac81cac5eea2951db9fbb555f0e` |

`staged-repos/custos/` is READ-ONLY. You write exactly TWO files:
`weave/custos-4.2-candidate-v1.md` (the candidate) and
`weave/42-regen-report.md` (your report). Nothing else.

## The task

Compute the Custos 4.2 candidate WHOLE from the inputs above,
under the consume-and-regenerate law: every section of the
predecessor is consciously CARRIED (re-derived intact), REPAIRED
(under a named ruling), SUPERSEDED (by the seed or the gates
content), or DROPPED (with grounds) — and the censuses account
all of it. The manifest (especially Amendment 4's repair-surface
list and section E) is your work order; the record + supplements
are your law; where this brief and the manifest disagree, the
manifest wins.

## The meld-method law (HARD)

Surviving bytes are NEVER emitted through your token stream.
Work in three passes:

1. **Plan pass:** read everything; write a section-by-section
   disposition table (predecessor section → carried / repaired /
   superseded / dropped, with the governing ruling for each).
2. **Byte-surgery pass:** assemble the candidate skeleton with a
   python script that SPLICES verbatim byte ranges from the
   predecessor (carried sections) and the seed file (the whole
   taxonomy chapter, byte-exact, as the new Chapter 2 — its
   in-file header block through its final line, with only the
   draft-status header replaced by a candidate-integrated
   heading, and that replacement done by the script, not by
   retyping). Verify each spliced range by digest against its
   source before and after splicing.
3. **Prose pass:** write ONLY the genuinely recomposed spans —
   the repairs under their rulings, the new-content integrations,
   the seams. Every repaired span cites its ruling (R-number,
   record or supplement) in a drafting comment you leave in the
   report, NOT in the candidate text.

## Sacrosanct spans (byte-exact, verify by grep after assembly)

These five user lines MUST appear byte-identically:
1. `KERI detects; a GARD adjudicates.`
2. `Her computed answer testifies.`
3. `acts, and is held to account, by the same committed judgments`
4. `receipt of performed governance`
5. `the compact form changes cost, never meaning`

The seed chapter (405 lines) is sacrosanct as a block: after
assembly, extracting the corresponding line range of the
candidate and diffing against `weave/42-taxonomy-chapter-v2.md`
body MUST yield only the agreed header substitution.

## The three seam-rules (ruled by the user; binding)

1. **Seed ↔ predecessor §5–§11:** predecessor object-class prose
   survives untouched UNLESS it asserts enumeration-over-
   generation, in which case it repairs under the seed's own
   citations (4.1 L1459, L1536–1537) — census-logged, minimal
   touch.
2. **Gates content ↔ §12:** §12's consumption ladder stays; the
   new compact-form/gates chapter (recomposed from
   `42-compact-form-gates.md` — content, not file-verbatim)
   cites the ladder downward; the sentence "until every gate
   stands, warranted receipts travel in the heavyweight
   envelope" appears ONCE, in the gates chapter, and §12 points
   to it.
3. **Terminology sweep (four-tier ladder: predicate < clause <
   covenant; commitment = substrate act only):** mechanical
   swaps where meaning is untouched; any site where the swap
   would CHANGE meaning is census-flagged as a finding, never
   silently resolved. Line 865's "composition warranty"
   double-duty site resolves explicitly. "Colored receipt" must
   not appear (check; ratified text is believed clean).

## The repair surfaces (execute each under its ruling)

Work from manifest Amendment 4's list — the ten surfaces, from
§6 (R16 removal-by-identification) through §9 (R17 three-layer
split) — plus the first-docket repairs (R1–R12 per the record as
corrected by supplement 1: seven walls with E-1's one-wall-retype
correction; R5's predicate in C-1's vocabulary; R6's succession
wording; R8's two pin kinds; R11's rescoped abstract with the
README/verify-kernel coupling NOTED in the report for the
ratifying authority). The generalized commitment — no ambient
input: order, membership, semantics — is stated ONCE where axiom
4 lives, with three named faces. New walls: NONE (R4/C-2:
membership conserved at seven, one retype).

## Register (binding)

Calm declarative specification prose. BCP 14 keywords only where
force is meant; no other ALL-CAPS. No economics vocabulary
(verification cost in engineering units only). KERI named
directly. No pulpit anaphora. Minimal-case-first preserved
everywhere the predecessor has it. Confessions and openness
clauses survive with force intact — confessed openness beats
invented closure; nothing the manifest holds open (R19, carriage
encoding, dossier answer) may be closed by drafting.

## The three censuses (appended to the candidate as its final
## appendix, per manifest law)

1. **Delta census:** every change from the predecessor, each
   with its governing ruling.
2. **Structure census:** every predecessor section dispositioned
   (carried/repaired/superseded/dropped) — zero unexplained
   entries.
3. **Collision-by-addition census:** every CARRIED span
   re-examined against the NEW commitments (the nine supplement-2
   rulings + the generalized ambient commitment); any carried
   text made defective by new law is repaired-and-logged or
   flagged — never silently retained.

## Report (`weave/42-regen-report.md`)

Output digest + line count; the disposition table; the spliced-
range verification log (source range, digest, target range); the
sacrosanct grep results; the census summaries (counts); every
seam decision with one-line grounds; anything you could not
resolve, stated plainly as OPEN rather than papered over.
