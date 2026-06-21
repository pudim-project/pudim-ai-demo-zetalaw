---
id: "T-Q2-terminal-exact"
type: "theorem"
title: "determine exact I_2 via certified L_2 description"
status: "proved"
tags: ["n-2", "open-problem-4", "polygamma", "proved", "terminal", "theorem"]
parents: ["T-Q2-J-rational-interval-terminal-certificate", "T-Q2-adaptive-finite-middle-qJ-cover-terminal-certificate", "T-Q2-adaptive-middle-cover-reduced-terminal-certificate", "T-Q2-analytic-denominator-reduced-assembly-terminal-certificate", "T-Q2-atanh-outside-cover-terminal-certificate", "T-Q2-compact-G-interval-terminal-certificate", "T-Q2-compact-one-crossing-outside-J-terminal-certificate", "T-Q2-compact-taylor-monotonicity-J-terminal-certificate", "T-Q2-critical-sign-certificate", "T-Q2-critical-zero-exact-endpoint", "T-Q2-derivative-taylor-compact-J-terminal-certificate", "T-Q2-finite-middle-near-one-qJ-cover-terminal-certificate", "T-Q2-full-compact-G-subdivision-terminal-certificate", "T-Q2-log-enclosure-reduction-terminal-certificate", "T-Q2-microinterval-zeta-terminal-certificate", "T-Q2-near-one-variable-cover-terminal-certificate", "T-Q2-near-zero-scaled-outside-cover-terminal-certificate", "T-Q2-outside-bracket-isolation-certificate", "T-Q2-finite-outside-cover-404-173-certificate", "T-Q2-reduced-terminal-assembly-certificate", "T-Q2-remaining-finite-middle-log-cover-terminal-certificate", "T-Q2-right-endpoint-G-sign-terminal-certificate", "T-Q2-taylor-compact-one-crossing-terminal-certificate", "T-Q2-three-regime-outside-cover-terminal-certificate"]
refs: ["private librarian audit", "private proof note", "wiki/notes/frontier-q2-endpoint.md"]
---

# Theorem: determine exact I_2 via certified L_2 description

## Statement

The exact admissible beta set \(\mathcal I_2\) for Qi--Lim--Nantomah Open Problem 4 is determined by a certified value or certified description of \(L_2=\sup_{0<x<1}Q_2(x)\), including the endpoint-inclusion convention.

## Dependencies

- [[wiki/nodes/T-Q2-J-rational-interval-terminal-certificate|deterministic rational interval certificate on J for R Lambda G Q2 proves terminal endpoint]]
- [[wiki/nodes/T-Q2-adaptive-finite-middle-qJ-cover-terminal-certificate|adaptive finite middle cover below qJ plus compact and near one covers proves terminal endpoint]]
- [[wiki/nodes/T-Q2-adaptive-middle-cover-reduced-terminal-certificate|adaptive reduced finite middle cover below qJ plus compact one crossing proves terminal endpoint]]
- [[wiki/nodes/T-Q2-analytic-denominator-reduced-assembly-terminal-certificate|analytic denominator reduced assembly proves terminal endpoint]]
- [[wiki/nodes/T-Q2-atanh-outside-cover-terminal-certificate|atanh log outside cover plus compact root bracket proves terminal endpoint]]
- [[wiki/nodes/T-Q2-compact-G-interval-terminal-certificate|finite rational compact bracket G certificate proves unique xi, global L2=Q2(xi), I2=(Q2(xi),3]]]
- [[wiki/nodes/T-Q2-compact-one-crossing-outside-J-terminal-certificate|compact outside J G one crossing and Q2 below qJ plus outside bounds proves terminal endpoint]]
- [[wiki/nodes/T-Q2-compact-taylor-monotonicity-J-terminal-certificate|compact Taylor monotonicity around J plus outside covers proves terminal endpoint]]
- [[wiki/nodes/T-Q2-critical-sign-certificate|unique G zero in B and global Q2 maximum at xi]]
- [[wiki/nodes/T-Q2-critical-zero-exact-endpoint|unique global critical zero xi gives L2=Q2(xi) and I2=(Q2(xi),3]]]
- [[wiki/nodes/T-Q2-derivative-taylor-compact-J-terminal-certificate|derivative or Taylor compact certificate outside J plus covers proves terminal endpoint]]
- [[wiki/nodes/T-Q2-finite-middle-near-one-qJ-cover-terminal-certificate|finite middle and near one Q2 cover below qJ plus compact and near zero covers proves terminal endpoint]]
- [[wiki/nodes/T-Q2-full-compact-G-subdivision-terminal-certificate|full compact G subdivision around J proves unique maximum and terminal endpoint]]
- [[wiki/nodes/T-Q2-log-enclosure-reduction-terminal-certificate|analytic log enclosure reduction converts G and Q2 certification to rational inequalities determining L2]]
- [[wiki/nodes/T-Q2-microinterval-zeta-terminal-certificate|microinterval J zeta and atanh log certificate proves terminal endpoint]]
- [[wiki/nodes/T-Q2-near-one-variable-cover-terminal-certificate|near one variable change Q2 cover below qJ plus other covers proves terminal endpoint]]
- [[wiki/nodes/T-Q2-near-zero-scaled-outside-cover-terminal-certificate|near zero scaled Q2 cover below qJ plus compact and remaining covers proves terminal endpoint]]
- [[wiki/nodes/T-Q2-outside-bracket-isolation-certificate|outside bracket Q2 upper cover plus inside one-zero enclosure determines L2 and I2]]
- [[wiki/nodes/T-Q2-finite-outside-cover-404-173-certificate|finite outside cover below bracket maximizer plus 404/173 ceiling determines L2]]
- [[wiki/nodes/T-Q2-reduced-terminal-assembly-certificate|reduced assembly of true endpoint covers finite middle cover and compact certificate proves terminal endpoint]]
- [[wiki/nodes/T-Q2-remaining-finite-middle-log-cover-terminal-certificate|remaining finite middle direct log cover plus compact certificate proves terminal endpoint]]
- [[wiki/nodes/T-Q2-right-endpoint-G-sign-terminal-certificate|right endpoint exact G sign plus compact one crossing and outside comparison proves terminal endpoint]]
- [[wiki/nodes/T-Q2-taylor-compact-one-crossing-terminal-certificate|Taylor or derivative bounded compact one crossing outside J plus covers proves terminal endpoint]]
- [[wiki/nodes/T-Q2-three-regime-outside-cover-terminal-certificate|three regime outside Q2 cover below J witness plus compact one zero proves terminal endpoint]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `wiki/notes/frontier-q2-endpoint.md`

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

_Proof source: `private proof note`._

## Tags

`n-2`, `open-problem-4`, `polygamma`, `proved`, `terminal`, `theorem`
