---
id: mrw-2ff2fe94bc57
type: example
title: Max-fiber antichain skeletons are union-free
aliases: ["mrw-2ff2fe94bc57", "Max-fiber antichain skeletons are union-free"]
status: proved
tags: ["example", "proved", "erdos", "lcm", "squarefree", "biased-measure", "union-free", "antichain", "support-tail", "patch-gate-audited"]
parents: ["mrw-b4075311abd3", "mrw-55a8d9eddd2e", "mrw-d0402aea6f58"]
refs: []
---

# Example: Max-fiber antichain skeletons are union-free

## Statement

Let \(P=\{1,\ldots,k\}\) be linearly ordered.  For each \(1\le m\le k\), let
\(\mathcal A_m\subseteq2^{\{1,\ldots,m-1\}}\) be an antichain, and define
\[
\mathcal F
=
\{X\cup\{m\}:\ 1\le m\le k,\ X\in\mathcal A_m\}.
\]
Then \(\mathcal F\) is union-free: there are no three distinct
\[
A,B,C\in\mathcal F
\]
with
\[
A\cup B=C.
\]

## Proof

Write \(\max(S)\) for the largest element of a nonempty set \(S\), so every
member of \(\mathcal F\) has a unique max-fiber representation
\[
S=X\cup\{\max(S)\},\qquad X\in\mathcal A_{\max(S)}.
\]

Suppose \(A=X\cup\{m\}\) and \(B=Y\cup\{n\}\) are in \(\mathcal F\), with
\(m\le n\).  If \(A\cup B\in\mathcal F\), then \(\max(A\cup B)=n\), so
\[
A\cup B=Z\cup\{n\}
\]
for some \(Z\in\mathcal A_n\).  Also \(Y\subseteq Z\), because \(B\subseteq
A\cup B\).

Since \(\mathcal A_n\) is an antichain and \(Y,Z\in\mathcal A_n\), this forces
\(Z=Y\).  Hence \(A\cup B=B\).  Thus any union of two members of
\(\mathcal F\) that lands back in \(\mathcal F\) is one of the two original
members, not a third distinct member.  Therefore \(\mathcal F\) is union-free.

## Depends on

- [[mrw-b4075311abd3]] for the union-free formulation.

## Used by

- [[mrw-55a8d9eddd2e]] as a non-rank-only skeleton that a weighted proof must
  control.

## Notes

- This is not a counterexample to the weighted union-free theorem.  It records a
  structural skeleton that is union-free by construction.
- The next audit is to prove that such max-fiber antichain skeletons have
  vanishing \(\nu_{P_k}\)-mass in the high-support window, or to identify a
  variant that can carry positive mass.
