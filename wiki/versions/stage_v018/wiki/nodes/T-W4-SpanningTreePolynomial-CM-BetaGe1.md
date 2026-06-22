---
id: "T-W4-SpanningTreePolynomial-CM-BetaGe1"
type: "theorem"
title: "W4 belongs to G beta above one"
status: "proved"
tags: ["application-candidate", "complete-monotonicity", "laplace-transform", "open-problem-solved", "proved", "riesz-representation", "source-solving", "spanning-tree-polynomial", "star-mesh", "strict-private-post-v016", "theorem", "true"]
parents: ["O-W4-SpanningTreePolynomial-CM-Beta-source-gate", "L-StarMesh-SpanningTree-ApexElimination", "L-K4Kirchhoff-RieszRank3-LaplaceRepresentation", "L-ConditionalStar-GaussianLaplaceKernel"]
refs: ["oracle/responses/OS-20260620T093606Z-oracle-response.md", "raw/student/20260620T1000-w4-spanning-tree-positive.md"]
---

# Theorem: W4 belongs to G beta above one

## Statement

Let \(W_4\) be the wheel with four spokes. For every \(\beta>1\), the inverse power \(T_{W_4}^{-\beta}\) of the spanning-tree polynomial is completely monotone on the positive edge cone. In particular, \(W_4\in G_\beta\) for every \(1<\beta<3/2\), answering the Scott--Sokal source question for this graph affirmatively.

## Dependencies

- [[wiki/nodes/O-W4-SpanningTreePolynomial-CM-Beta-source-gate|W4 spanning-tree polynomial complete-monotonicity source gate]]
- [[wiki/nodes/L-StarMesh-SpanningTree-ApexElimination|Star-mesh apex elimination for spanning-tree polynomials]]
- [[wiki/nodes/L-K4Kirchhoff-RieszRank3-LaplaceRepresentation|K4 Kirchhoff polynomial has a rank-three Riesz representation]]
- [[wiki/nodes/L-ConditionalStar-GaussianLaplaceKernel|Conditional star kernels are Gaussian Laplace transforms]]

## Proof and provenance references

- `oracle/responses/OS-20260620T093606Z-oracle-response.md`
- `raw/student/20260620T1000-w4-spanning-tree-positive.md`

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

_Proof source: `raw/student/20260620T1000-w4-spanning-tree-positive.md`._

## Do not claim

- Do not claim the endpoint \(\beta=1\) unless separately audited.
- Do not claim a full Scott--Sokal classification for all graphs.
- Do not public-stage without user request.
- Do not assign public APP numbering until staging/registry promotion.

## Tags

`application-candidate`, `complete-monotonicity`, `laplace-transform`, `open-problem-solved`, `proved`, `riesz-representation`, `source-solving`, `spanning-tree-polynomial`, `star-mesh`, `strict-private-post-v016`, `theorem`, `true`
