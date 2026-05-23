---
id: mrw-5fabc550bd7d
type: theorem
title: Explicit n=2 admissible beta subwindow
aliases: ["mrw-5fabc550bd7d", "Explicit n=2 admissible beta subwindow"]
status: proved
tags: ["theorem", "proved", "polygamma", "beta-window", "open-problem-4", "qi-lim-nantomah", "n-2", "admissible-interval", "hurwitz-zeta", "reciprocal-tail", "scout-audited", "source-grounded", "theory-growth"]
parents: [mrw-0241ab931d33]
refs: ["theory/forage/inbox/20260523T174843Z-scout-forage-inbox.md", "references/sources/20260518T101945Z-qi-lim-nantomah-polygamma-open-problems.md"]
---

# Theorem: Explicit n=2 admissible beta subwindow

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
\left[\frac52,3\right]\subseteq\mathcal I_2.
\]
Equivalently, for every \(5/2\le\beta\le3\) and every \(x>0\),
\[
x^\beta\bigl(\psi''(x)+x\psi^{(3)}(x)\bigr)
-\psi''(x)\psi''(1/x)<0.
\]

## Proof

For \(s>1\) and \(a>0\), write
\[
Z_s(a)=\sum_{k=0}^{\infty}(a+k)^{-s}.
\]
The standard polygamma expansion gives
\[
\psi''(x)=-2Z_3(x),
\qquad
\psi^{(3)}(x)=6Z_4(x).
\]
Thus
\[
F_{\beta,2}(x):=
x^\beta C_2(x)-P_2(x)
=
2x^\beta\bigl(3xZ_4(x)-Z_3(x)\bigr)
-4Z_3(x)Z_3(1/x).
\]

For every \(x>0\),
\[
xZ_4(x)
=\sum_{k=0}^{\infty}\frac{x}{(x+k)^4}
<
\sum_{k=0}^{\infty}\frac1{(x+k)^3}
=Z_3(x),
\]
because \(x\le x+k\) termwise and the terms with \(k\ge1\) are strict.  Hence
\[
3xZ_4(x)-Z_3(x)<2Z_3(x),
\]
and therefore
\[
F_{\beta,2}(x)
<
4Z_3(x)\bigl(x^\beta-Z_3(1/x)\bigr).
\]
Since \(Z_3(x)>0\), it remains to prove
\[
Z_3(1/x)>x^\beta
\]
for \(5/2\le\beta\le3\).

If \(x\ge1\), then the first term of \(Z_3(1/x)\) gives
\[
Z_3(1/x)>x^3\ge x^\beta,
\]
because \(\beta\le3\).

Now let \(0<x<1\).  Then \(\beta\ge5/2\) implies
\[
x^\beta\le x^{5/2}.
\]
Also
\[
Z_3(1/x)
=x^3\sum_{k=0}^{\infty}(1+kx)^{-3}.
\]
For \(f(t)=(1+xt)^{-3}\), the function \(f\) is positive, decreasing, and strictly convex on \([0,\infty)\).  The trapezoid estimate on each interval \([k,k+1]\), followed by summing and passing to the limit, gives
\[
\sum_{k=0}^{\infty}f(k)
>
\int_0^\infty f(t)\,dt+\frac12f(0)
=
\frac1{2x}+\frac12.
\]
For \(0<x<1\),
\[
\frac1{2x}+\frac12>x^{-1/2},
\]
because \(1+x>2\sqrt{x}\).  Consequently
\[
Z_3(1/x)
=x^3\sum_{k=0}^{\infty}(1+kx)^{-3}
>
x^3x^{-1/2}
=x^{5/2}
\ge x^\beta.
\]

The comparison \(Z_3(1/x)>x^\beta\) is therefore valid for all \(x>0\) and all \(5/2\le\beta\le3\).  Hence
\[
F_{\beta,2}(x)<0
\qquad(x>0),
\]
which proves the claimed admissible subwindow.

## Depends on

- [[wiki/nodes/mrw-0241ab931d33|Even-order envelope reduction for polygamma beta windows]]

## Used by

- [[wiki/nodes/mrw-19400778b4b5|Sharper explicit n=2 admissible beta subwindow]]

## Notes

- This theorem audits and locally proves Scout Candidate 1 from `20260523T174843Z-scout-forage`.
- It is a partial source-grounded result for Qi--Lim--Nantomah Open Problem 4, not the largest admissible \(n=2\) range.
- It is sharpened by [[wiki/nodes/mrw-19400778b4b5|Sharper explicit n=2 admissible beta subwindow]], which proves \([19/8,3]\subseteq\mathcal I_2\).
- Before the later sharpening, this theorem combined with [[wiki/nodes/mrw-3712cf1c88d8|Refined compact localization for the n=2 lower-envelope maximum]] gave the certified gap
\[
\frac{4629}{2000}<L_2\le\frac52,
\qquad
L_2=\sup_{0<x<1}Q_2(x).
\]
- The current sharper gap is recorded in [[wiki/nodes/mrw-19400778b4b5|Sharper explicit n=2 admissible beta subwindow]].
- The exact lower endpoint still requires a global upper bound for \(Q_2\) or a derivative-sign certification around the critical-point equation in [[wiki/nodes/mrw-a3170d192f6c|Critical-point equation for the n=2 lower-envelope maximum]].
