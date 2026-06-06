---
id: "T-Q2-compact-monotonicity-J-certificate"
type: "theorem"
title: "compact H positive certificate proves G decreasing and unique zero in J"
status: "proved"
tags: ["G-sign", "compact-one-crossing", "monotonicity", "proved", "student", "theorem"]
parents: ["T-endpoint-log-derivative-monotonicity-principle"]
refs: ["raw/student/20260525T185345-q2-fixed-scale-endpoint-certificate.py", "raw/student/20260525T195521-q2-compact-monotonicity-certificate.py", "raw/student/20260525T195521-q2-remainder-log-taylor-assembly-roll.md"]
---

# Theorem: compact H positive certificate proves G decreasing and unique zero in J

## Statement

On \([1409/5000,293/1000]\), a rational interval certificate proves \(H(x)=\Lambda(x)+x\Lambda'(x)>0\). Since \(\log x<0\), this gives \(G'(x)=\log x\,H(x)<0\). Together with the true endpoint signs \(G(287345/1000000)>0\) and \(G(287346/1000000)<0\), \(G\) has a unique zero \(\xi\in J\), \(Q_2\) is increasing to \(\xi\) and decreasing after \(\xi\) on the compact bracket.

## Dependencies

- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]

## Proof and provenance references

- `raw/student/20260525T185345-q2-fixed-scale-endpoint-certificate.py`
- `raw/student/20260525T195521-q2-compact-monotonicity-certificate.py`
- `raw/student/20260525T195521-q2-remainder-log-taylor-assembly-roll.md`

## Proof

This script proves a true auxiliary finite-middle outside-cover node:

the Q2 remaining finite middle 9 50 9 10 qJ cover.

The replayable certificate is:

\begin{verbatim}
\end{verbatim}

It proves
\[
Q_2(x)<q_J
\]
on
\[
\left[\frac9{50},\frac{1409}{5000}\right]
\cup
\left[\frac{293}{1000},\frac9{10}\right].
\]

The left bridge \([9/50,221050/1000000]\) uses the already-derived identity
\[
3xZ_4(x)-Z_3(x)
=2x^{-3}+\sum_{k=1}^{\infty}\frac{2x-k}{(x+k)^4}.
\]
For \(x<1/2\), this gives
\[
R(x)>Z_3(1/x).
\]
The certificate proves
\[
Z_3(1/x)>x^{1157/500}
\]
on \([9/50,221050/1000000]\). Since
\[
\frac{1157}{500}<\frac{115727}{50000}<q_J,
\]
this gives \(Q_2(x)<q_J\) on the bridge.

The remaining two subintervals use the direct comparison
\[
\log R(x)>\frac{115727}{50000}\log x.
\]
Since \(\log x<0\), this implies
\[
Q_2(x)<\frac{115727}{50000}<q_J.
\]
The script uses power-of-two range reduction for the atanh logarithm enclosure:
\[
\log r=\log(2^k r)-k\log 2,
\]
so every logarithm is evaluated with an argument in \([1,2)\).

The certificate output was:

\begin{verbatim}
interval_count 245
worst_margin_positive True
interval_count 3739
worst_margin_positive True
interval_count 3801
worst_margin_positive True
\end{verbatim}

Together with the earlier true covers \((0,9/50]\) and \([9/10,1)\), this covers all outside-compact points below \(q_J\).

This certificate also proves:

the Q2 compact monotonicity J certificate.

The replayable certificate is:

\begin{verbatim}
\end{verbatim}

Let
\[
H(x)=\Lambda(x)+x\Lambda'(x).
\]
Using \(Z_s'(x)=-sZ_{s+1}(x)\) and
\[
\frac{d}{dx}Z_s(1/x)=s x^{-2} Z_{s+1}(1/x),
\]
the script builds a rational interval enclosure for \(H\) using \(Z_3,\ldots,Z_6\) at \(x\) and \(Z_3,\ldots,Z_5\) at \(1/x\). It proves
\[
H(x)>0
\qquad
\left(\frac{1409}{5000}\le x\le\frac{293}{1000}\right).
\]

Since
\[
G'(x)=\log x\,H(x)
\]
and \(\log x<0\) on the compact bracket, this gives
\[
G'(x)<0.
\]
The existing endpoint certificate proves
\[
G(287345/1000000)>0,
\qquad
G(287346/1000000)<0.
\]
Therefore \(G\) has a unique zero
\[
\xi\in J=\left[\frac{287345}{1000000},\frac{287346}{1000000}\right],
\]
with \(G>0\) to the left of \(J\) and \(G<0\) to the right of \(J\) on the compact bracket.

Because
\[
Q_2'(x)=\frac{G(x)}{x(\log x)^2},
\]
\(Q_2\) is increasing before \(\xi\) and decreasing after \(\xi\) on the compact bracket.

The certificate output was:

\begin{verbatim}
\end{verbatim}

The true cover package is now:

\[
(0,9/50]\cup
\left[9/50,\frac{1409}{5000}\right]\cup
\left[\frac{293}{1000},9/10\right]\cup
[9/10,1).
\]

All points outside the compact bracket have \(Q_2(x)<q_J\), and \(q_J<Q_2(\xi)\) by the certified inner witness. On the compact bracket, \(Q_2\) has a unique maximum at the unique zero \(\xi\in J\). Thus
\[
L_2=Q_2(\xi).
\]

At \(\beta=Q_2(\xi)\), the defining inequality has equality at \(x=\xi\), so the lower endpoint is excluded. The known upper endpoint remains included. Therefore
\[
\mathcal I_2=(Q_2(\xi),3].
\]

This proves the terminal exact endpoint node.

_Proof source: `raw/student/20260525T195521-q2-remainder-log-taylor-assembly-roll.md`._

## Tags

`G-sign`, `compact-one-crossing`, `monotonicity`, `proved`, `student`, `theorem`
