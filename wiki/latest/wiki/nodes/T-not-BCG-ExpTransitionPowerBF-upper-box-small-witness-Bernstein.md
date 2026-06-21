---
id: "T-not-BCG-ExpTransitionPowerBF-upper-box-small-witness-Bernstein"
type: "theorem"
title: "BCG exponential-transition power is not Bernstein on a meaningful upper three-parameter box"
status: "proved"
tags: ["beghin-cristofaro-garrappa", "bernstein-function", "bernstein-polynomial-certificate", "meaningful-thickening", "not-app", "parameter-region-exclusion", "proved", "small-witness-cover", "theorem", "three-parameter-box", "true-negation"]
parents: ["O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold", "T-not-BCG-ExpTransitionPowerBF-fixed-line-a2-740872-to-one-Bernstein", "T-BCG-ExpTransitionPowerBF-finite-signed-moment-recurrence", "L-BCG-ExpTransitionPowerBF-InverseLaplace-Criterion"]
refs: ["private Oracle response", "private Oracle audit", "private proof note"]
---

# Theorem: BCG exponential-transition power is not Bernstein on a meaningful upper three-parameter box

## Statement

For every a1 in [59999/200000,60001/200000], c in [39999/20000,40001/20000], and a2 in [3/4,1), the function F(s)=s^((a2*c+a1*s)/(c+s)) is not a Bernstein function on (0,infinity).

## Dependencies

- [[wiki/nodes/O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold|Beghin-Cristofaro-Garrappa exponential-transition power Bernstein threshold]]
- [[wiki/nodes/T-not-BCG-ExpTransitionPowerBF-fixed-line-a2-740872-to-one-Bernstein|BCG exponential-transition power is not Bernstein on the fixed a2 interval [0.740872,1)]]
- [[wiki/nodes/T-BCG-ExpTransitionPowerBF-finite-signed-moment-recurrence|BCG finite signed-moment recurrence]]
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
a_1\in\left[\frac{59999}{200000},\frac{60001}{200000}\right],
\qquad
c\in\left[\frac{39999}{20000},\frac{40001}{20000}\right],
\qquad
a_2\in\left[\frac34,1\right),
\]
the function \(F_{a_1,a_2,c}\) is not a Bernstein function on \((0,\infty)\).

This box has transverse half-widths \(1/200000=5\cdot10^{-6}\) in \(a_1\) and \(1/20000=5\cdot10^{-5}\) in \(c\), and macroscopic \(a_2\)-width. It is materially larger than the previous local \(2\cdot10^{-9}\)-scale box around \(a_2=0.741\).

For fixed \(x>0\), define
\[
W_m(x;a_1,a_2,c)
=
\frac{x^mF_{a_1,a_2,c}^{(m)}(x)}{m!\,F_{a_1,a_2,c}(x)}.
\]
If \(F_{a_1,a_2,c}\) is Bernstein, then \(F'_{a_1,a_2,c}\) is completely monotone, so
\[
(-1)^{m-1}W_m(x;a_1,a_2,c)\ge0.
\]
For odd \(m\), a certified inequality \(W_m(x;a_1,a_2,c)<0\) is therefore a Bernstein obstruction.

Write
\[
\phi(s)=\log F_{a_1,a_2,c}(s)
=a_1\log s+c(a_2-a_1)\frac{\log s}{s+c}.
\]
For fixed rational \(x\), write
\[
\phi(x+xz)-\phi(x)=\sum_{j\ge1}r_j z^j,
\qquad
\frac{F(x+xz)}{F(x)}=\sum_{m\ge0}W_m z^m.
\]
Then
\[
W_0=1,\qquad
mW_m=\sum_{j=1}^m j\,r_jW_{m-j}.
\]

Let \(L(z)=\log(x+xz)\), and let \(\ell_0=\log x\), \(\ell_j=(-1)^{j+1}/j\) for \(j\ge1\). If
\[
\frac{L(z)}{x+xz+c}=\sum_{j\ge0}h_jz^j,
\]
then
\[
(x+c)h_0=\ell_0,\qquad
(x+c)h_j+xh_{j-1}=\ell_j\quad(j\ge1).
\]
Thus, for \(j\ge1\),
\[
r_j=a_1\ell_j+c(a_2-a_1)h_j
=\bigl(a_1\ell_j-ca_1h_j\bigr)+(ch_j)a_2.
\]
For fixed interval boxes in \((a_1,c)\), the recurrence therefore gives a polynomial in \(a_2\) with interval coefficients.

For the witness \((m,x)=(107,30)\), the polynomial \(W_{107}(30;a_1,a_2,c)\) was computed by the recurrence above with directed Decimal interval arithmetic at precision \(90\), using outward-rounded enclosures for \(\log 30\), over
\[
a_1\in\left[\frac{59999}{200000},\frac{60001}{200000}\right],
\qquad
c\in\left[\frac{39999}{20000},\frac{40001}{20000}\right].
\]
After the affine change
\[
a_2=\frac34+\frac1{100}t,\qquad 0\le t\le1,
\]
the interval-coefficient polynomial was converted to Bernstein form of degree \(107\). Every Bernstein coefficient has strictly negative upper bound. The largest upper bound was
\[
-2.54948544798543456781183787385736585412108741834464033207650798840055018046908670173111573\cdot10^{-7}.
\]
The smallest lower bound was
\[
-4.80131767449088858189322578902062571032814899369145428404501664471848360679871486923420912\cdot10^{-5}.
\]
Therefore
\[
W_{107}(30;a_1,a_2,c)<0
\]
throughout the box with \(a_2\in[3/4,19/25]\).

For the witness \((m,x)=(37,10)\), the polynomial \(W_{37}(10;a_1,a_2,c)\) was computed with the same interval-coefficient recurrence, using an outward-rounded enclosure for \(\log 10\), over the same \((a_1,c)\)-box.

After the affine change
\[
a_2=\frac{19}{25}+\frac6{25}t,\qquad 0\le t\le1,
\]
the interval-coefficient polynomial was converted to Bernstein form of degree \(37\). Every Bernstein coefficient has strictly negative upper bound. The largest upper bound was
\[
-1.86535039316846694521092263023474131642172073278317850257588831502946941530214469372324102\cdot10^{-5}.
\]
The smallest lower bound was
\[
-2.42739203035529308805409556618113050348159211862138758089298546812275238386227945874859575\cdot10^{-3}.
\]
Therefore
\[
W_{37}(10;a_1,a_2,c)<0
\]
throughout the box with \(a_2\in[19/25,1]\).

Restricting to the source parameter range \(a_2<1\), the two certificates cover \(a_2\in[3/4,1)\).

\emph{Conclusion.}
The two odd-order witnesses give a Bernstein obstruction throughout
\[
\left[\frac{59999}{200000},\frac{60001}{200000}\right]
\times
\left[\frac34,1\right)
\times
\left[\frac{39999}{20000},\frac{40001}{20000}\right],
\]
where the middle coordinate is \(a_2\). Hence \(F_{a_1,a_2,c}\) is not Bernstein throughout this three-parameter box.

This is a meaningful local three-parameter exclusion away from the lower endpoint. It does not solve the full BCG threshold, does not claim APP status, and does not imply failure of the broader fractional-relaxation nonnegativity or monotonicity property.

_Proof source: `private proof note`._

## Do not claim

- Do not claim the full BCG Bernstein threshold is solved.
- Do not claim APP status.
- Do not claim relaxation nonnegativity or monotonicity failure from this Bernstein obstruction alone.
- Do not extend below a2=3/4 or outside the stated a1,c box without a separate certificate.

## Tags

`beghin-cristofaro-garrappa`, `bernstein-function`, `bernstein-polynomial-certificate`, `meaningful-thickening`, `not-app`, `parameter-region-exclusion`, `proved`, `small-witness-cover`, `theorem`, `three-parameter-box`, `true-negation`
