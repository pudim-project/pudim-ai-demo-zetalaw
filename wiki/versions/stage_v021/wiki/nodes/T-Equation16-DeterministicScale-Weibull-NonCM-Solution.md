---
id: "T-Equation16-DeterministicScale-Weibull-NonCM-Solution"
type: "theorem"
title: "Jonckheere-Shneer equation (16) has a deterministic-scale non-CM Weibull solution"
status: "proved"
tags: ["app-0091-candidate", "app-candidate", "complete-monotonicity", "distributional-equation", "endpoint-obstruction", "front-propagation", "jonckheere-shneer", "negative-answer", "primitive-growth", "proved", "source-open-solved", "survival-function", "theorem", "true", "weibull-tail"]
parents: ["O-JonckheereShneer-Equation16-NonCM-Solution-source-gate", "B-DeterministicQuadraticScaleTail-SolutionCriterion", "B-WeibullShapeGreaterThanOne-NotCompletelyMonotone", "D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Endpoint-obstruction-certificate-language"]
refs: ["librarian/audits/LA-20260623T0016-equation16-weibull-noncm-strict-app.json", "oracle/responses/OS-20260623T001050Z-oracle-response.md", "raw/student/20260623T0016-equation16-weibull-noncm.md", "scout/forage/inbox/FI-20260623T000951Z.json"]
---

# Theorem: Jonckheere-Shneer equation (16) has a deterministic-scale non-CM Weibull solution

## Statement

For every \(b\in(1/2,1)\) and \(c>0\), let \(\alpha=\log(1/2)/\log b>1\), let \(\widetilde B=b\) almost surely, and set \(F(x)=e^{-cx^\alpha}\) on \([0,\infty)\). Then \(F\) is a continuous non-increasing survival function satisfying Jonckheere--Shneer equation (16), \(F(x)=\int_0^\infty F(xu)^2\,\mathbb P(\widetilde B\in du)\), but \(F\) is not completely monotone.

## Dependencies

- [[wiki/nodes/O-JonckheereShneer-Equation16-NonCM-Solution-source-gate|Jonckheere-Shneer equation (16) non-CM solution question]]
- [[wiki/nodes/B-DeterministicQuadraticScaleTail-SolutionCriterion|Deterministic quadratic scale tail solution criterion]]
- [[wiki/nodes/B-WeibullShapeGreaterThanOne-NotCompletelyMonotone|Weibull tail with shape greater than one is not completely monotone]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]

## Proof and provenance references

- `librarian/audits/LA-20260623T0016-equation16-weibull-noncm-strict-app.json`
- `oracle/responses/OS-20260623T001050Z-oracle-response.md`
- `raw/student/20260623T0016-equation16-weibull-noncm.md`
- `scout/forage/inbox/FI-20260623T000951Z.json`

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

## Do not claim

- Do not claim a classification of all \(\widetilde B\).
- Do not claim uniqueness or nonexistence of other CM/non-CM solutions.
- Do not translate the witness back to the original \(\xi\)-equation without a separate source sign-convention audit.
- Do not public-stage without explicit user request.

## Tags

`app-0091-candidate`, `app-candidate`, `complete-monotonicity`, `distributional-equation`, `endpoint-obstruction`, `front-propagation`, `jonckheere-shneer`, `negative-answer`, `primitive-growth`, `proved`, `source-open-solved`, `survival-function`, `theorem`, `true`, `weibull-tail`
