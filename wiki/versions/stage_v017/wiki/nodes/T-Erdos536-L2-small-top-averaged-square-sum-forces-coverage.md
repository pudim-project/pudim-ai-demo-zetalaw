---
id: "T-Erdos536-L2-small-top-averaged-square-sum-forces-coverage"
type: "theorem"
title: "Erdos536 L2 small top averaged square sum forces coverage"
status: "proved"
tags: ["coverage", "erdos-536", "l2-sieve", "lower-trace-rich", "proved", "student-proof", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema"]
refs: ["private attack plan", "private librarian audit", "private Oracle response", "private Oracle audit", "private proof note"]
---

# Theorem: Erdos536 L2 small top averaged square sum forces coverage

## Statement

Lower-trace-rich L2-small coverage theorem: in a lower-trace-rich admissible model with top law \(\tau_k\) and defect laws \(\lambda_C\), if the top-averaged coordinate square-sum satisfies \(\mathbf E_{C\sim\tau_k}\sum_{i\in C}\lambda_C(i\in D)^2\le 1-\epsilon\) for some fixed \(\epsilon>0\), then \(\mathbf E_{C\sim\tau_k}\Omega_k(C)\ge\epsilon\). Consequently the family contains a support-level fork and cannot be union-free under the distinct-triple convention.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private Oracle response`
- `private Oracle audit`
- `private proof note`

## Proof

The true coordinate \(L^2\) disjointness sieve gives, for every top \(C\),
\[
\Omega_k(C)
=1-\lambda_C^{\otimes2}\{D\cap E\ne\varnothing\}
\ge 1-I(C).
\]
Averaging over \(C\sim\tau_k\) gives
\[
\mathbf E_C\Omega_k(C)
\ge
1-\mathbf E_C I(C)
\ge \epsilon.
\]
The true positive-average coverage node then supplies distinct lower traces \(A,B\subsetneq C\) with \(A\cup B=C\). This is a union-free violation. No stability or mass-deletion principle is used.

Candidate: the Erdos536 L2 large coordinate concentration classification.

No complete classification was proved for the complementary branch where \(\mathbf E_C I(C)\) is close to or exceeds \(1\). The square-sum can be large for several reasons: fixed common core, endpoint shield, large atom/diagonal mass, large defect sizes, or more structured sparse-matching/intersecting behavior. The well-founded complexity tool gives a possible termination framework, but this pass did not prove that any of those branches strictly descends or yields an actual sparse-matching lower-trace construction.

The next AP should separate at least three sub-branches: atom/spread control, fixed-or-moving coordinate concentration, and genuine sparse-matching geometry.

Candidate: the Erdos536 lower trace poor entropy sink or obstruction.

No entropy/LYM/comparable-pair sink theorem was proved for lower-trace-poor families. No positive-mass non-rank-thin lower-trace-poor obstruction was constructed. This remains independent of the defect-law machinery because \(\lambda_C\) is unavailable or negligible in this branch.

The antichain empty-trace obstruction remains only structural: exact-rank antichains may be rank-thin or negligible under the intended prime-biased measure, so they are not yet the requested non-rank-thin positive-mass obstruction.

the Erdos536 L2 small top averaged square sum forces coverage: candidate_true.
the Erdos536 L2 large coordinate concentration classification: candidate_open.
the Erdos536 lower trace poor entropy sink or obstruction: candidate_open.
the Erdos536 coordinate coverage lower trace forces fork: remains open.
the Erdos536 prime biased weighted union free frontier: remains open.

_Proof source: `private proof note`._

## Tags

`coverage`, `erdos-536`, `l2-sieve`, `lower-trace-rich`, `proved`, `student-proof`, `theorem`, `true`
