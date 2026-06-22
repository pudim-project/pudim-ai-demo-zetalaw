---
id: "T-GBF-product-closure"
type: "theorem"
title: "generalized Bernstein classes closed under product with order addition"
status: "proved"
tags: ["bridge-patch", "complete-monotonicity", "finite-order", "generalized-bernstein", "product-closure", "proved", "theorem"]
parents: ["T-CM-closure-product-positive-mixture"]
refs: ["librarian/audits/LA-20260530T-kp-gbf-bridge-mainardi-demotion.json", "oracle/responses/ORACLE-FI-20260530T-elegance-033-oracle-forage-response.md", "raw/scout/FI-20260530T-elegance-033.md", "raw/student/20260530T-kp-gbf-bridge-mainardi-demotion.md", "wiki/definitions/generalized-stieltjes-bernstein-order.md"]
---

# Theorem: generalized Bernstein classes closed under product with order addition

## Statement

If \(\lambda_1,\lambda_2>0\), \(f_1\in\mathcal B_{\lambda_1}\), and \(f_2\in\mathcal B_{\lambda_2}\), then \(f_1f_2\in\mathcal B_{\lambda_1+\lambda_2}\).

## Dependencies

- [[wiki/nodes/T-CM-closure-product-positive-mixture|complete monotone functions closed under product positive sums and positive mixtures]]

## Proof and provenance references

- `librarian/audits/LA-20260530T-kp-gbf-bridge-mainardi-demotion.json`
- `oracle/responses/ORACLE-FI-20260530T-elegance-033-oracle-forage-response.md`
- `raw/scout/FI-20260530T-elegance-033.md`
- `raw/student/20260530T-kp-gbf-bridge-mainardi-demotion.md`
- `wiki/definitions/generalized-stieltjes-bernstein-order.md`

## Proof

For \(\lambda>0\), the source defines \(f\in\mathcal B_\lambda\) when
\[
x^{1-\lambda}f'(x)
\]
is completely monotone. It also recalls generalized Stieltjes classes \(\mathcal S_\lambda\) and the product closure
\[
\mathcal S_{\lambda_1}\mathcal S_{\lambda_2}\subseteq \mathcal S_{\lambda_1+\lambda_2}.
\]

Proposition 5.1 states that if
\[
f_1\in\mathcal B_{\lambda_1},\qquad f_2\in\mathcal B_{\lambda_2},
\]
then
\[
f_1f_2\in\mathcal B_{\lambda_1+\lambda_2}.
\]

Local proof audit: by definition \(f_j'(x)/x^{\lambda_j-1}\) is completely monotone, and by the cited Corollary 2.1, \(f_j(x)/x^{\lambda_j}\) is completely monotone. Then
\[
\frac{(f_1f_2)'(x)}{x^{\lambda_1+\lambda_2-1}}
=
\frac{f_1'(x)}{x^{\lambda_1-1}}\frac{f_2(x)}{x^{\lambda_2}}
+
\frac{f_1(x)}{x^{\lambda_1}}\frac{f_2'(x)}{x^{\lambda_2-1}}.
\]
The right side is a positive sum of products of completely monotone functions, hence completely monotone.

The same source's Proposition 5.11 defines a class \(\mathcal C_\alpha\): \(f\in\mathcal C_\alpha\) when \(x^\alpha f(x)\) is the Laplace transform of a decreasing logarithmically convex function. It proves
\[
f\in\mathcal C_\alpha
\quad\Longrightarrow\quad
\frac1f\in\mathcal B_{\alpha+1}
\]
and
\[
\frac{1}{x^{\alpha+1}f(x)}
\]
is completely monotone.

Promote bridge nodes:

the GBF product closure
the KP Calpha reciprocal GBF

Demote/quarantine:

_Proof source: `raw/student/20260530T-kp-gbf-bridge-mainardi-demotion.md`._

## Tags

`bridge-patch`, `complete-monotonicity`, `finite-order`, `generalized-bernstein`, `product-closure`, `proved`, `theorem`
