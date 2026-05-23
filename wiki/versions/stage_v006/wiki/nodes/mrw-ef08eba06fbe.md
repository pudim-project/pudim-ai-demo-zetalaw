---
id: mrw-ef08eba06fbe
type: proposition
title: Sign partition for reciprocal-digamma beta constraints
aliases: ["mrw-ef08eba06fbe", "Sign partition for reciprocal-digamma beta constraints"]
status: proved
tags: ["proposition", "proved", "digamma", "polygamma", "reciprocal-product", "beta-window", "sign-partition", "variational-reduction", "scout-audited", "source-grounded", "theory-growth"]
parents: [mrw-0e9002ec3122]
refs: []
---

# Proposition: Sign partition for reciprocal-digamma beta constraints

## Statement

Let
\[
A(x)=\psi(x)+x\psi'(x),\qquad
B(x)=\psi(x)\psi(1/x),
\]
and let \(z_\psi\) be the unique positive zero of \(\psi\).  Put
\[
a_\psi=\frac1{z_\psi}.
\]
Then \(A\) has a unique positive zero \(\eta_A\), and
\[
0<\eta_A<\frac12<a_\psi<1<z_\psi<2.
\]
Moreover,
\[
A(x)<0\quad(0<x<\eta_A),\qquad
A(x)>0\quad(x>\eta_A),
\]
and
\[
B(x)<0\quad(0<x<a_\psi\text{ or }x>z_\psi),
\]
while
\[
B(x)>0\quad(a_\psi<x<z_\psi).
\]

Consequently the pointwise reduction in [[wiki/nodes/mrw-0e9002ec3122|Pointwise reduction for reciprocal-digamma beta windows]] has no impossible point of the form \(A(x)\le0\le B(x)\).  If
\[
Q(x)=\frac{\log(B(x)/A(x))}{\log x}
\]
on the same-sign region \(A(x)B(x)>0\), then the beta-window is exactly
\[
\mathcal I
=
\left\{\beta\in\mathbb R:
\beta>Q(x)\ \text{for all }x\in(0,\eta_A)\cup(1,z_\psi),
\quad
\beta<Q(x)\ \text{for all }x\in(a_\psi,1)
\right\}.
\]
The intervals \((\eta_A,a_\psi)\) and \((z_\psi,\infty)\), and the boundary points \(x=\eta_A,a_\psi,1,z_\psi\), impose no beta-dependent restriction.

## Proof

The trigamma series gives
\[
\psi'(x)=\sum_{n=0}^\infty\frac1{(x+n)^2}>0
\]
for \(x>0\).  Hence \(\psi\) is strictly increasing.  Since
\[
\psi(1)=-\gamma<0,\qquad
\psi(2)=1-\gamma>0,
\]
there is a unique zero \(z_\psi\in(1,2)\).  Therefore \(a_\psi=1/z_\psi\) satisfies
\[
\frac12<a_\psi<1.
\]
The sign statement for \(B(x)=\psi(x)\psi(1/x)\) follows immediately from the sign of \(\psi(x)\) and \(\psi(1/x)\).

Now differentiate \(A\).  The locally uniformly convergent polygamma series give
\[
A'(x)=2\psi'(x)+x\psi''(x)
=2\sum_{n=0}^\infty\left(\frac1{(x+n)^2}-\frac{x}{(x+n)^3}\right)
=2\sum_{n=1}^\infty\frac{n}{(x+n)^3}>0.
\]
Thus \(A\) is strictly increasing.  As \(x\to0^+\),
\[
\psi(x)=-\frac1x-\gamma+O(x),\qquad
\psi'(x)=\frac1{x^2}+O(1),
\]
so
\[
A(x)=-\gamma+O(x)\to-\gamma<0.
\]
At \(x=1/2\), the classical values
\[
\psi(1/2)=-\gamma-2\log2,\qquad
\psi'(1/2)=\frac{\pi^2}{2}
\]
give
\[
A(1/2)=-\gamma-2\log2+\frac{\pi^2}{4}.
\]
Using the standard elementary bounds \(\gamma<3/5\), \(\log2<7/10\), and \(\pi^2>9\), we get
\[
A(1/2)>\frac94-\frac35-\frac75=\frac14>0.
\]
Since \(A\) is strictly increasing and starts negative, it has a unique zero \(\eta_A\), and \(0<\eta_A<1/2\).  Combining this with \(1/2<a_\psi\) gives the claimed ordering and the sign statement for \(A\).

It remains only to translate the signs into beta constraints.  On \((0,\eta_A)\), both \(A\) and \(B\) are negative and \(x<1\), so the pointwise reduction gives the lower constraint \(\beta>Q(x)\).  On \((\eta_A,a_\psi)\), \(A>0\) and \(B<0\), so \(F_\beta(x)=x^\beta A(x)-B(x)>0\) automatically.  On \((a_\psi,1)\), both \(A\) and \(B\) are positive and \(x<1\), so the constraint is \(\beta<Q(x)\).  On \((1,z_\psi)\), both \(A\) and \(B\) are positive and \(x>1\), so the constraint is \(\beta>Q(x)\).  On \((z_\psi,\infty)\), \(A>0\) and \(B<0\), so there is again no restriction.

At \(x=\eta_A\), \(A=0\) and \(B<0\), so \(F_\beta=-B>0\).  At \(x=a_\psi\) or \(x=z_\psi\), \(B=0\) and \(A>0\), so \(F_\beta=x^\beta A>0\).  At \(x=1\),
\[
F_\beta(1)=A(1)-B(1)=\frac{\pi^2}{6}-\gamma-\gamma^2>0
\]
by the same standard bounds.  Hence the displayed formula for \(\mathcal I\) contains all and only the beta-dependent constraints.

## Depends on

- [[wiki/nodes/mrw-0e9002ec3122|Pointwise reduction for reciprocal-digamma beta windows]]

## Used by

## Notes

- This proposition audits the empty/scaffold Scout pass `20260523T153713Z-scout-forage` and continues the prior Candidate 3 branch without importing any Scout claims from that scaffold.
- The result does not certify the sharp upper endpoint.  It narrows the remaining work to a lower-envelope question on \((0,\eta_A)\cup(1,z_\psi)\) and an upper-envelope question on \((a_\psi,1)\).
- The next useful target is to prove whether \(\sup_{(0,\eta_A)\cup(1,z_\psi)}Q=-1\) and to certify the global minimum of \(Q\) on \((a_\psi,1)\).
