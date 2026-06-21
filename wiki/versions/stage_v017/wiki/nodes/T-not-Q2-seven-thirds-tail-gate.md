---
id: "T-not-Q2-seven-thirds-tail-gate"
type: "theorem"
title: "exists x in (0,1) with Z3(1/x) <= x^(7/3)"
status: "proved"
tags: ["proved", "refutation", "student", "tail-gate", "theorem"]
parents: ["T-endpoint-log-derivative-monotonicity-principle"]
refs: ["private proof note", "wiki/notes/frontier-q2-endpoint.md"]
---

# Theorem: exists x in (0,1) with Z3(1/x) <= x^(7/3)

## Statement

not(For all \(0<x<1\), \(Z_3(1/x)>x^{7/3}\).)

## Dependencies

- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]

## Proof and provenance references

- `private proof note`
- `wiki/notes/frontier-q2-endpoint.md`

## Proof

the Q2 seven thirds tail gate asserted
\[
Z_3(1/x)>x^{7/3}\qquad(0<x<1),
\]
which would imply \(L_2\le7/3<397/170\).

Set
\[
y=\frac{17}{24},
\qquad
x=y^3,
\qquad
a=\frac1x=\left(\frac{24}{17}\right)^3.
\]
Then \(x^{7/3}=y^7\).

For \(f(t)=(a+t)^{-3}\), \(f\) is positive and decreasing. Therefore
\[
\sum_{k=50}^{\infty}(a+k)^{-3}
<
\int_{49}^{\infty}(a+t)^{-3}\,dt
=
\frac{1}{2(a+49)^2}.
\]
Hence
\[
Z_3(a)
<
\sum_{k=0}^{49}(a+k)^{-3}
+
\frac{1}{2(a+49)^2}.
\]

Exact rational arithmetic gives
\[
\left(\frac{17}{24}\right)^7
-
\left[
\sum_{k=0}^{49}(a+k)^{-3}
+
\frac{1}{2(a+49)^2}
\right]
>0.
\]
Numerically, this exact positive rational is approximately
\[
2.7883985511\cdot10^{-5}.
\]
Thus
\[
Z_3(1/x)=Z_3(a)<x^{7/3},
\]
so the universal \(7/3\) tail-gate statement is false.

the Q2 critical sign certificate and the Q2 interval derivative certificate remain open. The refutation increases the value of the derivative-sign route because the simplest \(7/3\) threshold is already too aggressive for the tail-gate inequality itself.

_Proof source: `private proof note`._

## Tags

`proved`, `refutation`, `student`, `tail-gate`, `theorem`
