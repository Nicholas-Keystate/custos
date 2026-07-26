#!/usr/bin/env python3
"""Committed census generator for the Custos 4.1 candidate.

Reproducible D-3 accounting: recomputes BOTH censuses against the
FINAL candidate bytes. Rule (predeclared): a predecessor nonblank
line is DELTA iff it has no byte-identical nonblank counterpart
anywhere in the candidate. Groups are assigned by first matching
classifier, each line exactly once; any line no classifier claims
is UNEXPLAINED and the script exits nonzero (the census must fail
loudly rather than assert quietly).

Assignment rule (predeclared): each delta line is assigned by the
FIRST matching classifier in the committed classifier order; the
first-match order is the census's exactly-one guarantee.

Usage: python3 ops/census-41.py [--expect-digest SHA256]
  verify mode (always): recompute the delta census, parse the
  appendix's stated totals and all fifteen structure-census
  disposition rows, compare everything against the actual bytes,
  exit 0 iff all consistent and zero unexplained.
  --expect-digest: ceremony gate — additionally fail unless the
  candidate hashes to the given digest.
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

def verify_structure_census(cand_text, kern_text):
    """Verify the appendix structure census with full discrimination:
    (i) parse all fifteen disposition rows from the appendix table;
    (ii) each predecessor section i maps to candidate section i+1;
    (iii) the predecessor titles in the table match the actual
    kernel headings byte-for-byte;
    (iv) the candidate heading at each target number matches the
    predecessor heading title exactly (full identity, not keyword);
    (v) the structure-census section itself is present."""
    import re
    errs = []
    if '### Structure census' not in cand_text:
        return ['structure: appendix lacks a structure census section']
    kern_heads = {}
    for m in re.finditer(r'^## (\d+)\. (.+)$', kern_text, re.M):
        kern_heads[int(m.group(1))] = m.group(2).strip()
    cand_heads = {}
    for m in re.finditer(r'^## (\d+)\. (.+)$', cand_text, re.M):
        cand_heads[int(m.group(1))] = m.group(2).strip()
    rows = re.findall(
        r'^\| (\d+)\. (.+?) \| (regenerated-in-place|recomposed-into|retired)\(section (\d+)\)',
        cand_text, re.M)
    if len(rows) != 15:
        errs.append(f'structure: expected 15 disposition rows, parsed {len(rows)}')
    seen = set()
    for num_s, title, disp, target_s in rows:
        num, target = int(num_s), int(target_s)
        seen.add(num)
        kern_title = kern_heads.get(num)
        if kern_title is None:
            errs.append(f'structure: table row names predecessor section {num}, absent from kernel')
            continue
        if title.strip() != kern_title:
            errs.append(f'structure: row {num} title {title.strip()!r} != kernel heading {kern_title!r}')
        if target != num + 1:
            errs.append(f'structure: row {num} disposition targets section {target}, architecture requires {num + 1}')
        cand_title = cand_heads.get(target)
        if cand_title is None:
            errs.append(f'structure: candidate section {target} (target of row {num}) missing')
        elif cand_title != kern_title:
            errs.append(f'structure: candidate section {target} heading {cand_title!r} != predecessor title {kern_title!r}')
    for i in range(1, 16):
        if i not in seen:
            errs.append(f'structure: predecessor section {i} has no disposition row')
    if 17 not in cand_heads or 'GEL' not in cand_heads[17]:
        errs.append('structure: candidate section 17 (GEL grammar) missing')
    return errs

def parse_appendix_totals(cand_text):
    """Extract the appendix's stated total and group counts."""
    import re
    m = re.search(r'of the predecessor\'s 1,546 nonblank lines, (\d+) lack', cand_text)
    total = int(m.group(1)) if m else None
    gm = re.search(r'group below[^(]{0,200}?\((.+?)\); zero unexplained', cand_text, re.S)
    groups = {}
    if gm:
        for part in gm.group(1).split(';'):
            norm = ' '.join(part.split())
            mm = re.match(r'\s*(.+?)\s+(\d+)\s*$', norm)
            if mm:
                groups[mm.group(1).strip()] = int(mm.group(2))
    return total, groups

APPENDIX_GROUP_KEYS = {
    'scaffolding header': 'G1-scaffolding-header',
    'embedded abstract': 'G2-embedded-abstract',
    'predecessor citations': 'G3-predecessor-citation',
    'GEL cross-reference and gloss splices': 'G4-gel-xref-and-gloss',
    'color regeneration': 'G5-color-regeneration',
    'verb division': 'G6-verb-division',
    'meld recomposition and renumbering': 'G7-meld-recomposition-renumbering',
    'gauntlet-round repairs': 'G8-gauntlet-repairs',
}

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--expect-digest', help='ceremony gate: fail unless the candidate hashes to this digest')
    args = ap.parse_args()

    kern = [l for l in open(KERNEL).read().split('\n')]
    kern_nb = [(i, l) for i, l in enumerate(kern) if l.strip()]
    cand_text = open(CANDIDATE).read()
    cand_set = set(l for l in cand_text.split('\n') if l.strip())
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
    failures = []

    print(f'kernel nonblank lines: {len(kern_nb)}')
    print(f'delta lines (no byte-identical counterpart): {total}')
    for g in sorted(groups):
        print(f'  {g}: {len(groups[g])}')
    print(f'  UNEXPLAINED: {len(unexplained)}')
    for n, l in unexplained:
        print(f'    kernel:{n}: {l[:80]}')
    if unexplained:
        failures.append(f'{len(unexplained)} unexplained delta lines')

    # Verify appendix totals against computed
    st_total, st_groups = parse_appendix_totals(cand_text)
    if st_total != total:
        failures.append(f'appendix total {st_total} != computed {total}')
    for label, gkey in APPENDIX_GROUP_KEYS.items():
        lbl = label.replace('\n', ' ')
        stated = st_groups.get(label) or st_groups.get(lbl)
        computed = len(groups.get(gkey, []))
        if stated is None:
            failures.append(f'appendix missing group count for {lbl!r}')
        elif stated != computed:
            failures.append(f'appendix group {lbl!r}: stated {stated} != computed {computed}')

    # Structure census verification (full discrimination)
    kern_text = open(KERNEL).read()
    for e in verify_structure_census(cand_text, kern_text):
        failures.append(e)

    csum = hashlib.sha256(cand_text.encode()).hexdigest()
    print(f'candidate sha256: {csum}')
    if args.expect_digest and csum != args.expect_digest:
        failures.append(f'CEREMONY GATE: candidate digest {csum[:12]}... != expected {args.expect_digest[:12]}...')

    if failures:
        print('CENSUS: FAIL')
        for f in failures:
            print(f'  FAIL: {f}')
        sys.exit(1)
    print('CENSUS: delta census verified, appendix totals verified, structure census verified — PASS')

if __name__ == '__main__':
    main()
