---
id: "T-not-Apery-shifted-positive-coefficientwise-measure-expansion"
type: "theorem"
title: "No positive coefficientwise measure expansion for shifted Apéry polynomials"
status: "proved"
tags: ["apery-polynomials", "coefficientwise", "method-obstruction", "positive-measure", "primitive-route-kill", "proved", "stieltjes-moment", "theorem", "true"]
parents: ["O-Apery-polynomial-Stieltjes-HankelTP-source-gate", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private Oracle response", "private proof note"]
---

# Theorem: No positive coefficientwise measure expansion for shifted Apéry polynomials

## Statement

There are no positive measures \(\mu_r\) on \([0,\infty)\) satisfying \([y^r]A_n(1+y)=\int_0^\infty t^n\,d\mu_r(t)\) for every \(n,r\ge0\), where \(A_n(x)=\sum_{k=0}^n \binom nk^2\binom{n+k}{k}^2x^k\).

## Dependencies

- [[wiki/nodes/O-Apery-polynomial-Stieltjes-HankelTP-source-gate|Apery polynomial Stieltjes moment and coefficientwise Hankel-total-positivity source gate]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`

## Proof

Let
\[
A_n(x)=\sum_{k=0}^n \binom nk^2\binom{n+k}{k}^2x^k.
\]
There are no positive measures \(\mu_r\) on \([0,\infty)\) satisfying
\[
[y^r]A_n(1+y)=\int_0^\infty t^n\,d\mu_r(t)
\]
for every \(n,r\ge0\).

Indeed, for \(r=1\),
\[
[y]A_0(1+y)=0,\qquad [y]A_1(1+y)=4.
\]
If \(\mu_1\) were positive, the zeroth moment condition would give
\[
\mu_1([0,\infty))=0,
\]
so \(\mu_1=0\), contradicting the first moment \(4\). Thus the direct coefficientwise positive-measure route to coefficientwise Hankel total positivity is impossible.

This does not refute Sokal's shifted coefficientwise Hankel-TP conjecture and does not refute the weaker fixed-\(x\ge1\) Stieltjes moment conjecture.

The source's shift \(x=1+y\) is essential. In the original \(x\)-basis, the adjacent \(2\times2\) Hankel minor
\[
A_3(x)A_5(x)-A_4(x)^2
\]
has a negative coefficient. Exact expansion gives coefficient list, from low to high degree,
\[
0,\ 244,\ -1600,\ 955200,\ 4305500,\ 35657104,\ 28254576,\ 23833600,\ 1391600.
\]
Equivalently,
\[
A_3(x)A_5(x)-A_4(x)^2
=
4x\bigl(
61-400x+238800x^2+1076375x^3+8914276x^4
+7063644x^5+5958400x^6+347900x^7
\bigr).
\]
The coefficient of \(x^2\) in the full minor is \(-1600\), so \((A_n(x))\) is not coefficientwise Hankel-TP in the unshifted variable \(x\).

This does not affect Sokal's shifted conjecture for \(A_n(1+y)\).

The replay used integer arithmetic with
\[
A_3(x)=1+144x+900x^2+400x^3,
\]
\[
A_4(x)=1+400x+8100x^2+19600x^3+4900x^4,
\]
and
\[
A_5(x)=1+900x+44100x^2+313600x^3+396900x^4+63504x^5.
\]

No numerical approximation is used in either obstruction.

_Proof source: `private proof note`._

## Do not claim

- Do not claim this refutes Sokal's shifted coefficientwise Hankel-TP conjecture.
- Do not claim this refutes the fixed-x Stieltjes moment conjecture.
- It only kills the direct positive coefficientwise measure expansion route.

## Tags

`apery-polynomials`, `coefficientwise`, `method-obstruction`, `positive-measure`, `primitive-route-kill`, `proved`, `stieltjes-moment`, `theorem`, `true`
