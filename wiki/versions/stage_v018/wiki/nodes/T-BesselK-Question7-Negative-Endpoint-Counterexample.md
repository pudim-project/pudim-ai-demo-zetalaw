---
id: "T-BesselK-Question7-Negative-Endpoint-Counterexample"
type: "theorem"
title: "BPV Bessel K Question 7 has a half-order endpoint counterexample"
status: "proved"
tags: ["application-candidate", "bessel-k", "derivative-sign", "endpoint-obstruction", "half-order", "open-problem-solved", "proved", "source-solving", "strict-private-plus10", "theorem", "true"]
parents: ["D-BesselK-Endpoint-Monotonicity-Question", "L-HalfOrder-BesselK-ClosedForm", "L-HalfOrder-KDerivative-SignRoot", "O-BesselK-Question7-Monotonicity-source-gate"]
refs: ["librarian/audits/LA-20260613T2308-besselk-q7-strict-app.json", "oracle/responses/OS-20260613T225958Z-oracle-response.md", "raw/student/20260613T2305-besselk-q7-endpoint-counterexample.md", "raw/student/20260614T-v016-besselk-q7-public.md"]
---

# Theorem: BPV Bessel K Question 7 has a half-order endpoint counterexample

## Statement

Baricz--Ponnusamy--Vuorinen Question 7 has a negative answer: \(u\mapsto u^2K_\nu'(u)\) is not strictly decreasing on \((0,2)\) for all \(|\nu|\le1/2\). The endpoint \(\nu=1/2\) has \((u^2K_{1/2}'(u))'>0\) on \(((1+\sqrt2)/2,2)\).

## Dependencies

- [[wiki/nodes/D-BesselK-Endpoint-Monotonicity-Question|BPV Bessel K endpoint monotonicity question]]
- [[wiki/nodes/L-HalfOrder-BesselK-ClosedForm|Half-order modified Bessel K closed form]]
- [[wiki/nodes/L-HalfOrder-KDerivative-SignRoot|Half-order Bessel K endpoint derivative has a sign root]]
- [[wiki/nodes/O-BesselK-Question7-Monotonicity-source-gate|Bessel K half-order monotonicity interval source gate]]

## Proof and provenance references

- `librarian/audits/LA-20260613T2308-besselk-q7-strict-app.json`
- `oracle/responses/OS-20260613T225958Z-oracle-response.md`
- `raw/student/20260613T2305-besselk-q7-endpoint-counterexample.md`
- `raw/student/20260614T-v016-besselk-q7-public.md`

## Proof

At the admissible endpoint \(\nu=1/2\),
\[
K_{1/2}(u)=\sqrt{\frac{\pi}{2u}}e^{-u}.
\]
With \(c=\sqrt{\pi/2}\),
\[
u^2K_{1/2}'(u)=-c e^{-u}\left(u^{3/2}+\frac12u^{1/2}\right).
\]
Differentiating gives
\[
\frac{d}{du}\{u^2K_{1/2}'(u)\}
=ce^{-u}u^{-1/2}\left(u^2-u-\frac14\right).
\]
The quadratic has positive root \((1+\sqrt2)/2\). Hence the derivative is positive on \(((1+\sqrt2)/2,2)\), so \(u\mapsto u^2K_{1/2}'(u)\) is increasing on a subinterval of \((0,2)\) and cannot be strictly decreasing there.

_Proof source: `raw/student/20260614T-v016-besselk-q7-public.md`._

## Do not claim

- Do not claim BPV Question 2 is solved by this theorem.
- Do not claim any other BPV Bessel K open question is solved.
- Do not claim public APP registry assignment.
- Do not public-stage without user request.

## Tags

`application-candidate`, `bessel-k`, `derivative-sign`, `endpoint-obstruction`, `half-order`, `open-problem-solved`, `proved`, `source-solving`, `strict-private-plus10`, `theorem`, `true`
