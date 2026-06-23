---
id: "B-OppositeOrder-CompressionDeterminant-Transfer"
type: "theorem"
title: "Opposite-order compression determinant transfer"
status: "proved"
tags: ["application-bridge", "bridge-theorem", "cauchy-binet", "compression", "determinant", "matrix-inequality", "primitive-support", "projection-dpp", "proved", "theorem", "true"]
parents: ["L-OppositeOrder-LogDet-Chebyshev", "D-Determinant-triangular-compression-language"]
refs: ["librarian/audits/LA-20260622T1445-bourin-compressiondet-strict-app.json", "oracle/responses/OS-20260622T141938Z-oracle-response.md", "raw/student/20260622T1438-bourin-compressiondet.md"]
---

# Theorem: Opposite-order compression determinant transfer

## Statement

Let \(V:\mathbb C^k\to\mathbb C^n\) be an isometry and set \(g_V(x)=\det(V^*\operatorname{diag}(x)V)\). If \(u\in\mathbb R^n\) is weakly decreasing and \(v\in\mathbb R^n\) is weakly increasing, then \(g_V(e^u)g_V(e^v)\ge g_V(e^{u+v})g_V(1)\). Equivalently, compression determinants satisfy a reverse product inequality for oppositely ordered diagonal data.

## Dependencies

- [[wiki/nodes/L-OppositeOrder-LogDet-Chebyshev|Opposite-order log-determinant Chebyshev inequality]]
- [[wiki/nodes/D-Determinant-triangular-compression-language|Determinant and triangular compression language]]

## Proof and provenance references

- `librarian/audits/LA-20260622T1445-bourin-compressiondet-strict-app.json`
- `oracle/responses/OS-20260622T141938Z-oracle-response.md`
- `raw/student/20260622T1438-bourin-compressiondet.md`

## Proof

Bourin Problem 1.6 asks whether the reverse determinant compression inequality
\[
\det A_E\det B_E\ge \det(AB)_E
\]
holds for every subspace \(E\) whenever \(A,B\ge0\) form an antimonotone pair in the source sense.

The source antimonotone hypothesis means that \(A\) and \(B\) are simultaneously diagonalizable through one Hermitian functional calculus, with eigenvalues oppositely ordered. Thus, after choosing the common eigenbasis, it is enough to treat
\[
A=\operatorname{diag}(a_1,\ldots,a_n),\qquad
B=\operatorname{diag}(b_1,\ldots,b_n),
\]
where \(a_1\ge\cdots\ge a_n\ge0\) and \(0\le b_1\le\cdots\le b_n\). The opposite orientation is the same after reversing the basis.

Let \(E\) have dimension \(k\), and let \(V:\mathbb C^k\to\mathbb C^n\) be an isometry with range \(E\). For \(x=(x_1,\ldots,x_n)\in(0,\infty)^n\), define
\[
g(x)=\det\bigl(V^*\operatorname{diag}(x)V\bigr).
\]
By Cauchy--Binet,
\[
g(x)=\sum_{|S|=k}p_S x_S,\qquad
p_S=|\det V_S|^2,\qquad
x_S=\prod_{i\in S}x_i.
\]
Also
\[
\sum_{|S|=k}p_S=g(1,\ldots,1)=\det(V^*V)=1.
\]
For \(a=(a_i)\), \(b=(b_i)\), and \(ab=(a_i b_i)\),
\[
\det A_E=g(a),\qquad
\det B_E=g(b),\qquad
\det(AB)_E=g(ab).
\]
The desired inequality is therefore
\[
g(a)g(b)\ge g(ab)g(1)=g(ab).
\]

Assume first that all \(a_i,b_i>0\). Put
\[
u_i=\log a_i,\qquad v_i=\log b_i,\qquad
\Phi(y)=\log g(e^y).
\]
Then \(u_1\ge\cdots\ge u_n\) and \(v_1\le\cdots\le v_n\). It is enough to prove
\[
\Phi(u)+\Phi(v)-\Phi(u+v)-\Phi(0)\ge0.
\]

For each \(y\), the tilted weights
\[
\mu_y(S)=\frac{p_S e^{\sum_{i\in S}y_i}}{g(e^y)}
\]
form the fixed-size projection determinantal measure associated with
\[
M_y=\operatorname{diag}(e^{y_i/2})V,\qquad
K_y=M_y(M_y^*M_y)^{-1}M_y^*.
\]
The kernel \(K_y\) is an orthogonal projection onto \(\operatorname{range} M_y\). Differentiating \(\Phi\) gives
\[
\partial_i\Phi(y)=\mu_y(i\in S)=(K_y)_{ii},
\]
and
\[
\partial_{ij}\Phi(y)=\operatorname{Cov}_{\mu_y}(1_{i\in S},1_{j\in S}).
\]
For a projection determinantal measure,
\[
\operatorname{Cov}(1_{i\in S},1_{j\in S})=-|(K_y)_{ij}|^2\qquad(i\ne j).
\]
Because \(\sum_i1_{i\in S}=k\) is constant, the covariance matrix has zero row sums, so
\[
\partial_{ii}\Phi(y)=\sum_{j\ne i}|(K_y)_{ij}|^2.
\]
Consequently, for real vectors \(r,s\),
\[
r^T\nabla^2\Phi(y)s
=\sum_{i<j}|(K_y)_{ij}|^2(r_i-r_j)(s_i-s_j).
\]

Apply this identity with \(r=u\) and \(s=v\). For \(i<j\),
\[
u_i-u_j\ge0,\qquad v_i-v_j\le0,
\]
hence each summand is nonpositive:
\[
u^T\nabla^2\Phi(y)v\le0\qquad(y\in\mathbb R^n).
\]
Integrating the mixed second derivative over the rectangle gives
\[
\Phi(u+v)-\Phi(u)-\Phi(v)+\Phi(0)
=\int_0^1\int_0^1
u^T\nabla^2\Phi(su+tv)v\,dt\,ds
\le0.
\]
Thus
\[
\Phi(u)+\Phi(v)\ge \Phi(u+v)+\Phi(0),
\]
and exponentiating yields
\[
g(a)g(b)\ge g(ab)g(1)=g(ab).
\]

_Proof source: `raw/student/20260622T1438-bourin-compressiondet.md`._

## Tags

`application-bridge`, `bridge-theorem`, `cauchy-binet`, `compression`, `determinant`, `matrix-inequality`, `primitive-support`, `projection-dpp`, `proved`, `theorem`, `true`
