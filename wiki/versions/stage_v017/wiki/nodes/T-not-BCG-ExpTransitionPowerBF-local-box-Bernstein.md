---
id: "T-not-BCG-ExpTransitionPowerBF-local-box-Bernstein"
type: "theorem"
title: "BCG exponential-transition power is not Bernstein on a local parameter box"
status: "proved"
tags: ["beghin-cristofaro-garrappa", "bernstein-function", "moving-point-certificate", "not-app", "parameter-region-exclusion", "proved", "scarpi-derivative", "signed-moment-obstruction", "theorem", "true-negation"]
parents: ["O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold", "T-not-BCG-ExpTransitionPowerBF-a2-741-Bernstein", "L-BCG-ExpTransitionPowerBF-InverseLaplace-Criterion"]
refs: ["private Oracle response", "private Oracle audit", "private proof note"]
---

# Theorem: BCG exponential-transition power is not Bernstein on a local parameter box

## Statement

For every (a1,c,a2) in [0.299999999,0.300000001] x [1.999999999,2.000000001] x [0.740999999,0.741000001], the function F(s)=s^((a2*c+a1*s)/(c+s)) is not a Bernstein function on (0,infinity).

## Dependencies

- [[wiki/nodes/O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold|Beghin-Cristofaro-Garrappa exponential-transition power Bernstein threshold]]
- [[wiki/nodes/T-not-BCG-ExpTransitionPowerBF-a2-741-Bernstein|BCG exponential-transition power is not Bernstein at a2=741/1000]]
- [[wiki/nodes/L-BCG-ExpTransitionPowerBF-InverseLaplace-Criterion|BCG exponential-transition power Bernstein inverse-Laplace criterion]]

## Proof and provenance references

- `private Oracle response`
- `private Oracle audit`
- `private proof note`

## Proof

Let
\[
F_{a_1,a_2,c}(s)=s^{(a_2c+a_1s)/(c+s)}.
\]
For every
\[
(a_1,c,a_2)\in
[0.299999999,0.300000001]
\times
[1.999999999,2.000000001]
\times
[0.740999999,0.741000001],
\]
the function \(F_{a_1,a_2,c}\) is not a Bernstein function on \((0,\infty)\).

Set
\[
x=700,\qquad m=2475.
\]
Write
\[
F(s)=e^{\Phi(s)},\qquad
\Phi(s)=a_1\log s+c(a_2-a_1)\frac{\log s}{c+s}.
\]
Define
\[
W_m=x^m\frac{F^{(m)}(x)}{m!\,F(x)}.
\]
Equivalently, \(W_m\) is the coefficient of \(z^m\) in
\[
\exp(\Phi(x+xz)-\Phi(x)).
\]

Let
\[
B=x+c,\qquad \rho=\frac{B}{x},\qquad L=\log x.
\]
If
\[
\Phi(x+xz)-\Phi(x)=\sum_{k\ge1}u_k z^k,
\]
then the scaled coefficients are
\[
u_k=(-1)^{k+1}\frac{a_1}{k}
+c(a_2-a_1)(-1)^k
\frac{\rho^{-k}}{B}
\left(
L-\sum_{r=1}^k\frac{\rho^r}{r}
\right).
\]
The exponential-coefficient recurrence is
\[
W_0=1,\qquad
mW_m=\sum_{k=1}^{m}k\,u_k\,W_{m-k}.
\]

This recurrence uses only arithmetic operations and the single constant \(\log 700\).

The recurrence was replayed with directed Decimal interval arithmetic at precision \(90\), over the full box
\[
\mathcal B=
[0.299999999,0.300000001]
\times
[1.999999999,2.000000001]
\times
[0.740999999,0.741000001].
\]
The logarithm was enclosed by
\[
\log 700\in
[6.5510803350434046731413356528119081448392877068394071405260459518727250821067742282596529087670681236,
\]
\[
6.5510803350434046731413356528119081448392877068394071405260459518727250821067742282596529087670681238].
\]

The replay produced
\[
W_{2475}(\mathcal B)
\subset
[-1.11493543651793047277262978299874241295522663498473525098280823520355408543192296633939394\cdot 10^{-10},
\]
\[
-2.31116490851197873562173862380566778717653494524682697434527599060558898602130724808080808\cdot 10^{-11}].
\]
In particular \(W_{2475}<0\) throughout the box.

Since \(2474\) is even,
\[
(-1)^{2474}\frac{F^{(2475)}(700)}{F(700)}
=\frac{2475!}{700^{2475}}W_{2475}.
\]
The prefactor is positive. Therefore the strict negativity of \(W_{2475}\) throughout \(\mathcal B\) gives
\[
(-1)^{2474}F^{(2475)}(700)<0
\]
throughout \(\mathcal B\).

If \(F\) were Bernstein, then \(F'\) would be completely monotone, so
\[
(-1)^nF^{(n+1)}(s)\ge0
\qquad(n\ge0,\ s>0).
\]
Taking \(n=2474\) and \(s=700\) gives a contradiction. Hence \(F\) is not Bernstein anywhere in the box.

By the admitted inverse-Laplace criterion, \(F\) is Bernstein if and only if \(K=\mathcal L^{-1}[F']\) is a nonnegative measure. The negative value of
\[
(-1)^{2474}F^{(2475)}(700)
\]
is equivalently a negative signed moment
\[
\int_0^\infty t^{2474}e^{-700t}\,K(dt)<0,
\]
so \(K\) cannot be nonnegative.

This is a genuine parameter-region exclusion, but it is a very small local box. It does not classify the full BCG Bernstein region and does not imply any statement about the broader relaxation nonnegativity/monotonicity question.

_Proof source: `private proof note`._

## Do not claim

- Do not claim the full BCG Bernstein threshold is solved.
- Do not claim APP status.
- Do not claim the relaxation solution is negative or nonmonotone from this Bernstein obstruction alone.

## Tags

`beghin-cristofaro-garrappa`, `bernstein-function`, `moving-point-certificate`, `not-app`, `parameter-region-exclusion`, `proved`, `scarpi-derivative`, `signed-moment-obstruction`, `theorem`, `true-negation`
