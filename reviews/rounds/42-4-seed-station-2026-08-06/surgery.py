#!/usr/bin/env python3
"""Seed-station round 42-4: v2 -> v3 minimal byte surgery.

Three enumerated exact-match substitutions (R-1, R-2, R-3), each
asserted exactly-once against the verified v2 bytes. Everything
else byte-identical.
"""
import hashlib

V2 = "weave/42-taxonomy-chapter-v2.md"
V3 = "weave/42-taxonomy-chapter-v3.md"
V2_SHA = "dfd1ddc1a092225470d2e075c0ad7eec55a4d10e892f38501d763212fcd2bd9a"

data = open(V2, "rb").read()
assert hashlib.sha256(data).hexdigest() == V2_SHA, "v2 digest mismatch — STOP"
text = data.decode("utf-8")

# The sacrosanct Utah exhibit sentence (USER-GATE): captured verbatim,
# verified untouched after surgery.
UTAH = (
    "Legislatures have\n"
    "begun to require, in prose, what no prose can deliver: that a\n"
    "predicate be verifiable without disclosure of its evidence, and\n"
    "that the authority issuing the underlying credential be barred\n"
    "from watching it being used (such as Utah's enrolled\n"
    "digital-identity statutes, which mandate age verification \"without\n"
    "revealing the individual's age or date of birth\" and place the\n"
    "endorsing department under an audit-checked bar on monitoring\n"
    "presentations; register, byte-grade)."
)
assert text.count(UTAH) == 1, "Utah exhibit sentence not located exactly once"

SUBS = [
    # R-1 (authority: GF-1 / N2(A5) / SF-2 — BLOCKING): issuer
    # non-observation is a surface obligation, not a type property.
    # Site: seed \u00a72.7, v2 lines 362-367.
    (
        "Where a mandate of the \u00a72.0 class additionally bars the issuing\n"
        "authority from observing use, the bar is discharged by type\n"
        "rather than by audit alone: under regime-side color a registered\n"
        "act carries no meaning of its own, meaning is computed at\n"
        "the consuming frame, and the issuer is structurally outside that\n"
        "computation \u2014 there is nothing to phone home about. And where\n",
        "Where a mandate of the \u00a72.0 class additionally bars the issuing\n"
        "authority from observing use, the type argument proves exactly\n"
        "what it proves: under regime-side color meaning is computed at\n"
        "the consuming frame, so no clause of committed law can require\n"
        "issuer contact. The bar on observation is discharged only where\n"
        "the verification path itself avoids issuer-observable surfaces \u2014\n"
        "evidence acquired from non-issuer witnesses or caches, no\n"
        "resolution through issuer-published endpoints during appraisal,\n"
        "presentation registries, where used, holder-controlled.\n"
        "Transport-surface observation is a deployment property, testable\n"
        "at the acquisition path; a mandate of this class binds the path,\n"
        "not just the semantics. And where\n",
    ),
    # R-2 (authority: SF-1 / S3-3 — "the conflation is the defect"):
    # the \u00a72.4 presentation-form conflation. Site: v2 lines 193-195.
    (
        "not in the ground and does not travel. A finding is disclosed\n"
        "*instead of* its evidence; a no-disclosure mandate is discharged\n"
        "by construction rather than by promise.\n",
        "not in the ground and does not travel. A finding disclosed in\n"
        "place of its evidence is lawful under one of the three\n"
        "presentation forms the objects section of this standard types \u2014\n"
        "replayed, warranted, or proven \u2014 and which form a no-disclosure\n"
        "mandate accepts is the mandate's own committed choice.\n",
    ),
    # R-3 (authority: SF-3): the \u00a72.8 confession list completes —
    # exactly two entries. Site: v2 line 393.
    (
        "narrowed-jury trade is confessed, not solved. The ur-element theorem of\n",
        "narrowed-jury trade is confessed, not solved. This chapter does\n"
        "not claim that type-level locality closes transport-level\n"
        "observation; the surface obligation a mandate of the \u00a72.0 class\n"
        "carries is stated where \u00a72.7 defines the posture. Clause-selective\n"
        "consumption depends on the presentation machinery the objects\n"
        "section types; the postures of this chapter name what is\n"
        "disclosed, never how a disclosure is proven. The ur-element theorem of\n",
    ),
]

for i, (old, new) in enumerate(SUBS, 1):
    n = text.count(old)
    assert n == 1, f"substitution {i}: old text found {n} times (need exactly 1)"
    text = text.replace(old, new)

# Post-surgery checks
assert text.count(UTAH) == 1, "Utah sentence damaged"
assert "discharged by type" not in text, "'discharged by type' survived"
assert "phone home" not in text, "'phone home' survived"
assert "replayed, warranted, or proven" in text
assert text.count("This chapter does\nnot claim that type-level locality") == 1

open(V3, "wb").write(text.encode("utf-8"))
out = open(V3, "rb").read()
print("v3 sha256:", hashlib.sha256(out).hexdigest())
print("v3 lines:", out.decode().count("\n"))
print("OK: all substitutions applied exactly once; all assertions passed")
