---
id: mrw-9077aa1c34bc
type: proposition
title: Top-union-free sections have a cover-probability mass cap
aliases: ["mrw-9077aa1c34bc", "Top-union-free sections have a cover-probability mass cap"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, star-assembly, upper-mixed-shadow, terminal-section, top-union-free, product-measure, cover-probability, high-window, terminal-shadow, escaped-mass, residual-obstruction]
parents: [mrw-dda277c43571, mrw-740b9e5c6cff]
refs: []
  - raw/20260523T022551Z-erdos-536-top-union-free-cover-probability-bound.md
  - raw/20260523T022551Z-erdos536-top-union-free-cover-probability-bound.md
  - raw/20260523T022551Z-scout-forage-ingest.md
  - theory/forage/requests/20260523T022551Z-erdos536-top-union-free-cover-probability-bound-request.md
  - theory/forage/responses/20260523T022551Z-erdos536-top-union-free-cover-probability-bound-response.md
  - oracle/requests/20260523T022551Z-erdos536-top-union-free-cover-probability-bound-oracle-request.md
  - oracle/responses/20260523T022551Z-erdos536-top-union-free-cover-probability-bound-oracle-response.md
---

# Proposition: Top-union-free sections have a cover-probability mass cap

## Statement
Let \(U\) be finite and let \(\mu_U\) be the product law on \(2^U\) with
coordinate inclusion probabilities \(q_u\in[0,1]\).  Define the distinct-cover
probability
\[
\operatorname{cov}^{\ne}_U
=
\mu_U^{\otimes2}\{(X,Y):X\cup Y=U,\ X\ne Y\}.
\]
Equivalently,
\[
\operatorname{cov}^{\ne}_U
=
\prod_{u\in U}(2q_u-q_u^2)
-
\left(\prod_{u\in U}q_u\right)^2,
\]
with the empty-product convention.

If \(\mathcal S\subseteq2^U\) is top-union-free on \(U\), meaning there are no
distinct \(X,Y\in\mathcal S\) with \(X\cup Y=U\), then
\[
\mu_U(\mathcal S)^2
\le
1-\operatorname{cov}^{\ne}_U,
\]
and hence
\[
\mu_U(\mathcal S)
\le
\sqrt{1-\operatorname{cov}^{\ne}_U}.
\]

More generally, let \(T=U\sqcup U^c\), let
\(\mu_T=\mu_U\otimes\mu_{U^c}\), and let \(\mathcal V\subseteq2^T\).  Suppose
that every \(U\)-section
\[
\mathcal V_U(D)
=
\{X\subseteq U:D\cup X\in\mathcal V\},
\qquad D\subseteq U^c,
\]
is top-union-free on \(U\).  Then every subfamily
\(\mathcal W\subseteq\mathcal V\) satisfies
\[
\mu_T(\mathcal W)
\le
\sqrt{1-\operatorname{cov}^{\ne}_U}.
\]
In particular, this applies to \(\mathcal W=\mathcal V\cap H\) for any
terminal window \(H\subseteq2^T\), including high-support windows.

Consequently, in the comparable endpoint branch \(f\subsetneq u\), if the
upper mixed-shadow exclusion from `mrw-740b9e5c6cff` holds for a fixed lower
terminal parent \(U\in\mathcal R_f\), then every high-window subfamily of
\(\mathcal R_u\) has terminal product measure at most
\[
\sqrt{1-\operatorname{cov}^{\ne}_U}.
\]

## Proof
Let \(X,Y\) be independent \(\mu_U\)-distributed traces.  If \(\mathcal S\) is
top-union-free, then
\[
(\mathcal S\times\mathcal S)
\cap
\{(X,Y):X\cup Y=U,\ X\ne Y\}
=
\emptyset.
\]
Therefore
\[
\mu_U(\mathcal S)^2
=
\mu_U^{\otimes2}(\mathcal S\times\mathcal S)
\le
1-\operatorname{cov}^{\ne}_U.
\]

For a coordinate \(u\in U\), two independent traces cover \(u\) with
probability
\[
1-(1-q_u)^2=2q_u-q_u^2.
\]
Independence over coordinates gives
\[
\mu_U^{\otimes2}(X\cup Y=U)
=
\prod_{u\in U}(2q_u-q_u^2).
\]
The equal covering pairs are exactly \(X=Y=U\), and have probability
\[
\left(\prod_{u\in U}q_u\right)^2.
\]
Subtracting this diagonal event gives the displayed formula for
\(\operatorname{cov}^{\ne}_U\).

For the fiber form, decompose by \(D\subseteq U^c\).  Each section
\[
\mathcal W_U(D)
=
\{X\subseteq U:D\cup X\in\mathcal W\}
\]
is a subfamily of \(\mathcal V_U(D)\), hence is also top-union-free on \(U\).
The preceding bound gives
\[
\mu_U(\mathcal W_U(D))
\le
\sqrt{1-\operatorname{cov}^{\ne}_U}
\qquad(D\subseteq U^c).
\]
Averaging over \(D\) under \(\mu_{U^c}\) yields
\[
\mu_T(\mathcal W)
=
\sum_{D\subseteq U^c}\mu_{U^c}(D)\mu_U(\mathcal W_U(D))
\le
\sqrt{1-\operatorname{cov}^{\ne}_U}.
\]
No product or monotonicity property of the subfamily \(\mathcal W\) is needed.

Finally, if \(U\in\mathcal R_f\) and \(f\subsetneq u\), `mrw-dda277c43571`
turns the upper mixed-shadow exclusion from `mrw-740b9e5c6cff` into
top-union-freeness of every \(U\)-section of \(\mathcal R_u\).  Applying the
fiber form with \(\mathcal V=\mathcal R_u\) gives the stated high-window bound.

## Depends on
- `mrw-dda277c43571` for the equivalence between comparable upper mixed-shadow
  exclusion and sectionwise top-union-freeness.
- `mrw-740b9e5c6cff` for the source of the comparable upper mixed-shadow
  exclusion in the nonempty star escape split.

## Used by
- Pending: quantifying or classifying the comparable upper mixed-shadow branch
  according to whether \(\operatorname{cov}^{\ne}_U\) is large enough to force
  measure loss, or small enough to signal residual/product structure.

## Notes
- Edge cases are harmless.  If \(U=\emptyset\), then both products are \(1\),
  so \(\operatorname{cov}^{\ne}_U=0\) and the bound says only
  \(\mu_U(\mathcal S)\le1\).  If some \(q_u=0\), no sampled pair can cover
  \(U\), so the bound is again trivial.  If some \(q_u=1\), the formula simply
  removes the deterministic coordinate from the nontrivial cover calculation.
- The diagonal correction is essential: top-union-freeness forbids distinct
  covering pairs, but it allows the single equal covering pair \((U,U)\).
- This is a local quantitative charging lemma, not terminal Erdos 536 evidence.
  It is useful only when the fixed lower parent \(U\) has non-negligible
  distinct-cover probability
  \[
  \operatorname{cov}^{\ne}_U
  =
  \prod_{u\in U}(2q_u-q_u^2)
  -
  \left(\prod_{u\in U}q_u\right)^2.
  \]
  If that quantity is tiny, the next branch is to classify the corresponding
  high-mass top-union-free sections as residual/product obstructions rather
  than claim decay from this bound alone.
- Oracle accepted the proposition with only notational clarification.  Scout
  returned only a scaffold response and was ingested raw-only.
