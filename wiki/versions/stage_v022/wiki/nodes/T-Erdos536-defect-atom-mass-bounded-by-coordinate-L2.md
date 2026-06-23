---
id: "T-Erdos536-defect-atom-mass-bounded-by-coordinate-L2"
type: "theorem"
title: "Erdos536 defect atom mass bounded by coordinate L2"
status: "proved"
tags: ["atom-mass", "defect-sets", "erdos-536", "l2-sieve", "proved", "student-proof", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema"]
refs: ["attack-plans/AP-20260606T2026-erdos536-square-sum-complement.json", "librarian/audits/LA-20260606T2035-erdos536-square-sum-complement-depletion-student.json", "oracle/responses/OS-20260606T224841Z-oracle-response.md", "raw/oracle/RO-OS-20260606T224841Z.json", "raw/student/20260606T2035-erdos536-square-sum-complement-depletion.md"]
---

# Theorem: Erdos536 defect atom mass bounded by coordinate L2

## Statement

Defect atom mass is bounded by coordinate L2 energy: for any probability law \(\lambda\) on nonempty defects \(D\subseteq C\), with independent \(D,E\sim\lambda\), the atom mass \(\alpha=\sum_D\lambda(D)^2=\Pr(D=E)\) is at most \(\sigma=\sum_{i\in C}\lambda(i\in D)^2=\mathbf E|D\cap E|\). Thus large atom mass is a subcase of L2-large energy, though not necessarily a common-core concentration.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]

## Proof and provenance references

- `attack-plans/AP-20260606T2026-erdos536-square-sum-complement.json`
- `librarian/audits/LA-20260606T2035-erdos536-square-sum-complement-depletion-student.json`
- `oracle/responses/OS-20260606T224841Z-oracle-response.md`
- `raw/oracle/RO-OS-20260606T224841Z.json`
- `raw/student/20260606T2035-erdos536-square-sum-complement-depletion.md`

## Proof

On the diagonal event \(D=E\), the defect is nonempty, so \(|D\cap E|=|D|\ge1\). Hence
\[
\mathbf E|D\cap E|\ge \Pr(D=E)=\sum_D\lambda(D)^2.
\]
The identity \(\mathbf E|D\cap E|=\sum_i\lambda(i\in D)^2\) is the coordinate \(L^2\) identity already admitted.

This shows large atom mass is a subcase of the \(L^2\)-large branch. It is still diagnostically distinct from common-core concentration: a large atom need not produce a coordinate shared by every defect, and a common core can occur with small atom mass.

Candidate: the Erdos536 defect atom spread control separates concentration.

The proved atom-energy lemma gives a clean diagnostic: atom mass cannot be large in the \(L^2\)-small branch, since \(\alpha_C\le I(C)\). However, the full AP candidate asked for a reduction saying either atom mass is small enough for distinct-pair conditioning or a large atom produces an explicit repeated-trace/chain obstruction. That stronger classification was not proved.

The next pass should split large atom mass into: dominant single lower trace, bounded family of repeated lower traces, and atom-heavy moving templates. Each must be tied either to rank/comparable-pair structure or to a real obstruction.

Candidate: the Erdos536 L2 large core shield descent or sparse matching.

No fixed/moving core extraction theorem was proved from large coordinate square-sum. The elementary fact remains that large \(\sum_i q_i^2\) indicates coordinate energy, but converting that into a persistent common core, endpoint shield, strict lexicographic descent, or actual sparse-matching lower-trace construction requires additional thresholds and persistence hypotheses.

This remains the lower-trace-rich complement after the true \(L^2\)-small branch.

Candidate: the Erdos536 lower trace poor comparable pair sink or obstruction.

No lower-trace-poor entropy/LYM/comparable-pair sink was proved. No positive-mass non-rank-thin lower-trace-poor obstruction was constructed. This remains independent of defect laws and should not invoke \(\lambda_C\) or square sums.

the Erdos536 defect atom mass bounded by coordinate L2: true.
the Erdos536 defect atom spread control separates concentration: candidate_open with true atom-energy sublemma.
the Erdos536 L2 large core shield descent or sparse matching: candidate_open.
the Erdos536 lower trace poor comparable pair sink or obstruction: candidate_open.
the Erdos536 coordinate coverage lower trace forces fork: remains open.
the Erdos536 prime biased weighted union free frontier: remains open.

_Proof source: `raw/student/20260606T2035-erdos536-square-sum-complement-depletion.md`._

## Tags

`atom-mass`, `defect-sets`, `erdos-536`, `l2-sieve`, `proved`, `student-proof`, `theorem`, `true`
