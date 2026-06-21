---
id: "T-CBF-difference-quotient-Stieltjes"
type: "theorem"
title: "complete Bernstein finite origin difference quotient is Stieltjes"
status: "proved"
tags: ["bridge-patch", "complete-bernstein-function", "difference-quotient", "proved", "stieltjes", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private proof note", "wiki/definitions/stieltjes-cbf-bridge.md"]
---

# Theorem: complete Bernstein finite origin difference quotient is Stieltjes

## Statement

If \(G\) is a complete Bernstein function with finite \(G(0+)\), then \((G(x)-G(0+))/x\) is a Stieltjes function.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
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

`bridge-patch`, `complete-bernstein-function`, `difference-quotient`, `proved`, `stieltjes`, `theorem`
