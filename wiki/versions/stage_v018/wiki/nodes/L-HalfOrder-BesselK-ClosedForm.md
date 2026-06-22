---
id: "L-HalfOrder-BesselK-ClosedForm"
type: "lemma"
title: "Half-order modified Bessel K closed form"
status: "proved"
tags: ["bessel-k", "bridge-lemma", "closed-form", "half-order", "lemma", "proved", "true"]
parents: ["D-Endpoint-obstruction-certificate-language", "T-Special-function-normal-form-calculus-principle"]
refs: ["oracle/responses/OFC-20260613T225236Z-oracle-first-contact-response.md", "raw/student/20260613T2305-besselk-q7-endpoint-counterexample.md", "raw/student/20260614T-v016-besselk-q7-public.md"]
---

# Lemma: Half-order modified Bessel K closed form

## Statement

For \(u>0\), \(K_{1/2}(u)=\sqrt{\pi/(2u)}e^{-u}\).

## Dependencies

- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]
- [[wiki/nodes/T-Special-function-normal-form-calculus-principle|Special-function normal-form calculus principle]]

## Proof and provenance references

- `oracle/responses/OFC-20260613T225236Z-oracle-first-contact-response.md`
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

`bessel-k`, `bridge-lemma`, `closed-form`, `half-order`, `lemma`, `proved`, `true`
