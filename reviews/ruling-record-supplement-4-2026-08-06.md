# Ruling record supplement 4 — errata against the ratified 4.2 edition (2026-08-06)

Supplements the record (`45a6d720…`) and supplements 1–3
(`e7ca1111…`, `7c5f6491…`, `79c7d7bd…`). Same law: prior bytes
stand; this document adds. Cited together always.

**Occasion.** The seed-PR reconciliation census (round 42-6,
`reviews/rounds/42-6-seed-reconciliation-2026-08-06/reconciliation-census.md`,
sha256 `8571fcdb…`) compared the twenty-two independently
drafted repair seeds against the ratified edition
(`spec/custos-4.2.md`, sha256 `68cc5c9b…`, anchored at KEL
sn 191/192). Zero seeds misread their rulings; two comparisons
convicted the RATIFIED TEXT. The ratifying authority ruled
(2026-08-06): errata published now, supplement grade. The
ratified bytes are immutable; these errata bind as drafting
obligations on the successor edition and as reading rules for
implementers of this one. The method convicts its instruments
impartially — this time, the edition itself.

---

## E4-1 (from census F-5) — the self-convicted payload bullet is
## pair-shaped; the edition's own doctrine is circuit-shaped

**The defect, at ratified coordinates.** §8.3's finding-payload
enumeration states (L1659–1660):

> A self-convicted finding SHALL carry the identifier of the
> canonical proof package for the contradictory pair.

§8.4 states the edition's ruled doctrine (L1824–1832): an
antinomy conviction's proof object "is a circuit, never merely a
pair … a pair cannot express the decisive case, cardinality
three or more, pairwise consistent, jointly unsatisfiable."

**Why this is a defect and not a tension:** the payload SHALL is
unsatisfiable for exactly the convictions R10 exists to admit. A
conforming evaluator that derives a cardinality-3 antinomy
cannot name "the contradictory pair" — there is none — and so
cannot discharge the SHALL. This is the unconstructible-payload
defect (R10's own finding class) reproduced at the payload site
by the assembly: the duplicity branch's pair vocabulary survived
in a bullet that must range over BOTH branches of
self-conviction. The antinomy-circuit seed
(`spec/custos-4.2-seed-antinomy-circuit.md`, merged) carried the
correct shape.

**The erratum (binding on the successor; reading rule now):**
the bullet is read as: *a self-convicted finding SHALL carry the
identifier of the canonical proof package for its kind — the
contradictory pair where the kind is duplicity; the
jointly-unsatisfiable circuit where the kind is antinomy* — per
§8.4's own object definitions. An implementer who satisfies
§8.4's circuit requirement satisfies the payload obligation; the
pair wording of the bullet confers no license to reject a
circuit-shaped payload.

## E4-2 (from census F-1) — canonical selection's empty subcode:
## "orders last" contradicts "lexicographic minimum"

**The defect, at ratified coordinates.** §8.3's canonical
selection (L1766–1779) commits the finding to cite "the
lexicographic minimum of (defeater-class rank, citation
identifier, subcode)" and then states "where the clause defines
none, the subcode is empty and orders last."

An empty value that orders LAST under a MINIMUM selection is a
contradiction at one boundary: when two defeats tie on class
rank and citation identifier and exactly one carries an empty
subcode, "minimum" selects the non-empty subcode while
"orders last" was written to say the empty one loses — the same
outcome — but when the empty-subcode defeat is the ONLY defeat
at the minimal (rank, identifier), the sentence pair gives no
consistent instruction: the tuple containing the empty subcode
IS the minimum, yet "orders last" reads as demoting it below
tuples that do not exist at that coordinate. Two implementers
can honestly disagree on whether "orders last" is a global sort
key (empty = +infinity, contradicting minimum semantics) or a
tie-break annotation (empty loses ties only). The
canonical-order seed's byte-comparison rule
(`spec/custos-4.2-seed-canonical-order.md`, merged) resolved
this: one comparison basis, stated once, with an explicit rule
for absent components.

**The erratum (binding on the successor; reading rule now):**
"orders last" is a TIE-BREAK annotation, not a global sort key —
the selection is the lexicographic minimum over (defeater-class
rank, citation identifier, subcode) where an absent subcode
compares GREATER than any present subcode at the same (rank,
identifier) and has no other effect. Equivalent statement: the
comparison basis is the seed's — absent components compare
after present ones, component-wise, within one total order.

---

## Register note

Both errata were found by the reconciliation census comparing
independently drafted seeds against the regenerated text — the
seed-PR rule's cross-check function working as designed. Both
defects entered through the assembly's recomposition of ruled
content, not through any ruling: the rulings were right; the
melder's prose under-executed them at two sites the gauntlet's
batteries did not probe (the payload bullet sat outside the
walls-enumeration battery's scope; the empty-subcode boundary
needs a discriminating vector, owed below). Successor obligation:
both sites repair under this supplement's readings. Station
obligation: the antinomy-payload vector pair (duplicity-pair
payload must-affirm; cardinality-3 circuit payload must-affirm —
the second discriminates against a pair-only reading) and the
empty-subcode boundary vector (sole-defeat-with-empty-subcode →
must-select-it; the vector convicts the +infinity reading).
