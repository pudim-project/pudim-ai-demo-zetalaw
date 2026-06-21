---
id: "L-Nonnegative-ID-Poisson-Mixture-DID"
type: "lemma"
title: "Nonnegative infinitely divisible Poisson mixtures are DID"
status: "proved"
tags: ["bridge-result", "compound-poisson", "discrete-infinite-divisibility", "lemma", "pgf", "poisson-mixture", "proved"]
parents: ["T-positive-Laplace-kernel-complete-monotonicity-principle", "T-Complete-monotonicity-closure-calculus-principle"]
refs: ["private Oracle response", "private proof note"]
---

# Lemma: Nonnegative infinitely divisible Poisson mixtures are DID

## Statement

If \(U\) is an infinitely divisible probability law supported on \([0,\infty)\), then the mixed Poisson law with PGF \(P_U(z)=\int_0^\infty e^{-\lambda(1-z)}\,U(d\lambda)\) is discretely infinitely divisible.

## Dependencies

- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `private Oracle response`
- `private proof note`

## Proof

\[
U\text{ infinitely divisible and supported on }[0,\infty)
\quad\Longrightarrow\quad
\operatorname{PoissonMix}(U)\text{ is DID}.
\]

Let \(U\) be a probability law supported on \([0,\infty)\), and suppose \(U\) is infinitely divisible as a real-valued law. Let
\[
P_U(z)=\int_0^\infty e^{-\lambda(1-z)}\,U(d\lambda)
\]
be the PGF of the mixed Poisson law.

For every \(n\ge1\), choose \(U_n\) with
\[
U=U_n^{*n}.
\]
Since \(U\) is supported on \([0,\infty)\), each \(U_n\) is also supported on \([0,\infty)\). Indeed, if \(U_n\) had support at some negative \(x\), then \(n\) independent draws in a small neighborhood of \(x\) would give \(U_n^{*n}\) positive mass on a negative interval, contradicting the support of \(U\).

Therefore
\[
P_{U_n}(z)=\int_0^\infty e^{-\lambda(1-z)}\,U_n(d\lambda)
\]
is a PGF, and by multiplicativity of Laplace transforms,
\[
P_U(z)=P_{U_n}(z)^n.
\]
Thus \(P_U\) has a PGF \(n\)-th root for every \(n\), so the mixed Poisson law is discretely infinitely divisible.

Equivalently, if \(L(s)=e^{-\phi(s)}\) is the Laplace transform of the nonnegative infinitely divisible law \(U\), then
\[
\phi(s)=ds+\int_{(0,\infty)}(1-e^{-sx})\,\Pi(dx).
\]
For \(P(z)=L(1-z)\),
\[
\log P(z)=\sum_{k\ge1}q_k(z^k-1),
\]
where
\[
q_k=d\,\mathbf 1_{k=1}+\int_{(0,\infty)}e^{-x}\frac{x^k}{k!}\,\Pi(dx)\ge0,
\]
and
\[
\sum_{k\ge1}q_k=d+\int_{(0,\infty)}(1-e^{-x})\,\Pi(dx)<\infty.
\]
This is the compound-Poisson coefficient form.

Townes's real-valued mixing framework uses the bilateral Laplace transform condition on a finite interval:
\[
L_X(t)=\mathbb E(e^{-tX})\quad\text{is completely monotone on }[0,1].
\]
This condition makes \(G_Y(z)=L_X(1-z)\) a PGF, but it does not force \(X\) to be supported on \([0,\infty)\). The direct root proof above needs support on \([0,\infty)\) for every convolution root. The subordinator proof also needs the one-sided Levy-Khintchine representation, which is exactly unavailable in the real-valued case.

Therefore the actual Townes problem remains:

\[
X\text{ real-valued ID},\quad L_X\text{ CM on }[0,1]
\quad\Longrightarrow ?\quad
L_X(1-z)\text{ is DID}.
\]

_Proof source: `private proof note`._

## Do not claim

- Do not use this lemma to solve the real-valued finite-interval BLT Townes conjecture.
- Do not infer support on [0,infty] from complete monotonicity only on [0,1].

## Tags

`bridge-result`, `compound-poisson`, `discrete-infinite-divisibility`, `lemma`, `pgf`, `poisson-mixture`, `proved`
