# Provenance

How this text came to be, in enough detail that its assurance
claims are checkable rather than asserted.

## The program

Custos 4.0 was drafted inside a standing annealing program: every
draft travels through committed adversarial review rounds before
ratification, all review briefs and verdicts are committed files,
and repairs execute only under recorded rulings by the ratifying
authority. The kernel in `spec/` passed through:

| Phase | Artifact | Verdict |
|---|---|---|
| Conservativity gate | `tools/gate40_conservativity.py` + JSONs | PASS — 52-span finding-codomain signature of the predecessor carried with 0 unjustified deltas, 1 justified (explicitly ruled) |
| First-round gauntlet, 3 parallel firewalled legs | assurance leg · drafting leg · substrate-native leg (`reviews/keri-native-review.md`, published) | 2 × FAIL, 1 × SOUND-WITH-FINDINGS — 58 findings, 9 repair clusters, all ratified and executed in bytes |
| Second-look round, 2 firewalled legs | discharge verification + cold-read of post-repair material | All 15 prior convictions verified discharged; new findings on new material only; repaired in a 27-site pass |
| Succession-completeness audit | `reviews/sol-33-completeness-audit.md` (published) | INCOMPLETE — 24 dropped groups; disposed by ruling (see the migration register's status header) |

The first gate run was itself convicted by two firewalled review
legs (its census note predicted a species delta the result
omitted); the published gate record is the rebuilt, re-run
version. The program treats that conviction as an advertisement:
a check that cannot fail is not a check.

One exhibit review is published in full: the substrate-native leg,
grounded entirely in public specification bytes. The remaining
legs cite the program's internal working registers; their
verdicts, finding counts, and sharpest catches are summarized
above rather than published with dangling citations.

## Lineage of the central concepts

- **KERI, ACDC, CESR** are the substrate of record, in the
  specifications stewarded by the Trust Over IP Foundation's
  specification working group, with keripy (WebOfTrust) as the
  reference implementation the executable evidence was exercised
  against. Cited, never restated.
- **Ambient verifiability** is Samuel M. Smith's term (KERI
  whitepaper v2.63, abstract): *verifiable by anyone, anywhere,
  at any time*. The kernel's abstract extends it from control
  provenance to governance provenance, with attribution.
- **The GEL** (governance event log) descends from the lead
  author's earlier published work on chartered registries: the
  Standing Registry — the registry that charters every
  operational registry in its scope — and the constitutional-
  registries line where the Governance Event Log is first named
  and disciplined ("not a new wire-format primitive"). The
  kernel's compression — a governed domain's law as the computed
  state of a committed log — is this standard's own restatement
  of those steps.
- **Predecessor**: Custos 3.3, superseded whole by the succession
  rule in the kernel's final section. The predecessor publishes
  by digest, not by copy: its sha256 is pinned in the kernel
  (§15) and in `SUCCESSION.md`; its bytes are committed workspace
  record, available on request. The completeness audit and
  migration register in `reviews/` carry the full disposition
  story.

## The falsifiers

The program keeps written kill criteria — conditions under which
this standard is wrong: no second implementation ever derives
equal state from the same corpus; the succession ceremony proves
unrunnable; every adoption channel refuses the shape; a closure
claim fails unrepairably. They are recorded here so that failure,
if it comes, is checkable too.
