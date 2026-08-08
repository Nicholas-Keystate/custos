#!/usr/bin/env python3
# census-42.py — ceremony gate for the custos-4.2 succession.
# Law (4.1 appendix, carried into 4.2): "The census verifier is a
# ceremony gate: it runs green against the exact ceremony bytes,
# invoked with the ceremony digest pinned, before any anchor is
# made." This verifier checks the WHOLE v1->v5 lineage from disk
# bytes: every recorded digest, the seed succession chain, the
# census-chain structure, sacrosanct spans, and the accounting
# counts. Exit 0 = green.
import hashlib, re, sys

SA = "/Users/hun-magnon/Documents/KERI/standard-annealing"
def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()

FAIL = []
def check(name, cond, detail=""):
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f" — {detail}" if detail and not cond else ""))
    if not cond: FAIL.append(name)

# ---- 1. The candidate lineage, every edition on disk at its digest ----
CHAIN = [
    ("v1 (assembly + authority line-21 edit)",
     f"{SA}/weave/custos-4.2-candidate-v1.md",
     "8b4f701a4446c4e3899f0f6ed113ce480153c03f541e22b0e773a67bc27c6c8d"),
    ("v2 (supplement-3 repair pass, 74 subs)",
     f"{SA}/weave/custos-4.2-candidate-v2.md",
     "a11f2902c6e18404ba22c9468681e8a92b57af01fe1de53b08dbabb2d5c786f0"),
    ("v3 (42-3 micro-pass, 8 subs)",
     f"{SA}/weave/custos-4.2-candidate-v3.md",
     "cd16f4ba46c861713a2bfc201ae2424f54809de4f8c0173a37410a95ca04a705"),
    ("v4 (seed-v3 succession splice)",
     f"{SA}/weave/custos-4.2-candidate-v4.md",
     "a9ac1ed5adf0d0ce85c993b7ecb6d459e4192c0d60efc09a93dccb8f91439c89"),
    ("v5 (42-5 bookkeeping, 12 subs) — CEREMONY SUBJECT",
     f"{SA}/weave/custos-4.2-candidate-v5.md",
     "68cc5c9b7164b33dffcf7b705a0d1301fe108c647d35638fec61d52d29b2775a"),
]
for name, path, want in CHAIN:
    try:
        got = sha(path)
        check(f"lineage: {name}", got == want, f"got {got[:16]}")
    except FileNotFoundError:
        check(f"lineage: {name}", False, "missing")

# ---- 2. The seed succession chain ----
SEEDS = [
    ("seed v2 (graduated, round 42-1)",
     f"{SA}/weave/42-taxonomy-chapter-v2.md",
     "dfd1ddc1a092225470d2e075c0ad7eec55a4d10e892f38501d763212fcd2bd9a"),
    ("seed v3.1 (station 42-4 + re-graduation + RG-1 bookkeeping)",
     f"{SA}/weave/42-taxonomy-chapter-v3.md",
     "5cef4ac8249365dac497c8f19b9b0009fc5b4fa51e7fadb0f5fb520a88345830"),
]
for name, path, want in SEEDS:
    got = sha(path)
    check(f"seed: {name}", got == want, f"got {got[:16]}")

# seed-of-record body must sit inside v5 verbatim
v5 = open(CHAIN[-1][1], encoding='utf-8').read()
s3 = open(SEEDS[1][1], encoding='utf-8').read().split('\n')
v2s = open(SEEDS[0][1], encoding='utf-8').read().split('\n')
start_anchor, end_anchor = v2s[25], v2s[400]
i, j = s3.index(start_anchor), s3.index(end_anchor)
body = '\n'.join(s3[i:j+1])
check("seed body (v3.1 coordinates) verbatim in v5", body in v5)
check("superseded seed v2 body ABSENT from v5",
      '\n'.join(v2s[25:401]) not in v5)

# ---- 3. Sacrosanct spans ----
for s, n in [("KERI detects; a GARD adjudicates.", 1),
             ("Her computed answer testifies.", 1),
             ("receipt of performed governance", 2),
             ("the compact form changes cost, never meaning", 1)]:
    check(f"sacrosanct [{s[:30]}...] count {n}", v5.count(s) == n,
          f"got {v5.count(s)}")
check("sacrosanct [acts-and-is-held wrapped]",
      len(re.findall(r"acts, and is held to account, by the same committed\njudgments", v5)) == 1)
check("authority edit: line 21 'KERI ends'",
      'KERI ends' in v5.split('\n')[20])

# ---- 4. Census chain structure (seven sections, counts) ----
heads = re.findall(r'^###? .*[Cc]ensus.*$', v5, re.M)
check("census sections >= 7 (3 assembly + repair + v3 + v4 + v5)",
      len(heads) >= 7, f"got {len(heads)}: {heads}")
check("repair census: 74 rows",
      len(re.findall(r'^\| [A-Z]\d+[a-z]? \| S3-', v5, re.M)) == 74,
      f"got {len(re.findall(r'^[|] [A-Z]0-9+', v5, re.M))}")
check("v3 micro-pass census: 8 rows",
      len(re.findall(r'^\| V3-\d \| GF-\d \|', v5, re.M)) == 8)
check("v5 bookkeeping census present",
      'v5 bookkeeping census' in v5)
check("v4 seed-succession census present",
      'v4 seed-succession census' in v5)

# ---- 5. Defect extinctions (the ceremony bytes carry no convicted text) ----
for pat, why in [("discharged by type", "GF-1/N2"),
                 ("six walls", "GF-2"),
                 ("colored receipt", "participle law"),
                 ("the\nKERI's", "GF-5")]:
    check(f"extinct: '{pat[:24]}' ({why})", pat not in v5)
check("no economics vocabulary (cheap/expensive/amortiz)",
      not re.search(r'\b(cheap|expensive|amortiz)\w*', v5[:v5.find('### Delta census')], re.I))

# ---- 6. Predecessor pin ----
check("4.1 of record at its ratified digest",
      sha(f"{SA}/staged-repos/custos/spec/custos-4.1.md") ==
      "ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05")
check("4.1 digest cited in v5 head",
      "ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05" in v5[:1200])

print()
if FAIL:
    print(f"CENSUS GATE: RED — {len(FAIL)} failure(s): {FAIL}")
    sys.exit(1)
print("CENSUS GATE: GREEN — ceremony may proceed against",
      hashlib.sha256(v5.encode()).hexdigest())
