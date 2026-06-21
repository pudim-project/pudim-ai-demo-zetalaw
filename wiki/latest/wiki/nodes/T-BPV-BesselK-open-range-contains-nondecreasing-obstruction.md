---
id: "T-BPV-BesselK-open-range-contains-nondecreasing-obstruction"
type: "theorem"
title: "BPV open range contains half order nondecreasing obstruction to universal decreasing extension"
status: "proved"
tags: ["bessel", "modified-bessel-k", "natural-extension-refuted", "not-app", "proved", "source-answer-partial", "theorem", "true"]
parents: ["T-not-BPV-BesselK-halforder-logderivative-square-decreasing"]
refs: ["private librarian audit", "private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-bpv-besselk-halforder-monotonicity.md"]
---

# Theorem: BPV open range contains half order nondecreasing obstruction to universal decreasing extension

## Statement

The BPV open range \(|\nu|<1\) contains an order, namely \(\nu=1/2\), for which \(u\mapsto K_\nu'(u)/K_\nu(u)^2\) is not decreasing on \((0,\infty)\). Therefore BPV Theorem 2(a)'s decreasing conclusion for \(|\nu|\ge1\) does not extend universally to \(|\nu|<1\).

## Dependencies

- [[wiki/nodes/T-not-BPV-BesselK-halforder-logderivative-square-decreasing|BPV Bessel K half order quotient not decreasing]]

## Proof and provenance references

- `private librarian audit`
- `private librarian audit`
- `private Oracle response`
- `private proof note`
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

_Proof source: `private proof note`._

## Do not claim

- Do not claim this is a full classification of BPV Question 2.
- Do not claim BPV stated a formal universal-decreasing conjecture.
- Do not count as a strict APP without a later audit upgrading the exact source-match gate.

## Tags

`bessel`, `modified-bessel-k`, `natural-extension-refuted`, `not-app`, `proved`, `source-answer-partial`, `theorem`, `true`
