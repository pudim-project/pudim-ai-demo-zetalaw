---
id: "T-not-BCG-ExpTransitionPowerBF-fixed-line-a2-741-750-Bernstein"
type: "theorem"
title: "BCG exponential-transition power is not Bernstein on the fixed a2 interval [0.741,0.75]"
status: "proved"
tags: ["a2-monotonicity", "beghin-cristofaro-garrappa", "bernstein-function", "fixed-line-exclusion", "not-app", "parameter-region-exclusion", "proved", "signed-moment-obstruction", "theorem", "true-negation"]
parents: ["O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold", "T-not-BCG-ExpTransitionPowerBF-local-box-Bernstein", "T-not-BCG-ExpTransitionPowerBF-a2-741-Bernstein", "L-BCG-ExpTransitionPowerBF-InverseLaplace-Criterion"]
refs: ["private Oracle response", "private Oracle audit", "private proof note"]
---

# Theorem: BCG exponential-transition power is not Bernstein on the fixed a2 interval [0.741,0.75]

## Statement

For every a2 in [741/1000,3/4], the function F(s)=s^((2*a2+(3/10)*s)/(s+2)) is not a Bernstein function on (0,infinity).

## Dependencies

- [[wiki/nodes/O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold|Beghin-Cristofaro-Garrappa exponential-transition power Bernstein threshold]]
- [[wiki/nodes/T-not-BCG-ExpTransitionPowerBF-local-box-Bernstein|BCG exponential-transition power is not Bernstein on a local parameter box]]
- [[wiki/nodes/T-not-BCG-ExpTransitionPowerBF-a2-741-Bernstein|BCG exponential-transition power is not Bernstein at a2=741/1000]]
- [[wiki/nodes/L-BCG-ExpTransitionPowerBF-InverseLaplace-Criterion|BCG exponential-transition power Bernstein inverse-Laplace criterion]]

## Proof and provenance references

- `private Oracle response`
- `private Oracle audit`
- `private proof note`

## Proof

Let
\[
F_{a_2}(s)=s^{(2a_2+(3/10)s)/(s+2)},\qquad 0<a_2<1.
\]
For every
\[
a_2\in\left[\frac{741}{1000},\frac34\right],
\]
the function \(F_{a_2}\) is not a Bernstein function on \((0,\infty)\).

Set \(x=700\), \(n=2475\), and write
\[
F_{a_2}(s)=e^{\Phi_{a_2}(s)},\qquad
\Phi_{a_2}(s)=\frac{3}{10}\log s+2\left(a_2-\frac{3}{10}\right)\frac{\log s}{s+2}.
\]
Define
\[
W_n(a_2)=\frac{x^nF_{a_2}^{(n)}(x)}{n!\,F_{a_2}(x)}.
\]
Then \(W_n(a_2)\) is the coefficient of \(z^n\) in
\[
\exp(\Phi_{a_2}(x+xz)-\Phi_{a_2}(x)).
\]

If
\[
\Phi_{a_2}(x+xz)-\Phi_{a_2}(x)=\sum_{k\ge1}r_k(a_2)z^k,
\]
then
\[
W_0=1,\qquad
mW_m=\sum_{k=1}^{m}k\,r_k(a_2)W_{m-k}.
\]

For \(x=700\), put \(d=702\), \(q=700/702=350/351\), and \(L=\log 700\).  Define
\[
A_0=L,\qquad A_k=-qA_{k-1}+\frac{(-1)^{k+1}}{k},
\qquad b_k=\frac{A_k}{d}.
\]
Then
\[
r_k(a_2)=\frac{3}{10}\frac{(-1)^{k+1}}{k}
+2\left(a_2-\frac{3}{10}\right)b_k.
\]

Let
\[
U_m(a_2)=\frac{\partial W_m(a_2)}{\partial a_2}.
\]
Since \(\partial r_k/\partial a_2=2b_k\), differentiating the coefficient recurrence gives
\[
U_0=0,
\]
and
\[
mU_m=\sum_{k=1}^{m}k\left(r_k(a_2)U_{m-k}+2b_kW_{m-k}\right).
\]

Thus \(U_{2475}<0\) on an interval implies \(W_{2475}\) is strictly decreasing there.

The recurrence for \(W_m\) and \(U_m\) was replayed with outward-rounded Decimal interval arithmetic, using precision \(60\) for the \(U\)-interval pass and a widened enclosure of \(\log 700\).

At the left endpoint,
\[
W_{2475}\left(\frac{741}{1000}\right)
\in
[-9.482685452985268354718896772331074388461119406946814693006913438383838\cdot10^{-11},
\]
\[
-4.026169900639782922928902547344167180370702403556281896801563692929293\cdot10^{-11}]
\]
from the stricter replay on \([0.741,0.74100001]\). In particular \(W_{2475}(741/1000)<0\).

The first derivative interval on
\[
a_2\in[0.741,0.745]
\]
was
\[
U_{2475}
\in
[-7.26841650202405141863817331045857360520837982673381677582788\cdot10^{-5},
\]
\[
-2.43270980887253051508881584764709888808854863713566161534626\cdot10^{-5}].
\]

The first derivative interval on
\[
a_2\in[0.745,0.75]
\]
was
\[
U_{2475}
\in
[-7.929413718005318183809705441714264524379937692591864444\cdot10^{-5},
\]
\[
-1.853488409661718699519451522498577986872152677301133657\cdot10^{-5}].
\]

Therefore \(U_{2475}(a_2)<0\) throughout \([0.741,0.75]\), and \(W_{2475}\) is strictly decreasing on that interval. Since \(W_{2475}(0.741)<0\), it follows that
\[
W_{2475}(a_2)<0
\qquad
\left(0.741\le a_2\le0.75\right).
\]

Here \(2474\) is even, and
\[
(-1)^{2474}\frac{F_{a_2}^{(2475)}(700)}{F_{a_2}(700)}
=
\frac{2475!}{700^{2475}}W_{2475}(a_2).
\]
The prefactor is positive, so \(W_{2475}(a_2)<0\) gives
\[
(-1)^{2474}F_{a_2}^{(2475)}(700)<0.
\]

If \(F_{a_2}\) were Bernstein, \(F_{a_2}'\) would be completely monotone, and hence
\[
(-1)^mF_{a_2}^{(m+1)}(s)\ge0
\qquad(m\ge0,\ s>0).
\]
Taking \(m=2474\) and \(s=700\) gives a contradiction.

Thus \(F_{a_2}\) is not Bernstein for every \(a_2\in[741/1000,3/4]\).

This improves the prior local \(a_2\)-width \(2\cdot10^{-9}\) around \(0.741\) to the fixed-line interval \([0.741,0.75]\) at \((a_1,c)=(3/10,2)\). It does not solve the full BCG threshold problem and does not imply failure of the broader fractional-relaxation nonnegativity or monotonicity property.

_Proof source: `private proof note`._

## Do not claim

- Do not claim the full BCG Bernstein threshold is solved.
- Do not claim APP status.
- Do not claim relaxation nonnegativity or monotonicity failure from this Bernstein obstruction alone.
- Do not extend the fixed-line interval below 741/1000 or above 3/4 without a separate certificate.

## Tags

`a2-monotonicity`, `beghin-cristofaro-garrappa`, `bernstein-function`, `fixed-line-exclusion`, `not-app`, `parameter-region-exclusion`, `proved`, `signed-moment-obstruction`, `theorem`, `true-negation`
