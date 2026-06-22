# Tao-Sendov root-gap asymptotics and effective defect

Status: partial source progress.

For the tangent-cluster free-critical quadratic
\[
p_d(y)=y^2+A_dy+B_d,
\]
write
\[
C(r,q)=qb+(1-q)a,\qquad q=\frac{m}{m+N}.
\]
Then
\[
|A_d-C|\le\frac2d,\qquad |B_d|\le\frac2d.
\]
If \(|C|\ge c_0\) and \(d\ge64/c_0^2\), the roots split into
\[
|y_S|\le\frac{8}{dc_0},\qquad
|y_L+C|\le\frac{10}{dc_0}.
\]

In the interior regime \(q\in(r,1)\),
\[
1-|C|^2=\Delta(r,q)=(2+r)(q-r)(1-q).
\]
Therefore
\[
1-s
\ge
\frac{\Delta(r,q)}{1+|C|}-\frac{10}{dc_0}
\ge
\frac{\Delta(r,q)}2-\frac{10}{dc_0}.
\]
If \(\Delta(r,q)\ge40/(dc_0)\), then
\[
1-s\ge\frac{\Delta(r,q)}4.
\]

The literal tangent-cluster geometry has the global lower bound
\[
|C|\ge2^{-1/2},
\]
so the small-\(|C|\) collision regime is absent.

Uniform root-gap stability still fails: as \(q\downarrow r\) or \(q\uparrow1\), \(\Delta(r,q)\to0\) and the large root approaches the unit circle.

Next frontier:

\[
O\text{-Tao-Sendov-boundary-layer-large-root-radial-expansion}.
\]

Artifacts:

- Attack plan: `.pudim/attack-plans/AP-20260604T-tao-sendov-root-gap-asymptotics-defect.json`
- Oracle Student: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-sendov-root-gap-asymptotics-student-response.md`
- Proof note: `.pudim/raw/student/20260604T-tao-sendov-root-gap-asymptotics-defect.md`
