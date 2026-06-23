---
id: "T-Baricz-gamma-quotient-a2b3-not-BF"
type: "theorem"
title: "Baricz gamma quotient counterexample at a=2 b=3 is not Bernstein"
status: "proved"
tags: ["baricz", "bernstein-function", "counterexample", "gamma-quotient", "proved", "source-solving", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260530T212800-baricz-gamma-quotient-counterexample.json", "oracle/responses/ORACLE-FI-20260530T-elegance-038-oracle-forage-response.md", "raw/scout/FI-20260530T-elegance-038.md", "raw/student/20260530T212800-baricz-gamma-quotient-counterexample.md", "wiki/notes/frontier-baricz-gamma-quotient-bernstein.md"]
---

# Theorem: Baricz gamma quotient counterexample at a=2 b=3 is not Bernstein

## Statement

For \(a=2\) and \(b=3\), the Baricz Gamma quotient \(x\mapsto\Gamma(x)\Gamma(x-a+b)/(\Gamma(x-a)\Gamma(x+b))\) is not a Bernstein function on \((2,\infty)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260530T212800-baricz-gamma-quotient-counterexample.json`
- `oracle/responses/ORACLE-FI-20260530T-elegance-038-oracle-forage-response.md`
- `raw/scout/FI-20260530T-elegance-038.md`
- `raw/student/20260530T212800-baricz-gamma-quotient-counterexample.md`
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

_Proof source: `raw/student/20260530T212800-baricz-gamma-quotient-counterexample.md`._

## Tags

`baricz`, `bernstein-function`, `counterexample`, `gamma-quotient`, `proved`, `source-solving`, `theorem`
