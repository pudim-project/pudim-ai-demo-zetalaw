---
id: "T-Complete-monotonicity-closure-calculus-principle"
type: "theorem"
title: "Complete-monotonicity closure calculus principle"
status: "proved"
tags: ["bernstein", "closure-calculus", "complete-monotonicity", "primitive", "principle", "proved", "structural-tool", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["raw/student/20260605T-primitive-complete-monotonicity-closure-calculus-principle.md", "raw/student/20260614T-v016-primitive-complete-monotonicity-closure-public.md"]
---

# Theorem: Complete-monotonicity closure calculus principle

## Statement

Complete monotonicity, logarithmic complete monotonicity, Stieltjes, Bernstein, and complete-Bernstein conclusions are transported by their standard closure operations, reciprocal transforms, derivative criteria, positive mixtures, and composition rules.

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `raw/student/20260605T-primitive-complete-monotonicity-closure-calculus-principle.md`
- `raw/student/20260614T-v016-primitive-complete-monotonicity-closure-public.md`

## Proof

A completely monotone function has a positive Laplace representation
\[
f(x)=\int_{[0,\infty)} e^{-xt}\,d\mu(t),
\]
so
\[
(-1)^nf^{(n)}(x)=\int_{[0,\infty)}t^ne^{-xt}\,d\mu(t)\ge0.
\]
Positive sums and mixtures add the representing measures. The Stieltjes and Bernstein derivative criteria reduce to the same positivity of representing measures or of \(f'\). Thus once an expression is reduced by these standard closure operations to positive measures, reciprocal transforms, derivative criteria, or Bernstein composition, the required complete-monotonicity or Bernstein conclusion follows.

_Proof source: `raw/student/20260614T-v016-primitive-complete-monotonicity-closure-public.md`._

## Tags

`bernstein`, `closure-calculus`, `complete-monotonicity`, `primitive`, `principle`, `proved`, `structural-tool`, `theorem`
