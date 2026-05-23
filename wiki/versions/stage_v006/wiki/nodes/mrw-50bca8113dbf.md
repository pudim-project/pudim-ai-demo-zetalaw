---
id: mrw-50bca8113dbf
type: corollary
title: Bipartite endpoint pair shields are one-from-each subtower residuals
aliases: ["mrw-50bca8113dbf", "Bipartite endpoint pair shields are one-from-each subtower residuals"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, bipartite-graph, endpoint-pairs, interval-shield, one-from-each, subtower, terminal-residual, variational-residual, support-tail, cross-core-coherence]
parents: [mrw-1b04240e9886, mrw-d7b3299d3813, mrw-b52df00c958c, mrw-23227179a350]
refs: []
  - raw/20260521T222219Z-erdos-536-bipartite-subtower-reduction.md
  - raw/20260521T222219Z-erdos536-bipartite-subtower-reduction.md
  - theory/forage/requests/20260521T222219Z-erdos536-bipartite-subtower-reduction-request.md
  - theory/forage/responses/20260521T222219Z-erdos536-bipartite-subtower-reduction-response.md
  - oracle/requests/20260521T222219Z-erdos536-bipartite-subtower-reduction-oracle-request.md
  - oracle/responses/20260521T222219Z-erdos536-bipartite-subtower-reduction-oracle-response.md
---

# Corollary: Bipartite endpoint pair shields are one-from-each subtower residuals

## Statement

Let
\[
P=T\sqcup X\sqcup Y
\]
be a finite disjoint decomposition with \(X,Y\ne\varnothing\), and let
\(\nu_P=\nu_T\otimes\nu_X\otimes\nu_Y\) be a product law with coordinate
probabilities \(q_p\in(0,1)\).  For \(x\in X\) and \(y\in Y\), put
\[
\alpha_x=q_x\prod_{u\in X\setminus\{x\}}(1-q_u),
\qquad
\beta_y=q_y\prod_{v\in Y\setminus\{y\}}(1-q_v),
\]
and
\[
\alpha_X=\sum_{x\in X}\alpha_x,
\qquad
\beta_Y=\sum_{y\in Y}\beta_y.
\]

Let \(G\subseteq X\times Y\) be a simple bipartite endpoint graph.  Among all
families
\[
\mathcal F
=
\bigcup_{xy\in E(G)}
\{\{x,y\}\cup R:R\in\mathcal R_{xy}\},
\qquad
\mathcal R_{xy}\subseteq2^T,
\]
that are pair-link-free in \(2^P\), define the supported high-support optimum
\[
\mathcal R_G(L)
:=
\sup_{\mathcal F}
\nu_P(\mathcal F\cap\{S:|S|>L\}).
\]
Then
\[
\mathcal R_G(L)
=
\left(\sum_{xy\in E(G)}\alpha_x\beta_y\right)\mathfrak M_T(L-2),
\]
where \(\mathfrak M_T(U)\) is the terminal pair-link-free residual at cutoff
\(U\).  In particular,
\[
\mathcal R_G(L)
\le
\alpha_X\beta_Y\,\mathfrak M_T(L-2),
\]
with equality in the endpoint factor when \(G=K_{X,Y}\).  Since
\(\alpha_x\beta_y>0\) for all \(x,y\), endpoint-factor equality occurs only
for \(G=K_{X,Y}\); the residual values may also be equal in degenerate cases
where \(\mathfrak M_T(L-2)=0\).

Consequently, the complete bipartite endpoint-pair shield is exactly the
\(r=1\) endpoint tower from `mrw-b52df00c958c`, with terminal core \(T\),
endpoint classes \(X,Y\), and endpoint factor
\[
\Gamma_1=\alpha_X\beta_Y.
\]
The balanced complete-bipartite diffuse example in `mrw-1b04240e9886` is
therefore not a new endpoint-shield branch: it is precisely the already
audited one-from-each endpoint-tower residual.

For a non-complete bipartite graph \(G\), the same model is a subtower, or
equivalently the full \(r=1\) endpoint tower with empty terminal fibers on
nonedges.

## Proof

If \(E(G)=\varnothing\), then the only supported family is empty and
\(\mathcal R_G(L)=0\), which is the displayed formula.  Assume now that
\(E(G)\ne\varnothing\).

The family \(\mathcal F\) is a one-from-each two-class assembly supported on
the endpoint pairs \(xy\in E(G)\).  To apply `mrw-d7b3299d3813` verbatim,
extend the fibers to all pairs in \(X\times Y\) by setting
\[
\mathcal R_{xy}=\varnothing
\qquad(xy\notin E(G)).
\]
Then `mrw-d7b3299d3813` says that \(\mathcal F\) is pair-link-free if and only
if every terminal fiber \(\mathcal R_{xy}\) is pair-link-free in \(2^T\).
Moreover,
\[
\nu_P(\mathcal F\cap\{S:|S|>L\})
=
\sum_{xy\in E(G)}
\alpha_x\beta_y\,
\nu_T(\mathcal R_{xy}\cap\{R:|R|>L-2\}).
\]
For each allowed edge \(xy\), the terminal slice is bounded by
\(\mathfrak M_T(L-2)\).  Thus
\[
\nu_P(\mathcal F\cap\{S:|S|>L\})
\le
\left(\sum_{xy\in E(G)}\alpha_x\beta_y\right)\mathfrak M_T(L-2).
\]

For the reverse inequality, take a terminal pair-link-free extremizer
\(\mathcal R^*\subseteq2^T\) for \(\mathfrak M_T(L-2)\), or an
\(\varepsilon\)-extremizer and let \(\varepsilon\downarrow0\).  Set
\[
\mathcal R_{xy}=\mathcal R^*
\qquad(xy\in E(G)).
\]
The endpoint-pair decoupling theorem again shows that the resulting
\(\mathcal F\) is pair-link-free, and the displayed measure identity attains
the upper bound.  This proves the exact formula for \(\mathcal R_G(L)\).

The inequality follows from
\[
\sum_{xy\in E(G)}\alpha_x\beta_y
\le
\sum_{x\in X}\sum_{y\in Y}\alpha_x\beta_y
=
\alpha_X\beta_Y,
\]
with endpoint-factor equality when \(G=K_{X,Y}\), and only then because all
\(\alpha_x\beta_y\) are positive.  For \(G=K_{X,Y}\), the endpoint patterns
are all pairs \(\{x,y\}\) with one point from \(X\) and one point from \(Y\).
This is exactly the full \(r=1\) endpoint tower in `mrw-b52df00c958c`; its
endpoint factor is \(\Gamma_1=\alpha_X\beta_Y\) and its terminal residual is
\(\mathfrak M_T(L-2)\).  If \(G\ne K_{X,Y}\), the same representation is the
full tower with empty fibers on nonedges.  This proves the claimed tower and
subtower identification.

Finally, in the balanced complete-bipartite construction of
`mrw-1b04240e9886`, \(q_b=\alpha/(2m)\) on each side and \(|X|=|Y|=m\), so
\[
\alpha_X
=
m\frac{\alpha}{2m}
\left(1-\frac{\alpha}{2m}\right)^{m-1}
\to
\frac{\alpha}{2}e^{-\alpha/2},
\]
and the same limit holds for \(\beta_Y\).  Hence
\[
\Gamma_1=\alpha_X\beta_Y\to e^{-\alpha}\frac{\alpha^2}{4},
\]
the same mass computed in `mrw-1b04240e9886`.  Thus that positive diffuse
bipartite shield is exactly the one-from-each tower factor.

## Depends on

- [[mrw-1b04240e9886]] Triangle-free endpoint pair shields carry positive diffuse residuals
- [[mrw-d7b3299d3813]] One-from-each two-class assemblies decouple by endpoint pair
- [[mrw-b52df00c958c]] Iterated endpoint-fiber towers have exact terminal residual value
- [[mrw-23227179a350]] Zero-Xi exact occupancy alternatives are endpoint-fiber towers

## Used by

## Notes

- This corollary quarantines the complete bipartite endpoint-pair obstruction
  from `mrw-1b04240e9886`: it is not new structure, but the previously audited
  exact one-from-each endpoint tower.
- The result also handles non-complete bipartite endpoint-pair shields as
  sub-towers dominated by the full one-from-each endpoint factor.
- It does not bound non-bipartite triangle-free endpoint-pair shields, such as
  blow-ups of odd cycles.  That is the next two-uniform shielded branch after
  the bipartite subtower reduction.
- No \(M_{P_k}(\theta)\), \(U_k(\theta)\), or \(R_P(\theta)\) theorem follows
  from this corollary without a terminal-core residual estimate.
