---
id: "B-WeibullShapeGreaterThanOne-NotCompletelyMonotone"
type: "lemma"
title: "Weibull tail with shape greater than one is not completely monotone"
status: "proved"
tags: ["app-0091-bridge", "complete-monotonicity", "endpoint-obstruction", "lemma", "proved", "second-derivative", "true", "weibull-tail"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Endpoint-obstruction-certificate-language"]
refs: ["raw/student/20260623T0016-equation16-weibull-noncm.md"]
---

# Lemma: Weibull tail with shape greater than one is not completely monotone

## Statement

If \(c>0\) and \(\alpha>1\), then \(F(x)=e^{-cx^\alpha}\) is not completely monotone on \((0,\infty)\). In fact \(F''(x)<0\) for all sufficiently small positive \(x\).

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]

## Proof and provenance references

- `raw/student/20260623T0016-equation16-weibull-noncm.md`

## Proof

This proof addresses the literal transformed nonlinear tail equation printed as
\[
F(x)=\int_0^\infty F(xb)^2\,\mathbb P(\widetilde B\in db).
\]

The source observes that this equation has the same form as the completely
monotone Laplace-transform equation, but here one seeks only a non-increasing
tail-type function \(F\), and explicitly asks whether solutions that are not
completely monotone exist.

The APP statement is deliberately restricted to this literal equation-(16)
existential question. It does not classify all laws of \(\widetilde B\), and it
does not translate the witness back through the source's sign convention for
the original \(\xi\)-equation.

Fix \(b\in(1/2,1)\) and \(c>0\), and define
\[
\alpha=\frac{\log(1/2)}{\log b}.
\]
Then \(\log b<0\), so \(\alpha>1\), and
\[
b^\alpha=\exp(\alpha\log b)=\frac12.
\]
Let \(\widetilde B=b\) almost surely and set
\[
F(x)=e^{-cx^\alpha},\qquad x\ge0.
\]

Then \(F(0)=1\), \(0<F\le1\), \(F\) is continuous and decreasing, and
\(F(x)\to0\) as \(x\to\infty\). Hence \(F\) is a survival function, namely of
the Weibull law with density
\[
f_\eta(x)=c\alpha x^{\alpha-1}e^{-cx^\alpha},\qquad x>0.
\]

For deterministic \(\widetilde B=b\),
\[
\int_0^\infty F(xu)^2\,\mathbb P(\widetilde B\in du)
=F(bx)^2
=\exp(-2cb^\alpha x^\alpha)
=\exp(-cx^\alpha)
=F(x).
\]
Thus \(F\) solves the printed equation (16).

Complete monotonicity on \((0,\infty)\) would imply \(F''(x)\ge0\) for all
\(x>0\). Direct differentiation gives
\[
F''(x)=c\alpha x^{\alpha-2}e^{-cx^\alpha}
\left(c\alpha x^\alpha-(\alpha-1)\right).
\]
Since \(\alpha>1\), for
\[
0<x<\left(\frac{\alpha-1}{c\alpha}\right)^{1/\alpha}
\]
the term in parentheses is negative, while the prefactor is positive. Hence
\(F''(x)<0\) on a nonempty interval and \(F\) is not completely monotone.

_Proof source: `raw/student/20260623T0016-equation16-weibull-noncm.md`._

## Tags

`app-0091-bridge`, `complete-monotonicity`, `endpoint-obstruction`, `lemma`, `proved`, `second-derivative`, `true`, `weibull-tail`
