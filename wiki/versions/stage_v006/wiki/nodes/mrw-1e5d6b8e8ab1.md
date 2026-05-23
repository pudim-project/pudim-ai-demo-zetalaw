---
id: mrw-1e5d6b8e8ab1
type: proposition
title: Product endpoint size polynomials control shifted-window residuals
aliases: ["mrw-1e5d6b8e8ab1", "Product endpoint size polynomials control shifted-window residuals"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, endpoint-tower, iterated-tower, product-closure, interval-shield, endpoint-polynomial, shifted-window, terminal-residual, variational-residual, support-tail, cross-core-coherence]
parents: [mrw-cd7b1fe1d9af, mrw-3d6bb8271a4c, mrw-20ca89f696f2]
refs: []
  - raw/20260522T024942Z-erdos-536-product-tower-endpoint-factor-envelope.md
  - raw/20260522T024942Z-erdos536-product-tower-endpoint-factor-envelope.md
  - raw/20260522T030334Z-scout-forage-ingest.md
  - theory/forage/requests/20260522T024942Z-erdos536-product-tower-endpoint-factor-envelope-request.md
  - theory/forage/responses/20260522T024942Z-erdos536-product-tower-endpoint-factor-envelope-response.md
---

# Proposition: Product endpoint size polynomials control shifted-window residuals

## Statement

Let
\[
B=B_1\sqcup\cdots\sqcup B_r
\]
be a finite disjoint endpoint decomposition with product law, and let each
\(\mathcal E_j\subseteq2^{B_j}\) be interval-shielded.  Define the endpoint
size polynomial
\[
G_j(z)=\sum_{e\in\mathcal E_j}\pi_{B_j}(e)z^{|e|}.
\]
Let
\[
\mathcal E_\otimes
=
\{e_1\sqcup\cdots\sqcup e_r:\ e_j\in\mathcal E_j\}
\]
and write
\[
G_\otimes(z)=\prod_{j=1}^rG_j(z)=\sum_{s=0}^K\Gamma_s z^s,
\]
where \(K\) is the maximum total endpoint size in the product support.
Then the exact product-tower residual is
\[
\mathcal R_\otimes(L)
=
\sum_{s=0}^K\Gamma_s\,\mathfrak M_T(L-s).
\]

Consequently, if a finite terminal shift profile satisfies
\[
\mathfrak M_T(L-s)\le\lambda_s(L)\mathfrak M_T(L)
\qquad(0\le s\le K),
\]
then
\[
\mathcal R_\otimes(L)
\le
\mathfrak M_T(L)\sum_{s=0}^K\Gamma_s\lambda_s(L).
\]
In particular, if
\[
\mathfrak M_T(L-s)\le \lambda^s\mathfrak M_T(L)
\qquad(0\le s\le K),
\]
then
\[
\mathcal R_\otimes(L)
\le
\mathfrak M_T(L)\prod_{j=1}^rG_j(\lambda).
\]

If each \(\mathcal E_j\) is \(k_j\)-uniform, with
\[
\Gamma_j=G_j(1),
\qquad
K=\sum_{j=1}^rk_j,
\]
then
\[
\mathcal R_\otimes(L)
=
\left(\prod_{j=1}^r\Gamma_j\right)\mathfrak M_T(L-K),
\]
and the scalar shift bound gives
\[
\mathcal R_\otimes(L)
\le
\lambda^K\left(\prod_{j=1}^r\Gamma_j\right)\mathfrak M_T(L).
\]

Finally, if \(\mathfrak M_T(L)>0\) eventually and
\[
\frac{\mathfrak M_T(L-s)}{\mathfrak M_T(L)}\to1
\qquad\text{for every fixed }0\le s\le K,
\]
then
\[
\frac{\mathcal R_\otimes(L)}{\mathfrak M_T(L)}
\to
G_\otimes(1)
=
\prod_{j=1}^rG_j(1).
\]
Thus fixed finite product towers are terminally neutral under shift-stable
terminal residual profiles; any decay must come from a genuine shifted-window
bound or from mass outside the exact product tower.

## Proof

By `mrw-cd7b1fe1d9af`, the product family \(\mathcal E_\otimes\) is
interval-shielded, and its exact supported residual is
\[
\sum_{(e_1,\ldots,e_r)}
\left(\prod_{j=1}^r\pi_{B_j}(e_j)\right)
\mathfrak M_T\!\left(L-\sum_{j=1}^r|e_j|\right).
\]
Group the summands by
\[
s=\sum_{j=1}^r|e_j|.
\]
The coefficient of \(\mathfrak M_T(L-s)\) is exactly
\[
\Gamma_s
=
\sum_{\substack{(e_1,\ldots,e_r)\\ \sum_j|e_j|=s}}
\prod_{j=1}^r\pi_{B_j}(e_j),
\]
which is the coefficient of \(z^s\) in
\[
\prod_{j=1}^r
\left(\sum_{e\in\mathcal E_j}\pi_{B_j}(e)z^{|e|}\right)
=
\prod_{j=1}^rG_j(z).
\]
This proves the exact polynomial residual identity.

The finite shift-profile inequality follows by multiplying each nonnegative
coefficient \(\Gamma_s\) by the assumed bound for
\(\mathfrak M_T(L-s)\).  The scalar case is the specialization
\(\lambda_s(L)=\lambda^s\), giving
\[
\sum_s\Gamma_s\lambda^s=G_\otimes(\lambda)=\prod_jG_j(\lambda).
\]

If \(\mathcal E_j\) is \(k_j\)-uniform, then every product pattern has total
endpoint size \(K=\sum_jk_j\).  Hence only \(\Gamma_K\) appears, and
\[
\Gamma_K
=
\prod_{j=1}^r\sum_{e\in\mathcal E_j}\pi_{B_j}(e)
=
\prod_{j=1}^r\Gamma_j.
\]

For the shift-stable case, divide the exact finite sum by
\(\mathfrak M_T(L)\).  Since \(K\) is fixed and finite, termwise convergence
gives
\[
\frac{\mathcal R_\otimes(L)}{\mathfrak M_T(L)}
=
\sum_{s=0}^K
\Gamma_s
\frac{\mathfrak M_T(L-s)}{\mathfrak M_T(L)}
\to
\sum_{s=0}^K\Gamma_s
=
G_\otimes(1)
=
\prod_jG_j(1).
\]

## Depends on

- [[mrw-cd7b1fe1d9af]] Products of interval-shielded endpoint families give exact tower residuals
- [[mrw-3d6bb8271a4c]] Interval-shielded endpoint mixtures reduce to endpoint variational residuals
- [[mrw-20ca89f696f2]] Cross-pattern pair-link intervals factor by endpoint and terminal cores

## Used by

## Notes

- The endpoint size polynomial is a bookkeeping device for finite product
  towers; it adds no terminal estimate by itself.
- The normalized shift-stable conclusion assumes \(\mathfrak M_T(L)>0\)
  eventually.  If the denominator vanishes, use the absolute shift-profile
  inequalities instead.
- This proposition identifies the exact missing ingredient: a nontrivial
  bound on the finite shifted-window profile
  \(\mathfrak M_T(L-s)/\mathfrak M_T(L)\), especially when total tower size
  grows.
