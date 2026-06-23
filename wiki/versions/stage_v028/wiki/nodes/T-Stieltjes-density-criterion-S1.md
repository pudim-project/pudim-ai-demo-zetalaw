---
id: "T-Stieltjes-density-criterion-S1"
type: "theorem"
title: "Laplace transform of completely monotone density is Stieltjes"
status: "proved"
tags: ["bridge-patch", "complete-monotonicity", "density-criterion", "laplace-transform", "proved", "stieltjes", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Laplace-kernel-and-tilted-moment-language"]
refs: ["librarian/audits/LA-20260530T-ramanujan-integral-stieltjes.json", "raw/student/20260530T-ramanujan-integral-stieltjes.md", "wiki/definitions/cm-stieltjes-density-criteria.md"]
---

# Theorem: Laplace transform of completely monotone density is Stieltjes

## Statement

If \(\phi\) is completely monotone on \((0,\infty)\) and \(F(x)=\int_0^\infty e^{-xt}\phi(t)\,dt\) is finite for \(x>0\), then \(F\) is a Stieltjes function.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `librarian/audits/LA-20260530T-ramanujan-integral-stieltjes.json`
- `raw/student/20260530T-ramanujan-integral-stieltjes.md`
- `wiki/definitions/cm-stieltjes-density-criteria.md`

## Proof

Completely monotone functions on \((0,\infty)\) are closed under pointwise products, nonnegative finite sums, and nonnegative parameter integrals whenever the integral is finite.

If \(\phi\) is completely monotone and
\[
F(x)=\int_0^\infty e^{-xt}\phi(t)\,dt
\]
is finite for every \(x>0\), then \(F\) is a Stieltjes function. Indeed, Bernstein's theorem gives
\[
\phi(t)=\int_0^\infty e^{-ts}\,d\mu(s),
\]
and Tonelli gives
\[
F(x)=\int_0^\infty \frac{d\mu(s)}{x+s}.
\]

If
\[
f(x)=a+bx+\int_0^\infty (1-e^{-xt})m(t)\,dt
\]
is a Bernstein representation and \(m\) is completely monotone, then \(f\) is a complete Bernstein function, subject to the usual Levy integrability condition.

_Proof source: `wiki/definitions/cm-stieltjes-density-criteria.md`._

## Tags

`bridge-patch`, `complete-monotonicity`, `density-criterion`, `laplace-transform`, `proved`, `stieltjes`, `theorem`
