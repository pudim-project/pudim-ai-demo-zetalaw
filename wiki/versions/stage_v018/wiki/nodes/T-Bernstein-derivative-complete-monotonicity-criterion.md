---
id: "T-Bernstein-derivative-complete-monotonicity-criterion"
type: "theorem"
title: "T-Bernstein-derivative-complete-monotonicity-criterion"
status: "proved"
tags: ["application-bridge", "bernstein-criterion", "bernstein-function", "complete-monotonicity", "criterion", "primitive", "proved", "structural-tool", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["raw/student/20260605T-bridge-bernstein-derivative-cm-criterion.md"]
---

# Theorem: T-Bernstein-derivative-complete-monotonicity-criterion

## Statement

Let f be nonnegative and continuously differentiable on an interval. If f' is completely monotone, then f is a Bernstein function on that interval. Conversely, for a differentiable Bernstein function, f' is completely monotone.

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `raw/student/20260605T-bridge-bernstein-derivative-cm-criterion.md`

## Proof

Let \(f\) be nonnegative and continuously differentiable on an interval \((a,\infty)\). A Bernstein function is exactly a nonnegative function whose derivative is completely monotone. Hence, if \(f'\) is completely monotone, the defining criterion is satisfied and \(f\) is Bernstein. Conversely, if \(f\) is a differentiable Bernstein function, the same defining criterion gives complete monotonicity of \(f'\). This proves the criterion.

_Proof source: `raw/student/20260605T-bridge-bernstein-derivative-cm-criterion.md`._

## Tags

`application-bridge`, `bernstein-criterion`, `bernstein-function`, `complete-monotonicity`, `criterion`, `primitive`, `proved`, `structural-tool`, `theorem`
