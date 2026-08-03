# Draft 03 — `xfr`

**Home:** new issue on WebOfTrust/keripy.
**Custos tracker:** #52. Lowest priority of the three and independent of
the other two. Post whenever; there is no sequencing constraint.

**Suggested title:** Tracking issue for the planned `xfr` (registry
control transfer) event

---

Opening this so the planned `xfr` event has somewhere to live — it came
up in discussion #1566 and I don't see a tracking issue for it.

From that thread:

> The second planned change is to add a transfer `xfr` event to expand the
> use cases of a registry to allow transfer of control over the registry
> from the issuer AID defined in the `rip` to a new controller issuer
> defined in the `xfr`. This event must doubly anchored.

Current state as of `8e67f2e6a`: `xfr` appears nowhere under `src/keri`
and is not in `Ilkage` (`kering.py:353-362`). So this is design, not code,
and this issue is just a place to hang it.

Questions, in the order they'd block an implementation:

1. **What is doubly anchored, exactly?** Presumably a seal in the outgoing
   controller's KEL and one in the incoming controller's KEL, so the
   transfer requires both parties' key state to commit. Is the ordering
   between them constrained, and what does a verifier do with a stream
   carrying only one of the two — escrow pending the second, or reject?
2. **Field set.** Does `xfr` carry the new controller AID directly, and
   does it also re-state the registry SAID (`rd`) and prior (`p`) the way
   `bup`/`upd` do?
3. **What happens to events on either side of it?** After a transfer, is
   the registry's history still verified against the *original* issuer's
   key state for events preceding the `xfr`, with the new controller's
   applying only after? I'd assume yes — it's the same positional
   discipline as delegation — but it's worth stating, because it decides
   whether a registry stays replayable across a transfer by someone who
   only holds the new controller's KEL.
4. **Interaction with the blinded state machinery.** Does a transfer
   invalidate outstanding blinds, or is the blinding factor derivation
   unaffected by a change of controller?

My interest is a governance log where control of the log may legitimately
move between parties — so (3) is the one that matters most to me. A
registry whose pre-transfer history stops verifying after a transfer would
be unusable for that, and a registry whose history keeps verifying is
close to exactly the primitive I'd otherwise have had to invent.

Happy to help implement once the design questions settle.
