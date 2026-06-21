---
id: "T-Baricz-gamma-quotient-BF-forall-negative-answer"
type: "theorem"
title: "Baricz gamma quotient Bernstein forall problem has negative answer"
status: "proved"
tags: ["application-candidate", "baricz", "bernstein-function", "gamma-quotient", "negative-answer", "proved", "source-solving", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "T-Baricz-gamma-quotient-a2b3-not-BF", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private proof note", "wiki/notes/frontier-baricz-gamma-quotient-bernstein.md"]
---

# Theorem: Baricz gamma quotient Bernstein forall problem has negative answer

## Statement

Baricz's question asking whether \(x\mapsto\Gamma(x)\Gamma(x-a+b)/(\Gamma(x-a)\Gamma(x+b))\) is a Bernstein function on \((a,\infty)\) for every \(a,b>0\) has a negative answer.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/T-Baricz-gamma-quotient-a2b3-not-BF|Baricz gamma quotient counterexample at a=2 b=3 is not Bernstein]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `wiki/notes/frontier-baricz-gamma-quotient-bernstein.md`

## Proof

Take \(a=2\), \(b=3\), and set \(y=x-2>0\). Then by the Gamma recurrence,
\[
\frac{\Gamma(x)\Gamma(x-a+b)}{\Gamma(x-a)\Gamma(x+b)}
=\frac{\Gamma(x)\Gamma(x+1)}{\Gamma(x-2)\Gamma(x+3)}
=\frac{(x-2)(x-1)}{(x+1)(x+2)}
=\frac{y(y+1)}{(y+3)(y+4)}.
\]

Let
\[
g(y)=\frac{y(y+1)}{(y+3)(y+4)},\qquad y>0.
\]

If \(g\) were a Bernstein function, then \(g'\) would be completely monotone. In particular \(g'''\ge0\) would be necessary.

Exact symbolic differentiation gives
\[
g'(y)=\frac{6(y^2+4y+2)}{(y+3)^2(y+4)^2},
\]
\[
g''(y)=
-\frac{12(y^3+6y^2+6y-10)}{(y+3)^3(y+4)^3},
\]
and
\[
g'''(y)=
\frac{36(y^4+8y^3+12y^2-40y-94)}{(y+3)^4(y+4)^4}.
\]

At \(y=1\),
\[
g'''(1)=-\frac{1017}{40000}<0.
\]

Therefore \(g'\) is not completely monotone, \(g\) is not Bernstein, and the Baricz for-all-\(a,b\) Bernstein question has a negative answer.

_Proof source: `private proof note`._

## Tags

`application-candidate`, `baricz`, `bernstein-function`, `gamma-quotient`, `negative-answer`, `proved`, `source-solving`, `theorem`
