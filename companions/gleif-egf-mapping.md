# The vLEI Ecosystem Governance Framework, read through Custos

**Status:** informative companion to Custos 4.0. Nothing in this
document is normative, for Custos or for anyone else. It is a
mapping exercise conducted under Custos's own law — in particular
under the travel posture of section 13, which forbids any claim in
this corpus from traveling as a defect report against another
ecosystem's governance. Where this document observes a difference
between what GLEIF's framework exhibits and what a Custos
construction would commit, the observation is a description of two
designs, and any question it raises travels as a question.

Citations to GLEIF materials are by document title in the vLEI
Ecosystem Governance Framework's own published corpus, current
edition. Citations to Custos 4.0 are by section number.

## 1. What this mapping is

Start with the concrete instance, because the instance is the
point. GLEIF — the Global Legal Entity Identifier Foundation —
operates the vLEI ecosystem: a production credential system on
KERI in which GLEIF's root autonomic identifier delegates to
Qualified vLEI Issuers (QVIs), QVIs issue Legal Entity vLEI
credentials, and Legal Entities issue role credentials to persons.
The whole arrangement is governed by the vLEI Ecosystem Governance
Framework (EGF): a published document corpus specifying who may be
qualified, what each credential means, what its issuance requires,
when it must be revoked, and how the ecosystem's identifiers are
managed. This is, by any reasonable measure, the world's largest
operating governance framework for KERI infrastructure: real
delegated identifiers, real witnesses, real credential registries,
real qualification and revocation, running under published law.

The thesis of this companion is exhibited rather than argued:
mapped through Custos objects, the vLEI ecosystem is an
adopted-grade GARD implemented in prose. That sentence uses two
terms of art exactly. "Adopted-grade" is Custos 4.0 section 3's
own category: a domain whose identifier was incepted bare, with
its founding law anchored (or in this case published) afterward,
is lawful under Custos at a confessed lesser grade than the
born-governed construction, whose founding law lies inside the
bytes the identity digest ranges over. "In prose" names the
carrier: the EGF's law is committed to documents that auditors
read, rather than to a governance event log that strangers replay.
Neither phrase is a criticism. The adopted construction is a
species section 3 defines and treats as lawful; prose law is how
nearly every governance framework on earth is carried; and the
interesting fact is not that GLEIF's framework differs from a
Custos construction but how little translation the mapping needs.
Row by row, the objects are already there.

The mapping also has a direction of gratitude worth stating once:
Custos did not invent the pattern this section maps. The vLEI
ecosystem demonstrated at production scale that delegated
identifier trees, credential-chained authority, and published
governance frameworks compose on KERI. Custos 4.0 is, in large
part, a formalization of what such an ecosystem exhibits — with
the additional commitment that the law itself become committed,
replayable bytes.

## 2. The mapping, row by row

Each row names the vLEI construct, the Custos 4.0 object it maps
to, and an honest grade: **exhibited in production** where the
vLEI ecosystem already operates the object's substance, and
**Custos-adds** where the Custos object commits something the
current framework carries differently or not at all. Every row
carries both marks somewhere, because that is what adopted-grade
means: the substance is exhibited; the committed, replayable form
is the addition.

| vLEI construct | Custos 4.0 object | Grade |
|---|---|---|
| GLEIF root autonomic identifier (the GLEIF Root AID, per the EGF's identifier management documents) | **gAID** (§3): the identifier whose key event log anchors the domain's governance | Exhibited in production: a real, witnessed, multi-custodial root identifier anchoring the ecosystem's delegation tree. Custos-adds: the born-governed genesis knot — founding law sealed at inception, inside the identity digest's range. The GLEIF Root AID was incepted with its framework published beside it, not sealed into it: the adopted construction of §3, exactly. |
| The EGF document corpus (the Ecosystem Governance Framework and its credential framework documents) | **Constitution** (§3): the law-in-force of the domain | Exhibited in production: comprehensive, versioned, published law actually governing issuance, qualification, and revocation. Custos-adds: the Constitution as *computed state* — under §3 a ratified text is an event in the GEL and the Constitution is what the fold returns over all of them, so two parties holding the log hold identical law by computation. The EGF is published as documents; which edition governed at a past moment is answered by document management rather than by replay. |
| QVI qualification (the Qualified vLEI Issuer qualification program: application, assessment, agreement, authorization to issue) | **Seating** (§3 organ/seat; §7 standing) | Exhibited in production: a real seating ceremony with published criteria, producing a delegated identifier and issuance authority — an organ seated to act in a named role. Custos-adds: the seat as a committed establishment act citing the role's clause, so that the QVI's standing is a covenant-derived judgment (§7) any verifier recomputes from registry evidence, rather than a status GLEIF attests. |
| vLEI credentials — Legal Entity, OOR, ECR (per their respective credential governance framework documents) | **Governed credentials** (§10): issuance and revocation under committed standing covenants (§7) | Exhibited in production: schema-typed, registry-bound, chained credentials with committed issuance and revocation — the substance of the governed-credential class, at scale. Custos-adds: the standing covenant as committed bytes — the rule that says *which* schemas, issued by *which* registries, confer *what*, carried in a replayable Constitution rather than in prose the verifier must read and operationalize per relying party. |
| Annual requalification and periodic review (per the qualification program's ongoing obligations) | **Cadence — the rotation-policy reflex** (§9): the frame's committed relationship to time | Exhibited in production: a real cadence, really enforced — qualification is not perpetual, and lapse has consequences. Custos-adds: cadence as committed clause measured in log positions, so that silence against the cadence is committed, dateable, appraisable evidence (§13's charter) rather than an administrative observation. |
| QVI revocation and termination (withdrawal of qualification, revocation of the QVI's authorization) | **Recourse** (§12): withdrawal of standing as a grounded enactment | Exhibited in production: real consequence — a terminated QVI genuinely loses its power to issue, and the ecosystem's registries reflect it. Custos-adds: the grounded-enactment profile of §12.1 — the revoking act committing, in its own bytes, the evidence bundle, law head, position, and terminal finding that ground it, so any verifier can recompute that the revocation was lawful, not merely observe that it occurred. |
| GLEIF audits and qualification assessments (the review and monitoring activities the EGF and qualification program specify) | **Findings** (§6): the four-valued codomain — affirmed, defeated with citation, pending with typed requirement, self-convicted | Exhibited in production: real appraisal against real criteria, by an authority that acts on the results. Custos-adds: the finding as a replayable object. Today an assessment is an interior act producing a report; a §6 finding is a judgment carrying its own ground, recomputable byte-identically by any verifier holding the committed evidence, with a complete transition system and no backward edges. |
| The delegated AID tree (GLEIF root → GLEIF-delegated identifiers → QVI AIDs → Legal Entity AIDs, per the identifier management documents) | **Delegated organs** (§9): seated organs as delegated identifiers of the gAID | Exhibited in production — and this row runs the other way: §9 says seated organs SHOULD be delegated identifiers, and the vLEI ecosystem is the standing production demonstration of why. Dual-anchored establishment, delegated recovery, authority readable off the KEL tree: the vLEI ecosystem exercises at ecosystem scale what Custos exercises at fixture scale. Custos-adds here is modest: the charter's explicit propagation of availability obligations down the strata (§13). |

One reading of the table, stated plainly: in every row the vLEI
ecosystem exhibits the *substance* — the organ, the law, the
cadence, the consequence — and the Custos addition is uniformly
the same move: carry the rule and the judgment as committed bytes,
so that appraisal is replay rather than testimony. That uniformity
is the thesis. The EGF is not missing pieces of a GARD; it is a
GARD whose law is carried in the one medium replay cannot reach.

## 3. OOR and ECR: one seat species, two evidence grades

The Official Organizational Role and Engagement Context Role
credentials repay a closer look, because the pair independently
exhibits a distinction Custos 4.0 derives from its standing law.

Under section 7, standing is a covenant-derived judgment: registry
evidence in, committed covenant set as the function, judgment of
authority out. Under section 10's relation axis, the same
governed-seat law operates at different distances from the frame's
own keys. Read through those two sections:

- An **OOR credential** evidences a seat whose standing covenant
  requires evidence that crosses an evidence boundary out of the
  ecosystem's own logs: the official role is verified against
  exogenous registries — corporate filings, public records —
  before issuance. In 4.0 terms, the standing covenant's
  requirement set includes composed evidence from outside the
  frame, consumed as evidence under §11's consumption relation:
  authenticated, resolved, appraised under the frame's own law.
  The qualification is corroborated at the boundary where the
  ecosystem's committed evidence ends and the exogenous record
  begins.
- An **ECR credential** evidences an endogenously declared seat:
  the Legal Entity's own committed declaration is the whole
  ground. No boundary is crossed; the standing covenant is
  discharged entirely by evidence the issuing frame itself
  commits.

The distinction is grading, not typology — one seat species,
two committed evidence postures, and a consuming frame may weigh
the difference exactly as §3 says a consumer may weigh the
adopted-grade difference. The EGF's own design already treats the
pair this way: the credential framework documents assign the two
roles different verification obligations, not different natures.

The same pair illustrates the transformation law's force locality
(§11). Consider an ECR credential naming an engagement between
Legal Entity A and Legal Entity B. Two local facts exist, and no
cross-frame binding anywhere: in A's frame, a seat whose scope
carries the engagement context as committed attenuation — its
force reaching exactly as far as A's own law conditions
affordances on it; in B's frame, if B relies, a committed act of
B's own — the foreign credential consumed as evidence (§11.1)
conditioning an affordance B alone grants and B alone withdraws.
The credential travels; force does not. Consumption confers
evidence-weight, never force — §11.1's rule, exhibited by a
production credential design that got the locality right without
a transformation law to tell it to.

## 4. What the mapping surfaces

Three differences between the exhibited system and a Custos
construction, each stated neutrally, each framed as what a GARD
construction would add — because that is what each one is.

**Prose law is read; committed law is replayed.** The EGF's
auditors, qualifiers, and counsel read the framework documents
and apply them — competently, and with the interpretive judgment
prose law requires. A GARD construction would add the other
audience: the stranger. Under §3's Constitution-as-computed-state,
which law governed at any position is a computation over the GEL,
identical for every holder of the logs; "was this issuance proper
under the law as it stood" becomes a replay rather than a records
request. Notably, the EGF corpus is unusually well prepared for
that lift: its documents mark requirements in defined-force
keyword grammar, and §2 of the kernel observes that a framework
marked this way can be lifted, span by span, into committed
predicates. The distance from here to there is a commitment
ceremony, not a rewrite.

**Qualification is attested; standing would be computed.** Today
a QVI's authority is a status GLEIF confers and attests, and
relying parties trust the attestation through the delegation
chain. A GARD construction would add standing as §7 defines it: a
judgment any verifier recomputes from the committed covenant set
over registry evidence, so that "may this issuer issue this
credential class today" is answered by replay rather than by
trusting that the qualification machinery ran. The attestation
does not disappear in that construction; it becomes a warranty
(§11.3) — evidence about a judgment, disciplined by the permanent
availability of replay.

**Audits produce reports; appraisal would produce findings.** An
assessment report is addressed to the parties and to the record; a
§6 finding is addressed to any verifier: it carries its ground,
names its law head and position, and admits exactly the
transitions the codomain's state machine permits. A GARD
construction would add that object — and with it the grounded
enactment of §12.1, under which a revocation carries the terminal
finding that grounds it and is defeated on its own bytes if the
ground fails replay. Consequence that explains itself, in bytes,
to strangers.

Each addition composes with what is already deployed rather than
replacing it. The identifiers, the delegation tree, the registries,
the credential schemas — the entire operational stratum the vLEI
ecosystem runs — is precisely the stratum Custos cites and never
restates. What a GARD construction adds sits above it: a
governance event log beside the key and transaction event logs the
ecosystem already maintains, carrying as committed events the acts
the framework already performs.

## 5. Affordance, and an invitation

A closing observation, carried from work on chartered
entitlements over credential graphs: constitutions do not just
constrain — they afford. A governance framework that can attest
identity and role answers who is legitimate; one whose law is
committed and replayable can go further, minting, scoping, and
revoking what that legitimacy permits, with the same
verifiability the credentials themselves carry. The vLEI
ecosystem's role credentials are the natural substrate for that
extension: an ECR already scopes what a person does in a context,
and the step from a role attested to an entitlement governed is a
vocabulary addition to the framework, not a change to the stack.
A complete polity does both: constrains its organs and affords
its members, on one committed record.

This companion is a mapping, and mappings raise questions. Under
Custos's own travel posture (§13), those questions travel as
questions, addressed to the custodians of the corpus they
concern; nothing here is an allocation request, a defect report,
or a proposal that any ecosystem adopt this standard's objects.
The questions this mapping would ask, if asked: whether the EGF's
keyword-marked requirement spans are a corpus its custodians
would ever wish to see carried as committed predicates; whether a
governance event log beside the ecosystem's existing logs is an
addition its operators would find worth its ceremony; and whether
the qualification lifecycle's evidence — application, assessment,
agreement, authorization — has a committed form its participants
would want replayable. The mapping's own answer is only this: the
objects are already there, the grades are honest, and the
distance is shorter than it looks.
