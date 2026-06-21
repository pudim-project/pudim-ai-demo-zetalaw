---
id: "L-CMSurvival-BernsteinWidder-InverseCriterion"
type: "lemma"
title: "Completely monotone survival functions are Laplace transforms"
status: "proved"
tags: ["bernstein-widder", "bridge-lemma", "complete-monotonicity", "inverse-criterion", "laplace-transform", "lemma", "prior-art-bridge", "proved", "true"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-positive-Laplace-kernel-complete-monotonicity-principle"]
refs: ["private proof note"]
---

# Lemma: Completely monotone survival functions are Laplace transforms

## Statement

A function \(S:[0,\infty)\to[0,1]\) is the Laplace transform of a probability measure on \([0,
+\infty)\) exactly when \(S(0)=1\), \(S\) is completely monotone on \((0,\infty)\), and the usual right-continuity/normalization conditions hold. Thus a survival function \(S=1-F_\xi\) has a nonnegative Laplace-transform inverse law precisely under this Bernstein--Widder condition.

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]

## Proof and provenance references

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

- Do not claim Bernstein--Widder is new.
- Use this only as bridge material for the source inverse question.

## Tags

`bernstein-widder`, `bridge-lemma`, `complete-monotonicity`, `inverse-criterion`, `laplace-transform`, `lemma`, `prior-art-bridge`, `proved`, `true`
