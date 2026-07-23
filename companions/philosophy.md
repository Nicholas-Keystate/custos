# Custos 4.0 — Philosophy Companion

**Status: informative.** This companion binds nothing. The kernel —
Custos 4.0, the ratified standard this repository carries — is the
document of record; its keyword-marked sentences are the law, and
where anything here appears to diverge from the kernel, the kernel
rules and the divergence is a defect of this prose. What this
document carries is the standard's reasons: why a governance layer
above KERI needed to exist at all, why it took the shape it took,
and what a reader should understand about the world the kernel
assumes before reading a single MUST. A specification tells you
what conforms. This companion tells you why conformance was worth
specifying.

Read the kernel first if you implement; read this first if you
want to know what problem you are holding.

---

## 1. The flaw and the layer

KERI solves attribution. Key state committed to witnessed,
end-verifiable logs settles who speaks for an identifier; duplicity
— two voices at one coordinate — is evident to any observer holding
both; and the trust decision is ruled in KERI's own words: an
honest validator must not trust key state carrying unreconciled
evidence of duplicity. There KERI deliberately stops. Whether a
duplicitous authority keeps its seat, whether acts it signed retain
standing, what a counterparty is owed once trust is withdrawn —
these are law above key state, and KERI imposes none. Every
consuming system improvises its consequences, and improvisation
does not compose.

Why is that a flaw and not a feature? Because of an asymmetry that
deserves to be stated as plainly as possible: **integrity is
self-certifying; authority is not.** A self-addressing identifier
is its own proof — the bytes either match their digest or they do
not, and no institution is consulted. But a digest cannot tell you
whether its issuer was entitled to assert a rule, and no
per-artifact mechanism can tell you that you have seen all the
rules. Entitlement and completeness are claims about a rule set,
not about any one artifact, and a rule set needs a distinguished
enumeration surface — a place where a stranger can know it holds
the domain's entire in-force law, not just the fragments someone
chose to show it.

Earlier work in the chartered-registries line put this as a job
description with six properties, and the table survives
translation into 4.0 vocabulary intact. A governance layer that
earns its adjectives must deliver:

| | Property | Statement | Failure means |
|---|---|---|---|
| **P1** | **Completeness** (closed-world rule discovery) | A stranger can know it holds the domain's *entire* in-force rule set, not just the rules someone chose to show it | Rule-state is testimony; split-view by omission |
| **P2** | **Cross-rule order with non-duplicity** | Rule changes are totally ordered against each other and against governed events; equivocation is third-party-detectable | "Which came first, the rule or the act" is litigated, not computed |
| **P3** | **Position-varying law without retroactivity** | Rules change; past judgments are stable under future change (the in-force fold: law-in-force-at-the-position wins, never latest-wins) | Judgment drift; historical verification impossible |
| **P4** | **Judgment non-duplicity** | The domain's *findings* are equivocation-proof: it cannot tell one party "affirmed" and another "defeated" undetectably | Governance accountability is unevidenceable |
| **P5** | **Self-amendment with a home** | The amendment rule governs itself from a well-defined place; the domain has identity criteria as an object | Meta-governance is circular or undefined; "the domain" is a fuzzy cluster |
| **P6** | **KERI-nativity** | End-verifiable from the gAID alone; no foreign consensus; the domain's own witnesses are the trust floor | Sovereignty mortgaged to infrastructure the domain does not control |

That same earlier work then ran the elimination ladder: try to do
the job without a committed governance log, steelman each
alternative, and watch where each one breaks. When it was written,
the ladder argued for a thing that did not yet have a standard.
Custos 4.0 now specifies that thing — the GEL, the governance
event log, and the GARD built around it — so the ladder reads
today not as advocacy but as explanation: this is why the
standard's central object has the shape it has, and why no smaller
shape suffices.

The ladder, one rung per alternative — what each genuinely
delivers, where it breaks against the table above, and the
exploit that breaks it:

| Alternative | What it genuinely delivers | What breaks | The exploit |
|---|---|---|---|
| **Rules sections (the ACDC `r` field) only** | A Ricardian contract per artifact: human- and machine-readable terms, digest-referenced, per-clause SAIDs, assent-gated disclosure — the right tool for exactly what it was designed for | No domain law: norms that apply to classes of parties and change over time cannot live in issued artifacts, and no enumeration surface says which artifacts' rules are the domain's (**P1, P2**) | Amending a rule embedded in ten thousand credentials requires mass re-issuance — so norms never change |
| **Governance-framework documents**, even digest-anchored | A governance *record* with content integrity | Document granularity, not clause granularity; not machine-evaluable; "which version governed at this position" is administrative testimony (**P2, P3**) | The recurring qualification audit — the standing operational cost of law carried at document granularity |
| **Pure charter chains** (governance as credentials and edges) | Issuance authority and scope completely; per-credential revocation | **P1, P2**: no completeness surface — a verifier can never know it has seen *all* applicable rules; per-credential lifecycles, never a sequence of the rule *set* | **Split-view by omission**: show different verifiers different rule subsets without equivocating on any single log. No witness catches it, because no log is incomplete |
| **Per-topic registries, no constitutional root** | Operational governance of each concern (roles, schemas, witnesses) | **P1** one level up (which registries are the domain's?) and **P5** — the amendment rule has no home that governs itself | Meta-governance circularity; the domain has no birth certificate, no identity criteria, no boundary |
| **Bare KEL anchoring** (governance acts sealed directly into the KEL) | Nearly everything: total order, witnessing, duplicity evidence — all inherited | Nothing cryptographic. It fails on KERI's own settled doctrine — the same segregation argument that gave credentials the TEL | Identity verification pays governance traffic; typing and state semantics get rebuilt as seal conventions — a nameless GEL |
| **Re-signed whole-state document** (root-document re-signed on every change) | The current set with threshold self-amendment — deployed at ecosystem scale for a decade elsewhere | **P3** (a tip without history: historical verification impossible) and **P2** (per-client split-view through the serving layer) | Serve different clients different "currents"; rollback and freeze held off only by expiry conventions |
| **External ledger** | P1, P2, P3 genuinely — global consensus supplies order and completeness | **P6**: governance hostage to a validator set the domain does not control; block-time displaces the domain's own first-seen coordinate | Mandate-fragility reborn one layer down: the domain escapes its regulator's mandate and acquires its validators' |
| **Schema-layer governance** (rules as schema evolution) | Typed vocabulary | Schemas are immutable and unordered; "which schema is current" *is* the open question; no standing semantics | Schemas are governance's vocabulary, not its state |

The rung that deserves the most respect is bare KEL anchoring,
because it fails last and teaches most: it delivers total order,
witnessing, and duplicity evidence for free, and what it fails is
a question KERI itself already asked and answered about
credentials — why TELs, rather than sealing credential state
directly into KELs? Segregation of identity lifecycle from
artifact lifecycle; registry-level semantics; verifier
cost-scoping. A reviewer who
accepts TELs but rejects the GEL must explain why rules deserve
less structure than the credentials those rules govern. The
kernel's answer is the modest one: rules deserve the same
structure — a TEL-shaped log with governance semantics, anchored
by the same seal discipline, adding no new anchoring pattern to
the wire. What the KEL is to keys and the TEL is to credentials,
the GEL is to law. Not an invention; the name for the place every
sound path was already going.

The first rung deserves the same careful treatment, because it is
the objection a reader fluent in ACDC raises first: the credential
layer already has a rules section. It does, and it is well made.
The `r` field carries a Ricardian contract — terms and conditions
that are human-readable, machine-readable, and referenceable by
digest — and its deployed uses are precisely contractual:
chain-link confidentiality terms a disclosee must accept before
full disclosure, waivers agreed before issuance, terms of use
that follow disclosed data through a chain of parties. Its
binding mechanism is assent, gated by the exchange ceremony
itself. Nested rule-groups even carry their own self-addressing
identifiers, so the substrate already provides clause-grade
addressing — which is why this standard mints no corpus
primitive. What the rules section cannot do is carry the
authority structure it depends on. A rules section has force
because the credential bearing it was issued under some
framework: something outside the artifact says which schemas are
authoritative, which issuers have standing, which terms a class
of transactions requires. That something is domain law, and it is
exactly what no artifact-interior mechanism can state about
itself. A Ricardian contract needs a jurisdiction. The rules
section is the contract; the GEL is the legal system — and the
relation between them is not competition but consumption: every
`r` field in a governed ecosystem draws its force from the law a
GEL commits. Contract law presupposes a jurisdiction; it cannot
be one.

## 2. Order and law

The deepest frame the standard's development record produced is a
taxonomy, and it is worth stating before the machinery, because
the machinery is its consequence. **Law is the committed subset of
order.** Order is regularity as such — any pattern conduct in fact
follows, whether or not anyone promised it. Law is order committed
to bytes such that deviation is convictable: a regularity signed
into a log, under an identifier, before the positions it judges,
so that conduct departing from it convicts the departing party on
committed evidence. The medium supplies order — key state folds
identically everywhere, digests resolve or convict, duplicity is
evident to any holder of the pair. Frames commit law above that
order. A GARD is a machine for converting order into law.

The conversion is the standard's one move, and the kernel derives
it explicitly: KERI admits events by its own mechanics; a frame
commits law, before the positions that law judges, over which
admitted events are lawful; appraisal returns findings; findings
ground recourse. Nothing below is modified; a layer of committed
judgment is added above an untouched lifecycle. An unlawful
rotation is valid key state and a convictable governance event on
the same bytes — order below, law above, one set of bytes.

The taxonomy also explains a distinction in the kernel's
transformation law that would otherwise look like fussiness.
Between two frames whose committed law shares a fragment, overlap
is measurable: clauses equal by self-addressing identifier, or
rules of one Constitution that another's committed rules satisfy
under a stated lens. The kernel calls this computed congruence and
insists, twice, that it confers nothing — no standing, no
adoption, no recognition follows from overlap by existing. Why
insist? Because congruence is order-grade: a regularity between
two bodies of law, measured, real, and uncommitted. Adoption is
law-grade: a committed event in the adopting frame's own GEL,
naming what it recognizes and under which lens, convictable if
betrayed. The gap between "our laws happen to agree" and "I have
committed to treat your law as evidence" is exactly the gap
between order and law, and the kernel's refusal to let measurement
substitute for commitment is the taxonomy applied at the boundary
between sovereigns. Congruence informs whom a frame adopts;
envelopes crystallize along it; diplomacy starts from a
measurement rather than a blank page. But nothing becomes law by
resemblance.

## 3. The fold

The kernel's definitions section carries a sentence that is easy
to read past and is the whole design: log and fold are one
structure read twice. The log is the committed evidence; the fold
is the computed judgment; nothing in the judgment may exceed the
evidence. A ratified text is an event in the GEL. The Constitution
— the law-in-force of a GARD — is not that text, not any text, but
the value the Gever returns folding the whole committed history at
a position. Two domains holding identical GELs hold identical
Constitutions. Law becomes replayable rather than testimonial: to
know what law governs, you do not ask an official; you run the
fold.

Beneath this sits an ontology worth making explicit, because it
explains why the architecture keeps refusing objects other systems
rush to build. KERI has exactly two moves: **commit a potential**
— digest it — and **realize a fragment** — sign it. Pre-rotation
commits a successor's digest before the successor exists; the KEL
that results is one actualized path through a committed tree of
possible successions. Seals are fragments-by-reference: the KEL
indexes a graph it never totalizes. First-seen is fragment
perspective made law: "the" global key state is a limit object the
architecture declines to construct, because only fragments and
their compositions exist, and the total view is a regulative ideal
— something that orders the system without being a state of it.
Every global object in the stack is such a declined limit, and
this is design, not poverty: an architecture that constructed the
global view would need a party to hold it, and that party would be
the judge above frames that the whole composition law forbids.

Duplicity, in this ontology, has its deepest characterization:
fragments are supposed to compose. Two views of one identifier
should glue on their overlap. Duplicity is the obstruction to
gluing — the committed proof that no consistent whole exists
behind the fragments a party has shown. Watchers are
overlap-computers. And the kernel's duplicity ladder — key tier,
registry tier, governance tier, each tier's two-voices invisible
to the machinery below — is the cost of computing gluing
obstructions at rising structural grain.

What the GARD adds to this ontology is one thing: it carries a
property KERI established for key state up to judgment. Ambient
verifiability — the term is Samuel M. Smith's, from the KERI
whitepaper — names the condition in which verification is
available to anyone, anywhere, from the committed bytes alone,
with no privileged vantage and no permissioned oracle. KERI made
control provenance ambiently verifiable: any validator, holding
the logs, computes the same key state. Custos makes governance
provenance ambiently verifiable: any verifier, holding the logs,
computes the same Constitution, the same standing, the same
finding, to the byte. KERI detects; a GARD appraises; the boundary
between those verbs is the standard's boundary, and everything
the standard does is push the reach of that one property up one
layer — from who may speak, to what the speech was worth under
committed law.

## 4. The reflexive question

*Quis custodiet ipsos custodes?* — Juvenal's question is the
oldest objection to any governance design: who guards the guards?
Every answer that posts another guard regresses. The standard's
answer does not post a guard; it changes what guarding is. The
guardian cannot speak except onto the record. Every act of the
authority — every enactment, every seating, every amendment to its
own law — is either lawful under its committed Constitution or
committed evidence that it was not, and any stranger holding the
logs reaches the same verdict, because the law is bytes and the
verdict is a computation. The guardian is guarded by its own log.

The kernel makes this precise as the reflexive class: governed
law. A GARD's own law passes the governability criterion using
itself — amendments are committed events, anchored through the
domain's own identifier, judged under the Constitution in force
before them. The construction is not paradoxical, because it is
positional: law never applies to itself at a coordinate, only to
its successor at the next, and succession is never retroactive.
Self-description without self-application. The measure of
lawfulness is among the objects measured, and the regress is cut
not by an unmoved mover but by an ordering — each position judged
by the law already in force when it arrived.

A positional recursion needs a base case, and the base case is
the genesis knot. A born-governed domain's genesis is a pair: an
inception event and a founding Constitution text. The text is
computed first — its authors pre-exist the domain — and names the
domain's authority only through a reserved sentinel, resolved at
verification; the inception seals the text's identifier among its
anchors; and the domain's identifier is the inception's
self-addressed prefix, so the founding law lies inside the bytes
the identity digest ranges over. The same keys under a different
founding law name a different domain. Identity and law are
knotted at birth, and the knot is closed by exclusion: the
domain's identifier appears nowhere in the founding text or
anything it cites, so the cycle that would otherwise make genesis
self-referential is cut exactly where no prior Constitution
exists.

The kernel also admits the other construction, honestly: a domain
may incept bare and anchor its founding law later. This is lawful
at a confessed lesser grade — adopted, not born-governed. An
adopted domain's identity ranges over keys alone; its founding
law is as displaceable as any later anchor; and a consuming frame
may weigh the difference. The grades exist because pretending
every domain can be born-governed would be a lie about deployed
reality, and the standard's posture is that a confessed lesser
grade outranks an unconfessed greater claim.

That posture is not hypothetical. The domain that ratified Custos
4.0 is itself adopted-grade, and its published succession record
says so: its authority identifier was incepted before its
founding law was ratified, continuity with the existing lineage
was chosen over re-inception, and the record confesses the grade
in the kernel's own vocabulary. The standard's first act as law
was to state, on the record, the respect in which its own house
falls short of its own strongest construction. That is not an
embarrassment to be footnoted; it is the discipline the whole
document teaches, practiced at the first opportunity, on itself.

## 5. Epistemology

The standard's development record yields one epistemic law that
outranks the rest: **a check that cannot fail is not a check.** It
is testimony wearing a check's uniform. A verifier that rejects
nothing verifies nothing; a probe that cannot find the defect
detects nothing; an affirmation with no exercised refusal is
grounded on nothing. The record behind this is a regularity, not
an anecdote: in adversarial review, the defects that survive
longest live in the checking layer, not the checked layer —
because the primary computation is graded by the world (wrong
keys throw, wrong digests mismatch), while a check is a claim
about a computation, and nothing in the world pushes back when
that claim floats free of its subject. So the standard types its
judgments to make ungrounded affirmation inexpressible: a finding
that does not carry its ground is not a finding; affirmed is
reachable only over a bundle that discharges the question's
entire committed requirement space; an evaluator facing an
uncommitted seam refuses rather than legislates; and an assurance
claim without its discriminating record travels as pending, never
as affirmed. The honest codomain has four values because honesty
needs all four: holds, defeated by this citation, waiting on this
named requirement, convicted out of its author's own mouth.

The same epistemology, turned outward, is the standard's answer
to the institutions it means to succeed. The aim is not to
displace today's credential authorities by force and become the
next unquestioned foundation — unquestionedness is the incumbent
pathology, not the prize. The aim is succession by
accountability: to be a foundation that is cheap to query, quick
to verify, impossible to impersonate, and a witness to its own
duplicity. Each clause of that sentence is an evidentiary claim,
not a promise of virtue. The system does not ask to be trusted;
it asks to be checked, and it is built so that checking is cheap
and every failure of its own conduct is committed evidence
against it.

Which yields the two-line core the whole standard compresses to:

Legitimacy here is replayability. Anyone can be the judge.

Not anyone may rule — ruling is standing under committed law, and
standing is earned through the covenants. But anyone holding the
logs can recompute every judgment the domain has ever issued and
convict the domain of any judgment that does not replay. The
bench is open. That openness is the discipline that makes every
other assurance in the standard mean something: warranted
consumption is honest because replay-native verification never
closes; one honest verifier recomputing from committed bytes
convicts a false warrantor on the warrantor's own signature. The
guard on the whole system is not an office. It is the permanent
possibility of the stranger who folds again.

## 6. The names

The standard's development record kept one rule for vocabulary:
the acronym is the mechanism; the etymology is the doctrine. The
names were chosen as compressed rulings, and they can be read
back as a summary of everything above.

**GARD** — Governed Autonomic Replayable Domain — is the
mechanism: committed law, self-certifying identity, judgment
recomputable by any verifier. But *gard* descends from the root
*gher-*, "to grasp, enclose" — the root of garden, yard, and,
through Latin *cohortem*, of court: the legal court and the
enclosure are one word. The doctrine in the lineage: jurisdiction
is a membrane. Every design question of the form "what may
cross?" is a boundary question, answered by a declared crossing
discipline — the transformation law — never by dissolving the
boundary. And the garden gloss holds too: an enclosure whose
contents are cultivated under continuous care, not a wall around
wilderness. A GARD's law is tended; amendment is constitutive.

**Covenant** — Latin *convenire*, "to come together." A covenant
is weightier than a contract: it constitutes a relationship
rather than clearing an exchange. In the standard, covenants
constrain acts and never perform them; their violation is breach,
appraised on the record — a valid act can be in breach, because
order below survives conviction above.

**Seam** — the stitched line where two fabrics that do not share
a weave are joined: the strongest and most failure-prone line in
the garment. Wherever the standard meets what bytes cannot
contain — the mind that holds a key, the world outside the log —
there is a seam, and the seam discipline is constant: no fact
crosses; only signed, liability-bearing utterances cross. Keys
authenticate; they do not author. The log binds parties to
committed confessions of interior acts; it never claims to verify
them.

**Custos** — Latin, guard, keeper. The name confesses the
standard's deepest interior fact: someone holds the keys. There
is a custodian at the bottom of every autonomic identifier, a
mind the bytes can bind but never contain — and a standard named
for the keeper is a standard that refuses to pretend otherwise.
Juvenal asked who guards the guards, and the question was
unanswerable for two thousand years because every answer was
another guard. The answer here is not a guard. The custodian is
guarded by the log: unable to speak except onto the record,
unable to equivocate without self-conviction, unable to rule
except under law any stranger can replay. Who guards the
guardian? The evidence the guardian cannot avoid creating —
held by anyone, judged by anyone, forever.
