---
id: "D-LaplaceSurvivalTransform"
type: "definition"
title: "Laplace-survival transform"
status: "proved"
tags: ["bridge-definition", "definition", "laplace-transform", "proved", "source-vocabulary", "survival-function", "true"]
parents: ["D-Laplace-kernel-and-tilted-moment-language", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["raw/student/20260614T0315-nagel-weiss-mecke-laplace-survival-poissonization.md"]
---

# Definition: Laplace-survival transform

## Statement

For a nonnegative random variable \(\zeta\) with Laplace transform \(L_\zeta(x)=\mathbb E e^{-x\zeta}\), a Laplace-survival transform is a construction of a random variable \(\xi\) whose distribution function satisfies \(F_\xi(x)=1-L_\zeta(x)\). If \(\mathbb P(\zeta=0)>0\), the natural exact construction is extended-valued with \(\xi=\infty\) on \(\{\zeta=0\}\).

## Dependencies

- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `raw/student/20260614T0315-nagel-weiss-mecke-laplace-survival-poissonization.md`

## Tags

`bridge-definition`, `definition`, `laplace-transform`, `proved`, `source-vocabulary`, `survival-function`, `true`
