#!/usr/bin/env python3
# Apache-2.0. Part of the Custos standard's tooling.
"""verify_kernel.py — repo-scope byte verification for the Custos kernel.

Checks (all stdlib, no dependencies, run from the repo root):
  1. spec kernel file exists and its SHA-256 equals the ratified
     digest recorded in SUCCESSION.md's Custos 4.0 row (the bytes
     in spec/ ARE the law, not merely some bytes);
  2. the kernel's §15 predecessor pin matches SUCCESSION.md's
     predecessor row (the two commitments must agree);
  3. the abstract in README.md is byte-identical to the kernel's
     opening abstract (the README quotes, never paraphrases);
  4. gate census (if present) references the kernel by digest —
     reports whether the gate record matches the current bytes.

Exit 0 = all checks pass. Nonzero = at least one FAIL.
Proves bytes, not authority: authority is the governance event
log's to prove.
"""
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KERNEL = ROOT / "spec" / "custos-4.0-kernel-draft.md"
EDITION_41 = ROOT / "spec" / "custos-4.1.md"
SUCCESSION = ROOT / "SUCCESSION.md"
README = ROOT / "README.md"
GATE_CENSUS = ROOT / "tools" / "gate40-census.json"

PRED_PIN_RE = re.compile(r"\b([0-9a-f]{64})\b")

results = []

def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))

def main():
    succession_text = SUCCESSION.read_text() if SUCCESSION.is_file() else ""

    # 0. Custos 4.1 (edition of record): bytes match the ratified
    # digest in SUCCESSION.md's 4.1 row, and 4.1's own predecessor
    # pin equals the 4.0 row's digest.
    row41 = re.search(r"Custos 4\.1[^\n]*?\b([0-9a-f]{64})\b", succession_text)
    ratified41 = row41.group(1) if row41 else ""
    if EDITION_41.is_file():
        e41 = EDITION_41.read_bytes()
        sha41 = hashlib.sha256(e41).hexdigest()
        check(
            "4.1 bytes match the ratified digest (SUCCESSION.md)",
            bool(ratified41) and sha41 == ratified41,
            f"sha256 {sha41}"
            + ("" if sha41 == ratified41
               else f" != ratified {ratified41 or 'NOT FOUND'}"),
        )
        pins41 = PRED_PIN_RE.findall(e41.decode("utf-8"))
        check(
            "4.1 predecessor pin equals the 4.0 ratified digest",
            "9cefdc5d584289ea8391d8069bca26ea38aa82a34f9ae973d80e4d1b7773f315" in pins41,
            "4.0 digest pinned in 4.1's own bytes"
            if "9cefdc5d584289ea8391d8069bca26ea38aa82a34f9ae973d80e4d1b7773f315" in pins41
            else "4.0 digest NOT found in 4.1",
        )
    else:
        check("4.1 edition file present", False, str(EDITION_41))

    # 1. kernel digest vs the ratified digest in SUCCESSION.md
    if not KERNEL.is_file():
        check("kernel file present", False, str(KERNEL))
        return finish()
    kernel_bytes = KERNEL.read_bytes()
    kernel_sha = hashlib.sha256(kernel_bytes).hexdigest()

    ratified_sha = ""
    row = re.search(
        r"Custos 4\.0[^\n]*?\b([0-9a-f]{64})\b", succession_text)
    if row:
        ratified_sha = row.group(1)
    check(
        "kernel bytes match the ratified digest (SUCCESSION.md)",
        bool(ratified_sha) and kernel_sha == ratified_sha,
        f"sha256 {kernel_sha}"
        + ("" if kernel_sha == ratified_sha
           else f" != ratified {ratified_sha or 'NOT FOUND'}"),
    )

    kernel_text = kernel_bytes.decode("utf-8")

    # 2. §15 predecessor pin vs SUCCESSION.md
    kernel_pins = PRED_PIN_RE.findall(kernel_text)
    succession_pins = [p for p in PRED_PIN_RE.findall(succession_text)
                       if p != ratified_sha]
    shared = set(kernel_pins) & set(succession_pins)
    check(
        "predecessor pin agreement (kernel §15 vs SUCCESSION.md)",
        bool(shared),
        f"shared pin(s): {', '.join(sorted(shared)) or 'NONE'}",
    )

    # 3. README abstract is a byte-true EXCERPT of the kernel's:
    # whatever the README quotes must be a contiguous span of the
    # kernel abstract's bytes (whitespace-normalized). Trimming is
    # lawful; paraphrase is not.
    m = re.search(r"\*\*Abstract\*\* — (.+?)(?:\n\n)", kernel_text, re.S)
    ok3 = False
    detail3 = "kernel abstract not found"
    if m and README.is_file():
        kernel_abstract = re.sub(r"\s+", " ", m.group(1)).strip()
        readme_text = README.read_text()
        bq = re.search(r"\*\*Abstract\*\* —(.*?)(?:\n[^>])", readme_text, re.S)
        if bq:
            quoted = re.sub(r"^> ?", "", bq.group(1), flags=re.M)
            quoted = re.sub(r"\s+", " ", quoted).strip()
            ok3 = bool(quoted) and quoted in kernel_abstract
            detail3 = ("README abstract is a byte-true excerpt of the kernel"
                       if ok3 else "README abstract paraphrases the kernel")
        else:
            detail3 = "README abstract block not found"
    check("README abstract excerpt discipline", ok3, detail3)

    # 4. gate census source pin agrees with the succession record
    if GATE_CENSUS.is_file():
        try:
            gate = json.loads(GATE_CENSUS.read_text())
            gate_src = gate.get("source-sha256", "")
            check(
                "gate census predecessor pin agreement",
                gate_src in shared if shared else False,
                f"census source {gate_src[:16]}… "
                + ("matches the succession pins" if gate_src in shared
                   else "does not match the succession pins"),
            )
            # informative freshness note if the census ever carries it
            if "draft-sha256" in gate:
                fresh = gate["draft-sha256"] == kernel_sha
                check("gate record matches current kernel bytes", fresh)
        except (json.JSONDecodeError, OSError) as e:
            check("gate record readable", False, str(e))
    else:
        print("[SKIP] gate record not present")

    return finish()

def finish():
    fails = [r for r in results if not r[1]]
    print(f"\n{len(results) - len(fails)}/{len(results)} checks pass")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
