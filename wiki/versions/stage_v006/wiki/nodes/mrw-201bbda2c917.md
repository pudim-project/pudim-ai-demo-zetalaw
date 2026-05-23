---
id: mrw-201bbda2c917
type: theorem
title: Right endpoint theorem for even-order polygamma beta windows
aliases: ["mrw-201bbda2c917", "Right endpoint theorem for even-order polygamma beta windows"]
status: proved
tags: ["theorem", "proved", "polygamma", "beta-window", "open-problem-4", "qi-lim-nantomah", "even-order", "right-endpoint", "hurwitz-zeta", "scout-audited", "source-grounded", "theory-growth"]
parents: [mrw-0241ab931d33, mrw-f3c6cef2ebb1]
refs: []
---

# Theorem: Right endpoint theorem for even-order polygamma beta windows

## Statement

Let \(n\ge2\) be even, and define
\[
C_n(x)=\psi^{(n)}(x)+x\psi^{(n+1)}(x),
\qquad
P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x).
\]
Then
\[
x^{n+1}C_n(x)-P_n(x)<0
\qquad(x>0).
\]
Consequently, the right endpoint \(\beta=n+1\) is admissible in the even-order Qi--Lim--Nantomah polygamma beta-window problem.

With
\[
Q_n(x)=\frac{\log(P_n(x)/C_n(x))}{\log x}
\qquad(x>0,\ x\ne1),
\]
the even-order admissible set is exactly
\[
\mathcal I_n
=
\left\{\beta\in\mathbb R:
\beta>Q_n(x)\text{ for every }0<x<1
\right\}
\cap(-\infty,n+1].
\]
Thus the even-order problem is reduced to the lower scalar envelope on \(0<x<1\).

## Proof

Use the sign-normalized Hurwitz-zeta notation
\[
Z_s(x)=\sum_{k=0}^{\infty}(x+k)^{-s},
\qquad
\Phi_m(x)=(-1)^{m+1}\psi^{(m)}(x)=m!Z_{m+1}(x).
\]
For even \(n\),
\[
\psi^{(n)}(x)=-n!Z_{n+1}(x),
\qquad
\psi^{(n+1)}(x)=(n+1)!Z_{n+2}(x),
\]
and hence
\[
C_n(x)=n!\bigl((n+1)xZ_{n+2}(x)-Z_{n+1}(x)\bigr),
\]
while
\[
P_n(x)=(n!)^2Z_{n+1}(x)Z_{n+1}(1/x).
\]

For every \(x>0\),
\[
xZ_{n+2}(x)<Z_{n+1}(x),
\]
because
\[
\frac{x}{(x+k)^{n+2}}\le\frac1{(x+k)^{n+1}}
\]
termwise, with strict inequality for every \(k\ge1\).  Therefore
\[
(n+1)xZ_{n+2}(x)-Z_{n+1}(x)<nZ_{n+1}(x).
\]
Since \(n!\ge n\) for \(n\ge2\),
\[
C_n(x)<(n!)^2Z_{n+1}(x).
\]
Also the first term of \(Z_{n+1}(1/x)\) is \(x^{n+1}\), and all remaining terms are positive, so
\[
Z_{n+1}(1/x)>x^{n+1}.
\]
Combining the last two inequalities gives
\[
P_n(x)
=(n!)^2Z_{n+1}(x)Z_{n+1}(1/x)
>
x^{n+1}(n!)^2Z_{n+1}(x)
>
x^{n+1}C_n(x).
\]
This proves the endpoint inequality.

It remains to translate this into the beta window.  By [[wiki/nodes/mrw-0241ab931d33|Even-order envelope reduction for polygamma beta windows]], for even \(n\ge2\),
\[
\mathcal I_n
=
\left\{\beta:
\beta>Q_n(x)\text{ for every }0<x<1,\ 
\beta<Q_n(x)\text{ for every }x>1
\right\},
\]
and
\[
\lim_{x\to\infty}Q_n(x)=n+1.
\]
The endpoint inequality \(x^{n+1}C_n(x)<P_n(x)\) gives
\[
Q_n(x)<n+1\qquad(0<x<1)
\]
and
\[
Q_n(x)>n+1\qquad(x>1),
\]
with the direction reversed on \(0<x<1\) because \(\log x<0\).  Hence every \(\beta\le n+1\) satisfies the full upper family of constraints \(\beta<Q_n(x)\) for \(x>1\), while every \(\beta>n+1\) fails for all sufficiently large \(x\) because \(Q_n(x)\to n+1\).  The lower constraints on \(0<x<1\) remain exactly as stated.  This proves the exact reduction
\[
\mathcal I_n
=
\left\{\beta\in\mathbb R:
\beta>Q_n(x)\text{ for every }0<x<1
\right\}
\cap(-\infty,n+1].
\]

In particular, \(\beta=n+1\) is admissible for every even \(n\ge2\), because \(Q_n(x)<n+1\) for every \(0<x<1\).

## Depends on

- [[wiki/nodes/mrw-0241ab931d33|Even-order envelope reduction for polygamma beta windows]]
- [[wiki/nodes/mrw-f3c6cef2ebb1|Odd-order collapse for polygamma beta windows]]

## Used by

- [[wiki/nodes/mrw-30f9a055fa9a|Certified two-sevenths lower obstruction for the n=2 beta window]]
- [[wiki/nodes/mrw-2a62d2bc84ad|Coarse compact maximum bracket for the n=2 lower envelope]]
- [[wiki/nodes/mrw-fd6576e56da0|Exact even-order beta window outside n=2]]

## Notes

- This theorem audits and locally reproves Scout Candidate 1 from `20260523T161710Z-scout-forage`.
- It does not compute the lower envelope
\[
L_n=\sup_{0<x<1}Q_n(x).
\]
For \(n=2\), the dyadic obstruction [[wiki/nodes/mrw-f27a36284da5|Dyadic lower obstruction for the n=2 polygamma beta window]] proves \(L_2>2.22869\), but the exact lower endpoint remains open.
- The certified \(x=2/7\) obstruction in [[wiki/nodes/mrw-30f9a055fa9a|Certified two-sevenths lower obstruction for the n=2 beta window]] improves the proved lower bound to \(L_2>231/100\).
- The bracket theorem [[wiki/nodes/mrw-2a62d2bc84ad|Coarse compact maximum bracket for the n=2 lower envelope]] improves the certified lower bound to \(L_2>1157/500\) and gives a compact bracket for an interior maximizer.
- The result closes the whole \(x>1\) upper-envelope side for every even order.
- The later exact-window theorem [[wiki/nodes/mrw-fd6576e56da0|Exact even-order beta window outside n=2]] upgrades the even \(n\ge4\) subfamily from right-endpoint admissibility to the full exact interval \([n,n+1]\).
