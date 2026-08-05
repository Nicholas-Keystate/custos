#!/usr/bin/env python3
# Apache-2.0. Part of the Custos standard's tooling.
"""verify_vectors.py — integrity checks over the conformance vector ledger.

The ledger is a corpus, not a harness: it states input shapes and
expected results, and any implementation can be run against it by
anyone. This tool proves the ledger's own integrity, never an
engine's conformance. Checks (all stdlib, run from the repo root):

  1. the ledger parses, carries schema 1, and every vector has the
     required fields with values in the permitted sets;
  2. vector identifiers are well formed and unique;
  3. every source the ledger cites is present and its SHA-256
     matches the pin recorded here (the ledger is bound to the
     bytes it was derived from, not to a path);
  4. every station obligation assigned by the ratified edition and
     the ruling records carries at least one vector — the coverage
     check, and the reason this file exists;
  5. every held vector names what it is held on, and no
     specifiable vector carries a hold;
  6. no vector claims byte grade while the carriage encoding is
     unratified (R5's interim discipline, tracker #57).

Exit 0 = all checks pass. Nonzero = at least one FAIL.
"""
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEDGER = ROOT / "vectors" / "ledger.json"

ID_RE = re.compile(r"^V-[A-Z0-9]{2,4}-\d{2}$")
REQUIRED = ("id", "family", "owed_by", "input", "expect", "grade", "status")
GRADES = {"semantic", "byte"}
STATUSES = {"specifiable", "held"}

# Every station obligation the ratified edition and the ruling
# records assign, as (source id, ruling label). A ruling that
# assigns an obligation and has no vector is the gap this check
# exists to catch; adding a ruling here without a vector fails the
# build, which is the intended direction of pressure.
OBLIGATIONS = [
    ("edition-4.1", "section 17, L2208-2211"),
    ("edition-4.1", "section 17, L2288-2289"),
    ("edition-4.1", "section 17, L2289-2296"),
    ("edition-4.1", "section 17, L2298-2300"),
    ("edition-4.1", "section 17, L2300-2302"),
    ("record-2026-07-30", "R1"),
    ("record-2026-07-30", "R2"),
    ("record-2026-07-30", "R3"),
    ("record-2026-07-30", "R6"),
    ("record-2026-07-30", "R8"),
    ("record-2026-07-30", "R9"),
    ("record-2026-07-30", "R10"),
    ("record-2026-07-30", "R11"),
    ("supplement-2", "R13"),
    ("supplement-2", "R14"),
    ("supplement-2", "R15"),
    ("supplement-2", "R17"),
    ("supplement-2", "R18"),
    ("supplement-2", "R20"),
    ("supplement-2", "11a"),
    ("supplement-3", "S3-1"),
    ("supplement-3", "S3-3"),
    ("supplement-3", "S3-4"),
    ("supplement-3", "S3-5"),
    ("supplement-3", "S3-7"),
    ("supplement-3", "S3-9"),
]

results = []


def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if not LEDGER.exists():
        check("ledger present", False, f"{LEDGER} not found")
        return
    try:
        ledger = json.loads(LEDGER.read_text())
    except json.JSONDecodeError as exc:
        check("ledger parses", False, str(exc))
        return
    check("ledger parses", True, f"{LEDGER.relative_to(ROOT)}")

    check("schema version", ledger.get("schema") == 1, f"schema={ledger.get('schema')}")

    vectors = ledger.get("vectors", [])
    families = set(ledger.get("families", {}))
    sources = {s["id"]: s for s in ledger.get("sources", [])}

    # 1 and 2 — shape and identity.
    bad_fields, bad_ids, bad_family, bad_source = [], [], [], []
    seen = set()
    for v in vectors:
        vid = v.get("id", "<no id>")
        if any(f not in v for f in REQUIRED):
            bad_fields.append(vid)
        if not ID_RE.match(str(vid)) or vid in seen:
            bad_ids.append(vid)
        seen.add(vid)
        if v.get("family") not in families:
            bad_family.append(vid)
        if v.get("owed_by", {}).get("source") not in sources:
            bad_source.append(vid)
        if v.get("grade") not in GRADES or v.get("status") not in STATUSES:
            bad_fields.append(vid)
    check("vector fields complete and typed", not bad_fields, ", ".join(sorted(set(bad_fields))))
    check("vector ids well formed and unique", not bad_ids, ", ".join(map(str, bad_ids)))
    check("families declared", not bad_family, ", ".join(bad_family))
    check("owing sources declared", not bad_source, ", ".join(bad_source))
    check("corpus non-empty", bool(vectors), f"{len(vectors)} vectors")

    # 3 — the ledger is bound to bytes, not to paths.
    drifted, missing = [], []
    for sid, s in sources.items():
        path = ROOT / s["path"]
        if not path.exists():
            missing.append(sid)
        elif sha256(path) != s["sha256"]:
            drifted.append(f"{sid} ({s['path']})")
    check("cited sources present", not missing, ", ".join(missing))
    check("cited sources match their pins", not drifted, ", ".join(drifted))

    # 4 — coverage, the check this file exists for.
    covered = {(v.get("owed_by", {}).get("source"), v.get("owed_by", {}).get("ruling")) for v in vectors}
    uncovered = [f"{s}:{r}" for s, r in OBLIGATIONS if (s, r) not in covered]
    check(
        "every assigned station obligation carries a vector",
        not uncovered,
        ", ".join(uncovered) if uncovered else f"{len(OBLIGATIONS)} obligations covered",
    )

    # 5 — holds are named.
    unnamed = [v["id"] for v in vectors if v.get("status") == "held" and not v.get("held_on")]
    stray = [v["id"] for v in vectors if v.get("status") == "specifiable" and v.get("held_on")]
    check("held vectors name their hold", not unnamed, ", ".join(unnamed))
    check("specifiable vectors carry no hold", not stray, ", ".join(stray))

    # 6 — R5's interim grade discipline.
    byte_claims = [v["id"] for v in vectors if v.get("grade") == "byte"]
    encoding_ratified = bool(ledger.get("grade_discipline", {}).get("byte_grade_available"))
    check(
        "no byte-grade expectation before the encoding ratifies",
        encoding_ratified or not byte_claims,
        ", ".join(byte_claims),
    )

    held = [v for v in vectors if v.get("status") == "held"]
    print(
        f"\n{len(vectors)} vectors across {len(families)} families; "
        f"{len(vectors) - len(held)} specifiable, {len(held)} held."
    )


def finish():
    failed = [name for name, ok, _ in results if not ok]
    print(f"\n{len(results) - len(failed)}/{len(results)} checks pass")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
    finish()
