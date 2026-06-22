---
id: "L-MaxEntropy-Pick-Mobius-Inversion"
type: "lemma"
title: "Nevanlinna Pick parameter extraction by Mobius inversion"
status: "proved"
tags: ["bridge-lemma", "lemma", "moment-problem", "nevanlinna-parametrization", "pick-function", "proved", "stieltjes-transform", "true"]
parents: ["O-MaxEntropy-indeterminate-moment-Pick-parameter-source-gate", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260612T1030-maxentropy-pick-bridge-audit.json", "oracle/responses/OS-20260612T1020Z-maxentropy-pick-live-oracle-response.md", "raw/student/20260612T1030-maxentropy-pick-bridge-and-lognormal-obstruction.md"]
---

# Lemma: Nevanlinna Pick parameter extraction by Mobius inversion

## Statement

Under Berg's convention \(S_\mu(z)=\int (x-z)^{-1}\,d\mu(x)\) and \(S_\varphi(z)=-(A(z)\varphi(z)-C(z))/(B(z)\varphi(z)-D(z))\), the corresponding Pick parameter is \(\varphi(z)=(D(z)S_\mu(z)+C(z))/(B(z)S_\mu(z)+A(z))\) wherever the denominator is nonzero.

## Dependencies

- [[wiki/nodes/O-MaxEntropy-indeterminate-moment-Pick-parameter-source-gate|Maximum-entropy density Pick parameter in indeterminate moment classes source gate]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260612T1030-maxentropy-pick-bridge-audit.json`
- `oracle/responses/OS-20260612T1020Z-maxentropy-pick-live-oracle-response.md`
- `raw/student/20260612T1030-maxentropy-pick-bridge-and-lognormal-obstruction.md`

## Proof

Berg's Nevanlinna parametrization uses the Stieltjes transform convention
\[
S_\mu(z)=\int_{\mathbb R}\frac{d\mu(x)}{x-z}
\]
and
\[
S_\varphi(z)=-\frac{A(z)\varphi(z)-C(z)}{B(z)\varphi(z)-D(z)}.
\]
If \(S=S_\varphi\), then
\[
S(B\varphi-D)=C-A\varphi,
\]
so
\[
(A+BS)\varphi=C+DS.
\]
Thus
\[
\varphi(z)=\frac{C(z)+D(z)S(z)}{A(z)+B(z)S(z)}.
\]
Equivalently,
\[
\varphi(z)=\frac{D(z)S(z)+C(z)}{B(z)S(z)+A(z)}.
\]

This is a valid parameter extraction lemma once the relevant density or Stieltjes transform is already known. It is not, by itself, a solution of Berg's open problem, because the problem is to identify the parameter for \(g_{h\max}\), and the transform of \(g_{h\max}\) is not given.

Let
\[
g_0(x)=\frac{1}{\sqrt{2\pi}x}\exp\left(-\frac{(\log x)^2}{2}\right)
\]
be the standard lognormal density and set
\[
p(x)=\sin(2\pi\log x),\qquad g_\varepsilon(x)=g_0(x)(1+\varepsilon p(x)).
\]
For \(|\varepsilon|\le1\), \(g_\varepsilon\ge0\). The perturbation preserves all integer moments. With \(Y=\log X\sim N(0,1)\),
\[
\int_0^\infty x^k g_0(x)p(x)\,dx
=
\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{ky-y^2/2}\sin(2\pi y)\,dy
=
\Im\exp\left(\frac{(k+2\pi i)^2}{2}\right)
=0
\]
for every integer \(k\ge0\).

For Shannon entropy \(H[g]=-\int g\log g\),
\[
\frac{d}{d\varepsilon}H[g_\varepsilon]\bigg|_{\varepsilon=0}
=-\int g_0p(\log g_0+1)\,dx.
\]
Since
\[
\log g_0(e^Y)=-\frac12Y^2-Y-\frac12\log(2\pi),
\]
the constant and \(Y^2\) terms integrate to zero against \(\sin(2\pi Y)\), while
\[
\frac{d}{d\varepsilon}H[g_\varepsilon]\bigg|_{\varepsilon=0}
=\mathbb E[Y\sin(2\pi Y)]
=2\pi e^{-2\pi^2}>0.
\]
Therefore the standard lognormal density is not stationary for Shannon entropy over the usual density class with the same integer moments.

This does not solve Berg's source problem. It shows:

the transform-inversion formula is a bridge once \(S_{h\max}\) is known;
a naive route through "the lognormal density is \(g_{h\max}\)" is locally obstructed under the usual moment-preserving density class;
the true maximum-entropy density, if it exists in the source's intended class, must satisfy a moment-null stationarity condition.

Do not promote this as an APP.

_Proof source: `raw/student/20260612T1030-maxentropy-pick-bridge-and-lognormal-obstruction.md`._

## Do not claim

- Do not claim this identifies the unknown maximum-entropy density.
- Do not claim this solves Berg's open problem unless the relevant Stieltjes transform is independently known in the source's required sense.

## Tags

`bridge-lemma`, `lemma`, `moment-problem`, `nevanlinna-parametrization`, `pick-function`, `proved`, `stieltjes-transform`, `true`
