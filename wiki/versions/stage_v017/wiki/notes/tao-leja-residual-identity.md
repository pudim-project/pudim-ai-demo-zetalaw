# Residual identity for the Chebyshev-Leja bottleneck

Status: partial source progress.

For a Leja step, write
\[
A=A_{\ell-1},\qquad y=x_\ell,\qquad B=X_n\setminus A,\qquad C=B\setminus\{y\}.
\]
Let
\[
\chi_C(t)=\prod_{z\in C}(t-z).
\]
Then the next-pivot Lebesgue value has the exact residual form
\[
1+\lambda_A(y)
=
\frac{\sum_{u\in X_n}\sin\theta_u|\chi_C(u)|}
{\sin\theta_y|\chi_C(y)|}.
\]

This transforms the remaining source-open upper-bound problem into a reverse residual weighted \(L^1\)-to-pivot inequality.

Other true bridge facts:

- The reverse pivot minimizes \(\sin\theta_z|\omega_B'(z)|\) over \(z\in B\).
- If \(r=|B|\), then \(\lambda_A(y)+1\le C^r n^{2r}\).
- The finite Chebyshev-Leja sequence is weak Leja on \([-1,1]\):
\[
|\omega_{\ell-1}(x_\ell)|\ge \frac1{C\log n}\|\omega_{\ell-1}\|_\infty.
\]

Remaining open bottleneck:
\[
\sum_\ell
\frac{\sum_{u\in X_n}\sin\theta_u|\chi_{C_\ell}(u)|}
{\sin\theta_{x_\ell}|\chi_{C_\ell}(x_\ell)|}
\le Cn^2(\log n)^B.
\]

Primary artifact:

- Student proof: `private proof note`
