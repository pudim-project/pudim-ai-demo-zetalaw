---
id: "T-NagelWeissMecke-LaplaceSurvival-Poissonization-Solution"
type: "theorem"
title: "Nagel-Weiss/Mecke Laplace-survival and Poissonization constructions"
status: "proved"
tags: ["application-candidate", "laplace-transform", "open-problem-solved", "poissonization", "probability-generating-function", "proved", "source-solving", "strict-private-plus10", "survival-function", "theorem", "true"]
parents: ["O-NagelWeissMecke-LaplaceSurvival-Poissonization-source-gate", "D-LaplaceSurvivalTransform", "L-UniformExponentialRace-LaplaceSurvival", "L-CMSurvival-BernsteinWidder-InverseCriterion", "L-ConditionalPoissonization-PGF"]
refs: ["private Oracle response", "private proof note"]
---

# Theorem: Nagel-Weiss/Mecke Laplace-survival and Poissonization constructions

## Statement

The Nagel--Weiss/Mecke Laplace-survival construction problem is solved in the finite-valued source scope: if \(\mathbb P(\zeta>0)=1\), then \(\xi=(-\log U)/\zeta\) satisfies \(F_\xi(x)=1-L_\zeta(x)\) for all \(x\ge0\). For arbitrary nonnegative \(\zeta\), the same formula holds on the extended half-line by setting \(\xi=\infty\) on \(\{\zeta=0\}\), and no finite-valued solution can satisfy the literal formula when \(\mathbb P(\zeta=0)>0\). The source's probability-generating-function construction problem is solved by \(\kappa_t\mid\zeta\sim\operatorname{Poisson}(t\zeta)\), which gives \(\mathbb E[x^{\kappa_t}]=L_\zeta(t(1-x))\).

## Dependencies

- [[wiki/nodes/O-NagelWeissMecke-LaplaceSurvival-Poissonization-source-gate|Nagel-Weiss/Mecke Laplace-survival and Poissonization source gate]]
- [[wiki/nodes/D-LaplaceSurvivalTransform|Laplace-survival transform]]
- [[wiki/nodes/L-UniformExponentialRace-LaplaceSurvival|Uniform exponential race gives the Laplace-survival transform]]
- [[wiki/nodes/L-CMSurvival-BernsteinWidder-InverseCriterion|Completely monotone survival functions are Laplace transforms]]
- [[wiki/nodes/L-ConditionalPoissonization-PGF|Conditional Poissonization realizes the Laplace PGF]]

## Proof and provenance references

- `private Oracle response`
- `private proof note`

## Proof

Since \(U\) is uniform on \((0,1)\),
\[
\mathbb P(-\log U\le y)=\mathbb P(U\ge e^{-y})=1-e^{-y},\qquad y\ge0.
\]
Thus \(E=-\log U\) has the exponential distribution with rate \(1\).

Condition on \(\zeta=z\). If \(z>0\), then
\[
\mathbb P\left(\frac{E}{z}\le x\mid \zeta=z\right)
=\mathbb P(E\le xz)=1-e^{-xz}.
\]
If \(z=0\) in the extended-valued convention, then \(\xi=\infty\), so
\[
\mathbb P(\xi\le x\mid \zeta=0)=0=1-e^{-x\cdot 0}.
\]
Taking expectations gives
\[
\mathbb P(\xi\le x)
=\mathbb E[1-e^{-x\zeta}]
=1-\mathbb E e^{-x\zeta}
=1-L_\zeta(x).
\]
This proves the source's forward construction in the finite case \(\mathbb P(\zeta>0)=1\), and proves the corrected extended-valued formula for arbitrary \(\zeta\ge0\).

The atom-at-zero caveat is necessary. By bounded convergence,
\[
L_\zeta(x)=\mathbb E e^{-x\zeta}\longrightarrow \mathbb P(\zeta=0),
\]
so
\[
1-L_\zeta(x)\longrightarrow 1-\mathbb P(\zeta=0).
\]
A finite distribution function on \([0,\infty)\) must tend to \(1\). Therefore no finite-valued \(\xi\) can satisfy the literal formula for all \(x\ge0\) when \(\mathbb P(\zeta=0)>0\).

For the probability-generating-function construction, condition on \(\zeta\). If \(\kappa_t\mid \zeta\sim\operatorname{Poisson}(t\zeta)\), then
\[
\mathbb E[x^{\kappa_t}\mid\zeta]
=\exp(t\zeta(x-1))
=\exp(-t(1-x)\zeta).
\]
Therefore
\[
\mathbb E[x^{\kappa_t}]
=\mathbb E e^{-t(1-x)\zeta}
=L_\zeta(t(1-x)).
\]
This is the source's requested \(G_t(x)\).

To realize \(\kappa_t\) as a transform of \(\zeta\) and uniforms, take iid uniforms \((\eta_i)\), set \(E_i=-\log\eta_i\), \(T_n=E_1+\cdots+E_n\), and
\[
N(a)=\max\{n\ge0:T_n\le a\}.
\]
Then \(N\) is a standard Poisson process and \(\kappa_t=N(t\zeta)\) supplies the conditional Poisson draw.

The inverse criterion is exactly Bernstein--Widder: normalized completely monotone survival functions are precisely Laplace transforms of probability measures on \([0,\infty)\). It is a bridge for the source inverse problem, not a new standalone theorem.

_Proof source: `private proof note`._

## Do not claim

- Do not claim the unqualified finite-valued construction works when \(\mathbb P(\zeta=0)>0\).
- Do not count the inverse Bernstein--Widder criterion as a separate fresh APP.
- Do not claim mixed-Poisson or Bernstein--Widder theory is new.
- Do not claim public APP registry assignment.
- Do not public-stage without user request.

## Tags

`application-candidate`, `laplace-transform`, `open-problem-solved`, `poissonization`, `probability-generating-function`, `proved`, `source-solving`, `strict-private-plus10`, `survival-function`, `theorem`, `true`
