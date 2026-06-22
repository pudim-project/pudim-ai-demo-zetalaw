# Leja-Chebyshev next-pivot Lebesgue reduction

Status: partial source progress.

The corrected Tao comment-thread target is an effective upper bound for the Newton condition number of first-kind Chebyshev roots in finite Leja order. The direct dyadic-prefix route does not close, but the problem reduces to a next-pivot Lebesgue estimate.

Let \(A_{\ell-1}=\{x_1,\ldots,x_{\ell-1}\}\) and
\[
\omega_{\ell-1}(t)=\prod_{i<\ell}(t-x_i).
\]
Let \(\lambda_{\ell-1}(x)\) be the ordinary Lebesgue function of \(A_{\ell-1}\). Then
\[
\Lambda_{\mathcal N}(\pi(X_n))
\le
1+C\log n
\sum_{\ell=2}^n
\left(1+\lambda_{\ell-1}(x_\ell)\right).
\]

The proof uses two facts:

The full Chebyshev root grid is an \(O(\log n)\)-norming set for degree \(<n\) polynomials:
\[
\|q\|_\infty\le C\log n\max_{y\in X_n}|q(y)|.
\]
The finite Leja rule makes \(x_\ell\) maximize \(|\omega_{\ell-1}|\) among unused grid points.

Therefore the remaining bottleneck is
\[
\sum_{\ell=2}^n\lambda_{\ell-1}(x_\ell)
\le
C n^2(\log n)^B.
\]
If this holds, then
\[
\Lambda_{\mathcal N}(\pi(X_n))
\le
C n^2(\log n)^{B+1}.
\]

Obstruction: exact dyadic-prefix structure is false for first-kind finite Chebyshev roots. For \(n=8\), the canonical Leja order starts \(1,8,4,6,\ldots\), not \(1,8,4,5,\ldots\).

Primary artifacts:

- Student proof: `.pudim/raw/student/20260604T-tao-leja-chebyshev-next-pivot-reduction.md`
- Student Oracle: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-leja-chebyshev-quadratic-upper-student-response.md`
