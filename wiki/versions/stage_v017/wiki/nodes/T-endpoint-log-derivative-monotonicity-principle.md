---
id: "T-endpoint-log-derivative-monotonicity-principle"
type: "theorem"
title: "T-endpoint-log-derivative-monotonicity-principle"
status: "proved"
tags: ["application-bridge", "endpoint-principle", "logarithmic-derivative", "monotonicity", "primitive", "proved", "structural-tool", "theorem"]
parents: []
refs: ["private proof note", "theory/latest/THEORY.tex#thm:gamma-product-sharp-threshold"]
---

# Theorem: T-endpoint-log-derivative-monotonicity-principle

## Statement

Let \(f>0\) be differentiable on \([1,\infty)\). If \((\log f)'\) is monotone on \([1,\infty)\), then the global monotonicity of \(f\) on \([1,\infty)\) is decided by the endpoint sign of \((\log f)'(1)\), with strictness away from the endpoint when the logarithmic derivative is strictly monotone.

## Proof and provenance references

- `private proof note`
- `theory/latest/THEORY.tex#thm:gamma-product-sharp-threshold`

## Proof

If \(J\) is nonincreasing and \(g\) is strictly increasing, then \(J-g\) is strictly decreasing on the half-line, so the sign of \(J-g\) everywhere is forced by its endpoint value. In the Gamma-product case, the logarithmic derivative of \(W_\rho\) is \(\psi(s+\rho)+\psi(s)\), which is strictly increasing because \(\psi'>0\). Its endpoint value at \(s=1\) is \(\psi(1+\rho)-\gamma\). Therefore \(W_\rho\) is strictly increasing, equivalently \(1/W_\rho\) is strictly decreasing, exactly when \(\psi(1+\rho)\ge\gamma\). The same endpoint comparison gives the stated extension with a differentiable factor \(u\) whose logarithmic derivative is nonincreasing.

_Proof source: `private proof note`._

## Tags

`application-bridge`, `endpoint-principle`, `logarithmic-derivative`, `monotonicity`, `primitive`, `proved`, `structural-tool`, `theorem`
