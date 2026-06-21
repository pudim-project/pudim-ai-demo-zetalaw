---
id: "T-BarbosaMenegatto-endpoint-additive-rectangle-not-SPD"
type: "theorem"
title: "Barbosa-Menegatto endpoint additive kernel is not strictly positive definite"
status: "proved"
tags: ["application-candidate", "finite-certificate", "generalized-stieltjes", "gneiting", "open-problem-solved", "product-kernel", "proved", "rectangle-annihilator", "source-solving", "strict-positive-definiteness", "strict-private-plus10", "theorem", "true"]
parents: ["L-Additive-product-kernel-rectangle-annihilator", "O-BarbosaMenegatto-Boundary-Gneiting-SPD-source-gate"]
refs: ["private librarian audit", "private Oracle response", "private proof note"]
---

# Theorem: Barbosa-Menegatto endpoint additive kernel is not strictly positive definite

## Statement

In the Barbosa--Menegatto generalized-Stieltjes endpoint \(D_f>0\), \(r=\lambda\), \(\mu_f=0\), \(C_fD_f>0\), the kernel \(G_\lambda(t,u,v)=C_fh(u,v)^{-\lambda}+D_fg(t)^{-\lambda}\) is not strictly positive definite on \(X\times Y\times Z\) whenever \(X\) is nontrivial and \(Y\times Z\) is nontrivial. Thus the exact nontrivial product-factor endpoint has a negative answer.

## Dependencies

- [[wiki/nodes/L-Additive-product-kernel-rectangle-annihilator|Additive product-kernel rectangle annihilator]]
- [[wiki/nodes/O-BarbosaMenegatto-Boundary-Gneiting-SPD-source-gate|Barbosa-Menegatto boundary Gneiting product-kernel strict positive definiteness source gate]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`

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

_Proof source: `private proof note`._

## Do not claim

- Do not claim singleton or one-factor degenerate cases are refuted by this theorem.
- Do not claim adjacent source cases \(r>\lambda\), \(\mu_f\ne0\), or \(D_f=0\).
- Do not public-stage without user request.

## Tags

`application-candidate`, `finite-certificate`, `generalized-stieltjes`, `gneiting`, `open-problem-solved`, `product-kernel`, `proved`, `rectangle-annihilator`, `source-solving`, `strict-positive-definiteness`, `strict-private-plus10`, `theorem`, `true`
