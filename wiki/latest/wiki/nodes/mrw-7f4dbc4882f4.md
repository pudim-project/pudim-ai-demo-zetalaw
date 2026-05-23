---
id: mrw-7f4dbc4882f4
type: proposition
title: Product towers absorb into degraded terminal thresholds
aliases: ["mrw-7f4dbc4882f4", "Product towers absorb into degraded terminal thresholds"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, endpoint-tower, product-closure, shifted-window, threshold-degradation, terminal-residual, support-tail, cross-core-coherence]
parents: [mrw-1e5d6b8e8ab1, mrw-474262d39b1d, mrw-cd7b1fe1d9af, mrw-20ca89f696f2]
refs: []
  - raw/20260522T040948Z-erdos-536-threshold-degraded-product-towers.md
  - raw/20260522T040948Z-erdos536-threshold-degraded-product-towers.md
  - raw/20260522T041923Z-scout-forage-ingest.md
  - theory/forage/requests/20260522T040948Z-erdos536-threshold-degraded-product-towers-request.md
  - theory/forage/responses/20260522T040948Z-erdos536-threshold-degraded-product-towers-response.md
  - oracle/requests/20260522T040948Z-erdos536-threshold-degraded-product-towers-oracle-request.md
  - oracle/responses/20260522T040948Z-erdos536-threshold-degraded-product-towers-oracle-response.md
---

# Proposition: Product towers absorb into degraded terminal thresholds

## Statement

Let \(P=B\sqcup T\) be a finite disjoint decomposition with product law, and
write
\[
\mu_X=\sum_{x\in X}q_x
\]
for the expected support size on a coordinate set \(X\).  Assume \(\mu_T>0\).
Let \(0\le\theta<1\), put
\[
L=\theta\mu_P=\theta(\mu_B+\mu_T),
\]
and suppose a finite endpoint product-tower residual has the exact polynomial
form
\[
\mathcal R_\otimes(L)
=
\sum_{s=0}^K\Gamma_s\,\mathfrak M_T(L-s),
\]
where \(\Gamma_s\ge0\) and \(\Gamma_s=0\) for \(s>K\).

Define the algebraic effective terminal threshold by
\[
\theta_K\mu_T
=
\theta\mu_T+\theta\mu_B-K
=
L-K,
\qquad\text{equivalently}\qquad
\theta_K=\theta+\frac{\theta\mu_B-K}{\mu_T}.
\]
Then
\[
\mathcal R_\otimes(\theta\mu_P)
\le
G(1)\,\mathfrak M_T(\theta_K\mu_T),
\qquad
G(1)=\sum_{s=0}^K\Gamma_s.
\]

Moreover, for any real \(\theta'<\theta\), and in particular for any
\(0\le\theta'<\theta\), if
\[
K-\theta\mu_B\le(\theta-\theta')\mu_T,
\]
then
\[
\mathcal R_\otimes(\theta\mu_P)
\le
G(1)\,\mathfrak M_T(\theta'\mu_T).
\]
Consequently, if \(K\) and \(\mu_B\) are bounded while \(\mu_T\to\infty\),
then for every fixed \(0\le\theta'<\theta\) the degraded-threshold bound
\[
\mathcal R_\otimes(\theta\mu_P)
\le
G(1)\,\mathfrak M_T(\theta'\mu_T)
\]
holds eventually.  More generally it holds whenever
\[
K-\theta\mu_B=o(\mu_T)
\]
after replacing \(\theta'\) by any fixed smaller parameter.

## Proof

For every \(s\le K\),
\[
L-s
=
\theta(\mu_B+\mu_T)-s
\ge
\theta(\mu_B+\mu_T)-K
=
\theta_K\mu_T.
\]
The residual function \(\mathfrak M_T(a)\) is monotone nonincreasing in the
threshold \(a\): if \(a\ge b\), then
\[
\{R\subseteq T:|R|>a\}\subseteq\{R\subseteq T:|R|>b\},
\]
so the supremum over pair-link-free families in the first high-support event
is at most the supremum over the second.  Therefore
\[
\mathfrak M_T(L-s)\le \mathfrak M_T(\theta_K\mu_T)
\qquad(0\le s\le K).
\]
Multiplying by \(\Gamma_s\ge0\) and summing gives
\[
\mathcal R_\otimes(L)
=
\sum_{s=0}^K\Gamma_s\mathfrak M_T(L-s)
\le
\left(\sum_{s=0}^K\Gamma_s\right)\mathfrak M_T(\theta_K\mu_T)
=
G(1)\mathfrak M_T(\theta_K\mu_T).
\]

If
\[
K-\theta\mu_B\le(\theta-\theta')\mu_T,
\]
then
\[
\theta_K\mu_T
=
\theta\mu_T+\theta\mu_B-K
\ge
\theta'\mu_T.
\]
Applying the same monotonicity once more gives
\[
\mathfrak M_T(\theta_K\mu_T)\le\mathfrak M_T(\theta'\mu_T),
\]
and hence the degraded-threshold bound.  The bounded-\(K\), bounded-\(\mu_B\)
case follows because \((\theta-\theta')\mu_T\to\infty\) for every fixed
\(\theta'<\theta\).

## Depends on

- [[mrw-1e5d6b8e8ab1]] Product endpoint size polynomials control shifted-window residuals
- [[mrw-474262d39b1d]] Terminal residuals have unbounded finite-shift ratios
- [[mrw-cd7b1fe1d9af]] Products of interval-shielded endpoint families give exact tower residuals
- [[mrw-20ca89f696f2]] Cross-pattern pair-link intervals factor by endpoint and terminal cores

## Used by

## Notes

- This is a threshold-degraded absorption lemma, not a decay theorem.  It does
  not compare \(\mathfrak M_T(\theta\mu_T-K)\) to
  \(\mathfrak M_T(\theta\mu_T)\), and it does not prove terminal decay without
  an independent theorem at the lower parameter \(\theta'\).
- The parameter \(\theta_K\) is algebraic and need not lie in \([0,1)\).  The
  displayed inequalities remain valid as long as \(\mathfrak M_T(a)\) is
  interpreted for real thresholds \(a\).
- The result avoids the obstruction in [[mrw-474262d39b1d]] because it uses
  slack \((\theta-\theta')\mu_T\) from the high-support scaling.  It would not
  justify taking \(\theta'=\theta\), and it gives no control when the endpoint
  size \(K\) is comparable to or larger than the available threshold slack.
- For fixed finite product towers at any positive \(\theta\), this proposition
  shows that the branch is self-similar: if the prime-biased terminal residual
  theorem is eventually proved for every \(0\le\theta'<1\), then fixed endpoint
  products contribute no separate obstruction.
