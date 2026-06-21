---
id: "L-FGN-ProjectionCoefficients-PrecisionFirstRow-Equivalence"
type: "lemma"
title: "fGn projection coefficients equal signed precision first-row entries"
status: "proved"
tags: ["bridge", "fractional-gaussian-noise", "lemma", "not-app", "precision-matrix", "projection-coefficients", "proved", "toeplitz", "true"]
parents: ["O-FGN-ProjectionCoefficientPositivity-source-gate"]
refs: ["private proof note"]
---

# Lemma: fGn projection coefficients equal signed precision first-row entries

## Statement

For a finite one-sided fractional Gaussian-noise projection, with covariance block \(\Sigma=\begin{pmatrix}1&r^T\\ r&T\end{pmatrix}\), projection vector \(\Gamma=T^{-1}r\), precision matrix \(Q=\Sigma^{-1}\), and Schur complement \(s=1-r^TT^{-1}r>0\), one has \(Q_{00}=s^{-1}\) and \(Q_{0,k}=-s^{-1}\Gamma_k\). Hence projection-coefficient positivity is equivalent to strict negativity of the corresponding first-row off-diagonal precision entries.

## Dependencies

- [[wiki/nodes/O-FGN-ProjectionCoefficientPositivity-source-gate|Fractional Gaussian noise projection-coefficient positivity source gate]]

## Proof and provenance references

- `private proof note`

## Proof

Let
\[
\Delta_j=B^H_j-B^H_{j-1}
\]
and let
\[
\rho_m=\mathbf E[\Delta_1\Delta_{m+1}]
=\frac12\big((m+1)^{2H}-2m^{2H}+(m-1)^{2H}\big).
\]
For a fixed finite projection of \(\Delta_1\) onto \(\Delta_2,\ldots,\Delta_n\), write
\[
T=(\rho_{|i-j|})_{2\le i,j\le n},\qquad
r=(\rho_{1},\ldots,\rho_{n-1})^T,
\]
and
\[
\Gamma=T^{-1}r.
\]
Equivalently, for the full covariance block
\[
\Sigma=
\begin{pmatrix}
1&r^T\\
r&T
\end{pmatrix},
\qquad Q=\Sigma^{-1},
\]
the Schur complement \(s=1-r^TT^{-1}r\) is positive and block inversion gives
\[
Q_{00}=s^{-1},\qquad Q_{0,k-1}=-s^{-1}\Gamma_k
\]
for \(2\le k\le n\). Therefore
\[
\Gamma_k>0\quad\Longleftrightarrow\quad Q_{0,k-1}<0.
\]
The source conjecture is thus equivalent to strict negativity of the appropriate first-row off-diagonal precision entries for every finite fGn covariance block.

At \(H=1/2\), the fGn covariance is independent white noise:
\[
\rho_0=1,\qquad \rho_m=0\quad(m\ge1).
\]
Thus \(T(1/2)=I\) and \(r(1/2)=0\). For \(m\ge1\),
\[
\left.\frac{\partial}{\partial H}\rho_m\right|_{H=1/2}
=(m+1)\log(m+1)-2m\log m+(m-1)\log(m-1),
\]
with \(0\log0=0\). This is the second finite difference of the convex function \(x\log x\), hence it is strictly positive for \(m\ge1\).

For fixed \(n\), \(T(H)\) and \(r(H)\) are analytic near \(H=1/2\). Since
\[
\Gamma(H)=T(H)^{-1}r(H)
\]
and \(T(1/2)=I\), one has
\[
\Gamma_k(H)=(H-1/2)\rho_{k-1}'(1/2)+O((H-1/2)^2)
\]
for \(2\le k\le n\). Each leading coefficient is positive, so for each fixed \(n\) there is \(\varepsilon_n>0\) such that
\[
\Gamma_k(H)>0\qquad (2\le k\le n,\ 1/2<H<1/2+\varepsilon_n).
\]

_Proof source: `private proof note`._

## Tags

`bridge`, `fractional-gaussian-noise`, `lemma`, `not-app`, `precision-matrix`, `projection-coefficients`, `proved`, `toeplitz`, `true`
