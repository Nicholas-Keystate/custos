# Custos 4.2 regeneration — assembly report

Date: 2026-08-03. Brief: weave/42-regen-brief.md (frozen).
Manifest: weave/42-input-manifest.md (sha256
74bdb8a0d950d8c7d8454cb7e015642636eae3d8944f954ba1d5e54d2ac950d9).
Assembler: fresh-context drafting agent; splice engine and text
modules staged under tmp staging (42_assemble.py — held at ops/held/42-assemble-engine.py; 42_texts.py,
42_texts2.py, 42_texts3.py, 42_texts4.py); assembly log at
ops/held/42-assembly-log.json (held copy; staging original was tmp-ephemeral). All verification below was
run from the written file's bytes, not from in-memory state.

## Output

- File: weave/custos-4.2-candidate-v1.md
- sha256: c62c1ddeeb5ad73fa8bdf5e1fb2a812865ccf72a8b04e05a8f6e38cddf2a67c8
- Lines: 3596. Headings: 56 (two chapters; sections 3–19;
  appendix with three censuses).

## Step 0 — input digest verification

All nine pinned inputs verified by `shasum -a 256` before any
content was read; all nine matched (exit 0). The splice engine
re-verifies the three inputs it opens (manifest, predecessor,
seed) by pinned digest at the top of every run and asserts
before splicing.

## Method

Meld-method law observed: every carried span entered the
candidate by python byte-range splice from digest-verified
inputs — never retyped through the drafting agent's token
stream. Repairs were applied as substitutions, each a
(label, ruling, old, new) tuple asserted to match exactly once
in the renumbered carried piece; any count ≠ 1 aborts the
build. Renumbering of carried sections 2–17 → 3–18 was
mechanical (regex over headings, subheadings, and
section-references; 16 headings, 14 subheadings, 31 refs
bumped; a post-check confirms zero refs > 19 remain).

## Spliced-range verification log

| Source | Range (lines) | Target | sha256 of spliced bytes |
|---|---|---|---|
| custos-4.1.md | 15–31 | Abstract p1 (2 repairs) | b031cff13218e42ff0aa546d66af3ec24881322ad4ef88b3503e043f7da73a92 |
| custos-4.1.md | 73–415 | Chapter 1 (3 repairs) | 1043a014ffbca0134ca4ea232e9adf666bae404022e99765f7d94a1db75739a9 |
| custos-4.1.md | 420–2306 | Sections 3–18 (renumbered, repaired) | 7333cebc123b955647c1c5c87c33e1c35268fde02637ef019cc0d5fe9f439643 |
| 42-taxonomy-chapter-v2.md | 26–401 | Chapter 2 body, candidate lines 454–829 | 47b2abdf8291714b563ef74fea2bacf170b0d6d9a15ca277dd5547878507f78b |

Digests above are of the pre-repair verbatim splices as
extracted; the Chapter 2 splice carries zero repairs (byte-exact
in the candidate, verified below). Composed-whole pieces (head,
abstract p2, introduction, Chapter 2 integration heading,
section 19, appendix) are new prose, not splices, and are so
dispositioned in the delta census.

## Disposition table

Full table is in the candidate's structure census (its binding
home per manifest law). Summary: 28 predecessor sections
dispositioned — 8 carried intact (1.0, 1.1, 1.3, 1.5, 1.6, 1.7,
§8→9, §11→12), 15 repaired under named rulings, 5 superseded
(head, introduction, the §17 gate paragraph into section 19,
the predecessor appendix, plus the abstract's second paragraph
regenerated under C-13), 0 dropped without grounds, 0
unexplained. Additions: Chapter 2 (seed, byte-exact), §7
blinding mandate (R18), §8.3 bearing rule (R13), §8.4
conviction ladder (R10/C-17/C-15), §8.5 compound closure (11a),
§13.5 convergence geometry (C-15), §18 designation-and-
membership block (R15), section 19 whole (C-16 + F-amendment),
the three-census appendix.

## Ruling-named substitutions

43 substitutions applied, every one attributed and
exactly-once-asserted: Abstract 1 (R11); Chapter 1 ×3
(R17 seal admissibility; generalized commitment at axiom 4;
R4/E-1/C-2 wall citation); scope ×3 (R5/R11, R16, Chapter-2
seam); reading rules ×2 (R8, R20); definitions ×2 (C-14, R17);
medium ×1 (8a); objects ×2 + structural ×4 (R16, R13, R15, R18,
line-865 sweep); codomain ×8 (R1, R2, R3, R5, R6, R9, R10, R13,
R14, 11a); seal ladder ×2 (R17, C-1); rotation ×1 (R18);
transformation ×4 (C-13, C-15, 8a, sweep); recourse ×1 (8a);
federation ×1 (R20); openness ×2 (R4 seven walls, R5 charter);
succession ×2 (lineage pins, R5/C-1 predicate); grammar ×3 + 
vectors ×1 (R15, wall-6 hook, gate-paragraph supersession).
Old/new digests per substitution are in
ops/held/42-assembly-log.json (held copy; staging original was tmp-ephemeral).

## Sacrosanct verification (grep from disk)

| Span | Candidate | Predecessor | Verdict |
|---|---|---|---|
| `KERI detects; a GARD adjudicates.` | 1 | 1 | PASS |
| `Her computed answer testifies.` | 1 | 1 | PASS |
| `acts, and is held to account, by the same committed judgments` | 1 (wrapped `committed\njudgments`, byte-identical to the predecessor's own wrap) | 1 (same wrap) | PASS |
| `receipt of performed governance` | 2 | 2 | PASS |
| `the compact form changes cost, never meaning` | 1 | 1 | PASS |

Note on span 3: in both the ratified predecessor and the
candidate the line wraps after "committed"; the span is
byte-identical to the predecessor's bytes, wrap included, and
whitespace-normalized grep confirms the sentence whole.

Seed block: the 376-line chapter body (seed lines 26–401)
appears in the candidate (lines 454–829) byte-identical — list
equality True, sha256 of the extracted range equal to the
sha256 of the seed body. The only delta versus the seed file is
the agreed header substitution: the seed's pin-closure header
(lines 1–25) and closing status line (403–406) replaced by the
integration heading, which itself pins the seed digest.

## Census summaries (counts)

- Delta census: 48 entries, each under its governing ruling.
- Structure census: 28 predecessor rows dispositioned; 10
  additions listed; zero unexplained either way.
- Collision-by-addition census: 11 repaired-on-collision
  findings (cross-referenced to delta entries) + 9
  examined-and-retained spans with grounds; zero carried spans
  retained defective; zero collisions unexamined.

## Seam decisions (one-line grounds each)

1. Seed ↔ §12 (object classes): brief's seam-rule 1 check run
   over the carried §12 — zero enumeration-over-generation
   assertions found (the open-enumeration paragraph is itself
   the seed's cited ground, 4.1 L1459/L1536–37), so the prose
   survives untouched; logged in the structure census row.
2. Gates ↔ §13.3: the consumption ladder stays in §13.3 and
   points downward to section 19; the envelope sentence appears
   exactly once, in section 19 (disk grep count: 1); §13.3's
   pointer paraphrases without repeating it.
3. Terminology sweep: four-tier ladder (predicate < clause <
   covenant; commitment = substrate act only) resolved at the
   §5 definition, not re-litigated at sites; line 865's
   "composition warranty" resolved explicitly to carriage
   commitment (delta 33); "colored receipt" absent from the
   candidate (disk count: 0).
4. Chapter 2 heading grade: seed's `#` chapter heading rendered
   as `##` to sit under the document's single `#` title;
   heading is integration apparatus, not seed body — the
   sacrosanct block starts at §2.0 and is byte-exact.
5. Renumbering: seed already speaks in final numbering (§2.x
   internal, "section 17" for succession), so Chapter 2 was NOT
   renumbered; only the predecessor body was.
6. First-seen survival: retained in §8.4 as medium-tier
   description re-marked per R9 (never an evaluator wall);
   remaining occurrences are census apparatus naming the repair.
7. "Economic" appears twice, both in the appendix naming the
   register the C-13 repair removed — register law binds the
   specification voice; the census names what was removed.

## Register checks (from disk)

- ALL-CAPS census: BCP 14 keywords + proper nouns/initialisms
  only (ACDC, AID, BCP, CESR, GARD, GEL, KEL, KERI, RFC, SAID,
  TEL); no rhetorical caps.
- Economics vocabulary: amortiz*/cheap/expensive — 0 in the
  document voice (see seam 7 for the two census mentions of
  "economic register").
- No section reference > 19 survives anywhere (renumber
  post-check: empty).

## OPEN items (stated plainly, not papered over)

1. R11 three-artifact coupling: the abstract's replay sentence
   is repaired here; the public repository README quotation and
   the verify-kernel check are OUTSIDE this assembly's write
   surface and must move together at publication — NOTED for
   the ratifying authority per the brief.
2. The committed census generator (census-is-a-program law) run
   against final-form bytes is a ceremony gate of the gauntlet,
   not discharged by this assembly; the appendix confesses this.
3. Held open by manifest law and NOT closed by drafting: R19
   seat shape; the carriage encoding (group round, non-gating);
   the dossier-inheritance question at gate one.
4. Section 19 is recomposed content from 42-compact-form-gates.md
   (content-not-file-verbatim, as the brief directs); it is new
   prose of this edition and should be gauntleted as such.

## Files written

Exactly two, per the brief: weave/custos-4.2-candidate-v1.md
and this report. staged-repos/custos/ untouched (read-only).
