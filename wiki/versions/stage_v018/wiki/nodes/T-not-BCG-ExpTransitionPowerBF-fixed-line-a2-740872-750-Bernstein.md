---
id: "T-not-BCG-ExpTransitionPowerBF-fixed-line-a2-740872-750-Bernstein"
type: "theorem"
title: "BCG exponential-transition power is not Bernstein on the fixed a2 interval [0.740872,0.75]"
status: "proved"
tags: ["beghin-cristofaro-garrappa", "bernstein-function", "fixed-line-exclusion", "lower-endpoint-refinement", "not-app", "parameter-region-exclusion", "proved", "signed-moment-obstruction", "theorem", "true-negation"]
parents: ["O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold", "T-not-BCG-ExpTransitionPowerBF-fixed-line-a2-741-750-Bernstein", "T-not-BCG-ExpTransitionPowerBF-local-box-Bernstein", "L-BCG-ExpTransitionPowerBF-InverseLaplace-Criterion"]
refs: ["oracle/responses/OS-20260611T1402Z-bcg-fixed-line-refinement-live-oracle-response.md", "raw/oracle/RO-OS-20260611T1402Z-bcg-fixed-line-refinement-live.json", "raw/student/20260611T1425-bcg-fixed-line-lower-endpoint-refinement.md", "theory/nodes/T-not-BCG-ExpTransitionPowerBF-fixed-line-a2-741-750-Bernstein.json"]
---

# Theorem: BCG exponential-transition power is not Bernstein on the fixed a2 interval [0.740872,0.75]

## Statement

For every a2 in [92609/125000,3/4], the function F(s)=s^((2*a2+(3/10)*s)/(s+2)) is not a Bernstein function on (0,infinity).

## Dependencies

- [[wiki/nodes/O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold|Beghin-Cristofaro-Garrappa exponential-transition power Bernstein threshold]]
- [[wiki/nodes/T-not-BCG-ExpTransitionPowerBF-fixed-line-a2-741-750-Bernstein|BCG exponential-transition power is not Bernstein on the fixed a2 interval [0.741,0.75]]]
- [[wiki/nodes/T-not-BCG-ExpTransitionPowerBF-local-box-Bernstein|BCG exponential-transition power is not Bernstein on a local parameter box]]
- [[wiki/nodes/L-BCG-ExpTransitionPowerBF-InverseLaplace-Criterion|BCG exponential-transition power Bernstein inverse-Laplace criterion]]

## Proof and provenance references

- `oracle/responses/OS-20260611T1402Z-bcg-fixed-line-refinement-live-oracle-response.md`
- `raw/oracle/RO-OS-20260611T1402Z-bcg-fixed-line-refinement-live.json`
- `raw/student/20260611T1425-bcg-fixed-line-lower-endpoint-refinement.md`
- `theory/nodes/T-not-BCG-ExpTransitionPowerBF-fixed-line-a2-741-750-Bernstein.json`

## Proof

Let
\[
F_{a_2}(s)=s^{(2a_2+(3/10)s)/(s+2)},\qquad 0<a_2<1.
\]
For every
\[
a_2\in\left[\frac{92609}{125000},\frac34\right],
\]
the function \(F_{a_2}\) is not a Bernstein function on \((0,\infty)\).

For fixed \(x>0\), write
\[
F_{a_2}(x+xz)/F_{a_2}(x)=\sum_{m\ge0}W_m(a_2)z^m.
\]
Equivalently,
\[
W_m(a_2)=\frac{x^mF_{a_2}^{(m)}(x)}{m!\,F_{a_2}(x)}.
\]

For the lower endpoint refinement set \(x=1200\), \(n=4206\), and
\[
\Phi_{a_2}(s)=\frac{3}{10}\log s+2\left(a_2-\frac{3}{10}\right)\frac{\log s}{s+2}.
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

For \(x=1200\), put \(d=1202\), \(q=1200/1202=600/601\), and \(L=\log 1200\). Define
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
Since \(\partial r_k/\partial a_2=2b_k\),
\[
U_0=0,\qquad
mU_m=\sum_{k=1}^{m}k\left(r_k(a_2)U_{m-k}+2b_kW_{m-k}\right).
\]

The recurrence was replayed with outward-rounded Decimal interval arithmetic.

At
\[
a_0=\frac{92609}{125000}=0.740872,
\]
the point replay at precision \(90\) gives
\[
W_{4206}(a_0)\in
[2.54052441742653871732765186728085735951110628858320120196237123136511536674379949365192582\cdot10^{-11},
\]
\[
2.54052441742653871732765186728085735951110628858320120196237123136511536783387980389919163\cdot10^{-11}].
\]
Thus \(W_{4206}(a_0)>0\).

On the full interval
\[
a_2\in[0.740872,0.741],
\]
the derivative replay at precision \(70\) gives
\[
U_{4206}(a_2)\in
[2.413165981903062543427305974596487687848942661126632929505614788509867\cdot10^{-5},
\]
\[
2.505998955674534382275080769819517039471061843872883569350675394135307\cdot10^{-5}].
\]
Thus \(U_{4206}>0\) on \([0.740872,0.741]\), so \(W_{4206}\) is strictly increasing there. Therefore
\[
W_{4206}(a_2)>0
\qquad
(0.740872\le a_2\le0.741).
\]

Since \(4206\) is even, the Bernstein derivative sign condition would require
\[
(-1)^{4205}W_{4206}(a_2)=-W_{4206}(a_2)\ge0.
\]
The strict positivity of \(W_{4206}\) contradicts this. Hence \(F_{a_2}\) is not Bernstein for every
\[
a_2\in[0.740872,0.741].
\]

The already the corresponding theorem the corresponding result proves that \(F_{a_2}\) is not Bernstein for every
\[
a_2\in[0.741,0.75].
\]
Combining the lower sliver \([0.740872,0.741]\) with that admitted interval gives
\[
a_2\in[0.740872,0.75]
\quad\Longrightarrow\quad
F_{a_2}\text{ is not Bernstein}.
\]

This improves the fixed-line lower endpoint from \(0.741\) to \(0.740872\). It does not certify the raw root \(0.740870966957\), does not extend the upper endpoint beyond \(3/4\), does not thicken in \((a_1,c)\), and does not solve the full BCG threshold problem.

_Proof source: `raw/student/20260611T1425-bcg-fixed-line-lower-endpoint-refinement.md`._

## Do not claim

- Do not claim the full BCG Bernstein threshold is solved.
- Do not claim APP status.
- Do not claim relaxation nonnegativity or monotonicity failure from this Bernstein obstruction alone.
- Do not extend below 92609/125000 or above 3/4 without a separate certificate.

## Tags

`beghin-cristofaro-garrappa`, `bernstein-function`, `fixed-line-exclusion`, `lower-endpoint-refinement`, `not-app`, `parameter-region-exclusion`, `proved`, `signed-moment-obstruction`, `theorem`, `true-negation`
