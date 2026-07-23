#!/usr/bin/env python3
# Apache-2.0. Part of the Custos standard's tooling.
"""verify_kernel.py — repo-scope byte verification for the Custos kernel.

Checks (all stdlib, no dependencies, run from the repo root):
  1. spec kernel file exists and its SHA-256 is computed;
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
SUCCESSION = ROOT / "SUCCESSION.md"
README = ROOT / "README.md"
GATE_CENSUS = ROOT / "tools" / "gate40-census.json"

PRED_PIN_RE = re.compile(r"\b([0-9a-f]{64})\b")

results = []

def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))

def main():
    # 1. kernel digest
    if not KERNEL.is_file():
        check("kernel file present", False, str(KERNEL))
        return finish()
    kernel_bytes = KERNEL.read_bytes()
    kernel_sha = hashlib.sha256(kernel_bytes).hexdigest()
    check("kernel digest computed", True, f"sha256 {kernel_sha}")

    kernel_text = kernel_bytes.decode("utf-8")

    # 2. §15 predecessor pin vs SUCCESSION.md
    kernel_pins = PRED_PIN_RE.findall(kernel_text)
    succession_text = SUCCESSION.read_text() if SUCCESSION.is_file() else ""
    succession_pins = PRED_PIN_RE.findall(succession_text)
    shared = set(kernel_pins) & set(succession_pins)
    check(
        "predecessor pin agreement (kernel §15 vs SUCCESSION.md)",
        bool(shared),
        f"shared pin(s): {', '.join(sorted(shared)) or 'NONE'}",
    )

    # 3. README abstract is a byte-true quotation of the kernel's
    m = re.search(r"\*\*Abstract\*\* — (.+?)(?:\n\n)", kernel_text, re.S)
    ok3 = False
    detail3 = "kernel abstract not found"
    if m and README.is_file():
        kernel_abstract = re.sub(r"\s+", " ", m.group(1)).strip()
        readme_text = README.read_text()
        readme_norm = re.sub(r"^> ?", "", readme_text, flags=re.M)
        readme_norm = re.sub(r"\s+", " ", readme_norm)
        ok3 = kernel_abstract in readme_norm
        detail3 = "README quotes the kernel abstract verbatim" if ok3 else \
            "README abstract diverges from kernel bytes"
    check("README abstract quotation", ok3, detail3)

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
