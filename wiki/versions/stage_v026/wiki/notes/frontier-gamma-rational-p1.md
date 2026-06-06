# Frontier: Gamma Rational Upper-Bound Constant p1

## Source

Yang, Qian, Chu, and Zhang, "On rational bounds for the gamma function", Journal of Inequalities and Applications 2017, article 210.

Source URL: https://link.springer.com/article/10.1186/s13660-017-1484-y

The 2017 article proves
\[
\Gamma(1+x)<\frac{x^2+9/5}{x+9/5}
\]
for \(0<x<1\), and records that the best possible upper parameter \(p_1\) is still open.

Follow-up literature check: Shen, Yang, Qian, Zhang, and Chu, "Sharp rational bounds for the gamma function", Mathematical Inequalities & Applications 23(3), 843--853, 2020, DOI https://doi.org/10.7153/mia-2020-23-68, proves the sharp result. Its Theorem 3.1 gives the if-and-only-if condition with
\[
p_0=\frac{x_0\Gamma(x_0+1)-x_0^2}{1-\Gamma(x_0+1)}=1.755\ldots,
\]
where \(x_0=0.192\ldots\) is the unique solution of the corresponding psi/Gamma critical equation on \((0,1)\).

Therefore this item is no longer a valid "fresh open problem" target. The local bridge below remains useful theory growth, but the source problem itself should be treated as literature-closed unless Pudim explicitly decides to reprove/import the 2020 theorem.

## Domain Fit

This is a Gamma-function endpoint and rational-envelope problem. It is close to the staged Gamma threshold layer, but the source problem is now known to be closed in the literature. It is not a Pudim application unless a local proof is later staged with a clear theory-growth dependency.

The useful bridge is to isolate the parameter. For
\[
R_p(x)=\frac{x^2+p}{x+p},
\]
one has
\[
\frac{\partial R_p(x)}{\partial p}=\frac{x-x^2}{(x+p)^2}>0
\]
on \(0<x<1\). Since \(0<\Gamma(1+x)<1\) on this interval, the pointwise condition
\[
\Gamma(1+x)<R_p(x)
\]
is equivalent to
\[
p>H(x),\qquad
H(x)=\frac{x(\Gamma(1+x)-x)}{1-\Gamma(1+x)}.
\]

Thus the optimal constant problem reduces to certifying
\[
p_*=\sup_{0<x<1} H(x).
\]

## First-Contact Numerics

Numerical first contact suggests an interior maximizer
\[
\xi\approx0.1927776581313346099476289523,
\qquad
p_*\approx1.7552752098189566314896646434.
\]

The endpoint checks are consistent with a strict interior maximum:
\[
\lim_{x\to0^+}H(x)=\frac1\gamma\approx1.7324547146,
\qquad
\lim_{x\to1^-}H(x)=\frac{\gamma}{1-\gamma}\approx1.365\ldots .
\]

These numerics agree with the 2020 paper. Student proved the envelope reduction locally, but should not continue treating this as an unresolved source problem. Rotate to the trigamma-tetragamma backup candidate or the reciprocal zeta-tail fallback.
