---
id: "T-QGamma-HankelKernel-STPInfinity"
type: "theorem"
title: "q-gamma Hankel kernel is strictly totally positive"
status: "proved"
tags: ["APP-0080-candidate", "application-candidate", "mellin-moment-kernel", "open-problem-solved", "proved", "q-gamma", "source-solving", "strict-private-post-v016", "strict-total-positivity", "theorem", "true"]
parents: ["O-QGamma-HankelKernel-STPInfinity-source-gate", "L-QBinomial-Atomic-Mellin-Representation", "L-Mellin-Moment-Kernel-STP-InfiniteSupport", "L-Generalized-Vandermonde-Chebyshev-StrictSign", "D-Determinant-triangular-compression-language"]
refs: ["private Oracle response", "private proof note"]
---

# Theorem: q-gamma Hankel kernel is strictly totally positive

## Statement

For every fixed \(0<q<1\), the kernel \(K_q(x,y)=\Gamma_q(x+y)\) is \(STP_\infty\) on \((0,\infty)^2\). Equivalently, for every \(m\ge1\) and every \(0<x_1<\cdots<x_m\), \(0<y_1<\cdots<y_m\), one has \(\det[\Gamma_q(x_i+y_j)]_{i,j=1}^m>0\).

## Dependencies

- [[wiki/nodes/O-QGamma-HankelKernel-STPInfinity-source-gate|q-gamma Hankel kernel strict total positivity source gate]]
- [[wiki/nodes/L-QBinomial-Atomic-Mellin-Representation|q-binomial atomic Mellin representation for q-gamma]]
- [[wiki/nodes/L-Mellin-Moment-Kernel-STP-InfiniteSupport|Positive Mellin moment kernels with infinite support are strictly totally positive]]
- [[wiki/nodes/L-Generalized-Vandermonde-Chebyshev-StrictSign|Generalized Vandermonde determinants have strict Chebyshev sign]]
- [[wiki/nodes/D-Determinant-triangular-compression-language|Determinant and triangular compression language]]

## Proof and provenance references

- `private Oracle response`
- `private proof note`

## Proof

For every fixed \(0<q<1\), prove that
\[
K_q(x,y)=\Gamma_q(x+y)
\]
is strictly totally positive of all orders on \((0,\infty)^2\).

Let \(\mu\) be a positive Borel measure on \((0,\infty)\) with at least \(m\) distinct support points. Suppose the Mellin moments
\[
M(s)=\int_0^\infty t^s\,d\mu(t)
\]
are finite for all \(s=x_i+y_j\), where
\[
0<x_1<\cdots<x_m,\qquad 0<y_1<\cdots<y_m.
\]
Then
\[
\det[M(x_i+y_j)]_{i,j=1}^m>0.
\]
If \(\mu\) has infinite support and the required moments are finite on the domain, then \(K(x,y)=M(x+y)\) is \(STP_\infty\).

By Andreief's identity, first for finite-support measures and then by approximation/monotone convergence of the nonnegative Cauchy-Binet expansion,
\[
\det[M(x_i+y_j)]_{i,j=1}^m
=\frac{1}{m!}\int_{(0,\infty)^m}
\det[t_k^{x_i}]_{i,k=1}^m
\det[t_k^{y_j}]_{j,k=1}^m
\prod_{k=1}^m d\mu(t_k).
\]
The integrand vanishes on diagonals. On the chamber \(0<t_1<\cdots<t_m\), both determinants are positive. Indeed, after writing \(t_k=e^{u_k}\), the functions \(u\mapsto e^{x_i u}\) form an extended complete Chebyshev system because their Wronskian is
\[
\det\left[\frac{d^{r-1}}{du^{r-1}}e^{x_i u}\right]_{i,r=1}^m
=e^{(x_1+\cdots+x_m)u}\prod_{1\le i<j\le m}(x_j-x_i)>0.
\]
The same argument applies to the \(y_j\). Since \(\mu\) has at least \(m\) support points, the ordered chamber has positive \(\mu^m\)-mass on sets where the integrand is strictly positive. Thus the determinant is strictly positive.

The moment hypotheses justify the determinant integral: expanding the product of determinants bounds the absolute integrand by a finite sum of products of the finite moments \(M(x_i+y_j)\).

For \(0<q<1\), the Jackson \(q\)-gamma function used by the source is
\[
\Gamma_q(z)=(1-q)^{1-z}\frac{(q;q)_\infty}{(q^z;q)_\infty},\qquad z>0.
\]
The \(q\)-binomial theorem gives
\[
\frac{1}{(q^z;q)_\infty}=\sum_{n=0}^{\infty}\frac{q^{nz}}{(q;q)_n}.
\]
Therefore
\[
\Gamma_q(z)=(1-q)(q;q)_\infty
\sum_{n=0}^{\infty}\frac{(q^n/(1-q))^z}{(q;q)_n}.
\]
Equivalently,
\[
\Gamma_q(z)=\int_0^\infty t^z\,d\mu_q(t),
\]
where
\[
\mu_q=(1-q)(q;q)_\infty
\sum_{n=0}^{\infty}\frac{1}{(q;q)_n}\,
\delta_{q^n/(1-q)}.
\]
This is a positive atomic measure with infinitely many distinct support points \(q^n/(1-q)\). The moments are finite for all \(z>0\), since the defining series converges for \(q^z\in(0,1)\).

Applying the Mellin moment kernel lemma to \(M(z)=\Gamma_q(z)\) gives, for every \(m\ge1\) and every strictly ordered \(x_i,y_j>0\),
\[
\det[\Gamma_q(x_i+y_j)]_{i,j=1}^m>0.
\]
Thus \(K_q(x,y)=\Gamma_q(x+y)\) is \(STP_\infty\) on \((0,\infty)^2\).

_Proof source: `private proof note`._

## Do not claim

- Do not extend this theorem to q>1 without a separate normalization and source audit.
- Do not conflate this continuous STP_infinity theorem with the source's discrete STP_3 q-Pochhammer lemma.
- Do not public-stage without user request.

## Tags

`APP-0080-candidate`, `application-candidate`, `mellin-moment-kernel`, `open-problem-solved`, `proved`, `q-gamma`, `source-solving`, `strict-private-post-v016`, `strict-total-positivity`, `theorem`, `true`
