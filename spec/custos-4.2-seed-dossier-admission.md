# Custos 4.2 seed — the dossier specification enters §3

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file. Executed
> under ruling R20, edition layer, of supplement 2 of 2026-08-01
> (sha256 7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb
> 1aea2670), which names PR #50 as this layer's vehicle.

---

## What this seed carries

Section 3's substrate of record names three specifications and one
reference implementation. The document dereferences a fourth —
the Trust Over IP verifiable-dossier specification — at three
sites, and its semantics reach inside the fold. R20's edition
layer admits it.

The admission is one clause, and it is not one site. A closing
register-accounting sentence asserts the exact opposite, and a
repair that moves only §3 leaves the candidate self-contradictory
at the same grade as the wall-enumeration incongruence R4 ruled.
Both sites are carried here.

The domain layer of R20 — the Constitution committing revision
digests as a functional-dependency declaration — is a separate
commitment with a separate seed,
`spec/custos-4.2-seed-semantics-pinning.md`. This file is only
the membership question: which specifications are of record.

## Repair, site 1 — §3's substrate of record

**Ratified span.** Cited, not edited (L568–577):

> **The substrate of record.** The protocol layer this document
> builds on is KERI, with ACDC as its credential layer and CESR as
> its encoding layer, in the specifications stewarded by the Trust
> Over IP Foundation's specification working group, and with keripy
> as the reference implementation this standard's executable
> evidence was exercised against, at the pinned checkout its record
> states. The revision of record for each specification is pinned
> in the engagement companion under this document's own pin
> discipline; within this document the substrate is cited by name
> and never restated.

**The defect.** The enumeration is not congruent with what the
document consumes. Three sites dereference the dossier
specification's semantics rather than merely naming it:

| Site | Lines | What is dereferenced |
|---|---|---|
| §6 | L859–869 | the portable carriage form, and a dossier's threshold semantics |
| §8 | L1247–1252 | the ACDC edge grammar *as profiled by* the dossier specification |
| §12.2 | L1643–1646 | presentation as a verifiable dossier; composition-warranty failure |

The §8 site is the load-bearing one. Threshold-operator semantics
decide which slots a pending requirement set enumerates, and
§7.3's byte-identity rule ranges over requirement-set contents.
So an unlisted specification's revision can change a finding, in
a document whose §3 states that the substrate is cited by name.
This is precisely the shape R20 names: semantics consumed by the
fold, reachable by no pin the text authorizes.

**Replacement.** The enumerating sentence gains a fourth member
and one clause of scope:

> **The substrate of record.** The protocol layer this document
> builds on is KERI, with ACDC as its credential layer and CESR as
> its encoding layer, together with the Trust Over IP
> verifiable-dossier specification, whose composition and
> threshold-operator semantics this document's fold consumes at
> the sites its own sections cite — in the specifications
> stewarded by the Trust Over IP Foundation's specification
> working group, and with keripy as the reference implementation
> this standard's executable evidence was exercised against, at
> the pinned checkout its record states. The revision of record
> for each specification is pinned in the engagement companion
> under this document's own pin discipline; within this document
> the substrate is cited by name and never restated.

The scope clause is deliberate. The dossier specification enters
as a consumed-semantics member, not as a protocol layer — it is
not beneath this document in the way KERI is — and stating the
grounds of its membership in the same sentence keeps §3's own
rule 3 (this document derives; it does not allude) satisfied for
the member being added.

## Repair, site 2 — the closing register accounting

**Ratified span.** Cited, not edited (L2464–2471):

> Register accounting, at close: the word "dossier" appears in
> this document only as the proper name of the Trust Over IP
> verifiable-dossier specification, cited as an external corpus —
> a cited name, never this document's own register. The phrase
> "the substrate" appears only after section 3 defines the
> substrate of record by name — KERI, ACDC, CESR — so every use
> dereferences to a named protocol; no reader meets the phrase
> before its referent.

**The defect this repair would create if site 1 moved alone.**
Two independent falsehoods, not one. The sentence enumerates the
substrate of record as "KERI, ACDC, CESR", which site 1 makes a
three-of-four undercount. And it characterizes "dossier" as
*"cited as an external corpus — a cited name, never this
document's own register"*, which is the accounting claim R20's
admission overturns: a specification whose semantics the fold
consumes and which §3 names of record is not merely an external
corpus.

**Replacement.**

> Register accounting, at close: the word "dossier" appears in
> this document as the proper name of the Trust Over IP
> verifiable-dossier specification, which section 3 names of
> record for the composition and threshold-operator semantics
> this document's fold consumes — a cited name under a named
> dependency, never this document's own register. The phrase
> "the substrate" appears only after section 3 defines the
> substrate of record by name — KERI, ACDC, CESR, and the
> verifiable-dossier specification — so every use dereferences
> to a named artifact; no reader meets the phrase before its
> referent.

"Named protocol" becomes "named artifact" because the fourth
member is not a protocol layer, and the accounting sentence would
otherwise mis-type the thing it has just enumerated.

## Ground

**Why admission rather than removal of the dependency.** The
alternative repair is to stop consuming dossier semantics — to
restate the threshold operators in this document's own text. That
is the option §3's own discipline forbids: *within this document
the substrate is cited by name and never restated*. Restating
would also fork a live upstream calculus, which is the failure
the engagement companion's stability caution already documents.

**Why the scope clause rather than a bare fourth name.** A bare
name would make the dossier specification's whole content
substrate of record, including parts the fold never touches. The
functional-dependency posture R20 adopts for the domain layer is
the same posture here: name the semantics consumed, so that a
later revision touching nothing consumed is visibly not a
migration.

**Why both sites in one seed.** §15 treats enumeration congruence
between two sites as a wall, and R4 ruled the wall-list case the
same way — one list, cited from the other site, never two
independently maintained enumerations. The register accounting is
an enumeration of the same set. Splitting them across two seeds
would reproduce the defect the ruling exists to close.

## Notes for the drafting authority

1. **The register accounting is a drafting-pass artifact, and its
   grade is unclear.** It sits at L2464–2471, before the appendix
   of record at L2310 — check the placement against the final
   structure, since a sentence that audits the document's own
   vocabulary may belong with the appendix rather than in ratified
   body text. If it is body text it is ruled material; if it is
   accounting, the repair is bookkeeping. This seed treats it as
   ratified text, which is the conservative reading.

2. **"Of record" now means two things.** For KERI, ACDC and CESR
   it means the protocol layer this document builds on. For the
   dossier specification it means semantics the fold consumes. The
   scope clause distinguishes them inside §3, but §3 does not
   define "of record" anywhere, so the distinction lives in one
   sentence's grammar. A one-line definition would be sturdier and
   is not proposed here, because adding a definition to §3 is a
   larger move than the ruling authorizes.

3. **Whether keripy is a fifth member is untouched and unclear.**
   The ratified sentence attaches keripy with *"and with keripy as
   the reference implementation"*, which reads as an accompaniment
   rather than a member — yet the closing accounting enumerates
   only three, excluding it. This seed does not resolve that; it
   is flagged because the repair puts a fourth member into a
   sentence whose membership grammar was already carrying an
   ambiguity.

4. **§12.2's site may be presentation rather than semantics.**
   L1643–1646 concerns a dossier as a presentation form and a
   composition warranty, which is arguably carriage rather than
   consumed semantics. The scope clause says "composition and
   threshold-operator semantics" and so covers it, but if the
   drafting authority reads §12.2 as pure carriage, the word
   "composition" can come out and the clause narrows to thresholds
   alone.

## Station obligations, elsewhere

None new. R20's vectors — the semantics-pin mismatch firing a
fail-loud refusal, and enumeration completeness where a pinned
rule the prose never mentioned governs anyway — belong to the
domain layer and are routed to #15 from
`spec/custos-4.2-seed-semantics-pinning.md`.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Executed under | Supplement 2, 2026-08-01, sha256 `7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670` — R20, edition layer, item 3 |
| Finding addressed | #43, part 2 (the dossier specification absent from §3's substrate of record) |
| Companion seed | `spec/custos-4.2-seed-semantics-pinning.md` — R20's domain layer |
| Companion artifact | `companions/engagement-companion.md` — carries the row and the observation this seed makes lawful |
| Sites touched | §3 L568–577; register accounting L2464–2471 |
| Re-ruling | No — §3's substrate of record has not previously been ruled |
| Status | Offered for merge. |
| Ratified bytes altered | None |
