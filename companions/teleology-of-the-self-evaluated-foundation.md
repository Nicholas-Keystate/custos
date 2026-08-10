# The Self-Evaluated Foundation
## A teleological history of the idea Custos runs toward

**Status:** DRAFT v0.3 (2026-08-10), published to the custos
companions shelf FOR ADVERSARIAL REVIEW — the claim in §V.6 is
gated on surviving an external double-refutation pass, and this
publication exists to feed that pass: refute it if you can.
v0.3 adds the law strand's three-seat deepening (Elster; Ostrom
1992; Nash's introspective tower) and residue ledger item 7
(the deterrence wager). Informative throughout; the kernel
rules on any divergence.

**Provenance:** four parallel research agents (Opus-class),
2026-08-01/02, each covering one strand under citation discipline:
every citation verified by web search against primary or
authoritative secondary sources; verbatim quotes only where the
source text was actually seen; anything unverifiable is marked
UNVERIFIED in place. Strand reports appear as Parts I–IV essentially
as delivered. Synthesis (Parts 0 and V) by the session that executed
the pilot this history culminates in. This document is written to
survive a Franzén-grade reading: it claims no evasion of Gödel
anywhere — only an accounting discipline over the residue.

**Custody:** every idea herein has named ancestors, cited never
retitled. The novelty claim is confined to §V.6 and stated with its
falsifier.

---

## Part 0 — The telos

A governance system whose own foundation is one of its governed
objects. Four properties, jointly:

- **P1 — self-evaluation.** The system evaluates its own foundation
  to *finding* grade: not sentiment, not votes, but replayable
  verdicts against declared invariants, capable of convicting the
  foundation and of certifying its cure.
- **P2 — sealed acts.** The verification runs are themselves
  attributable, sealed records *inside* the system under
  verification: who ran what, against which bytes, in what order —
  cryptographically committed, replayable by anyone.
- **P3 — liveness.** The evaluation is a standing organ, not a
  one-shot proof: it re-runs as the foundation changes, and a
  foundation change is itself a governed act admitted by replay.
- **P4 — confessed residue.** What cannot be self-verified is not
  assumed away but written into the constitution as a named,
  first-class object — with the form Löb's theorem forces: an
  axiom or an attestation of an external act, never a derived
  reflection theorem.

The concrete instance that motivates this history: on 2026-08-01,
KERI's validation layer for the single-signature fragment was
rewritten as an executable covenant set; a twelve-row invariant
table was run as a conformance suite against the reference
implementation (keripy); the suite convicted the foundation — the
likely-duplicitous escrow path has been dead code upstream since
February 2026 (a two-PR interaction regression; filed as
WebOfTrust/keripy#1569) — the proposed cure was applied in an
isolated worktree and the same suite certified it, with the fix's
blast radius exactly the two convicted rows; and the filing itself
was sealed as an attributable outward act in the polity's own
registry. One pass of the loop: found, filed, simulated, certified,
sealed. The foundation converted from an axiom into a finding
stream.

Each of the four strands below reached some of P1–P4 and paid for
the rest, each in its own currency. The history is teleological in
the honest sense: not that these authors aimed at our target, but
that the target is legible only as the completion of what each of
them, separately, could not finish.

---

# Part I — Logic: the price is discovered

## The Logic Strand: Self-Grounding Has a Price

## 1. Gödel (1931) — the price is discovered

**(a) What was proved.** In "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I" (*Monatshefte für Mathematik und Physik* 38: 173–198, 1931), Gödel proved two theorems. The second is the one that governs this strand. SEP states it as: "For any consistent system F within which a certain amount of elementary arithmetic can be carried out, the consistency of F cannot be proved in F itself" — formally, "Assume F is a consistent formalized system which contains elementary arithmetic. Then F ⊬ Cons(F)."

**Scope conditions, stated exactly** (these matter, because the whole strand is about *not* over-claiming):
- **Consistent.** If F is inconsistent it proves Cons(F) trivially. The theorem is conditional on consistency.
- **Effectively axiomatized** (recursively axiomatizable — the axiom set is decidable). A non-effective axiomatization (e.g. "all true arithmetic sentences") escapes.
- **Interprets enough arithmetic.** For G2, "F must contain a little bit more arithmetic than in the case of the first theorem" (SEP), with PRA a working minimum for the standard proof, and a version available for Robinson's Q.
- **Cons(F) must be expressed via a provability predicate satisfying the Hilbert–Bernays–Löb derivability conditions (D1)–(D3).** This is the load-bearing fine print: G2 is a theorem about *reasonable* consistency statements, not about every arithmetical formula extensionally equivalent to one (cf. Feferman's intensionality point, and Rosser-style variants).

**(b) The tax.** Nothing is externalized yet — Gödel *identifies the bill*. What is given up is Hilbert's hope that a system's own soundness could be an internal theorem. From 1931 onward, any self-grounding architecture must either (i) import an outside stronger principle, (ii) weaken the system until G2's hypotheses fail, or (iii) leave the residue unproved.

**(c) P1–P4.** Touches **P1** negatively: it is the precise statement of the *limit* on evaluating one's own foundation — it says self-evaluation is possible for everything *except* the consistency residue. Lacks P2, P3, P4 entirely; there is no actor, no record, no time.

**(d) Citation.** Kurt Gödel, "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I," *Monatshefte für Mathematik und Physik* 38 (1931): 173–198. VERIFIED (Springer; Wikipedia; SEP "Gödel's Incompleteness Theorems").

## 2. Tarski (1933/1935) — the residue is semantic, not just proof-theoretic

**(a) What was proved.** Undefinability of truth: no sufficiently strong consistent formal system can define its own truth predicate. SEP's Tarski entry gives Theorem I part (b): "assuming that the class of all provable sentences of the metatheory is consistent, it is impossible to construct an adequate definition of truth in the sense of convention T on the basis of [the language itself]." The structural conclusion is the language/metalanguage hierarchy: one "cannot define a truth predicate if the order of the metalanguage is at most equal to that of the language itself."

**(b) The tax.** Truth must be *externalized to a strictly stronger metalanguage*. This is the first explicit statement that self-reference costs you a level — the evaluator must sit above the evaluated. Gödel bounds *provability of consistency*; Tarski bounds *expressibility of correctness*. For a governance substrate this is the sharper constraint: the system can define its own *validity relation* (a syntactic, decidable notion) but not its own *truth*.

**(c) P1–P4.** Bounds **P1**: self-evaluation must be over a *definable-within* predicate (provability, conformance, validity), never over truth simpliciter. No P2/P3/P4.

**(d) Citation.** Alfred Tarski, *Pojęcie prawdy w językach nauk dedukcyjnych* (Warsaw: Towarzystwo Naukowe Warszawskie, 1933); German translation "Der Wahrheitsbegriff in den formalisierten Sprachen," *Studia Philosophica* 1 (1935): 261–405. VERIFIED (SEP "Alfred Tarski"). Note: frequently cited as 1936 (issue circulation); the volume is dated 1935 — flagging rather than resolving.

## 3. Gentzen (1936) — the first honest payment

**(a) What was built.** A consistency proof *for* Peano Arithmetic, using transfinite induction along the ordinal ε₀ plus otherwise elementary means. SEP's Hilbert's Program entry: "Gentzen published a consistency proof of first-order Peano Arithmetic (PA). As Gödel had shown was necessary, Gentzen's proof used methods that could not be formalized in PA itself, namely, transfinite induction along the ordinal ε₀."

**(b) The tax — itemized, and this is the point.** Gentzen did not evade G2; he *named the exact surcharge* and paid it from outside. He later closed the loop himself: transfinite induction up to ε₀ is expressible in PA but not provable in PA (*Mathematische Annalen* 119: 140–161, 1943), while PA does prove transfinite induction up to each α < ε₀. So ε₀ is not an arbitrary import — it is the *measured* strength deficit, an exact price tag. Gentzen defended the principle as "indisputable" (SEP, Hilbert's Program), which is itself a confession-shaped move: the residue is not eliminated, it is declared and argued for on the record.

**(c) P1–P4.** The ancestor of **P4** in embryo: the unverifiable residue is *quantified* (ordinal analysis = "how much foundation do you have to borrow"). Still no P1 (the proof runs outside PA), no P2, no P3.

**(d) Citation.** Gerhard Gentzen, "Die Widerspruchsfreiheit der reinen Zahlentheorie," *Mathematische Annalen* 112 (1936): 493–565; and "Beweisbarkeit und Unbeweisbarkeit von Anfangsfällen der transfiniten Induktion in der reinen Zahlentheorie," *Mathematische Annalen* 119 (1943): 140–161. VERIFIED (Springer; JSL reviews; SEP "The Development of Proof Theory").

## 4. Turing (1939) and Feferman (1962) — systems that grow by confessing

**(a) What was built.** Turing's Princeton thesis constructed *ordinal logics*: transfinite progressions in which each system is extended by adjoining a formal statement of its own consistency, indexed by ordinal notations in Kleene's O. He proved a completeness result for Π⁰₁ sentences — per SEP's proof-theory appendix, "for any true Π⁰₁ sentence φ a number a_φ ∈ cO with |a_φ| = ω+1 can be constructed such that T_{a_φ} ⊢ φ." His hoped-for Π⁰₂ completeness fails (SEP Theorem B.1: "There is a true Π⁰₂-sentence that is not provable in ⋃_{a∈cO} T_a"). Feferman (1962) replaced local with **uniform reflection** and got completeness for *all* arithmetical sentences: "for any true arithmetical sentence θ there exists a ∈ cO such that T_a ⊢ θ," with |a| < ω^(ω^(ω+1)).

**(b) The tax.** It moves, it does not vanish. SEP states the caveat exactly: "recognizing an a ∈ cO with T_a ⊢ ψ is at least as hard as recognizing that ψ is true." The undecidability is displaced from *proving the sentence* into *choosing the right ordinal notation / path through the progression*. Turing additionally showed such progressions cannot be invariant: different notations for the same ordinal yield different theorem sets. So the price of a system that repairs itself by confessing its own consistency is that **the confession itself requires an outside judgment about which confession to make.**

**(c) P1–P4.** This is the closest logical ancestor of the target. It gestures at **P1** (each stage evaluates the prior stage's foundation), strongly at **P4** (consistency is *added as an axiom, explicitly*, rather than assumed away), and — uniquely in this strand — at **P3**: a progression is an ongoing process, not a one-shot proof. It lacks **P2** absolutely: there is no actor who performs a stage, no record of who extended what, no attribution, no seal. And its P3 is idealized (transfinite, non-effective in the choice of path), not *live*.

**(d) Citations.** A. M. Turing, "Systems of Logic Based on Ordinals," *Proceedings of the London Mathematical Society* s2-45 (1939): 161–228. VERIFIED (LMS/Wiley; Oxford Academic; JSL review). Solomon Feferman, "Transfinite Recursive Progressions of Axiomatic Theories," *Journal of Symbolic Logic* 27, no. 3 (1962): 259–316. VERIFIED (Cambridge Core; Feferman's Stanford publication list).

## 5. Löb (1955) — the formal limit on self-trust

**(a) What was proved.** Answering Henkin's problem: for any sentence A in the language of F, "F ⊢ Prov_F(⌜A⌝) → A if, and only if, F ⊢ A" (SEP). A system that can prove "if I prove A, then A" already proves A outright. Corollary: the general reflection scheme Prov_F(⌜A⌝) → A is not available; and G2 falls out by taking A = ⊥.

**(b) The tax.** *Self-trust cannot be asserted; it can only be exhibited.* Any clause of the form "this system's verdicts are sound" is either vacuous (because the conclusion was already provable) or unprovable. A constitution therefore cannot contain a productive internal soundness clause.

**(c) P1–P4.** The precise constraint on **P1** and on the *form* of **P4**: the residue must be confessed as an **axiom or an attestation of an external act**, never derived as a reflection theorem. Löb is why "we assume our own soundness" is not an option and "we record that we could not verify this" is.

**(d) Citation.** M. H. Löb, "Solution of a Problem of Leon Henkin," *Journal of Symbolic Logic* 20, no. 2 (1955): 115–118, DOI 10.2307/2266895. VERIFIED (Cambridge Core; JSTOR; PDF at math.umd.edu).

## 6. Willard (2001) — the sharpest exhibit of the tax

**(a) What was built.** Axiom systems that *do* prove their own consistency, by falsifying G2's arithmetic-strength hypothesis. Willard's abstract (verified text): "We will study several weak axiom systems that use the Subtraction and Division primitives (rather than Addition and Multiplication) to formally encode the theorems of Arithmetic." Provided such a system does not recognize **multiplication** as total, it can verify its own semantic-tableaux, Herbrand, and cut-free consistency; if it additionally does not recognize **addition** as total, it can recognize the consistency of its Hilbert-style proofs. These systems cannot prove their canonical reflection principle, but can prove an approximation Willard calls the **Tangibility Reflection Principle**.

**(b) The tax — visible in the price tag.** Self-verification is *purchased*, and the currency is arithmetic strength: the totality of multiplication (and sometimes addition) is surrendered, which is exactly what the diagonalization needs. This is the cleanest empirical demonstration in the strand that G2's hypotheses are tight and that self-verification is a *trade*, not a discovery.

**(c) P1–P4.** Achieves **P1** in the strongest literal sense available to logic — genuine internal self-verification — and it is the exhibit proving P1 is not free. Lacks P2, P3, P4.

**(d) Citation.** Dan E. Willard, "Self-Verifying Axiom Systems, the Incompleteness Theorem and Related Reflection Principles," *Journal of Symbolic Logic* 66, no. 2 (June 2001): 536–596, DOI 10.2307/2695030. VERIFIED (Cambridge Core abstract fetched; JSTOR; Project Euclid).

## 7. Franzén (2005) — the discipline against over-claiming

**(a) What was built.** A book-length audit of misuses of the incompleteness theorems, explaining them informally while cataloguing in detail the misunderstandings and abuses rife in popular discussion of their significance.

**(b) The tax.** It is the *bill for rhetoric*: any claim that a system "transcends Gödel," or that incompleteness licenses conclusions about minds, machines, or governance, must be checked against the theorems' actual hypotheses (§1 above). Franzén is the standard by which our document should be read: we claim no evasion of G2, only an accounting discipline over the residue.

**(c) P1–P4.** Meta-level; constrains how P1 and P4 may be *stated*.

**(d) Citation.** Torkel Franzén, *Gödel's Theorem: An Incomplete Guide to Its Use and Abuse* (Wellesley, MA: A K Peters, 2005), x + 172 pp., ISBN 1-56881-238-8. VERIFIED (Cambridge *BSL* review; Oxford *Philosophia Mathematica* review; Taylor & Francis).

## Strand Summary

Logic establishes that the residue is **real** (Gödel), that it is **semantic as well as proof-theoretic** (Tarski), that it can be **measured and paid from outside** (Gentzen: ε₀ is the exact price of PA's consistency), that it can be **iteratively confessed as new axioms** (Turing, Feferman) at the cost of an outside judgment about which confession to make, that self-trust **can never be asserted internally without collapse** (Löb), and that genuine self-verification is **purchasable only by giving up arithmetic strength** (Willard). The confession move is therefore not an evasion of Gödel but the licensed response to him — and Löb tells us it must take the form of an *axiom or attestation*, never a derived reflection theorem. What logic cannot supply is everything that makes a governance substrate live: it has **no actor** (nobody performs the extension), **no log** (the act of verifying leaves no attributable, sealed record — P2 is absent from every milestone above), and **no liveness** (Turing–Feferman progressions are the only P3 gesture, and they are transfinite idealizations, not running processes). Custos inherits the residue and the confession discipline from this strand; it must import attribution, sealing, and continuous operation from elsewhere.

**Sources:** [Gödel 1931 (Springer)](https://link.springer.com/article/10.1007/BF01700692) · [SEP: Gödel's Incompleteness Theorems](https://plato.stanford.edu/entries/goedel-incompleteness/) · [SEP: Alfred Tarski](https://plato.stanford.edu/entries/tarski/) · [Tarski undefinability (Wikipedia)](https://en.wikipedia.org/wiki/Tarski's_undefinability_theorem) · [Gentzen 1936 (Springer)](https://link.springer.com/article/10.1007/BF01565428) · [Gentzen 1943 (Springer)](https://link.springer.com/article/10.1007/BF01564760) · [SEP: Hilbert's Program](https://plato.stanford.edu/entries/hilbert-program/) · [SEP: Development of Proof Theory](https://plato.stanford.edu/entries/proof-theory-development/) · [Turing 1939 (LMS)](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/plms/s2-45.1.161) · [SEP: Proof Theory, Appendix B (Turing & Feferman)](https://plato.stanford.edu/entries/proof-theory/appendix-b.html) · [Feferman 1962 (Cambridge Core)](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/transfinite-recursive-progressions-of-axiomatic-theories/F3FE77D3D5E5F27C9A8445BCCA971CFD) · [Löb 1955 (Cambridge Core)](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/solution-of-a-problem-of-leon-henkin1/3A115E94049C3221D4047ED4C340BDAA) · [Löb 1955 (PDF)](https://www.math.umd.edu/~laskow/Pubs/713/Lob.pdf) · [Willard 2001 (Cambridge Core)](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/selfverifying-axiom-systems-the-incompleteness-theorem-and-related-reflection-principles/7CD71AF3AEB5BCA5BAAC2F22FEF92817) · [Franzén 2005 (BSL review)](https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/abs/torkel-franzen-godels-theorem-an-incomplete-guide-to-its-use-and-abuse-ak-peters-ltd-wellesley-massachusetts-2005-x-172-pp/F3C9426992D36C1CD25695871CF6CB87)



---

# Part II — Systems: the toolchain is the attack surface


## The Toolchain Is the Attack Surface
## Systems & security strand, in teleological order

### 1. Ken Thompson, "Reflections on Trusting Trust" (1984)

**(a) Built.** The self-reproducing compiler Trojan. Thompson's Stage III inserts two payloads: one that miscompiles `login` to accept a known password, one that recognizes the compiler's own source and reinserts both. The bugs are then *removed from the compiler source*. The attack survives in the binary with, in his words, "no trace in source anywhere." He demonstrates that the artifact under audit and the instrument of audit are the same object.

**(b) Given up.** Everything. The lecture's MORAL is a terminal confession, not a countermeasure:

> "The moral is obvious. You can't trust code that you did not totally create yourself. (Especially code from companies that employ people like me.) No amount of source-level verification or scrutiny will protect you from using untrusted code."

And the regress is explicitly unbounded: "I could have picked on any program-handling program such as an assembler, a loader, or even hardware microcode. As the level of program gets lower, these bugs will be harder and harder to detect. A well-installed microcode bug will be almost impossible to detect."

**(c) P1–P4.** Touches P4 in embryo — the residue is *named*. But it is confessed as despair, addressed to the reader's conscience, not constituted as a governed provision with a remedy attached. P1 is declared impossible; P2 and P3 absent. This is the attack our telos answers, and its defect is precisely that the confession has no *seat*: nowhere to record it, no one accountable for it, nothing that acts on it.

**(d) Citation — VERIFIED.** Thompson, K. "Reflections on Trusting Trust," *Communications of the ACM* 27(8), August 1984, pp. 761–763. ACM Turing Award Lecture. DOI 10.1145/358198.358210. All quotes read verbatim from the CACM scan (p. 763, MORAL).

### 2. David A. Wheeler, Diverse Double-Compiling (2005/2009)

**(a) Built.** The first real refutation of Thompson's "obvious" moral. DDC, per Wheeler's own summary of the dissertation abstract:

> "source code is compiled twice: once with a second (trusted) compiler (using the source code of the compiler's parent), and then the compiler source code is compiled using the result of the first compilation. If the result is bit-for-bit identical with the untrusted executable, then the source code accurately represents the executable."

The 2009 dissertation adds a formal proof (the 2005 ACSAC paper had only informal justification) and drops the self-parenting assumption; demonstrated against four compilers, including a deliberately corrupted one.

**(b) Given up — the tax.** DDC does not eliminate the trusted seed; it *diversifies* it and then *names* it. It requires a second compiler, independent of the first, capable of compiling the parent's source, and **deterministic**. Wheeler is careful that this second compiler need not be trustworthy in general — only free of "triggers and payloads that would affect the DDC process." The gain is structural, in his framing: "an attacker must simultaneously subvert both the original compiler, and *all* of the compilers used in DDC." The externality is the OUTSIDE itself — you must possess an independent artifact you did not derive from the thing under test.

**(c) P1–P4.** Strong on **P1** (a toolchain evaluating whether its own binary corresponds to its own source) and genuinely strong on **P4**: the required outside is stated as a precondition, not smuggled. This is the closest ancestor of constitutional confession in the whole strand. Lacks **P2** entirely — a DDC run produces a comparison result, not an attributable sealed act; nobody can later prove *who ran it, when, against what*. Lacks **P3**: it is a one-shot audit, not a standing organ.

**(d) Citation — VERIFIED.** Wheeler, D.A. "Countering Trusting Trust through Diverse Double-Compiling," ACSAC 2005 (acsac.org/2005/abstracts/47.html). Wheeler, D.A. *Fully Countering Trusting Trust through Diverse Double-Compiling*, PhD dissertation, George Mason University, 2009 (directors: Menascé, Sandhu); arXiv:1004.5534.

### 3. Bootstrappable builds: stage0-posix, GNU Mes, live-bootstrap

**(a) Built.** The "shrink the axiom" move. Rather than diversify the trusted seed, reduce it until a human can read it. Guix's Full-Source Bootstrap starts from **"a 357-byte program"** (hex0-seed, x86-linux), and from it stage0-posix "first builds hex0 and then all the way up: hex1, catm, hex2, M0, cc_x86, M1, M2, get_machine (that's all of MesCC-Tools), and finally M2-Planet" — thence GNU Mes, TinyCC, and eventually GCC and a full distribution. Because hex0's input is ASCII-hex, the seed binary is byte-equivalent to its own source: the axiom is auditable by eye.

**(b) Given up.** The residue is smaller but real, and the authors say so: a 25 MiB statically-linked `guile-bootstrap` still drives Guix; the Linux kernel is unaddressed; architecture support is limited to x86_64 and i686. Below all of it sits Thompson's microcode. Shrinking an axiom is not discharging it.

**(c) P1–P4.** Advances **P4** materially — the residue is quantified in bytes and published, which is the honest form of confession. Partial **P1** (the toolchain reconstructs its own foundation from an inspectable germ). No **P2**: bootstrap runs are builds, not attributable governed acts. Weak **P3** — CI reruns it, but no organ is constituted around the result.

**(d) Citation — VERIFIED.** Nieuwenhuizen, J. and Courtès, L. "The Full-Source Bootstrap: Building from source all the way down," GNU Guix blog, 26 April 2023. Quotes read from the post.

### 4. Reproducible Builds (Debian et al.)

**(a) Built.** Fold determinism for artifacts. The official definition:

> "A build is reproducible if given the same source code, build environment and build instructions, any party can recreate bit-by-bit identical copies of all specified artifacts."

This converts "trust the builder" into "compare hashes" and makes any single compromised build machine detectable by any independent rebuilder. It is also DDC's enabling condition — bit-for-bit comparison is what makes double-compiling decisive.

**(b) Given up / silently moved.** RB proves *correspondence between inputs and output*. It does not prove the source is benign, the maintainer honest, or the compiler clean. A Thompson-compromised compiler reproduces its payload perfectly — reproducibility is fully compatible with a universally corrupted toolchain, which is exactly why RB needs DDC or bootstrapping underneath it. The build environment's "relevant attributes" are moreover defined by the distributor, so if that environment is itself supplied by the untrusted party, one reproducibly obtains the same compromised result.

**(c) P1–P4.** Real **P3** (continuous rebuild infrastructure across a whole distribution). Partial **P2** — rebuild results are published, but as status pages, not sealed attributable acts with signing identities. No **P1**: RB never evaluates its own validation rules. Weak **P4** — the limits are folklore among practitioners rather than a constitutional article.

**(d) Citation — VERIFIED.** reproducible-builds.org/docs/definition/ (definition quoted verbatim). Debian Wiki ReproducibleBuilds/About.

### 5. Trusted computing: TPM measured boot, remote attestation, IMA

**(a) Built.** IMA measures every executable loaded on Linux before execution and protects the measurement list by extending TPM PCRs, so a remote party can be given a signed quote over the boot-and-load history. This is genuinely *live* self-measurement: the machine reports its own composition, continuously, under hardware protection.

**(b) The axiom moved, not confessed.** The chain terminates in a Core Root of Trust for Measurement and a TPM endorsement key the platform cannot itself measure. Verification bottoms out in a vendor's manufacturing process and certificate — the vendor becomes the Grundnorm. Nothing in the architecture *says* this; the assumption is structural and silent, which is the exact failure mode our P4 exists to prevent. Thompson's regress is not broken here, only relocated to a party with a supply chain of its own.

**(c) P1–P4.** Genuine **P3**. Partial **P1** (the system measures its own loaded foundation, though not its own *validation rules*). Partial **P2** — the measurement list is an append-only log anchored in PCRs, but it is machine-local and the attestation acts are not themselves entered as records. **P4 absent, and inverted**: the residue is assumed away rather than declared.

**(d) Citation — VERIFIED.** Sailer, R., Zhang, X., Jaeger, T., van Doorn, L. "Design and Implementation of a TCG-based Integrity Measurement Architecture," 13th USENIX Security Symposium, San Diego, Aug 2004, pp. 223–238.

### 6. Certificate Transparency (Laurie, Langley, Kasper — RFC 6962, 2013)

**The closest systems ancestor of our telos.**

**(a) Built.** Append-only Merkle logs that audit the *authorities*. The abstract states the protocol publicly logs TLS certificates in a manner that

> "allows anyone to audit certificate authority (CA) activity and notice the issuance of suspect certificates as well as to audit the certificate logs themselves"

and specifies "append-only, untrusted logs of all issued certificates." Issuance produces an SCT — a signed, attributable receipt, entered into a log, at scale, live. Monitors and auditors are *constituted roles*.

**(b) The confessed residue — the row-11 analogue, exactly.** RFC 6962 is explicit that a log cannot prove its own consistency to a client alone. §5: "All clients should gossip with each other, exchanging STHs at least; this is all that is required to ensure that they all have a consistent view." §7.3: "Violation of the append-only property is detected by global gossiping, i.e., everyone auditing logs comparing their versions of the latest Signed Tree Heads. As soon as two conflicting Signed Tree Heads for the same log are detected, this is cryptographic proof of that log's misbehavior."

Read carefully: the split-view/partitioning attack is undetectable *from inside a single client's view*. Detection requires an act of comparison across observers — an irreducibly external cross-check. This is structurally identical to "this log is unforked": the property is not self-verifiable, only cross-verifiable. CT states the requirement honestly in normative text. Its shortfall is downstream: the IETF gossip work remained Internet-Drafts (`draft-ietf-trans-gossip-05`) rather than a deployed universal mechanism, so the confessed residue was named in the constitution but never given a working organ. *[The drafts' status is verified; the extent of production gossip deployment is UNVERIFIED and I do not assert it.]*

**(c) P1–P4.** Strong **P2** (issuance acts are sealed, attributable, logged), strong **P3** (live, adversarial, planetary scale). Partial **P1** — the logs audit CAs and, via consistency proofs, partly themselves. Genuine **P4 in text** — the residue is written into the specification — but under-implemented.

**(d) Citation — VERIFIED.** Laurie, B., Langley, A., Kasper, E. RFC 6962, *Certificate Transparency*, IETF, June 2013. Quotes read verbatim from rfc-editor.org, §5 and §7.3.

### 7. Supply-chain integrity: sigstore/Rekor, SLSA

**(a) Built.** CT's architecture generalized from certificates to *all* supply-chain acts. Rekor is an immutable, tamper-resistant, publicly auditable append-only ledger; every signing event is entered. Fulcio issues short-lived certificates bound to OIDC identity, so signatures carry an attributable actor without long-lived key custody. SLSA layers a build-provenance attestation (in-toto format: builder identity, source commit, trigger, parameters, artifact digest) and a maturity ladder over it.

**(b) Given up.** The roots are assumed: Fulcio's CA, the OIDC identity providers, and the build platform itself. SLSA is admirably candid about scope — Build L1 requires provenance to *exist and be available* while making no requirement about the build platform's trustworthiness *[verified via secondary summaries of slsa.dev, not primary-fetched]*. Provenance testifies that a build happened as described; it does not adjudicate whether the describing rules are sound.

**(c) P1–P4.** The strongest **P2 + P3** pair in the strand: signing acts as sealed, attributable, live log entries, operational across major ecosystems. **P1 absent** — Rekor does not evaluate its own validation layer, and no conformance suite can return a *finding* against it from inside. **P4 absent** — the trust roots are documented engineering assumptions, not constitutional confessions.

**(d) Citation — VERIFIED.** sigstore/rekor, "Software Supply Chain Transparency Log" (github.com/sigstore/rekor); SLSA framework, slsa.dev.

### 8. Tezos: the self-amending ledger (2014 / 2018)

**(a) Built.** A protocol that amends itself through recorded on-chain acts. The white paper — L.M. Goodman, *Tezos — a self-amending crypto-ledger*, 2 September 2014 — specifies a seed protocol under which stakeholders approve amendments *including amendments to the amendment procedure itself*. Mainnet launched 17 September 2018; the amendment cycle (exploration, promotion, cooldown, adoption) has carried the network through many protocol upgrades without hard forks.

**(b) Given up.** Amendment here is *preference aggregation*, not evaluation. Voting establishes that stakeholders assented, never that the proposed validation layer is correct; there is no conformance suite that can return a finding against the reference implementation and no mechanism by which such a finding would bind. And the deepest assumption is inverted: rather than confess non-forkedness as residue, the chain *defines it away* by consensus — the one property our telos insists must be confessed is the one a blockchain claims to have abolished.

**(c) P1–P4.** Real **P3** and real **P2** (amendment acts are attributable, sealed, ordered, on-chain). **P1 only nominally** — it amends its foundation without evaluating it. **P4 absent by construction.**

**(d) Citation — VERIFIED.** Goodman, L.M. *Tezos — a self-amending crypto-ledger*, white paper, 2 September 2014 (tezos.com/whitepaper.pdf); mainnet 17 September 2018.

## Strand summary

Thompson proved the toolchain is the attack surface and drew the wrong conclusion — that the only remedy is to create everything yourself, a counsel of despair with no seat and no remedy. Everything after is an argument with that sentence. Wheeler refuted its finality by *naming* a required outside: DDC works precisely because it confesses what it needs. Bootstrappable builds shrank the axiom to 357 auditable bytes; reproducible builds made artifacts foldable and comparable; trusted computing made measurement live but relocated the axiom to a vendor without saying so. Certificate Transparency contributed the decisive move — verification acts recorded in an append-only log that audits the authorities — together with the honest admission, in normative text, that a log cannot prove its own consistency to a lone client. Sigstore and SLSA made that architecture operational for the whole supply chain. What the strand delivers to our telos is therefore liveness, logs, and the discipline of either shrinking or diversifying the trusted seed. What it never delivered is P1 and P2 *held together*: the systems that evaluate a foundation (DDC, bootstrapping) leave no attributable record, and the systems that keep attributable records (CT, Rekor, Tezos) never evaluate their own validation layer to finding grade. The evaluator and the evaluated never became the same governed system — and P4, stated well by Wheeler and by RFC 6962, was everywhere a footnote rather than an article of the constitution.



---

# Part III — Verified verifiers: the tower and the confessed core


## The Verified-Verifier Line: Constructive Precedents in Mechanized Proof

Each milestone below pays Gödel's tax in a different currency. None achieves P2 (verification acts recorded attributably inside the verified system) or P3 (live, continuous operation) — every one is a one-shot artifact. The differentiator across the strand is *how much* of P1 (self-foundation-evaluation) is reached, and *how honestly* P4 (confessed residue) is stated.

## 1. The LCF Architecture and the de Bruijn Criterion (1972–1979; criterion named 2005)

**(a) What was verified.** Nothing was verified in the theorem-proving sense. LCF is an *architectural* answer: theorems live in an abstract ML type `thm` whose only constructors are the primitive inference rules, so the host language's type checker enforces that every theorem was derived by rule application. The theorem shape is not "⊢ Con(S)" but a static discipline: *no term of type `thm` exists that was not built by the kernel*. The de Bruijn criterion is the complementary move: a system satisfies it if it emits proof objects checkable by an independently written small program. Barendregt and Wiedijk state it as: a proof assistant satisfies the criterion if it generates "proof terms that can be checked independently from the system by a simple program that a skeptical user could write him/herself" — the verifying program "can be small" even when "the proof may have the size of several Megabytes."

**(b) Tax paid.** Everything: the ML compiler, the runtime, the host OS, the hardware, and — critically — the *parser and printer* outside the kernel are trusted wholesale. The kernel is small but unverified; only *shrunk*.

**(c) P1–P4.** No P1 (the system does not evaluate its own foundation; it merely makes the foundation small enough to eyeball). No P2, no P3. Partial P4 in spirit only — the trusted base is *named* but not constitutionally recorded.

**(d) Citation — VERIFIED.** M. Gordon, R. Milner, C. Wadsworth, *Edinburgh LCF: A Mechanised Logic of Computation*, LNCS 78, Springer, 1979. De Bruijn criterion: H. Barendregt and F. Wiedijk, "The Challenge of Computer Mathematics," *Phil. Trans. R. Soc. A*, 2005 (text at cs.ru.nl/~freek/notes/RSpaper.pdf).

## 2. Harrison, "Towards Self-verification of HOL Light" (IJCAR 2006)

**(a) What was verified — precisely.** Harrison verified *an imperfect but quite detailed model* of the HOL Light kernel — explicitly **without definitional mechanisms** — against a set-theoretic semantics formalized inside HOL Light itself. He does not prove ⊢_HOL Con(HOL), and says so. The two theorems are, verbatim from the paper:

> "– I ⊢_HOL Con(HOL) for a new axiom I about sets.
> – ⊢_HOL Con(HOL − {∞}) where HOL − {∞} is HOL with no axiom of infinity."

The added axiom I is a cardinal-closure assertion about a type universe (`(:ind_model) <_c (:I)` plus closure under powerset), i.e. a weak large-cardinal hypothesis. This is the two-system dodge stated with total honesty. Harrison also states the framing constraint outright:

> "if we want to prove the consistency of a proof checker, we need to use a logic that in at least some respects goes beyond the logic the checker itself supports."

**(b) Tax paid.** Two currencies at once: (i) an axiom removed (infinity) in one direction, (ii) an axiom added (I) in the other; plus definitional mechanisms out of scope, plus the model is of the *abstract logic*, not of the running OCaml. Harrison additionally confesses the reflexive-bootstrap risk — a soundness bug in HOL Light could be what "proved" these very statements — and answers it *externally*, by noting HOL Light proof logs are re-checkable in Isabelle/HOL (Obua's work).

**(c) P1–P4.** Strong P1 in aspiration and partial in fact. No P2, no P3. **Best-in-class P4 for its era**: the residue is not merely admitted but quantified into two named axiom deltas plus an external cross-check. This is the closest ancestor of "constitutionally confessed."

**(d) Citation — VERIFIED.** J. Harrison, "Towards Self-verification of HOL Light," IJCAR 2006, LNCS 4130, pp. 177–191 (author's page: cl.cam.ac.uk/~jrh13/papers/holhol.html; quotes taken from the PDF at that location).

*Successor, VERIFIED:* R. Kumar, R. Arthan, M. Myreen, S. Owens, "Self-Formalisation of Higher-Order Logic," *JAR*, extending Harrison's result to definitional mechanisms plus a CakeML kernel refinement.

## 3. Milawa — Davis (PhD 2009) and Myreen & Davis (ITP 2014 / JAR 2015)

**(a) What was verified — precisely.** Milawa is the *tower*. A Level 1 proof checker (`logic.proofp`) implements only the primitive rules. Eleven levels are built: each Level n+1 checker accepts new derived rules as single steps, and is **admitted by the level below** — a Level 1 proof of the Level 2 checker's "fidelity claim" is emitted and checked, then Level 2 admits Level 3, and so on to Level 11 (Level 2: propositional rules … Level 6: clause splitting … Level 9–10: fast rewriting … Level 11: all remaining tactics). The bootstrap comprises 2,081 definitions, 13,563 theorems, 8.4 GB of proof files; a Level 1 proof of one Level 7 obligation *failed after 25 GB allocated* — the tower exists because flat checking is infeasible, not merely inelegant.

Myreen & Davis then took it down to metal. In HOL4 they formalized Milawa's logic, proved it sound, proved the 1,700-line Lisp kernel faithful to that logic, and composed this with the x86 machine-code verification of the Jitawa Lisp runtime. Top-level theorem: a Hoare triple over the x86 model — total correctness (termination guaranteed) but *partial* in that any run may legitimately exit with an error message (heap exhaustion, overflow).

**(b) Tax paid.** The metatheory is **external**: HOL4, not Milawa, proves the soundness. Milawa's logic is deliberately weak (untyped, computational) precisely so HOL4 can prove it sound directly. The paper lists the skeptic's four remaining attacks explicitly: bugs in HOL4/its ML runtime/C compiler/OS/hardware; errors in the HOL4 x86 model versus real silicon; OS-mediated I/O; and mis-definition of the semantics (`|=π`) itself.

**(c) P1–P4.** The **strongest P1 in the strand** and the closest constructive ancestor of admission-by-replay: the tower is literally a chain of admissions, each certified by the level below, with the bottom small enough for human scrutiny. No P2 — the admissions produce proof files, not attributable sealed acts by identified parties. No P3 — proved once, ~4 person-years, then frozen. Good P4: the four-avenue skeptic's list is a confession, though a prose one, not a constitutional artifact.

**(d) Citations — VERIFIED.** J. C. Davis, *A Self-Verifying Theorem Prover*, PhD dissertation, University of Texas at Austin, December 2009 (UT repository). M. O. Myreen and J. Davis, "The Reflective Milawa Theorem Prover is Sound (Down to the Machine Code that Runs it)," ITP 2014; extended in *Journal of Automated Reasoning* 55 (2015), DOI 10.1007/s10817-015-9324-6.

## 4. CakeML (Kumar, Myreen, Norrish, Owens, POPL 2014)

**(a) What was verified.** A mechanically verified implementation of a substantial subset of Standard ML, realized as a read-eval-print loop in x86-64 machine code, with a correctness theorem stating that the REPL prints only results permitted by CakeML's semantics. Scope spans lexing, parsing, type checking, incremental/dynamic compilation, garbage collection, bignum arithmetic — and **compiler bootstrapping**: the compiler is applied to itself *inside the logic*, so the machine-code artifact is produced by verified evaluation rather than by an unverified build step.

**(b) Tax paid.** The metatheory is external (HOL4). The theorem is relative to a HOL4 model of x86-64. Bootstrapping-in-the-logic removes the compiler-build trust hole but not the prover, ISA model, OS, or hardware.

**(c) P1–P4.** P1 only for the *compiler's* foundation, not the logic's — CakeML does not evaluate the theory that certifies it. No P2, no P3. Modest P4 (assumptions stated in prose).

**(d) Citation — VERIFIED.** R. Kumar, M. O. Myreen, M. Norrish, S. Owens, "CakeML: A Verified Implementation of ML," POPL 2014, San Diego, DOI 10.1145/2535838.2535841.

*Convergence point — VERIFIED:* O. Abrahamsson, M. O. Myreen, R. Kumar, T. Sewell, "Candle: A Verified Implementation of HOL Light," ITP 2022, LIPIcs 237, 3:1–3:17 (extended version in *JAR*, 2025). Candle closes the Harrison and CakeML lines: a HOL Light clone with an end-to-end soundness theorem down to the executing machine code — every exported fact is valid in higher-order logic — with the REPL running the CakeML compiler internally. Still one-shot; still external metatheory; still no P2/P3.

## 5. Metamath Zero (Carneiro, 2019–present) — get the status right

**(a) What was verified — and what was NOT.** MM0 is a verification system with a multi-sorted first-order logic, formally specified in its own language, with a binary proof format (MMB certificates) admitting linear-time checking; it verifies the Metamath `set.mm` library in under 200 ms. The self-verification is **stated as intent, not achievement**. The arXiv abstract: *"Ultimately, we intend to use it to verify the correctness of the implementation of the verifier down to binary executable, so it can be used as a root of trust for more complex proof systems."* The repository confirms the same split: `mm0-c` (the bare-bones verifier), `x86.mm0`/`x86.mm1` (x86 formalization), and `peano.mm0`/`peano.mm1` exist; but `verifier.mm0` is described as the project's **main goal theorem** — the statement of MM0-verifier implementation correctness — with `verifier.mm1`, its proof, marked as future work. **Do not report MM0 as self-verified.**

**(b) Tax paid.** Currently: the entire implementation. The design intent is to pay in *specification down to the machine* rather than in axiom deltas — the ambition is the sharpest in the strand, the delivery incomplete.

**(c) P1–P4.** P1 designed-for, not attained. No P2, no P3. Good P4 by construction: the goal theorem is written down as a named unproved obligation — an unusually legible confession.

**(d) Citations — VERIFIED.** M. Carneiro, "Metamath Zero: The Cartesian Theorem Prover," arXiv:1910.10703 (v3, March 2020); published as "Metamath Zero: Designing a Theorem Prover Prover," ITP 2020, LNCS 12166. Repository: github.com/digama0/mm0.

## 6. MetaCoq / Coq-in-Coq (Sozeau et al., POPL 2020 + JAR 2020)

**(a) What was verified — precisely.** The first type checker for the kernel of Coq (**excluding the module system and template polymorphism**), proven correct in Coq against a formal specification of PCUIC, plus a verified erasure/extraction function. The claim is *implementation* correctness relative to an *axiomatized* metatheory.

**(b) Tax paid — the confessed assumptions, verbatim.**

> "our formalisation assumes strong normalisation of the reduction of CIC; and this even serves as the basis for the implementation of algorithmic conversion, which is defined by recursion on the strong normalisation assumption. We also assume other properties of the metatheory: subject reduction, validity, strengthening, guard condition for inductive types and fixpoints and proof-irrelevance. This is the only Achilles heel of our formalisation, the correctness of the specification of the metatheory: If the metatheory fulfills the well-known, assumed properties, then there is no error in the implementation."

The guard/positivity conditions are literally axioms in the development (`Axiom fix_guard`, `Axiom ind_guard`, plus stability of the fix-guard under reduction), treated as "syntactic oracles"; the authors bundle these with strong normalisation as "one axiom on the metatheory." The paper's own slogan for the trade: *"This paper proposes to switch from a trusted code base to a trusted theory base paradigm!"* — TCB → TTB. Consistency of Coq is explicitly disclaimed on Gödel grounds.

**(c) P1–P4.** Strong P1 modulo a large, precisely enumerated assumption set. No P2, no P3. **Best-in-class P4 for explicitness**: the residue is not prose but *axiom declarations in the artifact* — machine-locatable confession. This is the nearest precedent for making the confessed residue a first-class object rather than a caveat.

**(d) Citations — VERIFIED.** M. Sozeau, S. Boulier, Y. Forster, N. Tabareau, T. Winterhalter, "Coq Coq Correct! Verification of Type Checking and Erasure for Coq, in Coq," *PACMPL* 4(POPL), Art. 8, Jan. 2020, DOI 10.1145/3371076. Umbrella paper: M. Sozeau, A. Anand, S. Boulier, C. Cohen, Y. Forster, F. Kunze, G. Malecha, N. Tabareau, T. Winterhalter, "The MetaCoq Project," *JAR* 64(5):947–999, 2020, DOI 10.1007/s10817-019-09540-0.

## 7. seL4 (Klein et al., SOSP 2009) — the contrast case

**(a) What was verified.** Machine-checked functional correctness of a general-purpose OS microkernel — 8,700 lines of C and ~600 lines of assembler — by refinement from an abstract specification down to the C implementation, in Isabelle/HOL. The first such proof for a complete OS kernel.

**(b) Tax paid.** Stated in the abstract: the proof "assume[s] correctness of compiler, assembly code, and hardware." The refinement stops at the C source level; GCC is assumed to compile correctly; hand-written assembly and hardware behaviour are assumed.

**(c) P1–P4.** **P1 is absent in the reflexive sense**: seL4 is verified *entirely from outside*, by Isabelle/HOL, a system seL4 neither contains, runs, nor evaluates. The verified artifact has no relationship to its own verification. No P2, no P3. P4 present as a clear prose assumption list. seL4 is the purest demonstration that "verified" and "self-evaluating" are orthogonal axes — it is the most operationally deployed system in this strand and the least reflexive.

**(d) Citation — VERIFIED.** G. Klein et al., "seL4: Formal Verification of an OS Kernel," SOSP 2009, pp. 207–220, DOI 10.1145/1629575.1629596 (assumption language quoted from the paper's abstract and §"Assumptions").

## 8. Optional lines — verified status

- **Lean4Lean** (M. Carneiro, arXiv:2403.14064, 2024) — a typechecker for Lean **written in Lean**, with correctness results for the typechecker; consistency of the metatheory is assumed, and overall proof-system soundness is not established. Complements external checkers (`lean4checker`, Trepplein, nanoda_lib) that re-check Lean's environment outside the elaborator — the de Bruijn criterion applied to a system that does not natively satisfy it. **VERIFIED.**
- **Pollack-inconsistency** (F. Wiedijk, *ENTCS*, 2012) — the residue *below* every result above: a system is Pollack-consistent only if it can correctly re-parse the formulas it prints. Many provers are not. Every soundness theorem in this strand concerns the kernel; the human reads the *printer*. **VERIFIED.**
- **F\* self-certification** — **UNVERIFIED**; not confirmed within this search.

## Strand Summary

The tower plus the confessed core is buildable, and it has been built. Milawa is the existence proof: a trivially-checkable Level 1 admits eleven successively stronger provers, each admitted by the one below, and the whole stack was carried down to verified x86 through Jitawa — admission-by-replay, working, at scale. Harrison established the honest form of the confession (two named axiom deltas, plus an external cross-check), and MetaCoq made the residue machine-locatable by writing it as literal axioms and naming the trade: trusted code base → trusted theory base. Metamath Zero shows the ambition's frontier and its cost — the goal theorem `verifier.mm0` is stated; `verifier.mm1` is not yet proved. seL4 is the control: maximal deployment, zero reflexivity, verified wholly from outside. But every one is a museum piece. Each was proved once, over person-years, and then frozen; none is live (no P3), and not one records its own verification acts as attributable, sealed events inside the system being verified (no P2) — the proof files are artifacts, not attributable acts by identified parties in an append-only log. The strand supplies Custos with its architecture (the tower), its honesty standard (the enumerated axiom delta), and its precise negative space: nobody has yet made the act of verifying part of the record that is verified.



---

# Part IV — Law, governance, accounting: confession before computing


## Strand: Law, Governance, and Accounting — Grounding One's Own Authority

*Teleological history toward P1 (evaluates own foundation) · P2 (verification acts are attributable sealed records) · P3 (live/continuous) · P4 (unverifiable residue constitutionally confessed).*

## I. The problem named — Juvenal, *Satire VI* (c. 100–127 CE)

**(a) Move.** Names the regress: any enforcement apparatus is itself an object requiring enforcement. Originally a joke about locking up a wife, not political theory — the guards are corruptible *because they are inside the household they police*. That is our problem exactly: the verifier sits inside the system under verification.

**(b) Residue.** In the maxim, nowhere — stated as unresolvable, which is its rhetorical force. But the *text* puts its residue somewhere instructive. Modern editors bracket 6.346–348 as an interpolation; the lines duplicate material in the "O fragment," 34 lines discovered in 1899 by E. O. Winstedt in Bodleian MS Canonicianus Class. Lat. 41 (sigil O), now generally accepted as genuine. The O version is fuller and sharper: the guards are bought off, and the shared crime goes unmentioned. So the most-quoted form of the line naming the guard problem is the form editors judge spurious; the form they accept is the one nobody quotes. Philology could not verify its own foundation either — and invented the square bracket to **mark** the doubt inside the text rather than resolve or suppress it.

**(c) Properties.** The maxim: none — it is the problem statement P1–P4 must answer. The editorial apparatus around it: an early, notational **P4**.

**(d) Citation — VERIFIED.** Satire 6.346–348, bracketed in the transmitted text: *"[audio quid ueteres olim moneatis amici, / 'pone seram, cohibe.' sed quis custodiet ipsos / custodes? cauta est et ab illis incipit uxor.]"* O-fragment variant: *"'pone seram, cohibe'. sed quis custodiet ipsos / custodes, qui nunc lasciuae furta puellae / hac mercede silent? crimen commune tacetur."* (The Latin Library, Sat. 6; O-fragment provenance corroborated at Wikisource, Ramsay tr. Sourcing note: the Perseus/Ramsay edition rendered only through ~line 265 on fetch; Latin taken from The Latin Library and cross-checked.)

## II. The axiom confessed — Kelsen's *Grundnorm* (1934 / 1960)

**(a) Move.** Law's validity is a chain of authorizations. Kelsen follows it up and *stops honestly*: the terminal norm is not derived, it is **presupposed**. The Pure Theory does not claim to prove its own foundation; it declares the foundation an assumption and marks the objective validity of positive law as *conditional* on that assumption.

**(b) Residue.** **Presupposed** — parked in an explicitly labelled axiom slot at the apex of the hierarchy. This is the ancestor of a constitutional confession: the residue is named, typed, and located, not smuggled.

**(c) Properties.** **P4 in embryo** — the first rigorous confession of an unverifiable ground. **P1 partial**: the system evaluates norms against the foundation but never the foundation itself. No P2 (no attributable record of the validating act), no P3 (a static theoretical posture, not a running process).

**(d) Citation — VERIFIED.** *Reine Rechtslehre*, 1st ed. 1934 (tr. 2002), 2nd ed. 1960 (tr. 1967). "At some stage, in every legal system, we get to an authorizing norm that has not been authorized by any other legal norm, and thus it has to be presupposed to be legally valid"; the Pure Theory "presents the objective validity of positive law only as conditional—namely conditioned by the presupposed basic norm." (SEP, *The Pure Theory of Law*.)

## III. The residue relocated to social fact — Hart's rule of recognition (1961)

**(a) Move.** Replaces the presupposed norm with an **observed practice**. The rule of recognition is not a further norm to be validated; it exists in the convergent behaviour of officials treating certain criteria as the tests of validity. Foundation moves from *assumed* to *empirically checkable* — but checkable sociologically, outside the legal system's own operations.

**(b) Residue.** **Located in social fact**, outside the deductive system. Hart's second gift: **open texture** — rules have a settled core and an indeterminate penumbra, so judgment can never be fully mechanized. That is a second, independent confession: not just the foundation but the *application* has an irreducibly non-computable remainder.

**(c) Properties.** **P4 strong** (two confessions: ungrounded ultimate rule + open texture). **P3 real** — the rule of recognition exists only while it is being practised; it is a *live* fact, dying the moment officials stop. **P1 partial**, **P2 absent**: the practice constituting the foundation leaves no attributable, tamper-evident record of itself. You cannot replay it.

**(d) Citation — VERIFIED (quote), page UNVERIFIED.** H.L.A. Hart, *The Concept of Law* (OUP 1961). The ultimate rule "can neither be valid nor invalid but is simply accepted as appropriate for use in this way"; there is "no rule providing criteria for the assessment of its own legal validity." Open texture developed in Ch. VII. Quote confirmed across independent scholarly sources (QMUL HRLR; Wikipedia, *Rule of recognition*); paginated original not seen, so the customary "p. 109" cite is **UNVERIFIED**.

## IV. The paradox formalized — Alf Ross, *Mind* (1969)

**(a) Move.** Ross states the self-amendment problem as a **formal contradiction**: an amendment clause used to amend itself yields a rule whose authorizing premise is inconsistent with its conclusion. His conclusion: self-amendment is logically impossible; what actually operates must be an invisible, immutable amendment clause standing behind the visible one.

**(b) Residue.** **Entrenched by fiat, invisibly** — an unamendable meta-clause posited to save consistency. Least honest placement in the strand: the residue is hidden rather than confessed.

**(c) Properties.** Sharpens P1 into a *proof obligation*: a system that rewrites its own validation rule must survive an apparent contradiction. Lacks P2, P3, P4 (the invisible clause is a repair, not a confession).

**(d) Citation — VERIFIED.** Alf Ross, "On Self-Reference and a Puzzle in Constitutional Law," *Mind* LXXVIII/309 (Jan 1969), pp. 1–24. (Oxford Academic.)

## V. The requirement specified, then retracted — Elster (1979 / 2000)

**(a) Move.** *Ulysses and the Sirens* (1979) turns precommitment into design. A rational agent expects his future self to be unreliable, so he binds that self in advance: the crew's ears stopped, the captain lashed to the mast. Constitutions are the political mast — an earlier self engineering constraints against a later one. No one before Elster stated self-binding as architecture this precisely.

**(b) Residue — retracted by its own author.** *Ulysses Unbound* (2000) takes the analogy apart in three moves. Societies are not selves: an assembly that binds itself mostly binds others — successors, minorities, the unborn. Founding moments are not sober: constitutions are written in passion and partial interest, so the drunk self designs the mast. And fatally, the enforcement regress: the mast has no anchor. Every device by which a polity precommits is operated by the polity it restrains. The promisor enforces the promise, and can unmake it.

**(c) Properties.** **P4 strong, and unique in kind.** Alone in this lineage, Elster specified the constructive requirement precisely and then proved it unmeetable with the materials he had. The residue is confessed by the author against his own foundation — the most complete retraction in the strand. **P1–P3 absent**, all for one reason: Elster's substrate was solipsistic — no medium outside the promisor could hold a commitment, so every mast was gripped by the hand it was built to bind. The requirement stands, waiting on its material: the mast made of arithmetic, the crew made of anyone.

**(d) Citation — VERIFIED (works and dates); the retraction is paraphrased, not quoted.** Jon Elster, *Ulysses and the Sirens: Studies in Rationality and Irrationality* (Cambridge University Press, 1979; rev. ed. 1984; precursor article in *Social Science Information* 16, 1977); Jon Elster, *Ulysses Unbound: Studies in Rationality, Precommitment, and Constraints* (Cambridge University Press, 2000), DOI 10.1017/CBO9780511625008, incl. ch. 2, "Ulysses Unbound: Constitutions as Constraints." (Crossref; CUP.)

## VI. Law as self-producing — autopoietic legal theory (Luhmann; Teubner 1993)

**(a) Move.** Recasts the regress as a *feature*. Law is an operationally closed, self-referential system: it produces its own elements (legal communications) using only its own binary code, and validates them by its own recursive network. The Juvenal regress is not a bug to be terminated by an axiom — it is what a functioning legal order *is*. Foundation is not a point but a self-sustaining loop.

**(b) Residue.** **Dissolved into circularity, then re-described.** Closure is the answer; the "ground" is the ongoing self-reproduction. What remains unverifiable is the system's *environment* — the closure is exactly a confession that the outside cannot be internally represented.

**(c) Properties.** **P1 strongest in this strand before computing** (the system's operations are its own foundation, continuously) and **P3 constitutive** (an autopoietic system that stops operating ceases to exist). **No P2** — the communications are self-referential but not cryptographically attributable; the loop cannot prove *which* operations composed it. **P4 structural rather than declared.**

**(d) Citation — VERIFIED.** Gunther Teubner, *Law as an Autopoietic System* (Blackwell, 1993), developing Maturana, von Foerster and Niklas Luhmann; "law's autonomy in the self-reproduction of a communication network." (Springer chapter; PhilPapers.)

## VII. The paradox dissolved by practice — Suber, *The Paradox of Self-Amendment* (1990)

**(a) Move.** Book-length answer to Ross. Suber **concedes the logic** — self-amendment does reduce to formal contradiction under the "inference model" — and then denies logic is the arbiter. Under the **acceptance model**, the changed rule is valid because it is accepted and practised, contradiction notwithstanding. Empirically: legal systems amend their own foundations constantly and survive.

**(b) Residue.** **Located in acceptance**, i.e. Hart's social fact made explicitly load-bearing, and made *retroactive* — authority is acquired *ex post facto* from success.

**(c) Properties.** **P1 + P3 + P4.** This is the strand's high-water mark for self-amendment without cryptography: a foundation that rewrites itself, continuously, with the residue named as acceptance. **P2 absent and conspicuously so** — "accepted by whom, when, in what sequence?" has no verifiable answer; acceptance is precisely the quantity a signed, ordered log would make attributable.

**(d) Citation — VERIFIED.** Peter Suber, *The Paradox of Self-Amendment: A Study of Logic, Law, Omnipotence, and Change* (Peter Lang, 1990; ISBN 0-8204-1212-0), full text online. §6: "The acceptance model locates the authority of all law, including newly changed law, ultimately in the acceptance of the people governed by it, and in the practice and usage of the officials of the system"; a contradiction in the process "would not invalidate the result if the result is accepted by the people and officials, for acceptance and not formal logic is the final arbiter of legality"; "the power acquires authority *ex post facto* from success." (legacy.earlham.edu/~peters/writing/psa/sec06.htm)

## VIII. The core entrenched and adjudicated — Roznai (OUP 2017)

**(a) Move.** Modern doctrine: an amendment can be *unconstitutional*. Amendment power is a delegated, limited power (secondary constituent power), not sovereign; some cores are unamendable, explicitly or implicitly; and courts substantively review amendments against the constitution they alter. A constitution adjudicating changes to itself, in production, at scale.

**(b) Residue.** **Entrenched as unamendable** — the residue becomes a protected region of the constitution, plus a court whose own authority to strike amendments is itself contested (the regress reappears one level up, and Roznai's Part III is about enforcing it anyway).

**(c) Properties.** **P1 explicit and institutional** (self-evaluation of changes to self), **P3 live**, **P4 partial** (unamendability is a declared boundary of what the system will not re-derive). **P2 absent**: judgments are records, but not cryptographically attributable, ordered, replayable artifacts.

**(d) Citation — VERIFIED.** Yaniv Roznai, *Unconstitutional Constitutional Amendments: The Limits of Amendment Powers* (OUP 2017, ISBN 9780198768791); Part I comparative unamendability, Part II theory, Part III enforcement. (OUP.)

## IX. Accounting — reconciliation, externalized attestation, signed third book

**IX.a Double-entry (Pacioli, 1494).** *Move:* every event recorded twice with an arithmetic constraint (debits = credits); errors become **detectable by internal consistency check** rather than by trust. This is the first conformance suite: a self-applying invariant run continuously over the system's own records. *Residue:* consistency ≠ truth — books can balance and lie; residue silently ignored. *Properties:* P1 weak (invariants over its own records), **P3 strong** (run every period, forever). No P2 (entries are unsigned, the ledger is forgeable, ordering unattested), no P4. *Citation — VERIFIED:* Luca Pacioli, *Summa de Arithmetica* (Venice: Paganino de Paganini, 1494) — first printed exposition of double-entry, ~27pp within a 615pp encyclopedia, codifying the Venetian method. (ICAEW; Wikipedia.)

**IX.b The external auditor.** *Move:* since a balanced book proves nothing about honesty, institutionalize a verifier **structurally outside** the entity — with independence enforced by statute (no contemporaneous non-audit services, partner rotation, audit-committee pre-approval, an oversight board). *Residue:* **delegated to an outside auditor, and the auditor's own independence is confessed as the thing that cannot be internally verified** — hence "independence in appearance" as a separate, non-substitutable requirement. This is the strand's most explicit statement that *some verification must be exported*. *Properties:* P4 strong (the confession is codified as law), P3 strong (annual cycle). P1 **negative by design** — the whole point is that the entity may *not* verify itself. No P2. *Citation — VERIFIED:* Sarbanes-Oxley Act of 2002, Pub. L. 107-204, Title II (Auditor Independence), establishing the PCAOB. (congress.gov H.R.3763; PCAOB text.)

**IX.c Triple-entry (Grigg, 2005).** *Move:* the **digitally signed receipt**, held identically by both parties and the issuer, becomes the record. Signature-signature-signature: the evidentiary weight moves from institutional attestation to cryptography. *Residue:* **shrunk to the shared repository's ordering** — who holds it, whether it forked. *Properties:* **first genuine P2 in this strand** — the verifying act is itself a signed, attributable artifact, superior evidence to the ledger entry. P3 (per-transaction, continuous). P1 not addressed (receipts record transactions, not amendments to the accounting rules). *Citation — VERIFIED:* Ian Grigg, "Triple Entry Accounting," Systemics, Inc., 2005: "The Receipt is the Transaction"; "all three parties hold the same dominating record for each event"; "In evidentiary terms, the signed receipt is more powerful than double entry records due to the technical qualities of its signature." (iang.org/papers/triple_entry.html)

## X. Monitoring made internal, layered, and live — Ostrom (1990 / 1992)

**(a) Move.** Empirically: enduring commons do **not** solve Juvenal by importing an external Leviathan. They use **monitors who are themselves appropriators or accountable to the appropriators**, graduated sanctions, and **nested enterprises** — monitoring, enforcement, conflict resolution and governance organized in multiple layers. Verification is endogenous, continuous, and recursive across levels. The laboratory then confirmed the field. In "Covenants with and without a Sword" (1992), Ostrom, Walker and Gardner ran commons dilemmas under controlled conditions. Communication alone improves cooperation but does not hold it. Communication plus endogenous sanctioning — participants paying to sanction one another, no external enforcer anywhere in the design — sustains it. The title is this strand's vocabulary exactly, and the finding is its experimental case: the sword works precisely when it is held inside.

**(b) Residue.** **Distributed across levels rather than terminated** — each layer is watched by the layer it constitutes. The regress becomes a finite, working architecture instead of a paradox.

**(c) Properties.** **P1 + P3 exemplary** (self-monitoring, permanently on), and the layering is the institutional shape our nested-enterprise design inherits. **P2 absent** (monitoring reports are testimony, not receipts). P4 implicit. Read against Elster, the 1992 result is the endogenous enforcement his regress says should not stand. She showed the sword works when held inside; he showed why it should not. A committed medium outside any single promisor dissolves the disagreement — her sword, his mast, one substrate.

**(d) Citation — VERIFIED.** Elinor Ostrom, *Governing the Commons* (CUP 1990), design principles: monitoring — "monitors ... are accountable to the appropriators, or are the appropriators"; nested enterprises — "appropriation, provision, monitoring, enforcement, conflict resolution, and governance activities are organized in multiple layers of nested enterprises." (P2P Foundation; Patterns of Commoning.) Elinor Ostrom, James Walker, Roy Gardner, "Covenants with and without a Sword: Self-Governance Is Possible," *American Political Science Review* 86 (June 1992): 404–417, DOI 10.2307/1964229. VERIFIED (Crossref; bibliographic data — the experimental findings are paraphrased, not quoted).

## XI. The same seam reached from proof theory — Nash (c. 1998)

**(a) Move.** "Hierarchical Introspective Logics," an unpublished talk from the late 1990s posted on Nash's Princeton homepage, arrives at this strand's seam independently and from the other side. The overview concept: a logical system "cannot effectively state its own consistency," but one system can "state the formal consistency of another system." So build a tower in which each level overviews and affirms the consistency of the levels below it, none its own — self-binding, never self-judged, done as proof theory. Then comes the commitment-grounding maneuver, performed before any commitment medium existed. Turing's progressions lose invariance because ideal ordinals outrun every naming scheme: any language yields only enumerably many definitions against an unbounded supply of ordinals. Nash's answer indexes the levels not by ordinals but by committed definitions of ordinals — an ORDDEF predicate admits a definition only when the ground level can prove it names a unique ordinal. The level is grounded in the name actually written down, not in the ideal it points at.

**(b) Residue — confessed in the telling.** An unfinished talk, not a theorem set. By his own account the axioms and the choice of underlying set theory are "not fully crystallized"; none of it was published; he names "a great fear of possible error" as the reason for working slowly and alone. Beneath the personal confession sits the structural one: the definitions that index the tower are committed to nothing but the talk itself — a naming discipline with no medium to hold the names.

**(c) Properties.** He enters P3-shaped where Elster is P4-shaped. The hierarchy is built to be renewed: when definable ordinals run out, new axioms of infinity revive the extension. Evaluation is designed to keep going, though idealized like Turing's, never live. P1 gestured (each level evaluates the foundations below it, never its own). No P2: no actor, no record, no seal. P4 honest but personal — an author's confession, not a constitutional article.

**(d) Citation — VERIFIED (text read).** John F. Nash, Jr., "Hierarchical Introspective Logics," unpublished talk text, files dated 1998, hosted on Nash's Princeton mathematics homepage (web.math.princeton.edu/jfnj, Various_Etc./Logic/talk.CMU/). Quotes verbatim from the posted text; venue and exact date inferred from file names and timestamps only, and to that extent UNVERIFIED.

## XII. On-chain constitutionalism — Tezos (2014/2018) and the DAO fork (2016)

**XII.a Tezos — P1+P2+P3 in embryo.** *Move:* Ross's paradox implemented. The seed protocol "specifies a procedure for stakeholders to approve amendments to the protocol, **including amendments to the amendment procedure itself**" — Suber's acceptance model mechanized, with acceptance rendered as recorded, signed, ordered on-chain votes and activation performed by the protocol. Athens, the first amendment, was proposed Feb 2019 and **autonomously activated** May 2019 on a mainnet live since 17 Sept 2018. *Residue:* stakeholder distribution, off-chain proposal authorship, and chain-fork identity — largely unconfessed. *Properties:* **P1 + P2 + P3 together, for the first time in this history.** **P4 missing** — no constitutional statement of what the protocol cannot verify about itself. *Citation — VERIFIED:* L.M Goodman, "Tezos — a self-amending crypto-ledger," white paper, 2 Sept 2014 (position paper 3 Aug 2014). (tezos.com/whitepaper.pdf; amendment history at docs.tezos.com.)

**XII.b The DAO fork — the failure case.** *Move:* after the 17 June 2016 reentrancy exploit drained ~3.6M ETH, the foundation was amended by an **irregular state change** at block 1,920,000 on 20 July 2016 — outside any governed amendment process, ratified by miner adoption and non-binding off-chain sentiment, producing a permanent schism (Ethereum Classic, "code is law"). *Residue:* **silently ignored, then made visible as a chain split** — the unconfessed residue "this log is unforked" materialized as two logs. *Properties:* P2 partially (the fork block is recorded) but the *decision* was not an attributable act inside the system. **Absence of P1 and P4 is the causal story of the schism** — this is our sharpest argument that P4 must be constitutional, not optional. *Citation — VERIFIED:* Ethereum Foundation, "Hard Fork Completed," 20 July 2016; Ethereum Classic blog, 2016-07-20.

**XII.c DAO constitutionalism literature — VERIFIED (thin).** An emerging body frames DAO governance constitutionally, contrasting "code is law" with "code is constitution" — e.g. "Building the Foundation: A Constitutional Framework for Decentralised Autonomous Organisations," *JBBA*. Treat as early and uneven; no work found that supplies P2 and P4 jointly.

## Strand summary

Law solved liveness and confession centuries before computing. Kelsen was the first to write the axiom down instead of hiding it; Hart moved the residue into social fact and added open texture as a second, permanent confession; Ross proved self-amendment contradictory and Suber answered that acceptance, not logic, is the arbiter — which is why constitutions rewrite their own foundations daily and survive. Autopoietic theory showed the regress is the operating principle, not the flaw; Ostrom showed monitors must be endogenous and nested; Roznai showed a constitution can adjudicate changes to itself in court. Elster specified precommitment as constitutional design and then, against his own earlier book, proved the regress that undoes it — the promise enforced by the promisor; Ostrom's laboratory answered with covenants sustained by a sword held inside; and Nash reached the identical seam from proof theory: levels that state one another's consistency and never their own, indexed by committed definitions with no medium yet to hold them. Accounting contributed the continuously-run invariant suite (double-entry), the honest export of what cannot be self-verified (auditor independence), and finally the signed receipt as a third book (Grigg). What none of them ever had is a log whose entries verify themselves: acceptance leaves no attributable trace, official practice cannot be replayed, and even Juvenal's line naming the problem sits bracketed in its own manuscript tradition — the residue marked, never closed. Tezos got P1+P2+P3 and dropped P4; the DAO fork shows what the dropped confession costs. That is precisely the gap the other strands supply, and precisely why Custos must confess in the constitution what it cannot verify in the log.


---

# Part V — Synthesis: the four strands meet

## V.1 The matrix

The whole history in one table. Grades follow the strand reports;
"—" means absent, "~" partial.

| Milestone | P1 self-eval | P2 sealed acts | P3 live | P4 confessed |
|---|---|---|---|---|
| Gödel / Tarski / Löb (1931–55) | bounded | — | — | residue named |
| Gentzen (1936) | — (paid outside) | — | — | priced exactly (ε₀) |
| Turing / Feferman (1939/62) | staged | — | idealized | confessed as axioms |
| Willard (2001) | literal | — | — | tax visible in price |
| Kelsen (1934/60) | ~ | — | — | presupposed, labelled |
| Hart (1961) | ~ | — | yes | double confession |
| Suber (1990) | yes | — | yes | located in acceptance |
| Roznai (2017) | institutional | — | yes | entrenched core |
| Pacioli (1494) | weak (invariant suite) | — | strong | — |
| External audit (SOX 2002) | forbidden by design | — | annual | codified in statute |
| Grigg triple-entry (2005) | — | first germ | per-txn | shrunk to ordering |
| Ostrom (1990) | yes | — | exemplary | implicit |
| Thompson (1984) | declared impossible | — | — | despair, no seat |
| Wheeler DDC (2005/09) | strong | — | one-shot | stated precondition |
| Bootstrappable builds | ~ | — | weak | quantified in bytes |
| Reproducible Builds | — | ~ | strong | folklore |
| TPM / IMA (2004) | ~ | ~ | strong | **inverted** |
| Certificate Transparency (2013) | ~ | strong | strong | in normative text |
| sigstore / SLSA | — | strongest | strong | engineering prose |
| Tezos (2014/18) | nominal | real | real | absent |
| DAO fork (2016) | — | ~ | — | came due as a schism |
| Milawa / Jitawa (2009/14) | strongest (tower) | — | — | skeptic's list |
| Harrison (2006) | ~ | — | — | axiom deltas |
| MetaCoq (2020) | strong | — | — | machine-locatable |
| Metamath Zero (2019–) | intended | — | — | goal-theorem posture |
| seL4 (2009) | none (external) | — | — | prose assumptions |
| **The Custos loop (2026)** | **covenant set over own substrate** | **runs sealed in the GEL** | **standing organ** | **constitutional Ω-row** |

Read down the columns and the diagnosis is uniform. P1 at strength
appears only in the prover strand (Milawa, MetaCoq) and in law
(Suber, Roznai) — never with P2. P2 at strength appears only in the
transparency-log line (CT, sigstore, Tezos, Grigg's germ) — never
with P1. P3 belongs to law, operations, and infrastructure — never
to the provers. P4 at full honesty is the rarest column of all:
Kelsen and Hart in law, Gentzen and Feferman in logic, Harrison and
MetaCoq in proof, Wheeler and RFC 6962 in systems — and in every
single case as prose, footnote, or axiom file, never as an article
of a living constitution with an organ attached.

## V.2 Why the four never met

Each strand parked the residue where its own community could hold
it: logic in the metatheory, proof in the axiom file, systems in
the vendor or the gossip protocol, law in social fact. Those are
four different *places*, and each community's instruments could
only reach its own. Law could not make acceptance replayable
because it had no logs whose entries verify themselves; the provers
could not make verification live because a proof is an artifact,
not an act; the transparency logs could not evaluate their own
validation layers because they had schemas but no theory of
themselves; logic had no actor at all. The missing common part was
always the same object: **an append-only, attributable,
self-certifying record of acts** — which is precisely what KERI
supplies, and why the four strands become composable only on top of
it. The verifier strand states the negative space in one sentence:
nobody has yet made the act of verifying part of the record that is
verified. That sentence is the specification the loop fills.

## V.3 The intersection, instantiated

How the loop realizes each property — with receipts, since the
claim is precisely that receipts are the medium:

**P1.** The twelve-row invariant table is the foundation's
constitution; the covenant set (C2–C10, O1–O4) is its executable
statement; conformance is a replayable computation, not a reading.
The loop's first full pass convicted model #1 (rows 5+8 red:
duplicity evidence machinery dead at the pin and at upstream HEAD),
and the same suite certified the cure with blast radius exactly the
convicted rows. Note the Tarski discipline holding throughout: the
loop evaluates *validity* — finite, geometric predicates over
committed bytes — never truth simpliciter. The geometricity lint is
how the loop stays on the definable side of Tarski's line.

**P2.** The verification acts are sealed inside the discipline they
verify: the upstream filing was executed under a standing
authorization (SA-2), warranted by an attributable ruling, and
sealed into the polity's registry KEL (binding
`outward-act-keripy-1569`, checkpoint at sequence number 47);
conformance runs are content-addressed computations whose identity
is the hash of code plus inputs. This is Grigg's receipt and CT's
log grown to full generality: the receipt now covers *the act of
judging*, not only the act of transacting.

**P3.** The suite is a standing organ: it runs against any candidate
substrate tree, which turns a substrate upgrade into a governed
amendment admitted by replay (the kernel→engine bridge's
admission-by-replay socket, now powered — Milawa's tower made
operational and continuous). The February regression that nobody's
process caught for five months is the counterfactual: a polity
running this organ catches it at the merge gate.

**P4.** Row 11 of the invariant table — no log establishes its own
unforkedness; only external observation supplies it — is
constitutional text, paired with row 12 (the system may always be
applied to itself) so that reflexivity never becomes
self-absolution. The form honors Löb exactly: the confession is an
axiom and an attestation regime (witness receipts, watcher
observation), never a derived soundness theorem. And the
Turing–Feferman tax — the choice of *which* confession to make
requires a judgment from outside the formalism — is not evaded but
*put on the record*: in Custos the choice is a warranted, sealed,
attributable ruling. The outside judgment still exists; it now has
a name, a timestamp, and a signature.

### V.3.1 The constituted chooser

One inheritance deserves its own section, because it is the place
where the loop answers a sixty-year-old relocation problem rather
than merely composing known parts.

Turing's ordinal logics were the first attempt to *mechanize*
Gödel's tax: if the system cannot prove its own consistency, let it
confess Cons(T) as a new axiom, then confess the consistency of the
result, and iterate transfinitely. The completeness results (Turing
1939 for Π⁰₁; Feferman 1962 for all arithmetic sentences) say the
ladder reaches every truth. The caveat says the price: recognizing
*which path* through the ordinal notations reaches a given truth is
exactly as hard as recognizing the truth itself — and Turing showed
the path choice is not cosmetic, since different notations for the
same ordinal yield different theorem sets. The oracle is not
eliminated; it is relocated into the choice. The progression needs
a chooser, and the chooser is not in the formalism.

Every strand hit its own version of this. DDC needs someone to pick
the diverse compiler. Certificate Transparency's gossip needs
someone to decide which tree heads to compare, and with whom. The
external auditor must be appointed, and auditor independence is the
confession that the appointment itself cannot be self-certified.
Hart's rule of recognition *is* the chooser — dissolved into
unattributable official practice. Suber's acceptance model is a
chooser with no record: "accepted by whom, when, in what order?"
has no answer. Sixty years of mechanization attempts, in four
separate literatures, all terminating at the same unmechanizable
act of judgment — usually treated as an embarrassment, smuggled
into an appendix, or dissolved into sociology.

The loop's move is to stop trying to eliminate the chooser and
instead **constitute** it. The choice of which confession to make —
which invariants sit in the table, which substrate is seated, which
finding warrants an outward act — is made by an officer of the
polity under a scoped warrant, and the act of choosing is sealed
into the same log the choice governs. Feferman's oracle becomes an
officer: named seat, scoped authority, attributable signature,
replayable record, appealable ruling. Löb constrains the *form* of
the confession (attestation, never derived theorem); Turing and
Feferman constrain its *provenance* (chosen, never computed); the
sealed ruling satisfies both at once — it is an attestation whose
chooser is on the record.

Note precisely what this purchases and what it does not. It does
**not** make the judgment sound: sealing a ruling cannot make it
correct, and no such claim is made — the tax is not evaded; the
invoice now has a payer of record. What it purchases is that a
wrong confession changes *category*: from silent foundational flaw
to attributable act — citable, contestable, supersedable, and
subject to the same duplicity discipline as every other act.
Detection suffices at the meta-level exactly as it does at the
key-event level: you cannot prevent a bad ruling; you can make it
impossible to deny having made it.

Two corollaries. First, the progression's path — the sequence of
sealed confessions — is nothing other than the polity's
constitutional history: the governance log is an ordinal notation
written as a record, and Turing's non-invariance (different paths,
different theories) stops being a defect and becomes the honest
description of *plurality*: two polities that chose different
confession paths differ by a diffable, citable record, and their
cross-recognition is a comparison of committed paths rather than an
article of faith. Second, the common law has had this structure all
along: a precedent system is a Turing progression whose extensions
are attributed to named judges and preserved by reporters — what
the common law lacked was the self-certifying log, and what the
progressions lacked was the reporter. The loop is the two halves
joined.

And the regress does not terminate — it nests, Ostrom-fashion: the
officer's rulings are watched by organs those rulings constitute,
and the choice of the twelve rows was itself such a ruling,
amendable by the same sealed process. The ladder has no top. It has
a record.

## V.4 The inheritance ledger

What the loop takes from each ancestor, by name:

- **Gentzen:** itemize the price; never borrow silently. Ordinal
  analysis becomes the coverage confession — say exactly what the
  suite does not cover.
- **Turing/Feferman:** growth by confession — and the honest
  caveat that choosing the confession is itself a judgment, which
  Custos answers by sealing the judgment.
- **Löb:** the constitutional form of the confession clause —
  attestation, never reflection theorem.
- **Willard:** self-verification is a trade. Know what you sold.
- **Kelsen/Hart:** write the axiom down; locate the residue; and
  keep open texture in view — findings have a penumbra, which is
  why the codomain includes INSUFFICIENT, not just VALID/INVALID.
- **Suber:** acceptance is the arbiter — mechanized here as sealed
  enactment, answering his model's conspicuous gap ("accepted by
  whom, when, in what sequence?" now has a cryptographic answer).
- **Roznai:** the unamendable core — Custos's frozen floor — plus
  substantive review of amendments, mechanized as conformance.
- **Pacioli:** the continuously-run invariant suite over one's own
  records. **External audit:** some verification must be exported,
  and the export itself must be governed. **Grigg:** the signed
  receipt as the atom of P2.
- **Ostrom:** monitors endogenous, accountable, and nested — the
  organ structure; watchers as constituted roles rather than
  volunteer gossip.
- **Thompson:** the attack model, permanently in scope.
  **Wheeler:** the diverse outside as a named precondition —
  reborn as witness/watcher plurality. **Bootstrappable builds:**
  shrink the seed and publish its size. **Reproducible builds:**
  fold determinism as the comparison substrate (row 3).
- **Certificate Transparency:** verification acts in append-only
  logs auditing the authorities — and the gossip clause, RFC
  6962's confessed residue, which Custos inherits and gives what
  CT never shipped: a constituted organ (the watcher role) instead
  of an expired Internet-Draft.
- **LCF/de Bruijn:** shrink the judge; keep verdicts replayable by
  a program a skeptic could write.
- **Milawa:** the tower — admission-by-replay — as the architecture
  of engine admission. **Harrison:** the two-system dodge stated
  with total honesty. **MetaCoq:** the residue as machine-locatable
  axioms — our Ω-row is exactly this, promoted from axiom file to
  constitution. **Metamath Zero:** the goal-theorem posture — name
  the unproved obligation in the artifact itself.
- **seL4:** the control case — verification and reflexivity are
  orthogonal; deployment does not require reflexivity, but
  governance of one's own foundation does.
- **Tezos:** P1+P2+P3 jointly is achievable in production — and
  P4's absence is not a detail but the difference between
  amendment-as-preference and amendment-as-finding. **The DAO
  fork:** what the unconfessed residue costs when it comes due.

## V.5 The residue ledger — what the loop does not achieve

Stated at Franzén grade, because this section is the document's own
row 11:

1. **No consistency proof of anything.** Gödel II is untouched. The
   loop verifies events and conformance of implementations to a
   declared theory; it proves nothing about the theory's own
   consistency, and never will from inside.
2. **Unforkedness is never self-established.** Row 11 stands. The
   watcher organ supplies external observation; the organ's own
   coverage is finite and confessable. CT's split-view lesson is
   permanent structure, not a solved problem.
3. **Coverage is partial and dated.** All-green means: no listed
   invariant violated by the tested fragment on the tested vectors
   at the tested commit. The fragment is single-signature,
   no-witness, non-delegated today. Growth is the program, not the
   possession.
4. **The instruments are fallible and under the same law.** Our own
   admissibility extraction once graded a dead code path CERTAIN by
   trusting a call site; the upstream filing needed a correction
   within the hour. Both errors are on the record with their cures
   — which is the design working, not failing. The suite, the
   covenant set, and this document are committed objects subject to
   the discipline they describe.
5. **The Pollack residue.** Humans read renderings, not bytes. The
   committed chart (CESR) is trusted at the commitment boundary;
   the printer/parser gap Wiedijk named sits below every judgment
   stratum claim here.
6. **Thompson's regress is inherited, not evaded.** The loop audits
   the judgment stratum. Below it: Python, an operating system,
   microcode. The bootstrappable-builds and DDC postures are the
   named future confessions for that floor; they are not yet
   articles.
7. **The deterrence premise is a wager, not a theorem.** Every
   accountability claim above runs through an equilibrium
   premise: that a controller facing likely detection and
   portable proof does not equivocate. The loop proves none of
   this. What the architecture contributes is narrower and
   real: punishment *coordination* is solved — duplicity proof
   is portable and non-repudiable, so every counterparty's
   response fires without a coordinator. Two quantities remain
   premises. **p** — the probability a deviation is observed at
   all: watchers are voluntary, replay is costly, and no
   rational stranger re-folds; both external review panels
   independently convicted this (a warranty economy resting on
   "a re-folding population that does not yet exist"). **V** —
   what a convicted deviator loses: a fresh identifier loses
   nothing. Elster names the regress (the promise enforced by
   the promisor); Ostrom 1992 shows the sword can be held
   inside; Certificate Transparency shows confession alone does
   not fund the sword — RFC 6962's gossip clause was confessed
   and the organ still died. So this entry carries a
   requirement, not only a confession: a regime leaning on
   deterrence must charter and fund its monitoring organ (the
   vLEI's QVI regime is the standing proof that charter-and-fee
   suffices, without bonds or slashing) or must confess p ≈ 0
   for its threat model. Unlike every ancestor here, this
   lineage can measure its own premise: each detection and each
   realized consequence is a sealed act, so p and V are
   time-series readable from the log, not constants asserted
   about it. Formalizing the equilibrium itself (monitoring
   topology, watcher sufficiency, pricing) is arena work
   outside this document; no equilibrium claim is made.

## V.6 The claim, and its falsifier

At honest grade, after the four sweeps above: **no prior system
holds P1, P2, P3, and P4 jointly** — finding-grade evaluation of
its own foundation, verification acts sealed attributably inside
the system verified, as a standing organ, with the unverifiable
residue as constitutional text. The nearest misses are Tezos
(P1 nominal, P4 absent), Certificate Transparency (P1 partial, P4
textual but organ-less), and Milawa (P1 maximal, P2/P3 absent).
The claim is falsified by exhibiting one system with all four; this
document is the standing invitation to refute it, and per this
workspace's own audit discipline the claim does not graduate to
public assertion until it has survived an adversarial
double-refutation pass, which is hereby queued.

What is *not* claimed: any weakening of Gödel, Tarski, or Löb; any
novelty in the mathematics or the jurisprudence, which are cited
throughout; any assertion that the loop's green table means the
foundation is sound. The claim is an engineering-and-constitutional
composition: the strands existed; the log that could carry all four
did not, until attributable, replayable key-event infrastructure
made the acts of a polity self-certifying — at which point the
composition became executable, and was executed.

## V.7 Closing

Juvenal asked who watches the watchmen and meant it as a joke with
no answer — and the manuscript tradition bracketed the very lines
that ask it, philology's square bracket being perhaps the oldest
notation for a doubt confessed in place rather than resolved. Twenty centuries of the four strands produced answers
that each held one corner: name the residue, price it, confess it
as axiom; shrink the seed, diversify it, log the authorities;
tower the admissions; locate the ground in practice and entrench
the core. The loop's answer is not cleverer than any of these — it
is their composition on a substrate that finally lets the corners
touch: *the watchmen watch the watchmen, on the record, under the
law they enforce, and the one thing no watchman can see is written
above the door.*
