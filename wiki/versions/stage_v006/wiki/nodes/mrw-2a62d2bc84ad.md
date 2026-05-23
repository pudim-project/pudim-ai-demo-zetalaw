---
id: mrw-2a62d2bc84ad
type: corollary
title: Coarse compact maximum bracket for the n=2 lower envelope
aliases: ["mrw-2a62d2bc84ad", "Coarse compact maximum bracket for the n=2 lower envelope"]
status: proved
tags: ["corollary", "proved", "polygamma", "beta-window", "open-problem-4", "qi-lim-nantomah", "n-2", "lower-envelope", "maximum-bracket", "rational-certificate", "validated-interval", "theory-growth"]
parents: [mrw-30f9a055fa9a, mrw-201bbda2c917, mrw-0241ab931d33]
refs: ["references/sources/20260518T101945Z-qi-lim-nantomah-polygamma-open-problems.md"]
---

# Corollary: Coarse compact maximum bracket for the n=2 lower envelope

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
Q_2(1/4)<\frac{1157}{500}
<Q_2(2/7),
\qquad
Q_2(1/3)<\frac{1157}{500}
<Q_2(2/7).
\]
Consequently \(Q_2\) attains its maximum on the compact interval \([1/4,1/3]\) at some point
\[
\xi\in(1/4,1/3),
\]
and
\[
Q_2(\xi)>\frac{1157}{500}.
\]
In particular, the \(n=2\) lower envelope satisfies
\[
L_2:=\sup_{0<x<1}Q_2(x)>\frac{1157}{500},
\]
so every admissible \(n=2\) beta parameter satisfies
\[
\beta>\frac{1157}{500}.
\]

## Proof

Put
\[
Z_s(a)=\sum_{k=0}^{\infty}(a+k)^{-s}.
\]
For \(n=2\),
\[
C_2(x)=2(3xZ_4(x)-Z_3(x)),
\qquad
P_2(x)=4Z_3(x)Z_3(1/x),
\]
so
\[
R(x):=\frac{P_2(x)}{C_2(x)}
=
\frac{2Z_3(x)Z_3(1/x)}
{3xZ_4(x)-Z_3(x)}.
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
Substituting these rational upper and lower bounds into the formula for \(R(x)\) gives the following exact rational enclosures:
\[
R(2/7)<\frac{5507}{100000}
\qquad(N=30),
\]
\[
R(1/4)>\frac{4049}{100000}
\qquad(N=20),
\]
and
\[
R(1/3)>\frac{789}{10000}
\qquad(N=20).
\]
The required power comparisons are exact:
\[
\left(\frac{5507}{100000}\right)^{500}
<
\left(\frac27\right)^{1157},
\]
\[
\left(\frac{4049}{100000}\right)^{500}
>
\left(\frac14\right)^{1157},
\]
and
\[
\left(\frac{789}{10000}\right)^{500}
>
\left(\frac13\right)^{1157}.
\]
Therefore
\[
R(2/7)<(2/7)^{1157/500},
\]
while
\[
R(1/4)>(1/4)^{1157/500},
\qquad
R(1/3)>(1/3)^{1157/500}.
\]
Since \(\log x<0\) on \(0<x<1\), the inequality \(Q_2(x)>r\) is equivalent to \(R(x)<x^r\), and \(Q_2(x)<r\) is equivalent to \(R(x)>x^r\).  Hence
\[
Q_2(1/4)<\frac{1157}{500}
<Q_2(2/7),
\qquad
Q_2(1/3)<\frac{1157}{500}
<Q_2(2/7).
\]

The function \(Q_2\) is continuous on \([1/4,1/3]\), because \(C_2\) and \(P_2\) are positive there by [[wiki/nodes/mrw-0241ab931d33|Even-order envelope reduction for polygamma beta windows]].  Thus \(Q_2\) attains a maximum on \([1/4,1/3]\).  Since both endpoints are below \(1157/500\) and the interior point \(2/7\) is above \(1157/500\), any maximizer on this compact interval lies in \((1/4,1/3)\) and has value above \(1157/500\).  The lower-envelope and beta-obstruction conclusions follow from the envelope reduction.

## Depends on

- [[wiki/nodes/mrw-0241ab931d33|Even-order envelope reduction for polygamma beta windows]]
- [[wiki/nodes/mrw-201bbda2c917|Right endpoint theorem for even-order polygamma beta windows]]
- [[wiki/nodes/mrw-30f9a055fa9a|Certified two-sevenths lower obstruction for the n=2 beta window]]

## Used by

- [[wiki/nodes/mrw-8c1324a498bf|Sharper compact maximum bracket for the n=2 lower envelope]]

## Notes

- Numerically, \(Q_2(2/7)\approx2.31454314355\), but the promoted threshold in this node is the rational level \(1157/500=2.314\).
- The later corollary [[wiki/nodes/mrw-8c1324a498bf|Sharper compact maximum bracket for the n=2 lower envelope]] refines this compact bracket from \([1/4,1/3]\) to \([7/25,3/10]\).
- This is a coarse compact bracket, not a uniqueness theorem and not a global upper bound for \(Q_2\) on \((0,1)\).
- The next useful target is a derivative-sign or interval-monotonicity certificate that either narrows this bracket or gives a global upper bound for \(Q_2\).
