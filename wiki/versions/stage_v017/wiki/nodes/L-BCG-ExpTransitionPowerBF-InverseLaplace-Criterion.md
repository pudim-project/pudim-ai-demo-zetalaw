---
id: "L-BCG-ExpTransitionPowerBF-InverseLaplace-Criterion"
type: "lemma"
title: "BCG exponential-transition power Bernstein inverse-Laplace criterion"
status: "proved"
tags: ["beghin-cristofaro-garrappa", "bernstein-function", "criterion", "inverse-laplace", "lemma", "levy-density", "not-app", "primitive", "proved", "scarpi-derivative", "true"]
parents: ["O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold", "T-Referenced-Bernstein-Widder-Positive-Laplace-Density-Criterion-20260609"]
refs: ["private Oracle response", "private Oracle audit", "private proof note"]
---

# Lemma: BCG exponential-transition power Bernstein inverse-Laplace criterion

## Statement

Let F_{a1,a2,c}(s)=s^((a2*c+a1*s)/(c+s)), where 0<a1,a2<1 and c>0. Define K_{a1,a2,c} as the inverse Laplace transform of F'_{a1,a2,c}, equivalently of s^((a2*c+a1*s)/(c+s))*((a2*c+a1*s)/(s*(c+s))+(a1-a2)*c*log(s)/(s+c)^2). Then F_{a1,a2,c} is a Bernstein function if and only if K_{a1,a2,c} is a nonnegative measure on (0,infinity).

## Dependencies

- [[wiki/nodes/O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold|Beghin-Cristofaro-Garrappa exponential-transition power Bernstein threshold]]
- T-Referenced-Bernstein-Widder-Positive-Laplace-Density-Criterion-20260609

## Proof and provenance references

- `private Oracle response`
- `private Oracle audit`
- `private proof note`

## Proof

For
\[
F_{a_1,a_2,c}(s)=s^{(a_2c+a_1s)/(c+s)},
\qquad 0<a_1,a_2<1,\quad c>0,
\]
try to characterize the Bernstein property through a positive Levy-density or inverse-Laplace sign criterion.

Put
\[
q(s)=\frac{a_2c+a_1s}{c+s}
=a_1+\frac{(a_2-a_1)c}{s+c}.
\]
Then
\[
F(s)=s^{q(s)}
\]
and
\[
F'(s)
=F(s)\left(
\frac{a_2c+a_1s}{s(c+s)}
+\frac{(a_1-a_2)c\log s}{(s+c)^2}
\right).
\]

Since \(F(s)\sim s^{a_1}\), one has \(F'(s)\sim a_1s^{a_1-1}\to0\) as \(s\to\infty\). Therefore \(F\) is a Bernstein function if and only if \(F'\) is completely monotone, equivalently if and only if
\[
K_{a_1,a_2,c}
=
\mathcal L^{-1}\left[
s^{(a_2c+a_1s)/(c+s)}
\left(
\frac{a_2c+a_1s}{s(c+s)}
+\frac{(a_1-a_2)c\log s}{(s+c)^2}
\right)
\right]
\]
is a nonnegative measure on \((0,\infty)\).

This is exact but tautological unless one can identify or estimate \(K\) with a positive kernel.

The Levy-density route has not produced a certifiable positive-density theorem or parameter-region classification. The useful output is the exact inverse-Laplace criterion and a clear next direction:

use the signed moment identities
\[
(-1)^nF^{(n+1)}(s)
=
\int_0^\infty t^n e^{-st}\,K_{a_1,a_2,c}(dt)
\]
to organize derivative sign failures as signed-density moment witnesses. This matches the admitted \(F''(1)\) obstruction and the admitted moving-point high-order obstruction.

_Proof source: `private proof note`._

## Do not claim

- Do not claim this gives an explicit positive density.
- Do not claim the BCG threshold is solved.
- Do not claim complete Bernstein status.

## Tags

`beghin-cristofaro-garrappa`, `bernstein-function`, `criterion`, `inverse-laplace`, `lemma`, `levy-density`, `not-app`, `primitive`, `proved`, `scarpi-derivative`, `true`
