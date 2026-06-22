---
id: "T-YT-Bessel-W-nu-minus-half-Bernstein-slice"
type: "theorem"
title: "Yang Tian Bessel W conjecture boundary slice nu=-1/2 is Bernstein for tau <= 1/2"
status: "proved"
tags: ["attack-plan", "bernstein-function", "bessel", "partial-source-slice", "proved", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-Complete-monotonicity-closure-calculus-principle"]
refs: ["attack-plans/AP-20260528T172500-yang-tian-bessel-w-boundary.json", "librarian/audits/LA-20260528T173000-yang-tian-bessel-student.json", "raw/student/20260528T173000-yang-tian-bessel-w-boundary.md", "wiki/notes/frontier-yang-tian-bessel-w-bernstein.md"]
---

# Theorem: Yang Tian Bessel W conjecture boundary slice nu=-1/2 is Bernstein for tau <= 1/2

## Statement

For every \(\tau\in(0,1/2]\), the function \(x\mapsto W_{-1/2}(x^\tau)=x^\tau\coth(x^\tau)\) is a Bernstein function on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `attack-plans/AP-20260528T172500-yang-tian-bessel-w-boundary.json`
- `librarian/audits/LA-20260528T173000-yang-tian-bessel-student.json`
- `raw/student/20260528T173000-yang-tian-bessel-w-boundary.md`
- `wiki/notes/frontier-yang-tian-bessel-w-bernstein.md`

## Proof

The modified Bessel functions of half-integer order satisfy
\[
I_{-1/2}(x)=\sqrt{\frac2{\pi x}}\cosh x,\qquad
I_{1/2}(x)=\sqrt{\frac2{\pi x}}\sinh x.
\]
Therefore
\[
W_{-1/2}(x)
=\frac{xI_{-1/2}(x)}{I_{1/2}(x)}
=x\coth x.
\]
Thus the bounded slice is equivalent to proving that
\[
f_\tau(x)=x^\tau\coth(x^\tau)
\]
is Bernstein for \(0<\tau\le1/2\).

Let
\[
g(s)=\sqrt{s}\coth\sqrt{s},\qquad s>0.
\]
The classical Mittag--Leffler expansion gives
\[
z\coth z=1+2z^2\sum_{n=1}^\infty\frac1{z^2+\pi^2n^2}.
\]
With \(z=\sqrt{s}\),
\[
g(s)=1+2s\sum_{n=1}^\infty\frac1{s+\pi^2n^2}.
\]
Termwise differentiation is justified locally uniformly on compact subsets of \((0,\infty)\), since the differentiated series is dominated by a constant multiple of \(\sum n^{-2}\). Hence
\[
g'(s)
=2\sum_{n=1}^\infty
\frac{\pi^2n^2}{(s+\pi^2n^2)^2}.
\]
For every \(a>0\), the function \((s+a)^{-2}\) is completely monotone, since
\[
(-1)^m\frac{d^m}{ds^m}(s+a)^{-2}
=(m+1)!(s+a)^{-m-2}\ge0.
\]
Positive locally uniform sums of completely monotone functions are completely monotone, so \(g'\) is completely monotone. Therefore \(g\) is a Bernstein function.

This proves the YT Bessel W nu minus half partial fraction.

For \(0<a\le1\), \(x^a\) is a Bernstein function because
\[
\frac{d}{dx}x^a=ax^{a-1}
\]
is completely monotone. Bernstein functions are closed under composition: if \(f\) and \(h\) are Bernstein functions, then \(f\circ h\) is Bernstein.

This records the Bernstein functions composition closure.

Now fix \(0<\tau\le1/2\). Put \(a=2\tau\), so \(0<a\le1\). Then \(x^a\) is Bernstein, and
\[
f_\tau(x)=x^\tau\coth(x^\tau)
=g(x^{2\tau}).
\]
Since \(g\) and \(x^{2\tau}\) are Bernstein, their composition \(g(x^{2\tau})\) is Bernstein.

Hence
\[
x\mapsto W_{-1/2}(x^\tau)
\]
is a Bernstein function on \((0,\infty)\) for every \(0<\tau\le1/2\).

This proves the YT Bessel W nu minus half Bernstein slice.

_Proof source: `raw/student/20260528T173000-yang-tian-bessel-w-boundary.md`._

## Tags

`attack-plan`, `bernstein-function`, `bessel`, `partial-source-slice`, `proved`, `theorem`
