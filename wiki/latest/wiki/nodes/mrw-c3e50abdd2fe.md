---
id: mrw-c3e50abdd2fe
type: theorem
title: Refined Euler-Maclaurin n=2 admissible beta subwindow
aliases: ["mrw-c3e50abdd2fe", "Refined Euler-Maclaurin n=2 admissible beta subwindow"]
status: proved
tags: ["theorem", "proved", "polygamma", "beta-window", "open-problem-4", "qi-lim-nantomah", "n-2", "admissible-interval", "hurwitz-zeta", "reciprocal-tail", "euler-maclaurin", "sturm-certificate", "source-grounded", "theory-growth"]
parents: [mrw-da05add5bca1, mrw-0241ab931d33]
refs: []
---

# Theorem: Refined Euler-Maclaurin n=2 admissible beta subwindow

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
\left[\frac{257}{110},3\right]\subseteq\mathcal I_2.
\]

## Proof

As in [[wiki/nodes/mrw-da05add5bca1|Euler-Maclaurin n=2 admissible beta subwindow]], the \(n=2\) polygamma reduction gives
\[
F_{\beta,2}(x)
=
x^\beta C_2(x)-P_2(x)
<
4Z_3(x)\bigl(x^\beta-Z_3(1/x)\bigr).
\]
Thus it is enough to prove \(Z_3(1/x)>x^\beta\) for \(257/110\le\beta\le3\).

If \(x\ge1\), the first term gives
\[
Z_3(1/x)>x^3\ge x^\beta.
\]
Now let \(0<x<1\).  Since \(\beta\ge257/110\), it is enough to show
\[
Z_3(1/x)>x^{257/110}.
\]
The Euler--Maclaurin lower gate proved in [[wiki/nodes/mrw-da05add5bca1|Euler-Maclaurin n=2 admissible beta subwindow]] gives
\[
Z_3(1/x)>
\frac12x^2+\frac12x^3+\frac14x^4-\frac1{12}x^6
\qquad(0<x<1).
\]

It remains to compare the right side with \(x^{257/110}\).  Put \(y=x^{1/110}\).  After multiplying by the positive factor \(12y^{-220}\), the desired inequality is equivalent to
\[
P(y):=6+6y^{110}+3y^{220}-y^{440}-12y^{37}>0
\qquad(0<y<1).
\]
An exact Sturm calculation gives
\[
P(0)=6,\qquad P(1)=2,
\]
and zero roots in \((0,1)\): the sign variations of the Sturm chain at \(0\) and \(1\) are both \(13\).  Hence \(P(y)>0\) for \(0\le y\le1\), and so
\[
Z_3(1/x)>x^{257/110}\qquad(0<x<1).
\]

Thus \(Z_3(1/x)>x^\beta\) for every \(x>0\) and every \(257/110\le\beta\le3\).  The displayed bound for \(F_{\beta,2}\) gives \(F_{\beta,2}(x)<0\) for all \(x>0\), proving
\[
\left[\frac{257}{110},3\right]\subseteq\mathcal I_2.
\]

## Depends on

- [[wiki/nodes/mrw-da05add5bca1|Euler-Maclaurin n=2 admissible beta subwindow]]
- [[wiki/nodes/mrw-0241ab931d33|Even-order envelope reduction for polygamma beta windows]]

## Used by

- [[wiki/nodes/mrw-ea265a369095|Further refined Euler-Maclaurin n=2 admissible beta subwindow]]
- [[wiki/nodes/mrw-e497f41bfc07|Open Problem 4 reduction to the n=2 beta window]]

## Notes

- This sharpens the previous sufficient interval \([187/80,3]\) to \([257/110,3]\).
- It is sharpened by [[wiki/nodes/mrw-ea265a369095|Further refined Euler-Maclaurin n=2 admissible beta subwindow]], which proves \([397/170,3]\subseteq\mathcal I_2\).
- It is still not the exact \(n=2\) lower endpoint.
- Together with [[wiki/nodes/mrw-3712cf1c88d8|Refined compact localization for the n=2 lower-envelope maximum]], the current certified lower-envelope gap is
\[
\frac{4629}{2000}<L_2\le\frac{257}{110}.
\]
- Further tail-gate improvements remain possible, but the exact endpoint likely requires the derivative-sign route in [[wiki/nodes/mrw-a3170d192f6c|Critical-point equation for the n=2 lower-envelope maximum]].
