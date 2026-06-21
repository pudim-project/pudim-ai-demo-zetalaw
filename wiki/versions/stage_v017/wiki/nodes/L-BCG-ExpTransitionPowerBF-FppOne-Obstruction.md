---
id: "L-BCG-ExpTransitionPowerBF-FppOne-Obstruction"
type: "lemma"
title: "BCG exponential-transition power BF pointwise second-derivative obstruction"
status: "proved"
tags: ["beghin-cristofaro-garrappa", "bernstein-function", "consolidation-primitive-bait", "lemma", "pointwise-obstruction", "primitive", "proved", "scarpi-derivative", "true", "variable-order-fractional-relaxation"]
parents: ["O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold"]
refs: ["private librarian audit", "private Oracle response", "private proof note"]
---

# Lemma: BCG exponential-transition power BF pointwise second-derivative obstruction

## Statement

Let \(c>0\) and \(0<a_1,a_2<1\). Define \(F(s)=s^{(a_2c+a_1s)/(c+s)}\) on \((0,\infty)\). If \(F\) is a Bernstein function, then \((a_2c+a_1)^2-(a_2c+a_1)(c+1)+2c(a_1-a_2)\le 0\).

## Dependencies

- [[wiki/nodes/O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold|Beghin-Cristofaro-Garrappa exponential-transition power Bernstein threshold]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`

## Proof

Put
\[
E(s)=\frac{a_2c+a_1s}{c+s},\qquad g(s)=\log F(s)=E(s)\log s.
\]
Since \(F=e^g\), we have
\[
F''(s)=F(s)\left(g''(s)+(g'(s))^2\right).
\]

A Bernstein function has completely monotone derivative, hence \(F''(s)\le 0\) for all \(s>0\). In particular, if \(F\) is Bernstein, then \(F''(1)\le0\).

Now
\[
E'(s)=\frac{c(a_1-a_2)}{(c+s)^2}.
\]
Also
\[
g'(s)=E'(s)\log s+\frac{E(s)}s,
\]
so
\[
g'(1)=E(1)=\frac{a_2c+a_1}{c+1}.
\]
Differentiating once more,
\[
g''(s)=E''(s)\log s+\frac{2E'(s)}s-\frac{E(s)}{s^2}.
\]
The logarithmic term vanishes at \(s=1\), and therefore
\[
g''(1)=2E'(1)-E(1)
=\frac{2c(a_1-a_2)}{(c+1)^2}-\frac{a_2c+a_1}{c+1}.
\]
Since \(F(1)=1\),
\[
F''(1)=g''(1)+(g'(1))^2.
\]
Thus
\[
F''(1)=
\frac{(a_2c+a_1)^2-(a_2c+a_1)(c+1)+2c(a_1-a_2)}
{(c+1)^2}.
\]
The denominator is positive. Therefore \(F''(1)\le0\) implies
\[
(a_2c+a_1)^2-(a_2c+a_1)(c+1)+2c(a_1-a_2)\le 0,
\]
as claimed.

This is only a necessary condition for \(F\) to be Bernstein. It does not prove sufficiency and does not solve the full BCG parameter-threshold problem.

_Proof source: `private proof note`._

## Tags

`beghin-cristofaro-garrappa`, `bernstein-function`, `consolidation-primitive-bait`, `lemma`, `pointwise-obstruction`, `primitive`, `proved`, `scarpi-derivative`, `true`, `variable-order-fractional-relaxation`
