# Frontier Note: BMR Tau-Hypergeometric Midpoint Slice

## Status

Partial progress only.  The source's global log-concavity/concavity problem remains open.

## Source Frontier

Bansal, Mehrez, and Raina ask whether
\[
a\mapsto {}_2\phi^\tau_1(a,c-a;c;z)
\]
is log-concave, or concave, on \((0,c)\).

## Local Patch

For the coefficient
\[
A_k(a)=
\frac{\Gamma(c)}{\Gamma(a)\Gamma(c-a)}
\frac{\Gamma(a+k\tau)\Gamma(c-a+k\tau)}{\Gamma(c+k\tau)},
\]
one has
\[
(\log A_k)''=
\psi_1(a+k\tau)-\psi_1(a)
+\psi_1(c-a+k\tau)-\psi_1(c-a)\le0.
\]
Thus each coefficient is log-concave in \(a\), strictly for \(k\ge1\).

At \(a=c/2\), symmetry gives \(F'(c/2)=0\), and for \(0<z<1\) the positive nonzero terms give \(F''(c/2)<0\).  Hence
\[
(\log F)''(c/2)<0.
\]

## Boundary

This does not prove global log-concavity or concavity on \((0,c)\); it records a coefficientwise bridge and a strict midpoint local slice.
