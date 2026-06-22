---
id: "L-UniformExponentialRace-LaplaceSurvival"
type: "lemma"
title: "Uniform exponential race gives the Laplace-survival transform"
status: "proved"
tags: ["bridge-lemma", "exponential-race", "laplace-transform", "lemma", "probability-kernel", "proved", "survival-function", "true"]
parents: ["D-LaplaceSurvivalTransform", "D-Laplace-kernel-and-tilted-moment-language"]
refs: ["oracle/responses/OS-20260614T0315Z-oracle-response.md", "raw/student/20260614T0315-nagel-weiss-mecke-laplace-survival-poissonization.md"]
---

# Lemma: Uniform exponential race gives the Laplace-survival transform

## Statement

Let \(U\sim\operatorname{Unif}(0,1)\) be independent of a nonnegative random variable \(\zeta\), and set \(E=-\log U\). If \(\mathbb P(\zeta>0)=1\), then \(\xi=E/\zeta\) is finite and satisfies \(\mathbb P(\xi\le x)=1-L_\zeta(x)\) for every \(x\ge0\). For arbitrary \(\zeta\ge0\), the same equality holds for finite \(x\) under the extended convention \(\xi=\infty\) on \(\{\zeta=0\}\).

## Dependencies

- [[wiki/nodes/D-LaplaceSurvivalTransform|Laplace-survival transform]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `oracle/responses/OS-20260614T0315Z-oracle-response.md`
- `raw/student/20260614T0315-nagel-weiss-mecke-laplace-survival-poissonization.md`

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

_Proof source: `raw/student/20260614T0315-nagel-weiss-mecke-laplace-survival-poissonization.md`._

## Tags

`bridge-lemma`, `exponential-race`, `laplace-transform`, `lemma`, `probability-kernel`, `proved`, `survival-function`, `true`
