---
id: mrw-2945dff32e3e
type: proposition
title: CRT prefix-dispersion certificate for Erdos first-hit block uniformity
aliases: ["mrw-2945dff32e3e", "CRT prefix-dispersion certificate for Erdos first-hit block uniformity"]
status: proved
tags: ["proposition", "proved", "erdos", "logarithmic-density", "modular-residue", "tail-control", "crt", "uniformity", "sieve"]
parents: [mrw-3d524c92103b, mrw-ba29cdf1fd30, mrw-e0778085804e, mrw-536639208ce1, mrw-17f44100cb83]
refs: ["references/sources/20260518T185221Z-davenport-erdos-elementary-proof.md"]
---

# Proposition: CRT prefix-dispersion certificate for Erdos first-hit block uniformity

## Statement

Use the notation of [[wiki/nodes/mrw-e0778085804e|Block-uniform first-hit criterion for Erdos residue-class logarithmic density]].  For a finite block
\[
I=\{A+1,\ldots,B\},
\]
put
\[
G_I=\bigcup_{i\in I}H_i,\qquad
\eta_I=\sum_{i\in I}h_i,\qquad
L=L_B,\qquad T=n_B.
\]
For \(m\ge T\), the set \(G_I\) is periodic modulo \(L\).  Let
\[
D_I\subseteq\{1,\ldots,L\}
\]
be its eventual CRT support, with the residue \(0\pmod L\) represented by \(L\).  Thus
\[
\frac{|D_I|}{L}=\eta_I.
\]
Define the threshold-prefix concentration
\[
P_I=
\sup_{2\le x<T}\mu_x(G_I),
\]
with \(P_I=0\) when \(T\le2\), and the CRT prefix-dispersion constant
\[
R_I=
\sup_{2\le y\le L+1}
\frac{1}{\log y}
\sum_{\substack{d\in D_I\\d<y}}\frac1d.
\]
Then, with the absolute constant
\[
c_0=1+\frac1{\log 2},
\]
one has
\[
\sup_{x\ge2}\mu_x(G_I)\le P_I+R_I+c_0\eta_I.
\]

Consequently, if there are cutpoints \(0=N_0<N_1<\cdots\) for which the corresponding blocks satisfy
\[
P_{I_r}+R_{I_r}\le C\eta_{I_r}+\varepsilon_r,
\qquad
I_r=\{N_{r-1}+1,\ldots,N_r\},
\]
with \(C<\infty\), \(\varepsilon_r\ge0\), and
\[
\sum_{r=1}^{\infty}\varepsilon_r<\infty,
\]
then \(B\) has logarithmic density
\[
\delta=\lim_{N\to\infty}\delta_N.
\]

## Proof

Fix a finite block \(I=\{A+1,\ldots,B\}\).  For \(m\ge T=n_B\), all threshold conventions for the indices in \(I\) are active.  Each first-hit set \(H_i\) is periodic modulo \(L_i\) after its threshold, and hence periodic modulo \(L=L_B\) after \(T\).  Since the \(H_i\) are disjoint, their lifted supports modulo \(L\) are disjoint.  Therefore the eventual support \(D_I\) has density
\[
\frac{|D_I|}{L}
=
\sum_{i\in I}h_i
=
\eta_I.
\]

Let \(x\ge T\).  The part of \(G_I\) below \(T\) contributes at most \(P_I\log T\) to the unnormalized harmonic sum, and since \(\log x\ge\log T\), its contribution to \(\mu_x(G_I)\) is at most \(P_I\).

It remains to bound the eventual periodic part.  For a residue representative \(d\in D_I\), the integers in that class are \(d+kL\).  Hence
\[
\sum_{\substack{m<x\\m\equiv d\pmod L}}\frac1m
\le
\mathbf 1_{d<x}\frac1d
+\frac1L H_{\lfloor x/L\rfloor},
\]
where \(H_M=\sum_{1\le k\le M}1/k\) and \(H_0=0\).  Summing over \(d\in D_I\) gives
\[
\sum_{\substack{m<x\\m\bmod L\in D_I}}\frac1m
\le
\sum_{\substack{d\in D_I\\d<x}}\frac1d
+\eta_I H_{\lfloor x/L\rfloor}.
\]
The first term is at most \(R_I\log x\) by the definition of \(R_I\), because for \(x>L+1\) it is bounded by the \(y=L+1\) case and \(\log(L+1)\le\log x\).  The second term satisfies
\[
H_{\lfloor x/L\rfloor}\le 1+\log x.
\]
Since \(x\ge2\),
\[
\frac{1+\log x}{\log x}\le 1+\frac1{\log2}=c_0.
\]
Therefore the eventual periodic part contributes at most
\[
R_I+c_0\eta_I
\]
to \(\mu_x(G_I)\).  Combining with the threshold-prefix contribution proves
\[
\mu_x(G_I)\le P_I+R_I+c_0\eta_I
\]
for \(x\ge T\), while the same bound is immediate for \(2\le x<T\) from the definition of \(P_I\).  This proves the finite-block certificate.

For the block sequence \(I_r=\{N_{r-1}+1,\ldots,N_r\}\), the hypothesis gives
\[
\sup_{x\ge2}\mu_x(G_{I_r})
\le
(C+c_0)\eta_{I_r}+\varepsilon_r.
\]
This is exactly the block-uniform hypothesis in [[wiki/nodes/mrw-e0778085804e|Block-uniform first-hit criterion for Erdos residue-class logarithmic density]], with constant \(C+c_0\).  Since \(\sum_r\varepsilon_r<\infty\), that proposition proves that \(B\) has logarithmic density \(\delta\).

## Depends on

- [[wiki/nodes/mrw-3d524c92103b|Erdos residue-class logarithmic-density problem]]
- [[wiki/nodes/mrw-ba29cdf1fd30|Finite-shadow reduction for Erdos residue-class logarithmic density]]
- [[wiki/nodes/mrw-e0778085804e|Block-uniform first-hit criterion for Erdos residue-class logarithmic density]]
- [[wiki/nodes/mrw-536639208ce1|Escaping first-hit mass obstruction for finite-shadow decrement control]]
- [[wiki/nodes/mrw-17f44100cb83|Tail-continuity obstruction for Erdos residue-class logarithmic density]]

## Used by

- [[wiki/nodes/mrw-e0971c9b820a|Small-residue obstruction to unshifted CRT prefix-defect summability]]
- [[wiki/nodes/mrw-f1348014e087|Threshold-aware CRT certificate for Erdos first-hit block uniformity]]

## Notes

- This is a finite CRT certificate for the abstract block-uniform hypothesis, not a complete solution of Erdos Problem #25.
- The two quantities \(P_I\) and \(R_I\) separate the two known risks: threshold-scale mass before the block has become periodic, and harmonic concentration of the eventual CRT support at small representatives.
- The next target is no longer automatic summability of \(P_I+R_I\); the unshifted \(R_I\) defect is obstructed by threshold artifacts.  Use the threshold-aware \(Q_I\) certificate instead.
- The small-residue obstruction proves that \(R_I\) is too strong as an automatic summability target, because it may count formal representatives that lie before the activation threshold.  The threshold-aware replacement \(Q_I\) is recorded in [[wiki/nodes/mrw-f1348014e087|Threshold-aware CRT certificate for Erdos first-hit block uniformity]].
- The activation-scale \(Q_I\) bound is recorded in [[wiki/nodes/mrw-eaf102b5cac0|Activation-scale bound for threshold-aware Erdos first-hit defects]].
