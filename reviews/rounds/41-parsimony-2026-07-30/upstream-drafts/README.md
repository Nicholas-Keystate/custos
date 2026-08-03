# Upstream drafts — keripy

Drafts of messages to the KERI community, prepared here and posted from
there. Kept in this repository as provenance: what was asked, when, and
what the Custos-side interest was.

**These are keripy items, not Custos items.** Per `CONTRIBUTING.md`,
reviews of adjacent communities' work "travel as questions to them, never
as defect reports about them," so none of them is filed on this tracker as
a finding. The Custos-side *interest* in each is tracked, because that is
this project's own record:

| Draft | Custos tracker | Home | Status |
|---|---|---|---|
| `01-retain-upd.md` | #56 | reply on discussion #1566 | drafted |
| `02-v2-registry-processing.md` | #54 | new keripy issue | drafted |
| `03-xfr.md` | #52 | new keripy issue | drafted |

Sequencing matters and is not arbitrary:

1. **`01` first.** It is nearly free and it changes what `02` has to
   accomplish — if `upd` survives, the processing layer has a simpler
   public-state path to support.
2. **`02` should wait on Custos #55.** If a Custos enactment does not fit
   the `(td, ts)` form at all, the processing layer would be written
   against the wrong shape. `02` is drafted so it can be posted as a
   design question before that resolves, but the *implementation* offer
   in it should not be taken up until #55 reports.
3. **`03` is independent** and lowest priority.

Prior context, already posted: the original ask (discussion #1566,
2026-07-30) and the genus follow-up (2026-07-31). The answer and its
verification are in `../upstream-answer-1566.md`.
