---
id: "T-Q2-near-zero-1-100-qJ-cover"
type: "theorem"
title: "near zero scaled bound proves Q2 below qJ on (0,1/100]"
status: "proved"
tags: ["near-zero", "outside-cover", "proved", "scaled-enclosure", "student", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle"]
refs: ["private proof note"]
---

# Theorem: near zero scaled bound proves Q2 below qJ on (0,1/100]

## Statement

For \(0<x\le1/100\), the scaled lower bound \(R(x)>100x^2/303\) implies \(Q_2(x)<23/10\). Since the certified endpoint witness satisfies \(q_J>23/10\), this gives \(Q_2(x)<q_J\) on the near-zero interval \((0,1/100]\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `private proof note`

## Proof

This proof run proves a true auxiliary near-zero outside-cover node:

the Q2 near zero 1 100 qJ cover.

For \(0<x\le1/100\), use the defining expression
\[
R(x)=\frac{2Z_3(x)Z_3(1/x)}{3xZ_4(x)-Z_3(x)}.
\]

The following elementary bounds hold:
\[
Z_3(x)>x^{-3},
\qquad
Z_3(1/x)>\frac{x^2}{2},
\]
and, since \(\sum_{k=1}^{\infty} k^{-4}<2\),
\[
Z_4(x)<x^{-4}+2<\frac{101}{100}x^{-4}.
\]
Therefore
\[
3xZ_4(x)-Z_3(x)<3xZ_4(x)<\frac{303}{100}x^{-3}.
\]
Combining these inequalities gives
\[
R(x)>\frac{100}{303}x^2.
\]

For \(0<x\le1/100\), the exact integer inequality
\[
303^{10}<100^{13}
\]
implies
\[
x^{3/10}\le(1/100)^{3/10}<\frac{100}{303}.
\]
Thus
\[
R(x)>x^{23/10}.
\]
Because \(0<x<1\), \(\log x<0\), so
\[
Q_2(x)=\frac{\log R(x)}{\log x}<\frac{23}{10}.
\]

The endpoint verifier from the previous roll certified
\[
q_J\ge2.3145474010789204>\frac{23}{10}.
\]
Therefore
\[
Q_2(x)<q_J
\qquad(0<x\le1/100).
\]

This solves the near-zero part on \((0,1/100]\), but not the full near-zero candidate, because that candidate is bundled with compact one-crossing and remaining outside-cover data needed to solve the terminal node.

I extended the fixed-scale evaluator to variable input intervals using monotonicity:

\(Z_s(x)\) is decreasing in \(x\);
if \(x\in[a,b]\), then \(1/x\in[1/b,1/a]\), so \(Z_s(1/x)\) is bounded by endpoint evaluations.

The diagnostic script is:

\begin{verbatim}
\end{verbatim}

It shows the current direct interval propagation is much too wide on compact intervals. For example, with diagnostic settings \(N=800\), \(m=160\):

| interval | \(G\)-interval |
| --- | --- |
| \([0.2818,0.285]\) | \([-0.9506340057,0.8866459058]\) |
| \([0.2865,0.287345]\) | \([-0.2390965908,0.2352337019]\) |
| \([0.287346,0.288]\) | \([-0.1847162975,0.1807624398]\) |
| \([0.288,0.293]\) | \([-1.4708073814,1.2891978780]\) |

This does not prove or disprove the compact one-crossing route. It identifies interval dependency in \(\Lambda\), \(R\), and products involving \(x\log x\) as the immediate obstruction. A successful compact proof likely needs either much smaller adaptive intervals near \(J\), derivative/monotonicity information for the components, or a Taylor-model style enclosure instead of raw interval arithmetic.

No finite-middle/near-one cover was completed in this roll. The previous representative point checks remain useful, but converting them into a finite cover needs interval subdivision or a sharper model for \(Q_2\) on intervals.

a Taylor-model or derivative-bounded compact certificate for \(G\) outside \(J\), or
an adaptive finite-middle/near-one \(Q_2<q_J\) cover that avoids the raw interval dependency seen above.

_Proof source: `private proof note`._

## Tags

`near-zero`, `outside-cover`, `proved`, `scaled-enclosure`, `student`, `theorem`
