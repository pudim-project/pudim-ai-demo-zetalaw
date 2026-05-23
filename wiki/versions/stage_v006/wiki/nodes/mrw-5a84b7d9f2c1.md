---
id: mrw-5a84b7d9f2c1
type: note
title: Pole-family obstruction for the P1 kernel route
aliases: ["mrw-5a84b7d9f2c1", "Pole-family obstruction for the P1 kernel route"]
status: proved
tags: ["note", "proved", "polygamma", "trigamma", "complete-monotonicity", "pole-family", "laplace-kernel", "frontier"]
parents: [mrw-1c9d9f07a4ef, mrw-f0a031feea8e]
refs: []
---

# Note: Pole-family obstruction for the P1 kernel route

## Statement

Let
\[
P_1(x)=\psi'(x)\psi'(1/x).
\]
The canonical partial-fraction inverse-Laplace decomposition of \(P_1''\) cannot be proved nonnegative by certifying each pole family separately.  More precisely, in the canonical decomposition, every integer-pole family \(e^{-mt}\) with \(m\ge3\) is negative for all sufficiently small \(t>0\), and every reciprocal-pole family \(e^{-t/n}\) with \(n\ge2\) is negative for all sufficiently small \(t>0\).

This does not refute complete monotonicity of \(P_1''\).  It only rules out a too-local pole-family positivity proof and forces any positive-kernel proof to use cross-family cancellation, renormalization, or a different transform.

## Proof

The trigamma series gives
\[
P_1(x)=\sum_{r,s\ge0}\frac{x^2}{(x+r)^2(1+sx)^2}.
\]
For \(r,s\ge1\), \(rs\ne1\), put \(c=1/s\).  Partial fractions give
\[
\begin{aligned}
\frac{x^2}{(x+r)^2(1+sx)^2}
=&\frac{r^2}{(rs-1)^2}\frac1{(x+r)^2}
+\frac{2r}{(rs-1)^3}\frac1{x+r}\\
&+\frac1{s^2(rs-1)^2}\frac1{(x+1/s)^2}
-\frac{2r}{(rs-1)^3}\frac1{x+1/s}.
\end{aligned}
\]
The axis terms are
\[
\frac{x^2}{(x+r)^2}=1-\frac{2r}{x+r}+\frac{r^2}{(x+r)^2},
\qquad
\frac1{(1+sx)^2}=\frac1{s^2}\frac1{(x+1/s)^2}.
\]
The exceptional term is
\[
\frac{x^2}{(x+1)^4}
=\frac1{(x+1)^2}-\frac2{(x+1)^3}+\frac1{(x+1)^4}.
\]

Since differentiating twice multiplies the inverse-Laplace density by \(t^2\), the integer pole \(m\ge2\) contributes
\[
K_m^{\mathrm{int}}(t)
=e^{-mt}t^2\left[
m^2t-2m+
\sum_{n\ge1}
\left(
\frac{m^2t}{(mn-1)^2}
+\frac{2m}{(mn-1)^3}
\right)
\right].
\]
For \(m\ge3\), the bracket at \(t=0\) is
\[
2m\left(\sum_{n\ge1}\frac1{(mn-1)^3}-1\right).
\]
But
\[
\sum_{n\ge1}\frac1{(mn-1)^3}
\le \frac1{(m-1)^3}+\sum_{r\ge1}\frac1{(mr)^3}
<\frac18+\frac2{27}<1
\]
for \(m\ge3\).  Hence \(K_m^{\mathrm{int}}(t)<0\) for all sufficiently small \(t>0\).

Similarly, the reciprocal pole \(1/n\), \(n\ge2\), contributes
\[
K_n^{\mathrm{rec}}(t)
=e^{-t/n}t^2\left[
\frac{t}{n^2}
+\sum_{m\ge1}
\left(
\frac{t}{n^2(mn-1)^2}
-\frac{2m}{(mn-1)^3}
\right)
\right].
\]
At \(t=0\), the bracket is
\[
-2\sum_{m\ge1}\frac{m}{(mn-1)^3}<0.
\]
Thus \(K_n^{\mathrm{rec}}(t)<0\) for all sufficiently small \(t>0\).

The desired conclusion follows: separate pole-family positivity is impossible in this canonical decomposition.

## Depends on

- [[wiki/nodes/mrw-1c9d9f07a4ef|P1 trigamma product complete-monotonicity frontier]]
- [[wiki/nodes/mrw-f0a031feea8e|Higher-order monotonicity of polygamma products Pn]]

## Used by

## Notes

- The obstruction is a proof-route obstruction, not a counterexample to \(P_1''\) complete monotonicity or to convexity.
- Future positive-kernel work should group across the integer and reciprocal pole families before any sign certification.
