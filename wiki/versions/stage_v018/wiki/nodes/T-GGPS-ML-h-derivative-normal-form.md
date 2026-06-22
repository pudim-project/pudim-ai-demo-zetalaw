---
id: "T-GGPS-ML-h-derivative-normal-form"
type: "theorem"
title: "GGPS h implicit Gamma digamma derivative normal form"
status: "proved"
tags: ["attack-plan", "digamma", "gamma", "implicit-function", "proved", "theorem", "wide"]
parents: ["T-Special-function-normal-form-calculus-principle"]
refs: ["attack-plans/AP-20260528T132000-ggps-ml-h-convexity.json", "librarian/audits/LA-20260528T132000-ggps-ml-h-attack-plan.json", "librarian/audits/LA-20260528T133000-ggps-ml-h-student.json", "raw/student/20260528T132500-ggps-ml-h-convexity.md", "wiki/notes/frontier-ggps-ml-h-convexity.md"]
---

# Theorem: GGPS h implicit Gamma digamma derivative normal form

## Statement

For \(F(x,y)=\log2+2\log\Gamma(x+y)-\log\Gamma(y)-\log\Gamma(2x+y)\) and \(F(x,h(x))=0\), the derivatives of \(h\) are given by \(h'=-F_x/F_y\) and \(h''=-(F_{xx}+2h'F_{xy}+(h')^2F_{yy})/F_y\), with the corresponding \(\psi\) and \(\psi'\) expressions.

## Dependencies

- [[wiki/nodes/T-Special-function-normal-form-calculus-principle|Special-function normal-form calculus principle]]

## Proof and provenance references

- `attack-plans/AP-20260528T132000-ggps-ml-h-convexity.json`
- `librarian/audits/LA-20260528T132000-ggps-ml-h-attack-plan.json`
- `librarian/audits/LA-20260528T133000-ggps-ml-h-student.json`
- `raw/student/20260528T132500-ggps-ml-h-convexity.md`
- `wiki/notes/frontier-ggps-ml-h-convexity.md`

## Proof

\emph{Setup.}
Let
\[
F(x,y)=\log2+2\log\Gamma(x+y)-\log\Gamma(y)-\log\Gamma(2x+y).
\]
The boundary function \(h\) is defined implicitly by
\[
F(x,h(x))=0,
\]
equivalently
\[
2\Gamma(x+h(x))^2=\Gamma(h(x))\Gamma(2x+h(x)).
\]

Implicit differentiation gives
\[
h'(x)=-\frac{F_x(x,h(x))}{F_y(x,h(x))}.
\]
Here
\[
F_x(x,y)=2\psi(x+y)-2\psi(2x+y),
\]
and
\[
F_y(x,y)=2\psi(x+y)-\psi(y)-\psi(2x+y).
\]
The source already proves \(F_y(x,h(x))>0\), so this gives a stable first-derivative normal form.

Differentiating once more,
\[
h''(x)=-
\frac{F_{xx}+2h'F_{xy}+(h')^2F_{yy}}{F_y},
\]
where all partial derivatives are evaluated at \((x,h(x))\), and
\[
F_{xx}=2\psi'(x+y)-4\psi'(2x+y),
\]
\[
F_{xy}=2\psi'(x+y)-2\psi'(2x+y),
\]
\[
F_{yy}=2\psi'(x+y)-\psi'(y)-\psi'(2x+y).
\]

This proves the GGPS ML h derivative normal form.

Write
\[
h(x)=ax+bx^2+cx^3+O(x^4).
\]
Use
\[
\log\Gamma(u)
=-\log u-\gamma u+\frac{\zeta(2)}2u^2-\frac{\zeta(3)}3u^3+O(u^4)
\qquad(u\to0^+).
\]

Equivalently, set \(h=xu(x)\). Then
\[
F(x,xu)=
\log\frac{2u(u+2)}{(u+1)^2}
+\sum_{n\ge2}\frac{(-1)^n\zeta(n)}{n}x^n
\left(2(1+u)^n-u^n-(2+u)^n\right).
\]
At the positive root \(u_0=\sqrt2-1\), the derivative of the logarithmic leading term is \(\sqrt2\ne0\), so the branch is analytic in \(x\) after this desingularization.

The constant term in \(F(x,h(x))\) is
\[
\log2+\log a+\log(a+2)-2\log(a+1),
\]
so \(a\) is determined by
\[
2a(a+2)=(a+1)^2.
\]
The positive solution is
\[
a=\sqrt2-1.
\]

With \(a=\sqrt2-1\), the coefficient of \(x\) is proportional to \(b\), so \(b=0\). Equivalently, \(u'(0)=0\). Since \(2(1+u)^2-u^2-(2+u)^2=-2\), the coefficient of \(x^2\) is proportional to
\[
6\sqrt2\,c-\pi^2,
\]
hence
\[
c=\frac{\pi^2}{6\sqrt2}
=\frac{\sqrt2\pi^2}{12}.
\]

Therefore
\[
h(x)=(\sqrt2-1)x+\frac{\sqrt2\pi^2}{12}x^3+O(x^4).
\]
Consequently
\[
h''(x)=\frac{\sqrt2\pi^2}{2}x+O(x^2),
\]
so there exists \(\varepsilon>0\) such that
\[
h''(x)>0
\qquad(0<x<\varepsilon).
\]

This proves the GGPS ML h small x convexity.

_Proof source: `raw/student/20260528T132500-ggps-ml-h-convexity.md`._

## Tags

`attack-plan`, `digamma`, `gamma`, `implicit-function`, `proved`, `theorem`, `wide`
