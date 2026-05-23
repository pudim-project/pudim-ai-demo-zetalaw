---
id: mrw-8fcc1c2c5cda
type: counterexample
title: Ordinary shifts do not preserve union-free families
aliases: ["mrw-8fcc1c2c5cda", "Ordinary shifts do not preserve union-free families"]
status: proved
tags: [counterexample, proved, erdos-536, union-free, compression, shifting, route-kill, weighted-measure]
parents: [mrw-55a8d9eddd2e, mrw-265ec9f57561]
refs: ["references/sources/20260519T121424Z-union-free-compression-context.md"]
  - raw/20260519T121424Z-erdos536-compression-obstruction.md
  - references/requests/20260519T121424Z-union-free-compression-erudition-gate.md
  - references/sources/20260519T121424Z-union-free-compression-context.md
  - oracle/responses/20260519T121424Z-erdos536-compression-oracle-response.md
---

# Counterexample: Ordinary shifts do not preserve union-free families

## Statement

Ordinary \(ij\)-shifting, also called compression, does not preserve the
union-free property.

More explicitly, on the ground set \(\{1,2,3\}\), let
\[
\mathcal F=\{\{1\},\{1,2\},\{3\}\}.
\]
Then \(\mathcal F\) is union-free.  However, applying the ordinary shift
\(S_{2,3}\), which replaces \(3\) by \(2\) when possible, gives
\[
S_{2,3}(\mathcal F)=\{\{1\},\{2\},\{1,2\}\},
\]
and this shifted family is not union-free because
\[
\{1\}\cup\{2\}=\{1,2\}.
\]

Consequently, the prime-biased weighted union-free problem
[[mrw-55a8d9eddd2e]] cannot be reduced to shifted or left-compressed families
by the standard measure-increasing compression argument without an additional
union-aware constraint.

This is a genuine weighted-direction obstruction.  Under the prime weights
\[
q_1=\frac12,\qquad q_2=\frac13,\qquad q_3=\frac15,
\]
one has
\[
\nu(\mathcal F)=\frac7{15},
\qquad
\nu(S_{2,3}(\mathcal F))=\frac8{15}.
\]
Thus the shift increases the prime-biased product measure while leaving the
admissible class.

## Proof

First check \(\mathcal F\).  The union
\[
\{1\}\cup\{3\}=\{1,3\}
\]
is not in \(\mathcal F\).  The other unions involving \(\{1,2\}\) are either
\(\{1,2\}\) itself or \(\{1,2,3\}\), so no three distinct members
\(A,B,C\in\mathcal F\) satisfy \(A\cup B=C\).  Thus \(\mathcal F\) is
union-free.

Under \(S_{2,3}\), the set \(\{3\}\) is replaced by \(\{2\}\), since
\(\{2\}\notin\mathcal F\).  The sets \(\{1\}\) and \(\{1,2\}\) are unchanged.
Therefore
\[
S_{2,3}(\mathcal F)=\{\{1\},\{2\},\{1,2\}\}.
\]
This shifted family contains three distinct members satisfying
\[
\{1\}\cup\{2\}=\{1,2\},
\]
so it is not union-free.  This proves the counterexample.

For the displayed prime weights, direct multiplication gives
\[
\nu(\mathcal F)
=
\nu(\{1\})+\nu(\{1,2\})+\nu(\{3\})
=\frac4{15}+\frac2{15}+\frac1{15}
=\frac7{15},
\]
whereas
\[
\nu(S_{2,3}(\mathcal F))
=
\nu(\{1\})+\nu(\{2\})+\nu(\{1,2\})
=\frac4{15}+\frac2{15}+\frac2{15}
=\frac8{15}.
\]
So the counterexample occurs in the weight-increasing direction relevant to
the prime-biased problem.

## Depends on

- [[mrw-55a8d9eddd2e]] Prime-biased weighted union-free theorem
- [[mrw-265ec9f57561]] Subcritical max-fiber antichain width forces vanishing high-support mass

## Used by

- [[mrw-3474bf5c904f]] Union-aware weighted compression problem for prime-biased union-free families

## Notes

For the prime weights \(1/p_i\), ordinary shifts from larger primes to smaller
primes would be the natural measure-increasing operation.  This counterexample
shows that such shifts cannot be used as a black-box reduction to shifted
families.  A compression route must either preserve union-freeness by a
modified rule, work only in an extremal-admissible sense, or be replaced by a
container or decomposition argument that does not require shifted normal form.

The focused Oracle response audited this example and agreed that it blocks the
ordinary unrestricted shifted-family reduction, while not ruling out
admissible ad-extremis shifts or container methods.
