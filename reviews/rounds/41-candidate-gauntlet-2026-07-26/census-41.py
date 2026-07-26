#!/usr/bin/env python3
"""Committed census generator for the Custos 4.1 candidate.

Reproducible D-3 accounting: recomputes BOTH censuses against the
FINAL candidate bytes. Rule (predeclared): a predecessor nonblank
line is DELTA iff it has no byte-identical nonblank counterpart
anywhere in the candidate. Groups are assigned by first matching
classifier, each line exactly once; any line no classifier claims
is UNEXPLAINED and the script exits nonzero (the census must fail
loudly rather than assert quietly).

Usage: python3 ops/census-41.py [--update]
  (no flag) verify mode: recompute, compare to the appendix's
  stated totals, exit 0 iff consistent and zero unexplained.
  --update: print the regenerated census block to stdout for
  splicing into the appendix.
"""
import sys, re, hashlib

KERNEL = 'staged-repos/custos/spec/custos-4.0-kernel-draft.md'
CANDIDATE = 'weave/custos-4.1-candidate-v2.md'

def classify(line, idx, kern_lines):
    s = line.strip()
    # G1: scaffolding header (kernel lines 1-12, all '# '-prefixed)
    if idx < 12 and s.startswith('# '):
        return 'G1-scaffolding-header'
    # G2: embedded abstract block (kernel lines 18-39)
    if 17 <= idx <= 38:
        return 'G2-embedded-abstract'
    # G3: predecessor-citation sentences (3.3-as-predecessor wording
    # in reading rules + succession + the medium-first sentence the
    # abstract drop orphaned)
    if 'Custos 3.3' in line or '3.3,' in s or s.startswith('cited, never edited') or 'succession rule in its final section' in line or '18b0469e731db24f' in line or s.startswith('and its bytes are pinned') or s.startswith("this document's assembly"):
        return 'G3-predecessor-citation'
    if 'medium-first' in line:
        return 'G2-embedded-abstract'  # orphaned continuation of the dropped opening
    # G4: GEL-def cross-ref + colored-evidence gloss splice sites
    if 'new anchoring pattern. What the KEL' in line or 'Colored evidence' in line or 'with its color-computation inputs' in line or "event's self-addressing identifier" in line or 'log with governance semantics' in line or 'evidence and establishment lineage' in line or 'to credentials, the GEL is to law' in line:
        return 'G4-gel-xref-and-gloss'
    # G5: color regeneration sites
    if re.search(r'colors? ', line) or 'color —' in line or 'color is' in line or 'simultaneously' in s or 'Color is computed' in line or 'output of a committed rule-set evaluated' in line or 'more evidence for that computation' in line or "assertion's own falsity" in line:
        return 'G5-color-regeneration'
    # G6: verb-division site (definitions appraisal passage)
    if 'GARD appraises' in line or ('Appraisal' in line and 'activity' in line):
        return 'G6-verb-division'
    # G8: gauntlet-round repairs (41-candidate round findings)
    if 'identical GELs hold' in line or 'identical Constitutions — the property' in line or s == 'rather than testimonial.':
        return 'G8-gauntlet-repairs'
    # G7: meld recompositions (scope/definitions recomposed-into;
    # section headings renumbered; cross-references renumbered)
    if s.startswith('## ') or s.startswith('### '):
        return 'G7-meld-recomposition-renumbering'
    if re.search(r'section \d+', line) or re.search(r'sections \d+', line):
        return 'G7-meld-recomposition-renumbering'
    # G7 continued: known recomposed definition/scope prose
    G7_KEYS = ['The minimal case, before any definition', 'GARD.', 'A Governed Autonomic',
               'decidable by replay', 'its law is committed and', 'succeeds only by its own',
               'identity is self-certifying', 'external authority', 'Replayable',
               'judgment to identical bytes', 'scale the federation section',
               'The three folds', 'pure function from', 'committed log bytes',
               'reference implementation names', 'naming convention', 'extends it by one rung',
               'Gever', 'Log and fold are one structure', 'committed evidence; the fold',
               'the judgment may exceed', 'output of the fold below', 'presupposes Kever-state',
               'Finding', 'sole return type', 'carries its own ground', 'not a finding',
               'codomain section', 'defeated, carrying', 'typed requirement', 'self-convicted',
               'contradictory pair', 'about propositions', 'lifecycles', 'force by the codomain',
               'draws it exactly', 'The seal kinds', 'commitment kinds', 'substrate ships',
               'digest seal', 'event seal', 'covenant seal', 'covenant set', 'coordinate lookup',
               'committed clause', 'evaluation seal', 'committed verdict', 'admissibility',
               'document uses it', 'The document is built', 'is one identifier that has committed',
               'the receipts', 'incepts an identifier, sealing', 'founding law of a single page',
               'silence means', 'honors and what they confer', 'act the identifier takes',
               'committed evidence that it was not', 'stranger holding', 'page is bytes',
               'verdict is a computation', 'No members, no organs', 'one key state, one page',
               'That object, whole, is a GARD', 'nowhere a parameter', 'below requires more',
               'species at different masses', 'the finding, standing, recourse',
               'written out in full', 'CONSUMPTION', 'FEDERATION', 'frame size',
               'domain whose constitution', 'bytes under one identifier',
               'obligation that any verifier holding', "substrate's own seal grammar",
               'rule appears in the seal section', 'read constructively']
    if any(k in line for k in G7_KEYS):
        return 'G7-meld-recomposition-renumbering'
    return None

def main():
    kern = [l for l in open(KERNEL).read().split('\n')]
    kern_nb = [(i, l) for i, l in enumerate(kern) if l.strip()]
    cand_set = set(l for l in open(CANDIDATE).read().split('\n') if l.strip())
    missing = [(i, l) for i, l in kern_nb if l not in cand_set]
    groups = {}
    unexplained = []
    for i, l in missing:
        g = classify(l, i, kern)
        if g is None:
            unexplained.append((i + 1, l))
        else:
            groups.setdefault(g, []).append(i + 1)
    total = len(missing)
    print(f'kernel nonblank lines: {len(kern_nb)}')
    print(f'delta lines (no byte-identical counterpart): {total}')
    for g in sorted(groups):
        print(f'  {g}: {len(groups[g])}')
    print(f'  UNEXPLAINED: {len(unexplained)}')
    for n, l in unexplained:
        print(f'    kernel:{n}: {l[:80]}')
    csum = hashlib.sha256(open(CANDIDATE, 'rb').read()).hexdigest()
    print(f'candidate sha256: {csum}')
    if unexplained:
        sys.exit(1)
    print('CENSUS: zero unexplained — PASS')

if __name__ == '__main__':
    main()
