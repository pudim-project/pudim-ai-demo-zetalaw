---
id: "T-BuricElezovic-Cor6-BestB-VariationalThreshold"
type: "theorem"
title: "Buric-Elezovic half-shift psi-log best-b threshold"
status: "proved"
tags: ["bridge-result", "complete-monotonicity", "digamma", "laplace-density", "literature-closure-risk", "not-app", "proved", "source-restatement-required", "theorem"]
parents: ["L-Affine-Laplace-Density-Threshold", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private Oracle response", "private proof note", "wiki/notes/buric-elezovic-best-b-threshold.md"]
---

# Theorem: Buric-Elezovic half-shift psi-log best-b threshold

## Statement

Let \(A(t)=1/t-1/(2\sinh(t/2))\) and \(b_*=\sup_{t>0}-A'(t)/A(t)\). For \(b\in\mathbb R\), \(f_b(x)=(x+b)(\psi(x+1/2)-\log x)\) is completely monotone on \((0,\infty)\) if and only if \(b\ge b_*\).

## Dependencies

- [[wiki/nodes/L-Affine-Laplace-Density-Threshold|Affine Laplace density threshold]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `wiki/notes/buric-elezovic-best-b-threshold.md`

## Proof

The standard integral representation for \(\psi\), combined with Frullani's formula for \(\log x\), gives
\[
\psi\left(x+\frac12\right)-\log x
=\int_0^\infty e^{-xt}
\left(\frac1t-\frac{1}{2\sinh(t/2)}\right)\,dt
=\int_0^\infty e^{-xt}A(t)\,dt.
\]
The density is positive because \(2\sinh(t/2)>t\) for \(t>0\). Moreover
\[
A(t)=\frac{t}{24}+O(t^3)\quad(t\downarrow0),
\qquad
A(t)=\frac1t+O(e^{-t/2})\quad(t\to\infty).
\]
Thus the integration-by-parts boundary term \(e^{-xt}A(t)\) vanishes at both endpoints for each \(x>0\), and
\[
x\int_0^\infty e^{-xt}A(t)\,dt
=\int_0^\infty e^{-xt}A'(t)\,dt.
\]
Therefore
\[
f_b(x)=\int_0^\infty e^{-xt}\bigl(A'(t)+bA(t)\bigr)\,dt.
\]

If \(b\ge b_*\), then \(A'(t)+bA(t)\ge0\) for all \(t>0\). Hence, for every integer \(n\ge0\),
\[
(-1)^n f_b^{(n)}(x)
=\int_0^\infty t^n e^{-xt}\bigl(A'(t)+bA(t)\bigr)\,dt\ge0,
\]
so \(f_b\) is completely monotone.

Conversely, if \(b<b_*\), then by continuity there is a nonempty open interval \(I\subset(0,\infty)\) such that
\[
A'(t)+bA(t)<0\qquad(t\in I).
\]
The signed density \((A'(t)+bA(t))\,dt\) is locally finite and has a finite Laplace transform for every \(x>0\). If \(f_b\) were completely monotone, Bernstein's theorem would represent it as the Laplace transform of a positive Radon measure. Laplace-transform uniqueness for locally finite signed measures would force that positive measure to equal the signed density measure above, impossible because the signed density is negative on \(I\). Therefore \(f_b\) is not completely monotone.

Finally,
\[
\frac{-A'(t)}{A(t)}\sim-\frac1t\quad(t\downarrow0),
\qquad
\frac{-A'(t)}{A(t)}\sim\frac1t\quad(t\to\infty),
\]
so the supremum defining \(b_*\) is finite.

_Proof source: `private proof note`._

## Do not claim

- Do not claim APP status.
- Do not claim the decimal value of b_* is certified.
- Do not claim uniqueness of the maximizing t.

## Tags

`bridge-result`, `complete-monotonicity`, `digamma`, `laplace-density`, `literature-closure-risk`, `not-app`, `proved`, `source-restatement-required`, `theorem`
