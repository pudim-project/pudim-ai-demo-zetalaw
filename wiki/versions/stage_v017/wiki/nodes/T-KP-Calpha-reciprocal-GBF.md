---
id: "T-KP-Calpha-reciprocal-GBF"
type: "theorem"
title: "Koumandos Pedersen C alpha reciprocal belongs to generalized Bernstein and normalized reciprocal is CM"
status: "proved"
tags: ["bridge-patch", "generalized-bernstein", "laplace-transform", "log-convexity", "proved", "reciprocal", "theorem"]
parents: ["T-GBF-product-closure", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private proof note", "wiki/definitions/generalized-stieltjes-bernstein-order.md"]
---

# Theorem: Koumandos Pedersen C alpha reciprocal belongs to generalized Bernstein and normalized reciprocal is CM

## Statement

If \(f\in\mathcal C_\alpha\) in the Koumandos--Pedersen sense, then \(1/f\in\mathcal B_{\alpha+1}\) and \(1/(x^{\alpha+1}f(x))\) is completely monotone.

## Dependencies

- [[wiki/nodes/T-GBF-product-closure|generalized Bernstein classes closed under product with order addition]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
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

_Proof source: `private proof note`._

## Tags

`bridge-patch`, `generalized-bernstein`, `laplace-transform`, `log-convexity`, `proved`, `reciprocal`, `theorem`
