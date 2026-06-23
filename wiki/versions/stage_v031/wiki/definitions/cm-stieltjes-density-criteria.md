# Complete-Monotone Density Criteria

## Closure

Completely monotone functions on \((0,\infty)\) are closed under pointwise products, nonnegative finite sums, and nonnegative parameter integrals whenever the integral is finite.

## Stieltjes Density Criterion

If \(\phi\) is completely monotone and
\[
F(x)=\int_0^\infty e^{-xt}\phi(t)\,dt
\]
is finite for every \(x>0\), then \(F\) is a Stieltjes function. Indeed, Bernstein's theorem gives
\[
\phi(t)=\int_0^\infty e^{-ts}\,d\mu(s),
\]
and Tonelli gives
\[
F(x)=\int_0^\infty \frac{d\mu(s)}{x+s}.
\]

## Complete-Bernstein Levy Density Criterion

If
\[
f(x)=a+bx+\int_0^\infty (1-e^{-xt})m(t)\,dt
\]
is a Bernstein representation and \(m\) is completely monotone, then \(f\) is a complete Bernstein function, subject to the usual Levy integrability condition.
