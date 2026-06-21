---
id: "T-Khasnis-Sholapurkar-Q46-NegativeAnswer"
type: "theorem"
title: "Khasnis-Sholapurkar Question 4.6 has a negative answer"
status: "proved"
tags: ["Hausdorff-moment", "application-candidate", "endpoint-obstruction", "joint-complete-monotonicity", "open-problem-solved", "proved", "source-solving", "strict-private-plus10", "theorem", "true"]
parents: ["T-PolynomialReciprocal-JCM-DegreeGap-Obstruction", "L-JCM-SliceEndpoint-ConcavityObstruction", "O-Khasnis-Sholapurkar-Q46-JCM-source-gate"]
refs: ["private proof note", "private proof note"]
---

# Theorem: Khasnis-Sholapurkar Question 4.6 has a negative answer

## Statement

For every \(a_0,b_0>0\) and \(0<b_1<a_1<b_2<b_3\), the net \(\beta_{m,n}=1/[b_0(m+b_1)(m+b_2)(m+b_3)+a_0(m+a_1)n]\) on \(\mathbb Z_+^2\) is not jointly completely monotone. Thus Khasnis-Sholapurkar Question 4.6 is answered negatively.

## Dependencies

- [[wiki/nodes/T-PolynomialReciprocal-JCM-DegreeGap-Obstruction|Degree-gap obstruction for reciprocal polynomial JCM nets]]
- [[wiki/nodes/L-JCM-SliceEndpoint-ConcavityObstruction|Slice endpoint concavity obstruction for reciprocal JCM nets]]
- [[wiki/nodes/O-Khasnis-Sholapurkar-Q46-JCM-source-gate|Khasnis-Sholapurkar Question 4.6 reciprocal polynomial JCM source gate]]

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

`Hausdorff-moment`, `application-candidate`, `endpoint-obstruction`, `joint-complete-monotonicity`, `open-problem-solved`, `proved`, `source-solving`, `strict-private-plus10`, `theorem`, `true`
