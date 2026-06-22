---
id: "L-ConditionalPoissonization-PGF"
type: "lemma"
title: "Conditional Poissonization realizes the Laplace PGF"
status: "proved"
tags: ["bridge-lemma", "laplace-transform", "lemma", "poissonization", "prior-art-bridge", "probability-generating-function", "proved", "true"]
parents: ["D-Laplace-kernel-and-tilted-moment-language", "D-LaplaceSurvivalTransform"]
refs: ["oracle/responses/OS-20260614T0315Z-oracle-response.md", "raw/student/20260614T0315-nagel-weiss-mecke-laplace-survival-poissonization.md"]
---

# Lemma: Conditional Poissonization realizes the Laplace PGF

## Statement

Let \(\zeta\ge0\) and, for \(t>0\), let \(\kappa_t\mid\zeta\sim\operatorname{Poisson}(t\zeta)\). Then \(\kappa_t\) is nonnegative integer-valued and \(\mathbb E[x^{\kappa_t}]=L_\zeta(t(1-x))\) for every \(0\le x\le1\). The conditional Poisson draw can be realized from iid uniforms by the usual exponential-interarrival construction of a Poisson process.

## Dependencies

- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]
- [[wiki/nodes/D-LaplaceSurvivalTransform|Laplace-survival transform]]

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

## Do not claim

- Do not claim mixed-Poisson or Cox construction theory is new.
- Use this as a source-specific construction and bridge lemma.

## Tags

`bridge-lemma`, `laplace-transform`, `lemma`, `poissonization`, `prior-art-bridge`, `probability-generating-function`, `proved`, `true`
