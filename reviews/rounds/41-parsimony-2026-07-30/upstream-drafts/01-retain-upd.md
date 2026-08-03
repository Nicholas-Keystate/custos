# Draft 01 — retain `upd`

**Home:** reply on WebOfTrust/keripy discussion #1566 (the thread is live
and Sam is engaged, so this belongs there rather than in a new issue).
**Custos tracker:** #56. **Post first** — it is nearly free and it changes
what draft 02 has to accomplish.

---

One more thing from your answer that I'd like to push back on gently,
because it turns out to matter quite a bit for what I'm doing.

> We have discussed without disagreement of deprecating the `upd` event so
> only the `rip` and `bup` remain. This was because a blindable update can
> be unblinded by merely attaching the unblinded attribute block.

That reasoning is clearly right for credential state. Blinding is the
default posture there, disclosure is the exception, and a `bup` plus an
attached unblinded block reproduces everything `upd` does. Within that
frame `upd` really is redundant.

I think the polarity inverts for a public, indefinitely replayable log —
which is the shape of both use cases I mentioned, the governance work and
the anchoring of timestamps and merkle roots from other ecosystems. Those
are public by construction. Nobody is protecting the state; the whole
point is that anyone can recompute it years later from the log alone.

For that shape, `bup`-only costs something:

- **The event stops being self-contained.** Every consumer must always
  carry event plus attachment, so the blinding factor and its UUID become
  per-event overhead in the only case that occurs.
- **The state moves outside the bytes the seal covers directly.** It is
  still committed — `b` is the block's SAID — but a reader goes seal →
  event → `b` → block → `ts`, where `upd` gives seal → event → `ts`. For
  archival replay by third parties long after the fact, the shorter path
  is worth real money.
- **The correlation-resistance machinery is aimed at a threat this log
  doesn't have.** Deriving the UUID from the update sn and a salty nonce
  exists to stop correlation of credential state across disclosures.
  Governance events are *meant* to correlate — that correlation is the
  constitution.

There's also a point that bears on the answer you gave me. The most
useful thing in it was that the state string's vocabulary isn't limited
and `td` doesn't have to be an ACDC SAID — that reframed the problem for
me completely. `upd` is the form that makes that extensibility legible on
the wire. If only `bup` survives, the extension surface you just pointed
me at is reachable only through a disclosure step, which seems like it
undersells it.

So: is the deprecation firm, or is there room to keep `upd` as the
unblinded variant for registries that are public by construction? If the
concern is carrying two code paths, a lighter answer would be to document
that the unblinded block travels in the clear as the normal case for such
registries — but I think the event form is cleaner, because it puts the
state inside the bytes rather than beside them.

Happy to write this up properly as an issue if that's more useful than a
discussion reply.
