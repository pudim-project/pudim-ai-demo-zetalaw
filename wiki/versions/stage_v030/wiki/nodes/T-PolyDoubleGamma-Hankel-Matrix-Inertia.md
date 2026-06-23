---
id: "T-PolyDoubleGamma-Hankel-Matrix-Inertia"
type: "theorem"
title: "Poly-double-gamma derivative Hankel matrix has fixed inertia"
status: "proved"
tags: ["app-0086-candidate", "app-candidate", "finite-certificate", "hankel-matrix", "laplace-kernel", "moment-gram", "poly-double-gamma", "primitive-growth", "proved", "source-open-solved", "spectral-inertia", "theorem", "true"]
parents: ["O-PolyDoubleGamma-HankelSpectralBehavior-source-gate", "D-PolyDoubleGamma-Derivative-Hankel-Matrix", "B-PolyDoubleGamma-Derivative-Laplace-Representation", "L-Signed-Hankel-Moment-Gram-StrictPD"]
refs: ["librarian/audits/LA-20260622T1217-poly-double-gamma-first-contact.json", "librarian/audits/LA-20260622T1230-poly-double-gamma-strict-app.json", "oracle/responses/OS-20260622T1221Z-poly-double-gamma-hankel-inertia-oracle-response.md", "raw/oracle/RO-OS-20260622T1221Z-poly-double-gamma-hankel-inertia.json", "raw/student/20260622T1228-poly-double-gamma-hankel-inertia.md"]
---

# Theorem: Poly-double-gamma derivative Hankel matrix has fixed inertia

## Statement

For \(y>0\), \(n\ge2\), and positive integers \(j,m\), the matrix \(H_m^{(n,j)}(y)=[\psi_2^{(n+(a+b)j)}(y)]_{a,b=0}^m\) satisfies \((-1)^{n+1}H_m^{(n,j)}(y)\succ0\). Hence its inertia is \((m+1,0,0)\) for odd \(n\) and \((0,m+1,0)\) for even \(n\). This solves the fixed-inertia/eigenvalue-sign component of Mishra--Swaminathan Remark 4.1.

## Dependencies

- [[wiki/nodes/O-PolyDoubleGamma-HankelSpectralBehavior-source-gate|Poly-double-gamma derivative Hankel spectral-behaviour source gate]]
- [[wiki/nodes/D-PolyDoubleGamma-Derivative-Hankel-Matrix|Poly-double-gamma derivative Hankel matrix]]
- [[wiki/nodes/B-PolyDoubleGamma-Derivative-Laplace-Representation|Poly-double-gamma derivative Laplace representation]]
- [[wiki/nodes/L-Signed-Hankel-Moment-Gram-StrictPD|Signed Hankel moment Gram strict positivity]]

## Proof and provenance references

- `librarian/audits/LA-20260622T1217-poly-double-gamma-first-contact.json`
- `librarian/audits/LA-20260622T1230-poly-double-gamma-strict-app.json`
- `oracle/responses/OS-20260622T1221Z-poly-double-gamma-hankel-inertia-oracle-response.md`
- `raw/oracle/RO-OS-20260622T1221Z-poly-double-gamma-hankel-inertia.json`
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

## Do not claim

- Do not claim to solve all possible meanings of the source phrase spectral behaviour.
- Do not claim eigenvalue asymptotics, spacing, eigenvectors, conditioning, parameter monotonicity, or total positivity of all minors.
- Do not attach the theorem to the source's possibly misprinted two-by-two specialization rather than the Proposition 4.1 matrix entries.
- Do not public-stage without explicit user request.

## Tags

`app-0086-candidate`, `app-candidate`, `finite-certificate`, `hankel-matrix`, `laplace-kernel`, `moment-gram`, `poly-double-gamma`, `primitive-growth`, `proved`, `source-open-solved`, `spectral-inertia`, `theorem`, `true`
