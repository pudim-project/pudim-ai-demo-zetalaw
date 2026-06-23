---
id: "T-CBF-Levy-density-CM-criterion"
type: "theorem"
title: "Bernstein function with completely monotone Levy density is complete Bernstein"
status: "proved"
tags: ["bridge-patch", "complete-bernstein-function", "complete-monotonicity", "levy-density", "proved", "standard-closure", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260530T-ramanujan-integral-stieltjes.json", "raw/student/20260530T-ramanujan-integral-stieltjes.md", "wiki/definitions/cm-stieltjes-density-criteria.md"]
---

# Theorem: Bernstein function with completely monotone Levy density is complete Bernstein

## Statement

A Bernstein function with representation \(f(x)=a+bx+\int_0^\infty(1-e^{-xt})m(t)\,dt\) is complete Bernstein when the Levy density \(m\) is completely monotone and satisfies the usual Levy integrability condition.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

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

`bridge-patch`, `complete-bernstein-function`, `complete-monotonicity`, `levy-density`, `proved`, `standard-closure`, `theorem`
