---
id: "T-Ramanujan-integral-Stieltjes-and-antiderivative-CBF"
type: "theorem"
title: "T-Ramanujan-integral-Stieltjes-and-antiderivative-CBF"
status: "proved"
tags: ["application-bridge", "complete-bernstein", "proved", "ramanujan-integral", "source-open-solved", "stieltjes", "theorem"]
parents: ["T-Ramanujan-antiderivative-complete-Bernstein", "T-Ramanujan-integral-Stieltjes", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["raw/student/20260605T-bridge-ramanujan-stieltjes-cbf-assembly.md"]
---

# Theorem: T-Ramanujan-integral-Stieltjes-and-antiderivative-CBF

## Statement

The Mishra--Swaminathan Ramanujan integral application is resolved in the combined form: \(I_R(x)=\int_0^\infty e^{-xt}\,dt/[t(\pi^2+\log^2 t)]\) is a Stieltjes function and its primitive \(\widetilde I_R(x)=a+\int_0^\infty(1-e^{-xt})\,dt/[t(\pi^2+\log^2 t)]\) is a complete Bernstein function.

## Dependencies

- [[wiki/nodes/T-Ramanujan-antiderivative-complete-Bernstein|Ramanujan integral antiderivative is complete Bernstein]]
- [[wiki/nodes/T-Ramanujan-integral-Stieltjes|Ramanujan integral I_R is Stieltjes]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `raw/student/20260605T-bridge-ramanujan-stieltjes-cbf-assembly.md`

## Proof

The node the Ramanujan integral Stieltjes proves that
\(I_R(x)=\int_0^\infty e^{-xt}\,dt/[t(\pi^2+\log^2 t)]\) is a Stieltjes function. The node the Ramanujan antiderivative complete Bernstein proves that the primitive
\(\widetilde I_R(x)=a+\int_0^\infty(1-e^{-xt})\,dt/[t(\pi^2+\log^2 t)]\)
is a complete Bernstein function. These are exactly the two clauses of APP-0014, so the conjunction gives the source-facing application result.

_Proof source: `raw/student/20260605T-bridge-ramanujan-stieltjes-cbf-assembly.md`._

## Tags

`application-bridge`, `complete-bernstein`, `proved`, `ramanujan-integral`, `source-open-solved`, `stieltjes`, `theorem`
