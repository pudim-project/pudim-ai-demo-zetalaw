---
id: "T-Baricz-Vq-q-logconvexity-open-problem"
type: "theorem"
title: "Baricz V_q parameter q log-convexity open problem"
status: "proved"
tags: ["attack-plan", "complete-monotonicity", "coulomb-regularization", "laplace-transform", "log-convexity", "open-problem", "proved", "theorem"]
parents: ["T-Baricz-Vq-strict-q-logconvexity"]
refs: ["private attack plan", "private librarian audit", "private librarian audit", "private scout artifact", "private proof note", "scout/forage/inbox/FI-20260528T-next-loop-015.json", "wiki/notes/frontier-baricz-vq-logconvexity.md"]
---

# Theorem: Baricz V_q parameter q log-convexity open problem

## Statement

For Baricz's function \(V_q(x)=\frac{2e^{x^2}}{\Gamma(q+1)}\int_x^\infty e^{-t^2}(t^2-x^2)^q\,dt\), prove that for every fixed \(x>0\), the map \(q\mapsto V_q(x)\) is log-convex on \((-1,\infty)\).

## Dependencies

- [[wiki/nodes/T-Baricz-Vq-strict-q-logconvexity|Baricz V_q strictly log-convex in q]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private librarian audit`
- `private scout artifact`
- `private proof note`
- `scout/forage/inbox/FI-20260528T-next-loop-015.json`
- `wiki/notes/frontier-baricz-vq-logconvexity.md`

## Proof

Put \(u=t^2-x^2\). Then \(t=(u+x^2)^{1/2}\) and
\[
dt=\frac{du}{2(u+x^2)^{1/2}}.
\]
Since \(e^{x^2}e^{-t^2}=e^{-u}\), the factor \(2\) in the definition cancels the \(1/2\) from \(dt\), giving
\[
V_q(x)=\frac1{\Gamma(q+1)}
\int_0^\infty e^{-u}u^q(u+x^2)^{-1/2}\,du.
\]
This integral is finite for \(q>-1\): near \(0\) the integrand is \(O(u^q)\), and at infinity it is exponentially decaying.

For \(r>0\),
\[
r^{-1/2}=\frac1{\sqrt\pi}\int_0^\infty s^{-1/2}e^{-rs}\,ds.
\]
With \(r=u+x^2\), Tonelli's theorem applies because the integrand is nonnegative. Thus
\[
\begin{aligned}
V_q(x)
&=\frac1{\Gamma(q+1)\sqrt\pi}
\int_0^\infty\int_0^\infty
e^{-u}u^q s^{-1/2}e^{-(u+x^2)s}\,ds\,du\\
&=\frac1{\Gamma(q+1)\sqrt\pi}
\int_0^\infty s^{-1/2}e^{-x^2s}
\left(\int_0^\infty u^q e^{-(1+s)u}\,du\right)\,ds\\
&=\frac1{\sqrt\pi}\int_0^\infty
s^{-1/2}e^{-x^2s}(1+s)^{-(q+1)}\,ds.
\end{aligned}
\]
The last step uses
\[
\int_0^\infty u^q e^{-(1+s)u}\,du
=\frac{\Gamma(q+1)}{(1+s)^{q+1}}.
\]

Therefore the Baricz Vq q Laplace normal form is true.

Let \(a=q+1>0\). The normal form becomes
\[
V_{a-1}(x)=\frac1{\sqrt\pi}\int_0^\infty
s^{-1/2}e^{-x^2s}(1+s)^{-a}\,ds.
\]
For each integer \(n\ge0\), differentiation under the integral gives
\[
(-1)^n\frac{d^n}{da^n}V_{a-1}(x)
=\frac1{\sqrt\pi}\int_0^\infty
(\log(1+s))^n s^{-1/2}e^{-x^2s}(1+s)^{-a}\,ds\ge0.
\]
The differentiation is justified locally uniformly in \(a>0\): near \(s=0\), \((\log(1+s))^n s^{-1/2}=O(s^{n-1/2})\), and as \(s\to\infty\), the factor \(e^{-x^2s}\) dominates every logarithmic and polynomial factor.

Thus \(a\mapsto V_{a-1}(x)\) is completely monotone on \((0,\infty)\). Equivalently, after the change of variables \(y=\log(1+s)\), it is a positive Laplace transform in \(a\).

Therefore the Baricz Vq q complete monotonicity is true.

For \(a>0\), write
\[
F_x(a)=V_{a-1}(x)
=\int_{(0,\infty)} e^{-ay}\,d\nu_x(y),
\]
where \(\nu_x\) is the positive pushforward of
\[
\frac1{\sqrt\pi}s^{-1/2}e^{-x^2s}\,ds
\]
under \(y=\log(1+s)\). This measure is not concentrated at one point because it has positive density on \(s>0\), hence on \(y>0\).

For \(a_1\ne a_2\) and \(0<\lambda<1\), strict Holder inequality gives
\[
F_x(\lambda a_1+(1-\lambda)a_2)
<
F_x(a_1)^\lambda F_x(a_2)^{1-\lambda}.
\]
Strictness holds because \(e^{-a_1y}\) and \(e^{-a_2y}\) are not proportional \(\nu_x\)-almost everywhere unless \(\nu_x\) is supported at a single \(y\).

Thus \(a\mapsto F_x(a)\) is strictly log-convex on \((0,\infty)\). Since \(a=q+1\), the shift preserves strict log-convexity, so \(q\mapsto V_q(x)\) is strictly log-convex on \((-1,\infty)\) for every fixed \(x>0\).

Therefore the Baricz Vq strict q logconvexity is true, and it implies the source node the Baricz Vq q logconvexity open problem.

_Proof source: `private proof note`._

## Tags

`attack-plan`, `complete-monotonicity`, `coulomb-regularization`, `laplace-transform`, `log-convexity`, `open-problem`, `proved`, `theorem`
