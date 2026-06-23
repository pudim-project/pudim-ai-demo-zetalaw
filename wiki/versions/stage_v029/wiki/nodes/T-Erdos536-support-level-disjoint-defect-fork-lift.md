---
id: "T-Erdos536-support-level-disjoint-defect-fork-lift"
type: "theorem"
title: "Erdos536 support level disjoint defect fork lift"
status: "proved"
tags: ["defect-sets", "erdos-536", "fork-lift", "proved", "support-level", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema"]
refs: ["attack-plans/AP-20260606T185720-erdos536-matching-like-defect-obstructions.json", "librarian/audits/LA-20260606T1904-erdos536-matching-obstruction-support-lift-student.json", "oracle/responses/OS-20260606T215832Z-oracle-response.md", "raw/oracle/RO-OS-20260606T215832Z.json", "raw/student/20260606T1904-erdos536-matching-obstruction-support-lift.md", "theory/nodes/T-Erdos536-defect-disjointness-coverage-normal-form.json"]
---

# Theorem: Erdos536 support level disjoint defect fork lift

## Statement

For any family \(\mathcal F_k\), occupied top \(C\in\mathcal F_k\), and proper lower traces \(A,B\in\mathcal F_k\) with \(A,B\subsetneq C\), the disjoint-defect condition \((C\setminus A)\cap(C\setminus B)=\varnothing\) is equivalent to \(A\cup B=C\). Hence any support-level disjoint defect pair below an occupied top is a fork, and union-free families have pairwise-intersecting defect supports below every occupied top.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]

## Proof and provenance references

- `attack-plans/AP-20260606T185720-erdos536-matching-like-defect-obstructions.json`
- `librarian/audits/LA-20260606T1904-erdos536-matching-obstruction-support-lift-student.json`
- `oracle/responses/OS-20260606T215832Z-oracle-response.md`
- `raw/oracle/RO-OS-20260606T215832Z.json`
- `raw/student/20260606T1904-erdos536-matching-obstruction-support-lift.md`
- `theory/nodes/T-Erdos536-defect-disjointness-coverage-normal-form.json`

## Proof

\emph{Setup.}
The refuted move remains quarantined: do not claim that small disjoint-pair probability implies deletion of \(o(1)\) mass to a pairwise-intersecting support. The true tool is instead the exact defect identity: for lower traces \(A,B\subsetneq C\) with defects \(D=C\setminus A\), \(E=C\setminus B\),
\[
D\cap E=\varnothing\quad\Longleftrightarrow\quad A\cup B=C.
\]

Candidate: $c1.

If \(C\in\mathcal F_k\) and \(A,B\in\mathcal L_{\mathcal F_k}(C)\) have disjoint defects, then \(A,B,C\) are distinct members of \(\mathcal F_k\) and
\[
A\cup B=C.
\]
Thus any support-level disjoint defect pair below an occupied top is already a fork. In particular, a genuinely union-free family has no support-level disjoint defect pair below any occupied top.

Proof: by definition \(A,B\subsetneq C\), so \(A\ne C\) and \(B\ne C\). If \(D\cap E=\varnothing\), then the true defect normal form gives \(A\cup B=C\). Also \(A\ne B\), since \(A=B\subsetneq C\) would imply \(A\cup B=A\ne C\). Hence the three family members form a forbidden union triple.

This is useful, but it does not prove the full candidate as stated. The candidate asks for either rank-thinness or a positive/fork obstruction strong enough to imply the coordinate-coverage theorem. A sparse matching component may give support-level forks while still having conditional two-sample mass \(o(1)\), so it does not yield \(\mathbf E\Omega_k(C)>0\) without an extra density or union-free-target reformulation.

Candidate: $c2.

The support-level lift absorbs matching obstructions for exactly union-free families: a matched edge is already fatal. However, the current source node is stronger and density-based: it asks for positive expected coordinate coverage, not merely existence of a fork. The matching construction shows that support-level existence and positive two-sample density are not equivalent. No proof was found that every sparse matching component is rank-thin, common-core, or endpoint-recursive with positive-density loss.

The right next formulation must choose one of two paths:

1. weaken the source route to a support-level theorem sufficient for the weighted union-free frontier; or
2. add a quantitative lower bound proving that admissible matching components cannot have vanishing conditional mass per matched edge.

Candidate: $c3.

The finite matching and projective-plane constructions show abstract defect laws with vanishing disjoint-pair probability and no simple common core. They can be locally represented below a single top \(C\) by taking lower traces \(C\setminus D
or each defect atom \(D\). This realizes the support geometry, but it is not yet an admissible positive-mass Erdos536 sequence: a single top has negligible product mass, and adding many tops while preserving union-free constraints and non-rank-thin positive ambient mass is not solved.

Thus the diagnostic construction remains open. The local model is a serious obstruction to density-based proofs, but not yet a counterexample to the Erdos536 lower-trace route.

Promote $lift:

For any family \(\mathcal F_k\), occupied top \(C\in\mathcal F_k\), and proper lower traces \(A,B\in\mathcal F_k\) with \(A,B\subsetneq C\), disjoint defects \((C\setminus A)\cap(C\setminus B)=\varnothing\) are equivalent to the fork relation \(A\cup B=C\). Therefore union-free families have support-level pairwise-intersecting defect supports below every occupied top.

$c1: candidate_open, with true support-level lift sublemma $lift.
$c2: candidate_open.
$c3: candidate_open, local matching/projective-plane diagnostics only.

_Proof source: `raw/student/20260606T1904-erdos536-matching-obstruction-support-lift.md`._

## Tags

`defect-sets`, `erdos-536`, `fork-lift`, `proved`, `support-level`, `theorem`, `true`
