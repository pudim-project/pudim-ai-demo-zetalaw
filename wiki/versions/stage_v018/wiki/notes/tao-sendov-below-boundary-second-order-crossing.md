# Tao-Sendov below-boundary second-order crossing

Status: proved local tangent-cluster theorem.

In the below-boundary chart
\[
q=r-\frac{\mu}{d},
\]
for the tangent-cluster quadratic, the large root \(y_L\to-C_r\) has the expansion
\[
1-|y_L|
=
\frac{\kappa_r\Delta}{d}
+\frac{\Theta(r,\mu)}{d^2}
+O(d^{-3}),
\]
where
\[
\Delta=r^2(3-r^2)-\mu,\qquad
\kappa_r=\frac{(1-r)(2+r)}2.
\]
The explicit second-order term is
\[
\Theta(r,\mu)
=
\frac{r+2}{8}
\left[
(r+1)^2(r-2)\Delta^2
+4r(7-10r^2+6r^4-r^6)\Delta
+4r(r-1)P(r)
\right],
\]
with
\[
P(r)=r^6+r^5-5r^4-5r^3+4r^2+4r+2.
\]

On the first-order transition line \(\Delta=0\),
\[
\Theta
=
\frac{r(r-1)(r+2)}2P(r)<0
\]
for \(0<r<1\). Thus at \(\mu=r^2(3-r^2)\), the large root is already outside the unit disk at order \(d^{-2}\).

This closes the specific second-order crossing target, but it remains a local tangent-cluster theorem, not a global Tao-Sendov theorem.

Primary proof artifact: `.pudim/raw/student/20260604T-tao-sendov-below-boundary-second-order-crossing.md`.

Oracle artifact: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-sendov-below-boundary-second-order-student-response.md`.
