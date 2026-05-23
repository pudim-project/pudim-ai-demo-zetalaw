---
id: mrw-da05add5bca1
type: theorem
title: Euler-Maclaurin n=2 admissible beta subwindow
aliases: ["mrw-da05add5bca1", "Euler-Maclaurin n=2 admissible beta subwindow"]
status: proved
tags: ["theorem", "proved", "polygamma", "beta-window", "open-problem-4", "qi-lim-nantomah", "n-2", "admissible-interval", "hurwitz-zeta", "reciprocal-tail", "euler-maclaurin", "sturm-certificate", "source-grounded", "theory-growth"]
parents: [mrw-19400778b4b5, mrw-0241ab931d33]
refs: ["theory/forage/inbox/20260523T184322Z-scout-forage-inbox.md", "references/sources/20260518T101945Z-qi-lim-nantomah-polygamma-open-problems.md"]
---

# Theorem: Euler-Maclaurin n=2 admissible beta subwindow

## Statement

Let
\[
C_2(x)=\psi''(x)+x\psi^{(3)}(x),
\qquad
P_2(x)=\psi''(x)\psi''(1/x),
\]
and
\[
\mathcal I_2=\{\beta\in\mathbb R:x^\beta C_2(x)-P_2(x)<0\text{ for all }x>0\}.
\]
Then
\[
\left[\frac{187}{80},3\right]\subseteq\mathcal I_2.
\]

## Proof

As in [[wiki/nodes/mrw-19400778b4b5|Sharper explicit n=2 admissible beta subwindow]], put
\[
Z_s(a)=\sum_{k=0}^{\infty}(a+k)^{-s}
\]
and
\[
F_{\beta,2}(x)=x^\beta C_2(x)-P_2(x).
\]
The polygamma expansion gives
\[
F_{\beta,2}(x)
=
2x^\beta\bigl(3xZ_4(x)-Z_3(x)\bigr)
-4Z_3(x)Z_3(1/x).
\]
Since
\[
3xZ_4(x)-Z_3(x)<2Z_3(x),
\]
we have
\[
F_{\beta,2}(x)
<
4Z_3(x)\bigl(x^\beta-Z_3(1/x)\bigr).
\]
Thus it is enough to prove \(Z_3(1/x)>x^\beta\) for \(187/80\le\beta\le3\).

If \(x\ge1\), the first term gives
\[
Z_3(1/x)>x^3\ge x^\beta.
\]
Now let \(0<x<1\).  Since \(\beta\ge187/80\), it is enough to show
\[
Z_3(1/x)>x^{187/80}.
\]

First note that for \(u>0\),
\[
\frac1{1-e^{-u}}>
\frac1u+\frac12+\frac{u}{12}-\frac{u^3}{720}.
\]
Indeed, after multiplying the difference by \(720u(e^u-1)>0\), the numerator is
\[
N(u)=u^4e^u-u^4-60u^2e^u+60u^2+360ue^u+360u-720e^u+720.
\]
Its Taylor coefficients vanish before order \(7\), and for \(n\ge7\) the coefficient of \(u^n\) is
\[
\frac{(n-6)(n-5)(n-3)(n+8)}{n!}>0.
\]
Hence \(N(u)>0\) for \(u>0\).

Using
\[
(1+kx)^{-3}
=
\frac12\int_0^\infty t^2e^{-(1+kx)t}\,dt
\]
and summing the positive integrands gives
\[
\sum_{k=0}^{\infty}(1+kx)^{-3}
=
\frac12\int_0^\infty
\frac{t^2e^{-t}}{1-e^{-xt}}\,dt.
\]
The preceding Bernoulli lower bound with \(u=xt\) gives
\[
\sum_{k=0}^{\infty}(1+kx)^{-3}
>
\frac1{2x}+\frac12+\frac{x}{4}-\frac{x^3}{12}.
\]
Therefore
\[
Z_3(1/x)
=x^3\sum_{k=0}^{\infty}(1+kx)^{-3}
>
\frac12x^2+\frac12x^3+\frac14x^4-\frac1{12}x^6.
\]

It remains to compare the right side with \(x^{187/80}\).  Put \(y=x^{1/80}\).  After multiplying by the positive factor \(12y^{-160}\), the desired inequality is equivalent to
\[
P(y):=6+6y^{80}+3y^{160}-y^{320}-12y^{27}>0
\qquad(0<y<1).
\]
An exact Sturm calculation gives
\[
P(0)=6,\qquad P(1)=2,
\]
and zero roots in \((0,1)\): the sign variations of the Sturm chain at \(0\) and \(1\) are both \(13\).  Hence \(P(y)>0\) for \(0\le y\le1\), and so
\[
Z_3(1/x)>x^{187/80}\qquad(0<x<1).
\]

Thus \(Z_3(1/x)>x^\beta\) for every \(x>0\) and every \(187/80\le\beta\le3\).  The displayed bound for \(F_{\beta,2}\) then gives \(F_{\beta,2}(x)<0\) for all \(x>0\), proving
\[
\left[\frac{187}{80},3\right]\subseteq\mathcal I_2.
\]

## Depends on

- [[wiki/nodes/mrw-19400778b4b5|Sharper explicit n=2 admissible beta subwindow]]
- [[wiki/nodes/mrw-0241ab931d33|Even-order envelope reduction for polygamma beta windows]]

## Used by

- [[wiki/nodes/mrw-c3e50abdd2fe|Refined Euler-Maclaurin n=2 admissible beta subwindow]]
- [[wiki/nodes/mrw-e497f41bfc07|Open Problem 4 reduction to the n=2 beta window]]

## Notes

- This sharpens the previous sufficient interval \([19/8,3]\) to \([187/80,3]\).
- It is sharpened by [[wiki/nodes/mrw-c3e50abdd2fe|Refined Euler-Maclaurin n=2 admissible beta subwindow]], which proves \([257/110,3]\subseteq\mathcal I_2\).
- It is still not the exact \(n=2\) lower endpoint.
- Together with [[wiki/nodes/mrw-3712cf1c88d8|Refined compact localization for the n=2 lower-envelope maximum]], the current certified lower-envelope gap is
\[
\frac{4629}{2000}<L_2\le\frac{187}{80}.
\]
- The Bernoulli lower gate used here numerically has its own limiting threshold near \(2.3338651268\), so further progress toward the exact endpoint likely needs either a sharper tail gate or the derivative-sign route in [[wiki/nodes/mrw-a3170d192f6c|Critical-point equation for the n=2 lower-envelope maximum]].
