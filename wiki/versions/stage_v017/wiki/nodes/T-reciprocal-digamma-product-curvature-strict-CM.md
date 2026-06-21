---
id: "T-reciprocal-digamma-product-curvature-strict-CM"
type: "theorem"
title: "T-reciprocal-digamma-product-curvature-strict-CM"
status: "proved"
tags: ["application-bridge", "complete-monotonicity", "digamma", "laplace-kernel", "polygamma", "proved", "source-open-solved", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-positive-Laplace-kernel-complete-monotonicity-principle"]
refs: ["private proof note", "theory/latest/THEORY.tex#thm:reciprocal-digamma-product-complete-monotonicity"]
---

# Theorem: T-reciprocal-digamma-product-curvature-strict-CM

## Statement

For \(P_0(x)=\psi(x)\psi(1/x)\), the function \(-P_0''\) is strictly completely monotone on \((0,\infty)\). In particular, \(P_0\) is strictly concave on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]

## Proof and provenance references

- `private proof note`
- `theory/latest/THEORY.tex#thm:reciprocal-digamma-product-complete-monotonicity`

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

_Proof source: `private proof note`._

## Tags

`application-bridge`, `complete-monotonicity`, `digamma`, `laplace-kernel`, `polygamma`, `proved`, `source-open-solved`, `theorem`
