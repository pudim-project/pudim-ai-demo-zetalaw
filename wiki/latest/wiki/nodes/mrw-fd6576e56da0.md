---
id: mrw-fd6576e56da0
type: theorem
title: Exact even-order beta window outside n=2
aliases: ["mrw-fd6576e56da0", "Exact even-order beta window outside n=2"]
status: proved
tags: ["theorem", "proved", "polygamma", "beta-window", "open-problem-4", "qi-lim-nantomah", "even-order", "n-ge-4", "exact-window", "hurwitz-zeta", "factorial-gap", "scout-audited", "source-grounded", "theory-growth"]
parents: [mrw-0241ab931d33]
refs: ["theory/forage/inbox/20260523T181642Z-scout-forage-inbox.md", "references/sources/20260518T101945Z-qi-lim-nantomah-polygamma-open-problems.md"]
---

# Theorem: Exact even-order beta window outside n=2

## Statement

Let \(n\ge4\) be even, and define
\[
C_n(x)=\psi^{(n)}(x)+x\psi^{(n+1)}(x),
\qquad
P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x).
\]
Let
\[
\mathcal I_n=\{\beta\in\mathbb R:x^\beta C_n(x)-P_n(x)<0\text{ for all }x>0\}.
\]
Then
\[
\mathcal I_n=[n,n+1].
\]

## Proof

By [[wiki/nodes/mrw-0241ab931d33|Even-order envelope reduction for polygamma beta windows]], every admissible \(\beta\) satisfies
\[
n\le\beta\le n+1.
\]
It remains to prove that every \(\beta\in[n,n+1]\) is admissible.

For \(s>1\) and \(a>0\), put
\[
Z_s(a)=\sum_{k=0}^{\infty}(a+k)^{-s}.
\]
Since \(n\) is even,
\[
\psi^{(n)}(x)=-n!Z_{n+1}(x),
\qquad
\psi^{(n+1)}(x)=(n+1)!Z_{n+2}(x).
\]
Therefore
\[
C_n(x)=n!\big((n+1)xZ_{n+2}(x)-Z_{n+1}(x)\big)
\]
and
\[
P_n(x)=(n!)^2Z_{n+1}(x)Z_{n+1}(1/x).
\]

For every \(x>0\),
\[
xZ_{n+2}(x)<Z_{n+1}(x),
\]
because \(x/(x+k)^{n+2}\le (x+k)^{-n-1}\) termwise, with strict inequality for \(k\ge1\).  Hence
\[
C_n(x)<n\,n!Z_{n+1}(x).
\]
Thus
\[
x^\beta C_n(x)-P_n(x)
<
n!Z_{n+1}(x)\bigl(n x^\beta-n!Z_{n+1}(1/x)\bigr).
\]
It is enough to prove
\[
(n-1)!Z_{n+1}(1/x)>x^\beta.
\]

If \(x\ge1\), the first term of \(Z_{n+1}(1/x)\) gives
\[
Z_{n+1}(1/x)>x^{n+1}.
\]
Since \(\beta\le n+1\) and \((n-1)!>1\),
\[
(n-1)!Z_{n+1}(1/x)>(n-1)!x^{n+1}\ge x^\beta.
\]

If \(0<x<1\), then
\[
Z_{n+1}(1/x)
=
x^{n+1}\sum_{k=0}^{\infty}(1+kx)^{-n-1}.
\]
For the decreasing positive function \(f(t)=(1+xt)^{-n-1}\),
\[
\sum_{k=0}^{\infty}f(k)>\int_0^\infty f(t)\,dt=\frac1{nx}.
\]
Therefore
\[
Z_{n+1}(1/x)>\frac{x^n}{n}.
\]
Because \(n\ge4\),
\[
\frac{(n-1)!}{n}>1.
\]
Also \(x^n\ge x^\beta\) for \(0<x<1\) and \(\beta\ge n\).  Consequently
\[
(n-1)!Z_{n+1}(1/x)
>
\frac{(n-1)!}{n}x^n
>
x^\beta.
\]
This proves \(x^\beta C_n(x)-P_n(x)<0\) for all \(x>0\) and all \(\beta\in[n,n+1]\).  Combining with the necessary endpoint constraint gives
\[
\mathcal I_n=[n,n+1].
\]

## Depends on

- [[wiki/nodes/mrw-0241ab931d33|Even-order envelope reduction for polygamma beta windows]]

## Used by

- [[wiki/nodes/mrw-e497f41bfc07|Open Problem 4 reduction to the n=2 beta window]]

## Notes

- This theorem audits and locally proves Scout Candidate 1 from `20260523T181642Z-scout-forage`.
- Together with [[wiki/nodes/mrw-f3c6cef2ebb1|Odd-order collapse for polygamma beta windows]], this solves Qi--Lim--Nantomah Open Problem 4 for all \(n\ge1\) except the even exceptional case \(n=2\).
- The proof fails exactly at \(n=2\), where \((n-1)!/n=1/2<1\).  This explains why the current \(n=2\) route needs genuine lower-envelope maximization rather than the factorial-gap shortcut.
- The consolidated classification status is recorded in [[wiki/nodes/mrw-e497f41bfc07|Open Problem 4 reduction to the n=2 beta window]].
