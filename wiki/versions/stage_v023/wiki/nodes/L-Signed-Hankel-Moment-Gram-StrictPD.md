---
id: "L-Signed-Hankel-Moment-Gram-StrictPD"
type: "lemma"
title: "Signed Hankel moment Gram strict positivity"
status: "proved"
tags: ["bridge-lemma", "finite-certificate", "hankel-matrix", "inertia", "lemma", "moment-gram", "positive-definite", "primitive-growth", "proved", "true"]
parents: ["D-Laplace-kernel-and-tilted-moment-language", "D-Determinant-triangular-compression-language", "T-Exact-finite-certificate-verification-principle"]
refs: ["oracle/responses/OS-20260622T1221Z-poly-double-gamma-hankel-inertia-oracle-response.md", "raw/student/20260622T1228-poly-double-gamma-hankel-inertia.md"]
---

# Lemma: Signed Hankel moment Gram strict positivity

## Statement

Let \(\mu\) be a positive measure with strictly positive mass on an interval and finite moments through the needed orders. For distinct monomials \(x^{0j},x^{1j},\ldots,x^{mj}\) with \(j\ge1\), the matrix \(G_{ab}=\int x^{aj}x^{bj}\,d\mu(x)\) is strictly positive definite. Any matrix obtained from \(G\) by real diagonal sign congruence and one global sign has the corresponding fixed inertia.

## Dependencies

- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]
- [[wiki/nodes/D-Determinant-triangular-compression-language|Determinant and triangular compression language]]
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `oracle/responses/OS-20260622T1221Z-poly-double-gamma-hankel-inertia-oracle-response.md`
- `raw/student/20260622T1228-poly-double-gamma-hankel-inertia.md`

## Proof

Assume \(y>0\), \(n\ge2\), and \(j,m\ge1\). The source derivative Laplace representation is
\[
\psi_2^{(r)}(y)=(-1)^{r+1}\int_0^\infty e^{-yt}\frac{t^r}{(1-e^{-t})^2}\,dt,
\qquad r\ge2.
\]
For \(r=n+(a+b)j\), this gives
\[
H_{ab}(y)=(-1)^{n+(a+b)j+1}
\int_0^\infty e^{-yt}\frac{t^{n+(a+b)j}}{(1-e^{-t})^2}\,dt.
\]

Define
\[
d\mu_y(t)=e^{-yt}\frac{t^n}{(1-e^{-t})^2}\,dt,\qquad t>0.
\]
This is a positive measure. It has all required moments: near \(0\), its density behaves like \(t^{n-2}\,dt\), integrable because \(n\ge2\); at infinity, \(e^{-yt}\) gives exponential decay.

Let
\[
G_{ab}(y)=\int_0^\infty t^{aj}t^{bj}\,d\mu_y(t),
\qquad
S=\operatorname{diag}((-1)^{aj})_{a=0}^{m}.
\]
Then
\[
H(y)=(-1)^{n+1}S\,G(y)\,S.
\]
Indeed, the \((a,b)\) entry on the right has sign
\[
(-1)^{n+1+aj+bj}
\]
times the positive moment integral, which equals
\[
(-1)^{n+(a+b)j+1}
\int_0^\infty e^{-yt}\frac{t^{n+(a+b)j}}{(1-e^{-t})^2}\,dt.
\]

The matrix \(G(y)\) is strictly positive definite. For a nonzero vector \(c=(c_0,\ldots,c_m)\),
\[
c^T G(y)c
=\int_0^\infty \left(\sum_{a=0}^m c_a t^{aj}\right)^2\,d\mu_y(t)>0.
\]
The polynomial \(\sum_a c_a t^{aj}\) is not identically zero unless all \(c_a=0\), and \(d\mu_y\) has strictly positive density on \((0,\infty)\).

Since \(S\) is invertible and diagonal, Sylvester's law of inertia gives
\[
\operatorname{Inertia}(H(y))=\operatorname{Inertia}((-1)^{n+1}G(y)).
\]
Therefore \(H(y)\) is positive definite for odd \(n\) and negative definite for even \(n\):
\[
\operatorname{Inertia}(H(y))=
\begin{cases}
(m+1,0,0),& n\ \text{odd},\\
(0,m+1,0),& n\ \text{even}.
\end{cases}
\]
Equivalently,
\[
(-1)^{n+1}H(y)\succ0.
\]

The determinant sign shadow is
\[
(-1)^{(n+1)(m+1)}\det H(y)>0.
\]

_Proof source: `raw/student/20260622T1228-poly-double-gamma-hankel-inertia.md`._

## Tags

`bridge-lemma`, `finite-certificate`, `hankel-matrix`, `inertia`, `lemma`, `moment-gram`, `positive-definite`, `primitive-growth`, `proved`, `true`
