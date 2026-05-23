---
id: mrw-cd7b1fe1d9af
type: proposition
title: Products of interval-shielded endpoint families give exact tower residuals
aliases: ["mrw-cd7b1fe1d9af", "Products of interval-shielded endpoint families give exact tower residuals"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, endpoint-tower, iterated-tower, product-closure, interval-shield, multipartite, transversal, diffuse-limit, terminal-residual, variational-residual, support-tail, higher-uniformity, cross-core-coherence]
parents: [mrw-3d6bb8271a4c, mrw-20ca89f696f2, mrw-fd7565b99af5]
refs: []
  - raw/20260522T020942Z-erdos-536-iterated-multipartite-endpoint-towers.md
  - raw/20260522T020942Z-erdos536-iterated-multipartite-endpoint-towers.md
  - raw/20260522T021719Z-scout-forage-ingest.md
  - theory/forage/requests/20260522T020942Z-erdos536-iterated-multipartite-endpoint-towers-request.md
  - theory/forage/responses/20260522T020942Z-erdos536-iterated-multipartite-endpoint-towers-response.md
  - oracle/requests/20260522T020942Z-erdos536-iterated-multipartite-endpoint-towers-oracle-request.md
  - oracle/responses/20260522T020942Z-erdos536-iterated-multipartite-endpoint-towers-oracle-response.md
---

# Proposition: Products of interval-shielded endpoint families give exact tower residuals

## Statement

Let
\[
B=B_1\sqcup\cdots\sqcup B_r
\]
be a finite disjoint endpoint decomposition with product law.  For each
\(j\), let \(\mathcal E_j\subseteq2^{B_j}\) be interval-shielded.  Define
\[
\mathcal E_\otimes
=
\{e_1\sqcup\cdots\sqcup e_r:\ e_j\in\mathcal E_j\text{ for all }j\}
\subseteq2^B.
\]
Then \(\mathcal E_\otimes\) is interval-shielded.

Consequently, for every terminal core \(T\) disjoint from \(B\), the exact
supported high-support residual is
\[
\mathcal R_\otimes(L)
=
\sum_{(e_1,\ldots,e_r)\in\mathcal E_1\times\cdots\times\mathcal E_r}
\left(\prod_{j=1}^r\pi_{B_j}(e_j)\right)
\mathfrak M_T\!\left(L-\sum_{j=1}^r|e_j|\right).
\]

If each \(\mathcal E_j\) is \(k_j\)-uniform and
\[
\Gamma_j=\sum_{e\in\mathcal E_j}\pi_{B_j}(e),
\qquad
K=\sum_{j=1}^r k_j,
\]
then this reduces to the exact tower residual
\[
\mathcal R_\otimes(L)
=
\left(\prod_{j=1}^r\Gamma_j\right)\mathfrak M_T(L-K).
\]

In particular, if each \(\mathcal E_j\) is the complete \(k_j\)-partite
transversal support on
\[
B_j=X_{j,1}\sqcup\cdots\sqcup X_{j,k_j},
\]
then
\[
\Gamma_j=\prod_{i=1}^{k_j}a_{j,i},
\qquad
a_{j,i}
=
\sum_{x\in X_{j,i}}q_x
\prod_{u\in X_{j,i}\setminus\{x\}}(1-q_u).
\]
For fixed finite \(r\) and fixed \(k_j\), under balanced diffuse weights at
level \(j\), with
\(|X_{j,i}|=m_j\), \(q_x=\alpha_j/(k_jm_j)\), and \(m_j\to\infty\), the
endpoint factor tends to
\[
\prod_{j=1}^r
e^{-\alpha_j}\frac{\alpha_j^{k_j}}{k_j^{k_j}}
=
e^{-\sum_j\alpha_j}
\prod_{j=1}^r\frac{\alpha_j^{k_j}}{k_j^{k_j}}.
\]

Thus every finite product of interval-shielded endpoint supports, and in
particular every finite product of complete multipartite transversal endpoint
supports of fixed uniformities, is an exact shifted terminal residual.  This
is a self-similar shifted-terminal obstruction only; it gives no terminal
decay, no shifted-window contraction, and no \(R_P(\theta)\) lift without
additional control of \(\mathfrak M_T(L-K)\).

## Proof

Take
\[
A_\ell=e_{\ell,1}\sqcup\cdots\sqcup e_{\ell,r}\in\mathcal E_\otimes
\qquad(\ell=1,2,3)
\]
and suppose \(A_3\in I_B(A_1,A_2)\).  Since the endpoint blocks \(B_j\) are
disjoint, interval containment factors over them:
\[
e_{3,j}\in I_{B_j}(e_{1,j},e_{2,j})
\qquad\text{for every }j.
\]
Indeed, this is just the coordinatewise identity for symmetric difference and
union over disjoint blocks:
\[
A_1\triangle A_2
=
\bigsqcup_j(e_{1,j}\triangle e_{2,j}),
\qquad
A_1\cup A_2
=
\bigsqcup_j(e_{1,j}\cup e_{2,j}).
\]
Because \(\mathcal E_j\) is interval-shielded and
\(e_{1,j},e_{2,j},e_{3,j}\in\mathcal E_j\), we get
\[
e_{1,j}=e_{2,j}=e_{3,j}
\]
for every \(j\).  Therefore \(A_1=A_2=A_3\), and
\(\mathcal E_\otimes\) is interval-shielded.

The exact residual formula now follows from `mrw-3d6bb8271a4c`, together with
product measure on disjoint endpoint blocks:
\[
\pi_B(e_1\sqcup\cdots\sqcup e_r)
=
\prod_{j=1}^r\pi_{B_j}(e_j).
\]

If each \(\mathcal E_j\) is \(k_j\)-uniform, then
\[
\sum_j |e_j|=K
\]
for every tuple.  The terminal factor is constant, so the endpoint sum factors:
\[
\sum_{(e_1,\ldots,e_r)}
\prod_j\pi_{B_j}(e_j)
=
\prod_j\sum_{e_j\in\mathcal E_j}\pi_{B_j}(e_j)
=
\prod_j\Gamma_j.
\]

For complete multipartite transversal levels, `mrw-fd7565b99af5` gives
\(\Gamma_j=\prod_i a_{j,i}\) at each level.  In the balanced diffuse
specialization,
\[
a_{j,i}
=
m_j\frac{\alpha_j}{k_jm_j}
\left(1-\frac{\alpha_j}{k_jm_j}\right)^{m_j-1}
\to
\frac{\alpha_j}{k_j}e^{-\alpha_j/k_j}.
\]
Multiplying over \(i\) gives
\[
\Gamma_j\to e^{-\alpha_j}\frac{\alpha_j^{k_j}}{k_j^{k_j}},
\]
and multiplying over \(j\) gives the displayed product limit.

## Depends on

- [[mrw-3d6bb8271a4c]] Interval-shielded endpoint mixtures reduce to endpoint variational residuals
- [[mrw-20ca89f696f2]] Cross-pattern pair-link intervals factor by endpoint and terminal cores
- [[mrw-fd7565b99af5]] k-partite k-uniform endpoint shields have exact shifted residuals

## Used by

## Notes

- This proposition formalizes the iterated endpoint-tower obstruction
  requested after `mrw-fd7565b99af5`.
- It is deliberately a residual identity, not a decay theorem.  It says that
  finite products of shielded endpoint choices stay shielded, so no
  cross-fiber exclusion appears inside the tower.
- The diffuse product limit assumes fixed finite \(r\) and fixed uniformities
  \(k_j\).  Growing tower depth or growing total \(K=\sum_jk_j\) requires a
  separate shifted-window comparison theorem.
- The next route must either compare shifted terminal windows after the total
  tower size \(K\), or prove that positive mass outside such exact product
  towers forces nonconstant endpoint interval triples.
