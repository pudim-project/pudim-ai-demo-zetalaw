# Tao-Sendov product-root uniform stability

Status: proved local tangent-cluster perturbative theorem.

There is an absolute \(\varepsilon_0>0\) such that every perturbation of the tangent-cluster roots
\[
r,\qquad -1,\ldots,-1,\qquad \tau,\ldots,\tau,
\qquad
\tau=\frac r2+i\sqrt{1-\frac{r^2}{4}},
\]
with
\[
|\alpha_i+1|\le\varepsilon_0,
\qquad
|\beta_j-\tau|\le\varepsilon_0,
\]
has a critical point in \(D(r,1)\), uniformly for all \(0<r\le1\) and all \(m,N\ge1\).

The proof does not use the false inherited condition \(q=m/(m+N)\ge r\). Instead it tracks the product-controlled root through
\[
g(y)=yF(y)
=1+y\sum_\ell\frac1{y-U_\ell}.
\]
For large \(m+N\), the zero is found near \(y=0\) on a contour of radius \(O(1/(m+N))\). For bounded \(m+N\), compactness and Hurwitz continuity preserve the exact product-root zero.

The naive proof on a fixed circle \(|y|=R\), \(\sqrt{2/3}<R<1\), fails: the second exact free root can approach that circle, so no uniform lower bound for \(|F_0|\) exists there.

Primary proof artifact: `.pudim/raw/student/20260604T-tao-sendov-product-root-uniform-stability.md`.

Oracle artifact: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-sendov-product-root-stability-student-response.md`.
