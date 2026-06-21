---
id: "T-AB-reciprocal-sum-gate-a-plus-b-le-one-third"
type: "theorem"
title: "Alzer Berg reciprocal Gini Gamma quotient complete monotonicity forces a plus b at most one third"
status: "proved"
tags: ["alzer-berg", "complete-monotonicity", "diagonal-gate", "gamma-quotient", "necessary-condition", "proved", "theorem"]
parents: ["T-AB-reciprocal-log-diagonal-expansion", "T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-ab-reciprocal-gini-gamma-quotient.md"]
---

# Theorem: Alzer Berg reciprocal Gini Gamma quotient complete monotonicity forces a plus b at most one third

## Statement

If \(x\mapsto1/P_{a,b}(u,v;x)\) is completely monotone on \((0,\infty)\) for every \(v>u>0\), then \(a+b\le1/3\).

## Dependencies

- [[wiki/nodes/T-AB-reciprocal-log-diagonal-expansion|Alzer Berg reciprocal Gini Gamma quotient logarithm diagonal cubic expansion]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `wiki/notes/frontier-ab-reciprocal-gini-gamma-quotient.md`

## Proof

For \(a\ne b\), the Gini mean is
\[
G_{a,b}(u,v)
=\left(\frac{u^a+v^a}{u^b+v^b}\right)^{1/(a-b)}.
\]
The case \(a=b\) is obtained by continuity. Put \(v=u+h=u(1+t)\). Then
\[
\log \frac{G_{a,b}(u,u+h)}{u}
=\frac{1}{a-b}
\left[
\log(1+(1+t)^a)-\log(1+(1+t)^b)
\right].
\]
For a real parameter \(c\),
\[
\log(1+(1+t)^c)
=\log2+\frac c2t+\frac{c(c-2)}8t^2+O(t^3).
\]
Thus
\[
\log \frac{G_{a,b}(u,u+h)}{u}
=\frac12t+\frac{a+b-2}{8}t^2+O(t^3).
\]
Exponentiating gives
\[
G_{a,b}(u,u+h)
=u+\frac h2+\frac{a+b-1}{8u}h^2+O(h^3).
\]

Let \(Q_{a,b}=1/P_{a,b}\), \(r=a+b\), and \(y=x+u\). With \(v=u+h\),
\[
\log Q_{a,b}(u,u+h;x)
=\log\Gamma(y+h)-\log\Gamma(y)
-h\,\psi(x+G_{a,b}(u,u+h)).
\]
Using the Gini expansion,
\[
x+G_{a,b}(u,u+h)
=y+\frac h2+\frac{r-1}{8u}h^2+O(h^3).
\]
Taylor expansion gives
\[
\log\Gamma(y+h)-\log\Gamma(y)
=h\psi(y)+\frac{h^2}{2}\psi'(y)+\frac{h^3}{6}\psi''(y)+O(h^4),
\]
and
\[
h\psi\left(y+\frac h2+\frac{r-1}{8u}h^2+O(h^3)\right)
=h\psi(y)+\frac{h^2}{2}\psi'(y)
h^3\left(\frac{r-1}{8u}\psi'(y)+\frac18\psi''(y)\right)+O(h^4).
\]
Therefore
\[
\log Q_{a,b}(u,u+h;x)
=h^3\left(
\frac{\psi''(y)}{24}
-\frac{r-1}{8u}\psi'(y)
\right)+O(h^4).
\]

Assume \(x\mapsto Q_{a,b}(u,v;x)\) is completely monotone for every \(v>u>0\). Then it is decreasing and nonnegative. Standard Gamma and digamma asymptotics give
\[
\lim_{x\to\infty}Q_{a,b}(u,v;x)=1.
\]
Hence \(Q_{a,b}(u,v;x)\ge1\), so \(\log Q_{a,b}(u,v;x)\ge0\).

For fixed \(u,x>0\), let \(h\downarrow0\). The leading coefficient in the expansion must be nonnegative:
\[
\frac{\psi''(y)}{24}
-\frac{r-1}{8u}\psi'(y)
\ge0.
\]
Since \(\psi'(y)>0\),
\[
r\le 1+\frac{u\psi''(y)}{3\psi'(y)}.
\]
Here \(y=x+u\), so for each \(y>0\) and every \(0<u<y\),
\[
r\le 1+\frac{u\psi''(y)}{3\psi'(y)}.
\]
Letting \(u\uparrow y\) gives
\[
r\le 1+\frac{y\psi''(y)}{3\psi'(y)}
\qquad (y>0).
\]
Finally, as \(y\downarrow0\),
\[
\psi'(y)\sim y^{-2},
\qquad
\psi''(y)\sim -2y^{-3}.
\]
Therefore
\[
1+\frac{y\psi''(y)}{3\psi'(y)}\to \frac13,
\]
and hence
\[
a+b=r\le \frac13.
\]

_Proof source: `private proof note`._

## Tags

`alzer-berg`, `complete-monotonicity`, `diagonal-gate`, `gamma-quotient`, `necessary-condition`, `proved`, `theorem`
