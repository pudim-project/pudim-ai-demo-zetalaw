---
id: "T-CM-closure-product-positive-mixture"
type: "theorem"
title: "complete monotone functions closed under product positive sums and positive mixtures"
status: "proved"
tags: ["bridge-patch", "closure", "complete-monotonicity", "proved", "standard-closure", "theorem"]
parents: ["T-positive-Laplace-kernel-complete-monotonicity-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private proof note", "wiki/definitions/cm-stieltjes-density-criteria.md"]
---

# Theorem: complete monotone functions closed under product positive sums and positive mixtures

## Statement

Completely monotone functions on \((0,\infty)\) are closed under pointwise products, nonnegative finite sums, and nonnegative parameter integrals whenever the integral is finite.

## Dependencies

- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
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

`bridge-patch`, `closure`, `complete-monotonicity`, `proved`, `standard-closure`, `theorem`
