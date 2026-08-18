VERDICT: REFUTED

**Exhibit:** Certificate Transparency — Ben Laurie, Adam Langley, Emilia Kasper, RFC 6962, IETF, June 2013, as enforced in production by the Chrome CT policy and public CT monitors before 2026.

**Exact clause destroyed:** §V.6’s claim that **“no prior system holds P1, P2, P3, and P4 jointly,”** and specifically the document’s own dismissal of Certificate Transparency as only **“P1 partial, P4 textual but organ-less.”**

### Why Certificate Transparency holds P1–P4 under Part 0’s own grading

**P1 — finding-grade self-evaluation.**  
The document itself concedes CT logs “audit CAs and, via consistency proofs, partly themselves,” but downgrades this to “~”. That downgrade is not defensible under Part 0. CT’s evaluation is not sentiment and not a vote. It is cryptographic verification against declared invariants:

- an **inclusion proof** gives a replayable, third-party-checkable verdict that a certificate is in a particular log at a particular position under a signed tree head;
- a **consistency proof** between two signed tree heads gives a replayable verdict that the log grew append-only;
- if a log violates append-only, RFC 6962 §7.3 says conflicting signed tree heads are **“cryptographic proof of that log’s misbehavior.”**

That is a finding-grade verdict capable of convicting the log, not a reputation score. The CT policy layer provides the cure consequence: a log that misbehaves is removed from trusted log lists, and any replacement log can be audited from genesis with the same replayable machinery. The document’s Part 0 P1 definition does not require the system to repair a convicted cryptographic log *in place*; it requires the evaluation to be capable of convicting the foundation and certifying a cure. CT’s verification layer does exactly that: it convicts a bad log and can certify a new or remediated log’s consistency.

**P2 — sealed, attributable verification acts.**  
The document already grades CT P2 as **strong**, and that is correct. A Signed Certificate Timestamp is a signed, attributable receipt entered into the log; the signed tree heads are themselves signed commitments; who asserted what, against which log, in what order, is publicly replayable.

**P3 — standing organ.**  
The document already grades CT P3 as **strong**. This is not a one-shot audit: logs emit signed tree heads on a standing cadence; monitors and auditors run continuously; browser policy enforces CT across the public Web PKI at planetary scale.

**P4 — confessed residue as constitutional text.**  
RFC 6962 §5 states:

> “All clients should gossip with each other, exchanging STHs at least; this is all that is required to ensure that they all have a consistent view.”

RFC 6962 §7.3 states that append-only violation is detected by global gossiping, and that two conflicting signed tree heads are cryptographic proof of misbehavior.

That is exactly the residue the document’s own Part 0 P4 requires: **the log cannot establish its own unforkedness; only external observation supplies it.** It is written into the protocol’s normative constitution, not left as folklore, not smuggled. The docket’s “organ-less” grading adds an implementation-funding requirement that is not present in the P4 definition. Under the definitions actually stated in Part 0, CT clears P4.

### Why this is a refutation, not a near-miss

This is not four systems each holding one property. It is one system—Certificate Transparency—holding all four jointly. Two of the document’s own downgrades on the CT row, P1 and P4, are mistaken when measured against Part 0’s stated definitions. With P1 and P4 upgraded, the CT row reads:

| System | P1 | P2 | P3 | P4 |
|---|---|---|---|---|
| Certificate Transparency (2013) | yes | strong | strong | in normative text |

That destroys the “no prior system” conjunction.

DRIFT
- If the authors intend §V.6 to survive, the repair is not to dispute CT’s cryptographic mechanisms but to amend Part 0’s P4 so that it expressly requires a standing, chartered, funded organ rather than merely normative constitutional text. Under the current definitions, CT refutes the claim.
- The document may also need to explain why the Chrome CT log-policy enforcement layer and the existing public CT monitors do not count as the organ it says CT lacked.
