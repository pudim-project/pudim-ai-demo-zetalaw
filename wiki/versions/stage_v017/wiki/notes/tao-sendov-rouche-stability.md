# Tao-Sendov tangent-cluster Rouché stability

Status: partial source progress.

The exact tangent-cluster model has a free critical point uniformly inside \(D(r,1)\). This pass proves fixed-parameter perturbative stability.

For fixed \(0<r\le1\), \(m,N\ge1\), and
\[
\tau=\frac r2+i\sqrt{1-\frac{r^2}{4}},
\]
small perturbations of the roots in
\[
(z-r)(z+1)^m(z-\tau)^N
\]
preserve a critical point in \(D(r,1)\). More strongly, after choosing a zero-free contour \(|z-r|=\rho<1\) enclosing an interior critical point of the exact model, sufficiently small perturbations preserve the critical-point count in \(D(r,\rho)\).

The proof is Rouché's theorem applied to \(P'\) on the contour.

This does not prove uniform stability in \(r,m,N\), and it does not prove a global annular Sendov theorem.

Next frontier:

\[
O\text{-Tao-Sendov-quantitative-tangent-cluster-stability}.
\]

The missing ingredient is an explicit lower bound for
\[
\min_{|z-r|=\rho}|P^{0\,\prime}(z)|
\]
from the quadratic free-critical equation.

Artifacts:

- Attack plan: `private attack plan`
- Oracle Student: `private Oracle response`
- Proof note: `private proof note`
