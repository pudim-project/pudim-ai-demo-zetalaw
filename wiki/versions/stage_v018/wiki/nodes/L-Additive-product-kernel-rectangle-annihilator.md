---
id: "L-Additive-product-kernel-rectangle-annihilator"
type: "lemma"
title: "Additive product-kernel rectangle annihilator"
status: "proved"
tags: ["bridge-lemma", "endpoint-obstruction", "finite-certificate", "lemma", "primitive-growth", "product-kernel", "proved", "rectangle-annihilator", "strict-positive-definiteness", "true"]
parents: ["D-Finite-dimensional-l1-dual-certificate-language", "D-Endpoint-obstruction-certificate-language", "T-Exact-finite-certificate-verification-principle"]
refs: ["librarian/audits/LA-20260613T1645-barbosa-menegatto-spd-strict-app.json", "oracle/responses/OS-20260613T163450Z-oracle-response.md", "raw/student/20260613T1640-barbosa-menegatto-spd-rectangle.md"]
---

# Lemma: Additive product-kernel rectangle annihilator

## Statement

If \(X\) and \(W\) each contain at least two points, then any finite-valued kernel on \(X\times W\) of the form \(K((x,w),(x',w'))=A K_X(x,x')+B K_W(w,w')\) is not strictly positive definite on \(X\times W\). A four-point checkerboard coefficient vector on a nontrivial product rectangle gives a zero quadratic form.

## Dependencies

- [[wiki/nodes/D-Finite-dimensional-l1-dual-certificate-language|finite dimensional l1 primal representation coordinate atom dual linear functional certificate language]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `librarian/audits/LA-20260613T1645-barbosa-menegatto-spd-strict-app.json`
- `oracle/responses/OS-20260613T163450Z-oracle-response.md`
- `raw/student/20260613T1640-barbosa-menegatto-spd-rectangle.md`

## Proof

Let \(X\) and \(W\) be sets with at least two points. Let \(K_X\colon X\times X\to\mathbb R\) and \(K_W\colon W\times W\to\mathbb R\) be finite-valued kernels, and let \(A,B\in\mathbb R\). Define
\[
K((x,w),(x',w'))=A K_X(x,x')+B K_W(w,w').
\]
Then \(K\) is not strictly positive definite on \(X\times W\).

Choose \(x_0\ne x_1\) in \(X\) and \(w_0\ne w_1\) in \(W\). The four points
\[
p_{ij}=(x_i,w_j),\qquad i,j\in\{0,1\},
\]
are pairwise distinct. Put \(a=(1,-1)\), \(b=(1,-1)\), and \(c_{ij}=a_i b_j\). Thus the coefficient vector is
\[
(c_{00},c_{01},c_{10},c_{11})=(1,-1,-1,1),
\]
which is nonzero.

The quadratic form is
\[
\begin{aligned}
Q
&=\sum_{i,j,k,\ell} c_{ij}c_{k\ell}
\left(AK_X(x_i,x_k)+BK_W(w_j,w_\ell)\right)\\
&=A\left(\sum_j b_j\right)^2\sum_{i,k}a_i a_kK_X(x_i,x_k)
+B\left(\sum_i a_i\right)^2\sum_{j,\ell}b_j b_\ell K_W(w_j,w_\ell).
\end{aligned}
\]
Since \(\sum_i a_i=\sum_j b_j=0\), we have \(Q=0\). This is a zero quadratic form for a nonzero coefficient vector on distinct points, contradicting strict positive definiteness.

This proof does not address singleton \(X\), singleton \(Y\times Z\), or other one-factor degeneracies. The four-point rectangle cannot be formed there, and strict positive definiteness depends on the remaining one-factor kernel and constants.

This proof also does not address the adjacent source cases \(r>\lambda\), \(\mu_f\ne0\), \(D_f=0\), complete-Bernstein analogues, or any non-additive variant.

_Proof source: `raw/student/20260613T1640-barbosa-menegatto-spd-rectangle.md`._

## Tags

`bridge-lemma`, `endpoint-obstruction`, `finite-certificate`, `lemma`, `primitive-growth`, `product-kernel`, `proved`, `rectangle-annihilator`, `strict-positive-definiteness`, `true`
