---
id: "T-Guo-ASCM-SCM-DerivativeComposition-NoCondition"
type: "theorem"
title: "Guo ASCM/SCM derivative composition without the growth condition"
status: "proved"
tags: ["ASCM", "SCM", "complete-monotonicity", "composition", "faa-di-bruno", "guo", "proved", "strict-private-app", "theorem", "true"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Log-function-derivative-chain-language", "T-Complete-monotonicity-closure-calculus-principle"]
refs: ["raw/student/20260613T0615-guo-ascm-scm-condition-waiver-proof.md", "raw/student/20260614T-v016-guo-ascm-public.md"]
---

# Theorem: Guo ASCM/SCM derivative composition without the growth condition

## Statement

Let \(I^+\) and \(I_1^+\) be open intervals contained in \((0,\infty)\). If \(f'\ge0\), \(f'\in ASCM(I_1^+)\), \(g'\in SCM(I^+)\), and \(R(g)\subset I_1^+\), then \((f\circ g)'\in ASCM(I^+)\). Therefore the condition \(2xg'(x)\ge g(x)\) in Guo's Theorem 45 can be waived.

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Log-function-derivative-chain-language|Log-function derivative-sign regions]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `raw/student/20260613T0615-guo-ascm-scm-condition-waiver-proof.md`
- `raw/student/20260614T-v016-guo-ascm-public.md`

## Proof

Set \(F=f'\), \(u=g'\), and
\[
H=(f\circ g)'=F(g)u.
\]
For \(H\in ASCM(I^+)\), it is enough to show that for every \(m\ge2\),
\[
B_m(x):=(-1)^{m-1}x^m(f\circ g)^{(m)}(x)
\]
is nonnegative and decreasing on \(I^+\). This is the ASCM condition for \(H\), with \(m=n+1\).

Faà di Bruno's formula gives
\[
(f\circ g)^{(m)}(x)
=
\sum_{\Lambda_m}
\frac{m!}{i_1!\cdots i_m!}\,
f^{(k)}(g(x))
\prod_{j=1}^m
\left(\frac{g^{(j)}(x)}{j!}\right)^{i_j},
\]
where
\[
\Lambda_m=\left\{(i_1,\ldots,i_m)\in\mathbb N_0^m:\sum_{j=1}^m j i_j=m\right\},
\qquad
k=\sum_{j=1}^m i_j.
\]

For each \(j\ge1\), since \(u=g'\in SCM(I^+)\), the function
\[
G_j(x):=\frac{(-1)^{j-1}x^j g^{(j)}(x)}{j!}
=\frac{(-1)^{j-1}x^j u^{(j-1)}(x)}{j!}
\]
is nonnegative and decreasing. In particular, \(g'\ge0\), so \(g\) is increasing.

For the \(f\)-factor, first take \(k=1\). Then \(f^{(1)}(g(x))=F(g(x))\). The hypothesis \(F\ge0\) gives nonnegativity, and \(F\in ASCM\) gives \(-y^2F'(y)\ge0\), hence \(F'\le0\). Since \(g\) is increasing, \(F(g(x))\) is nonnegative and decreasing.

For \(k\ge2\), the ASCM condition for \(F\) gives
\[
A_k(y):=(-1)^{k-1}y^k f^{(k)}(y)
=(-1)^{k-1}y^k F^{(k-1)}(y)
\]
nonnegative and decreasing on \(I_1^+\). Therefore
\[
(-1)^{k-1}f^{(k)}(y)=A_k(y)y^{-k}
\]
is also nonnegative and decreasing, because it is the product of two nonnegative decreasing functions. Composing with the increasing function \(g\), the function
\[
(-1)^{k-1}f^{(k)}(g(x))
\]
is nonnegative and decreasing on \(I^+\).

Now fix a term in the Faà di Bruno sum. The sign exponent satisfies
\[
(k-1)+\sum_{j=1}^m (j-1)i_j
=
(k-1)+(m-k)=m-1,
\]
and the \(x\)-weights satisfy
\[
\prod_{j=1}^m x^{j i_j}=x^m.
\]
Hence
\[
(-1)^{m-1}x^m
f^{(k)}(g(x))
\prod_{j=1}^m
\left(\frac{g^{(j)}(x)}{j!}\right)^{i_j}
\]
is a positive numerical coefficient times
\[
\left[(-1)^{k-1}f^{(k)}(g(x))\right]
\prod_{j=1}^m G_j(x)^{i_j}.
\]
Every factor is nonnegative and decreasing. Products and finite sums of nonnegative decreasing functions are nonnegative and decreasing. Thus \(B_m\) is nonnegative and decreasing for every \(m\ge2\).

Therefore \(H=(f\circ g)'\in ASCM(I^+)\). The source condition \(2xg'(x)\ge g(x)\) is unnecessary for Theorem 45.

_Proof source: `raw/student/20260613T0615-guo-ascm-scm-condition-waiver-proof.md`._

## Do not claim

- Do not extend this to the non-derivative composition statements.
- Do not claim \(f'\circ g\in ASCM\).
- Do not public-stage without user request.

## Tags

`ASCM`, `SCM`, `complete-monotonicity`, `composition`, `faa-di-bruno`, `guo`, `proved`, `strict-private-app`, `theorem`, `true`
