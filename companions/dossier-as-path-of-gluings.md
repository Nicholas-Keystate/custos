# The Dossier as a Path of Gluings

**Status:** informative companion, draft v0.1 (2026-07-31),
against the ratified 4.1 kernel. Not normative — for Custos, for
the ToIP dossier specification, or for anyone else. Written for
the dossier specification's author and for any implementer of
dossier verification.

**Posture:** per the kernel's travel discipline, nothing here
proposes text for another community's specification; it proposes
a way of *seeing* what that specification already does, and one
test the ecosystem will eventually need that no current
implementation performs. Where this document raises a question,
the question travels as a question. Mathematics is cited at the
end for readers who want it; no part of the argument requires it.

---

## 1. The claim in one paragraph

A credential is not primarily a statement — it is a *splice*. It
takes a fact that lives inside one authority's world (an issuer's
logs, replayable by anyone) and commits an identification across
the boundary into another party's world ("the subject of this
entry IS the controller of that identifier"). A dossier, then, is
not a bag of statements: it is a **path of splices** — a chain of
committed identifications that carries a fact from the world where
it was born, across several sovereign boundaries, to the verifier
who must act on it. Verification, seen this way, is not "check
each signature" — it is "check that the path *composes*: that each
splice was live at the moment relied upon, and that the ends of
the chain actually meet." Every piece of that check is a replay
over committed logs. This reading changes nothing about what
today's dossiers do — and it predicts exactly where tomorrow's
dossiers will fail, which is the reason to write it down.

## 2. Three definitions, no mathematics

**A committed fact.** Anything a stranger can recompute from logs:
"this KEL's controlling keys at event 41 were K," "this registry
issued credential C at its TEL event 12 and has not revoked it."
Inside one authority's cone, such facts are *decided* — replay
settles them, and two honest verifiers cannot disagree.

**A splice (committed identification).** A signed, anchored
assertion that connects two sovereign worlds: an ACDC whose issuer
is one AID and whose subject is another. The issuer cannot decide
facts in the subject's world, and vice versa; the splice is the
*only* lawful connective tissue. Crucially, a splice has *state*:
the issuer's TEL is the ledger of which splices that authority
currently maintains — issuance opens one, revocation closes one
prospectively, with a receipt, at a datable position. KERI never
erases a splice; it closes one on the record.

**A path.** Splices compose: GLEIF identifies a QVI; the QVI
identifies a legal entity; the LE identifies an officer. A dossier
is the committed record of such a path (plus the evidence needed
to replay each hop). The fact that arrives at the verifier — "this
person may sign for that company" — was never decided in any
single world. It is decided only *by the path*.

## 3. What verification is, restated

For each hop: (a) replay the issuer's KEL to the anchoring
coordinate — were the signing keys valid *then*; (b) replay the
TEL — was the splice open *then*, and is it open now if currency
is required; (c) check the schema and the binding of subject to
the next hop's issuer. For the path: (d) check the ends meet —
the root the verifier trusts, and the presenter who is here now.

Notice what (d) really is: a *composition* check, not a signature
check. Steps (a)–(c) are per-hop and every implementation performs
them. Step (d) is where the dossier is more than its parts — and
where a defect can exist that no hop exhibits. That is the
prediction this note exists to make.

## 4. Why nothing has broken yet: today's trust graphs are trees

The vLEI ecosystem — the most mature dossier practice running —
has one root (GLEIF), and authority flows outward. The trust graph
is a **tree**: there are no loops. In a tree, if every hop checks,
the path checks; the composition step (d) can never fail
independently, because two paths between the same endpoints do not
exist. Every current dossier verifier implicitly relies on this.
It is not a flaw. It is an unstated assumption — and it is about
to expire.

## 5. The loop problem arrives with cross-recognition

The moment two ecosystems recognize *each other* — GSMA recognizes
DirectTrust, DirectTrust recognizes an EUDI trust list, EUDI
recognizes GSMA — the trust graph acquires **cycles**. Now two
facts hold at once:

1. Every bilateral recognition can be individually valid, current,
   and honestly maintained; and
2. carrying a credential around the loop — translating it A→B,
   B→C, C→A under the committed recognition agreements — can fail
   to return what you started with.

No hop is broken. No party is dishonest. No pairwise audit will
ever find the defect, because the defect does not live in any
pair — it lives in the *triangle*. Conflict-of-laws has known this
failure for centuries under the name *renvoi* (jurisdiction A
defers to B, B to C, C back to A), and its lesson is standing: the
cure is never another bilateral agreement; it is always a
multilateral instrument that closes the triangle explicitly.

Dossiers will be the first place this bites in our world, because
a dossier is precisely the artifact that *walks* the trust graph.
A dossier assembled inside one ecosystem and consumed in another,
through a recognition edge that is part of a cycle, is a path
whose composition check (d) is no longer guaranteed by the tree
assumption — and no current verifier performs any other check.

## 6. The loop test (implementable today)

The defect is detectable by replay, with no new cryptography:

1. Enumerate the recognition edges the dossier's path relies on.
2. If the relied-upon edges lie in a cycle of the recognition
   graph, walk the cycle: apply each committed translation in
   order to a test credential (or to the dossier's own binding
   claims).
3. Byte-compare arrival against departure (SAIDs make this exact
   rather than interpretive).
4. Mismatch = a **loop finding**: publishable evidence that the
   cycle's translations do not compose, attributable to the cycle
   as a whole, prior to any assignment of fault.

This is a conformance test for *federations*, not for credentials
— a class of test that currently does not exist anywhere in the
SSI stack. An accountant would recognize it instantly: pairwise
receipts are entries; the loop test is the **trial balance**.
Double-entry bookkeeping's genius was not the two entries — it was
the balance check that made a ledger's incoherence computable.
Cross-recognition ecosystems are keeping pairwise books today
with no trial balance. Blockchains avoided needing one by forcing
a single global ledger — one book, no reconciliation, at the price
of a consensus regime and the deletion of every local view that
loses the fork race. Ecosystems of sovereign authorities cannot
pay that price, so they need the balance check instead.

## 7. What a dossier spec could carry (four MAY-grade thoughts)

Offered as digestion material, not as proposed text:

1. **Path explicitness.** A dossier already contains its hops;
   making the *path* a first-class, machine-readable object (an
   ordered list of splice references with their TEL coordinates)
   would let a verifier run step (d) as computation rather than
   reconstruction.
2. **Edge citations.** Where a hop relies on a cross-ecosystem
   recognition, the dossier could cite the recognition instrument
   by digest — making the loop-relevant edges enumerable (step 1
   of the loop test) from the dossier alone.
3. **Cycle disclosure.** An assembler that knows its path touches
   a recognition cycle could say so — a one-bit confession that
   tells the verifier the tree assumption does not hold here.
4. **Loop findings as evidence.** A slot for attaching (or
   referencing) known loop findings about the cycles touched —
   so a federation's published trial balance travels with the
   dossiers that depend on it.

None of these changes what a dossier asserts. They make the
composition check — the one check that today rests on an expiring
assumption — computable by strangers, which is the same standard
every other part of the stack already meets.

## 8. Where the mathematics lives (for readers who want it)

The picture above is a standard one in another field. Facts
decided inside one world are "local sections"; splices are
"identifications on overlaps"; the question of whether locally
valid data assembles into one global story is the "gluing"
problem; the obstruction to gluing is measured by cohomology
(H⁰ = the globally decided; H¹ = pairwise identifications and
their failures; H² = whether the identifications themselves
cohere around triangles — the trial balance). The relevant exact
statement for two worlds is the Mayer–Vietoris principle;
everything used here is finite and computable by replay — no
infinities, no conjectures. The reason for saying this at all:
sixty years of theorems about when local consistency does and
does not imply global consistency come along for free, and they
say the triangle level is not optional — it is the first level at
which honest parts can make a dishonest whole. (References:
any standard treatment of sheaves and Čech cohomology, e.g.
Mac Lane & Moerdijk; the governance-side derivation lives in the
program's annealing record and travels here as companions
mature.)

## 9. Status and custody

Draft for one reader's digestion. Claims about KERI/ACDC/TEL
mechanics are replayable against keripy at the program's pinned
checkout. The tree observation about vLEI is an observation about
the current deployment, not a criticism. "Renvoi" is standard
conflict-of-laws vocabulary; "trial balance" is standard
accounting vocabulary; both cited as observations, never
retitled. The loop test claims novelty only as *deployed
practice* — the underlying mathematics is classical, which is a
feature: the test's authority should rest on replay, not on us.
