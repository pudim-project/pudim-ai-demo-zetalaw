---
id: "T-Yang-MillsRatio-HalfGamma-LogConvexity"
type: "theorem"
title: "Yang Mills-ratio half-gamma log-convexity"
status: "proved"
tags: ["application-candidate", "gamma-normalization", "laplace-transform", "log-convexity", "mills-ratio", "open-problem-solved", "proved", "source-solving", "strict-private-post-v016", "theorem", "tilted-variance", "true"]
parents: ["O-Yang-MillsRatio-HalfGamma-LogConvexity-source-gate", "D-Yang-MillsOrderMomentKernel", "L-SqrtLaplace-GammaTilt-LogConvexity", "D-Laplace-kernel-and-tilted-moment-language", "T-From-Mills-Laplace-CM-normal-form"]
refs: ["oracle/responses/OS-20260620T145456Z-oracle-response.md", "raw/student/20260620T1505-yang-mills-halfgamma-logconvexity.md"]
---

# Theorem: Yang Mills-ratio half-gamma log-convexity

## Statement

Let \(R_p(x)=\int_0^\infty t^p\exp(-t^2/2-xt)\,dt\) for \(x>0\) and \(p>-1\). For every fixed \(x>0\), the function \(p\mapsto R_p(x)/\Gamma((p+1)/2)\) is strictly log-convex on \((-1,\infty)\). This proves Yang's Remark 11 conjectural log-convexity under the source normalization.

## Dependencies

- [[wiki/nodes/O-Yang-MillsRatio-HalfGamma-LogConvexity-source-gate|Yang order-p Mills-ratio half-gamma log-convexity source gate]]
- [[wiki/nodes/D-Yang-MillsOrderMomentKernel|Yang order-p Mills moment kernel]]
- [[wiki/nodes/L-SqrtLaplace-GammaTilt-LogConvexity|Square-root Laplace gamma tilt gives strict log-convexity]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]
- [[wiki/nodes/T-From-Mills-Laplace-CM-normal-form|Mills ratio positive Laplace representation and complete monotonicity]]

## Proof and provenance references

- `oracle/responses/OS-20260620T145456Z-oracle-response.md`
- `raw/student/20260620T1505-yang-mills-halfgamma-logconvexity.md`

## Proof

Yang's source normalization is
\[
R_p(x)=\int_0^\infty t^p\exp(-t^2/2-xt)\,dt,\qquad p>-1,\quad x>0.
\]
Put \(a=(p+1)/2\), so \(p=2a-1\). With \(y=t^2/2\), one has
\[
t^{2a-1}\,dt=2^{a-1}y^{a-1}\,dy
\]
and therefore
\[
R_{2a-1}(x)
=2^{a-1}\int_0^\infty y^{a-1}e^{-y}e^{-x\sqrt{2y}}\,dy.
\]

For \(x>0\), use the square-root Laplace identity
\[
e^{-x\sqrt{2y}}
={x\over\sqrt{2\pi}}\int_0^\infty
s^{-3/2}\exp\!\left(-{x^2\over 2s}\right)e^{-sy}\,ds.
\]
This is the standard Levy-density representation of the function \(y\mapsto e^{-x\sqrt{2y}}\). The kernel
\[
k_x(s)={x\over\sqrt{2\pi}}s^{-3/2}\exp\!\left(-{x^2\over 2s}\right),\qquad s>0,
\]
is positive and integrates to \(1\), as is seen by evaluating the identity at \(y=0\).

Since all terms are nonnegative, Tonelli's theorem gives
\[
\begin{aligned}
R_{2a-1}(x)
&=2^{a-1}\int_0^\infty y^{a-1}e^{-y}
\left(\int_0^\infty e^{-sy}k_x(s)\,ds\right)dy \\
&=2^{a-1}\int_0^\infty k_x(s)
\left(\int_0^\infty y^{a-1}e^{-(1+s)y}\,dy\right)ds \\
&=2^{a-1}\Gamma(a)\int_0^\infty (1+s)^{-a}k_x(s)\,ds .
\end{aligned}
\]
Thus
\[
{R_{2a-1}(x)\over \Gamma(a)}
=2^{a-1}\int_0^\infty (1+s)^{-a}k_x(s)\,ds.
\]

Let \(S_x\) be distributed with density \(k_x\), and set \(Z_x=\log(1+S_x)\). Then
\[
{R_{2a-1}(x)\over \Gamma(a)}
=2^{a-1}\mathbb E e^{-aZ_x}.
\]
For the tilted law
\[
d\mathbb P_{a,x}
={e^{-aZ_x}\over \mathbb E e^{-aZ_x}}\,d\mathbb P_{Z_x},
\]
ordinary differentiation of the finite Laplace transform gives
\[
{d^2\over da^2}\log {R_{2a-1}(x)\over \Gamma(a)}
=\operatorname{Var}_{a,x}(Z_x)\ge 0.
\]
The added affine term \((a-1)\log 2\) contributes no second derivative.

Because \(a=(p+1)/2\), the \(p\)-curvature is
\[
{d^2\over dp^2}\log {R_p(x)\over \Gamma((p+1)/2)}
={1\over4}\operatorname{Var}_{a,x}\!\bigl(\log(1+S_x)\bigr)\ge 0.
\]
For \(x>0\), \(k_x\) is positive on all of \((0,\infty)\), so \(\log(1+S_x)\) is nonconstant under every tilted law. The variance is therefore strictly positive, proving strict log-convexity.

_Proof source: `raw/student/20260620T1505-yang-mills-halfgamma-logconvexity.md`._

## Do not claim

- Do not claim strictness at \(x=0\).
- Do not claim the separate moment-ratio concavity route.
- Do not assign public APP numbering until staging/registry promotion.
- Do not public-stage without user request.

## Tags

`application-candidate`, `gamma-normalization`, `laplace-transform`, `log-convexity`, `mills-ratio`, `open-problem-solved`, `proved`, `source-solving`, `strict-private-post-v016`, `theorem`, `tilted-variance`, `true`
