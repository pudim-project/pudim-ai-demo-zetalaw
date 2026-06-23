---
id: "T-Bazhlekova-Wright-density-topcap-bridge-normal-form"
type: "theorem"
title: "Bazhlekova Wright density topcap bridge normal form"
status: "proved"
tags: ["bazhlekova", "bridge", "laplace-density", "proved", "theorem", "top-cap", "wright-function"]
parents: ["T-positive-Laplace-kernel-complete-monotonicity-principle"]
refs: ["librarian/audits/LA-20260601T041900-bazhlekova-wright-density-bridge-student.json", "oracle/responses/ORACLE-OS-20260601T005309-bazhlekova-wright-density-thresholds-oracle-response.md", "raw/oracle/RO-ORACLE-OS-20260601T005309-bazhlekova-wright-density-thresholds.json", "raw/student/20260601T041900-bazhlekova-wright-density-bridge.md", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova Wright density topcap bridge normal form

## Statement

For the normalized Bazhlekova symbol \(h(s)=s^\alpha(1+s^{-p})^{1/2}\), with \(0<\beta=\alpha-p/2<\alpha<1\) and the principal branch in the no-cover seed range, define \(\mathcal W_{\alpha,p}(x)=-\sum_{m\ge0}\binom{1/2}{m}x^m/\Gamma(pm-\alpha)\). Then \(\mathcal L^{-1}\{h'\}(t)=t^{-\alpha}\mathcal W_{\alpha,p}(t^p)\), and the Wright top-cap limit has the same sign as \(\mathcal W_{\alpha,p}(\lambda^{-1})\). Thus normalized derivative density positivity and top-cap positivity are the same Wright-function sign problem.

## Dependencies

- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]

## Proof and provenance references

- `librarian/audits/LA-20260601T041900-bazhlekova-wright-density-bridge-student.json`
- `oracle/responses/ORACLE-OS-20260601T005309-bazhlekova-wright-density-thresholds-oracle-response.md`
- `raw/oracle/RO-ORACLE-OS-20260601T005309-bazhlekova-wright-density-thresholds.json`
- `raw/student/20260601T041900-bazhlekova-wright-density-bridge.md`
- `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`

## Proof

Put
\[
\alpha=\frac a2,\qquad p=a-b,\qquad \beta=\frac b2=\alpha-\frac p2,
\]
so that
\[
h(s)=s^{b/2}(1+s^{a-b})^{1/2}
=s^\alpha(1+s^{-p})^{1/2}.
\]
At the two no-cover seeds,
\[
(\alpha,p)=\left(\frac34,\frac{11}{10}\right),
\qquad
(\alpha,p)=\left(\frac{11}{20},\frac{21}{20}\right),
\]
and \(0<\beta<\alpha<1\), \(1<p<2\).

Define the Wright-normalized series
\[
\mathcal W_{\alpha,p}(x)
=
-\sum_{m=0}^{\infty}
\binom{1/2}{m}\frac{x^m}{\Gamma(pm-\alpha)}.
\]
The coefficient ratio and the gamma denominator show that this series is entire in \(x\).

For \(s>1\), the binomial expansion gives
\[
h'(s)
=
\sum_{m=0}^{\infty}
\binom{1/2}{m}(\alpha-pm)s^{\alpha-pm-1}.
\]
For each \(m\), analytic continuation of the elementary Laplace formula gives
\[
\mathcal L\left\{
\frac{t^{pm-\alpha}}{\Gamma(pm-\alpha)}
\right\}(s)
=(pm-\alpha)s^{\alpha-pm-1}.
\]
Therefore
\[
\mathcal L^{-1}\{h'\}(t)
=
-\sum_{m=0}^{\infty}
\binom{1/2}{m}
\frac{t^{pm-\alpha}}{\Gamma(pm-\alpha)}
=
t^{-\alpha}\mathcal W_{\alpha,p}(t^p).
\]
For \(1<p<2\) the Wright series has subexponential growth, so the Laplace transform is defined on \(s>0\). Equality for \(s>1\) extends to \(s>0\) by analytic continuation on the principal branch.

Consequently, at the no-cover seeds, complete monotonicity of \(h'\) is equivalent to
\[
\mathcal W_{\alpha,p}(x)\ge0
\qquad(x>0),
\]
because the inverse Laplace transform is the locally integrable density above.

The previous top-cap audit used the signed polynomials \(R_n(y)=(-1)^{n-1}Q_n(y)\). Its formal top-cap function was
\[
W^{\mathrm{top}}_{\alpha,p}(\lambda)
=
1-\frac{\Gamma(1-\alpha)}{\alpha}
\sum_{m\ge1}\binom{1/2}{m}
\frac{\lambda^{-m}}{\Gamma(pm-\alpha)}.
\]
Since
\[
-\frac1{\Gamma(-\alpha)}
=\frac{\alpha}{\Gamma(1-\alpha)},
\]
the two normalizations satisfy
\[
W^{\mathrm{top}}_{\alpha,p}(\lambda)
=
\frac{\Gamma(1-\alpha)}{\alpha}
\mathcal W_{\alpha,p}(\lambda^{-1}).
\]
The factor \(\Gamma(1-\alpha)/\alpha\) is positive. Thus top-cap positivity and normalized derivative density positivity are the same sign problem after \(x=\lambda^{-1}\).

_Proof source: `raw/student/20260601T041900-bazhlekova-wright-density-bridge.md`._

## Tags

`bazhlekova`, `bridge`, `laplace-density`, `proved`, `theorem`, `top-cap`, `wright-function`
