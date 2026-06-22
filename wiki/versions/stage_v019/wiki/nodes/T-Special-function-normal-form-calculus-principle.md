---
id: "T-Special-function-normal-form-calculus-principle"
type: "theorem"
title: "Special-function normal-form calculus principle"
status: "proved"
tags: ["derivative-calculus", "normal-form", "primitive", "principle", "proved", "special-functions", "structural-tool", "theorem"]
parents: []
refs: ["raw/student/20260605T-primitive-special-function-normal-form-calculus-principle.md", "raw/student/20260614T-v016-primitive-special-function-normal-form-public.md"]
---

# Theorem: Special-function normal-form calculus principle

## Statement

A special-function inequality or monotonicity claim may be transported to an explicit derivative, recurrence, integral, product, or partial-fraction normal form, after which sign, convexity, or monotonicity is decided in that normal form.

## Proof and provenance references

- `raw/student/20260605T-primitive-special-function-normal-form-calculus-principle.md`
- `raw/student/20260614T-v016-primitive-special-function-normal-form-public.md`

## Proof

Let the target expression be represented on its domain by an identity
\[
F(x)=N(x),
\]
where \(N\) is written using recurrence relations, logarithmic derivatives, an integral formula, a product, or a partial fraction expansion. If the normal form proves the required sign pattern, for example
\[
(-1)^kN^{(k)}(x)\ge0\qquad (x\in I),
\]
then the identity gives \((-1)^kF^{(k)}(x)\ge0\) on the same domain. The same substitution transfers monotonicity and convexity inequalities, since differentiating equal normal forms preserves equality of the derivatives used in the sign test.

_Proof source: `raw/student/20260614T-v016-primitive-special-function-normal-form-public.md`._

## Tags

`derivative-calculus`, `normal-form`, `primitive`, `principle`, `proved`, `special-functions`, `structural-tool`, `theorem`
