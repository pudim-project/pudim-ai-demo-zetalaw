---
id: mrw-25cdd8da0601
type: proposition
title: Pair-link-free families have injective one-swap insertion fibers
aliases: ["mrw-25cdd8da0601", "Pair-link-free families have injective one-swap insertion fibers"]
status: proved
tags: [erdos-536, squarefree-support, pair-link, hypergraph-independent-set, one-swap, insertion-fiber, johnson-exchange, support-tail, patch-gate-audited]
parents: [mrw-3c39ca3d1973, mrw-b1f87c9d6a42, mrw-4f1e9a2d6b73, mrw-6d4a8b0f2c91]
refs: []
  - raw/20260520T022056Z-erdos-536-sparse-pair-link-hypergraph-prove-one-swap-inserti.md
  - references/sources/20260520T022056Z-one-swap-insertion-fiber-context.md
  - oracle/requests/20260520T022056Z-erdos536-one-swap-insertion-fibers-oracle-request.md
  - oracle/responses/20260520T022056Z-erdos536-one-swap-insertion-fibers-oracle-response.md
---

# Proposition: Pair-link-free families have injective one-swap insertion fibers

## Statement
Let \(P\) be a finite set and put
\[
I(A,B)=\{C\subseteq P:A\triangle B\subseteq C\subseteq A\cup B\},
\qquad
I^\circ(A,B)=I(A,B)\setminus\{A,B\}.
\]
Let \(\mathcal F\subseteq2^P\) be pair-link-free, meaning there are no
pairwise distinct \(A,B,C\in\mathcal F\) with \(C\in I^\circ(A,B)\).

Fix \(A\in\mathcal F\).  For \(y\in P\setminus A\), define the one-swap
insertion fiber
\[
D_y^{\mathcal F}(A)
=
\{x\in A:(A\setminus\{x\})\cup\{y\}\in\mathcal F\}.
\]
Then
\[
|D_y^{\mathcal F}(A)|\le 1
\qquad(y\in P\setminus A).
\]
Consequently the same-rank one-swap neighborhood
\[
\Gamma_1^{\mathcal F}(A)
=
\{B\in\mathcal F:|A\setminus B|=|B\setminus A|=1\}
\]
satisfies
\[
|\Gamma_1^{\mathcal F}(A)|\le |P\setminus A|.
\]

## Proof
Suppose, to the contrary, that \(x,z\in D_y^{\mathcal F}(A)\) are distinct.
Set
\[
B=(A\setminus\{x\})\cup\{y\},
\qquad
C=(A\setminus\{z\})\cup\{y\}.
\]
By the definition of \(D_y^{\mathcal F}(A)\), both \(B\) and \(C\) lie in
\(\mathcal F\).  Also \(A\in\mathcal F\), \(B\ne A\), and \(C\ne A\) because
\(y\notin A\).  Finally \(C\ne B\), since \(x\in C\setminus B\).

Now
\[
A\triangle B=\{x,y\}.
\]
The set \(C\) contains both \(x\) and \(y\), and \(C\subseteq A\cup B\).
Therefore
\[
A\triangle B\subseteq C\subseteq A\cup B,
\]
so \(C\in I(A,B)\).  Since \(C\notin\{A,B\}\), in fact
\[
C\in I^\circ(A,B).
\]
This gives a forbidden pair-link triple \(A,B,C\in\mathcal F\), contradicting
the pair-link-free hypothesis.  Hence each insertion fiber has size at most
one.

Every \(B\in\Gamma_1^{\mathcal F}(A)\) has the unique form
\[
B=(A\setminus\{x\})\cup\{y\}
\]
with \(x\in A\) and \(y\in P\setminus A\).  Grouping such neighbors by the
inserted coordinate \(y\) and applying the fiber bound gives
\[
|\Gamma_1^{\mathcal F}(A)|
=
\sum_{y\in P\setminus A}|D_y^{\mathcal F}(A)|
\le |P\setminus A|.
\]

## Depends on
- [[mrw-3c39ca3d1973]] Pair-link shadow criterion for biased squarefree residuals
- [[mrw-b1f87c9d6a42]] Full rank bands have full genuine pair-link projection
- [[mrw-4f1e9a2d6b73]] Capped random pair-links are overlap-sparse
- [[mrw-6d4a8b0f2c91]] Capped pair-link relations have no positive-mass endpoint core

## Used by

## Notes
- This is a structural constraint on independent sets in the three-uniform
  pair-link hypergraph.  It is not a positive-mass theorem and does not prove
  \(U_k(\theta)\to0\).
- The statement is deliberately one-sided.  Fixing the deleted coordinate
  \(x\) and allowing many inserted coordinates \(y\) does not by itself create
  the same pair-link triple.
- The degree consequence controls only Johnson one-swap neighbors, i.e. same-rank
  neighbors at symmetric difference \(2\).  It does not control the full
  same-rank slice at larger Hamming distance or unequal-rank neighborhoods.
- The next missing bridge is a weighted one-swap expansion theorem: positive
  \(\nu_P\)-mass in a high-support band would need to force many same-insertion
  collisions, or else exhibit a genuine positive-mass family with globally low
  one-swap expansion.
