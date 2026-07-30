# Why a GEL and not a TEL

A fair question, asked by everyone who meets Custos knowing KERI:
you already have a log for things that aren't key events. It's
called a TEL. Governance events aren't key events. So why is
there a third log?

The short answer is that there isn't one. A GEL is a TEL. What's
new is not the log but the thing that reads it. The rest of this
note explains why the name exists anyway, where the design is
genuinely awkward, and the one small thing KERI could do that
would make a chunk of the awkwardness go away.

## What a TEL already lets you do

A TEL is a hash-chained sequence of transaction events, each
sealed into a KEL. The seal is what does the work: because key
events are nonrepudiably signed by their controller, a seal
pointing at a transaction event is a commitment to that event by
that controller. Everything downstream — attribution, ordering,
persistence across rotation — follows from the seal.

Critically, the seal doesn't care what it points at. The ACDC
specification says so directly:

> Any number of transaction event types can be constructed for
> different applications that may be securely attributed without
> complicating KEL semantics. The seals need no semantics beyond
> their secure attributability to the AID of the KEL controller.

Read that again, because it settles most of the question. KERI
does not think of a TEL as "the credential revocation log." It
thinks of a TEL as extensibility for KEL semantics — a way to
attach any application's state machine to an identifier without
touching key state. Credential issuance and revocation is the
first transaction event type anyone built. It was never meant to
be the last.

So governance events in a TEL isn't a workaround. It's the
invitation.

## Custos accepts the invitation

Custos takes it. Its own text says the GEL is

> a TEL-shaped log with governance semantics: its events are
> sealed into the anchoring KEL by the same discipline KERI's
> registry layer uses, and this standard introduces no new
> anchoring pattern.

No new seal kind, no new anchoring rule, no new wire pattern for
getting events into a KEL. Structurally, a GEL is a registry.

## Then what is actually new?

Not the log. The fold.

KERI has two folds already, though it doesn't use that word. A
Kever walks a KEL and accumulates current key state. A Tever
walks a TEL and accumulates current registry state. Both are
pure functions: same events in, same state out, for everybody.

The rules those folds run under are fixed by the protocol. A
Kever's transition rules are in the KERI spec. No key event
changes them. You can rotate keys, you can't amend what rotation
means.

Custos adds a third fold, the Gever, and this one is different in
exactly one way: its transition rules are committed data living
in the log it reads. A domain's law says how governance events
are to be interpreted, and a governance event can amend that law.
The rules move, and they move by being written into the same log
the fold is walking.

That is the whole novelty. It sounds circular and isn't, because
it's positional: law never applies to itself, only to its
successor. An amendment is judged under the law in force before
it. Everything after folds under the new text, everything before
stays computable under the old.

So the honest framing for a KERI audience is: **Custos does not
propose a new log type. It proposes a new fold, over a registry
whose transition rules are themselves in the registry.** The name
"GEL" is a label for "the registry that fold reads." Whether that
label earns its own three-letter acronym is a fair thing to argue
about, and reasonable people will land differently. It is not a
new mechanism.

## Where it gets awkward

Here's the part worth bringing to KERI's maintainers.

In principle a TEL holds any transaction event type. In practice
the set is closed and curated. Under KERI v1 it is six: registry
inception, registry rotation, issue, revoke, and the two
backer-signed variants. Under the ACDC v2 registry it is three —
`rip`, `bup`, `upd`. Each has a fixed list of permitted fields,
and the parser rejects extras by default. Put a governance field
in an issuance event and validation fails.

That's a reasonable thing for keripy to do — closed schemas catch
real bugs. But it means an application inventing a tenth
transaction event type, exactly as the ACDC spec invites, has
nowhere to put it. The extensibility is in the specification and
not in the code.

So Custos ended up offering two ways to write governance events,
and read both as compromises.

**Track one** uses the existing event types unchanged. A
governance act is an issuance whose SAID points at the actual
content, sitting off to the side. Any registry-capable consumer
parses the stream without error — and understands nothing.

**Track two** mints new event types for governance, which is
precisely what the ACDC spec says you may do. The events say what
they are. The cost is that no tooling has ever seen them, and
Custos additionally reserves a CESR genus for the family — a
reservation nobody upstream has recognized, which the document is
candid about, calling it "enacted, unrecognized."

## The ask, and the answer

That framing was worth taking to KERI's maintainers, so it was,
as a question rather than a defect report. Two things came back,
and the second was a correction.

**On an extension point: no.** There is no plan for a way to
register an application-defined transaction event type. You may
define your own — "the seals in the associated KEL don't
differentiate what they are sealing so there could be any number
of TEL types" — but you carry the fork and you buy the adoption
yourself. That is the invitation restated with its price tag
attached, and the price is permanent rather than transitional.

**On track one: the description above understates the
substrate.** The v2 blindable registry's attribute block carries
a pair — a SAID and a **state string** — and the vocabulary of
that string is not constrained by anything. Nor does the SAID
have to address an ACDC; it can be the SAID or merkle root of
whatever you like. The maintainers already plan to use the pair
this way themselves, anchoring an IPEX Grant message rather than
a credential.

Which means the reuse option is not "parses everywhere, means
nothing anywhere." A governance act's *kind* can travel in the
state string and its *content* in the SAID, using the existing
event types unchanged, with no minted ilk and no genus
reservation at all. That is a third form, and on present evidence
it beats both tracks Custos wrote down.

It is not free. The unblinded variant of the update event is
slated for deprecation, so the state string ends up inside the
blinded attribute block: a consumer sees a digest until the
unblinded block is attached. The commitment is intact — the event
covers the block's SAID — but legibility becomes a disclosure act
rather than a property of the wire. For a public governance log
that is a small operational cost and, incidentally, a privacy
gain. It still has to be said out loud rather than assumed.

Worth saying plainly: this was an ecosystem gap on our reading,
and it turned out to be partly a reading gap on ours. The
architecture anticipated this case better than the two-track
design gave it credit for. What remains genuinely unbuilt is the
*fold*: the v2 registry has message builders and no state
machine, so a Gever would be the first fold over it. That is an
opportunity, not an obstacle, but it does mean nobody should
claim the substrate already does this.

## The question still outstanding

One thing didn't get asked, and it's the one Custos most needs an
answer to. The event-type question is about ilks — plain string
values in a `t` field, which any application may choose without
coordination. The genus question is about CESR code points, which
are a different kind of thing: the genus and version table is the
one table the CESR spec says all protocols must hold identically.

Reserving three characters nobody has agreed you hold, and then
emitting streams under them, is not the same act as choosing an
ilk, and Custos's document currently treats the two as though
they were. Whether an application coordinates a code point before
emitting under it, or reserves one and seeks recognition
afterward, is a process question with a steward on the other end
of it. That ask is still to be made.

## The bug that falls out of all this

An adversarial review of Custos 4.1 found something worth
knowing, and it's a direct consequence of how completely the
reduction to a TEL succeeds.

Under track one, a governance event is byte-identical in form to
an ordinary credential event. Same event type, same fields, same
anchoring. And Custos expects a governed domain to have both — it
separately describes domains that issue credentials and domains
that enact law, often the same domain.

The correction above makes this worse rather than better. If
governance events are ordinary registry events distinguished only
by the contents of a state string, a GEL is even less
distinguishable from a credential registry than the two-track
design assumed.

The specification commits a rule for what *order* to fold GEL
events in. It never commits a rule for *which events are GEL
events*. The founding law records which of the two tracks a
domain uses. It doesn't record which registry is the governance
registry.

So two correct implementations, holding identical bytes, can
disagree about what the law says. One folds every registry event
under the domain's identifier as governance, and the domain's
constitution acquires clauses nobody enacted. Another looks for
some designation, finds none, and picks a rule — the first
registry created, or the one named in founding law, or the one
whose identifier appears in a particular clause. Three plausible
guesses, three different constitutions, no error raised anywhere.

Custos elsewhere insists that two evaluations of the same inputs
must return byte-identical results. This breaks that, quietly.

The fix is small: require the founding law to name the governance
registry, at the same level of commitment it already gives to
track choice. That's a sentence, plus a test case for what
happens when the designation is missing.

And notice the shape of it. The bug exists *because* the GEL is
so thoroughly a TEL. If governance events were visibly different
from credential events, the question of which is which would
never arise. Custos got the reduction right and then didn't
finish the sentence.

## Bottom line

The design is sound. A panel of KERI-native reviewers went at it
specifically looking for constructs that don't earn their keep,
and most of the attacks failed — including, notably, the two
sharpest ones, which turned out to be arguments that would have
dissolved things KERI itself ships. What survived is
underspecification at seams, not architectural error.

If you take one thing to a KERI audience, take this: Custos isn't
proposing a third kind of log. It's proposing a third kind of
fold, and reusing your log for it, in exactly the way your own
ACDC specification says logs may be reused.

The friction isn't in the idea, and it turned out to be smaller
than this note first claimed. The extension point does have an
implementation — a state string with no fixed vocabulary and a
SAID that can address anything — and the honest reckoning is that
Custos designed around a limitation that was only partly there.
Two tracks were written where the substrate supports one. What
genuinely has no implementation behind it is the *fold*, and that
was always the part Custos was bringing.
