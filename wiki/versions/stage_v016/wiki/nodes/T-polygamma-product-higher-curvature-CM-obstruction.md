---
id: "T-polygamma-product-higher-curvature-CM-obstruction"
type: "theorem"
title: "T-polygamma-product-higher-curvature-CM-obstruction"
status: "proved"
tags: ["application-bridge", "complete-monotonicity", "pointwise-obstruction", "polygamma", "proved", "source-open-solved", "theorem"]
parents: ["T-Pointwise-obstruction-certificate-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["raw/student/20260605T-bridge-polygamma-product-higher-curvature-obstruction.md", "theory/latest/THEORY.tex#thm:pn-complete-monotonicity-counterexample"]
---

# Theorem: T-polygamma-product-higher-curvature-CM-obstruction

## Statement

For the higher-order Qi--Lim--Nantomah polygamma products \(P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x)\), the asserted universal complete monotonicity of \(P_n''\) fails. More precisely, \(P_n'''(2)>0\) for every \(n\ge29\), so \(P_n''\) is not completely monotone for those \(n\).

## Dependencies

- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `raw/student/20260605T-bridge-polygamma-product-higher-curvature-obstruction.md`
- `theory/latest/THEORY.tex#thm:pn-complete-monotonicity-counterexample`

## Proof

The staged APP-0008 proof gives a rationally certified derivative witness \(P_n'''(2)>0\) for every \(n\ge29\). If \(P_n''\) were completely monotone, then its first derivative would have to be nonpositive everywhere. The positive value at \(x=2\) is therefore a pointwise obstruction certificate. By the pointwise obstruction principle, this witness refutes the source's stronger universal complete-monotonicity assertion.

_Proof source: `raw/student/20260605T-bridge-polygamma-product-higher-curvature-obstruction.md`._

## Tags

`application-bridge`, `complete-monotonicity`, `pointwise-obstruction`, `polygamma`, `proved`, `source-open-solved`, `theorem`
