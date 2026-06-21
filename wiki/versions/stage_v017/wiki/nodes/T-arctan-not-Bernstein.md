---
id: "T-arctan-not-Bernstein"
type: "theorem"
title: "arctan is not Bernstein since derivative is not completely monotone"
status: "proved"
tags: ["arctan", "bernstein-function", "bridge-patch", "obstruction", "proved", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-Complete-monotonicity-closure-calculus-principle"]
refs: ["private librarian audit", "private proof note", "wiki/notes/bridge-reciprocal-arctan-lcm-stieltjes.md"]
---

# Theorem: arctan is not Bernstein since derivative is not completely monotone

## Statement

The function \(x\mapsto\arctan x\) is not a Bernstein function on \((0,\infty)\), because its derivative \((1+x^2)^{-1}\) is not completely monotone.

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

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

`arctan`, `bernstein-function`, `bridge-patch`, `obstruction`, `proved`, `theorem`
