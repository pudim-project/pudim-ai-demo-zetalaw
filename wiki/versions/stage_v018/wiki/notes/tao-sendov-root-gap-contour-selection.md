# Tao-Sendov root-gap contour selection

Status: deployable fixed-parameter contour theorem plus no-uniform-gap obstruction.

For the tangent-cluster quadratic
\[
Q(y)=d(y-y_1)(y-y_2),
\]
at least one root has modulus \(<1\). Define
\[
s=\max\{|y_j|:|y_j|<1\},\qquad
\rho_*=\frac{1+s}{2}.
\]
Then \(\rho_*\) avoids both root radii and encloses exactly the free roots with modulus \(<1\). The product gap satisfies
\[
\prod_{j=1}^2|\rho_*-|y_j||
\ge
\left(\frac{1-s}{2}\right)^2.
\]

This gives the deployable log-derivative boundary bound
\[
\mu_{\rho_*}
\ge
\frac{d(1-s)^2}{4(1+r+\rho_*)(1+\rho_*)}.
\]

The same pass proves a genuine obstruction to uniformity: no universal \(\delta>0\) has \(s\le1-\delta\). In the large-degree limit with
\[
q=\frac{m}{m+N}\in(r,1),
\]
one root tends to
\[
-C(q),\qquad C(q)=qb+(1-q)a,
\]
and
\[
|C(q)|^2-1=(2+r)(q-r)(q-1).
\]
As \(q\downarrow r\), the inner root approaches the unit circle.

Next frontier:

\[
O\text{-Tao-Sendov-root-gap-asymptotics-effective-defect}.
\]

Artifacts:

- Attack plan: `.pudim/attack-plans/AP-20260604T-tao-sendov-root-gap-contour-selection.json`
- Oracle Student: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-sendov-root-gap-student-response.md`
- Proof note: `.pudim/raw/student/20260604T-tao-sendov-root-gap-contour-selection.md`
