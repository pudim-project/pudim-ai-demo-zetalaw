---
id: "T-Stieltjes-reciprocal-is-BF"
type: "theorem"
title: "reciprocal of nonzero Stieltjes function is Bernstein"
status: "proved"
tags: ["bernstein-function", "bridge-patch", "proved", "standard-closure", "stieltjes", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private proof note", "wiki/notes/bridge-reciprocal-arctan-lcm-stieltjes.md"]
---

# Theorem: reciprocal of nonzero Stieltjes function is Bernstein

## Statement

If \(f\) is a nonzero Stieltjes function, then \(1/f\) is a Bernstein function.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `wiki/notes/bridge-reciprocal-arctan-lcm-stieltjes.md`

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

_Proof source: `private proof note`._

## Tags

`bernstein-function`, `bridge-patch`, `proved`, `standard-closure`, `stieltjes`, `theorem`
