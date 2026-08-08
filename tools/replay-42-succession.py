#!/usr/bin/env python3
# replay-42-succession.py — the 4.2 ratification's conformance
# vector, PUBLISHED FORM (finding #76, part 2). A stranger holding
# only this repository re-runs every check the ceremony's cited
# "first conformance vector" ran, except the two KEL-seal checks,
# which need the authority's key event log and are confessed below
# rather than silently skipped: the KEL is device-held by design
# (the anchors are the authority's to prove; the lineage record
# states the coordinates sn 191/192 and the seal SAIDs any KEL
# copy must exhibit). Everything else derives from published
# bytes. Requires: keripy (WebOfTrust, main) for SAID computation;
# pure-hash checks run even without it.
import sys, os, json, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def P(rel): return os.path.join(ROOT, rel)

ok = True
def chk(name, cond):
    global ok
    print(('[PASS] ' if cond else '[FAIL] ') + name)
    ok = ok and cond

try:
    from keri.core.coring import Diger
    HAVE_KERI = True
except ImportError:
    HAVE_KERI = False
    print("[NOTE] keripy unavailable — SAID recomputation checks skipped;"
          " sha256 checks still run (install WebOfTrust/keripy main for the full vector)")

def said_of(rel):
    return Diger(ser=open(P(rel), 'rb').read()).qb64
def sad_said(obj):
    c = dict(obj); c['d'] = "#" * 44
    return Diger(ser=json.dumps(c, indent=1).encode()).qb64

so = json.load(open(P("lineage/succession-object-4.1-to-4.2.json")))
em = json.load(open(P("lineage/evidence-manifest-4.1-to-4.2.json")))
ra = json.load(open(P("lineage/ratification-act-4.1-to-4.2.json")))
ea = json.load(open(P("lineage/effectiveness-act-4.1-to-4.2.json")))
lr = json.load(open(P("lineage/lineage-record-4.1-to-4.2.json")))

# 1. document digests from published bytes
doc = open(P("spec/custos-4.2.md"), 'rb').read()
chk("successor sha256 matches published bytes",
    hashlib.sha256(doc).hexdigest() == so['successor_sha256'])
pred = open(P("spec/custos-4.1.md"), 'rb').read()
chk("predecessor sha256 matches published bytes",
    hashlib.sha256(pred).hexdigest() == so['predecessor_sha256'])

if HAVE_KERI:
    chk("succession object SAID recomputes", sad_said(so) == so['d'])
    chk("successor SAID matches bytes", Diger(ser=doc).qb64 == so['successor_said'])
    chk("predecessor SAID matches bytes", Diger(ser=pred).qb64 == so['predecessor_said'])
    chk("evidence manifest SAID recomputes",
        sad_said(em) == em['d'] == so['evidence_manifest_said'])
    chk("ratification act SAID recomputes", sad_said(ra) == ra['d'])
    chk("effectiveness act SAID recomputes", sad_said(ea) == ea['d'])
    # 2. EVERY evidence leg from published bytes (the #76 repair:
    # all 16 legs are now in this repository)
    LEGS = {
     "input-manifest": "weave/42-input-manifest.md",
     "seed-graduation": "reviews/rounds/42-1-taxonomy-gauntlet-2026-07-31/round-design.md",
     "regen-brief": "weave/42-regen-brief.md",
     "regen-report": "weave/42-regen-report.md",
     "collider-brief": "reviews/rounds/42-2-integration-review-2026-08-03/review-brief.md",
     "collider-sol": "reviews/rounds/42-2-integration-review-2026-08-03/sol-leg-findings.md",
     "collider-fable": "reviews/rounds/42-2-integration-review-2026-08-03/fable-leg-findings.md",
     "collider-collation": "reviews/rounds/42-2-integration-review-2026-08-03/collation.md",
     "supplement-3": "reviews/ruling-record-supplement-3-2026-08-03.md",
     "repair-report": "weave/42-repair-report.md",
     "gauntlet-design": "reviews/rounds/42-3-full-gauntlet-2026-08-05/round-design.md",
     "gauntlet-report": "reviews/rounds/42-3-full-gauntlet-2026-08-05/gauntlet-report.md",
     "station-record": "reviews/rounds/42-4-seed-station-2026-08-06/station-record.md",
     "regauntlet-report": "reviews/rounds/42-5-targeted-regauntlet-2026-08-06/regauntlet-report.md",
     "census-verifier": "lineage/census-42-as-run.py",
     "seed-of-record": "weave/42-taxonomy-chapter-v3.md",
    }
    n = 0
    for tag, rel in LEGS.items():
        got = said_of(rel)
        want = em['reviews'][tag]['said']
        if got == want: n += 1
        else: print(f"    [leg MISMATCH] {tag}: {got} != {want}")
    chk(f"evidence legs replay from published bytes ({n}/16)", n == 16)
    # 3. lineage id + coordinates
    lid = Diger(ser=(so['predecessor_said'] + so['authority_aid']).encode()).qb64
    chk("lineage id derives from predecessor+authority",
        lid == ra['lineage_id'] == lr['lineage_id'])

chk("acts cite the succession object",
    ra['succession_object_said'] == so['d'] == ea['succession_object_said'])
chk("effectiveness cites ratification coordinate sn 191",
    ea['ratification']['coordinate']['sn'] == 191)
chk("lineage record coordinates: rat 191 / eff 192",
    lr['entries'][0]['ratification_coordinate']['sn'] == 191 and
    lr['entries'][1]['effectiveness_coordinate']['sn'] == 192)

print()
print("KEL-SEAL CHECKS (2): NOT RUN — the authority's key event log is"
      " device-held by design. The claim a KEL copy must satisfy:"
      f" the ixn at sn 191 carries a SealRoot rd == {ra['d']};"
      f" the ixn at sn 192 carries a SealRoot rd == {ea['d']}.")
print()
print("REPLAY:", "GREEN — the succession derives from published bytes"
      if ok else "RED")
sys.exit(0 if ok else 1)
