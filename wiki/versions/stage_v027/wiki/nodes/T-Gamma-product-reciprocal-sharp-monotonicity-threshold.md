---
id: "T-Gamma-product-reciprocal-sharp-monotonicity-threshold"
type: "theorem"
title: "T-Gamma-product-reciprocal-sharp-monotonicity-threshold"
status: "proved"
tags: ["application-bridge", "digamma", "endpoint-threshold", "gamma-product", "proved", "source-open-solved", "theorem"]
parents: ["T-endpoint-log-derivative-monotonicity-principle"]
refs: ["raw/student/20260605T-bridge-gamma-product-threshold.md", "theory/latest/THEORY.tex#thm:gamma-product-sharp-threshold"]
---

# Theorem: T-Gamma-product-reciprocal-sharp-monotonicity-threshold

## Statement

Let \(\rho_*>0\) be the unique solution of \(\psi(1+\rho_*)=\gamma\). For \(\rho>-1\), \(\varphi_\rho(s)=1/(\Gamma(s+\rho)\Gamma(s))\) is strictly decreasing on \([1,\infty)\) if and only if \(\rho\ge\rho_*\). Equivalently, \(\Gamma(s+\rho)\Gamma(s)\) is strictly increasing on \([1,\infty)\) exactly in that parameter range.

## Dependencies

- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]

## Proof and provenance references

- `raw/student/20260605T-bridge-gamma-product-threshold.md`
- `theory/latest/THEORY.tex#thm:gamma-product-sharp-threshold`

## Proof

If \(J\) is nonincreasing and \(g\) is strictly increasing, then \(J-g\) is strictly decreasing on the half-line, so the sign of \(J-g\) everywhere is forced by its endpoint value. In the Gamma-product case, the logarithmic derivative of \(W_\rho\) is \(\psi(s+\rho)+\psi(s)\), which is strictly increasing because \(\psi'>0\). Its endpoint value at \(s=1\) is \(\psi(1+\rho)-\gamma\). Therefore \(W_\rho\) is strictly increasing, equivalently \(1/W_\rho\) is strictly decreasing, exactly when \(\psi(1+\rho)\ge\gamma\). The same endpoint comparison gives the stated extension with a differentiable factor \(u\) whose logarithmic derivative is nonincreasing.

_Proof source: `raw/student/20260605T-bridge-gamma-product-threshold.md`._

## Tags

`application-bridge`, `digamma`, `endpoint-threshold`, `gamma-product`, `proved`, `source-open-solved`, `theorem`
