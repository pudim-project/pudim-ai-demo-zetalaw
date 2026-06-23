# Frontier: Garrappa--Gerhold--Popolizio--Simon Mittag-Leffler Boundary Convexity

Scout forage `FI-20260528T-next-loop-008` selected the boundary function \(h\) from Garrappa--Gerhold--Popolizio--Simon, arXiv:2410.11852.

The source defines \(h:(0,\infty)\to(0,\infty)\) by
\[
2\Gamma(x+h(x))^2=\Gamma(h(x))\Gamma(2x+h(x)).
\]

The paper proves that \(h\) is real analytic and increasing, extends continuously by \(h(0)=0\), satisfies \(h'(0)=\sqrt2-1\), and is strictly convex on \([1,\infty)\). It explicitly leaves strict convexity on the whole interval \((0,\infty)\) as a believed but unresolved point.

The local Theory fit is through Gamma, digamma/trigamma kernels, implicit differentiation, and endpoint asymptotic expansion. Bounded Student scope: derive the implicit derivative normal form and prove only a small-\(x\) convexity slice.

## Student/Librarian outcome `20260528T133000Z`

Student proved the implicit derivative normal form and the endpoint expansion
\[
h(x)=(\sqrt2-1)x+\frac{\sqrt2\pi^2}{12}x^3+O(x^4).
\]

Thus
\[
h''(x)=\frac{\sqrt2\pi^2}{2}x+O(x^2),
\]
so \(h''(x)>0\) for all sufficiently small positive \(x\). This proves a local convexity slice near \(0\), but the source's full convexity problem remains open on the remaining middle interval.
