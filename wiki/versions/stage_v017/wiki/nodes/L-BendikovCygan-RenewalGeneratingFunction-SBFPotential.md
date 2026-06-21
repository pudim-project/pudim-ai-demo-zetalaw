---
id: "L-BendikovCygan-RenewalGeneratingFunction-SBFPotential"
type: "lemma"
title: "Bendikov-Cygan renewal generating function from SBF potential density"
status: "proved"
tags: ["bridge-lemma", "coefficient-extraction", "discrete-subordination", "lemma", "potential-density", "proved", "renewal-sequence", "special-bernstein", "true"]
parents: ["O-BGPW-SpecialBernstein-RenewalDecreasing-source-gate", "D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Laplace-kernel-and-tilted-moment-language", "L-GammaMonotoneDensity-MomentSequence-Decreasing"]
refs: ["private Oracle response", "private Oracle response", "private proof note"]
---

# Lemma: Bendikov-Cygan renewal generating function from SBF potential density

## Statement

For a Bendikov--Cygan source-normalized special Bernstein function \(\psi\), the renewal generating function \(F(z)=\sum_{k\ge0}C_\psi(k)z^k\) satisfies \(F(z)=1/\psi(1-z)\). Using the special-Bernstein potential representation \(1/\psi(\lambda)=b+\int_0^\infty e^{-\lambda t}u(t)\,dt\) with \(b\ge0\) and nonincreasing \(u\), one has \(C_\psi(0)=b+\int_0^\infty e^{-t}u(t)\,dt\) and \(C_\psi(k)=k!^{-1}\int_0^\infty t^k e^{-t}u(t)\,dt\) for \(k\ge1\).

## Dependencies

- [[wiki/nodes/O-BGPW-SpecialBernstein-RenewalDecreasing-source-gate|Bendikov-Cygan special-Bernstein renewal monotonicity source gate]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]
- [[wiki/nodes/L-GammaMonotoneDensity-MomentSequence-Decreasing|Gamma moments of a decreasing density form a decreasing normalized sequence]]

## Proof and provenance references

- `private Oracle response`
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

`bridge-lemma`, `coefficient-extraction`, `discrete-subordination`, `lemma`, `potential-density`, `proved`, `renewal-sequence`, `special-bernstein`, `true`
