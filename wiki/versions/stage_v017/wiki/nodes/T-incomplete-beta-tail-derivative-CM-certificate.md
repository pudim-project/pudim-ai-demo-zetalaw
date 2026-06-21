---
id: "T-incomplete-beta-tail-derivative-CM-certificate"
type: "theorem"
title: "incomplete beta tail derivative has positive discrete Laplace representation for lambda at most one"
status: "proved"
tags: ["bernstein-function", "bridge-patch", "complete-monotonicity", "incomplete-beta", "laplace-transform", "proved", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Laplace-kernel-and-tilted-moment-language", "T-Complete-monotonicity-closure-calculus-principle"]
refs: ["private attack plan", "private librarian audit", "private Oracle artifact", "private proof note", "private scout response", "wiki/notes/frontier-incomplete-beta-tail-bernstein.md"]
---

# Theorem: incomplete beta tail derivative has positive discrete Laplace representation for lambda at most one

## Statement

For \(b>0\) and \(0<\lambda\le1\), the derivative of \(I_{b,\lambda}(x)=B(b,\lambda)-B(b,\lambda;e^{-x})\) is completely monotone; for \(0<\lambda<1\), \(I_{b,\lambda}'(x)=\sum_{n=0}^\infty (1-\lambda)_n e^{-(b+n)x}/n!\).

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private Oracle artifact`
- `private proof note`
- `private scout response`
- `wiki/notes/frontier-incomplete-beta-tail-bernstein.md`

## Proof

The substitution \(u=e^{-t}\) gives
\[
B(b,\lambda)-B(b,\lambda;e^{-x})
=\int_{e^{-x}}^1u^{b-1}(1-u)^{\lambda-1}\,du
=\int_0^x e^{-bt}(1-e^{-t})^{\lambda-1}\,dt.
\]
Therefore
\[
I_{b,\lambda}'(x)=e^{-bx}(1-e^{-x})^{\lambda-1}.
\]
For \(\lambda=1\), this is \(e^{-bx}\), a completely monotone function.

For \(0<\lambda<1\), put \(c=1-\lambda\). Then \(c\in(0,1)\), and
\[
(1-e^{-x})^{-c}
=\sum_{n=0}^\infty \frac{(c)_n}{n!}e^{-nx}
\]
with positive coefficients and locally uniform convergence on \((0,\infty)\). Thus
\[
I_{b,\lambda}'(x)
=\sum_{n=0}^\infty \frac{(c)_n}{n!}e^{-(b+n)x},
\]
the Laplace transform of the positive discrete measure
\[
\sum_{n=0}^\infty \frac{(c)_n}{n!}\delta_{b+n}.
\]
So \(I_{b,\lambda}'\) is completely monotone. Since \(I_{b,\lambda}(x)\ge0\), \(I_{b,\lambda}\in C^\infty(0,\infty)\), and \(I_{b,\lambda}'\) is completely monotone, \(I_{b,\lambda}\) is a Bernstein function.

_Proof source: `private proof note`._

## Tags

`bernstein-function`, `bridge-patch`, `complete-monotonicity`, `incomplete-beta`, `laplace-transform`, `proved`, `theorem`
