# Review brief — the over-generalization tendency and the missed integration surface (2026-08-03)

## The charge, from the ratifying authority (verbatim intent)

The Custos 4.2 candidate systematically writes "the encoding
substrate" / "the credential layer" / "the medium" where CESR,
ACDC, and KERI are meant specifically. The authority has ruled
this a defect class and ordered a WHOLISTIC review — beyond
naming: "it is more than names, we must actually understand the
finger pointing at the moon."

The suspicion: the generic register is not just a prose tic — it
is a SYMPTOM of under-integration. Where the document abstracts
over "an encoding layer," it stops SEEING what CESR specifically
offers; where it abstracts over "a credential layer," it stops
seeing ACDC's actual machinery. The compact receipt form (the
candidate's section 19) exists ONLY because CESR's genus/count-
code architecture makes it possible — that is what integration
looks like: a design move that could not have been made against
a generic substrate. The question is where ELSE such moves are
waiting, unseen because the prose blurred the specific into the
generic. Custos means to be KIN to KERI/CESR/ACDC — a peer layer
designed WITH the family's actual mechanisms, not floating above
an abstracted stack.

## Your task, two parts

**PART A — the audit.** Read the candidate for every site where
key infrastructure is named generically ("the substrate", "the
medium", "the encoding layer", "the credential layer", "registry
machinery", etc.). For each LOAD-BEARING site, classify:
- TRUE GENERALITY: the claim genuinely holds for any conformant
  implementation of the abstract role (keep, with grounds);
- FALSE GENERALITY: the design depends on the named spec's
  specific mechanics (CESR count codes/genus tables/framing,
  ACDC SAID-addressing/graduated disclosure/edge grammar/
  registry (TEL) semantics, KERI KEL/superseding-recovery/
  witness-receipt machinery) — the generic prose claims a
  portability the design does not have;
- MISSED INTEGRATION: the site where writing generically caused
  the design to NOT USE a specific mechanism the family offers —
  the most valuable class. Name the mechanism and sketch the
  integration.

**PART B — the innovation survey.** Independent of prose sites:
enumerate the specific mechanisms of CESR, ACDC, and KERI that
this architecture COULD integrate but currently does not (or
uses shallowly). For each: the mechanism (with its actual
technical shape), the Custos surface it would serve, and what
the integration would enable that the current design cannot do.
Think the way the compact-receipt form was found: CESR genus
reservation -> a governance-native wire form. What are the other
moves of that class? Consider at minimum: CESR (count codes,
genus/version tables, native field maps vs JSON, streaming/
pipelining, cold-start framing, op codes), ACDC (graduated/
partial/selective disclosure, chain-link confidentiality, edges
and edge operators, schema as type, bulk issuance, contractually
protected disclosure), KERI (witness receipts and thresholds,
superseding recovery, delegation (dip/drt), multisig, watchers/
judges/juries, key state notices, BADA/RUN, OOBIs). Do not limit
to these lists.

Rank part-B findings by leverage: which integration would most
strengthen the standard's actual guarantees (not its rhetoric)?

## Register for your output

Findings, not praise. Each finding: site (line range where
applicable), classification, grounds in one or two sentences,
and for MISSED INTEGRATION / part-B entries a concrete sketch.
Severity: BLOCKING candidates (false generality that would
mislead an implementer) / MAJOR (missed integration with real
leverage) / NOTE. No padding. The authority reads conclusions.

## Inputs

- The candidate: weave/custos-4.2-candidate-v1.md (sha256
  c62c1ddeeb5ad73fa8bdf5e1fb2a812865ccf72a8b04e05a8f6e38cddf2a67c8,
  3,596 lines). Sections: Ch1 domain, Ch2 governed-object
  taxonomy, 3-18 machinery, 19 compact form + gates, appendix
  censuses.
- The ratified predecessor for comparison where useful:
  staged-repos/custos/spec/custos-4.1.md.
- The gates/transport doctrine: weave/42-compact-form-gates.md.
- KERI/CESR/ACDC knowledge: your own; where you cite a specific
  upstream mechanism, name the spec section or the keripy
  surface so the claim is checkable.
