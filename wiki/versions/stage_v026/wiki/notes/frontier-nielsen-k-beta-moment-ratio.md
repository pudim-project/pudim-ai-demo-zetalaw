# Frontier Note: Nielsen \(k\)-Beta Moment-Ratio Bridge

## Status

Resolved locally as a `bridge_patch` forage result. The source problem is not part of the old Qi--Lim--Nantomah author cluster and was selected because it grows the current complete-monotonicity/Laplace-kernel layer.

## Source

Li Yin and Jumei Zhang, "On some properties of special functions involving \(k\)-gamma and \(k\)-digamma functions", arXiv:2502.15852.

Scout artifact: `FI-20260526T140000Z-C001`.

## Local Theorem

For \(k>0\), \(n\ge0\), and \(f_k(x)=x\beta_k(x)\),
\[
\frac{f_k^{(n+1)}(x)}{f_k^{(n)}(x)f_k^{(n+2)}(x)}
\]
is strictly increasing on \((0,\infty)\) for odd \(n\), and strictly decreasing on \((0,\infty)\) for even \(n\).

## New Reusable Bridge

If
\[
a_j(x)=\int_0^\infty t^j e^{-xt}\,d\mu(t)>0,
\]
then
\[
B_n(x)=\frac{a_{n+1}(x)}{a_n(x)a_{n+2}(x)}
\]
is strictly increasing. The proof uses moment log-convexity and
\[
\frac{d}{dx}\log B_n(x)=r_n(x)-r_{n+1}(x)+r_{n+2}(x)>0,
\qquad
r_j(x)=\frac{a_{j+1}(x)}{a_j(x)}.
\]

This bridge is now recorded as `T-CM-Laplace-moment-ratio-monotonicity`.
