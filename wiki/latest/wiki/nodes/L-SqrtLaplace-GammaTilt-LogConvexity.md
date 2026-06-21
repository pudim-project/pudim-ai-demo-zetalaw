---
id: "L-SqrtLaplace-GammaTilt-LogConvexity"
type: "lemma"
title: "Square-root Laplace gamma tilt gives strict log-convexity"
status: "proved"
tags: ["bridge", "gamma-tilt", "laplace-transform", "lemma", "levy-density", "log-convexity", "proved", "strict-private-post-v016", "tilted-variance", "true"]
parents: ["D-Laplace-kernel-and-tilted-moment-language"]
refs: ["private Oracle response", "private proof note"]
---

# Lemma: Square-root Laplace gamma tilt gives strict log-convexity

## Statement

For \(x>0\), let \(k_x(s)=x(2\pi)^{-1/2}s^{-3/2}\exp(-x^2/(2s))\) on \((0,\infty)\). Then \(k_x\) is a positive probability density and, for every \(a>0\), \(\Gamma(a)^{-1}\int_0^\infty y^{a-1}e^{-y}e^{-x\sqrt{2y}}\,dy=\int_0^\infty(1+s)^{-a}k_x(s)\,ds\). Consequently the logarithmic second derivative in \(a\) of this gamma-normalized transform equals the tilted variance of \(\log(1+S_x)\), and is strictly positive.

## Dependencies

- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `private Oracle response`
- `private proof note`

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

_Proof source: `private proof note`._

## Do not claim

- Do not infer moment-ratio concavity from this lemma.
- Do not claim strictness at the degenerate endpoint \(x=0\).
- Do not public-stage without user request.

## Tags

`bridge`, `gamma-tilt`, `laplace-transform`, `lemma`, `levy-density`, `log-convexity`, `proved`, `strict-private-post-v016`, `tilted-variance`, `true`
