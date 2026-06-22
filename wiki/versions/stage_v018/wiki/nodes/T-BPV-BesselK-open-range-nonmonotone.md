---
id: "T-BPV-BesselK-open-range-nonmonotone"
type: "theorem"
title: "BPV Bessel K open range is nonmonotone"
status: "proved"
tags: ["application-candidate", "bessel", "endpoint-obstruction", "modified-bessel-k", "monotonicity-classification", "proved", "source-open-solved", "theorem", "true"]
parents: ["O-BPV-BesselK-logderivative-square-monotonicity-source-gate", "T-BPV-BesselK-halforder-logderivative-square-unimodal"]
refs: ["librarian/audits/LA-20260613T0330-bpv-open-range-nonmonotone-strict-app.json", "oracle/responses/OS-20260613Tbpv-besselk-open-range-nonmonotone-oracle-response.md", "raw/student/20260613T0325-bpv-besselk-open-range-nonmonotone.md"]
---

# Theorem: BPV Bessel K open range is nonmonotone

## Statement

For every \(|\nu|<1\), the function \(g_\nu(u)=K_\nu'(u)/K_\nu(u)^2\) is not monotone on \((0,\infty)\). More precisely, \(g_\nu'(u)>0\) for all sufficiently small \(u>0\), while \(g_\nu'(u)<0\) for all sufficiently large \(u\).

## Dependencies

- [[wiki/nodes/O-BPV-BesselK-logderivative-square-monotonicity-source-gate|BPV Bessel K logarithmic-derivative square monotonicity source gate]]
- [[wiki/nodes/T-BPV-BesselK-halforder-logderivative-square-unimodal|BPV Bessel K half order quotient derivative sign unique critical point unimodal]]

## Proof and provenance references

- `librarian/audits/LA-20260613T0330-bpv-open-range-nonmonotone-strict-app.json`
- `oracle/responses/OS-20260613Tbpv-besselk-open-range-nonmonotone-oracle-response.md`
- `raw/student/20260613T0325-bpv-besselk-open-range-nonmonotone.md`

## Proof

Since \(K_{-\nu}=K_\nu\), it is enough to treat \(0\le\nu<1\). Put
\[
y_\nu(u)=\frac{uK_\nu'(u)}{K_\nu(u)}.
\]
The modified Bessel equation gives
\[
K_\nu''(u)=\left(1+\frac{\nu^2}{u^2}\right)K_\nu(u)-\frac1uK_\nu'(u).
\]
Differentiating \(g_\nu=K_\nu'/K_\nu^2\) yields
\[
g_\nu'(u)=\frac{K_\nu K_\nu''-2(K_\nu')^2}{K_\nu^3}
=\frac{F_\nu(u)}{u^2K_\nu(u)},
\]
where
\[
F_\nu(u)=u^2+\nu^2-y_\nu(u)-2y_\nu(u)^2.
\]
Since \(K_\nu(u)>0\) on \((0,\infty)\), the sign of \(g_\nu'\) is the sign of \(F_\nu\).

First assume \(0<\nu<1\). The standard small-argument expansion
\[
K_\nu(u)\sim 2^{\nu-1}\Gamma(\nu)u^{-\nu}
\]
gives \(y_\nu(u)\to-\nu\) as \(u\downarrow0\). Hence
\[
F_\nu(u)\to \nu^2+\nu-2\nu^2=\nu(1-\nu)>0.
\]
Thus \(g_\nu'(u)>0\) for all sufficiently small \(u>0\).

For \(\nu=0\), the standard expansions
\[
K_0(u)\sim-\log(u/2)-\gamma,\qquad K_0'(u)=-K_1(u)\sim-\frac1u
\]
give
\[
y_0(u)\sim-\frac{1}{-\log(u/2)-\gamma}\to0^-.
\]
Writing \(a(u)=-y_0(u)>0\), for all sufficiently small \(u\) we have \(a(u)<1/2\), and therefore
\[
F_0(u)=u^2-y_0(u)-2y_0(u)^2
=u^2+a(u)(1-2a(u))>0.
\]
So \(g_0'(u)>0\) near zero.

For large \(u\), the standard expansion
\[
\frac{K_\nu'(u)}{K_\nu(u)}
=-1-\frac{1}{2u}+O(u^{-2})
\]
gives
\[
y_\nu(u)=-u-\frac12+O(u^{-1}).
\]
Substituting into \(F_\nu\),
\[
F_\nu(u)
=u^2+\nu^2-y_\nu(u)-2y_\nu(u)^2
=-u^2-u+\nu^2+O(1)<0
\]
for all sufficiently large \(u\). Thus \(g_\nu'(u)<0\) eventually.

The derivative has opposite signs near the two endpoints. Therefore \(g_\nu\) is neither increasing nor decreasing on \((0,\infty)\) for every \(|\nu|<1\).

_Proof source: `raw/student/20260613T0325-bpv-besselk-open-range-nonmonotone.md`._

## Do not claim

- Do not claim exact critical-point counts for \(|\nu|<1\); only endpoint-sign nonmonotonicity is proved.
- Do not public-stage without a separate user request.

## Tags

`application-candidate`, `bessel`, `endpoint-obstruction`, `modified-bessel-k`, `monotonicity-classification`, `proved`, `source-open-solved`, `theorem`, `true`
