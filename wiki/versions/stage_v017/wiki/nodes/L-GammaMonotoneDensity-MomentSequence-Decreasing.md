---
id: "L-GammaMonotoneDensity-MomentSequence-Decreasing"
type: "lemma"
title: "Gamma moments of a decreasing density form a decreasing normalized sequence"
status: "proved"
tags: ["bridge-lemma", "gamma-law", "lemma", "moment-sequence", "negative-covariance", "primitive-growth", "proved", "renewal-coefficients", "true"]
parents: ["D-Laplace-kernel-and-tilted-moment-language", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private Oracle response", "private proof note"]
---

# Lemma: Gamma moments of a decreasing density form a decreasing normalized sequence

## Statement

Let \(u:(0,\infty)\to[0,\infty)\) be nonincreasing and locally integrable with finite gamma-weighted moments. Define \(M_k=k!^{-1}\int_0^\infty t^k e^{-t}u(t)\,dt\) for \(k\ge1\). Then \(M_{k+1}\le M_k\) for every \(k\ge1\). If additionally \(M_0=b+\int_0^\infty e^{-t}u(t)\,dt\) with \(b\ge0\), then \(M_1\le M_0\).

## Dependencies

- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private Oracle response`
- `private proof note`

## Proof

Let
\[
K(z)=\sum_{n\ge1}c(\psi,n)z^n.
\]
The Bendikov--Cygan discrete subordination coefficient calculation gives
\[
K(z)=1-\psi(1-z),
\]
under the source normalization \(\psi(0)=0\), \(\psi(1)=1\). Since \(C(0)=1\) and
\[
C(n)=\sum_{j=1}^{n}c(\psi,j)C(n-j),
\]
the generating function \(F(z)=\sum_{n\ge0}C(n)z^n\) satisfies
\[
F(z)=\frac{1}{1-K(z)}=\frac{1}{\psi(1-z)}.
\]

For \(\psi\in\mathrm{SBF}\), the source-cited potential representation gives
\[
\frac{1}{\psi(\lambda)}
=b+\int_0^\infty e^{-\lambda t}u(t)\,dt,
\]
where \(b\ge0\) and \(u\) is nonincreasing. Substituting \(\lambda=1-z\),
\[
F(z)=b+\int_0^\infty e^{-t}e^{zt}u(t)\,dt
=b+\sum_{k\ge0}\frac{z^k}{k!}\int_0^\infty t^k e^{-t}u(t)\,dt.
\]
Therefore
\[
C(0)=b+\int_0^\infty e^{-t}u(t)\,dt=1
\]
and, for \(k\ge1\),
\[
C(k)=\frac1{k!}\int_0^\infty t^k e^{-t}u(t)\,dt.
\]

For \(k\ge1\),
\[
C(k+1)-C(k)
=\frac1{(k+1)!}\int_0^\infty t^k e^{-t}(t-(k+1))u(t)\,dt.
\]
If \(T\sim\Gamma(k+1,1)\), this is
\[
C(k+1)-C(k)=\frac1{k+1}\operatorname{Cov}(T,u(T)).
\]
The covariance is nonpositive because \(t\mapsto t\) is increasing and \(u\) is nonincreasing:
\[
\operatorname{Cov}(T,u(T))
=\frac12\iint (t-s)(u(t)-u(s))\,d\mu_k(t)d\mu_k(s)\le0.
\]
Thus \(C(k+1)\le C(k)\) for \(k\ge1\).

For \(k=0\), the atom \(b\) must be kept:
\[
C(1)-C(0)
=\int_0^\infty (t-1)e^{-t}u(t)\,dt-b
=\operatorname{Cov}_{\mathrm{Exp}(1)}(T,u(T))-b\le0.
\]
Hence \(C(1)\le C(0)\), completing the monotonicity proof.

_Proof source: `private proof note`._

## Tags

`bridge-lemma`, `gamma-law`, `lemma`, `moment-sequence`, `negative-covariance`, `primitive-growth`, `proved`, `renewal-coefficients`, `true`
