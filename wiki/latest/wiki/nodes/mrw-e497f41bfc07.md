---
id: mrw-e497f41bfc07
type: corollary
title: Open Problem 4 reduction to the n=2 beta window
aliases: ["mrw-e497f41bfc07", "Open Problem 4 reduction to the n=2 beta window"]
status: proved
tags: ["corollary", "proved", "polygamma", "beta-window", "open-problem-4", "qi-lim-nantomah", "classification", "n-2", "exceptional-case", "source-grounded", "theory-growth"]
parents: [mrw-f3c6cef2ebb1, mrw-fd6576e56da0, mrw-ea265a369095]
refs: []
---

# Corollary: Open Problem 4 reduction to the n=2 beta window

## Statement

For \(n\ge1\), define
\[
C_n(x)=\psi^{(n)}(x)+x\psi^{(n+1)}(x),
\qquad
P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x),
\]
and
\[
\mathcal I_n=\{\beta\in\mathbb R:x^\beta C_n(x)-P_n(x)<0\text{ for all }x>0\}.
\]
Then Qi--Lim--Nantomah Open Problem 4 is solved for every \(n\ge1\) except possibly \(n=2\), in the following precise sense:

- If \(n\ge1\) is odd, then
\[
\mathcal I_n=\mathbb R.
\]
- If \(n\ge4\) is even, then
\[
\mathcal I_n=[n,n+1].
\]
- For \(n=2\), the exact lower endpoint remains unresolved.  With
\[
L_2=\sup_{0<x<1}Q_2(x),
\qquad
Q_2(x)=\frac{\log(P_2(x)/C_2(x))}{\log x},
\]
the current certified bounds are
\[
\frac{4629}{2000}<L_2\le\frac{397}{170},
\qquad
\left[\frac{397}{170},3\right]\subseteq\mathcal I_2.
\]

## Proof

The odd-order statement is exactly [[wiki/nodes/mrw-f3c6cef2ebb1|Odd-order collapse for polygamma beta windows]].  For every odd \(n\ge1\), that theorem proves
\[
x^\beta C_n(x)-P_n(x)<0
\]
for every \(x>0\) and every \(\beta\in\mathbb R\), hence \(\mathcal I_n=\mathbb R\).

The even \(n\ge4\) statement is exactly [[wiki/nodes/mrw-fd6576e56da0|Exact even-order beta window outside n=2]], which proves
\[
\mathcal I_n=[n,n+1]
\]
for every even \(n\ge4\).

It remains only to record the present \(n=2\) status.  The upper inclusion
\[
\left[\frac{397}{170},3\right]\subseteq\mathcal I_2
\]
is [[wiki/nodes/mrw-ea265a369095|Further refined Euler-Maclaurin n=2 admissible beta subwindow]].  The strict lower obstruction
\[
L_2>\frac{4629}{2000}
\]
follows from [[wiki/nodes/mrw-3712cf1c88d8|Refined compact localization for the n=2 lower-envelope maximum]].  Thus the only unresolved case of Open Problem 4, under the convention \(n\in\mathbb N=\{1,2,\ldots\}\), is the exact \(n=2\) lower endpoint.

## Depends on

- [[wiki/nodes/mrw-f3c6cef2ebb1|Odd-order collapse for polygamma beta windows]]
- [[wiki/nodes/mrw-fd6576e56da0|Exact even-order beta window outside n=2]]
- [[wiki/nodes/mrw-ea265a369095|Further refined Euler-Maclaurin n=2 admissible beta subwindow]]

## Used by

## Notes

- This is a consolidation node, not a new proof mechanism.
- The \(n=0\) digamma beta-window is Qi--Lim--Nantomah Open Problem 3 and is not part of this \(n\ge1\) Open Problem 4 classification.
- The next mathematical target is the exceptional \(n=2\) scalar envelope \(L_2\).
