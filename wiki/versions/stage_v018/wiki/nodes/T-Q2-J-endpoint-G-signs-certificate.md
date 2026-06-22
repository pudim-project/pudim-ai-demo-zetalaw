---
id: "T-Q2-J-endpoint-G-signs-certificate"
type: "theorem"
title: "fixed scale rational interval certificate proves G left endpoint positive and right endpoint negative on J"
status: "proved"
tags: ["G-sign", "microinterval", "proved", "rational-interval-arithmetic", "student", "theorem", "true-helper"]
parents: ["T-endpoint-log-derivative-monotonicity-principle"]
refs: ["raw/student/20260525T185345-q2-fixed-scale-endpoint-certificate.py", "raw/student/20260525T185345-q2-rational-interval-roll.md"]
---

# Theorem: fixed scale rational interval certificate proves G left endpoint positive and right endpoint negative on J

## Statement

Using fixed-scale outward-rounded rational interval arithmetic with scale \(10^{70}\), Hurwitz-zeta tail cutoff \(N=4000\), and atanh logarithm truncation \(m=220\), the endpoint signs on \(J=[287345/1000000,287346/1000000]\) are certified: \(G(287345/1000000)>0\) and \(G(287346/1000000)<0\).

## Dependencies

- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]

## Proof and provenance references

- `raw/student/20260525T185345-q2-fixed-scale-endpoint-certificate.py`
- `raw/student/20260525T185345-q2-rational-interval-roll.md`

## Proof

The useful progress is a replayable fixed-scale rational interval certificate for the endpoint signs on
\[
J=\left[\frac{287345}{1000000},\frac{287346}{1000000}\right].
\]

The verifier is:

\begin{verbatim}
\end{verbatim}

It uses:

decimal scale \(10^{70}\), interpreted as rational endpoints with denominator \(10^{70}\);
outward rounding after every interval operation;
the true Hurwitz-zeta tail enclosure with cutoff \(N=4000\);
the true atanh logarithm enclosure with truncation \(m=220\).

The right endpoint output is:
\[
G\left(\frac{287346}{1000000}\right)
\in
[-1.0114449998779718\cdot 10^{-7},
 -1.0004930415540797\cdot 10^{-7}],
\]
so
\[
G\left(\frac{287346}{1000000}\right)<0.
\]

The left endpoint output is:
\[
G\left(\frac{287345}{1000000}\right)
\in
[1.3291193143713952\cdot 10^{-6},
 1.3302145207712275\cdot 10^{-6}],
\]
so
\[
G\left(\frac{287345}{1000000}\right)>0.
\]

The same run gives certified endpoint intervals for \(Q_2\):
\[
Q_2\left(\frac{287346}{1000000}\right)
\in
[2.3145474010789204,\;2.3145474013074594],
\]
and
\[
Q_2\left(\frac{287345}{1000000}\right)
\in
[2.3145474010775446,\;2.314547401306085].
\]

This proves the auxiliary node the Q2 J endpoint G signs certificate.

The endpoint sign certificate gives an exact sign change in \(J\), but the terminal candidates also require:

a one-crossing certificate for \(G\) on the compact bracket;
a rational lower witness at or near the true maximizer, not just endpoint signs;
a finite outside-cover proof split into near-zero, finite-middle, and near-one regimes.

Those pieces were not completed in this roll.

_Proof source: `raw/student/20260525T185345-q2-rational-interval-roll.md`._

## Tags

`G-sign`, `microinterval`, `proved`, `rational-interval-arithmetic`, `student`, `theorem`, `true-helper`
