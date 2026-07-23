# Confidentiality and anchored delivery

**Companion to Custos 4.0.** This document is not normative. It
elaborates the kernel's confessed disclosure posture and its
availability charter into one connected account; where the two
differ, the kernel rules. Nothing here introduces an object
class, a finding value, or a corpus primitive: every mechanism
named below is the substrate's own, the kernel's own, or a
deployment-lane construction the kernel already scopes.

The subject is one boundary seen from two sides. Disclosure asks
what a domain owes to whom, and what it lawfully withholds.
Delivery asks what a domain serves, and why. The chapters show
the answers coincide: the serving surface a domain's committed
anchors define is exactly the disclosure surface its judgments
require.


## Chapter 1 — Disclosure

### 1.1 The baseline the kernel confesses

The kernel's disclosure posture is the fixed point of this
chapter. The verification cone of an edict — the minimal
committed log spans from which a fresh verifier authenticates
the enacting voice, resolves the coordinate, and recomputes the
enactor's standing — maximizes authenticity and auditability at
privacy's expense: a fetchable cone discloses the registry
evidence it carries, including evidence about persons. The
kernel makes this trade openly — of the three properties no
protocol maximizes at once, authenticity ranks first — and
commits the full-disclosure baseline; confidentiality profiles
are deployment law, not kernel law.

The baseline has a precise consequence for withholding. A cone
span withheld under a graduated-disclosure profile is appraised
by the ordinary pending species: an undisclosed span is a typed
requirement, not a defect. Withholding is lawful but never free
— the domain trades terminal findings for pending ones, and the
trade is readable in every finding it affects.

### 1.2 The salt-assurance ladder

Where a domain publishes digests whose preimages carry personal
or otherwise guarded data, the committed salting discipline
determines what a brute-force adversary recovers from the
digest alone. A revealed salt's entropy is not verifiable after
the fact, so assurance attaches to generation, never to the
value. Four grades:

| Grade | Construction | What a verifier gets |
|---|---|---|
| SA-0 declared | committed salting rules as written; salt drawn by unattested means | a liability-backed posture: a short or reused salt fails at reveal, and the failure is evidence against the committer |
| SA-1 attested | the generation algorithm is committed by digest and executed in an attested environment; the execution record (algorithm digest, context, output commitment) is witnessed | "the committed algorithm ran" — attestor-signed evidence, consumed like any exogenous attestation: it binds the signer and no one else |
| SA-2 derived | the salt is a deterministic derivation over a committed domain-separation context — a deterministic signature (RFC 8032) or a hierarchical derivation from a committed root seed | the committer had no discretion given the key or seed; the verifier recomputes and byte-checks at reveal; the root's entropy carries the derivation |
| SA-3 unique | the salt is a verifiable random function output (RFC 9381) over the context — cryptographically one salt per key and context | grinding is killed rather than detected — but see the polarity rule below before reading this as the top of a ladder |

The grades are declared per surface — per clause kind or
disclosure surface — never per domain: a single domain lawfully
declares different grades, and different polarities, on
different surfaces.

### 1.3 The polarity cross

Commitment multiplicity — one party holding many commitments
whose contents or contexts overlap — is dual-use, split by
which axis carries the multiplicity.

Grinding over contents is the attack: many candidate contents
prepared for one governed slot, the retro-justifying one
revealed after the fact. It is killed at the slot layer — one
sealed clause per governed slot, so at most one commitment can
ever discharge into the position — never at the salt layer,
whose machinery neither causes nor cures it.

Grinding over contexts is the feature: one content, many
presentation contexts, one salt each, so that two presentations
of the same fact are uncorrelatable at the commitment layer.
Hierarchical deterministic derivation from a root seed is the
honest construction: replayable by the issuer (auditable,
provably derived), unlinkable by outsiders. Batch issuance
leverages exactly this multiplicity for privacy.

Each surface therefore declares a polarity beside its grade:
unique-per-slot on adjudicative surfaces (sealed clauses,
committed vectors, envelope anchors — where the law demands one
voice), or multiple-by-design on presentation surfaces
(credentials, presentations, membership evidence — where
correlation is the harm). A domain may declare SA-2
unique-per-slot on adjudicative kinds and SA-2
multiple-by-design on disclosure surfaces: the same machinery,
opposite polarity, both witnessed.

The evidential consequence follows the polarity, not the count.
Multiplicity on a presentation surface is conformant; the
misconduct trigger is multiplicity on a surface the domain
declared unique — a violation of one's own committed posture,
misconduct defined by self-declared law. An SA-2 reveal that
fails recomputation, or a declared SA-1 attestation that is
absent, fails statically at reveal under its own grade.

### 1.4 When each grade is honest

SA-0 is honest wherever the threat model is reveal-time audit:
the domain accepts liability for its salt discipline and the
verifier accepts a posture rather than a proof. SA-1 is honest
where an attestor the consumer already trusts at the seam
exists, and dishonest where presented as more than an
attestation, since it binds only its signer. SA-2 is the honest
default: derivation removes committer discretion and is
checkable by byte equality at reveal, with no new cryptographic
admission. SA-3 is honest only on uniqueness-critical surfaces,
and those are rarer than the ladder's shape suggests:
slot-layer uniqueness already covers most adjudicative need,
the verifiable-random-function construction may not survive a
post-quantum deployment profile, and its necessity must be
argued surface by surface.

The anti-pattern is ladder monotonicity — the belief that a
higher grade is always the safer choice. SA-3 on a presentation
surface is a correlation beacon wearing a security medal:
cryptographically enforced one-salt-per-context uniqueness, on
a surface whose entire purpose is uncorrelatable multiplicity,
hands every observer a linking invariant the domain itself
constructed. The mirror error — salt-layer uniqueness where
slot-layer uniqueness is the actual requirement — secures the
wrong layer and breaks privacy multiplicity as a side effect.
Grade and polarity are chosen together or chosen wrong.

### 1.5 Blinding limits

Withholding has a floor, and the kernel's typing rule draws it.
A finding is a judgment that carries its own ground; a value
without its ground is not a member of the finding type. A
blinded appraisal, whatever assurance machinery produced it, is
therefore not consumable as a finding: a consumer handed a
verdict without its ground holds evidence that someone judged,
not a judgment. It may travel as a warranty — a signed
attestation of a computed finding under a pinned lens, evidence
about a judgment — but the judgment itself remains the
consuming frame's computation, and that computation needs the
ground.

The same floor bounds what a domain may keep confidential.
Constitutional outputs cannot hide: the governance event log's
enactments, the law head a finding cites, the standing
computation a cone must let a stranger recompute — these are
the domain's public spine, because every traveling judgment
depends on strangers recomputing them. Confidentiality profiles
operate below the spine, on leaf evidence: registry evidence
about persons, guarded preimages, spans withheld into pendency.
A profile that blinds the spine produces not a confidential
domain but a domain whose judgments cannot travel.

### 1.6 Graduated disclosure as a confessed trade

Graduated and redacted disclosure — committing digests first
and revealing preimages selectively, under the carriage
specification's own machinery — is the deployment-lane
instrument the kernel already permits. Two disciplines govern
its honest use. First, the pending conversion of 1.1: a
withheld span is a typed requirement, and the domain carries
the pendency it creates. Second, irreversibility: what goes
under an availability covenant is replicated by every verifier
that relies on it (chapter 2), and replication makes erasure
structurally impossible. The redaction boundary is drawn before
first publication — the public graph is the salted, redacted
projection from the start, with no second chance; a profile
that publishes first and redacts later has confessed a breach,
not adopted a posture.


## Chapter 2 — Anchored delivery

### 2.1 The genus, first

The SAID-addressed content graph is the general shape of a
content corpus, and it is the substrate's own: self-addressed
data items, typed edges, digests as names — the credential
layer's graph pattern, not a governance invention. Law is a
tenant of that shape; so are evidence, schemas, dossiers,
ratified texts, conviction records, and the bytes of this
companion. One shape, many tenants — and this companion adds no
corpus primitive to it. What Custos adds is exclusively the
anchoring discipline laid over the shape: which nodes of the
graph a domain's committed events reach, and what reaching
them obligates.

### 2.2 The anchoring discipline

A domain's serving surface is the digest-closure of its
committed anchors: every content item whose digest is reachable
from an event in the domain's logs — a seal in the key event
log, a registry event, a governance enactment — by following
committed digests through the graph, is inside the surface.
What is committed is owed: served on request, disclosable to
the appraisals that cite it, replayable by the strangers the
availability charter names. What is unanchored is not owed,
however adjacent or often requested. The boundary is computed
from the logs, never declared beside them: no committed anchor
is disowned by omission from an index, and no obligation is
acquired by advertising unanchored bytes.

The verification cone is the per-edict instance of this
closure: the minimal spans one edict's replay reads, closed
transitively, shortness convicted by the replay itself. The
serving surface is the union of the cones over everything the
domain has committed — the anchored closure. Cone completeness
is decidable per edict; the charter's obligation is the union.

### 2.3 Availability as covenant

Anchoring says what is owed; it does not by itself keep the
bytes fetchable. The availability charter is the kernel's
committed floor — key state and evidence a domain's judgments
depend on remain available and receipt-consistent at every
stratum of its delegation tree — and this section states the
deployment shape that discharges it. A delivery network does
five things: naming, integrity, discovery, availability,
incentive. Under the substrate's assumptions the first three
dissolve or reduce. Naming and integrity are intrinsic to the
digest: any byte source — mirror, adversary, pocket drive — is
exactly as good as the origin, because verification is in the
name, and untrusted transport is free. Discovery rides the
substrate's out-of-band introduction machinery. Availability is
the irreducible residue: absence is not a signable artifact.
What bytes are can be proven; that a host did not serve them
cannot be transferably proven, because a failed fetch is an
observation, not a fact.

Host misbehavior splits into two cases of different evidential
grade. Serving wrong bytes is self-evidencing to anyone: a
signed response whose payload fails its digest is, with the
host's covenant, a transferable conviction — duplicity-grade
evidence against the host. Serving nothing is observable but
never transferably provable: silence is appraised against a
committed posture — heartbeat cadence, challenge obligations, a
cure window measured in position, standing withdrawal at breach
— and the resulting findings stay pending-shaped and
per-observer. Cryptography handles substitution; covenants
handle silence; a design claiming to make absence transferably
provable has rebuilt a trusted uptime oracle with extra steps.

The covenant construction uses only committed machinery: a
host's identifier commits, in its own log, to serve a named
digest set (or the closure of a named dossier) at named
endpoints, at a heartbeat cadence, until a committed position.
Large artifacts chunk under a hash tree, so a challenge samples
random leaves and custody is proven by logarithmically many
slices. Failed challenges accumulate as witnessed observations
from plural observers — one observer's timeout proves nothing —
and mature into posture breach, cure window, and standing
withdrawal, never retroactively: content served yesterday
remains valid-as-served yesterday.

Above the covenant floor sits the mechanism that makes the
charter cheap to keep: replication through reliance. Every
verifier that replays a cone necessarily holds its complete
evidence bytes at that moment. Under a serve-after-verify
default — cache as projection, derived and never authoritative
— availability grows monotonically with reliance: the more a
judgment matters, the more independently verified copies of its
cone exist, with no coordination. The delivery network is not
deployed; it accretes. Reliance-weighted durability covers the
popular graph; covenant-backed floors cover the unpopular tail.

### 2.4 One boundary, two sides

The disclosure boundary — what a domain owes to whom, at what
grade, behind what salting, into what pendency — and the
delivery boundary — the digest-closure of committed anchors,
under charter — are the same boundary seen from opposite sides.
What the verification cone justifies serving is the honest
answer to what the domain has committed to disclose: every span
a traveling judgment's replay reads is owed, at the disclosure
grade its surface declares; every byte outside the anchored
closure is owed to no one; every span lawfully withheld under a
confidentiality profile is accounted for on both sides at once
— undelivered on the serving side, a typed requirement on the
appraisal side. A domain whose serving surface and disclosure
posture disagree has committed evidence of the disagreement,
readable from its own logs as an unserved obligation or an
unowed delivery.

### 2.5 Open questions, stated as open

Live-query privacy. The charter obligates a serving surface,
and every consumption path is a request at a host: the request
stream itself — who fetched which cone, when, how often — is an
observation surface the salting discipline does not reach.
Salt-assurance grades protect committed digests from preimage
recovery, not requesters from the host's own log of requests.
What a serving host may retain, correlate, or disclose about
its request stream is deployment law without a committed
profile; neither the kernel nor this companion settles it.

Asker-blindness beyond offline replay. A verifier holding a
complete cone replays in private; the domain learns nothing.
The moment verification needs a live fetch — a fresh registry
read, a heartbeat check, a span outside the local cache — the
asker is visible to the surface it queries. Whether a domain
can serve its charter while remaining blind to who is asking —
private information retrieval over the anchored closure, or a
weaker committed non-retention posture — has no committed
construction in this program's record; this companion states
the question rather than answering it.
