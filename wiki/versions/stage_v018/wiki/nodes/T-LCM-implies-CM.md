---
id: "T-LCM-implies-CM"
type: "theorem"
title: "logarithmic complete monotonicity implies complete monotonicity"
status: "proved"
tags: ["complete-monotonicity", "logarithmically-completely-monotone", "proved", "standard-closure", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260530T-elegance-028-arctan-bridge.json", "raw/student/20260530T-elegance-028-arctan-lcm-bridge.md", "wiki/definitions/logarithmically-completely-monotone.md"]
---

# Theorem: logarithmic complete monotonicity implies complete monotonicity

## Statement

Every logarithmically completely monotone function on \((0,\infty)\) is completely monotone.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260530T-elegance-028-arctan-bridge.json`
- `raw/student/20260530T-elegance-028-arctan-lcm-bridge.md`
- `wiki/definitions/logarithmically-completely-monotone.md`

## Proof

If \(1/\arctan x\) were a Stieltjes function, then its reciprocal \(\arctan x\) would be a Bernstein function. A Bernstein function has completely monotone derivative.

But
\[
(\arctan x)'=\frac1{1+x^2},
\]
and
\[
\left(\frac1{1+x^2}\right)''
=\frac{2(3x^2-1)}{(1+x^2)^3},
\]
which is negative for \(0<x<1/\sqrt3\). Hence \((\arctan x)'\) is not completely monotone, \(\arctan x\) is not Bernstein, and \(1/\arctan x\) is not Stieltjes.

_Proof source: `raw/student/20260530T-elegance-028-arctan-lcm-bridge.md`._

## Tags

`complete-monotonicity`, `logarithmically-completely-monotone`, `proved`, `standard-closure`, `theorem`
