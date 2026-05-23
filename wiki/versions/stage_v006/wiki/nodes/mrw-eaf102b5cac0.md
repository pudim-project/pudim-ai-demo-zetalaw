---
id: mrw-eaf102b5cac0
type: proposition
title: Activation-scale bound for threshold-aware Erdos first-hit defects
aliases: ["mrw-eaf102b5cac0", "Activation-scale bound for threshold-aware Erdos first-hit defects"]
status: proved
tags: ["proposition", "proved", "erdos", "logarithmic-density", "modular-residue", "tail-control", "crt", "uniformity", "threshold", "activation-scale"]
parents: [mrw-3d524c92103b, mrw-ba29cdf1fd30, mrw-e0778085804e, mrw-f1348014e087, mrw-e0971c9b820a, mrw-17f44100cb83]
refs: ["references/sources/20260518T213009Z-erdos-activation-scale-context.md"]
---

# Proposition: Activation-scale bound for threshold-aware Erdos first-hit defects

## Statement

Use the notation of [[wiki/nodes/mrw-f1348014e087|Threshold-aware CRT certificate for Erdos first-hit block uniformity]].  For a finite block
\[
I=\{A+1,\ldots,B\},
\]
put
\[
G_I=\bigcup_{i\in I}H_i,\qquad \eta_I=\sum_{i\in I}h_i,\qquad L=L_B,\qquad T=n_B.
\]
Assume \(T\ge2\).  Then the threshold-aware defect \(Q_I\) satisfies
\[
Q_I\le \frac{L_B}{n_B\log n_B}\eta_I.
\]

Consequently, suppose \(0=N_0<N_1<\cdots\) are cutpoints and
\[
I_r=\{N_{r-1}+1,\ldots,N_r\}.
\]
If there are \(C<\infty\) and nonnegative \(\varepsilon_r\) such that
\[
P_{I_r}+\frac{L_{N_r}}{n_{N_r}\log n_{N_r}}\eta_{I_r}
\le
C\eta_{I_r}+\varepsilon_r,
\qquad
\sum_r\varepsilon_r<\infty,
\]
then \(B\) has logarithmic density
\[
\delta=\lim_N\delta_N.
\]

## Proof

For each \(d\in D_I\), the first active representative \(\tau_I(d)\) is defined by
\[
\tau_I(d)\ge T=n_B,\qquad \tau_I(d)\equiv d\pmod L.
\]
Thus if \(x<T\), the sum in the definition of \(Q_I\) is empty.  If \(x\ge T\), then
\[
\sum_{\substack{d\in D_I\\ \tau_I(d)<x}}\frac1{\tau_I(d)}
\le
\frac{|D_I|}{T}.
\]
The eventual CRT support has density \(\eta_I\), so
\[
|D_I|=L\eta_I=L_B\eta_I.
\]
Dividing by \(\log x\ge\log T=\log n_B\) gives
\[
\frac1{\log x}
\sum_{\substack{d\in D_I\\ \tau_I(d)<x}}\frac1{\tau_I(d)}
\le
\frac{L_B\eta_I}{n_B\log n_B}.
\]
Taking the supremum over \(x\ge2\) proves the activation-scale bound for \(Q_I\).

For the block sequence, the hypothesis and the just-proved bound imply
\[
P_{I_r}+Q_{I_r}
\le
C\eta_{I_r}+\varepsilon_r.
\]
The threshold-aware CRT certificate [[wiki/nodes/mrw-f1348014e087|Threshold-aware CRT certificate for Erdos first-hit block uniformity]] then gives
\[
\sup_{x\ge2}\mu_x(G_{I_r})
\le
(C+c_0)\eta_{I_r}+\varepsilon_r.
\]
This is the block-uniform hypothesis in [[wiki/nodes/mrw-e0778085804e|Block-uniform first-hit criterion for Erdos residue-class logarithmic density]].  Hence \(B\) has logarithmic density \(\delta\).

## Depends on

- [[wiki/nodes/mrw-3d524c92103b|Erdos residue-class logarithmic-density problem]]
- [[wiki/nodes/mrw-ba29cdf1fd30|Finite-shadow reduction for Erdos residue-class logarithmic density]]
- [[wiki/nodes/mrw-e0778085804e|Block-uniform first-hit criterion for Erdos residue-class logarithmic density]]
- [[wiki/nodes/mrw-f1348014e087|Threshold-aware CRT certificate for Erdos first-hit block uniformity]]
- [[wiki/nodes/mrw-e0971c9b820a|Small-residue obstruction to unshifted CRT prefix-defect summability]]
- [[wiki/nodes/mrw-17f44100cb83|Tail-continuity obstruction for Erdos residue-class logarithmic density]]

## Used by

- [[wiki/nodes/mrw-7586943cc138|First-cycle entropy bound for threshold-aware Erdos defects]]

## Notes

- This proposition is a sufficient activation-scale subcase, not a complete solution of Erdos Problem #25.
- The key ratio is
\[
\Lambda_I=\frac{L_B}{n_B\log n_B}.
\]
Future progress must either improve this crude activation-scale cost using residue overlap, construct a true actual-mass obstruction, or restart outside the #25 tail-continuity route.
- This does not revive the unshifted \(R_I\) route; it applies only to the threshold-aware defect \(Q_I\).
- The first-cycle entropy bound [[wiki/nodes/mrw-7586943cc138|First-cycle entropy bound for threshold-aware Erdos defects]] improves the support-size-only estimate by replacing the linear ratio with a packed harmonic profile \(\Phi(T,M)\).
