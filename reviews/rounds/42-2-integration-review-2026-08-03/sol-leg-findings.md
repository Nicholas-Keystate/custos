Review target: [weave/custos-4.2-candidate-v1.md](/Users/hun-magnon/Documents/KERI/standard-annealing/weave/custos-4.2-candidate-v1.md), 3,596 lines, workspace SHA-256 `8b4f701a4446c4e3899f0f6ed113ce480153c03f541e22b0e773a67bc27c6c8d`.

The charged digest `c62c1dde…` does not identify these bytes. The corpus-identity discrepancy is BLOCKING for ratification. Findings below apply only to `8b4f701a…`.

## Conclusions

The authority’s suspicion is confirmed. The generic register masks three different defects:

- KERI properties are repeatedly promoted into properties of a “medium,” including claims stronger than KERI actually supplies.
- ACDC is usually reduced to “schema + registry + edge,” leaving its disclosure graph, contractual confidentiality, presentation control, and bulk issuance machinery outside the architecture.
- CESR appears deeply only in §19. Elsewhere it is treated as interchangeable serialization, preventing native-CESR forms, streaming proofs, typed framing, and protocol-operation designs.

Five BLOCKING technical claims should not survive unchanged:

1. Clause-selective disclosure is claimed to discharge a no-disclosure mandate while revealing neither evidence nor issuer, without an ACDC presentation construction.
2. Witnesses are said to discharge availability of KEL/TEL/GEL evidence; KERI witness receipts do not provide that guarantee.
3. ACDC edge thresholds are said to be the same algebra as KERI signing thresholds, such that a rotation verifier can evaluate an endorsement quorum.
4. A “substrate-grade blinding factor” in a universal “credential-layer salt-field discipline” is imposed on arbitrary governed objects.
5. The genus reservation and seat-enactment design treats CESR code-table allocation as unilateral GEL law rather than a locally governed profile whose CESR interpretation remains dependent on an externally identified genus table.

## Part A — load-bearing audit

### A1. Medium identity overstates KERI convergence

**Site:** lines 1249–1277  
**Severity:** BLOCKING  
**Classification:** FALSE GENERALITY

“KEL folds to the same key state everywhere” and admission is “identical for every observer” omit KERI’s observer-relative BADA/first-seen state, receipt availability, recovery evidence, and escrow state. Given the same complete accepted event set, the deterministic fold agrees; observers need not hold or accept the same best available data.

Concrete correction: name KERI and separate:

- syntactic/cryptographic verification;
- BADA acceptance by a particular verifier;
- sufficient witness agreement;
- eventual comparison through watchers or KSN exchange.

Checkable surfaces: KERI specification “Best Available Data Acceptance,” “Key State Notice,” “First Seen”; keripy `eventing.Kevery`, `vdr.eventing` BADA branches, and [querying.py](/Users/hun-magnon/Documents/KERI/keripy/src/keri/app/querying.py:23).

### A2. “Medium convicts duplicity” suppresses the witness/watcher mechanism

**Site:** lines 1255–1269; 2361–2371; 2514–2521  
**Severity:** MAJOR  
**Classification:** MISSED INTEGRATION

The text correctly qualifies conviction by possession of both branches, but leaves branch discovery as an abstract observer condition. KERI supplies a concrete detection architecture: witnesses receipt events; watchers compare observed KEL state; KSNs summarize state; judges and jurors adjudicate disputed key-state reports.

Integration: define a governance duplicity-evidence acquisition profile:

1. KSNs for gAID, organ, registrar, and warrantor AIDs;
2. witness-threshold evidence supporting each reported state;
3. watcher discrepancy reports;
4. judge/juror resolution records;
5. conversion of the resulting KERI proof into a Custos typed requirement or self-conviction ground.

This would turn “anyone holding both” into an interoperable acquisition and challenge procedure.

### A3. Selective disclosure is described as an abstract digest trick

**Site:** lines 559–579  
**Severity:** MAJOR  
**Classification:** FALSE GENERALITY

Commit-publicly/disclose-selectively is not inherited merely because bytes have an address and digest. A guessable law clause is dictionary-recoverable; a monolithic SAID does not permit partial verification; selective disclosure requires a deliberately nested, independently saidified and blinded structure.

Integration: represent a Constitution as an ACDC-style nested SAD graph:

- independently saidified clause blocks;
- salts/nonces inside each confidential block;
- edge references from law head to clause blocks;
- schema identifiers typing each block;
- compacted nodes represented by their SAIDs;
- disclosed nodes accompanied by the necessary path and anchor evidence.

ACDC’s technical shape is nested partial disclosure, not “digest exists, therefore selective disclosure.”

### A4. Clause-selective finding does not prove the undisclosed computation

**Site:** lines 603–622  
**Severity:** BLOCKING  
**Classification:** MISSED INTEGRATION

Revealing only the cited clause proves that the clause was committed; it does not prove that the hidden birthdate or other hidden evidence satisfies it. The sentence “a finding is disclosed instead of its evidence” substitutes an assertion for verification unless the verifier replays disclosed evidence, accepts a warranty, or verifies a proof.

Concrete integration: specify three distinct ACDC/KERI-native presentations:

- **Replay presentation:** disclose the relevant nested ACDC evidence blocks and their SAID paths.
- **Warranted presentation:** disclose a registry-bound warranty ACDC citing the finding, clause, evidence commitment, lens, and warranty TEL.
- **Proof presentation:** disclose a proof bound to those same SAIDs.

The current prose conflates all three and therefore overclaims the mandate.

### A5. Issuer non-observation is not achieved “by type”

**Site:** lines 798–807  
**Severity:** BLOCKING  
**Classification:** FALSE GENERALITY

Local appraisal prevents a semantic phone-home requirement, but does not structurally prevent issuer observation. A verifier may query an issuer-controlled TEL, resolve issuer OOBIs, expose correlatable credential or registry identifiers, or use an issuer-observable presentation registry.

Integration: require an offline verification cone, holder-mediated presentation, non-issuer witnesses/watchers or cached TEL state, blinded/link-minimized ACDC disclosure, and a contractually protected disclosure edge. The bar on observation must be tested at the transport and resolution surfaces, not inferred from where meaning is computed.

### A6. Governed credential and registry remain abstract TEL wrappers

**Site:** lines 690–706  
**Severity:** MAJOR  
**Classification:** MISSED INTEGRATION

The architecture uses issuance and revocation state, but not the ACDC credential graph that makes conferral, provenance, delegation, and disclosure machine-addressable.

Integration: make every standing covenant select:

- an ACDC schema SAID;
- issuer/issuee constraints;
- required edge labels and operators;
- source credential chains;
- TEL and presentation-registry requirements;
- permitted disclosure posture;
- contract/confidentiality edges.

That makes standing a fold over an actual typed ACDC graph instead of “registry evidence under some law.”

### A7. “Exactly one entry point: the gAID” is too strong

**Site:** lines 1326–1336  
**Severity:** MAJOR  
**Classification:** FALSE GENERALITY

A gAID is a cryptographic entry point, not a discovery or availability endpoint. A fresh verifier also needs a trustworthy discovery path for KELs, witness endpoints, registries, schemas, and evidence bytes. Those are precisely the surfaces OOBIs and endpoint-role records serve.

Integration: make the verification cone root an OOBI bundle bound to the gAID, with role-specific endpoints for witnesses, watchers, registrars, schema/data resolution, and cone service. Material acquired through OOBI remains subject to in-band KERI/BADA verification.

### A8. Warranty typing is one of the few genuine specific integrations

**Site:** lines 1360–1369  
**Severity:** NOTE  
**Classification:** TRUE GENERALITY at the object boundary; ACDC-specific implementation underneath

“Schema-typed, registry-bound, lens cited by edge” properly identifies ACDC mechanics and yields a warranty that is typed, revocable, and graph-linked. The final “existing toolchain/no bespoke parser” claim is not yet grounded, however: it requires an exhibited ACDC field map, schema, TEL event sequence, edge labels, and successful keripy verification.

Concrete gate: materialize one warranty with `SerderACDC`, schema resolution, `ri` registry binding, edge verification, issuance, revocation, and re-verification.

### A9. Universal credential-layer blinding is not an ACDC rule

**Site:** lines 1386–1395  
**Severity:** BLOCKING  
**Classification:** FALSE GENERALITY

ACDC provides fields and constructions in which salty nonces/blinding can prevent dictionary attacks. It does not provide a universal “salt-field discipline” applicable to every arbitrary self-addressed object. The mandate leaves location, entropy, disclosure, canonicalization, and verification undefined.

Integration: restrict the rule to a named ACDC SAD profile. State:

- which block carries the nonce;
- nonce type and minimum entropy;
- whether it is disclosed with the block;
- which SAID preimage includes it;
- how nested partial disclosure preserves verification;
- must-reject vectors for missing, reused, low-entropy, or misplaced nonces.

Keripy’s current structural surface includes `BlindState`, `BoundState`, `Noncer`, and `structing.blind`; those are not interchangeable with an unspecified credential salt.

### A10. Kever/Tever do not instantiate the governance codomain

**Site:** lines 1435–1439  
**Severity:** BLOCKING  
**Classification:** FALSE GENERALITY

Kever and Tever acceptance machinery do not return Custos’s four-valued, ground-carrying finding type. Escrow, validation failure, missing receipts, stale key state, TEL state, and duplicity evidence are operational and protocol-specific outcomes, not direct instances of `affirmed/defeated/pending/self-convicted`.

Integration: define explicit adapters:

- KERI acceptance/escrow/BADA outcome → typed evidence fact;
- Tever registry state → typed evidence fact;
- Custos Gever predicate over those facts → Custos finding.

Without adapters, “same four-valued scheme at every tier” misleads implementers into changing or misdescribing KERI.

### A11. Recovery windows are described too generically

**Site:** lines 1471–1479  
**Severity:** MAJOR  
**Classification:** FALSE GENERALITY

The non-delegated rule depends on KERI’s recovery geometry: a recovery rotation supersedes a disputed non-establishment suffix from the latest establishment event. Delegated recovery additionally depends on valid delegator anchoring and the delegator’s recoverable state. “Stay open longer” is not a complete decision rule.

Integration: type pending requirements using actual KERI coordinates:

- subject establishment event;
- disputed event;
- candidate recovery rotation;
- prior next-key commitment;
- delegator event and anchoring seal for `dip/drt`;
- witness-threshold and first-seen evidence;
- event that closes the relevant superseding opportunity.

Ground: operational-stratum W7/W8 and keripy `eventing.py` delegated-event escrow and recovery branches.

### A12. ACDC edge algebra is falsely equated with KERI signing thresholds

**Site:** lines 1838–1857  
**Severity:** BLOCKING  
**Classification:** FALSE GENERALITY

ACDC/dossier edge operators compose referenced credential evidence. KERI signing thresholds evaluate indexed signatures against an ordered current key list, including exact rational-weight clauses. Similar threshold notation does not make them “one algebra,” and the ability to validate a rotation does not imply schema, issuer, edge, TEL, or dossier evaluation.

Integration: define an explicit translation profile only if desired:

- ACDC slots and edge labels;
- KERI-style rational threshold syntax;
- canonical slot order;
- issuer qualification predicate;
- duplicate-edge treatment;
- missing, revoked, selectively undisclosed, or wrong-schema slot behavior.

Until that profile exists, say “analogous threshold constructions,” not identical machinery.

### A13. The ignored latest-establishment seal is an identified integration gap

**Site:** lines 1883–1892  
**Severity:** MAJOR  
**Classification:** MISSED INTEGRATION

The candidate itself admits the mechanism and leaves it unused. A latest-establishment seal can bind a claim to the current establishment state without naming a fixed historical event in advance.

Integration surfaces:

- warranty lens key-state freshness;
- organ-seat current authority;
- cone root state;
- federation counterparty state;
- migration/recovery checkpoints.

Its use must be explicit about non-monotonic resolution and appraisal position: “latest” must resolve at a committed position, never ambient now.

### A14. “Generic typed seal with a reserved type value” is under-specified

**Site:** lines 1904–1913  
**Severity:** MAJOR  
**Classification:** FALSE GENERALITY

The claim depends on a concrete CESR seal clan/count code and parser behavior, not on generic seal semantics. A locally reserved semantic value inside an otherwise parseable field is different from introducing a CESR code that vanilla parsers do not know.

Integration: publish the exact CESR/KERI carriage:

- existing seal clan/count code;
- field-map shape;
- location in the anchoring event or attachment group;
- how vanilla keripy parses and preserves it;
- how governance-aware code dispatches the reserved semantic type.

The candidate’s own §19 genus analysis shows why “generic typed” is insufficient.

### A15. KERI delegation is specifically and correctly invoked, but shallowly

**Site:** lines 2028–2038  
**Severity:** NOTE / MAJOR opportunity  
**Classification:** TRUE GENERALITY for the stated recommendation; MISSED INTEGRATION beyond it

The `dip/drt` dual-anchor claim is KERI-specific and sound: the delegate signs; the delegator authorizes through an anchoring seal; delegated establishment and recovery are governed by KERI acceptance.

Missing integration: make seats actual delegated AIDs by profile, not merely `SHOULD`, and map seat creation, rotation, revocation, and loss of delegation to exact `dip/drt` events and escrows. The current “seat is an establishment act” remains too abstract for interoperability.

### A16. The open governed-X generator claims portability it does not possess

**Site:** lines 2071–2087; 2153–2158  
**Severity:** MAJOR  
**Classification:** FALSE GENERALITY

“Any substrate lifecycle” is too broad. The construction relies on KERI-specific properties: self-certifying control, signed and digest-chained events, establishment/non-establishment distinction, committed coordinates, recoverability rules, and anchorable SAIDs. Many event systems satisfying the prose criterion cannot support the stated duplicity or recovery guarantees.

Correction: state the generator over KERI-native or KERI-bound lifecycles, then provide an explicit conformance interface for any foreign lifecycle claiming equivalence.

### A17. Governed witness attestation is not yet tied to KERI witness thresholds

**Site:** lines 2117–2124  
**Severity:** MAJOR  
**Classification:** MISSED INTEGRATION

Witness receipts are grouped with warranties mainly through “duty to speak.” KERI witnesses are a configured set with a toad threshold, establishment-event changes, indexed/non-indexed receipt material, and agreement semantics.

Integration: make an availability charter carry, per stratum:

- witness list and `toad` derived from the applicable establishment state;
- which events require threshold receipt;
- cadence or response-position obligation;
- receipt group form;
- witness-set rotation;
- shortfall represented as exact missing witness indices;
- duplicity evidence where witnesses receipt competing branches.

This would make availability findings derive from KERI receipt machinery rather than metaphor.

### A18. Federation rejects multisig where multisig could serve internal governance

**Site:** lines 2207–2222  
**Severity:** NOTE  
**Classification:** TRUE GENERALITY for bilateral federation; MISSED INTEGRATION elsewhere

Rejecting a shared group AID as the federation itself is grounded: it creates a joint controller and makes exit a group-control operation. That does not justify the architecture’s near-total omission of multisig for gAID administration, organs, warranty issuance, law enactment, or curator liability.

Integration: retain matched anchors for sovereign federation, but permit KERI group AIDs with weighted thresholds as internal organs or threshold warrantors.

### A19. Authentication is not one generic “substrate admission” step

**Site:** lines 2255–2260  
**Severity:** BLOCKING  
**Classification:** FALSE GENERALITY

Signatures, coordinates, and witness receipts do not form one context-free verdict. KERI verification requires current key state, correct establishment lineage, threshold satisfaction, event ordering, possible delegation approval, receipt threshold, escrow resolution, and BADA state.

Integration: make step 1 a typed KERI result containing:

- event cryptographic validity;
- establishment and delegation state;
- controller threshold satisfaction;
- witness receipt threshold and roster coordinate;
- BADA/first-seen grade;
- unresolved escrow requirements.

The Gever can then appraise that result without pretending KERI emitted a scalar verdict.

### A20. Witnesses do not discharge the availability charter

**Site:** lines 2631–2644  
**Severity:** BLOCKING  
**Classification:** FALSE GENERALITY

KERI witnesses provide receipted key-event availability/consistency according to their protocol role. They do not, merely by witnessing, guarantee availability of arbitrary TEL spans, GEL contents, schemas, ACDCs, clause bytes, or dossier payloads. A KEL seal proves commitment, not retrievability of the sealed preimage.

Integration: separate:

- KERI witness receipt obligations for KEL events;
- registrar/backer obligations for TEL state;
- repository or endpoint obligations for schemas, ACDCs, GEL clauses, and cone payloads;
- watcher checks for inconsistent serving;
- OOBI-discovered endpoints;
- signed non-delivery/timeout records where applicable.

### A21. OOBI is reduced to endpoint discovery

**Site:** lines 2651–2666  
**Severity:** MAJOR  
**Classification:** MISSED INTEGRATION

OOBI can carry role-specific introduction data and bootstrap KERI verification relationships; well-known OOBIs and multifactor OOBI authentication also give Custos a native trust-on-first-contact surface.

Integration: define a Custos OOBI profile exposing gAID, witnesses, watchers, registrars, schema servers, cone servers, and governance-genus routes. Resolve OOBI material under BADA before admitting it. Relevant keripy stores include `oobis`, `roobi`, `woobi`, `mfa`, and `rmfa` in `db/basing.py`; resolution lives in `app/oobiing.py`.

### A22. “Encoding layer is closed” is too broad

**Site:** lines 2668–2688  
**Severity:** MAJOR  
**Classification:** FALSE GENERALITY

CESR canonicality is version/genus/table-relative. JSON, CBOR, MGPK, and native CESR representations; version-string handling; field ordering; count-code versions; cold-start identification; and parser profiles can all affect acceptance. Section 19 itself demonstrates that a parser lacking the genus table cannot even skip an unknown group.

Correction: name CESR and pin:

- protocol version;
- CESR genus/table version;
- serialization kind;
- field map;
- count-code table;
- canonicalization profile;
- parser conformance vectors.

### A23. Native composable attachment grammar is declared a default without a form

**Site:** lines 2763–2770  
**Severity:** MAJOR  
**Classification:** MISSED INTEGRATION

This is precisely the under-integration diagnosed by the authority. CESR attachment grammar is not a generic alternative to envelopes: it offers count-delimited groups, nested material, indexed signatures, seal groups, pipelining, and stream framing. The document chooses it rhetorically but designs only §19’s receipt bundle.

Integration: charter concrete CESR-native forms for edicts, findings, warranties, cones, recognition anchors, and grounded enactments, each with a native field map and allowed attachment groups.

### A24. Track-one TEL reuse is not semantically neutral

**Site:** lines 2934–2941  
**Severity:** BLOCKING  
**Classification:** FALSE GENERALITY

Using existing registry ilks with governance semantics is not merely a “colorless base.” KERI TEL ilks have fixed field domains and transition semantics. Reinterpreting those event forms may collide with issuance/revocation/registry meanings or cause registry-capable consumers to mutate TEL state, not simply “parse unharmed.”

Integration: identify the exact TEL ilks and fields reused, demonstrate that their native Tever effects are acceptable, and prove round-trip equivalence. Otherwise use a KERI `exn` route or CESR-native governance form rather than semantic overloading.

### A25. Governance-genus reservation is treated as more autonomous than CESR permits

**Site:** lines 3019–3029; 3153–3175  
**Severity:** BLOCKING  
**Classification:** FALSE GENERALITY

A GEL enactment can govern a local profile, but it cannot by itself reserve CESR code points for interoperable interpretation. A CESR parser sizes and dispatches material through its genus/version tables. The candidate correctly confesses lack of steward recognition, then still speaks of “reserved coordinates” and later says gate two is “pure enactment.”

Concrete correction:

- distinguish a Custos-local experimental genus table from an upstream CESR reservation;
- pin the complete table as bytes;
- give it a protocol/genus/version field;
- require explicit route negotiation and table acquisition;
- treat upstream recognition as the interoperability gate;
- do not call seat enactments sufficient to create CESR meaning.

### A26. §19 is genuinely CESR-native but stops one integration too early

**Site:** lines 3065–3277  
**Severity:** NOTE / MAJOR opportunity  
**Classification:** TRUE SPECIFICITY with MISSED INTEGRATION

The count-code framing, genus-relative parsing, receipt SAD/attachment distinction, and route isolation are actual CESR/KERI mechanics. This is the strongest integrated section.

The missed move: use CESR’s existing outer counted groups and protocol/genus version primitives to make the bundle itself a self-framing native group, rather than define identity over a canonically reassembled concatenation whose group-primary-identifier extraction remains external logic. A Custos bundle group could contain:

1. protocol/genus/version primitive;
2. bundle SAID;
3. counted receipt SAD;
4. counted attachment-group sequence;
5. warranty edge/reference group.

That yields streaming boundary detection, typed dispatch, and single-pass hashing.

## Part B — innovation survey, ranked by leverage

### B1. KERI witness-threshold evidence as the availability and authenticity grade

**Leverage:** 1 — highest  
**Severity:** MAJOR

**Mechanism:** KERI establishment events commit witness sets and receipt thresholds; witness receipts bind events; witness changes occur under establishment succession.

**Custos surface:** verification cones, edict authentication, availability charter, warranties, federation entry.

**Integration:** attach a `KERI-authentication-grade` to every cone root: controller threshold verified, applicable witness roster identified, receipt threshold satisfied, and establishment coordinate cited. Pending findings enumerate missing receipt indices.

**New guarantee:** authentication and replication strength become byte-decidable rather than “heavily receipted.”

### B2. Watchers, KSNs, judges, and jurors as the observation architecture

**Leverage:** 2  
**Severity:** MAJOR

**Mechanism:** KSNs summarize key state; watchers obtain and compare state; judge/juror roles handle disputed reports; keripy exposes role names and KSN query flows.

**Custos surface:** duplicity detection, false-warranty monitoring, charter enforcement, cross-frame conviction.

**Integration:** define governed watcher reports and KSN comparison packages as schema-typed evidence. Seat judges/jurors as constructor-plane organs whose determinations remain replayable evidence, not replacements for the fold.

**New guarantee:** the “credible threat of replay” acquires an operational evidence-production pathway.

### B3. ACDC graduated disclosure as the native clause/evidence graph

**Leverage:** 3  
**Severity:** MAJOR

**Mechanism:** nested saidified blocks may be compacted to their SAIDs; selected blocks expand while undisclosed subgraphs remain commitments; salts protect guessable preimages.

**Custos surface:** Constitution clauses, findings, evidence bundles, cones, law heads.

**Integration:** encode law and evidence as nested ACDC-compatible SAD graphs, with clause-level schemas and salts. A finding carries the disclosed subgraph plus compact commitments to the rest.

**New guarantee:** actual verifiable partial disclosure, rather than disclosure by prose declaration.

### B4. Contractually protected disclosure and chain-link confidentiality

**Leverage:** 4  
**Severity:** MAJOR

**Mechanism:** selective disclosure is accompanied by enforceable restrictions on use and onward disclosure; downstream disclosure carries confidentiality obligations along the chain.

**Custos surface:** admitted and clause-selective postures; cross-frame evidence consumption.

**Integration:** make every protected presentation cite a confidentiality covenant ACDC whose edges identify discloser, disclosee, permitted purpose, onward-transfer conditions, and recourse forum/domain. Downstream disclosure requires a successor edge preserving or strengthening the covenant.

**New guarantee:** misuse and onward disclosure become committed breaches, which cryptographic selectivity alone cannot provide.

### B5. ACDC presentation registries

**Leverage:** 5  
**Severity:** MAJOR

**Mechanism:** an issuee-controlled presentation registry can make presentations independently stateful and revocable, including detection of presentation-key compromise.

**Custos surface:** warranties, admitted disclosure, delegated representatives, replay protection.

**Integration:** require high-stakes warranty or finding presentations to cite an issuee-controlled presentation registry; appraisal checks both credential TEL state and presentation state.

**New guarantee:** compromise or replay of presentation authority can be defeated without revoking the underlying credential.

### B6. KERI multisig and fractional thresholds for governance organs

**Leverage:** 6  
**Severity:** MAJOR

**Mechanism:** group AIDs commit ordered member keys and integer or exact rational thresholds; keripy supplies multisig inception, rotation, interaction, registry, issuance, and revocation coordination.

**Custos surface:** gAID custody, organs, enactments, warrantors, curators, recovery custodians.

**Integration:** define organ profiles as KERI group AIDs, with the organ’s threshold and member succession governed by its KEL and its seat delegated from the gAID.

**New guarantee:** quorum governance is enforced cryptographically at authorship, not merely checked afterward as composed evidence.

### B7. Delegated identifiers as the actual seat primitive

**Leverage:** 7  
**Severity:** MAJOR

**Mechanism:** `dip/drt` events require both delegate signatures and delegator anchoring; delegation and delegated recovery have protocol-level escrows and lineage.

**Custos surface:** seating, organ scope, charter propagation, organ recovery.

**Integration:** replace the abstract default seat with a delegated-AID seat profile. Seat establishment cites the delegated inception/rotation and the delegator anchor; loss of valid delegation defeats standing automatically.

**New guarantee:** an organ cannot manufacture or silently extend its own seat.

### B8. Superseding recovery as constitutional continuity machinery

**Leverage:** 8  
**Severity:** MAJOR

**Mechanism:** pre-rotation commitments authorize recovery; a valid recovery rotation supersedes a disputed non-establishment suffix from the applicable establishment event; delegated recovery adds delegator constraints.

**Custos surface:** unlawful rotations, compromise recourse, anchor grades, pending windows.

**Integration:** define recovery-policy clauses as refinements of actual KERI recovery coordinates, with grounded recourse attached to the recovery rotation or its delegator seal.

**New guarantee:** recovery judgments and finality become protocol-derived rather than an abstract four-axis policy overlay.

### B9. CESR-native governance field maps

**Leverage:** 9  
**Severity:** MAJOR

**Mechanism:** native CESR uses ordered field maps with derivation codes and self-framing primitives; protocol and genus versions determine interpretation.

**Custos surface:** GEL events, findings, requirements, warranties, recognition events, grounded enactments.

**Integration:** mint native field maps for the small stable types, retaining JSON only as a human/debug representation. Each map pins field order, code class, optionality, and version.

**New guarantee:** byte identity, smaller carriage, single grammar, and removal of JSON canonicalization freedom.

### B10. CESR outer counted groups and streaming/pipelining

**Leverage:** 10  
**Severity:** MAJOR

**Mechanism:** count codes delimit groups in quadlets/triplets; streams may be processed incrementally; attachments can follow framed SADs without waiting for a document envelope.

**Custos surface:** cones, receipt bundles, warranty streams, bulk replay.

**Integration:** emit cone segments as independently verified counted groups ordered by committed dependency coordinates. Allow verification and folding to begin before the complete cone arrives; escrow unresolved references by SAID.

**New guarantee:** bounded-memory replay, early tamper detection, resumable transfer, and pipelined appraisal.

### B11. CESR cold-start and genus/version negotiation

**Leverage:** 11  
**Severity:** MAJOR

**Mechanism:** initial trits distinguish message, text, binary, count-code, and opcode forms; protocol/genus versions select code tables. Keripy implements cold-start detection in `kering.sniff` and genus-version handling in `vc.protocoling`.

**Custos surface:** route isolation, compact form, migration, multi-version federation.

**Integration:** begin every Custos-native stream with an explicit protocol/genus/version primitive and committed route profile. Version migration becomes a GEL enactment, while the stream remains mechanically self-identifying.

**New guarantee:** deterministic parser selection and clean coexistence of experimental and recognized Custos genera.

### B12. CESR op codes for governance stream control

**Leverage:** 12  
**Severity:** NOTE / MAJOR if transport enters scope

**Mechanism:** CESR distinguishes operation-code starts from material and count-code starts; op codes can carry stream-control operations without pretending they are committed application events.

**Custos surface:** cone requests, continuation, cancellation, checkpointing, backpressure, route negotiation.

**Integration:** define non-evidentiary op codes for request/continue/end/checkpoint while keeping every governance assertion in saidified event material.

**New guarantee:** operational transport control is mechanically separated from committed governance speech.

### B13. ACDC schema SAIDs as executable governance types

**Leverage:** 13  
**Severity:** MAJOR

**Mechanism:** an ACDC cites an immutable schema by SAID; validators resolve and apply the exact schema; schema changes produce new identifiers.

**Custos surface:** clauses, findings, pending requirements, warranties, recourse acts, seat enactments.

**Integration:** assign a schema SAID to every public Custos object type and make schema migration an explicit GEL enactment with compatibility rules.

**New guarantee:** “typed” becomes independently executable and version-exact.

### B14. ACDC edge labels/operators as the law graph

**Leverage:** 14  
**Severity:** MAJOR

**Mechanism:** edges link ACDCs and other saidified objects under labeled relationships; operators constrain graph satisfaction.

**Custos surface:** verification cones, precedent/succession, federation recognition, evidentiary bearing, warranty lenses.

**Integration:** standardize edge labels such as `ground`, `law-head`, `subject`, `prior`, `delegation`, `registry-state`, `confidentiality`, and `undercuts`; define canonical traversal and cycle refusal.

**New guarantee:** cone closure and evidentiary bearing become graph-verifiable instead of prose-defined citation walks.

### B15. ACDC bulk issuance

**Leverage:** 15  
**Severity:** NOTE

**Mechanism:** a committed set structure can represent issuance to many members with membership proofs and shared state-update machinery rather than one full issuance object per member.

**Custos surface:** mass role admission, witness/observer rosters, federation membership, statutory license populations.

**Integration:** permit a standing covenant to accept membership in a schema-typed bulk issuance set, with individual membership proof and applicable bulk registry state.

**New guarantee:** large governed populations without linear issuance carriage.

### B16. BADA/RUN as the cone synchronization protocol

**Leverage:** 16  
**Severity:** MAJOR

**Mechanism:** BADA determines acceptable best-available state; KERI query/reply routes and KSN/log queries acquire missing events and reconcile state.

**Custos surface:** fresh-verifier cone acquisition, pending cure, mirror divergence, replay synchronization.

**Integration:** map every missing KEL/TEL/GEL dependency to a concrete query route and acceptance predicate; record the resulting accepted state and unresolved escrows.

**New guarantee:** `pending(absent)` acquires an interoperable cure procedure.

### B17. OOBI role discovery and multifactor introduction

**Leverage:** 17  
**Severity:** MAJOR

**Mechanism:** OOBIs introduce AIDs and role endpoints; well-known and multifactor OOBI flows can corroborate endpoint association before in-band verification.

**Custos surface:** gAID bootstrap, cone service, registrars, witnesses, watchers, warranty services.

**Integration:** publish a Custos OOBI bundle and require role-specific resolution records in the cone bootstrap.

**New guarantee:** a stranger can actually find the bytes that “one entry point” is supposed to unlock.

## Ratification disposition

**NOT FIT FOR RATIFICATION.**

The digest mismatch blocks identification of the reviewed candidate. Independently, A4, A5, A9, A10, A12, A19, A20, A24, and A25 contain implementer-misleading false generality. The highest-value repair is not a naming sweep. It is a coordinated integration pass centered on four concrete moves:

1. make KERI authentication a typed result incorporating establishment, delegation, witness threshold, BADA, and recovery state;
2. make Constitution/evidence disclosure an actual nested ACDC graph;
3. make availability and duplicity acquisition use witnesses, KSNs, watchers, judges, OOBIs, and query routes;
4. extend §19’s CESR-native design discipline to every portable Custos object.