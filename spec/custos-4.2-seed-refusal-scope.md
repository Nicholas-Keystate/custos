# Custos 4.2 seed — scoping the replay claim to what replays

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges finding #10 only. Executed under ruling R11 of the
> ruling record of 2026-07-30 (sha256 45a6d7208f0faca82946f2bfacb
> 04799994b5cf2c9afdef53f24def9d8cf8552). Offered to the drafting
> authority, which owns the wording.
>
> This seed carries a **coupled edit across three artifacts**.
> One of the three is ratified text and cannot move until 4.2; the
> other two must move with it and not before. The sequencing is
> stated in the coupling section and matters more than the wording.

---

## What this seed carries

One sentence of the abstract is rescoped. The abstract promises
that a stranger recomputes "the same Constitution, the same
findings, the same refusals, byte for byte"; the body classifies
refusal as not a finding, excludes it from the codomain, and
scopes the replay obligation to judgments — which a refusal
expressly is not.

The repair scopes the claim rather than committing a refusal
record, because committing one would resolve a ratified openness
question as a side effect of an abstract's wording.

## Repair — the abstract's replay claim

**Ratified span (4.1 L27–29).** Cited, not edited.

> The property this yields is replayable governance: any stranger
> holding the logs computes the same Constitution, the same
> findings, the same refusals, byte for byte.

**The supporting spans, all cited and none edited.** Section 7.5
(L1197–1201):

> Refusal is not a fifth finding value — it is the evaluator
> declining to answer an ill-posed question, recorded as an
> operational fact.

Section 7.1 (L967–972), which excludes operational conditions from
the codomain by construction. Section 2 (L424), which scopes the
replay obligation to "every judgment". And section 15's second
openness question (L2082–2086), which leaves open whether a
committed refusal record exists at all.

**The defect.** The abstract's sentence quantifies over three
things and only two of them are artifacts the document commits.
A refusal is expressly not a judgment, not a finding, and not a
codomain member; it is recorded as an operational fact, and
whether that record has a committed form is an open question the
document declines to answer. So "the same refusals, byte for byte"
promises byte-equality over an artifact that may not exist, in the
one sentence most readers will read.

**Replacement.**

> The property this yields is replayable governance: any stranger
> holding the logs computes the same Constitution and the same
> findings, byte for byte, and reaches the same refusals — a
> refusal being a decision derivable from the same committed
> triple rather than a committed artifact of its own.

**Ground.** The scoping is what the body already says. A refusal
is derivable: given the same bundle, the same law head and the
same position, the seam that is uncommitted is uncommitted for
every verifier, so every verifier refuses. That is a real and
strong property — it is determinism over the decision — and it is
not byte-equality over a record, because there may be no record.

The alternative repair is to commit a refusal-record form, which
would make the current sentence true as written. That resolves
section 15's second openness question, and resolving a ratified
openness question under the pressure of an abstract's phrasing is
the wrong order of operations. R11 declined it for the same reason
R5 declined to pin the carriage encoding: an openness clause that
can be closed by an adjacent repair's convenience is not an
openness clause.

## The coupling — three artifacts, one edit

The abstract is not a free surface. Two other artifacts quote or
verify it, and a change to L29 that moves alone breaks the
repository's own consistency check.

| Artifact | What it holds | When it moves |
|---|---|---|
| `spec/custos-4.1.md` L27–29 | the ratified sentence | never — the replacement lands in 4.2 |
| `README.md` L18–22 | a quoted excerpt of the abstract | when 4.2 ratifies, together with it |
| `tools/verify_kernel.py` check 3 | proves the README quotes rather than paraphrases | when its edition-of-record pointer advances to 4.2 |

**Check 3 is an excerpt discipline, not a byte-identity one.** Its
own comment reads "Trimming is lawful; paraphrase is not", and it
passes when the README's quoted span is a contiguous
whitespace-normalized substring of the edition's abstract. The
ruling record describes it as enforcing a byte-identical quote;
that is the stricter reading, and the repair should be written
against what the tool actually enforces.

The practical consequence is that the README has more freedom than
a byte-identity coupling would give it. It may quote a shorter
contiguous span and stay green. It may not paraphrase.

## Notes for the drafting authority

Some things surfaced in drafting that finding #10 did not name.

1. **The README can be brought into line before 4.2 ratifies, and
   this seed deliberately does not do it.** Because check 3 tests
   for a contiguous excerpt, the README could stop its quote before
   the refusals clause and stay green against 4.1 today — the
   quoted span would simply be a shorter prefix of the same
   ratified abstract. That would stop the repository's front door
   from republishing an over-scoped claim while 4.1 is in force.

   I have not done it, because the trim lands mid-sentence and the
   README's copy is the drafting authority's to shape, not a
   contributor's. It is available if wanted, and it is the only
   part of this repair that does not have to wait for succession.

2. **The replacement sentence is longer than the one it replaces,
   in the document's most-read paragraph.** The original earns its
   force from a triple cadence — Constitution, findings, refusals —
   and the repair breaks the cadence to add a qualifying clause.
   That is a real cost in the abstract specifically. An alternative
   shape drops refusals from the sentence entirely and states the
   refusal property in its own sentence afterward, which keeps the
   cadence and separates the two claims. I have not drafted it that
   way because it changes more of the paragraph, and the abstract
   is exactly where a minimal edit is worth preferring.

3. **"Reaches the same refusals" is doing quiet work and should be
   checked.** It claims determinism over the refusal decision, not
   over any record of it. That follows from the triple being closed
   and the seam being uncommitted for everyone — but it presumes
   that whether a seam is committed is itself derivable from the
   triple, which is true only if the requirement space is fully
   committed ex-ante. R2 now says it is. Before R2 the sentence
   would have been an overclaim.

4. **11a is now ruled, and it extends this repair to the
   composition grain.** This seed left #41 alone deliberately —
   the ruled text sits inside section 7.5's quoted amendment
   block, and 11a deserved its own ruling rather than arriving as
   an inference from an abstract's rescoping. Supplement 2 gives
   it one: if any component of a compound invocation refuses, the
   invocation refuses, with its grounds named per section 9's
   three-kind discipline; the refusal record cites the components
   already computed, which stand as ordinary findings at their own
   coordinates; and no product object ever contains a refused
   coordinate.

   The three statements now tell one story, which is worth stating
   here because each is read alone. The abstract says a refusal is
   a decision derivable from the committed triple, not a committed
   artifact. Section 7.5 says the evaluator refuses the
   invocation. 11a says what survives that refusal: a sibling's
   refusal un-happens nothing, so the findings already computed
   are facts at their coordinates, and the refusal answers about
   the seam rather than about the subject. A stranger replaying
   the same triple reaches the same refusal *and* the same
   surviving findings — which is the rescoped claim above, holding
   at the composition grain as well as at the single question.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Executed under | Ruling record 2026-07-30, sha256 `45a6d7208f0faca82946f2bfacb04799994b5cf2c9afdef53f24def9d8cf8552` — R11; extended to the composition grain by supplement 2, 11a, sha256 `7c5f6491976bd5fb12dcbab4c1520002f9f5a1cdf9bf94dc2f0964bb1aea2670` |
| Findings discharged | #10 (abstract's refusal claim vs the body) |
| Re-ruling | No |
| Coupled artifacts | `README.md`, `tools/verify_kernel.py` check 3 — move at 4.2 ratification, not before |
| Openness question left open | Section 15's second — whether a committed refusal record exists |
| Adjacent, not discharged | #41 — ruled 11a by supplement 2 and seeded separately; cited here in note 4 so the abstract, section 7.5 and the compound-product rule read as one story |
| Status | Unpinned draft; enters the 4.2 candidate by succession |
| Ratified bytes altered | None |
