---
id: "T-Erdos536-small-defect-intersecting-system-forces-coordinate-marginal"
type: "theorem"
title: "Erdos536 small defect intersecting system forces coordinate marginal"
status: "proved"
tags: ["coordinate-concentration", "defect-sets", "erdos-536", "intersecting", "proved", "student-proof", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema"]
refs: ["attack-plans/AP-20260606T2043-erdos536-sharpened-remaining-branches.json", "librarian/audits/LA-20260606T2057-erdos536-sharpened-branches-depletion-student.json", "oracle/responses/OS-20260606T225548Z-oracle-response.md", "raw/oracle/RO-OS-20260606T225548Z.json", "raw/student/20260606T2057-erdos536-sharpened-branches-depletion.md"]
---

# Theorem: Erdos536 small defect intersecting system forces coordinate marginal

## Statement

Small-defect intersecting-system coordinate lemma: if \(\mathcal D\) is a pairwise-intersecting family of nonempty defects, \(\lambda\) is a probability law on \(\mathcal D\), and \(D_0\in\mathcal D\) has size \(m\), then some coordinate \(i\in D_0\) has marginal \(\lambda(i\in D)\ge1/m\).

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]

## Proof and provenance references

- `attack-plans/AP-20260606T2043-erdos536-sharpened-remaining-branches.json`
- `librarian/audits/LA-20260606T2057-erdos536-sharpened-branches-depletion-student.json`
- `oracle/responses/OS-20260606T225548Z-oracle-response.md`
- `raw/oracle/RO-OS-20260606T225548Z.json`
- `raw/student/20260606T2057-erdos536-sharpened-branches-depletion.md`

## Proof

The inequality follows from \(q_i^2\le(\max_j q_j)q_i\) and summation. The condition \(I\ge1\) is the local necessary condition for zero disjoint-defect probability in the union-free lower-trace branch, via the true \(L^2\)-small coverage theorem.

Node added open: the Erdos536 spread intersecting defect design obstruction.

The AP's large-coordinate classification is incomplete. There are local pairwise-intersecting defect systems with small atom mass, small maximum coordinate marginal, large expected defect size, and no disjoint pairs. A projective-plane line system is the model example: lines pairwise intersect, the uniform line law has \(\max_i q_i\to0\), atom mass tends to zero, and \(\sum_i q_i^2\to1\). This is not a global Erdos536 counterexample, because actual lower-trace realization and positive prime-biased mass are not proved. It is, however, a real local obstruction to an atom/core/shield-only classification.

Candidate: the Erdos536 large atom lower trace obstruction classification.

No dominant-atom/finite-cluster/moving-template classification was proved. The new small-defect and bounded-mean lemmas show that atom and bounded-size branches can force coordinate marginals under intersecting assumptions, but they do not classify large atoms into the requested templates.

Candidate: the Erdos536 coordinate energy core shield persistence descent.

The bounded-mean lemma gives a clean route from \(L^2\)-large plus bounded expected defect size to coordinate concentration. However, it also exposes a missing branch: if expected defect size is unbounded and maximum coordinate marginal remains small, spread intersecting design-like systems may survive. No fixed/moving core, endpoint shield descent, or sparse-matching construction was proved.

Candidate: the Erdos536 lower trace poor comparable sink or nonrankthin construction.

No lower-trace-poor sink theorem or positive-mass non-rank-thin construction was proved. This branch remains independent of defect laws.

the Erdos536 small defect intersecting system forces coordinate marginal: true.
the Erdos536 bounded mean defect size forces coordinate concentration: true.
the Erdos536 spread intersecting defect design obstruction: open obstruction node.
the Erdos536 large atom lower trace obstruction classification: candidate_open.
the Erdos536 coordinate energy core shield persistence descent: candidate_open.
the Erdos536 lower trace poor comparable sink or nonrankthin construction: candidate_open.
the Erdos536 coordinate coverage lower trace forces fork: remains open.
the Erdos536 prime biased weighted union free frontier: remains open.

_Proof source: `raw/student/20260606T2057-erdos536-sharpened-branches-depletion.md`._

## Tags

`coordinate-concentration`, `defect-sets`, `erdos-536`, `intersecting`, `proved`, `student-proof`, `theorem`, `true`
