---
id: "T-Du-Wang-h3-middle-window-increasing"
type: "theorem"
title: "Du Wang h3 increasing on middle parameter window one half to one"
status: "proved"
tags: ["attack-plan", "digamma", "du-wang", "gamma", "middle-window", "monotonicity", "polygamma", "proved", "theorem"]
parents: ["T-Du-Wang-h31-middle-window-u-monotonicity"]
refs: ["private attack plan", "private librarian audit", "private Oracle response", "private scout artifact", "private proof note", "wiki/notes/frontier-du-wang-h3-monotonicity.md"]
---

# Theorem: Du Wang h3 increasing on middle parameter window one half to one

## Statement

For every \(1/2\le a\le1\), Du--Wang's function \(h_3\) is increasing on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Du-Wang-h31-middle-window-u-monotonicity|Du Wang h31 driver is nondecreasing from a nonnegative endpoint on the middle window]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private Oracle response`
- `private scout artifact`
- `private proof note`
- `wiki/notes/frontier-du-wang-h3-monotonicity.md`

## Proof

For \(t>1/2\), define
\[
S_m(t)=\sum_{n=0}^{\infty}\frac1{(n+t)^m}.
\]
The polygamma identities give
\[
\psi''(t)=-2S_3(t),\qquad \psi'''(t)=6S_4(t).
\]
Thus the desired bound
\[
-\frac{2\psi''(t)}{\psi'''(t)}\ge t-\frac12
\]
is equivalent to
\[
2S_3(t)-3\left(t-\frac12\right)S_4(t)\ge0.
\]
Write \(y=t-\frac12>0\).  Using
\[
S_m(t)=\frac1{\Gamma(m)}
\int_0^\infty \frac{x^{m-1}e^{-tx}}{1-e^{-x}}\,dx
\]
and
\[
\frac{e^{-tx}}{1-e^{-x}}
=e^{-yx}\frac1{2\sinh(x/2)},
\]
set
\[
K(x)=\frac1{2\sinh(x/2)}.
\]
Then
\[
2S_3(t)-3yS_4(t)
=
\int_0^\infty e^{-yx}x^2K(x)\,dx
-\frac y2\int_0^\infty e^{-yx}x^3K(x)\,dx.
\]
Since \(x^3K(x)\sim x^2\) as \(x\downarrow0\) and decays exponentially at
infinity, integration by parts gives
\[
y\int_0^\infty e^{-yx}x^3K(x)\,dx
=
\int_0^\infty e^{-yx}(x^3K(x))'\,dx.
\]
Therefore
\[
2S_3(t)-3yS_4(t)
=
\int_0^\infty e^{-yx}
\left(x^2K(x)-\frac12(x^3K(x))'\right)dx.
\]
Now
\[
K'(x)=-\frac12K(x)\coth(x/2),
\]
so
\[
x^2K(x)-\frac12(x^3K(x))'
=
\frac12x^2K(x)\left(\frac x2\coth(x/2)-1\right).
\]
For \(z>0\), \(z\coth z>1\).  The integrand is therefore strictly positive,
and
\[
2S_3(t)-3\left(t-\frac12\right)S_4(t)>0.
\]
This proves
\[
-\frac{2\psi''(t)}{\psi'''(t)}>t-\frac12,
\qquad t>\frac12.
\]

This proves the Du Wang polygamma ratio halfline bound.

Let \(1/2\le a\le1\), \(u>0\), and \(t=a+u\).  Since \(a\ge1/2\),
\[
u=t-a\le t-\frac12.
\]
The ratio lemma gives
\[
t-\frac12<-\frac{2\psi''(t)}{\psi'''(t)}.
\]
Because \(\psi'''(t)>0\),
\[
2\psi''(t)+u\psi'''(t)<0.
\]
Consequently
\[
H_a'(u)=-u^2\{2\psi''(t)+u\psi'''(t)\}>0.
\]
Together with \(H_a(0+)=2\log\Gamma(a)\ge0\), this gives
\[
H_a(u)\ge0
\qquad (u>0,\ 1/2\le a\le1).
\]

This proves the Du Wang h31 middle window u monotonicity.

For \(x>0\), \(u=x\), and \(t=x+a\),
\[
h_3'(x)=\widetilde h_3'(x+a)=\frac{h_{31}(x+a)}{x^2}
=\frac{H_a(x)}{x^2}\ge0.
\]
The inequality is strict for \(x>0\) except possibly at the endpoint
\(a=1,u=0\), which is outside the open \(x\)-interval.  Thus \(h_3\) is
increasing on \((0,\infty)\) for every
\[
\frac12\le a\le1.
\]

This monotonicity result combines with the previously proved outer-window nonmonotonicity theorem to complete the open-problem source classification.

The outer-window nonmonotonicity result proves that \(h_3\) is not monotone for
\[
0<a<\frac12
\qquad\text{or}\qquad
1<a<2.
\]
The middle-window theorem above proves increasing behavior for
\[
\frac12\le a\le1.
\]
Therefore Du--Wang Open Problem 2 is classified on \(0<a<2\):
\[
h_3 \text{ is increasing on }(0,\infty)
\quad\Longleftrightarrow\quad
\frac12\le a\le1,
\]
and it is not monotone on the two outer windows.

This proves the Du Wang h3 open problem 2 classification.

_Proof source: `private proof note`._

## Tags

`attack-plan`, `digamma`, `du-wang`, `gamma`, `middle-window`, `monotonicity`, `polygamma`, `proved`, `theorem`
