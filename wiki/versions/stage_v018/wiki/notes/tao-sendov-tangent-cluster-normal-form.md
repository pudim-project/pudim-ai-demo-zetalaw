# Tao-Sendov tangent-cluster normal form

Status: true model certificate; partial source progress.

The tangent-cluster route-kill from the cap-mass pass is not itself a Sendov obstruction.

For
\[
P_{m,N,r}(z)=(z-r)(z+1)^m(z-\tau)^N,
\qquad
\tau=\frac r2+i\sqrt{1-\frac{r^2}{4}},
\]
with \(0<r\le1\), \(m,N\ge1\), a free critical point lies in \(D(r,1)\). The explicit bound is
\[
\min_{\zeta\ \mathrm{free}}|\zeta-r|
\le
\sqrt{\frac{1+r}{m+N+1}}
\le
\sqrt{\frac23}.
\]

The proof clears denominators in the logarithmic derivative equation
\[
\frac1{z-r}+\frac m{z+1}+\frac N{z-\tau}=0.
\]
After setting \(y=z-r\), the free critical equation becomes a quadratic
\[
Q(y)=(1+m+N)y^2+(a+b+mb+Na)y+ab,
\]
where \(a=1+r\) and \(b=r-\tau\), with \(|b|=1\). Vieta gives
\[
|y_1y_2|=\frac{1+r}{1+m+N}\le\frac23,
\]
so one root has \(|y|<1\).

Next frontier:

\[
O\text{-Tao-Sendov-tangent-cluster-Rouche-stability}.
\]

Prove local, then possibly uniform, stability when the clusters at \(-1\) and \(\tau\) are perturbed.

Artifacts:

- Attack plan: `.pudim/attack-plans/AP-20260604T-tao-sendov-tangent-cluster-normal-form.json`
- Oracle Student: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-sendov-tangent-cluster-student-response.md`
- Proof note: `.pudim/raw/student/20260604T-tao-sendov-tangent-cluster-normal-form.md`
