---
id: "T-KP-balanced-2F1-Dirac-Stieltjes-measure"
type: "theorem"
title: "balanced 2F1 hypergeometric Stieltjes representation has Dirac measure at one"
status: "proved"
tags: ["attack-plan", "dirac-measure", "hypergeometric", "proved", "stieltjes", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private attack plan", "private librarian audit", "private proof note", "wiki/notes/frontier-kp-hypergeometric-stieltjes.md"]
---

# Theorem: balanced 2F1 hypergeometric Stieltjes representation has Dirac measure at one

## Statement

For \(a>0\) and \(\sigma>0\), \({}_2F_1(\sigma,a;a;-z)=(1+z)^{-\sigma}\), so the generalized Stieltjes representing measure on \([0,1]\) is the Dirac mass \(\delta_1\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private proof note`
- `wiki/notes/frontier-kp-hypergeometric-stieltjes.md`

## Proof

This is a bounded pass. It proves the \(q=1\) balanced Dirac representation, records the source's \(q=2\) balanced formula, and leaves the general \(q\) balanced representing-measure problem open.

For \(a>0\) and \(\sigma>0\), the Gauss hypergeometric series gives
\[
{}_{2}F_1(\sigma,a;a;-z)
=\sum_{n=0}^{\infty}\frac{(\sigma)_n(a)_n}{(a)_n n!}(-z)^n
=\sum_{n=0}^{\infty}\frac{(\sigma)_n}{n!}(-z)^n.
\]
By the binomial theorem,
\[
\sum_{n=0}^{\infty}\frac{(\sigma)_n}{n!}(-z)^n=(1+z)^{-\sigma}.
\]
The generalized Stieltjes kernel at \(t=1\) is exactly
\[
\int_{[0,1]}\frac{d\delta_1(t)}{(1+tz)^\sigma}
=\frac{1}{(1+z)^\sigma}.
\]
Therefore the balanced \(q=1\) representing measure is \(\delta_1\).

Karp--Prilepkina explicitly compute the limiting representing measure for the balanced \(q=2\) case \(b_1+b_2=a_1+a_2\), under the source's admissibility assumptions. In the notation of the source, they obtain an atom at \(t=1\) and a continuous part such that
\[
{}_{3}F_2(\sigma,a_1,a_2;b_1,b_2;-z)
\]
is represented as a generalized Stieltjes transform with kernel \((1+tz)^{-\sigma}\), with continuous density proportional to
\[
t^{a_2-1}
{}_{2}F_1(b_1-a_1+1,b_2-a_1+1;2;1-t).
\]

The source derives this by taking the limit \(b_1+b_2-a_1-a_2\to0\) in its positive-measure representation and states that the same formula may also be checked by comparing power-series coefficients and using Gauss summation.

_Proof source: `private proof note`._

## Tags

`attack-plan`, `dirac-measure`, `hypergeometric`, `proved`, `stieltjes`, `theorem`
