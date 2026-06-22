# Tao-Sendov logarithmic-derivative quantitative tangent stability

Status: fixed-parameter stability and methodological upgrade.

The direct \(P'\)-Rouché theorem had exponential cluster-factor losses. The normalized logarithmic derivative
\[
F(y)=y\frac{P'(r+y)}{P(r+y)}
\]
removes those product losses.

For the exact model,
\[
F_0(y)=1+\frac{my}{a+y}+\frac{Ny}{b+y}
=\frac{Q(y)}{(a+y)(b+y)}.
\]
On \(|y|=\rho\),
\[
\min |F_0|
\ge
\frac{d\prod_{j=1}^2|\rho-|y_j||}{(1+r+\rho)(1+\rho)}.
\]
For cluster perturbation size \(e\),
\[
|F-F_0|
\le
\rho e\left[
\frac{m}{(1+r-\rho)(1+r-\rho-e)}
+\frac{N}{(1-\rho)(1-\rho-e)}
\right].
\]
If this is smaller than the boundary lower bound, Rouché preserves the free critical zero count inside \(|y|<\rho\).

This is still fixed-parameter/contour-dependent, but it removes the exponential dependence in \(m,N\) from direct \(P'\)-Rouché.

Next frontier:

\[
O\text{-Tao-Sendov-exact-root-gap-contour-selection}.
\]

Artifacts:

- Attack plan: `.pudim/attack-plans/AP-20260604T-tao-sendov-logderivative-quantitative-stability.json`
- Oracle Student: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-sendov-logderivative-stability-student-response.md`
- Proof note: `.pudim/raw/student/20260604T-tao-sendov-logderivative-stability.md`
