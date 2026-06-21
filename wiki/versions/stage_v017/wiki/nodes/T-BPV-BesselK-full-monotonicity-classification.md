---
id: "T-BPV-BesselK-full-monotonicity-classification"
type: "theorem"
title: "BPV Bessel K quotient monotonicity classification"
status: "proved"
tags: ["application-candidate", "bessel", "cited-external-theorem", "modified-bessel-k", "monotonicity-classification", "proved", "source-open-solved", "theorem", "true"]
parents: ["T-BPV-BesselK-open-range-nonmonotone", "O-BPV-BesselK-logderivative-square-monotonicity-source-gate"]
refs: ["private librarian audit", "private proof note"]
---

# Theorem: BPV Bessel K quotient monotonicity classification

## Statement

The function \(u\mapsto K_\nu'(u)/K_\nu(u)^2\) is strictly decreasing on \((0,\infty)\) for \(|\nu|\ge1\), by BPV Theorem 2(a), and is nonmonotone on \((0,\infty)\) for \(|\nu|<1\), by the endpoint-sign theorem.

## Dependencies

- [[wiki/nodes/T-BPV-BesselK-open-range-nonmonotone|BPV Bessel K open range is nonmonotone]]
- [[wiki/nodes/O-BPV-BesselK-logderivative-square-monotonicity-source-gate|BPV Bessel K logarithmic-derivative square monotonicity source gate]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`

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

_Proof source: `private proof note`._

## Do not claim

- Do not claim this is independent of BPV Theorem 2(a) on the closed range.
- Do not public-stage without a separate user request.

## Tags

`application-candidate`, `bessel`, `cited-external-theorem`, `modified-bessel-k`, `monotonicity-classification`, `proved`, `source-open-solved`, `theorem`, `true`
