---
id: "T-reciprocal-arctan-not-Stieltjes"
type: "theorem"
title: "reciprocal arctan is completely monotone but not Stieltjes"
status: "proved"
tags: ["arctan", "bridge-patch", "complete-monotonicity", "proved", "separator", "stieltjes", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-arctan-not-Bernstein", "T-Complete-monotonicity-closure-calculus-principle"]
refs: ["librarian/audits/LA-20260530T-elegance-028-arctan-bridge.json", "raw/student/20260530T-elegance-028-arctan-lcm-bridge.md", "wiki/notes/bridge-reciprocal-arctan-lcm-stieltjes.md"]
---

# Theorem: reciprocal arctan is completely monotone but not Stieltjes

## Statement

The function \(x\mapsto1/\arctan x\) is not a Stieltjes function.

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-arctan-not-Bernstein|arctan is not Bernstein since derivative is not completely monotone]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `librarian/audits/LA-20260530T-elegance-028-arctan-bridge.json`
- `raw/student/20260530T-elegance-028-arctan-lcm-bridge.md`
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

_Proof source: `raw/student/20260530T-elegance-028-arctan-lcm-bridge.md`._

## Tags

`arctan`, `bridge-patch`, `complete-monotonicity`, `proved`, `separator`, `stieltjes`, `theorem`
