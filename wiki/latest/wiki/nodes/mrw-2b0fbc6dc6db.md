---
id: mrw-2b0fbc6dc6db
type: theorem
title: First-order asymptotic for polynomial Gamma-product thresholds
aliases: ["mrw-2b0fbc6dc6db", "First-order asymptotic for polynomial Gamma-product thresholds"]
status: proved
tags: ["theorem", "proved", "gamma", "monotonicity", "sharp-threshold", "polynomial", "asymptotic", "outside-route", "theory-growth"]
parents: [mrw-c165b8d5e4e2, mrw-37311e7a5a0f, mrw-73218406186e, mrw-1396775c6089]
refs: []
---

# Theorem: First-order asymptotic for polynomial Gamma-product thresholds

## Statement

Keep the notation of [[wiki/nodes/mrw-37311e7a5a0f|Variational sharp threshold for polynomial Gamma-product monotonicity]].  Thus
\[
J_m(s)=\frac{m s^{m-1}}{s^m+1},
\qquad
R_m(s)=\psi^{-1}\!\big(J_m(s)-\psi(s)\big)-s,
\qquad s\ge1,
\]
and
\[
\rho_m=\max_{s\ge1}R_m(s)
\]
is the sharp threshold for strict decrease of
\[
\Phi_{\rho,m}(s)=\frac{s^m+1}{\Gamma(s+\rho)\Gamma(s)}
\]
on \([1,\infty)\).

Then
\[
\log\rho_m=m-\log m+\gamma-1+o(1),
\qquad m\to\infty.
\]
Equivalently,
\[
\rho_m=\exp(\gamma-1+o(1))\,\frac{e^m}{m}.
\]

## Proof

Put
\[
H_m(s)=J_m(s)-\psi(s).
\]
The variational formula says
\[
R_m(s)=\psi^{-1}\!\big(H_m(s)\big)-s.
\]
We first reduce the logarithm of the threshold to the maximum of \(H_m\).
The elementary digamma asymptotic
\[
\psi(x)=\log x+O(1/x)
\qquad(x\to\infty)
\]
implies
\[
\log\psi^{-1}(y)=y+o(1)
\qquad(y\to\infty).
\]

Let
\[
s_0=(m-1)^{1/m}.
\]
The previous scale theorem [[wiki/nodes/mrw-c165b8d5e4e2|Exponential scale for polynomial Gamma-product thresholds]] already shows \(\rho_m\to\infty\).  Hence, at a maximizer \(s_m\) of \(R_m\), the quantity
\[
A_m=s_m+\rho_m=\psi^{-1}\!\big(H_m(s_m)\big)
\]
tends to infinity.  Therefore
\[
\log\rho_m
\le \log A_m
=H_m(s_m)+o(1)
\le \max_{s\ge1}H_m(s)+o(1).
\]
Conversely, evaluating \(R_m\) at \(s_0\) gives
\[
\rho_m\ge \psi^{-1}\!\big(H_m(s_0)\big)-s_0.
\]
Since \(s_0\to1\) and \(H_m(s_0)\to\infty\), the same inverse-digamma estimate gives
\[
\log\rho_m\ge H_m(s_0)+o(1).
\]
Thus it remains to prove
\[
\max_{s\ge1}H_m(s)=H_m(s_0)+o(1).
\]

The derivative identity
\[
J_m'(s)
=
\frac{m s^{m-2}\big((m-1)-s^m\big)}{(s^m+1)^2}
\]
shows that \(J_m\) has its global maximum at \(s_0\), with value
\[
M_m=J_m(s_0)=(m-1)^{(m-1)/m}.
\]
For every \(s\ge1\), \(\psi(s)\ge\psi(1)=-\gamma\), so
\[
H_m(s)=J_m(s)-\psi(s)\le M_m+\gamma.
\]
On the other hand, \(s_0\to1\), and \(\psi\) is continuous at \(1\), so
\[
\psi(s_0)=-\gamma+o(1).
\]
Therefore
\[
H_m(s_0)=M_m-\psi(s_0)=M_m+\gamma+o(1),
\]
and hence
\[
\max_{s\ge1}H_m(s)=M_m+\gamma+o(1).
\]

It remains only to expand \(M_m\).  We have
\[
M_m=(m-1)\exp\!\left(-\frac{\log(m-1)}{m}\right),
\]
and since \(\log(m-1)/m\to0\),
\[
M_m
=(m-1)\left(1-\frac{\log(m-1)}{m}
 +O\!\left(\frac{(\log m)^2}{m^2}\right)\right)
=m-\log m-1+o(1).
\]
Combining the estimates,
\[
\log\rho_m
=\max_{s\ge1}H_m(s)+o(1)
=M_m+\gamma+o(1)
=m-\log m+\gamma-1+o(1).
\]
This proves the theorem.

## Depends on

- [[wiki/nodes/mrw-c165b8d5e4e2|Exponential scale for polynomial Gamma-product thresholds]]
- [[wiki/nodes/mrw-37311e7a5a0f|Variational sharp threshold for polynomial Gamma-product monotonicity]]
- [[wiki/nodes/mrw-73218406186e|Support localization for polynomial Gamma-threshold maximizers]]
- [[wiki/nodes/mrw-1396775c6089|Sharp reciprocal Gamma-product monotonicity threshold]]

## Used by

## Notes

- This sharpens the scale theorem [[wiki/nodes/mrw-c165b8d5e4e2|Exponential scale for polynomial Gamma-product thresholds]] from \(O(1)\) logarithmic precision to the first-order constant.
- The proof does not require uniqueness of the maximizer of \(R_m\).  It uses only the variational threshold formula, the scale theorem, the maximum of \(J_m\), and elementary asymptotics of \(\psi\).
- This is internal theory-growth material for the Bulboaca--Zayed polynomial threshold branch, not public staging material and not terminal evidence for Erdos #536.
