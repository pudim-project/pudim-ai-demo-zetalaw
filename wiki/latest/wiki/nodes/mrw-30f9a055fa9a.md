---
id: mrw-30f9a055fa9a
type: corollary
title: Certified two-sevenths lower obstruction for the n=2 beta window
aliases: ["mrw-30f9a055fa9a", "Certified two-sevenths lower obstruction for the n=2 beta window"]
status: proved
tags: ["corollary", "proved", "polygamma", "beta-window", "open-problem-4", "qi-lim-nantomah", "n-2", "lower-envelope", "rational-certificate", "validated-interval", "theory-growth"]
parents: [mrw-201bbda2c917, mrw-f27a36284da5, mrw-0241ab931d33]
refs: ["references/sources/20260518T101945Z-qi-lim-nantomah-polygamma-open-problems.md"]
---

# Corollary: Certified two-sevenths lower obstruction for the n=2 beta window

## Statement

Let
\[
C_2(x)=\psi''(x)+x\psi^{(3)}(x),
\qquad
P_2(x)=\psi''(x)\psi''(1/x),
\]
and
\[
Q_2(x)=\frac{\log(P_2(x)/C_2(x))}{\log x}
\qquad(0<x<1).
\]
Then
\[
Q_2(2/7)>\frac{231}{100}.
\]
Consequently, every admissible parameter in the \(n=2\) even-order polygamma beta window satisfies
\[
\beta>\frac{231}{100}.
\]
Together with [[wiki/nodes/mrw-201bbda2c917|Right endpoint theorem for even-order polygamma beta windows]], the current certified enclosure is
\[
\frac{231}{100}<\beta\le3,
\]
with \(\beta=3\) known to be admissible.

## Proof

Write
\[
Z_s(a)=\sum_{k=0}^{\infty}(a+k)^{-s}.
\]
For \(n=2\),
\[
\psi''(x)=-2Z_3(x),
\qquad
\psi^{(3)}(x)=6Z_4(x),
\]
so
\[
C_2(x)=2(3xZ_4(x)-Z_3(x)),
\qquad
P_2(x)=4Z_3(x)Z_3(1/x).
\]
At \(x=2/7\), put
\[
R=\frac{P_2(2/7)}{C_2(2/7)}
=
\frac{2Z_3(2/7)Z_3(7/2)}
{(6/7)Z_4(2/7)-Z_3(2/7)}.
\]

For \(s>1\), \(a>0\), and \(N\ge1\), define
\[
S_{s,N}(a)=\sum_{k=0}^{N-1}(a+k)^{-s},
\]
\[
L_{s,N}(a)=S_{s,N}(a)+\frac{(a+N)^{1-s}}{s-1},
\qquad
U_{s,N}(a)=S_{s,N}(a)+\frac{(a+N-1)^{1-s}}{s-1}.
\]
Monotone integral comparison gives
\[
L_{s,N}(a)<Z_s(a)<U_{s,N}(a).
\]
Using \(N=20\), exact rational arithmetic gives
\[
\frac67 L_{4,20}(2/7)-U_{3,20}(2/7)>\frac{8549}{100},
\]
and
\[
2U_{3,20}(2/7)U_{3,20}(7/2)<\frac{471}{100}.
\]
Therefore
\[
R<
\frac{471/100}{8549/100}
=\frac{471}{8549}
<\frac{551}{10000}.
\]
The final comparison is also rational:
\[
\left(\frac{551}{10000}\right)^{100}
<
\left(\frac27\right)^{231}.
\]
Hence
\[
R<\left(\frac27\right)^{231/100}.
\]
Since \(\log(2/7)<0\), dividing by \(\log(2/7)\) reverses the inequality and gives
\[
Q_2(2/7)
=\frac{\log R}{\log(2/7)}
>\frac{231}{100}.
\]

By [[wiki/nodes/mrw-0241ab931d33|Even-order envelope reduction for polygamma beta windows]], admissibility for \(n=2\) requires
\[
\beta>Q_2(x)\qquad(0<x<1).
\]
Thus every admissible \(\beta\) satisfies \(\beta>231/100\).  The admissible upper endpoint \(\beta=3\) follows from [[wiki/nodes/mrw-201bbda2c917|Right endpoint theorem for even-order polygamma beta windows]].

## Depends on

- [[wiki/nodes/mrw-0241ab931d33|Even-order envelope reduction for polygamma beta windows]]
- [[wiki/nodes/mrw-f27a36284da5|Dyadic lower obstruction for the n=2 polygamma beta window]]
- [[wiki/nodes/mrw-201bbda2c917|Right endpoint theorem for even-order polygamma beta windows]]

## Used by

- [[wiki/nodes/mrw-2a62d2bc84ad|Coarse compact maximum bracket for the n=2 lower envelope]]

## Notes

- Numerically, \(Q_2(2/7)\approx2.31454314355\), but the promoted claim is only the rational certificate \(Q_2(2/7)>231/100\).
- The stronger bracket theorem [[wiki/nodes/mrw-2a62d2bc84ad|Coarse compact maximum bracket for the n=2 lower envelope]] proves \(Q_2(2/7)>1157/500\) and brackets an interior maximizer on \([1/4,1/3]\).
- This is still not the global lower-envelope solution.  It improves the certified necessary lower bound and gives a reproducible interval-certificate template for later work near the suspected maximum.
