---
id: "T-Jovanovic-Treml-arctan-logderivative-CM"
type: "theorem"
title: "reciprocal arctan logarithmic derivative has source imported complete monotonicity"
status: "proved"
tags: ["arctan", "bridge-patch", "complete-monotonicity", "laplace-kernel", "proved", "source-import", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260530T-elegance-028-arctan-bridge.json", "oracle/responses/ORACLE-FI-20260530T-elegance-028-oracle-forage-response.md", "raw/scout/FI-20260530T-elegance-028.md", "raw/student/20260530T-elegance-028-arctan-lcm-bridge.md", "scout/forage/context/FC-20260530T-elegance-028.json", "wiki/notes/bridge-reciprocal-arctan-lcm-stieltjes.md"]
---

# Theorem: reciprocal arctan logarithmic derivative has source imported complete monotonicity

## Statement

The function \(x\mapsto ((1+x^2)\arctan x)^{-1}\) is completely monotone on \((0,\infty)\), by the Jovanovic--Treml positive-kernel theorem.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260530T-elegance-028-arctan-bridge.json`
- `oracle/responses/ORACLE-FI-20260530T-elegance-028-oracle-forage-response.md`
- `raw/scout/FI-20260530T-elegance-028.md`
- `raw/student/20260530T-elegance-028-arctan-lcm-bridge.md`
- `scout/forage/context/FC-20260530T-elegance-028.json`
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

`arctan`, `bridge-patch`, `complete-monotonicity`, `laplace-kernel`, `proved`, `source-import`, `theorem`
