---
id: mrw-c165b8d5e4e2
type: theorem
title: Exponential scale for polynomial Gamma-product thresholds
aliases: ["mrw-c165b8d5e4e2", "Exponential scale for polynomial Gamma-product thresholds"]
status: proved
tags: ["theorem", "proved", "gamma", "monotonicity", "sharp-threshold", "polynomial", "asymptotic-scale", "outside-route", "theory-growth"]
parents: [mrw-37311e7a5a0f, mrw-73218406186e, mrw-1396775c6089]
refs: ["references/sources/20260518T153717Z-bulboaca-zayed-gamma-monotonicity.md"]
---

# Theorem: Exponential scale for polynomial Gamma-product thresholds

## Statement

Keep the notation of [[wiki/nodes/mrw-37311e7a5a0f|Variational sharp threshold for polynomial Gamma-product monotonicity]].  Thus, for \(m\ge1\),
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

Then, as \(m\to\infty\),
\[
\log \rho_m=m-\log m+O(1).
\]
Equivalently, the polynomial Gamma-product threshold has exponential scale
\[
\rho_m=\exp(O(1))\,\frac{e^m}{m}.
\]

## Proof

Let
\[
s_0=(m-1)^{1/m},
\qquad
M_m=J_m(s_0)=(m-1)^{(m-1)/m}.
\]
The derivative formula already used in [[wiki/nodes/mrw-73218406186e|Support localization for polynomial Gamma-threshold maximizers]] is
\[
J_m'(s)
=
\frac{m s^{m-2}\big((m-1)-s^m\big)}{(s^m+1)^2}.
\]
Hence \(J_m\) is increasing on \([1,s_0]\), decreasing on \([s_0,\infty)\), and its global maximum is \(M_m\).

First,
\[
M_m
=(m-1)\exp\!\left(-\frac{\log(m-1)}{m}\right)
=m-\log m+O(1).
\]
Indeed, \(\log(m-1)/m\to0\), so expanding the exponential gives
\[
M_m=(m-1)\left(1-\frac{\log(m-1)}{m}
 +O\!\left(\frac{(\log m)^2}{m^2}\right)\right)
=m-\log m+O(1).
\]

Let \(s_m\) be a maximizer of \(R_m\), whose existence is proved in [[wiki/nodes/mrw-37311e7a5a0f|the variational threshold theorem]].  Put
\[
A_m=s_m+\rho_m
=\psi^{-1}\!\big(J_m(s_m)-\psi(s_m)\big).
\]
Since \(s_m\ge1\), the monotonicity of \(\psi\) gives \(\psi(s_m)\ge\psi(1)=-\gamma\).  Since \(J_m(s_m)\le M_m\),
\[
\psi(A_m)=J_m(s_m)-\psi(s_m)\le M_m+\gamma.
\]
Use the elementary digamma estimate
\[
\psi(x)\ge \log x-\frac1x
\qquad (x>0).
\]
Here \(A_m>1\) for \(m\ge4\), so
\[
\log \rho_m\le \log A_m
\le \psi(A_m)+1
\le M_m+\gamma+1.
\]
Thus \(\log\rho_m\le M_m+O(1)\).

For the lower bound, evaluate \(R_m\) at \(s_0\).  Let
\[
B_m=\psi^{-1}\!\big(M_m-\psi(s_0)\big).
\]
Then \(\rho_m\ge R_m(s_0)=B_m-s_0\).  The elementary upper estimate
\[
\psi(x)<\log x\qquad(x>0)
\]
gives
\[
B_m>\exp(M_m-\psi(s_0)).
\]
For all sufficiently large \(m\), one has \(1<s_0<2\), while \(M_m-\psi(s_0)\to\infty\).  Hence \(B_m>2s_0\), and therefore
\[
\rho_m\ge B_m-s_0\ge \frac12 B_m.
\]
Consequently
\[
\log\rho_m
\ge M_m-\psi(s_0)-\log2.
\]
Since \(1\le s_0\le2\), the quantity \(\psi(s_0)\) is bounded independently of \(m\).  Therefore
\[
\log\rho_m\ge M_m-O(1).
\]
Combining the upper and lower bounds gives
\[
\log\rho_m=M_m+O(1)=m-\log m+O(1),
\]
as claimed.

## Depends on

- [[wiki/nodes/mrw-37311e7a5a0f|Variational sharp threshold for polynomial Gamma-product monotonicity]]
- [[wiki/nodes/mrw-73218406186e|Support localization for polynomial Gamma-threshold maximizers]]
- [[wiki/nodes/mrw-1396775c6089|Sharp reciprocal Gamma-product monotonicity threshold]]

## Used by

- [[wiki/nodes/mrw-2b0fbc6dc6db|First-order asymptotic for polynomial Gamma-product thresholds]]

## Notes

- This theorem is an asymptotic scale theorem, not an exact evaluation of \(\rho_m\).
- It prevents a purely numerical continuation of the polynomial Gamma branch: any certified table for \(\rho_m\) should now be measured against the structural scale \(e^m/m\).
- This is outside the Erdos #536 tower and is not terminal evidence for any pair-link-free or lcm problem.
