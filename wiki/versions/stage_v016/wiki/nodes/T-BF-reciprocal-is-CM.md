---
id: "T-BF-reciprocal-is-CM"
type: "theorem"
title: "reciprocal of nonzero Bernstein function is completely monotone"
status: "proved"
tags: ["bernstein-function", "closure-lemma", "complete-monotonicity", "proved", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260529T-next-loop-dagum-cm-student.json", "raw/student/20260529T-next-loop-dagum-cm.md", "wiki/notes/frontier-dagum-cm-threshold.md"]
---

# Theorem: reciprocal of nonzero Bernstein function is completely monotone

## Statement

If \(g\) is a nonzero Bernstein function on \((0,\infty)\), then \(1/g\) is completely monotone.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260529T-next-loop-dagum-cm-student.json`
- `raw/student/20260529T-next-loop-dagum-cm.md`
- `wiki/notes/frontier-dagum-cm-threshold.md`

## Proof

For \(0<\beta\le1\), \(x^\beta\) is a Bernstein function, so \(1+x^\beta\) is Bernstein. A nonzero Bernstein function has completely monotone reciprocal. Hence \((1+x^\beta)^{-1}\) is completely monotone. The factor \(x^{-\alpha}\) is completely monotone for \(\alpha\ge0\), and products of completely monotone functions are completely monotone. The case \(\beta=0\) is immediate because \(f_{\alpha,0}(x)=2^{-1}x^{-\alpha}\).

For \(1<\beta\le2\), put \(\gamma=\beta/2\in(1/2,1]\). The elementary Laplace identity
\[
\frac1{x(1+x^2)}=\int_0^\infty e^{-xt}(1-\cos t)\,dt
\]
shows that \(h(x)=1/(x(1+x^2))\) is completely monotone. Since \(x^\gamma\) is Bernstein, \(h(x^\gamma)\) is completely monotone. But
\[
h(x^\gamma)=\frac1{x^\gamma(1+x^{2\gamma})}
=\frac1{x^{\beta/2}(1+x^\beta)}
=f_{\beta/2,\beta}(x).
\]
Multiplication by \(x^{-(\alpha-\beta/2)}\) proves complete monotonicity for \(\alpha\ge\beta/2\).

For \(\beta=2\), sufficiency for \(\alpha\ge1\) follows from the preceding paragraph. For necessity, first \(f_{0,2}(x)=1/(1+x^2)\) is not completely monotone, for example because its inverse Laplace kernel is \(\sin t\).

Let \(0<\alpha<1\). The inverse Laplace kernel of \(x^{-\alpha}\) is \(t^{\alpha-1}/\Gamma(\alpha)\), and the inverse Laplace kernel of \(1/(1+x^2)\) is \(\sin t\). Hence the inverse kernel of \(f_{\alpha,2}\) is
\[
\eta_\alpha(t)=\frac1{\Gamma(\alpha)}\int_0^t(t-s)^{\alpha-1}\sin s\,ds.
\]
At \(t=2\pi\),
\[
\Gamma(\alpha)\eta_\alpha(2\pi)
=\int_0^\pi\left((2\pi-s)^{\alpha-1}-(\pi-s)^{\alpha-1}\right)\sin s\,ds.
\]
Since \(\alpha-1<0\), the bracket is negative for \(0<s<\pi\). Therefore \(\eta_\alpha(2\pi)<0\). By uniqueness of the Laplace transform for locally finite measures, \(f_{\alpha,2}\) cannot be completely monotone. Thus \(f_{\alpha,2}\in CM\) exactly when \(\alpha\ge1\).

_Proof source: `raw/student/20260529T-next-loop-dagum-cm.md`._

## Tags

`bernstein-function`, `closure-lemma`, `complete-monotonicity`, `proved`, `theorem`
