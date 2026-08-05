# Custos 4.2 seed — the two-kind pin discipline

> DRAFT — repair seed for the 4.2 candidate. Unpinned until
> declared final. Enters the candidate by succession; the ratified
> Custos 4.1 bytes (sha256 ff8b9e7a6e95239dcd1111340f4969720e5268
> 57f1746f116b42b5b405b72b05) are untouched by this file.
> Discharges findings #23 and #4 only; every other span of section
> 3.2 stands as ratified. Executed under ruling R8 of the ruling
> record of 2026-07-30 (sha256 45a6d7208f0faca82946f2bfacb0479999
> 4b5cf2c9afdef53f24def9d8cf8552). Offered to the drafting
> authority, which owns the wording.

---

## What this seed carries

One reading rule of section 3.2 is replaced. It states a pin
discipline that describes one of the two pin forms this document
actually uses, and the form it omits is the one carrying the
document's most load-bearing commitments.

The replacement covers both forms and states the separation law
the ruling rests on: **the pin answers which bytes; normativity
answers which of those bytes bind.** Two rulings, never one.

## Repair — reading rule 2

**Ratified span (4.1 L548–557).** Cited, not edited.

> 2. Digest pins name exact bytes. Where this document pins a
>    digest, the pinned preimage is defined in the text beside the
>    pin, computed with the digest's own field carrying a
>    placeholder of the same length as the encoded digest — the
>    substrate's rule is length-parametric by derivation code, and
>    forty-four characters is this document's current profile, the
>    256-bit digest class — and verified by round trip before the
>    pin travels. A digest whose preimage is not stated is not a
>    pin; it is decoration, and this document contains none.

**The defect.** The rule describes a self-addressing digest — a
SAID, where the digest lives inside the bytes it commits to, so
its own field must be blanked to a same-length placeholder before
hashing. That is a real discipline and it is correctly stated.

It does not describe a whole-file sha256 pin, and the document
uses those everywhere. There is no digest field inside
`spec/custos-4.0-kernel-draft.md` to blank, no placeholder, and
nothing length-parametric. The preimage question for that form is
different in kind: not *which field is blanked* but *which extent
of the file is hashed*.

Two independent routes reached the same gap. Finding #4 reached it
by reading — either "where this document pins a digest" is
universal, and is falsified by section 16's whole-file pins, or it
is a term of art already scoped to SAID pins, in which case a
second pin form carries the document's heaviest commitments with
no stated discipline at all. Finding #23 reached it from
implementation: the 4.0 edition-of-record digest `9cefdc5d5842…`
is the digest of the whole file including a 12-line scaffolding
header that both editions rule was never ratified bytes. The
ratified extent hashes to `f529388df9fc…` instead.

The escape route does not save the rule. Even under the
term-of-art reading, the document still has a pin form with no
discipline — which is the same defect wearing a different hat.

**Replacement.**

> 2. Digest pins name exact bytes. This document uses two pin
>    forms, and each states its own preimage.
>
>    **Self-addressing pins.** Where the digest is a field of the
>    bytes it commits to, the pinned preimage is those bytes with
>    that field carrying a placeholder of the same length as the
>    encoded digest. The placeholder character is `#`. The
>    substrate's rule is length-parametric by derivation code, and
>    forty-four characters is this document's current profile, the
>    256-bit digest class.
>
>    **External whole-file pins.** Where the digest commits to a
>    separate artifact, the pinned preimage is **that file as
>    published**, in full, from its first octet to its last. No
>    extent within the file is excluded, and a ruling that some
>    span of the file is non-normative does not remove that span
>    from the preimage.
>
>    The two questions are separate and are answered separately:
>    the pin says which bytes; normativity says which of those
>    bytes bind. A span may be inside a committed preimage and
>    bind nothing, and this document contains such spans.
>
>    Every pin is verified by round trip before it travels. A
>    digest whose preimage is not stated is not a pin; it is
>    decoration, and this document contains none.

**Ground.** `9cefdc5d5842…` stands correct as anchored. It appears
in `SUCCESSION.md` L12, in this document at four sites, and is
checked by `tools/verify_kernel.py`; it is anchored in the
governance event log at sn 187/188. Re-pinning to the ratified
extent would ask the governance log to correct a digest it has
already anchored — a succession-grade act, not an errata edit —
for an end the separation law reaches with one clause.

The separation law is also truer to this standard's own thesis
than the alternative. The computation stands on its own: anyone
can fetch the file and recompute. What binds is a different
question, and this document already answers it elsewhere — the
appendix at L2348–2350 rules the scaffolding header "never
ratified bytes". Both statements are true at once, and they were
only ever in tension because one rule was being asked to make both
rulings.

The mild awkwardness — a committed preimage containing bytes ruled
non-normative — is stated in the replacement rather than hidden,
because a reader who notices it and finds no acknowledgement will
reasonably conclude the pin is wrong.

## Notes for the drafting authority

Some things surfaced in drafting that the findings did not name.

1. **The placeholder character is a commitment this seed makes and
   the ruling does not.** R8 says the placeholder character is to
   be named; it does not say which. This seed proposes `#` because
   it is outside the Base64URL alphabet CESR uses for digest
   encodings, so a placeholder can never be confused with a
   partially-written digest. Any character outside that alphabet
   works equally well and the choice is worth confirming rather
   than inheriting from a draft.

2. **The whole-file rule should be checked against every existing
   pin before the candidate ratifies, not after.** The rule as
   written is falsifiable by any pin in the corpus whose preimage
   is not the published file. I have not audited all of them. That
   audit belongs in the census tooling — a check that recomputes
   every whole-file pin against the published artifact — rather
   than in a reviewer's reading, and it would have caught #23
   mechanically.

3. **Finding #23's hardest case is gone for a different reason,
   and the candidate should not lean on this seed for it.** Under
   R4 the fixed walls are carried by this edition's own ratified
   text rather than imported by referent from the kernel. So the
   4.0 pin no longer determines what binds — only what the
   predecessor was. This seed makes the pin correct; R4 is what
   makes it a smaller question.

4. **"As published" needs a referent that survives the
   publication channel.** A file as published is unambiguous only
   where the published artifact is byte-stable — no trailing
   newline normalization, no line-ending translation, no transport
   re-encoding. The corpus is stored in git and served over HTTP,
   both of which can touch line endings. The candidate should say
   that the preimage is the artifact's octets as committed to the
   repository, or name whatever other canonical source it prefers,
   because "as published" alone leaves a checkout on a different
   platform able to compute a different digest in good faith.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.1, sha256 `ff8b9e7a6e95239dcd1111340f4969720e526857f1746f116b42b5b405b72b05` |
| Executed under | Ruling record 2026-07-30, sha256 `45a6d7208f0faca82946f2bfacb04799994b5cf2c9afdef53f24def9d8cf8552` — R8 |
| Findings discharged | #23 (the 4.0 pin's preimage), #4 (the pin discipline's scope) |
| Re-ruling | No |
| Anchored digests re-anchored | None — `9cefdc5d5842…` stands correct as anchored |
| Status | Unpinned draft; enters the 4.2 candidate by succession |
| Ratified bytes altered | None |
