---
id: "L-HalfOrder-KDerivative-SignRoot"
type: "lemma"
title: "Half-order Bessel K endpoint derivative has a sign root"
status: "proved"
tags: ["bessel-k", "bridge-lemma", "derivative-sign", "endpoint-obstruction", "lemma", "proved", "quadratic-certificate", "true"]
parents: ["L-HalfOrder-BesselK-ClosedForm", "D-Endpoint-obstruction-certificate-language", "T-endpoint-log-derivative-monotonicity-principle", "T-Special-function-normal-form-calculus-principle"]
refs: ["librarian/audits/LA-20260613T2308-besselk-q7-strict-app.json", "oracle/responses/OS-20260613T225958Z-oracle-response.md", "raw/student/20260613T2305-besselk-q7-endpoint-counterexample.md", "raw/student/20260614T-v016-besselk-q7-public.md"]
---

# Lemma: Half-order Bessel K endpoint derivative has a sign root

## Statement

Let \(F(u)=u^2K_{1/2}'(u)\). Then \(F'(u)=\sqrt{\pi/2}e^{-u}u^{-1/2}(u^2-u-1/4)\), so \(F'(u)>0\) for \(u>(1+\sqrt2)/2\), in particular on a nonempty subinterval of \((0,2)\).

## Dependencies

- [[wiki/nodes/L-HalfOrder-BesselK-ClosedForm|Half-order modified Bessel K closed form]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]
- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]
- [[wiki/nodes/T-Special-function-normal-form-calculus-principle|Special-function normal-form calculus principle]]

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

## Tags

`bessel-k`, `bridge-lemma`, `derivative-sign`, `endpoint-obstruction`, `lemma`, `proved`, `quadratic-certificate`, `true`
