---
id: "T-not-BPV-BesselK-halforder-logderivative-square-decreasing"
type: "theorem"
title: "BPV Bessel K half order quotient not decreasing"
status: "proved"
tags: ["bessel", "half-order-explicit", "modified-bessel-k", "monotonicity", "negative-answer", "not-app", "proved", "source-answer-partial", "theorem", "true"]
parents: ["T-BPV-BesselK-halforder-logderivative-square-unimodal"]
refs: ["librarian/audits/LA-20260612T2210-bpv-besselk-halforder-nonmonotone.json", "oracle/responses/OS-20260612T2158Z-bpv-besselk-halforder-oracle-response.md", "raw/student/20260612T2205-bpv-besselk-halforder-nonmonotone.md", "wiki/notes/frontier-bpv-besselk-halforder-monotonicity.md"]
---

# Theorem: BPV Bessel K half order quotient not decreasing

## Statement

For \(\nu=1/2\), the function \(u\mapsto K_\nu'(u)/K_\nu(u)^2\) is not decreasing on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-BPV-BesselK-halforder-logderivative-square-unimodal|BPV Bessel K half order quotient derivative sign unique critical point unimodal]]

## Proof and provenance references

- `librarian/audits/LA-20260612T2210-bpv-besselk-halforder-nonmonotone.json`
- `oracle/responses/OS-20260612T2158Z-bpv-besselk-halforder-oracle-response.md`
- `raw/student/20260612T2205-bpv-besselk-halforder-nonmonotone.md`
- `wiki/notes/frontier-bpv-besselk-halforder-monotonicity.md`

## Proof

Put \(C=\sqrt{\pi/2}\). The half-order identity gives
\[
K_{1/2}(u)=C u^{-1/2}e^{-u}.
\]
Hence
\[
\frac{K_{1/2}'(u)}{K_{1/2}(u)}
=\frac{d}{du}\log K_{1/2}(u)
=-1-\frac{1}{2u}.
\]
Therefore
\[
g(u)=\frac{K_{1/2}'(u)/K_{1/2}(u)}{K_{1/2}(u)}
=-C^{-1}e^u\left(u^{1/2}+\frac12u^{-1/2}\right).
\]
Differentiating,
\[
g'(u)
=-C^{-1}e^u
\left(u^{1/2}+u^{-1/2}-\frac14u^{-3/2}\right)
=-C^{-1}e^u u^{-3/2}\left(u^2+u-\frac14\right).
\]
The quadratic \(u^2+u-\frac14\) has the single positive zero
\[
r=\frac{-1+\sqrt2}{2}.
\]
It is negative on \((0,r)\) and positive on \((r,\infty)\). Since the remaining prefactor in \(g'\) is strictly negative, \(g'(u)>0\) on \((0,r)\) and \(g'(u)<0\) on \((r,\infty)\).

Thus the half-order quotient increases first and then decreases. It is not decreasing on \((0,\infty)\).

_Proof source: `raw/student/20260612T2205-bpv-besselk-halforder-nonmonotone.md`._

## Tags

`bessel`, `half-order-explicit`, `modified-bessel-k`, `monotonicity`, `negative-answer`, `not-app`, `proved`, `source-answer-partial`, `theorem`, `true`
