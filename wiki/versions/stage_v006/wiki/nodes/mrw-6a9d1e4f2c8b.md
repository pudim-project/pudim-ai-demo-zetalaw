---
id: mrw-6a9d1e4f2c8b
type: note
title: Star deletion traces obstruct trace-local growing-deletion estimates
aliases: ["mrw-6a9d1e4f2c8b", "Star deletion traces obstruct trace-local growing-deletion estimates"]
status: proved
tags: [note, proved, erdos-536, union-free, deletion-trace, intersecting-family, star, obstruction, growing-deletion, support-tail]
parents: [mrw-cc4f876149b7, mrw-0d6b8cbd7ced, mrw-55a8d9eddd2e, mrw-d0402aea6f58, mrw-3c39ca3d1973]
refs: []
  - raw/20260519T141427Z-erdos536-growing-deletion-trace.md
  - references/requests/20260519T141427Z-growing-deletion-trace-erudition-gate.md
  - references/sources/20260519T141427Z-growing-deletion-trace-context.md
  - oracle/responses/20260519T141427Z-erdos536-star-trace-oracle-response.md
---

# Note: Star deletion traces obstruct trace-local growing-deletion estimates

## Statement

Let \(C\) be a finite nonempty set, fix \(x\in C\), and define the star deletion
trace
\[
\mathcal S_x(C)=\{D\subseteq C:\ x\in D\}.
\]
Then \(\mathcal S_x(C)\) is pairwise intersecting.  Moreover, if
\(\pi_{C,\lambda}\) is the product law on \(2^C\) under which each coordinate
lies in the deletion set independently with probability \(0<\lambda<1\), then
\[
\pi_{C,\lambda}(\mathcal S_x(C))=\lambda.
\]
If \(L_n\) is any sequence with
\[
\limsup_{n\to\infty}\frac{L_n}{n}<\lambda,
\]
then along every sequence \(|C_n|=n\),
\[
\pi_{C_n,\lambda}\bigl(\{D\in\mathcal S_{x_n}(C_n): |D|\ge L_n\}\bigr)
\longrightarrow \lambda.
\]
Equivalently, for each \(n\) one may choose any root \(x_n\in C_n\) and use
\(\mathcal S_{x_n}(C_n)\).

This is a statement for fixed \(0<\lambda<1\) and thresholds measured relative
to \(|C_n|\).  It does not control thresholds measured relative to
\(S_k=\sum_{i\le k}1/p_i\) unless the relevant top supports satisfy
\(|C_n|\asymp S_k\).

Consequently, pairwise intersection of deletion traces alone cannot prove that
large-deletion trace mass vanishes for thresholds below the ambient deletion
mean \(\lambda |C|\).  A growing-deletion proof of [[mrw-55a8d9eddd2e]] must
use global information about how rooted traces are realized across many top
sets, the full union hypergraph, or the full pair-link hypergraph.  It cannot
be only a trace-local theorem saying that an intersecting deletion trace has
negligible mass below the natural deletion mean.

## Proof

Any two members of \(\mathcal S_x(C)\) both contain \(x\), so
\(\mathcal S_x(C)\) is pairwise intersecting.

Under \(\pi_{C,\lambda}\), membership in \(\mathcal S_x(C)\) is exactly the
event \(x\in D\).  Hence
\[
\pi_{C,\lambda}(\mathcal S_x(C))=\lambda.
\]

Conditioned on \(x\in D\), the remaining deletion size is distributed as
\[
|D|=1+\operatorname{Bin}(|C|-1,\lambda).
\]
If \(|C_n|=n\) and \(\limsup L_n/n<\lambda\), choose
\(\rho\) such that
\[
\limsup_{n\to\infty}\frac{L_n}{n}<\rho<\lambda.
\]
For all sufficiently large \(n\), \(L_n\le \rho n\).  Since
\[
\frac{1+\operatorname{Bin}(n-1,\lambda)}{n}\to\lambda
\]
in probability, we have
\[
\Pr\!\left(1+\operatorname{Bin}(n-1,\lambda)<L_n\right)\to0
\]
by Chebyshev's inequality, or any standard weak law of large numbers.  Therefore
\[
\pi_{C_n,\lambda}\bigl(\{D\in\mathcal S_{x_n}(C_n): |D|\ge L_n\}\bigr)
=
\lambda\,
\Pr\!\left(1+\operatorname{Bin}(n-1,\lambda)\ge L_n\right)
\to\lambda.
\]
This proves the claim.

## Depends on

- [[mrw-cc4f876149b7]] Intersecting deletion-trace obstruction for
  lower-shadow union covers
- [[mrw-0d6b8cbd7ced]] Bounded-deletion rank-congruence obstruction for
  union-free containers
- [[mrw-55a8d9eddd2e]] Prime-biased weighted union-free theorem
- [[mrw-d0402aea6f58]] Biased lower-shadow union-cover problem for Erdos 536
- [[mrw-3c39ca3d1973]] Pair-link shadow criterion for biased squarefree
  residuals

## Used by

- Next route: replace a trace-local growing-deletion estimate by a global
  root-consistency, rooted-container, or pair-link theorem.

## Notes

This note is not a counterexample to the full weighted union-free theorem.
It is a counterexample only to a trace-local shortcut.  Star traces can carry
fixed positive mass at deletion sizes tending to infinity, and at linear
thresholds \(L_n\le(\lambda-\varepsilon)|C_n|\), while remaining pairwise
intersecting.  At the critical scale \(L_n\sim\lambda |C_n|\), or above it, the
behavior is different and is not used here.

This is also not a realization theorem: it does not show that the traces
\(\mathcal S_x(C)\) arise coherently as \(\mathcal D_{\mathcal F}(C)\) for a
positive-mass high-support union-free family.  The remaining question is
whether such rooted traces can occur coherently on a positive \(\nu_{P_k}\)-mass
high-support union-free family.  That global realization problem is exactly the
next useful target.
