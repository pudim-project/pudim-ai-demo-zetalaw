---
id: "L-K4Kirchhoff-RieszRank3-LaplaceRepresentation"
type: "lemma"
title: "K4 Kirchhoff polynomial has a rank-three Riesz representation"
status: "proved"
tags: ["bridge", "complete-monotonicity", "laplace-transform", "lemma", "proved", "riesz-representation", "spanning-tree-polynomial", "strict-private-post-v016", "true"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Determinant-triangular-compression-language"]
refs: ["private proof note"]
---

# Lemma: K4 Kirchhoff polynomial has a rank-three Riesz representation

## Statement

For the complete graph \(K_4\), the spanning-tree polynomial is a rank-three determinant \(T_{K_4}(y)=\det\sum_e y_e b_eb_e^T\). For every \(\beta>1\), \(T_{K_4}(y)^{-\beta}\) is a positive Laplace transform in the six edge variables via the \(3\times3\) Riesz/Wishart integral; the three edge variables on any triangle correspond to squared distances of three Euclidean points in the Riesz support.

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Determinant-triangular-compression-language|Determinant and triangular compression language]]

## Proof and provenance references

- `private proof note`

## Proof

Root \(K_4\) at vertex \(3\). For the remaining vertices \(0,2,4\), use edge vectors
\[
b_{03}=e_0,\quad b_{23}=e_2,\quad b_{43}=e_4,\quad
b_{02}=e_0-e_2,\quad b_{04}=e_0-e_4,\quad b_{24}=e_2-e_4 .
\]
Then
\[
T_{K_4}(y)=\det M(y),\qquad
M(y)=\sum_{ij} y_{ij} b_{ij}b_{ij}^{T}.
\]
For \(\beta>1\), the \(3\times3\) Riesz/Wishart integral gives
\[
\det M(y)^{-\beta}
=C_\beta\int_{Y>0}
\exp\!\left(-\operatorname{tr}(M(y)Y)\right)
(\det Y)^{\beta-2}\,dY,
\]
with \(C_\beta>0\). Writing
\[
U_{ij}=b_{ij}^{T}Yb_{ij},
\]
the exponent is \(-\sum y_{ij}U_{ij}\). If \(Y=LL^T\), then \(U_{ij}=|L^Tb_{ij}|^2\). In particular the triple
\[
(U_{02},U_{04},U_{24})
\]
is the squared-distance triple of the three points \(L^Te_0,L^Te_4,L^Te_2\), hence can be represented in \(\mathbb R^2\).

For fixed such a squared-distance triple, choose points
\(\xi_0,\xi_2,\xi_4\in\mathbb R^2\) with
\[
U_{02}=|\xi_0-\xi_2|^2,\quad
U_{04}=|\xi_0-\xi_4|^2,\quad
U_{24}=|\xi_2-\xi_4|^2.
\]
The Gaussian completion identity gives
\[
S^{-1}\exp\left(
-{paU_{02}+pdU_{04}+adU_{24}\over S}
\right)
=\pi^{-1}\int_{\mathbb R^2}
\exp\left(-p|z-\xi_0|^2-a|z-\xi_2|^2-d|z-\xi_4|^2\right)\,dz .
\]
Multiplying by the gamma representation
\[
S^{-(\beta-1)}
=\Gamma(\beta-1)^{-1}\int_0^\infty t^{\beta-2}e^{-tS}\,dt
\]
shows that, for every \(\beta>1\),
\[
S^{-\beta}
\exp\left(
-{paU_{02}+pdU_{04}+adU_{24}\over S}
\right)
\]
is a positive Laplace transform in the variables \(p,a,d\).

From the star-mesh identity and the Riesz integral,
\[
T_{W_4}^{-\beta}
=S^{-\beta}T_{K_4}(y)^{-\beta}
\]
is an integral of the product
\[
\exp(-qU_{02})\exp(-sU_{04})\exp(-rU_{03})
\exp(-bU_{23})\exp(-cU_{34})
\]
with the three-arm star factor above. Each factor is a positive Laplace kernel in its edge-variable block, and the Riesz and Gaussian/gamma measures are positive. Tonelli's theorem therefore gives a positive Laplace representation for \(T_{W_4}^{-\beta}\) on \((0,\infty)^8\).

Hence \(T_{W_4}^{-\beta}\) is completely monotone for every \(\beta>1\). In Scott--Sokal notation, \(W_4\in G_\beta\) throughout the source-open interval \(1<\beta<3/2\).

_Proof source: `private proof note`._

## Tags

`bridge`, `complete-monotonicity`, `laplace-transform`, `lemma`, `proved`, `riesz-representation`, `spanning-tree-polynomial`, `strict-private-post-v016`, `true`
