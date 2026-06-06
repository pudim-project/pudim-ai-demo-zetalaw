---
id: "T-Q2-near-one-9-10-qJ-cover"
type: "theorem"
title: "finite rational subdivision proves near one Q2 below qJ on [9/10,1)"
status: "proved"
tags: ["near-one", "outside-cover", "proved", "q2-cover", "student", "theorem"]
parents: ["T-Exact-finite-certificate-verification-principle", "D-Rational-certificate-and-finite-cover-language"]
refs: ["raw/student/20260525T191756-q2-final-cover-mechanisms-roll.md", "raw/student/20260525T191756-q2-near-one-rgt1-certificate.py"]
---

# Theorem: finite rational subdivision proves near one Q2 below qJ on [9/10,1)

## Statement

On \([9/10,1)\), a finite rational subdivision certificate proves \(R(x)>1\). Since \(0<x<1\) implies \(\log x<0\), this gives \(Q_2(x)<0<q_J\) throughout \([9/10,1)\).

## Dependencies

- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]
- [[wiki/nodes/D-Rational-certificate-and-finite-cover-language|Rational certificates and finite covers]]

## Proof and provenance references

- `raw/student/20260525T191756-q2-final-cover-mechanisms-roll.md`
- `raw/student/20260525T191756-q2-near-one-rgt1-certificate.py`

## Proof

This proof run proves the auxiliary near-one cover:

the Q2 near one 9 10 qJ cover.

It is enough to prove \(R(x)>1\) on \([9/10,1)\). Then \(\log R(x)>0\) and \(\log x<0\), so
\[
Q_2(x)=\frac{\log R(x)}{\log x}<0<q_J.
\]

For \(x\in[a,b]\subset[9/10,1]\), write
\[
A=Z_3(x),\qquad B=Z_3(1/x),\qquad C=Z_4(x),
\]
and
\[
D=3xC-A.
\]
The verifier uses monotonicity of \(Z_s\) to form rational bounds:
\[
A\ge L_3(b),
\qquad
B\ge L_3(1/a),
\qquad
C\le U_4(a),
\]
where \(L_s\) and \(U_s\) are the true integral-tail rational enclosures. It then certifies
\[
2L_3(b)L_3(1/a)>3b\,U_4(a)-L_3(b)\ge D,
\]
and separately certifies \(D>0\) on the same interval.

The replayable verifier is:

\begin{verbatim}
\end{verbatim}

It uses ten subintervals of width \(10^{-3}\) on \([0.90,0.91]\), then nine subintervals of width \(10^{-2}\) on \([0.91,1]\). The worst certified margin is on \([0.900,0.901]\):
\[
2L_3(b)L_3(1/a)-D_{\rm hi}
\ge 0.10105537374759396>0.
\]

Therefore \(R(x)>1\), and hence \(Q_2(x)<q_J\), on \([9/10,1)\).

The compact Taylor/derivative candidate remains open. This proof run did not build the Taylor-model or derivative-bounded certificate for \(G\) outside \(J\).

The adaptive finite-middle candidate remains open. The remaining outside-cover region is now reduced to
\[
\left[\frac1{100},\frac{1409}{5000}\right]
\cup
\left[\frac{293}{1000},\frac9{10}\right],
\]
because \((0,1/100]\) and \([9/10,1)\) are now true covered regions below \(q_J\).

derivative/Taylor control for \(G\) on the compact bracket outside \(J\), or
adaptive finite-middle coverage of
\[
\left[\frac1{100},\frac{1409}{5000}\right]
\cup
\left[\frac{293}{1000},\frac9{10}\right].
\]

_Proof source: `raw/student/20260525T191756-q2-final-cover-mechanisms-roll.md`._

## Tags

`near-one`, `outside-cover`, `proved`, `q2-cover`, `student`, `theorem`
