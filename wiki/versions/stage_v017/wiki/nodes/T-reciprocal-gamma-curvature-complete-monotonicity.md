---
id: "T-reciprocal-gamma-curvature-complete-monotonicity"
type: "theorem"
title: "T-reciprocal-gamma-curvature-complete-monotonicity"
status: "proved"
tags: ["application-bridge", "complete-monotonicity", "gamma", "laplace-kernel", "polygamma", "proved", "source-open-solved", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-positive-Laplace-kernel-complete-monotonicity-principle"]
refs: ["private proof note", "theory/latest/THEORY.tex#thm:reciprocal-gamma-complete-monotonicity"]
---

# Theorem: T-reciprocal-gamma-curvature-complete-monotonicity

## Statement

For \(H(x)=\log\Gamma(x)+\log\Gamma(1/x)\), the second derivative \(H''\) is completely monotone on \((0,\infty)\), solving the Qi--Lim--Nantomah reciprocal-Gamma curvature problem.

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]

## Proof and provenance references

- `private proof note`
- `theory/latest/THEORY.tex#thm:reciprocal-gamma-complete-monotonicity`

## Proof

The staged APP-0004 proof derives a positive reciprocal-Weierstrass/Laplace-kernel representation for \(H''\). By the positive Laplace-kernel complete-monotonicity principle, every derivative has the alternating sign pattern required for complete monotonicity. Thus the source problem is solved affirmatively.

_Proof source: `private proof note`._

## Tags

`application-bridge`, `complete-monotonicity`, `gamma`, `laplace-kernel`, `polygamma`, `proved`, `source-open-solved`, `theorem`
