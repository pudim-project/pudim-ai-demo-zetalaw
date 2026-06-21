---
id: "T-Sokal-GS-order-monotonicity-direct-triangular-formula"
type: "theorem"
title: "Sokal generalized Stieltjes test conditions weaken with order by positive triangular transform"
status: "proved"
tags: ["bridge-patch", "generalized-stieltjes", "order-monotonicity", "positive-coefficients", "proved", "sokal", "theorem"]
parents: ["T-Sokal-GS-lambda-derivative-generating-function", "D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Determinant-triangular-compression-language"]
refs: ["private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-sokal-gs-lambda-derivative-compression.md"]
---

# Theorem: Sokal generalized Stieltjes test conditions weaken with order by positive triangular transform

## Statement

For \(\tau\ge0\), Sokal's tests satisfy \(F^{[\lambda+\tau]}_{n,k}(x)=k!\sum_{r=0}^{k}F^{[\lambda]}_{n,r}(x)[z^{k-r}](1-z)^{-\tau}/r!\), so nonnegativity of all order-\(\lambda\) tests directly implies nonnegativity of all order-\(\lambda+\tau\) tests.

## Dependencies

- [[wiki/nodes/T-Sokal-GS-lambda-derivative-generating-function|Sokal generalized Stieltjes tests have formal exponential generating function in k]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Determinant-triangular-compression-language|Determinant and triangular compression language]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `wiki/notes/frontier-sokal-gs-lambda-derivative-compression.md`

## Proof

Fix \(n\ge0\), \(x>0\), and write \(a=n+\lambda\). For this proof \(f\) is fixed and only the coefficients depend on \(\lambda\). Put
\[
G_j(x)=(-1)^n x^j f^{(n+j)}(x).
\]
Then Sokal's test can be written as
\[
F^{[\lambda]}_{n,k}(x)
=
\sum_{j=0}^k \binom{k}{j}(a+j)_{k-j}G_j(x),
\]
where \((u)_m=\Gamma(u+m)/\Gamma(u)\).

Consider the exponential generating series in the formal variable \(z\):
\[
\mathcal F(z)
=
\sum_{k\ge0}F^{[\lambda]}_{n,k}(x)\frac{z^k}{k!}.
\]
Coefficient extraction is finite in each degree, so this is a formal identity. Interchanging the finite coefficient contributions gives
\[
\begin{aligned}
\mathcal F(z)
&=\sum_{k\ge0}\sum_{j=0}^k
\binom{k}{j}(a+j)_{k-j}G_j(x)\frac{z^k}{k!}\\
&=\sum_{j\ge0}G_j(x)\frac{z^j}{j!}
\sum_{m\ge0}(a+j)_m\frac{z^m}{m!}\\
&=\sum_{j\ge0}G_j(x)\frac{z^j}{j!}(1-z)^{-a-j}\\
&=(1-z)^{-a}\sum_{j\ge0}G_j(x)
\frac{(z/(1-z))^j}{j!}.
\end{aligned}
\]
Since \(a=n+\lambda\), differentiating with respect to \(\lambda\) gives
\[
\partial_\lambda \mathcal F(z)
=
-\log(1-z)\mathcal F(z).
\]
But
\[
-\log(1-z)=\sum_{m\ge1}\frac{z^m}{m},
\]
so comparison of coefficients of \(z^k\) yields
\[
\frac{\partial_\lambda F^{[\lambda]}_{n,k}(x)}{k!}
=
\sum_{r=0}^{k-1}
\frac{F^{[\lambda]}_{n,r}(x)}{r!}\frac1{k-r}.
\]
Multiplying by \(k!\) proves the first-derivative formula:
\[
\partial_\lambda F^{[\lambda]}_{n,k}(x)
=
\sum_{r=0}^{k-1}\frac{k!}{r!(k-r)}
F^{[\lambda]}_{n,r}(x).
\]
The \(k=0\) case gives \(0\), as expected.

For higher derivatives, the same generating-function identity gives
\[
\partial_\lambda^\ell \mathcal F(z)
=
(-\log(1-z))^\ell \mathcal F(z).
\]
Thus
\[
\frac{\partial_\lambda^\ell F^{[\lambda]}_{n,k}(x)}{k!}
=
\sum_{r=0}^{k}
\frac{F^{[\lambda]}_{n,r}(x)}{r!}
[z^{k-r}](-\log(1-z))^\ell.
\]
Since \(-\log(1-z)\) starts with \(z\), the coefficient is zero unless \(k-r\ge\ell\), giving the displayed sum over \(0\le r\le k-\ell\).

All coefficients are nonnegative because \(-\log(1-z)=\sum_{m\ge1}z^m/m\) has strictly positive Taylor coefficients, and products of power series with nonnegative coefficients have nonnegative coefficients. Therefore every \(\lambda\)-derivative of a Sokal test is a nonnegative linear combination of lower-\(k\) tests.

The same generating function gives an integrated order-monotonicity formula. For \(\tau\ge0\),
\[
\mathcal F_{\lambda+\tau}(z)
=
(1-z)^{-\tau}\mathcal F_\lambda(z),
\]
and hence
\[
F^{[\lambda+\tau]}_{n,k}(x)
=
k!\sum_{r=0}^{k}
\frac{F^{[\lambda]}_{n,r}(x)}{r!}
[z^{k-r}](1-z)^{-\tau}.
\]
Since \([z^m](1-z)^{-\tau}=(\tau)_m/m!\ge0\), nonnegativity of the order-\(\lambda\) tests implies nonnegativity of the order-\(\lambda+\tau\) tests by a direct triangular formula.

_Proof source: `private proof note`._

## Tags

`bridge-patch`, `generalized-stieltjes`, `order-monotonicity`, `positive-coefficients`, `proved`, `sokal`, `theorem`
