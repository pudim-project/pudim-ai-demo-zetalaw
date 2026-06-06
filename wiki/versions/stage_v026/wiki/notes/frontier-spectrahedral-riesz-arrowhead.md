# Spectrahedral Riesz Arrowhead Kernel

## Source

Kozhasov--Michalek--Sturmfels develop Riesz kernels as integral certificates for complete monotonicity of negative powers of hyperbolic and spectrahedral determinant polynomials. In the spectrahedral setting they note that explicit formulas for spectrahedral volume functions would be desirable.

## Local Seed

For
\[
p(x,y,z)=x(xy-z^2)
\]
on \(C=\{x>0,xy>z^2\}\), the exponent \(\alpha=2\) is the \(3\times3\) spectrahedral volume exponent. Under the pairing \(xu+yv+zw\),
\[
p(x,y,z)^{-2}
=\int e^{-xu-yv-zw}
\frac{4\sqrt v}{15\pi}
\left(u-\frac{w^2}{4v}\right)^{5/2}
\mathbf 1_{\{v>0,u>w^2/(4v)\}}\,du\,dv\,dw.
\]

This is a nonnegative Riesz/Laplace kernel and hence a complete-monotonicity certificate.

## Boundary

The pencil is block diagonal:
\[
p=\det\operatorname{diag}\left(x,\begin{pmatrix}x&z\\z&y\end{pmatrix}\right).
\]
So this is a bridge seed and normalization regression test, not a generic spectrahedral-volume solution.

The next worthwhile frontier is a genuinely non-block \(3\times3\) determinant pencil at \(\alpha=2\).
