---
id: "T-BendikovCygan-SBF-RenewalSequence-Nonincreasing"
type: "theorem"
title: "Bendikov-Cygan special-Bernstein renewal sequence is nonincreasing"
status: "proved"
tags: ["application-candidate", "discrete-subordination", "gamma-covariance", "open-problem-solved", "proved", "renewal-sequence", "source-solving", "special-bernstein", "strict-private-post-v016", "theorem", "true"]
parents: ["O-BGPW-SpecialBernstein-RenewalDecreasing-source-gate", "L-BendikovCygan-RenewalGeneratingFunction-SBFPotential", "L-GammaMonotoneDensity-MomentSequence-Decreasing"]
refs: ["oracle/responses/OS-20260620T0410Z-bendikov-cygan-sbf-renewal-oracle-response.md", "raw/student/20260620T0418-bendikov-cygan-sbf-renewal-positive.md"]
---

# Theorem: Bendikov-Cygan special-Bernstein renewal sequence is nonincreasing

## Statement

For every Bendikov--Cygan source-normalized special Bernstein function \(\psi\), the discrete renewal sequence \(C_\psi(k)\) is nonincreasing: \(C_\psi(k+1)\le C_\psi(k)\) for every \(k\ge0\). Consequently the Bendikov--Cygan open question asking whether special Bernstein functions have decreasing discrete renewal sequences is answered affirmatively, with decreasing interpreted as nonincreasing.

## Dependencies

- [[wiki/nodes/O-BGPW-SpecialBernstein-RenewalDecreasing-source-gate|Bendikov-Cygan special-Bernstein renewal monotonicity source gate]]
- [[wiki/nodes/L-BendikovCygan-RenewalGeneratingFunction-SBFPotential|Bendikov-Cygan renewal generating function from SBF potential density]]
- [[wiki/nodes/L-GammaMonotoneDensity-MomentSequence-Decreasing|Gamma moments of a decreasing density form a decreasing normalized sequence]]

## Proof and provenance references

- `oracle/responses/OS-20260620T0410Z-bendikov-cygan-sbf-renewal-oracle-response.md`
- `raw/student/20260620T0418-bendikov-cygan-sbf-renewal-positive.md`

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

_Proof source: `raw/student/20260620T0418-bendikov-cygan-sbf-renewal-positive.md`._

## Do not claim

- Do not describe the result as strict decrease; the identity exponent gives equality.
- Do not preserve the earlier BGPW attribution in public-facing text; the exact source is Bendikov--Cygan.
- Do not public-stage without user request.

## Tags

`application-candidate`, `discrete-subordination`, `gamma-covariance`, `open-problem-solved`, `proved`, `renewal-sequence`, `source-solving`, `special-bernstein`, `strict-private-post-v016`, `theorem`, `true`
