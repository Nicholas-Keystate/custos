# Seat packet — text-identity review (2026-08-27)

You are one seat in a multi-seat blind review. Other seats exist,
under more than one administration; you will not see their
verdicts, and they will not see yours, until all are sealed. Work
from committed bytes only.

## Reading order (read fully before reasoning)

1. Workspace bedrock: AGENTS.md (workspace root)
2. The ratified corpus whose identity is at issue:
   staged-repos/custos/spec/custos-4.2.md — especially §6 (the
   medium) and §17 (succession and ratification)
3. The five members below — their full filed texts are committed
   in this round dir: filings/issue-85.md, filings/issue-86.md,
   filings/issue-90.md, filings/pr-92.md + filings/pr-92.diff,
   filings/issue-77-organ3-excerpt.md (the confessed-open
   question is in its final sentences)
4. The two standing guards that already patrol this territory:
   staged-repos/custos/tools/check-corpus-characters.py
   staged-repos/custos/tools/check-block-lines.py
5. Freshest carriage precedent:
   staged-repos/custos/reviews/ruling-record-supplement-10-2026-08-27.md
6. The seal vocabulary and Cardinal Grounds rows in notation.md
   (workspace root)

## The question

What is the identity of a provision of committed law — across
reformatting, across carriage, across amendment — and how is
that identity referenced and hashed?

## The five members (UNORDERED — any structure among them is
## yours to find and defend, not given)

- Issue #85: law is referenced two ways — by content and by
  place; a SAID-only identity cannot carry "the superseded
  defeater relation" as a stable reference across amendment.
- Issue #86 (MAJOR): characters are uncommitted — law can be
  written to read one way and hash another (normalization forms,
  homoglyphs, invisible code points).
- Issue #90: carriage wrapping vs line-pins — reflow changes
  bytes without changing text; line-anchored references break.
- PR #92: a locator-carriage seed, currently HELD, proposing how
  a place-reference travels inside committed artifacts.
- The confessed-open successor-binding question (issue #77,
  obligation organ 3, grade 2): when a successor binds to law,
  does it CITE the provision's identity or CARRY its bytes?

ADVOCACY WARNING: these filings are authored positions (several
by one reviewer, one seed by the workspace that packaged this
round). Treat all as advocacy, none as findings. Check bytes;
do not trust prose. Where a filing asserts a byte-level fact,
verify it at the cited site before consuming it.

## The questions you answer (all five, in order)

Q1. Is this one doctrine or several? If one, state it; if
    several, draw the seams and say which members belong where.
Q2. What is the minimal canonical-form commitment that makes
    stable reference possible at all? (Unicode normalization?
    byte-freezing? a grammar-derived canonical emission?) Ground
    the answer in what the two standing guards ALREADY commit
    the corpus to — read their code and state what invariant
    they enforce today.
Q3. Can a place-reference (a locator) be made stable across
    amendment without becoming a mutable pointer — and if not,
    which property gives? State the trade as a trade.
Q4. Successor binding at grade 2: citation or carriage? Argue
    from your Q2/Q3 answers, not from taste. If your answer is
    "neither as stated" or "both, split by case," define the
    split.
Q5. COVERAGE COMPLETENESS EXHIBIT: construct a concrete case the
    current corpus rules do NOT prevent, in which one text reads
    one way to a human and hashes or binds another way to the
    machinery. Give actual characters/bytes (escape sequences
    acceptable), name which guard or rule fails to catch it, and
    demonstrate the divergence (deletion/substitution
    discipline: show what changes and what stays fixed). A
    review with only passing cases proves nothing.

## Verdict form (your single output file)

For each of Q1–Q5: your answer; evidence bytes cited as
path:line; your confessed limits (what you could not verify and
why). Then, mandatory, once for the whole verdict: the REVERSAL
CONDITION — the single strongest consideration that would
reverse your central ruling.

Integrity convention: every quoted passage carries its source
path and line. Quoting text that does not exist in the committed
corpus voids the verdict whole.
