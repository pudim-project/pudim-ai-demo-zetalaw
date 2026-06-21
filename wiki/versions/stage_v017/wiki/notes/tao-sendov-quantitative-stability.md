# Tao-Sendov quantitative tangent-cluster stability

Status: effective fixed-parameter theorem; direct \(P'\)-Rouché uniformity fails.

The fixed-parameter Rouché theorem can be made explicit. For the model
\[
P^0(z)=(z-r)(z+1)^m(z-\tau)^N,
\]
write \(y=z-r\), \(a=1+r\), \(b=r-\tau\), \(d=m+N+1\), and
\[
P^{0\,\prime}(z)=(a+y)^{m-1}(b+y)^{N-1}Q(y).
\]
If \(Q(y)=d(y-y_1)(y-y_2)\), then on \(|z-r|=\rho<1\),
\[
\min |P^{0\,\prime}|
\ge
(1+r-\rho)^{m-1}(1-\rho)^{N-1}
d\prod_{j=1}^2|\rho-|y_j||.
\]
This gives an explicit perturbation radius
\[
\varepsilon_\rho=
\min\left\{
\frac{1-\rho}{2},
\frac{\Lambda_\rho}{2d(d-1)(2+r+\rho)^{d-2}}
\right\}.
\]

The result is useful but not uniform: the direct \(P'\)-Rouché route loses exponentially in \(m,N\).

Next frontier:

\[
O\text{-Tao-Sendov-logderivative-quantitative-tangent-stability}.
\]

The normalized logarithmic derivative
\[
F_0(y)=1+\frac{my}{a+y}+\frac{Ny}{b+y}
=\frac{Q(y)}{(a+y)(b+y)}
\]
should avoid the large cluster-factor losses.

Artifacts:

- Attack plan: `private attack plan`
- Oracle Student: `private Oracle response`
- Proof note: `private proof note`
