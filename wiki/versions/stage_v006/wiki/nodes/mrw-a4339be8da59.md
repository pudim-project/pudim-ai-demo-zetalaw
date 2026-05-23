---
id: mrw-a4339be8da59
type: proposition
title: Ratio-normal-form reduction for P1 convexity
aliases: ["mrw-a4339be8da59", "Ratio-normal-form reduction for P1 convexity"]
status: proved
tags: ["proposition", "proved", "polygamma", "trigamma", "convexity", "ratio-normal-form", "frontier"]
parents: [mrw-1c9d9f07a4ef, mrw-5a84b7d9f2c1, mrw-f0a031feea8e]
refs: ["references/sources/20260518T142240Z-qiln-open-problem-2-refresh.md", "references/sources/20260518T142240Z-dlmf-polygamma-series.md"]
---

# Proposition: Ratio-normal-form reduction for P1 convexity

## Statement

For \(m\ge1\), put
\[
A_m(x)=(-1)^{m+1}\psi^{(m)}(x),\qquad x>0,
\]
and define the scale-free ratios
\[
U(x)=\frac{xA_2(x)}{A_1(x)},\qquad
V(x)=\frac{xA_3(x)}{A_2(x)}.
\]
Let
\[
P_1(x)=\psi'(x)\psi'(1/x)=A_1(x)A_1(1/x).
\]
Then
\[
P_1''(x)=\frac{A_1(x)A_1(1/x)}{x^2}\Phi(x),
\]
where
\[
\Phi(x)=U(x)V(x)+U(1/x)V(1/x)-2U(1/x)U(x)-2U(1/x).
\]
Consequently the convexity assertion \(P_1''(x)\ge0\) is equivalent to
\[
\Phi(x)\ge0\qquad(x>0).
\]

## Proof

Since \(A_m'(x)=-A_{m+1}(x)\), differentiating
\[
P_1(x)=A_1(x)A_1(1/x)
\]
twice gives
\[
\begin{aligned}
P_1''(x)
=&A_3(x)A_1(1/x)
-2x^{-2}A_2(x)A_2(1/x)\\
&-2x^{-3}A_1(x)A_2(1/x)
+x^{-4}A_1(x)A_3(1/x).
\end{aligned}
\]
Write \(u=U(x)\), \(v=V(x)\), \(\bar u=U(1/x)\), and \(\bar v=V(1/x)\).  The definitions give
\[
A_2(x)=\frac{uA_1(x)}{x},\qquad
A_3(x)=\frac{uvA_1(x)}{x^2},
\]
and, because the reciprocal argument is \(1/x\),
\[
A_2(1/x)=x\bar u A_1(1/x),\qquad
A_3(1/x)=x^2\bar u\bar v A_1(1/x).
\]
Substituting these four identities into the displayed formula for \(P_1''\) yields
\[
P_1''(x)
=\frac{A_1(x)A_1(1/x)}{x^2}
\left(uv+\bar u\bar v-2u\bar u-2\bar u\right),
\]
which is the stated formula.  The prefactor is strictly positive for \(x>0\), so \(P_1''(x)\ge0\) is equivalent to \(\Phi(x)\ge0\).

## Depends on

- [[wiki/nodes/mrw-1c9d9f07a4ef|P1 trigamma product complete-monotonicity frontier]]
- [[wiki/nodes/mrw-5a84b7d9f2c1|Pole-family obstruction for the P1 kernel route]]
- [[wiki/nodes/mrw-f0a031feea8e|Higher-order monotonicity of polygamma products Pn]]

## Used by

- [[wiki/nodes/mrw-58db958e1bf1|Convexity of the reciprocal trigamma product]]

## Notes

- This is a reduction, not a proof of \(P_1''(x)\ge0\) and not a proof of complete monotonicity.
- It packages the required cross-family cancellation into a two-scale ratio inequality involving \(x\) and \(1/x\).  The convexity theorem node uses this reduction to prove \(\Phi(x)>0\).
- The helper `calculations/check_p1_ratio_reduction.py` only checks the algebra numerically on a grid; the proof above is the local proof.
