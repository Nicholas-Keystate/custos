# Succession record — Custos 3.3 → Custos 4.0

The detached record the kernel's succession clause (§15) requires:
predecessor digest, successor digest, and the lineage a stranger
can verify without trusting this repository.

## The editions

| Edition | Status | SHA-256 |
|---|---|---|
| Custos 3.3 | Superseded whole at the effectuation coordinate below | `18b0469e731db24f6bca45525828e4417751929306ea21e09977088e08a20ceb` |
| Custos 4.0 | **RATIFIED AND EFFECTIVE** | `9cefdc5d584289ea8391d8069bca26ea38aa82a34f9ae973d80e4d1b7773f315` |

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

## The ratification record

Ratified and effectuated 2026-07-23, as enactments in the
maintainers' governance event log (authority AID
`EFolWr6gUggZS9im4f1pWSoKB9Ngd-T9YI0c8tlGIaHU`):

| Field | Value |
|---|---|
| Kernel SAID (Blake3-256, CESR qb64) | `ELDBQXbJ20g3K-MSIqvcz1z4dSzasKxx8FkBovmo8cF1` |
| Succession object SAID | `EDMQ3uf-ykiwAKjnRxyenb3pGrZp0rzjon8Vi8Hm-beQ` |
| Evidence manifest SAID | `EMnF-y7r-a-6VPsPtN_xHQPAsLiPEeol6N-MFtI1xReI` |
| Lineage id | `ED9lzvOtsAvCa8IbXRYGh_6X6TkW2N8VQ4y6VObkkity` |
| Ratification act | `EIq9vT-V__NE9EcKUMd0lLdgzSkt0imQhuHVedCtQWM6`, anchored at KEL sn 181 |
| Effectuation act | `ECForf8ycgYjp8m-P25BYJCAsyNOL8CD5mM_783f1HOv`, anchored at KEL sn 182 |
| Prospectivity | 4.0 binds positions at and after sn 182, none before |
| Predecessor lineage | 3.2→3.3 ratified sn 172 / effective sn 173; 3.1→3.2 at sn 170/171 |

**Grade confession (per the kernel's own §3 genesis knot):** the
authority AID was incepted before its founding law was ratified —
this domain is therefore **adopted-grade**, not born-governed: its
identity ranges over keys alone, and its law is anchored, never
sealed at birth. Confessed by ruling; continuity with the sn
170–182 lineage was chosen over re-inception. The kernel treats
the adopted construction as lawful at a confessed lesser grade;
this record is that confession.

The succession object, evidence manifest (digest-addressed review
record: five adversarial legs, the completeness audit, the gate),
acts, and lineage record are committed workspace artifacts,
SAID-addressed above; holders may request them and verify every
digest independently.

## Verify

```
python tools/verify_kernel.py
```

Recomputes the kernel digest, extracts the §15 predecessor pin,
and checks internal consistency of this record. It proves bytes,
not authority: authority is the governance event log's to prove.
