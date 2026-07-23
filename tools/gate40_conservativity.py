#!/usr/bin/env python3
# Apache-2.0. Part of the Custos standard's tooling.
"""Step-3b conservativity gate — 4.0 kernel draft vs custos-3.3.

Cite-and-copy derivative of reviews/rounds/s14-codomain-2026-07-22/
leg4_extract.py + leg4_signature.py (committed pattern; per the
cookbook, copied never imported). Two changes only, both declared:

1. The NEW signature is built from the 4.0 KERNEL DRAFT section 6
   (custos-4.0-kernel-draft.md), not from the shelf. Discipline
   preserved: a field enters the new signature ONLY when a
   committed probe (exact substring of the draft's bytes) verifies
   the draft states it. Absent structure is represented as absent
   — the comparison, not this builder, decides whether absence is
   a loss.
2. The OLD signature and census machinery are byte-identical in
   logic to leg4; the 3.3 source pin (sha256) is unchanged.

Scope honesty (cookbook section 0, SOL audit D2): this gate covers
the 52-span finding-codomain signature ONLY. No other conservation
claim may cite it.

Symbol table (injective, as leg4): VALID->affirmed,
INVALID->defeated, INSUFFICIENT->pending,
DUPLICITOUS->self-convicted. Payload table: citation->citation,
defeater-class->defeater-class (the draft carries it explicitly —
the leg4 shelf-run's payload-field-loss delta is expected to
RESOLVE here), requirement-set->typed-requirement, proof->proof.
"""

from __future__ import annotations

import base64
import hashlib
import json
import re
import sys
from pathlib import Path

from blake3 import blake3

ROOT = Path(__file__).resolve().parents[3]
SOURCE_REL = "weave/gamma/custos-3.3.md"
EXPECTED_SOURCE_SHA256 = (
    "18b0469e731db24f6bca45525828e4417751929306ea21e09977088e08a20ceb"
)
DRAFT_REL = (
    "reviews/rounds/40-drafting-2026-07-22/custos-4.0-kernel-draft.md"
)

MARKERS = (
    ("VALID", re.compile(rb"(?<![A-Z])VALID(?![A-Z])")),
    ("INVALID", re.compile(rb"(?<![A-Z])INVALID(?![A-Z])")),
    ("INSUFFICIENT", re.compile(rb"(?<![A-Z])INSUFFICIENT(?![A-Z])")),
    ("DUPLICITOUS", re.compile(rb"(?<![A-Z])DUPLICITOUS(?![A-Z])")),
    ("order-glyph", re.compile("⊑".encode("utf-8"))),
    ("evidence-growth", re.compile(rb"evidence-growth", re.IGNORECASE)),
    ("monotone", re.compile(rb"monotone", re.IGNORECASE)),
    ("ex-ante", re.compile(rb"ex-ante", re.IGNORECASE)),
    ("enumerable", re.compile(rb"enumerable", re.IGNORECASE)),
    ("defeater", re.compile(rb"defeater", re.IGNORECASE)),
)

OLD_TO_NEW = {
    "VALID": "affirmed",
    "INVALID": "defeated",
    "INSUFFICIENT": "pending",
    "DUPLICITOUS": "self-convicted",
}

PAYLOAD_SYMBOL_TABLE = {
    "citation": "citation",
    "defeater-class": "defeater-class",
    "requirement-set": "typed-requirement",
    "proof": "proof",
}


def canonical_json_bytes(value: object) -> bytes:
    return (
        json.dumps(
            value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        + b"\n"
    )


def qb64_blake3_256(data: bytes) -> str:
    raw = blake3(data).digest()
    return "E" + base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")


def source_blocks(data: bytes):
    lines = data.splitlines(keepends=True)
    byte_cursor = 0
    block_start_byte = None
    block_start_line = None
    block_parts: list[bytes] = []
    for line_number, line in enumerate(lines, start=1):
        if line.strip():
            if block_start_byte is None:
                block_start_byte = byte_cursor
                block_start_line = line_number
            block_parts.append(line)
        elif block_start_byte is not None:
            block_parts.append(line)
            yield (
                block_start_byte,
                byte_cursor + len(line),
                block_start_line,
                line_number,
                b"".join(block_parts),
            )
            block_start_byte = None
            block_start_line = None
            block_parts = []
        byte_cursor += len(line)
    if block_start_byte is not None:
        yield (
            block_start_byte,
            len(data),
            block_start_line,
            len(lines),
            b"".join(block_parts),
        )


def extract_census() -> dict:
    source = ROOT / SOURCE_REL
    data = source.read_bytes()
    observed = hashlib.sha256(data).hexdigest()
    if observed != EXPECTED_SOURCE_SHA256:
        raise SystemExit(
            f"3.3 source digest mismatch: expected "
            f"{EXPECTED_SOURCE_SHA256}, observed {observed}"
        )
    rows = []
    for start, end, line_start, line_end, span in source_blocks(data):
        hits = [name for name, pattern in MARKERS if pattern.search(span)]
        if not hits:
            continue
        rows.append(
            {
                "ruling-id": f"F3-R{len(rows) + 1:04d}",
                "file:line": f"{SOURCE_REL}:{line_start}",
                "line-end": line_end,
                "byte-start": start,
                "byte-end-exclusive": end,
                "span-said": qb64_blake3_256(span),
                "markers-hit": hits,
            }
        )
    body = {
        "schema": "s14-leg4-census-v1-40gate",
        "source": SOURCE_REL,
        "source-sha256": observed,
        "rulings": rows,
    }
    census = dict(body)
    census["census-said"] = qb64_blake3_256(canonical_json_bytes(body))
    return census


def support(census: dict, line: int) -> list[str]:
    found = []
    for row in census["rulings"]:
        start = int(row["file:line"].rsplit(":", 1)[1])
        if start <= line <= int(row["line-end"]):
            found.append(row["ruling-id"])
    if not found:
        raise SystemExit(f"no 3.3 ruling span supports source line {line}")
    return found


def edge(source: str, target: str, condition: str | None = None) -> dict:
    result = {"from": source, "to": target}
    if condition is not None:
        result["condition"] = condition
    return result


def old_signature(census: dict) -> dict:
    # Byte-identical in logic to leg4_signature.old_signature.
    return {
        "name": "custos-3.3 finding codomain",
        "tier": "T3-claims",
        "constructors": {
            "VALID": {"payload-fields": []},
            "INVALID": {
                "payload-fields": ["citation", "defeater-class"],
                "field-constraints": {
                    "citation": (
                        "violated-or-superseding-clause-SAID; for crypto, "
                        "failed-verification-subject-SAID"
                    ),
                    "defeater-class": [
                        "crypto", "authority", "merit", "superseded"
                    ],
                },
            },
            "INSUFFICIENT": {
                "payload-fields": ["requirement-set"],
                "field-constraints": {
                    "requirement-set": {
                        "element-fields": [
                            "requirement-kind",
                            "subject-SAID",
                            "citing-clause-SAID-list",
                        ],
                        "requirement-kinds": [
                            "absent", "window-open", "unresolved-conflict"
                        ],
                        "canonical-order": [
                            "subject-SAID",
                            "requirement-kind",
                            "citing-clause-list-bytes",
                        ],
                        "deduplicated": True,
                    }
                },
            },
            "DUPLICITOUS": {
                "payload-fields": ["proof"],
                "field-constraints": {
                    "proof": "canonical A7 proof-package SAID"
                },
            },
        },
        "permitted-transitions": [
            edge("INSUFFICIENT", "VALID"),
            edge("INSUFFICIENT", "INVALID"),
            edge(
                "INSUFFICIENT",
                "DUPLICITOUS",
                "new-bearing-pair-or-new-governed-status-evidence",
            ),
            edge("VALID", "DUPLICITOUS", "new-bearing-on-Q-pair"),
            edge("INVALID", "DUPLICITOUS", "new-bearing-on-Q-pair"),
        ],
        "forbidden-transitions": [
            edge("VALID", "INVALID"),
            edge("INVALID", "VALID"),
            edge("VALID", "INSUFFICIENT"),
            edge("INVALID", "INSUFFICIENT"),
            edge("DUPLICITOUS", "INSUFFICIENT"),
            edge("DUPLICITOUS", "VALID"),
            edge("DUPLICITOUS", "INVALID"),
        ],
        "terminality": {
            "VALID": "final-except-new-bearing-on-Q-duplicity-pair",
            "INVALID": "final-except-new-bearing-on-Q-duplicity-pair",
            "INSUFFICIENT": "nonterminal-bottom",
            "DUPLICITOUS": "terminal-for-poisoned-question",
        },
        "predicates": {
            "finding-input": "(B,h,alpha)-only",
            "evidence-growth": "B subset-of B-prime",
            "monotonicity": (
                "finding(B,h,alpha) subset-order finding(B-prime,h,alpha)"
            ),
            "ex-ante-enumerability": (
                "all admissible defeating evidence is in needs(Q)"
            ),
            "duplicity-scope": "bearing-on-Q",
            "invalid-canonical-selection": (
                "lexicographic minimum of "
                "(defeater-class-rank,citation-SAID,subcode)"
            ),
        },
        "support": {
            "constructors": support(census, 720),
            "permitted-transitions": support(census, 852),
            "forbidden-transitions": support(census, 864),
            "terminality": support(census, 870),
            "invalid-payload": support(census, 885),
            "invalid-selection": support(census, 894),
            "insufficient-encoding": support(census, 928),
            "ex-ante-enumerability": sorted(
                set(support(census, 578) + support(census, 599))
            ),
        },
    }


# --- NEW signature: built from the 4.0 kernel draft section 6 ---
# Discipline: every structural assertion below is admitted only if
# its PROBE (exact substring) is present in the draft bytes. A probe
# miss aborts the build — the draft, not this table, is the source.

DRAFT_PROBES = {
    "values-enumerated": "The codomain has four values",
    "affirmed": "**affirmed** — the proposition holds",
    "defeated-citation": "**defeated(citation)**",
    "defeated-class": "together with the defeater's class",
    "pending-typed": "**pending(typed-requirement)**",
    "self-convicted-proof": "**self-convicted(proof)**",
    "ground-typing-rule": (
        "A value that does not carry its ground is not a\nmember of this type"
    ),
    "payload-defeated": (
        "A defeated finding SHALL carry its defeater class and its\n  citation"
    ),
    "defeater-class-enumeration": (
        "The\ndefeater classes are enumerated and ranked, in this order,\n"
        "carried from the predecessor unchanged: **crypto** (a\n"
        "cryptographic verification failed), **authority** (the actor\n"
        "lacked the invoked power), **merit** (the content violates a\n"
        "committed clause), **superseded** (a later lawful act displaced\n"
        "the subject)"
    ),
    "subcode-definition": (
        "The subcode is the defeat's discriminator within\nits citation"
    ),
    "payload-defeated-citation-def": (
        "the violated or superseding clause's identifier, or,\n"
        "  for cryptographic defeat, the identifier of the failed\n"
        "  verification subject"
    ),
    "payload-pending": (
        "A pending finding SHALL carry its typed requirement set:\n"
        "  deduplicated elements, each carrying requirement kind, subject\n"
        "  identifier, and the list of citing clauses, in canonical order\n"
        "  (subject, then kind, then citing-clause bytes)"
    ),
    "payload-proof": (
        "A self-convicted finding SHALL carry the identifier of the\n"
        "  canonical proof package for the contradictory pair"
    ),
    "species-four": (
        "species are absent, window-open, unresolved-conflict, and\n"
        "> expired/abandoned"
    ),
    "t-p-a": "| pending | affirmed | the requirement set discharges affirmatively |",
    "t-p-d": "| pending | defeated | the requirement set discharges by defeat |",
    "t-p-s": (
        "| pending | self-convicted | a bearing contradictory pair, or new "
        "governed-status evidence (committed\nevidence newly bearing on the "
        "subject's status under the\ngovernance tier's committed predicates), "
        "enters the bundle |"
    ),
    # NOTE (second-look repair FS-10, user-ruled sweep): the probe
    # follows the draft's dereference gloss; the transition edge is
    # unchanged — the gloss defines the evidence class inline.
    "t-a-s": (
        "| affirmed | self-convicted | a contradictory pair bearing on the "
        "question enters the bundle |"
    ),
    "t-d-s": (
        "| defeated | self-convicted | a contradictory pair bearing on the "
        "question enters the bundle |"
    ),
    "f-a-d": "| affirmed | defeated |",
    "f-d-a": "| defeated | affirmed |",
    "f-a-p": "| affirmed | pending |",
    "f-d-p": "| defeated | pending |",
    "f-s-p": "| self-convicted | pending |",
    "f-s-a": "| self-convicted | affirmed |",
    "f-s-d": "| self-convicted | defeated |",
    "term-final": (
        "Affirmed and defeated are final except for one\nevent"
    ),
    "term-bottom": "Pending is the\nnon-terminal bottom",
    "term-poisoned": (
        "Self-convicted is terminal for its question\n"
        "\u2014 the question is poisoned"
    ),
    "input-triple": (
        "A finding is a function of exactly three inputs: the\n"
        "committed evidence bundle, the committed law head under which it\n"
        "is appraised, and the appraisal position"
    ),
    "byte-identical": (
        "Two evaluations of the same triple\nSHALL return byte-identical findings"
    ),
    "monotonicity": (
        "where one committed bundle is a subset of another,\n"
        "appraisal under the larger bundle refines and never contradicts\n"
        "appraisal under the smaller"
    ),
    "subset-order": (
        "monotonicity is over the subset\norder on bundles at a fixed law head "
        "and position, never over\nwall time"
    ),
    "ex-ante": (
        "Defeating evidence is ex-ante enumerable: everything\n"
        "that could defeat a question is in that question's committed\n"
        "requirement space before appraisal begins"
    ),
    "duplicity-scope": (
        "Contradictory pairs\nconvict only where they bear on the question"
    ),
    "canonical-selection": (
        "the finding SHALL cite the\nlexicographic minimum of (defeater-class "
        "rank, citation\nidentifier, subcode)"
    ),
}


def new_signature(draft_text: str, draft_sha256: str) -> dict:
    missing = [k for k, probe in DRAFT_PROBES.items() if probe not in draft_text]
    if missing:
        raise SystemExit(f"draft probes MISSING (abort): {missing}")
    return {
        "name": "custos-4.0 kernel draft section 6 finding codomain",
        "tier": "T3",
        "constructors": {
            "affirmed": {"payload-fields": []},
            "defeated": {
                "payload-fields": ["citation", "defeater-class"],
                "field-constraints": {
                    "citation": (
                        "violated-or-superseding-clause-SAID; for crypto, "
                        "failed-verification-subject-SAID"
                    ),
                    "defeater-class": [
                        "crypto", "authority", "merit", "superseded"
                    ],
                },
            },
            "pending": {
                "payload-fields": ["typed-requirement"],
                "field-constraints": {
                    "typed-requirement": {
                        "element-fields": [
                            "requirement-kind",
                            "subject-SAID",
                            "citing-clause-SAID-list",
                        ],
                        "requirement-kinds": [
                            "absent", "window-open", "unresolved-conflict",
                            "expired/abandoned"
                        ],
                        "canonical-order": [
                            "subject-SAID",
                            "requirement-kind",
                            "citing-clause-list-bytes",
                        ],
                        "deduplicated": True,
                    }
                },
            },
            "self-convicted": {
                "payload-fields": ["proof"],
                "field-constraints": {
                    "proof": "canonical A7 proof-package SAID"
                },
            },
        },
        "permitted-transitions": [
            edge("pending", "affirmed"),
            edge("pending", "defeated"),
            edge(
                "pending",
                "self-convicted",
                "new-bearing-pair-or-new-governed-status-evidence",
            ),
            edge("affirmed", "self-convicted", "new-bearing-on-Q-pair"),
            edge("defeated", "self-convicted", "new-bearing-on-Q-pair"),
        ],
        "forbidden-transitions": [
            edge("affirmed", "defeated"),
            edge("defeated", "affirmed"),
            edge("affirmed", "pending"),
            edge("defeated", "pending"),
            edge("self-convicted", "pending"),
            edge("self-convicted", "affirmed"),
            edge("self-convicted", "defeated"),
        ],
        "terminality": {
            "affirmed": "final-except-new-bearing-on-Q-duplicity-pair",
            "defeated": "final-except-new-bearing-on-Q-duplicity-pair",
            "pending": "nonterminal-bottom",
            "self-convicted": "terminal-for-poisoned-question",
        },
        "predicates": {
            "finding-input": "(B,h,alpha)-only",
            "evidence-growth": "B subset-of B-prime",
            "monotonicity": (
                "finding(B,h,alpha) subset-order finding(B-prime,h,alpha)"
            ),
            "ex-ante-enumerability": (
                "all admissible defeating evidence is in needs(Q)"
            ),
            "duplicity-scope": "bearing-on-Q",
            "invalid-canonical-selection": (
                "lexicographic minimum of "
                "(defeater-class-rank,citation-SAID,subcode)"
            ),
        },
        "probes": {k: True for k in DRAFT_PROBES},
        "note": (
            "constraint values are admitted via probes: each probe string "
            "is verbatim draft bytes stating the constraint, including "
            "the full defeater-class enumeration with ranks and the "
            "subcode definition (both present in draft bytes as of the "
            "post-gauntlet repair pass). The new signature carries FOUR "
            "pending species per the ratified F1 amendment; the "
            "comparator records the added species as an explicit "
            "justified delta in the justified-deltas field. This gate "
            "covers the 52-span finding-codomain signature ONLY."
        ),
        "source": {"file": DRAFT_REL, "sha256": draft_sha256},
    }


def translate_edge(item: dict) -> dict:
    translated = dict(item)
    translated["from"] = OLD_TO_NEW[item["from"]]
    translated["to"] = OLD_TO_NEW[item["to"]]
    return translated


def compare(old: dict, new: dict) -> dict:
    deltas = []
    justified = []
    mapped_values = list(OLD_TO_NEW.values())

    for old_name, new_name in OLD_TO_NEW.items():
        old_fields = old["constructors"][old_name]["payload-fields"]
        new_fields = new["constructors"][new_name]["payload-fields"]
        mapped_fields = [
            PAYLOAD_SYMBOL_TABLE[f]
            for f in old_fields
            if PAYLOAD_SYMBOL_TABLE.get(f) is not None
        ]
        lost = [f for f in old_fields if PAYLOAD_SYMBOL_TABLE.get(f) is None]
        for f in lost:
            deltas.append(
                {
                    "kind": "payload-field-loss",
                    "constructor": f"{old_name}->{new_name}",
                    "old-field": f,
                }
            )
        if sorted(mapped_fields) != sorted(new_fields):
            # defeated carries citation + defeater-class; typed-requirement
            # naming: pending's old field requirement-set maps to
            # typed-requirement — set comparison after mapping.
            deltas.append(
                {
                    "kind": "payload-signature-mismatch",
                    "constructor": f"{old_name}->{new_name}",
                    "expected-new-fields": sorted(mapped_fields),
                    "observed-new-fields": sorted(new_fields),
                }
            )
        old_constraints = old["constructors"][old_name].get(
            "field-constraints", {}
        )
        new_constraints = new["constructors"][new_name].get(
            "field-constraints", {}
        )
        for old_field, constraint in old_constraints.items():
            target = PAYLOAD_SYMBOL_TABLE.get(old_field)
            if target is not None and new_constraints.get(target) != constraint:
                observed = new_constraints.get(target)
                # Justified-delta path: the F1 amendment RATIFIES a
                # fourth pending species. If the ONLY difference is
                # the added species, record it as a justified delta,
                # not a conservativity failure.
                if (
                    old_field == "requirement-set"
                    and isinstance(constraint, dict)
                    and isinstance(observed, dict)
                ):
                    o2 = dict(observed)
                    kinds = list(o2.get("requirement-kinds", []))
                    if "expired/abandoned" in kinds:
                        o2["requirement-kinds"] = [
                            k for k in kinds if k != "expired/abandoned"
                        ]
                        if o2 == constraint:
                            justified.append(
                                {
                                    "kind": "justified-delta",
                                    "constructor": f"{old_name}->{new_name}",
                                    "delta": (
                                        "pending species expired/abandoned "
                                        "ADDED by the ratified F1 amendment "
                                        "(verdict-s14.md section 2); "
                                        "extension above the conserved "
                                        "signature, not a loss"
                                    ),
                                }
                            )
                            continue
                deltas.append(
                    {
                        "kind": "dropped-or-altered-payload-predicate",
                        "constructor": f"{old_name}->{new_name}",
                        "old-field": old_field,
                        "expected": constraint,
                        "observed": observed,
                    }
                )

    expected_permitted = [translate_edge(e) for e in old["permitted-transitions"]]
    expected_forbidden = [translate_edge(e) for e in old["forbidden-transitions"]]
    for item in expected_permitted:
        if item not in new["permitted-transitions"]:
            deltas.append({"kind": "missing-permitted-transition", "edge": item})
    for item in new["permitted-transitions"]:
        if item not in expected_permitted:
            deltas.append({"kind": "broadened-transition", "edge": item})
    for item in expected_forbidden:
        if item not in new["forbidden-transitions"]:
            deltas.append({"kind": "dropped-forbidden-transition", "edge": item})
    for item in new["forbidden-transitions"]:
        if item not in expected_forbidden:
            deltas.append({"kind": "extra-forbidden-transition", "edge": item})

    for old_name, old_flag in old["terminality"].items():
        observed = new["terminality"].get(OLD_TO_NEW[old_name])
        if observed != old_flag:
            deltas.append(
                {
                    "kind": "terminality-mismatch",
                    "constructor": f"{old_name}->{OLD_TO_NEW[old_name]}",
                    "expected": old_flag,
                    "observed": observed,
                }
            )

    for name, expected in old["predicates"].items():
        observed = new["predicates"].get(name)
        if observed != expected:
            deltas.append(
                {
                    "kind": "dropped-or-altered-predicate",
                    "predicate": name,
                    "expected": expected,
                    "observed": observed,
                }
            )

    return {
        "schema": "s14-leg4-comparison-v1-40gate",
        "scope": (
            "finding-codomain signature only (52-span census); no other "
            "conservation claim may cite this gate"
        ),
        "symbol-table": {
            "constructors": OLD_TO_NEW,
            "payload-fields": PAYLOAD_SYMBOL_TABLE,
            "injective": len(set(mapped_values)) == len(mapped_values),
        },
        "old-signature": old,
        "new-signature": new,
        "equal-modulo-symbol-table": not deltas,
        "result": "PASS" if not deltas else "FAIL",
        "deltas": deltas,
        "justified-deltas": justified,
    }


def main() -> None:
    census = extract_census()
    draft_path = ROOT / DRAFT_REL
    draft_bytes = draft_path.read_bytes()
    draft_text = draft_bytes.decode("utf-8")
    draft_sha = hashlib.sha256(draft_bytes).hexdigest()

    old = old_signature(census)
    new = new_signature(draft_text, draft_sha)
    comparison = compare(old, new)

    out_dir = Path(__file__).resolve().parent
    (out_dir / "gate40-census.json").write_bytes(
        canonical_json_bytes(census)
    )
    (out_dir / "gate40-comparison.json").write_bytes(
        canonical_json_bytes(comparison)
    )
    print(
        json.dumps(
            {
                "census-spans": len(census["rulings"]),
                "census-said": census["census-said"],
                "draft-sha256": draft_sha,
                "result": comparison["result"],
                "delta-count": len(comparison["deltas"]),
                "deltas": comparison["deltas"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    sys.exit(0 if comparison["result"] == "PASS" else 1)


if __name__ == "__main__":
    main()
