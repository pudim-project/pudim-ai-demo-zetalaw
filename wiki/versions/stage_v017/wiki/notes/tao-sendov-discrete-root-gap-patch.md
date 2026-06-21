# Tao-Sendov discrete root-gap patch

Status: partial source progress.

This note records the discrete tangent-cluster root-gap patch obtained after the boundary-layer expansion. It is scoped to the tangent-cluster model and does not prove a global Sendov theorem.

For fixed compact \(r\)-ranges
\[
0<r_0\le r\le1-\rho<1,
\]
take integers \(m,N\ge1\), \(D=m+N\), \(q=m/D\), and \(d=D+1\). In the tangent-cluster quadratic
\[
p_{d,q}(y)=y^2+A_{d,q}y+\frac{ab}{d},
\qquad
A_{d,q}=C(r,q)+\frac{a+b-C(r,q)}{d},
\]
the proved patch is:

\[
q\ge r
\quad\Longrightarrow\quad
1-s\ge\frac{c(r_0,\rho)}d
\]
for some \(c(r_0,\rho)>0\) and all sufficiently large \(d\), where \(s\) is the largest modulus among roots of \(p_{d,q}\) inside the unit disk.

The all-\(q\) version is false. In the below-boundary layer
\[
q=r-\frac{\mu}{d},
\]
the boundary expansion gives
\[
1-|y_L|
=
\frac{\kappa_r\bigl(r^2(3-r^2)-\mu\bigr)}d
+O(d^{-2}),
\qquad
\kappa_r=\frac{(1-r)(2+r)}2.
\]
The coefficient vanishes at \(\mu=r^2(3-r^2)\). Because \(r\) is continuous, the exact discrete values \(q=m/(m+N)\) do not prevent tuning into this crossing layer. Thus the best all-\(q\) replacement must be a trichotomy or a second-order crossing statement.

Primary proof artifact: `private proof note`.

Oracle artifact: `private Oracle response`.
