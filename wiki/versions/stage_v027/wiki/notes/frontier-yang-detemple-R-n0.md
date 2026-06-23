# Frontier Note: Yang Detemple \(R(x)\) Constants

## Status

Partial progress only.  The all-\(n\) source problem remains open.

## Source Frontier

Yang asks for best constants \(a_k,b_k\) such that
\[
\left(\sum_{k=0}^{n+1}a_kx^{2k}\right)R(x)-\sum_{k=0}^{n}b_kx^{2k}
\]
is completely monotone, where
\[
R(x)=\psi(x+1/2)-\log x.
\]

## Local Patch

For \(n=0\), normalize \(a_1=24\).  The tail expansion forces
\[
b_0=1,\qquad a_0=\frac{21}{5}.
\]
The resulting function
\[
F_0(x)=\left(24x^2+\frac{21}{5}\right)(\psi(x+1/2)-\log x)-1
\]
is completely monotone.

The proof uses
\[
R(x)=\int_0^\infty e^{-xt}
\left(\frac1t-\frac{1}{2\sinh(t/2)}\right)dt
\]
and shows the induced kernel
\[
24r''(t)+\frac{21}{5}r(t)
\]
is positive through a hyperbolic power-series certificate.

## Boundary

This settles only the normalized \(n=0\) slice and should not be treated as a solution of Yang's full all-\(n\) problem.
