# Migration register — Custos 3.3 → 4.0
# Status: PROPOSED (every row awaits user refinement; no row is
# law until ruled). Source: sol-33-completeness-audit.md (verdict
# INCOMPLETE, CA-01..24; full ledger L-001..L-136 therein).
# Repair form: per the audit's §7 — one row per dropped unit,
# exactly one disposition each. At ratification this register is
# pinned by kernel §15; it restores the succession trail, not the
# predecessor's length.
# Disposition kinds:
#   KERNEL-SEAT   — a ruled span is added to the 4.0 kernel
#                   (byte change; executes in one final pass
#                   after refinement, before the step-5 read)
#   COMPANION     — assigned to a named companion by this ruling
#   SUPERSEDED    — predecessor rule explicitly replaced; the
#                   row states the replacement and migration
#   RETAINED-DEBT — carried as open debt with a committed
#                   discharge criterion (fixture lane / docket)
# Date: 2026-07-23

## RULING (2026-07-23): NO ROW-BY-ROW MIGRATION

The user ruled the register's premise superseded. Disposition of
ALL rows resolves by publication rather than migration:

1. ONE kernel seat executes: M-042 (succession-integrity
   controls, CA-18) — ruled the essential theme of the audit,
   extended by the user's mapping to git publication: version
   control preserves history; the GEL computes which bytes are
   law. Seated in kernel section 15.
2. Custos 3.3 is NOT migrated. It is STAGED WHOLE, immutable and
   digest-pinned, beside 4.0 in a public repository, in a
   governed way: the succession record (3.3 digest, ratifying
   enactment, effectuation coordinate) is replayable from the
   GEL, and 3.3's full text remains available for anyone to take
   from. Every DROPPED unit of the audit is thereby disposed:
   nothing is lost when the immutable predecessor travels with
   the succession record. Strangers consume 3.3 directly;
   companions may later mine it; no row lapses silently.
3. All other KERNEL-SEAT, COMPANION, SUPERSEDED, and
   RETAINED-DEBT proposals below are PRESERVED AS ADVISORY
   ANALYSIS ONLY — a map of where 3.3's cargo could seat if
   future editions or companions want it. None execute.
4. Licensing (ruled): Community Specification License 1.0 for
   specification text; Apache-2.0 for all executable artifacts.
5. Publication (ruled): fresh public repository; README carries
   the 4.0 abstract; keri-git-said instruments (message SAIDs,
   KERI signing, ACDC sidecar); repo = projection, never
   authority.

The proposed rows below are retained verbatim for the record.

## Named companion targets (defined once; rows cite by ID)

| ID | Companion | Charter |
|---|---|---|
| C1 | Corpus & enactment | Smith-tree corpus model, clause-kind registry, enactment/supersession/disposition schemas, closure tiers + endorsement envelope, seating procedure, membership/root-organ tables, succession-object schema + ceremony |
| C2 | Evaluation engine | CPX profile, predicate-language conformance, structural subsumption, @ROOT legality, kfs/cpr binding, epoch anchoring (S-14 interior review adjacency) |
| C3 | Confidentiality & disclosure | Membrane strata, blinding, scoped erasure, salt annex (3.3 Annex F intact), live-query/asker privacy |
| C4 | Conformance & fixtures | Conformance ladder, vector families, primitive-deletion test, bridge profiles, projection schemas |
| C5 | Deployment & observation | KAWA/DEL behavior pins, first-seen edge classification, juror/judge roles, typed seam-claim schemas, duress anti-pattern |
| C6 | Liability & service | Obligation artifacts, L1–L5 liability ladder, tenure attachment, service-term commitments, post-seam economics |

## Register rows

### CA-01 — standing triad and elevation law
| Row | Unit (3.3 cite) | Disposition | Target / ground |
|---|---|---|---|
| M-001 | Granted/committed/derived standing grades + explicit-elevation law (3.3:3–24, 252–270, 549–564, 1023–1047) | KERNEL-SEAT | §7: compact three-grade table + one SHALL (elevation is an enactment, never silent); grade mechanics beyond the table → C1 |

### CA-02 — enactment-echo triple
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-002 (L-013, L-077) | Echo triple: predecessor coordinate + warranted predecessor-head SAID + enacting-seal SAID; defect classes (3.3:252, 1099–1152) | KERNEL-SEAT | §12.1 grounded-enactment content gains the three fields; genesis carve-out already discharged by the (K0,C) knot |

### CA-03 — closure tiers and endorsement envelope
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-003 (L-057) | Three closure tiers, non-interchangeable claims (3.3:549–564) | COMPANION | C1; kernel retains one sentence — see M-004 |
| M-004 | Closure grades SHALL NOT be conflated (tier table's floor) | KERNEL-SEAT | one sentence, §7 or §12.2 |
| M-005 (L-054, L-055) | Endorsement bonds 1–2, tuple-bound bilateral consent (3.3:500–526) | COMPANION | C1 |
| M-006 (L-056) | Open rule-object class, attenuation, blinded envelope (3.3:528–547) | COMPANION | C1 (attenuation proof mechanics → C2) |
| M-007 (L-090) | Organizational closure/bootstrap criterion (3.3:1569–1575) | COMPANION | C1 |

### CA-04 — two-sided perimeter and seam doctrine
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-008 (L-041, L-064) | At-most-one exogenous seam; interior seam necessity; no fact crosses, only signed utterances (3.3:411, 618–681) | KERNEL-SEAT | compact seam rule in §4 or §11 (~4 lines, 1–2 SHALLs) |
| M-009 (L-062) | Typed exogenous claim classes + fallback semantics (3.3:620–648) | COMPANION | C5 |
| M-010 (L-063) | Seam-duplicity package, no verifier choice (3.3:649–660) | COMPANION | C5 |

### CA-05 — closure-grade prevention test
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-011 | Prevention constitutive only within prevention-grade perimeter (3.3:14–24) | KERNEL-SEAT | §12.2: narrow the prevention claim to committed-delegation closure; cross-ref M-004 |

### CA-06 — wrongness strata vocabulary
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-012 (L-068) | MALFORMED/ILL-SHAPED strata; committed-object vs bundle-absence rule (3.3:232–248, 751–765) | SUPERSEDED | mapping (this row is the migration): MALFORMED → canonical-form refusal; ILL-SHAPED committed content → defeated citing clause; absent bundle evidence → pending. Register row travels pinned; kernel unchanged |

### CA-07 — defeat subcode registry
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-013 (L-124) | 33-code additive registry + field-role rule (3.3:894–926, 2521–2638) | SUPERSEDED | clause-local enumeration (4.0:729–742) replaces the standard-level registry. Migration: predecessor findings keep their codes as historical evidence; no new finding emits registry codes; the field-role tiebreak survives as C2 guidance |

### CA-08 — Smith-tree corpus and clause kinds
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-014 (L-015, L-081) | SAID-addressed Smith tree, closed node kinds, one-clause leaves, strata (3.3:254, 1288–1322, 2139–2167) | COMPANION | C1; kernel's one-clause/one-ground invariant already carried (4.0:646–659) |

### CA-09 — enactment/supersession/capture-floor law
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-015 (L-009, L-079) | One-epoch capture floor (3.3:213–220, 1198–1247) | KERNEL-SEAT | §15: one sentence (no amendment step may shorten the window that would have caught it) |
| M-016 (L-078) | Unit of enactment; per-class cascade/grandfather; migration maps; probation; emergency sunset (3.3:1161–1197) | COMPANION | C1 |
| M-017 (L-117) | EMG-01 emergency fold equivalence vector (3.3:2249–2268) | RETAINED-DEBT | fixture lane; discharge = executed vector |
| M-018 (L-008) | Inoperability ≠ nonexistence (frozen standing) (3.3:203–212) | COMPANION | C1, with QA-OPEN-02 retirement noted at M-034 |

### CA-10 — genesis battery residue
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-019 | Old fixed-point bundle + exact seal list (3.3:1248–1287) | SUPERSEDED | by the (K0,C) knot (4.0:228–252) — this row makes the supersession explicit |
| M-020 (L-115) | Structural-nonexistence vs curable-posture partition (3.3:2189–2216) | COMPANION | C1 genesis-profile annex |

### CA-11 — N1–N5 constructions
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-021 (L-083) | N1/N1-P pre-rotated law, weakest-branch confession (3.3:1333–1372) | COMPANION | C1 construction profiles |
| M-022 (L-084) | N2 conservative attenuation (3.3:1373–1382) | COMPANION | C2 |
| M-023 (L-085) | N3 sealed clauses, force-at-reveal, anti-grinding (3.3:1383–1437) | COMPANION | C1 (salt dependency → C3) |
| M-024 | N4 two-anchor sovereignty pattern | SUPERSEDED | by the federation envelope (4.0:1162–1192); lifecycle states (pending/renewal/lapse) → C1 via M-025 |
| M-025 (L-086 residue) | N4 amendment/pending/nonrenewal lifecycle (3.3:1438–1462) | COMPANION | C1 |
| M-026 (L-087) | N5 sealed disposition vectors (3.3:1463–1479) | COMPANION | C1 |
| M-027 (L-082) | Election/posture rule for N1–N5 (3.3:1323–1331) | COMPANION | C1 (posture registry adjacency M-031) |

### CA-12 — CPX and predicate language
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-028 (L-088, L-119..122, L-061, L-116) | CPX profile whole: closure/purity/types/operators/bounds, kfs/cpr, epoch anchoring, @ROOT tables, frozen-SAID citation, cross-kind gap (3.3:1484–1521, 2218–2245, 2292–2517) | COMPANION | C2 wholesale |
| M-029 | Predicate-language floor | KERNEL-SEAT | one sentence (§5 or §11): committed predicates SHALL be in a pinned, terminating, canonically-encoded, fail-closed language |

### CA-13 — salt discipline
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-030 (L-125) | Salt annex: 128-bit CSPRNG, domain-separation tuple, no reuse, reveal triple (3.3:2642–2684) | COMPANION | C3, carried intact (security-bearing; no weakening in transit) |

### CA-14 — declared-posture registry
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-031 (L-097) | Posture registry + omission/false-declaration violations (3.3:1665–1692) | KERNEL-SEAT | §13: minimal declaration duty (a GARD SHALL declare its elected postures; omission and false declaration are the two violations); the registry schema itself → C1 |
| M-032 (L-010) | Concentration is posture, not waiver (3.3:221–223) | COMPANION | C1 posture rows |
| M-033 (L-131) | B_end demotion record (3.3:2725–2729) | RETAINED-DEBT | migration row: posture history preserved in predecessor bytes; discharge = C1 posture annex cites it |

### QA-OPEN retirements (explicit supersessions the audit requested)
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-034 (L-093) | frozen(declared|expired) standing state (3.3:1600–1622) | SUPERSEDED | by the five-part freezability criterion (4.0:1548–1554); old semantics readable as historical evidence; C1 carries the state table if revived |
| M-035 (L-058) | Acta-log and three-log admitted profiles (3.3:566–573) | SUPERSEDED | 4.0 adopts KEL/TEL/GEL exclusively; profile plurality retired |

### CA-15 — membrane, blinding, erasure
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-036 (L-098, L-099, L-100) | Strata per event/artifact/node; constitutional outputs unblindable; blinded appraisals non-consumable; duplicity defeats confidentiality; scoped erasure (3.3:1694–1722) | COMPANION | C3 wholesale |
| M-037 | Non-consumability + permanence floors | KERNEL-SEAT | two sentences (§5 or §13): a blinded appraisal SHALL NOT be consumable as a finding; commitment and destruction acts are permanent |

### CA-16 — membership and root/organ boundary
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-038 (L-101, L-118) | Membership/expulsion split; twelve-case root-appraisal table (3.3:1724–1731, 2270–2288) | COMPANION | C1 |
| M-039 | No-root-party-appraisal rule | KERNEL-SEAT | one sentence, §12 |

### CA-17 — asker-blindness and intake classes
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-040 (L-102) | Intake-class declaration; offline replay asker-blind; live-query reservation + rerun gate (3.3:1739–1756) | KERNEL-SEAT | §13: declaration duty + rerun condition (~3 lines); live-query privacy mechanics → C3 |
| M-041 (L-113) | Primitive quarantine/deletion test (3.3:2080–2098) | COMPANION | C4 |

### CA-18 — succession lifecycle controls
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-042 (L-002, L-104) | Detached lineage record; latest-unsuperseded eligibility; superseded-ratification defense; fork rule (3.3:28–65, 1758–1852) | KERNEL-SEAT | §15: detached-record + latest-unsuperseded + fork sentences (~5 lines); succession-object schema + ceremony → C1 |

### CA-19 — conformance ladder
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-043 (L-030, L-108) | G-* rungs; consumption-tier orthogonality (3.3:1923–1937, 2169–2187) | COMPANION | C4 |
| M-044 | Orthogonality floor | KERNEL-SEAT | one sentence, §13: consumption policy SHALL NOT discharge conformance |

### CA-20 — vector corpus
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-045 (L-107, L-110, L-128) | Vector families + manifest posture + unexecuted-emergency debt (3.3:1880–1965, 2715–2717) | RETAINED-DEBT | C4 docket: full predecessor vector inventory; obsolete vectors marked only via explicit supersession map; discharge = C4 manifest |

### CA-21 — projection doctrine and bridges
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-046 (L-114) | Projections derived/nonauthoritative; required reference fields; divergence vs staleness; insufficient-grade reliance (3.3:2102–2128) | KERNEL-SEAT | §5: nonauthority + required-reference fields (~3 lines); failure taxonomy → C4 |
| M-047 (L-112) | Bridge profiles (3.3:2054–2076) | COMPANION | C4 |

### CA-22 — economics and liability
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-048 (L-095) | Economics register: bounty mechanics, subsidy disclosure, no-toll floor, service terms (3.3:1646–1654) | SUPERSEDED | monetary/equilibrium machinery excluded from the kernel by the within-gard vocabulary rule (4.0:875–878); post-seam economics + service terms → C6 (the supersession is of kernel seating, not of the subject) |
| M-049 (L-096) | Obligation artifacts; L1–L5 liability ladder; tenure; piercing warrants (3.3:1656–1663) | COMPANION | C6 |

### CA-23 — witness/watcher behavior pins
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-050 (L-071) | KAWA/DEL inherited pins; first-seen edges; juror/judge roles (3.3:367–387, 813–840) | COMPANION | C5; kernel's witness/watcher distinction already carried (4.0:1568–1589) |
| M-051 (L-092) | Duress-signaling anti-pattern (3.3:1593–1598) | COMPANION | C5 |

### CA-24 — predecessor debts
| Row | Unit | Disposition | Target / ground |
|---|---|---|---|
| M-052 (L-127) | Affected-context vector debt (3.3:2711–2714) | RETAINED-DEBT | C4 docket; discharge = vector executed |
| M-053 (L-129) | Capture-floor/N1 grade tension (3.3:2718–2722) | RETAINED-DEBT | re-opens against M-015's seat; discharge = tension re-adjudicated under 4.0 wording |
| M-054 (L-132) | Frozen-SAID vs @ROOT deferred consent (3.3:2730–2732) | RETAINED-DEBT | C2 docket |
| M-055 (L-133) | N3/secret-law resolved tension (3.3:2733–2740) | COMPANION | C1, travels with M-023 (resolution preserved with its construction) |
| M-056 (L-134) | Zero-seam/telos resolved tension (3.3:2741–2747) | COMPANION | C5, travels with the seam schemas (resolution preserved) |
| M-057 (L-105) | Carried forks/deferrals list (3.3:1853–1865) | RETAINED-DEBT | each fork gets a row in the C-docket it belongs to; discharge = per-fork disposition at first companion drafting |
| M-058 | Old debts unmatched by 4.0 §§13–15 confessions (crypto-agility, PQ deletion, data-availability economics, pre-anchor status, first-seen gaps) (3.3:1966–2053, 2709–2753) | RETAINED-DEBT | one row each in the relevant companion docket at drafting; discharge criterion stated per row; none silently lapse |

## Tallies (PROPOSED)

| Disposition | Rows |
|---|---|
| KERNEL-SEAT | 13 (M-001, 002, 004, 008, 011, 015, 029, 031, 037, 039, 040, 042, 044, 046 — ~30 added lines total, all compact) |
| COMPANION | 27 (C1×14, C2×3, C3×3, C4×4, C5×5, C6×1 by primary target) |
| SUPERSEDED | 7 (M-012, 013, 019, 024, 034, 035, 048) |
| RETAINED-DEBT | 8 |

## Execution note

No row executes until ruled. On ratification of this register:
(1) the 13 kernel seats land in one final byte pass (gate +
guards re-run; second-look reviewers' verified spans untouched);
(2) kernel §15 gains the register pin sentence; (3) companion
charters C1–C6 enter the standing docket with their assigned
cargo; (4) retained-debt rows enter their docket lanes. The
register is then frozen and pinned; 3.3's trail is restored.
