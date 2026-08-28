# Issue #90: Finding (MINOR): the document's own carriage wraps at 80 columns, which makes a line number name a fragment and breaks pins in the drafting corpus
Filed by dhh1128 at 2026-08-26T23:27:09Z

I think there's a defect in how this document is carried rather than in what it says, so nothing ratified is falsified and the grade is MINOR. The ratified 4.2 bytes (sha256 68cc5c9b7164b33dffcf7b705a0d1301fe108c647d35638fec61d52d29b2775a) wrap at eighty columns, and §1.7 makes this section normative for this document itself (L412), so how the document carries itself is in scope for its own gate.

Two consequences, and the second is the one I didn't expect.

A line number names a sentence fragment. The required-payload rule for a pending finding occupies L1647-1658, which is twelve lines holding one rule, and any single line of it is a piece of a clause rather than a thing you can cite. That's most of why citing this document by line feels useless: the unit you can name and the unit that means something aren't the same unit.

The second one is worse and it's mechanical. Wrapping puts line breaks inside sha256 digests. Measured 2026-08-26 across `spec/`: 23 of 27 files contain a digest broken across a line boundary, 49 digests in all. Every one of them is a pin, in a seed header, naming the ratified edition that seed repairs. Reading rule 2 says a digest pin names exact bytes, and that "a digest whose preimage is not stated is not a pin; it is decoration" (L993-1010). A digest a reader can't select, grep, or paste without repairing it by hand is most of the way to decoration too. The ratified document itself is clean — 11 digests, all whole on one line — so the damage is confined to the drafting corpus, which is where the pins to ratified editions live.

For a repair I'd offer one line per block. A block is a paragraph, a list item, a table row, a fenced block. A line number then names a semantic unit, a changed block is a one-line diff, and a digest can't be broken because there's no wrap to break it. The document has roughly 370 blocks against 3,940 lines today.

The cost is that reflowing invalidates every existing line citation at once. Measured the same day, outside `.ignored/`: 606 explicitly-formed line citations across 47 files, 487 of the `L####` form and 119 of the `4.x:####` form. Citations into ratified 4.2 stay valid against ratified 4.2, which is never edited, so what breaks is their usefulness as pointers into the successor. That cost is paid once whenever it's paid, which argues for paying it in the same act as any other change to how the document is carried rather than twice.

It's also the one piece of this that's provable rather than argued. A reflow is correct when normalizing whitespace on both sides and diffing gives nothing, so a check can say whether an editorial pass changed any text, and nobody has to take anyone's word for it.

Relates to #75 (§1.7's comprehension gate, docketed as unrun — this is a third closure it doesn't test), #85, and #77.
