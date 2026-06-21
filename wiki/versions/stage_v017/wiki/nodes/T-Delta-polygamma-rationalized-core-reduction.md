---
id: "T-Delta-polygamma-rationalized-core-reduction"
type: "theorem"
title: "sufficiency reduces to D<A and D^5>A^6 for Delta normalized functions"
status: "proved"
tags: ["bridge-layer", "polygamma", "proved", "rationalized-inequality", "student", "theorem"]
parents: ["T-Special-function-normal-form-calculus-principle"]
refs: ["private librarian audit", "private proof note", "wiki/notes/frontier-trigamma-tetragamma-sharp-double-inequality.md"]
---

# Theorem: sufficiency reduces to D<A and D^5>A^6 for Delta normalized functions

## Statement

For \(A(x)=(x^2+4x+12)/(12(x+1)^2)\) and \(D(x)=x^4((\psi'(x))^2+\psi''(x))\), the sufficiency part of the Qi--Agarwal sharp exponent problem reduces to proving the two core inequalities \(D(x)<A(x)\) and \(D(x)^5>A(x)^6\) for all \(x>0\), together with positivity of \(D\).

## Dependencies

- [[wiki/nodes/T-Special-function-normal-form-calculus-principle|Special-function normal-form calculus principle]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `wiki/notes/frontier-trigamma-tetragamma-sharp-double-inequality.md`

## Proof

Let
\[
\Delta(x)=(\psi'(x))^2+\psi''(x),
\qquad
A(x)=\frac{x^2+4x+12}{12(x+1)^2},
\qquad
D(x)=x^4\Delta(x).
\]
The source's exponent inequality is
\[
\frac{1}{x^4}A(x)^\alpha<\Delta(x)<\frac{1}{x^4}A(x)^\beta
\]
for \(x>0\), with proposed sharp conditions \(\alpha\ge6/5\) and \(\beta\le1\).

For \(x>0\),
\[
0<A(x)<1,
\]
because the numerator is positive and
\[
12(x+1)^2-(x^2+4x+12)=11x^2+20x>0.
\]

As \(x\to0^+\), the standard polygamma expansions give
\[
\psi'(x)=\frac1{x^2}+\zeta(2)+O(x),
\qquad
\psi''(x)=-\frac2{x^3}+O(1).
\]
Hence
\[
D(x)=1-2x+O(x^2).
\]
Also
\[
A(x)=1-\frac53x+O(x^2).
\]
Therefore
\[
\frac{\log D(x)}{\log A(x)}\to\frac{2}{5/3}=\frac65.
\]
The lower inequality \(A(x)^\alpha<D(x)\) is equivalent, since \(\log A(x)<0\), to
\[
\alpha>\frac{\log D(x)}{\log A(x)}
\]
pointwise, with the usual endpoint limiting convention. Thus any global lower exponent must satisfy \(\alpha\ge6/5\).

As \(x\to\infty\), using the standard asymptotic expansions
\[
\psi'(x)=\frac1x+\frac1{2x^2}+\frac1{6x^3}+O(x^{-5}),
\]
and
\[
\psi''(x)=-\frac1{x^2}-\frac1{x^3}-\frac1{2x^4}+O(x^{-6}),
\]
one obtains
\[
D(x)=\frac1{12}+\frac1{6x}+O(x^{-2}).
\]
Meanwhile
\[
A(x)=\frac1{12}+\frac1{6x}+O(x^{-2}).
\]
Thus
\[
\frac{\log D(x)}{\log A(x)}\to1.
\]
The upper inequality \(D(x)<A(x)^\beta\) is equivalent to
\[
\frac{\log D(x)}{\log A(x)}>\beta,
\]
again because \(\log A(x)<0\). Therefore every global upper exponent must satisfy \(\beta\le1\).

This proves the Delta polygamma endpoint exponent necessity.

At the sharp endpoint exponents, the desired sufficiency is
\[
A(x)^{6/5}<D(x)<A(x).
\]
Since \(A(x)>0\), the lower bound is equivalent to
\[
D(x)^5>A(x)^6
\]
provided \(D(x)>0\). Therefore the sufficiency part reduces to the rationalized core
\[
D(x)<A(x),
\qquad
D(x)^5>A(x)^6,
\qquad
D(x)>0.
\]
This proves the Delta polygamma rationalized core reduction.

Numerical first contact supports the core inequalities on logarithmic samples from \(10^{-4}\) to \(10^4\). Endpoint expansions are also favorable:
\[
A(x)-D(x)=\frac{x}{3}+O(x^2)
\quad (x\to0^+),
\]
and
\[
A(x)-D(x)=\frac{41}{90x^2}+O(x^{-3})
\quad (x\to\infty).
\]
For the lower residual,
\[
D(x)^5-A(x)^6
=\frac{10\pi^2-97}{6}x^2+O(x^3)
\quad (x\to0^+),
\]
and
\[
D(x)^5-A(x)^6\to \frac{11}{12^6}
\quad (x\to\infty).
\]

_Proof source: `private proof note`._

## Tags

`bridge-layer`, `polygamma`, `proved`, `rationalized-inequality`, `student`, `theorem`
