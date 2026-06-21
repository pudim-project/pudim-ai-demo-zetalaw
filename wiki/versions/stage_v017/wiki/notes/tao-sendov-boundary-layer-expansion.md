# Tao-Sendov boundary-layer expansion

Status: partial source progress.

This note records a proved tangent-cluster model statement arising from the Tao-related Sendov effectivization branch. It is not a solution of the global Sendov problem or of Tao's full explicit-\(n_0\) question.

For fixed \(0<r<1\), define
\[
\eta=\sqrt{1-\frac{r^2}{4}},\qquad
a=1+r,\qquad
b=\frac r2-i\eta,\qquad
\kappa_r=\frac{(1-r)(2+r)}2.
\]
For the tangent-cluster quadratic
\[
p_{d,q}(y)=y^2+A_{d,q}y+\frac{ab}{d},
\qquad
A_{d,q}=C(r,q)+\frac{a+b-C(r,q)}{d},
\qquad
C(r,q)=(1-q)a+qb,
\]
let \(y_L\) be the large root in the relevant boundary chart.

In the chart \(q=r+\lambda/d\),
\[
1-|y_L|
=
\frac{\kappa_r\bigl(\lambda+r^2(3-r^2)\bigr)}{d}
+O_r\!\left(\frac{(1+\lambda)^2}{d^2}\right).
\]
For \(\lambda\ge0\), this first-order coefficient is positive when \(0<r<1\).

In the chart \(q=1-\lambda/d\),
\[
1-|y_L|
=
\frac{\kappa_r\lambda}{d}
+O_r\!\left(\frac{(1+\lambda)^2}{d^2}\right).
\]
At the formal endpoint \(\lambda=0\), the large root lies exactly on the unit circle.

These formulas match the interior defect
\[
1-|C(r,q)|
=
\frac{(2+r)(q-r)(1-q)}{1+|C(r,q)|}
\]
whenever \(\lambda\to\infty\) and \(\lambda=o(d)\).

Open follow-ups:

- `O-Tao-Sendov-discrete-root-gap-patch`: convert the continuous charts into an exact integer lower bound for \(1-s\) in the tangent-cluster model on compact \(r\)-ranges.
- `O-Tao-Sendov-r1-double-boundary-layer`: handle the degenerate endpoint \(r\to1\), where \(\kappa_r\to0\).

Primary proof artifact: `private proof note`.

Oracle artifact: `private Oracle response`.
