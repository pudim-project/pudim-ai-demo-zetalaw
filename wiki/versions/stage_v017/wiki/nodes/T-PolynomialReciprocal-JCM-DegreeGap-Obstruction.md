---
id: "T-PolynomialReciprocal-JCM-DegreeGap-Obstruction"
type: "theorem"
title: "Degree-gap obstruction for reciprocal polynomial JCM nets"
status: "proved"
tags: ["Hausdorff-moment", "degree-gap-obstruction", "endpoint-obstruction", "joint-complete-monotonicity", "polynomial-reciprocal", "proved", "theorem", "true"]
parents: ["L-JCM-SliceEndpoint-ConcavityObstruction", "D-Endpoint-obstruction-certificate-language", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private proof note", "private proof note"]
---

# Theorem: Degree-gap obstruction for reciprocal polynomial JCM nets

## Statement

Let \(A,B\) be positive polynomial sequences on \(\mathbb Z_+\) with positive leading coefficients and \(\deg B-\deg A\ge2\). Then the two-parameter net \(\beta_{m,n}=1/(B(m)+A(m)n)\) is not jointly completely monotone.

## Dependencies

- [[wiki/nodes/L-JCM-SliceEndpoint-ConcavityObstruction|Slice endpoint concavity obstruction for reciprocal JCM nets]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private proof note`
- `private proof note`

## Proof

For \(a_0,b_0>0\) and \(0<b_1<a_1<b_2<b_3\), let
\[
\beta_{m,n}
=
\frac{1}{b_0(m+b_1)(m+b_2)(m+b_3)+a_0(m+a_1)n},
\qquad m,n\in\mathbb Z_+.
\]
The target is to prove that this net is not jointly completely monotone, giving a negative answer to Khasnis-Sholapurkar Question 4.6.

Let \(A_m,B_m>0\) and
\[
\beta_{m,n}=\frac{1}{B_m+A_m n}.
\]
Set \(r_m=B_m/A_m\). If \(\{\beta_{m,n}\}\) is jointly completely monotone, then
\[
r_{m+1}-2r_m+r_{m-1}\le 0
\]
for every \(m\ge1\).

Indeed, joint complete monotonicity is equivalent to the Hausdorff representation
\[
\beta_{m,n}=\int_{[0,1]^2} x^m t^n\,d\mu(x,t)
\]
for a positive finite measure \(\mu\). For a Borel set \(E\subset[0,1]\), define
\[
\nu_m(E)=\int_{[0,1]\times E}x^m\,d\mu(x,t).
\]
Cauchy-Schwarz gives the log-convexity inequality
\[
\nu_m(E)^2\le \nu_{m-1}(E)\nu_{m+1}(E).
\]

For fixed \(m\), the \(n\)-slice has the unique Hausdorff representing density
\[
d\nu_m(t)=\phi_m(t)\,dt,\qquad
\phi_m(t)=\frac{1}{A_m}t^{r_m-1},
\]
because
\[
\int_0^1 t^n\phi_m(t)\,dt
=
\frac{1}{A_m(n+r_m)}
=
\frac{1}{B_m+A_mn}.
\]
Taking \(E=(0,\varepsilon)\) gives
\[
\nu_m(E)=\frac{\varepsilon^{r_m}}{A_m r_m}
=
\frac{\varepsilon^{r_m}}{B_m}.
\]
Thus
\[
\left(\frac{\varepsilon^{r_m}}{B_m}\right)^2
\le
\frac{\varepsilon^{r_{m-1}}}{B_{m-1}}
\frac{\varepsilon^{r_{m+1}}}{B_{m+1}},
\]
or
\[
\frac{B_{m-1}B_{m+1}}{B_m^2}
\varepsilon^{-\{r_{m+1}-2r_m+r_{m-1}\}}\le1.
\]
If \(r_{m+1}-2r_m+r_{m-1}>0\), the left side tends to \(+\infty\) as \(\varepsilon\downarrow0\), contradiction. This proves the lemma.

_Proof source: `private proof note`._

## Tags

`Hausdorff-moment`, `degree-gap-obstruction`, `endpoint-obstruction`, `joint-complete-monotonicity`, `polynomial-reciprocal`, `proved`, `theorem`, `true`
