---
id: mrw-1c9d9f07a4ef
type: note
title: P1 trigamma product complete-monotonicity frontier
aliases: ["mrw-1c9d9f07a4ef", "P1 trigamma product complete-monotonicity frontier"]
status: partial
tags: ["note", "partial", "polygamma", "trigamma", "complete-monotonicity", "non-tail", "frontier"]
parents: [mrw-f0a031feea8e, mrw-dee642b8e9cb]
refs: []
refs: []
---

# Note: P1 trigamma product complete-monotonicity frontier

## Statement

Let
\[
P_1(x)=\psi'(x)\psi'(1/x),\qquad x>0.
\]
The complete monotonicity of \(P_1''\) remains open after this cycle.  The cycle established an exact derivative recurrence for audit work and found no numerical sign obstruction through order \(35\) on the grid
\[
x\in\{0.05,0.1,0.2,0.5,1,2,5,10,20\}.
\]
This is evidence only, not a proof.

## Exact Normal Form

For \(m\ge1\), set
\[
A_m(x)=(-1)^{m+1}\psi^{(m)}(x)
=m!\sum_{k=0}^{\infty}(x+k)^{-m-1}.
\]
Then \(A_m'(x)=-A_{m+1}(x)\) and \(P_1(x)=A_1(x)A_1(1/x)\).  Direct differentiation gives
\[
\begin{aligned}
P_1''(x)=&
A_3(x)A_1(1/x)
-\frac{2}{x^2}A_2(x)A_2(1/x)\\
&-\frac{2}{x^3}A_1(x)A_2(1/x)
+\frac{1}{x^4}A_1(x)A_3(1/x).
\end{aligned}
\]

For higher derivatives define
\[
T_{p,i,j}(x)=x^{-p}A_i(x)A_j(1/x).
\]
The exact recurrence
\[
\frac{d}{dx}T_{p,i,j}(x)
=-pT_{p+1,i,j}(x)-T_{p,i+1,j}(x)+T_{p+2,i,j+1}(x)
\]
generates \((P_1'')^{(r)}\) as a finite linear combination of \(T_{p,i,j}\) for every \(r\ge0\).

## Audit Evidence

The script `calculations/check_p1_trigamma_cm.ps1` uses the recurrence above and floating-point series evaluation.  With `-MaxOrder 35`, no sampled value violated
\[
(-1)^r(P_1'')^{(r)}(x)\ge0
\]
on the grid listed above.  At \(x=2\), the first alternating values for \(r=0,\ldots,8\) were approximately
\[
0.25008,\ 0.35441,\ 0.69467,\ 1.73623,\ 5.25492,\ 18.6111,\ 75.3247,\ 342.484,\ 1727.04.
\]

## Failed Proof Routes

- Same-point Turan inequalities for \(A_m(x)\) give useful lower bounds such as \(A_1(x)A_3(x)\ge\frac32A_2(x)^2\), but the reciprocal chain-rule term \(-2x^{-3}A_1(x)A_2(1/x)\) is not absorbed by that bound alone.
- A termwise rational Laplace-kernel decomposition of
  \[
  \left(\frac{x}{(x+m)(1+\ell x)}\right)^2
  \]
  gives mixed \(t^2e^{-at}\) and \(t^3e^{-at}\) coefficients.  The signs may still cancel globally, but this cycle did not find a positive grouping.
- The previous high-order counterexample method does not transfer: the \(p=2\) dominant-summand numerics are positive in the tested orders instead of exposing an alternating-sign failure.

## 2026-05-18 Order-80 Audit Update

The follow-up sprint `20260518T110932Z-research-only-p1-kernel-or-counterexample-sprint` ran the same floating-point recurrence checker to order \(80\).  It reported apparent high-order failures, with first reported failures including \(x=20,r=37\), \(x=10,r=42\), and \(x=2,r=49\).  These are not accepted as counterexamples.

The reason is exactness, not optimism: the calculation is a double-precision evaluation of large signed finite \(T_{p,i,j}\) sums, so the high-order regime is cancellation-sensitive.  The double-series model
\[
P_1(x)=\sum_{m,n\ge0}\left(\frac{x}{(x+m)(1+nx)}\right)^2
\]
also gives a pole-principal sanity check warning against trusting these signs without interval arithmetic.  For example,
\[
\left(\frac{x}{(x+1)^2}\right)^2=\frac{x^2}{(x+1)^4}
\]
has positive alternating high derivatives once the total derivative order is at least \(11\).  A valid counterexample therefore requires an exact rational interval certificate for the finite \(T_{p,i,j}\) expression at a rational point.

## 2026-05-18 Dyadic Interval Certificate Attempt

The sprint `20260518T120047Z-p1-exact-interval-sprint` added `.math-wiki/calculations/certify_p1_interval.ps1`.  The helper builds the exact integer \(T_{p,i,j}\) recurrence coefficients and encloses each \(A_m(q)\) at rational \(q\) by outward-rounded dyadic rational intervals from finite sums plus monotone integral tails.

The helper did not certify any of the previous floating failures.  Representative rigorous enclosures still straddled zero:

- \(x=20,r=37,N=1000\), 32768 dyadic bits: approximately \([-4.20\cdot10^4,4.20\cdot10^4]\).
- \(x=5,r=43,N=1000\), 32768 dyadic bits: approximately \([-2.21\cdot10^{34},2.21\cdot10^{34}]\).
- \(x=2,r=49,N=1000\), 32768 dyadic bits: approximately \([-4.18\cdot10^{61},4.18\cdot10^{61}]\).
- \(x=1,r=46,N=1000\), 32768 dyadic bits: approximately \([-2.23\cdot10^{70},2.23\cdot10^{70}]\).

This is a route obstruction rather than a sign result.  The direct \(A_m\)-product interval method bounds after severe cancellation has already appeared.  A future certificate should split the double series or pole families before interval bounding, or else find a positive kernel grouping.

## 2026-05-18 Pole-Family Obstruction

The sprint `20260518T125130Z-p1-pole-family-sprint` tested the natural next architecture: decompose the double-series atoms
\[
F_{m,n}(x)=\frac{x^2}{(x+m)^2(1+nx)^2}
\]
into partial fractions at the integer poles \(-m\) and reciprocal poles \(-1/n\), then inspect the inverse-Laplace density for \(P_1''\).

This produced a proved route obstruction, promoted as [[wiki/nodes/mrw-5a84b7d9f2c1|Pole-family obstruction for the P1 kernel route]]: in the canonical decomposition, every integer-pole family \(e^{-mt}\) with \(m\ge3\) is negative for sufficiently small \(t>0\), and every reciprocal-pole family \(e^{-t/n}\) with \(n\ge2\) is negative for sufficiently small \(t>0\).

This is not a counterexample to complete monotonicity or convexity.  It says only that separate pole-family positivity is impossible.  Future kernel work must group across pole families or renormalize before sign certification.

## 2026-05-18 Ratio Normal Form Reduction And Convexity Theorem

The sprint `20260518T142240Z-build-a-cross-family-cancellation-or-renormalized-laplace-ke` promoted [[wiki/nodes/mrw-a4339be8da59|Ratio-normal-form reduction for P1 convexity]].  With
\[
U(x)=\frac{xA_2(x)}{A_1(x)},\qquad V(x)=\frac{xA_3(x)}{A_2(x)},
\]
it proves that
\[
P_1''(x)=\frac{A_1(x)A_1(1/x)}{x^2}
\left[
U(x)V(x)+U(1/x)V(1/x)-2U(x)U(1/x)-2U(1/x)
\right].
\]
The same sprint then promoted [[wiki/nodes/mrw-58db958e1bf1|Convexity of the reciprocal trigamma product]], proving the bracket is strictly positive and hence \(P_1''(x)>0\) for all \(x>0\).  Complete monotonicity of \(P_1''\) remains open.

## Depends on

- [[wiki/nodes/mrw-f0a031feea8e|Higher-order monotonicity of polygamma products Pn]]
- [[wiki/nodes/mrw-dee642b8e9cb|Counterexample to complete monotonicity of higher-order polygamma product curvature]]

## Used by

- [[wiki/nodes/mrw-5a84b7d9f2c1|Pole-family obstruction for the P1 kernel route]]
- [[wiki/nodes/mrw-a4339be8da59|Ratio-normal-form reduction for P1 convexity]]
- [[wiki/nodes/mrw-58db958e1bf1|Convexity of the reciprocal trigamma product]]

## Notes

- This node is intentionally partial for complete monotonicity.  For convexity of \(P_1\), cite [[wiki/nodes/mrw-58db958e1bf1|Convexity of the reciprocal trigamma product]].
- Next proof route: construct a globally nonnegative Laplace kernel for \(P_1''\) using cross-family cancellation or renormalization, or produce an exact complete-monotonicity counterexample certificate.  Floating-point failures from the order-80 screen remain advisory only.
