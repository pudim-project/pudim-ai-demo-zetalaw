---
id: mrw-9e0b4f1a5c33
type: proposition
title: Fixed-junta comparable-pair visibility forces vanishing mass
aliases: ["mrw-9e0b4f1a5c33", "Fixed-junta comparable-pair visibility forces vanishing mass"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, union-free, fixed-junta, root-consistency, comparable-pairs, antichain, product-measure, conditional-source, support-tail]
parents: [mrw-1f7c23e5a9d4, mrw-6a9d1e4f2c8b, mrw-55a8d9eddd2e, mrw-d0402aea6f58, mrw-b4075311abd3, mrw-cc4f876149b7, mrw-54968b07a069]
refs: []
  - raw/20260519T153428Z-erdos536-fixed-junta-root-consistency.md
  - references/requests/20260519T153428Z-fixed-junta-root-erudition-gate.md
  - references/sources/20260519T153428Z-fixed-junta-root-context.md
  - theory/forage/requests/20260519T153428Z-erdos536-fixed-junta-root-consistency-request.md
  - theory/forage/responses/20260519T153428Z-erdos536-fixed-junta-root-consistency-response.md
  - raw/20260519T154115Z-scout-forage-ingest.md
  - oracle/requests/20260519T153428Z-erdos536-fixed-junta-root-oracle-request.md
  - oracle/responses/20260519T153428Z-erdos536-fixed-junta-root-oracle-response.md
---

# Proposition: Fixed-junta comparable-pair visibility forces vanishing mass

## Statement

Let
\[
P_k=\{p_1,\ldots,p_k\},\qquad q_i=\frac1{p_i},
\]
and let \(\nu_k\) be the product law on \(2^{P_k}\) with
\[
\nu_k(p_i\in S)=q_i.
\]
Put
\[
V_k=\sum_{i\le k}q_i(1-q_i).
\]
Assume the product-measure antichain estimate
\[
\mu(\mathcal A)
\le
C\left(1+\sum_i r_i(1-r_i)\right)^{-1/2}
\tag{1}
\]
for every antichain \(\mathcal A\) under every Bernoulli product law whose
coordinate probabilities satisfy \(0<r_i\le1/2\), with an absolute constant
\(C\).

Fix a finite set \(J\) of prime coordinates.  Suppose that, for each \(k\),
\(\mathcal F_k\subseteq2^{P_k}\) satisfies the fixed-junta comparable-pair
visibility condition
\[
A,C\in\mathcal F_k,\qquad A\subsetneq C
\quad\Longrightarrow\quad
(C\setminus A)\cap J\ne\varnothing.
\tag{2}
\]
Then
\[
\nu_k(\mathcal F_k)
\le
2^{|J\cap P_k|}C(1+V_k)^{-1/2}
\le
2^{|J|}C(1+V_k)^{-1/2}.
\tag{3}
\]
In particular, for fixed finite \(J\),
\[
\nu_k(\mathcal F_k)\to0.
\]
The same conclusion holds after intersecting \(\mathcal F_k\) with any
high-support event \(H_{k,\theta}=\{S:|S|>\theta\sum_{i\le k}q_i\}\).

Consequently, a positive-mass prime-biased high-support obstruction to
[[mrw-55a8d9eddd2e]] cannot have the property that every comparable-pair deletion
hits one fixed finite root or junta.

## Proof

For \(U\subseteq J\cap P_k\), define the \(J\)-trace class
\[
\mathcal F_{k,U}
=
\{S\in\mathcal F_k:S\cap J=U\}.
\]
Each \(\mathcal F_{k,U}\) is an antichain.  Indeed, if
\[
A,C\in\mathcal F_{k,U},
\qquad
A\subsetneq C,
\]
then \(A\) and \(C\) have the same trace on \(J\).  Hence
\[
(C\setminus A)\cap J=\varnothing,
\]
contradicting the visibility condition (2).

Apply the product-measure antichain estimate (1) to each antichain
\(\mathcal F_{k,U}\) under the full product law \(\nu_k\).  Since all prime
coordinate probabilities satisfy \(0<q_i\le1/2\), this gives
\[
\nu_k(\mathcal F_{k,U})
\le
C(1+V_k)^{-1/2}.
\]
There are \(2^{|J\cap P_k|}\) possible traces, so summing over trace classes gives
\[
\nu_k(\mathcal F_k)
=
\sum_{U\subseteq J\cap P_k}\nu_k(\mathcal F_{k,U})
\le
2^{|J\cap P_k|}C(1+V_k)^{-1/2},
\]
which is (3).

Finally,
\[
V_k
=
\sum_{i\le k}\frac1{p_i}\left(1-\frac1{p_i}\right)
=
\sum_{i\le k}\frac1{p_i}-\sum_{i\le k}\frac1{p_i^2}
\to\infty,
\]
because \(\sum_p1/p=\infty\) and \(\sum_p1/p^2<\infty\).  Hence the right-hand
side of (3) tends to \(0\) for fixed finite \(J\).  Intersecting with
\(H_{k,\theta}\) can only decrease the measure.

## Depends on

- [[mrw-1f7c23e5a9d4]] Finite-junta deletion traces obstruct trace-local rooted
  estimates
- [[mrw-6a9d1e4f2c8b]] Star deletion traces obstruct trace-local
  growing-deletion estimates
- [[mrw-54968b07a069]] Product-measure antichain bounds kill max-fiber skeletons
- [[mrw-55a8d9eddd2e]] Prime-biased weighted union-free theorem
- [[mrw-d0402aea6f58]] Biased lower-shadow union-cover problem for Erdos 536
- [[mrw-b4075311abd3]] Union-free reformulation of the biased lower-shadow route
- [[mrw-cc4f876149b7]] Intersecting deletion-trace obstruction for lower-shadow
  union covers

## Used by

- Next #536 route: any positive-mass high-support union-free counterexample must
  have roots or visibility coordinates escaping every fixed finite \(J\), or must
  realize comparable-pair deletions that are not forced to hit a fixed junta.

## Notes

- This result globalizes, but does not contradict, the trace-local obstruction in
  [[mrw-1f7c23e5a9d4]].  Fixed finite-junta deletion traces can have positive
  trace-local deletion mass, but they cannot be imposed coherently on all
  comparable pairs of a positive-mass family when \(J\) is fixed.
- The theorem does not prove \(U_k(\theta)\to0\).  Union-freeness gives
  pairwise-intersecting deletion traces below each top set; it does not imply the
  stronger fixed-junta visibility condition (2).
- For \(J=\varnothing\), condition (2) says that \(\mathcal F_k\) has no proper
  comparable pair, so the proposition reduces to the antichain estimate itself.
- For growing \(J=J_k\), the displayed trace-sum bound gives decay only when
  \(2^{|J_k|}=o(\sqrt{V_k})\).  A conditional proof through outside-coordinate
  variance can still work if
  \[
  \sum_{p_i\notin J_k}q_i(1-q_i)\to\infty,
  \]
  but the fixed-junta conclusion is false when \(J_k=P_k\), where the visibility
  condition is vacuous.
