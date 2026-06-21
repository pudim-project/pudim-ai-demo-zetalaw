---
id: "L-TricomiPsi-IntegerPolynomial-CM-Counterfamily"
type: "lemma"
title: "Tricomi Psi integer polynomial complete-monotonicity counterfamily"
status: "proved"
tags: ["bridge", "complete-monotonicity", "endpoint-obstruction", "laplace-transform", "lemma", "proved", "strict-private-post-v016", "tricomi", "true"]
parents: ["D-TricomiPsi-StandardIntegralRepresentation", "D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Laplace-kernel-and-tilted-moment-language"]
refs: ["private Oracle response", "private proof note"]
---

# Lemma: Tricomi Psi integer polynomial complete-monotonicity counterfamily

## Statement

For every integer \(m\ge1\), the quotient \(z\mapsto \Psi(m,2m+1,z)^2/\Psi(2m,2m+1,z)\) is a polynomial in \(z^{-1}\) with nonnegative coefficients, hence is completely monotone on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/D-TricomiPsi-StandardIntegralRepresentation|Tricomi Psi standard Laplace integral representation]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `private Oracle response`
- `private proof note`

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

_Proof source: `private proof note`._

## Do not claim

- Do not claim this proves the repaired c<1 version of the source problem.
- Do not infer complete monotonicity for arbitrary c>1.
- Do not public-stage without user request.

## Tags

`bridge`, `complete-monotonicity`, `endpoint-obstruction`, `laplace-transform`, `lemma`, `proved`, `strict-private-post-v016`, `tricomi`, `true`
