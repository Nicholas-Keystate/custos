# X.509 trust-route assumptions — enumeration note
# Status: TO-BE-DEVELOPED — drafted as a working enumeration for
# Daniel Hardman's review; findings-not-edits membrane applies.
# Purpose: enumerate the assumptions of the certificate-authority
# trust architecture as the inherited baseline that KERI-based
# infrastructure (and the GARD layer above it) transcends — so the
# transcendence claim is itemized and checkable, never vibes.
# Custody: X.509/PKIX, CA/Browser Forum, CT are their communities'
# corpora — cited, never restated; every row travels as a question
# or an observation, never a defect report (kernel travel posture).
# Date opened: 2026-07-23

## The eight assumptions, enumerated

A-1. VENDOR-CURATED ROOTS. The relying party's trust anchors are
an administratively curated root store shipped by OS/browser
vendors. The end relier delegates root selection wholesale; the
route of trust begins in a list someone else edits.
  Transcended by: self-certifying identifiers — the root of trust
  is the key pair's entropy, not a curated list; no root store
  exists to edit.

A-2. UNCONSTRAINED CROSS-AUTHORITY REACH. Any trusted CA may
issue for any name: hundreds of authorities each hold the whole
namespace. (Name constraints exist in the spec; deployment is the
counterexample of record.)
  Transcended by: an AID's key state is vouched for by its OWN
  witnesses; no third authority holds issuance reach over it.

A-3. WEAKEST-LINK SECURITY. System security equals the weakest
of all trusted CAs; one compromised or coerced authority breaks
every name (the DigiNotar-class incident as the exhibit).
  Transcended by: per-identifier trust bases; compromising one
  controller's infrastructure reaches that controller only.

A-4. REVOCATION AS RETROFIT. CRL/OCSP are availability-dependent,
privacy-leaking, and soft-fail in deployed practice: consequence
machinery bolted on and widely bypassed.
  Transcended by: KERI — rotation/recovery as first-class
  committed events in the same log as issuance; GARD layer —
  revocation as a grounded enactment carrying its finding
  (consequence as computation, kernel section 12).

A-5. BINDING BY ATTESTATION. The name-to-key binding rests on the
CA's validation procedure (DV/OV/EV) — an interior act, never
committed as replayable evidence. The relier trusts that the
procedure ran.
  Transcended by: the binding IS the derivation — self-addressing
  and self-certifying; nothing interior to trust.

A-6. RENTED IDENTITY, NO SUCCESSION LINEAGE. The name is leased
(registrar) and the certificate expires (CA); rotation is
re-issuance with no committed succession lineage; control
provenance is not end-verifiable.
  Transcended by: pre-rotation and the KEL — committed,
  end-verifiable control provenance across the identifier's whole
  life.

A-7. DETECTION BY VOLUNTARY TRANSPARENCY. Certificate
Transparency is the confession, retrofitted: append-only logs
bolted beside the authority structure, monitors unchartered and
unpaid, misissuance discovered by whoever happens to look. (CT
logs are watchers; the annealing record's S-13/X.509 mapping row
carries this.)
  Transcended by: witnessed receipts as validity condition (KAWA)
  + duplicity evident in the medium; GARD layer — observation
  chartered where obligated (availability charter), ambient where
  free.

A-8. AMBIENT GOVERNANCE. The law of the system (CA/Browser Forum
baseline requirements) is prose; compliance is audited (WebTrust)
not replayed; the ultimate consequence — root-store distrust — is
a vendor's political act with no committed ground. Judgment is
real and entirely unexaminable: the improvised-justice condition,
deployed at Internet scale.
  Transcended by: the GARD — law as committed bytes, findings
  carrying grounds, distrust as a grounded enactment any verifier
  replays. This row is the Custos thesis stated against the
  world's largest running counterexample.

## Shape notes for development (Daniel's review invited on all)

- Rows A-1..A-7 are substrate-level (KERI transcends them); A-8
  is the governance row (the GARD transcends it). The split is
  the same seam as the kernel's KERI-detects/GARD-appraises
  boundary — worth preserving in any published form.
- Each row wants a citation to the X.509/PKIX or CA/B corpus at
  the assumption's seat (RFC 5280, BR sections) before this
  travels anywhere — currently from working knowledge, marked.
- Candidate companion placement: sibling to the GLEIF EGF mapping
  companion (triage-board section J row 1) — EGF maps the
  KERI-native governance exhibit; this note maps the inherited
  baseline. Together they bracket the kernel: what came before,
  what runs today, what the kernel adds.
- Open question for Daniel: which rows does the dossier/vLEI
  work already argue in ToIP-published form, so we cite rather
  than restate?
