---
id: "T-Stieltjes-reciprocal-CBF"
type: "theorem"
title: "reciprocal of nonzero Stieltjes function is complete Bernstein"
status: "proved"
tags: ["bridge-patch", "complete-bernstein-function", "proved", "standard-closure", "stieltjes", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260530T-karp-sitnik-stieltjes-ratio.json", "raw/student/20260530T-karp-sitnik-stieltjes-ratio.md", "wiki/definitions/stieltjes-cbf-bridge.md"]
---

# Theorem: reciprocal of nonzero Stieltjes function is complete Bernstein

## Statement

If \(F\) is a nonzero Stieltjes function on \((0,\infty)\), then \(1/F\) is a complete Bernstein function.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260530T-karp-sitnik-stieltjes-ratio.json`
- `raw/student/20260530T-karp-sitnik-stieltjes-ratio.md`
- `wiki/definitions/stieltjes-cbf-bridge.md`

## Proof

A Stieltjes function has the form
\[
f(x)=c+\int_0^\infty \frac{d\mu(t)}{x+t},
\qquad c\ge0,\quad \mu\ge0,
\]
with the usual local integrability condition. Compact-support variants such as
\[
f(x)=\int_0^1\frac{d\nu(s)}{1+sx}
\]
are equivalent after a change of variables and scaling.

if \(F\) is a nonzero Stieltjes function, then \(1/F\) is a complete Bernstein function;
if \(G\) is complete Bernstein and \(G(0+)<\infty\), then
\[
\frac{G(x)-G(0+)}{x}
\]
is Stieltjes.

Together these convert normalized Stieltjes transforms \(F(0)=1\) into Stieltjes defect quotients
\[
\frac{1/F(x)-1}{x}.
\]

_Proof source: `wiki/definitions/stieltjes-cbf-bridge.md`._

## Tags

`bridge-patch`, `complete-bernstein-function`, `proved`, `standard-closure`, `stieltjes`, `theorem`
