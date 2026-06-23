---
id: "T-positive-Laplace-kernel-complete-monotonicity-principle"
type: "theorem"
title: "T-positive-Laplace-kernel-complete-monotonicity-principle"
status: "proved"
tags: ["application-bridge", "bernstein-widder", "complete-monotonicity", "laplace-transform", "primitive", "principle", "proved", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Laplace-kernel-and-tilted-moment-language"]
refs: ["raw/student/20260605T-bridge-positive-laplace-kernel-polygamma-p0.md"]
---

# Theorem: T-positive-Laplace-kernel-complete-monotonicity-principle

## Statement

If \(F(x)=\int_0^\infty e^{-xt}\,d\mu(t)\) on \((0,\infty)\) for a positive measure \(\mu\), then \(F\) is completely monotone. If the representing measure is nonzero in every relevant derivative order, the complete monotonicity is strict.

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `raw/student/20260605T-bridge-positive-laplace-kernel-polygamma-p0.md`

## Proof

Let \(F:(0,\infty)\to\mathbb R\) have a positive Laplace representation
\[
F(x)=\int_{[0,\infty)}e^{-xt}\,d\mu(t),
\]
where \(\mu\) is a positive measure for which the differentiated integrals are finite on compact subintervals. Then \(F\) is completely monotone. If the relevant moments of \(\mu\) are nonzero, the corresponding inequalities are strict.

Differentiating under the integral gives, for every \(r\ge0\),
\[
(-1)^rF^{(r)}(x)=\int_{[0,\infty)}t^r e^{-xt}\,d\mu(t)\ge0.
\]
This is the Bernstein--Widder sign pattern. If \(t^r\mu\) is nonzero, the integral is positive for every \(x>0\), giving strictness in that order.

_Proof source: `raw/student/20260605T-bridge-positive-laplace-kernel-polygamma-p0.md`._

## Tags

`application-bridge`, `bernstein-widder`, `complete-monotonicity`, `laplace-transform`, `primitive`, `principle`, `proved`, `theorem`
