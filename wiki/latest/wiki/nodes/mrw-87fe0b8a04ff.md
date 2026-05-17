---
id: mrw-87fe0b8a04ff
type: conjecture
title: Scout forage proposed solution
aliases: ["mrw-87fe0b8a04ff", "Scout forage proposed solution"]
status: superseded
tags: ["scout-forage", "solution", "superseded"]
parents: [mrw-900d84ddee24]
refs: []
---

# Conjecture: Scout forage proposed solution

## Statement

A candidate solution was returned but has not been locally proved.

## Evidence

Candidate solved: none locally proved.

Advisory proposed solution for Candidate 1: The Oracle response proposes a telescoping enclosure for
\[
T_7(n)=\sum_{k=n}^{\infty}k^{-7}
\]
using
\[
Q(n)=120n^6-360n^5+660n^4-720n^3+354n^2-54n+375,\qquad P(n)=Q(n)/20,
\]
and claims that for \(n\ge 28\),
\[
\left\lfloor T_7(n)^{-1}\right\rfloor
=
\left\lfloor P(n)\right\rfloor.
\]

Proof-audit risks:
- The raw Oracle transcript contains malformed display math and at least one corrupted identity line in the first telescoping comparison.
- The algebraic difference identities involving \(Q(k)\), \(Q(k+1)\), \(Q(k)-3\), and \(Q(k+1)-3\) must be independently expanded and verified.
- The congruence claim about possible fractional parts of \(P(n)\) modulo \(20\) must be checked.
- The finite cases \(1\le n\le 27\) were asserted but not locally certified.
- The literature status must be updated beyond the 2018 "no formula known for \(s>6\)" statement before any public claim that this solves a currently open problem.

Partial local sanity check:
- Symbolic expansion confirmed the two displayed telescoping difference identities in the normalized response.
- The residues of \(Q(n)\) modulo \(20\) over one complete residue cycle are \(3,15,19\), as claimed.
- Decimal interval checks found no failure for \(28\le n\le80\).
- These checks do not certify the finite cases \(1\le n\le27\) or the current open-problem literature status.

Local status: superseded by the proved theorem node [[wiki/nodes/mrw-28bcccec471e|Exact inverse-tail floor formula at s=7]].

## Resolution

- [[wiki/nodes/mrw-28bcccec471e|Exact inverse-tail floor formula at s=7]]

## Notes

- This node preserves the original scout-forage proposed solution. The proved, audited version is the theorem node linked above.
