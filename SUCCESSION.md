# Succession record — Custos 3.3 → Custos 4.0

The detached record the kernel's succession clause (§15) requires:
predecessor digest, successor digest, and the lineage a stranger
can verify without trusting this repository.

## The editions

| Edition | Status | SHA-256 |
|---|---|---|
| Custos 3.3 | Ratified predecessor; superseded whole upon 4.0's effectuation | `18b0469e731db24f6bca45525828e4417751929306ea21e09977088e08a20ceb` |
| Custos 4.0 kernel | CANDIDATE (pre-ratification) | `see spec/ — recompute with tools/verify_kernel.py` |

The 3.3 digest above is also pinned inside the kernel's own §15 —
the two pins must agree, and `tools/verify_kernel.py` checks that
they do.

## Why the predecessor publishes by digest, not by copy

Custos 3.3 is committed, immutable record. This repository cites
it by digest rather than carrying its bytes: holders of the bytes
can verify them against the pin above; anyone needing them may
request them from the maintainers. This is the kernel's own
mirror rule practiced on its own predecessor — a repository
preserves history; which bytes are law is computed from the
governance event log, never read off any mirror. The
completeness audit and migration register under `reviews/` record
exactly what the 4.0 kernel carries, transforms, supersedes, and
leaves in the predecessor.

## Ratification (pending)

Ratification of 4.0 is an enactment: an event in the maintainers'
governance event log sealing the ratified kernel's SAID, with a
stated effectuation coordinate. When it lands, this file gains:

- the ratified kernel digest (final bytes, post-ratification-read);
- the enacting event's coordinate and seal;
- the effectuation coordinate (succession is never retroactive:
  4.0 binds positions at and after it, none before);
- replay instructions for the succession record.

Until then, the kernel is a candidate and this repository says so.

## Verify

```
python tools/verify_kernel.py
```

Recomputes the kernel digest, extracts the §15 predecessor pin,
and checks internal consistency of this record. It proves bytes,
not authority: authority is the governance event log's to prove.
