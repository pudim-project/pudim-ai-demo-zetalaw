---
id: mrw-18e9c7b0a5af
type: proposition
title: Product-square moment kills high-intersection cliques
aliases: ["mrw-18e9c7b0a5af", "High-intersection clique quarantine"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, union-free, pair-link, high-intersection, t-intersecting, product-measure, biased-measure, overlap-graph, cluster-cover, route-kill]
parents: [mrw-7c6a0e9f2d31, mrw-55a8d9eddd2e, mrw-d0402aea6f58, mrw-b4075311abd3, mrw-cc4f876149b7, mrw-3c39ca3d1973, mrw-a92d7b6e4031]
refs: []
  - raw/20260519T225444Z-erdos536-high-intersection-clustering.md
  - references/requests/20260519T225444Z-high-intersection-clique-erudition-gate.md
  - references/sources/20260519T225444Z-high-intersection-clique-context.md
  - theory/forage/requests/20260519T225444Z-erdos536-high-intersection-clustering-request.md
  - theory/forage/responses/20260519T225444Z-erdos536-high-intersection-clustering-response.md
  - raw/20260519T230237Z-scout-forage-ingest.md
  - oracle/requests/20260519T225444Z-erdos536-high-intersection-clique-oracle-request.md
  - oracle/responses/20260519T225444Z-erdos536-high-intersection-clique-oracle-response.md
---

# Proposition: Product-square moment kills high-intersection cliques

## Statement

Let \(P\) be a finite set of primes and let \(\nu_P\) be the product law on
\(2^P\) with
\[
\nu_P(p\in X)=\frac1p.
\]
Put
\[
\Sigma_2(P)=\sum_{p\in P}\frac1{p^2},
\qquad
\Sigma_2=\sum_p\frac1{p^2}.
\]
Then \(\Sigma_2<\infty\).

Let \(t\ge1\).  Suppose that \(\mathcal F\subseteq2^P\) satisfies
\[
|A|\ge t\qquad(A\in\mathcal F)
\tag{1}
\]
and
\[
|A\cap B|\ge t\qquad(A\ne B,\ A,B\in\mathcal F).
\tag{2}
\]
Then
\[
\nu_P(\mathcal F)
\le
\left(\frac{\Sigma_2(P)}{t}\right)^{1/2}
\le
\left(\frac{\Sigma_2}{t}\right)^{1/2}.
\tag{3}
\]

Consequently, for
\[
P_k=\{p_1,\ldots,p_k\},
\qquad
S_k=\sum_{i\le k}\frac1{p_i},
\]
and fixed \(0<\gamma<\theta\), every family
\[
\mathcal F_k\subseteq H_{k,\theta}
=\{A\subseteq P_k:\ |A|>\theta S_k\}
\]
whose distinct members satisfy
\[
|A\cap B|\ge\gamma S_k
\tag{4}
\]
has
\[
\nu_{P_k}(\mathcal F_k)=O_\gamma(S_k^{-1/2})\to0.
\tag{5}
\]

More generally, if \(\mathcal F_k\subseteq H_{k,\theta}\) is covered by
\(m_k\) subfamilies, each internally satisfying (4), then
\[
\nu_{P_k}(\mathcal F_k)
\le
m_k\left(\frac{\Sigma_2}{\lceil\gamma S_k\rceil}\right)^{1/2}.
\tag{6}
\]
In particular, \(\nu_{P_k}(\mathcal F_k)\to0\) whenever
\[
m_k=o(\sqrt{S_k}).
\tag{7}
\]

## Proof

The convergence of \(\Sigma_2\) follows from comparison with the square-summable
integer series:
\[
\sum_p\frac1{p^2}\le \sum_{n\ge2}\frac1{n^2}<\infty.
\]

Let \(X,Y\) be independent \(\nu_P\)-samples.  If \(X,Y\in\mathcal F\), then
\[
|X\cap Y|\ge t.
\]
Indeed, if \(X\ne Y\), this is (2); if \(X=Y\), it is (1).  Therefore
\[
\nu_P(\mathcal F)^2
=
\Pr(X\in\mathcal F,\ Y\in\mathcal F)
\le
\Pr(|X\cap Y|\ge t).
\tag{8}
\]
The coordinates of \(X\cap Y\) are independent indicators with probabilities
\[
\Pr(p\in X\cap Y)=\frac1{p^2}.
\]
Thus
\[
\mathbb E|X\cap Y|
=
\Sigma_2(P).
\tag{9}
\]
Markov's inequality gives
\[
\Pr(|X\cap Y|\ge t)\le \frac{\Sigma_2(P)}{t}.
\tag{10}
\]
Combining (8) and (10) proves (3).

For the high-support corollary, put
\[
t_k=\lceil\gamma S_k\rceil.
\]
Since \(0<\gamma<\theta\), every member of \(H_{k,\theta}\) satisfies
\(|A|\ge t_k\).  Since \(|A\cap B|\) is
integer-valued, (4) implies \(|A\cap B|\ge t_k\).  Applying (3) with
\(P=P_k\) and \(t=t_k\) gives
\[
\nu_{P_k}(\mathcal F_k)
\le
\left(\frac{\Sigma_2}{\lceil\gamma S_k\rceil}\right)^{1/2}
=O_\gamma(S_k^{-1/2}),
\]
which tends to zero because \(S_k\to\infty\).

The cover statement follows by applying the same bound to each internally
\(\gamma S_k\)-intersecting subfamily and summing the resulting measures.

## Consequences

This proposition is the high-overlap companion to the sparse-code quarantine
[[mrw-7c6a0e9f2d31]].  For fixed \(0<\gamma<\theta\), form the overlap graph on
a high-support family by joining \(A\) and \(B\) when
\[
|A\cap B|\ge \gamma S_k.
\]
The private-shadow bound shows that independent sets in this graph have
vanishing \(\nu_{P_k}\)-mass.  The present proposition shows that cliques have
\(O_\gamma(S_k^{-1/2})\) mass, and that covers by \(o(\sqrt{S_k})\) such
cliques also have vanishing mass.

Thus a positive-mass high-support union-free or squarefree pair-link-free
obstruction cannot be explained by either a sparse-intersection code or by one
high-intersection cluster, nor by a bounded or \(o(\sqrt{S_k})\)-sized cover by
such clusters.  The surviving obstruction, if it exists, must have mixed
overlap-graph structure: no positive-mass low-overlap independent part and no
small high-overlap clique cover.

This does not prove the prime-biased weighted union-free theorem
[[mrw-55a8d9eddd2e]].  It sharpens the next target: prove that the mixed
overlap graph forced by [[mrw-7c6a0e9f2d31]] and this proposition yields a union
triple or pair-link hit, or construct a genuine positive-mass counterexample
with many small high-intersection clusters.
