---
id: "L-StarMesh-SpanningTree-ApexElimination"
type: "lemma"
title: "Star-mesh apex elimination for spanning-tree polynomials"
status: "proved"
tags: ["bridge", "finite-certificate", "lemma", "proved", "schur-complement", "spanning-tree-polynomial", "strict-private-post-v016", "true"]
parents: ["D-Determinant-triangular-compression-language", "D-Finite-dimensional-l1-dual-certificate-language"]
refs: ["raw/student/20260620T0845-k5minuse-spanning-tree-positive.md"]
---

# Lemma: Star-mesh apex elimination for spanning-tree polynomials

## Statement

Let a graph network on three terminals have spanning-tree polynomial \(T_H\). Adjoining one apex with positive conductances \(u_1,u_2,u_3\) to the terminals multiplies the spanning-tree polynomial by \(U=u_1+u_2+u_3\) and adds terminal triangle conductances \(u_iu_j/U\).

## Dependencies

- [[wiki/nodes/D-Determinant-triangular-compression-language|Determinant and triangular compression language]]
- [[wiki/nodes/D-Finite-dimensional-l1-dual-certificate-language|finite dimensional l1 primal representation coordinate atom dual linear functional certificate language]]

## Proof and provenance references

- `raw/student/20260620T0845-k5minuse-spanning-tree-positive.md`

## Proof

Let \(G=K_5-e\), realized as two nonadjacent apices joined to the terminal triangle \(\{2,3,4\}\). Write
\[
a=(a_1,a_2,a_3)=(x_{02},x_{03},x_{04}),\qquad
b=(b_1,b_2,b_3)=(x_{12},x_{13},x_{14}),
\]
\[
c=(c_{12},c_{13},c_{23})=(x_{23},x_{24},x_{34}),
\qquad A=a_1+a_2+a_3,\quad B=b_1+b_2+b_3 .
\]
For a triangle edge-vector \(w=(w_1,w_2,w_3)\), put
\[
E(w)=w_1w_2+w_1w_3+w_2w_3 .
\]
The claim is that \(T_G^{-\beta}\) is completely monotone in all nine positive edge variables for every \(\beta>1\).

\emph{Lemma 1: star-mesh factorization of \(T\_{K\_5-e}\).}

For \(u=(u_1,u_2,u_3)\), define
\[
p_u=\left({u_1u_2\over u_1+u_2+u_3},
          {u_1u_3\over u_1+u_2+u_3},
          {u_2u_3\over u_1+u_2+u_3}\right).
\]
Then
\[
T_{K_5-e}(a,b,c)=AB\,E(c+p_a+p_b).
\]

Indeed, if a network \(H\) on three terminals has spanning-tree polynomial \(T_H\), adjoining a new apex with conductances \(u_1,u_2,u_3\) to the terminals multiplies the reduced Laplacian determinant by \(U=u_1+u_2+u_3\) and replaces \(H\) by the star-mesh transformed network with added terminal edge conductances \(p_u\). This is the Schur complement of the apex diagonal block \(U\) in the weighted Laplacian:
\[
L_H+\operatorname{diag}(u)-{uu^T\over U}.
\]
The last matrix is the terminal Laplacian of \(H\) plus a triangle with edge conductances \(u_iu_j/U\). Applying this twice, once for each apex, leaves the terminal triangle with edge vector \(c+p_a+p_b\), whose spanning-tree polynomial is \(E\).

For \(w_i>0\) and \(\beta>1/2\),
\[
E(w)^{-\beta}
=C_\beta\int_{Y>0}
\exp\{-w_1(Y_{11}+Y_{22}-2Y_{12})-w_2Y_{11}-w_3Y_{22}\}
(\det Y)^{\beta-3/2}\,dY
\]
with \(C_\beta>0\), where \(Y\) ranges over positive definite \(2\times2\) symmetric matrices.

This is the standard \(2\times2\) Riesz/Wishart integral applied to
\[
M(w)=
\begin{pmatrix}
w_1+w_2 & -w_1\\
-w_1 & w_1+w_3
\end{pmatrix},
\qquad \det M(w)=E(w).
\]
The exponent is \(-\operatorname{tr}(M(w)Y)\), and the Wishart integral is valid for \(\beta>(2-1)/2=1/2\).

For \(Y>0\), choose vectors \(u,v\in\mathbb R^2\) with Gram matrix \(Y\). Then
\[
r_{12}=Y_{11}+Y_{22}-2Y_{12}=|u-v|^2,\quad
r_{13}=Y_{11}=|u|^2,\quad
r_{23}=Y_{22}=|v|^2 .
\]

For every \(r_{ij}=|u_i-u_j|^2\) with \(u_1,u_2,u_3\in\mathbb R^2\),
\[
A^{-1}\exp(-p_a\cdot r)
=\pi^{-1}\int_{\mathbb R^2}
\exp\left(-\sum_{i=1}^3 a_i|z-u_i|^2\right)\,dz.
\]
This is the elementary Gaussian completion identity
\[
\sum_i a_i|z-u_i|^2
=A\left|z-\frac{\sum_i a_iu_i}{A}\right|^2
{1\over A}\sum_{i<j}a_ia_j|u_i-u_j|^2 .
\]
Thus \(A^{-1}e^{-p_a\cdot r}\) is a positive Laplace transform in the variables \(a_i\). For \(\beta>1\),
\[
A^{-\beta}e^{-p_a\cdot r}
=A^{-(\beta-1)}\big(A^{-1}e^{-p_a\cdot r}\big)
\]
is again completely monotone, because
\[
A^{-(\beta-1)}
=\Gamma(\beta-1)^{-1}\int_0^\infty t^{\beta-2}e^{-tA}\,dt.
\]
The same statement holds for \(B^{-\beta}e^{-p_b\cdot r}\).

From Lemma 1,
\[
T_G^{-\beta}=A^{-\beta}B^{-\beta}E(c+p_a+p_b)^{-\beta}.
\]
Insert Lemma 2 with \(w=c+p_a+p_b\). For each positive \(Y\), the factor involving \(c\) is
\[
\exp(-c\cdot r(Y)),
\]
a positive Laplace kernel in the triangle-edge variables. The factors involving \(a\) and \(b\) are
\[
A^{-\beta}\exp(-p_a\cdot r(Y)),
\qquad
B^{-\beta}\exp(-p_b\cdot r(Y)),
\]
which are completely monotone by Lemma 3 for every \(\beta>1\). The product is a completely monotone function in disjoint variable blocks, and integration against the positive Riesz measure preserves complete monotonicity by Tonelli.

Therefore \(T_{K_5-e}^{-\beta}\) is completely monotone on \((0,\infty)^9\) for every \(\beta>1\). In Scott--Sokal notation, \(K_5-e\in G_\beta\) for every \(1<\beta<3/2\).

_Proof source: `raw/student/20260620T0845-k5minuse-spanning-tree-positive.md`._

## Tags

`bridge`, `finite-certificate`, `lemma`, `proved`, `schur-complement`, `spanning-tree-polynomial`, `strict-private-post-v016`, `true`
