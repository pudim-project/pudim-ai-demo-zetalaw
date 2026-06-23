---
id: "T-Q2-left-middle-1-100-9-50-qJ-cover"
type: "theorem"
title: "left middle zeta lower bound proves Q2 below qJ on [1/100,9/50]"
status: "proved"
tags: ["left-middle", "outside-cover", "proved", "q2-cover", "student", "theorem"]
parents: ["T-Exact-finite-certificate-verification-principle", "D-Rational-certificate-and-finite-cover-language"]
refs: ["raw/student/20260525T194109-q2-left-middle-zeta-subcover.py", "raw/student/20260525T194109-q2-reduced-middle-compact-roll.md"]
---

# Theorem: left middle zeta lower bound proves Q2 below qJ on [1/100,9/50]

## Statement

For \(1/100\le x\le9/50\), the denominator identity gives \(3xZ_4(x)-Z_3(x)<2x^{-3}\), hence \(R(x)>Z_3(1/x)\). A finite rational subdivision certificate proves \(Z_3(1/x)>x^{23/10}\) on this interval, so \(Q_2(x)<23/10<q_J\).

## Dependencies

- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]
- [[wiki/nodes/D-Rational-certificate-and-finite-cover-language|Rational certificates and finite covers]]

## Proof and provenance references

- `raw/student/20260525T194109-q2-left-middle-zeta-subcover.py`
- `raw/student/20260525T194109-q2-reduced-middle-compact-roll.md`

## Proof

This proof run proves a new true auxiliary outside-cover node:

the Q2 left middle 1 100 9 50 qJ cover.

Let
\[
D(x)=3xZ_4(x)-Z_3(x).
\]
For \(0<x<1/2\),
\[
D(x)
=2x^{-3}+\sum_{k=1}^{\infty}\frac{2x-k}{(x+k)^4}
<2x^{-3},
\]
because \(2x-k<0\) for every \(k\ge1\). Since \(Z_3(x)>x^{-3}\), the defining formula for \(R\) gives
\[
R(x)=\frac{2Z_3(x)Z_3(1/x)}{D(x)}
>Z_3(1/x).
\]

The replayable certificate

\begin{verbatim}
\end{verbatim}

uses the true Hurwitz-zeta integral-tail enclosure with \(N=4000\). On a deterministic adaptive cover of \([1/100,9/50]\), for each rational interval \([a/10^6,b/10^6]\) it proves
\[
\underline Z_3(10^6/a)^{10}>(b/10^6)^{23},
\]
where \(\underline Z_3(10^6/a)\) is the certified lower bound for \(Z_3(1/(a/10^6))\). Therefore
\[
Z_3(1/x)>x^{23/10}
\]
throughout \([1/100,9/50]\). Combining with \(R(x)>Z_3(1/x)\), and using \(0<x<1\), gives
\[
Q_2(x)<23/10.
\]
The endpoint certificate gives \(q_J\ge2.3145474010789204>23/10\), so
\[
Q_2(x)<q_J
\qquad (1/100\le x\le9/50).
\]

The certificate output was:

\begin{verbatim}
interval_count 160
worst_margin_positive True
\end{verbatim}

Together with the earlier true near-zero node, the left outside region is now covered on \((0,9/50]\).

I also tested a direct comparison route
\[
\log R(x)>\theta\log x
\]
with \(\theta=115727/50000=2.31454<q_J\). This is the right inequality for \(Q_2(x)<\theta\), since \(\log x<0\).

The route is promising near the reduced finite-middle endpoints: one-microinterval tests pass at \([281799/10^6,281800/10^6]\) and \([293000/10^6,293001/10^6]\). However, the broad adaptive run hit the same exact-log obstruction already seen in earlier rolls: the atanh logarithm enclosure is inefficient when the certified lower bound for \(R\) is very small, so broad intervals near \(1/100\) produce useless lower logs unless split by a different analytic mechanism.

This diagnostic was not promoted as Theory. It does suggest the next finite-middle certificate should combine:

the new \(R>Z_3(1/x)\) left-middle mechanism through \(9/50\);
direct \(\log R>\theta\log x\) or Taylor-model intervals only after the small-\(R\) regime has been removed;
compact derivative/Taylor control around \([1409/5000,293/1000]\setminus J\).

The true outside-cover intervals are now:

\[
(0,1/100]\cup[1/100,9/50]\cup[9/10,1).
\]

The finite-middle cover still needs:

\[
[9/50,1409/5000]\cup[293/1000,9/10].
\]

The compact one-crossing/dominance route still needs a proof on:

\[
[1409/5000,293/1000]\setminus J.
\]

The current argument candidates remain open because these two remaining certificate families are not complete.

_Proof source: `raw/student/20260525T194109-q2-reduced-middle-compact-roll.md`._

## Tags

`left-middle`, `outside-cover`, `proved`, `q2-cover`, `student`, `theorem`
