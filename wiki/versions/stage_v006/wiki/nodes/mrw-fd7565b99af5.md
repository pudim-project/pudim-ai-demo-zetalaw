---
id: mrw-fd7565b99af5
type: proposition
title: k-partite k-uniform endpoint shields have exact shifted residuals
aliases: ["mrw-fd7565b99af5", "k-partite k-uniform endpoint shields have exact shifted residuals"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, occupancy-pattern, interval-shield, k-uniform, multipartite, transversal, diffuse-limit, terminal-residual, variational-residual, support-tail, higher-uniformity, cross-core-coherence]
parents: [mrw-3d6bb8271a4c, mrw-20ca89f696f2, mrw-1e4b87d9862b, mrw-d602b51accb8]
refs: []
  - raw/20260522T012941Z-erdos-536-kpartite-kuniform-endpoint-shields.md
  - raw/20260522T012941Z-erdos536-kpartite-kuniform-endpoint-shields.md
  - theory/forage/requests/20260522T012941Z-erdos536-kpartite-kuniform-endpoint-shields-request.md
  - theory/forage/responses/20260522T012941Z-erdos536-kpartite-kuniform-endpoint-shields-response.md
  - oracle/requests/20260522T012941Z-erdos536-kpartite-kuniform-endpoint-shields-oracle-request.md
  - oracle/responses/20260522T012941Z-erdos536-kpartite-kuniform-endpoint-shields-oracle-response.md
---

# Proposition: k-partite k-uniform endpoint shields have exact shifted residuals

## Statement

Let \(k\ge1\), and let
\[
B=X_1\sqcup\cdots\sqcup X_k
\]
be a finite disjoint endpoint coordinate set with independent product weights
\(0<q_b<1\).  Let
\[
H\subseteq X_1\times\cdots\times X_k
\]
be any \(k\)-partite \(k\)-uniform transversal hypergraph, and define
\[
\mathcal E(H)
=
\bigl\{\{x_1,\ldots,x_k\}:(x_1,\ldots,x_k)\in E(H)\bigr\}
\subseteq2^B.
\]
Then \(\mathcal E(H)\) is interval-shielded.  Consequently, for every
terminal core \(T\) disjoint from \(B\), its exact supported high-support
residual is
\[
\mathcal R_H(L)
=
\sum_{e\in\mathcal E(H)}\pi_B(e)\,\mathfrak M_T(L-k).
\]

In the complete \(k\)-partite case \(H=K_{X_1,\ldots,X_k}\), put
\[
a_i
=
\sum_{x\in X_i}q_x\prod_{u\in X_i\setminus\{x\}}(1-q_u),
\qquad 1\le i\le k.
\]
Then
\[
\mathcal R_{X_1,\ldots,X_k}(L)
=
\left(\prod_{i=1}^k a_i\right)\mathfrak M_T(L-k).
\]
For balanced diffuse weights \(|X_i|=m\), \(q_b=\alpha/(km)\), and
\(m\to\infty\), the endpoint factor satisfies
\[
\prod_{i=1}^k a_i
\to
e^{-\alpha}\frac{\alpha^k}{k^k}.
\]

This generalizes the singleton, complete bipartite, and tripartite endpoint
branches.  It remains a self-similar residual theorem: it passes the hard part
to the terminal core with cutoff shifted by \(k\), and it gives no terminal
\(R_P(\theta)\) lift by itself.

## Proof

Let \(e_1,e_2\in\mathcal E(H)\) be distinct.  Then there is a part \(X_i\) in
which their selected coordinates differ; write these two coordinates as
\(x_i\ne x_i'\).  Hence
\[
\{x_i,x_i'\}\subseteq e_1\triangle e_2.
\]
Every endpoint set \(e_3\in I_B(e_1,e_2)\) contains the symmetric difference
\(e_1\triangle e_2\).  Therefore it contains both \(x_i\) and \(x_i'\), two
points from the same part \(X_i\).  But every member of \(\mathcal E(H)\)
contains exactly one point from each \(X_i\).  Thus no nonconstant interval
witness \(e_3\in\mathcal E(H)\cap I_B(e_1,e_2)\) exists.  The only endpoint
interval triples inside \(\mathcal E(H)\) are the constant ones, so
\(\mathcal E(H)\) is interval-shielded.

The exact residual formula follows directly from `mrw-3d6bb8271a4c`, since
every endpoint pattern in \(\mathcal E(H)\) has cardinality \(k\).

For \(H=K_{X_1,\ldots,X_k}\), the product probability of selecting exactly
\(\{x_1,\ldots,x_k\}\) and no other endpoint coordinate factors over the
disjoint parts.  Summing over all \(x_i\in X_i\) gives
\[
\sum_{x_1,\ldots,x_k}\pi_B(\{x_1,\ldots,x_k\})
=
\prod_{i=1}^k a_i.
\]
Finally, in the balanced diffuse case,
\[
a_i
=
m\frac{\alpha}{km}
\left(1-\frac{\alpha}{km}\right)^{m-1}
\to
\frac{\alpha}{k}e^{-\alpha/k}
\]
for every \(i\).  Multiplying these \(k\) identical limits gives
\[
\prod_{i=1}^k a_i
\to
\left(\frac{\alpha}{k}e^{-\alpha/k}\right)^k
=
e^{-\alpha}\frac{\alpha^k}{k^k}.
\]

## Depends on

- [[mrw-3d6bb8271a4c]] Interval-shielded endpoint mixtures reduce to endpoint variational residuals
- [[mrw-20ca89f696f2]] Cross-pattern pair-link intervals factor by endpoint and terminal cores
- [[mrw-1e4b87d9862b]] Tripartite 3-uniform endpoint shields carry positive diffuse residuals
- [[mrw-d602b51accb8]] Triangle-free endpoint pair shields obey the fractional bipartite envelope

## Used by

## Notes

- For \(k=1\), this recovers the singleton endpoint residual.  For \(k=2\),
  the complete case recovers the complete bipartite one-from-each residual.
  For \(k=3\), it recovers and generalizes `mrw-1e4b87d9862b`.
- The proof uses only the endpoint interval definition and the transversal
  one-from-each condition; no external hypergraph extremal theorem is needed.
- The diffuse factor \(e^{-\alpha}\alpha^k/k^k\) is positive for every fixed
  \(k\), so endpoint-profile mass alone cannot produce terminal decay.
- The next live target is to compare these shifted windows across \(k\), or to
  prove terminal-core residual decay/cross-fiber exclusions that are invisible
  to interval-shielded endpoint support.
