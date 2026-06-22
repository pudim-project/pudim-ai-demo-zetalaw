---
id: "T-Not-TricomiPsiQuotient-CM-c-window"
type: "theorem"
title: "Tricomi Psi quotient complete-monotonicity window is false"
status: "proved"
tags: ["application-candidate", "complete-monotonicity", "counterexample", "endpoint-obstruction", "hypergeometric", "laplace-transform", "open-problem-solved", "proved", "source-solving", "strict-private-post-v016", "theorem", "tricomi", "true"]
parents: ["O-TricomiPsiQuotient-CM-c-window-source-gate", "D-TricomiPsi-StandardIntegralRepresentation", "L-TricomiPsi-IntegerPolynomial-CM-Counterfamily", "D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Laplace-kernel-and-tilted-moment-language"]
refs: ["oracle/responses/OS-20260620T1832Z-tricomi-psi-quotient-oracle-response.md", "raw/student/20260620T1840-tricomi-psi-quotient-counterexample.md"]
---

# Theorem: Tricomi Psi quotient complete-monotonicity window is false

## Statement

Ferreira--Simon Conjecture 2, read literally as the assertion that \(z\mapsto \Psi(a,c,z)^2/\Psi(2a,c,z)\) is completely monotone on \((0,\infty)\) if and only if \(c\in[0,1]\), is false. At \(a=1\) and \(c=3\), the quotient equals \((1+z^{-1})^2\), which is completely monotone although \(3\notin[0,1]\).

## Dependencies

- [[wiki/nodes/O-TricomiPsiQuotient-CM-c-window-source-gate|Tricomi Psi quotient complete monotonicity c-window source gate]]
- [[wiki/nodes/D-TricomiPsi-StandardIntegralRepresentation|Tricomi Psi standard Laplace integral representation]]
- [[wiki/nodes/L-TricomiPsi-IntegerPolynomial-CM-Counterfamily|Tricomi Psi integer polynomial complete-monotonicity counterfamily]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `oracle/responses/OS-20260620T1832Z-tricomi-psi-quotient-oracle-response.md`
- `raw/student/20260620T1840-tricomi-psi-quotient-counterexample.md`

## Proof

The same calculation gives a reusable family. For every integer \(m\ge1\), set \(a=m\) and \(c=2m+1\). Then
\[
\Psi(m,2m+1,z)
=\frac1{\Gamma(m)}\int_0^\infty e^{-zt}t^{m-1}(1+t)^m\,dt.
\]
Expanding \((1+t)^m\) gives a finite sum of positive multiples of \(z^{-m-k}\). Meanwhile
\[
\Psi(2m,2m+1,z)
=\frac1{\Gamma(2m)}\int_0^\infty e^{-zt}t^{2m-1}\,dt
=z^{-2m}.
\]
Hence the quotient is the square of a polynomial in \(z^{-1}\) with nonnegative coefficients, and is completely monotone. These are all outside the proposed window because \(c=2m+1>1\).

_Proof source: `raw/student/20260620T1840-tricomi-psi-quotient-counterexample.md`._

## Do not claim

- Do not claim the repaired c<1 problem is solved.
- Do not claim a full classification of all c>1.
- Do not claim source-proved special cases as new.
- Do not assign public APP numbering until staging/registry promotion.
- Do not public-stage without user request.

## Tags

`application-candidate`, `complete-monotonicity`, `counterexample`, `endpoint-obstruction`, `hypergeometric`, `laplace-transform`, `open-problem-solved`, `proved`, `source-solving`, `strict-private-post-v016`, `theorem`, `tricomi`, `true`
