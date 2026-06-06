---
id: "T-Sokal-GS-lambda-derivative-compression-open"
type: "theorem"
title: "Sokal generalized Stieltjes lambda derivative compression problem"
status: "proved"
tags: ["application-candidate", "derivative-test", "generalized-stieltjes", "open-problem-solved", "proved", "sokal", "solved-source-open", "source-open", "theorem"]
parents: ["T-Sokal-GS-all-lambda-derivatives-positive-combination", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["attack-plans/AP-20260531T090000-sokal-gs-lambda-derivative.json", "librarian/audits/LA-20260531T090000-sokal-gs-lambda-derivative.json", "oracle/responses/ORACLE-OS-20260531T-sokal-gs-lambda-derivative-oracle-response.md", "raw/scout/20260531T090000-sokal-gs-lambda-derivative-source.md", "raw/scout/RS-20260531T090000-sokal-gs-lambda-derivative-source.json", "raw/student/20260531T090000-sokal-gs-lambda-derivative.md", "wiki/notes/frontier-sokal-gs-lambda-derivative-compression.md"]
---

# Theorem: Sokal generalized Stieltjes lambda derivative compression problem

## Statement

For Sokal's generalized-Stieltjes derivative tests \(F^{[\lambda]}_{n,k}(x)\), find formulae expressing \(\partial_\lambda^\ell F^{[\lambda]}_{n,k}(x)\) as nonnegative linear combinations of the same test functions.

## Dependencies

- [[wiki/nodes/T-Sokal-GS-all-lambda-derivatives-positive-combination|all lambda derivatives of Sokal generalized Stieltjes tests are nonnegative lower k combinations]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `attack-plans/AP-20260531T090000-sokal-gs-lambda-derivative.json`
- `librarian/audits/LA-20260531T090000-sokal-gs-lambda-derivative.json`
- `oracle/responses/ORACLE-OS-20260531T-sokal-gs-lambda-derivative-oracle-response.md`
- `raw/scout/20260531T090000-sokal-gs-lambda-derivative-source.md`
- `raw/scout/RS-20260531T090000-sokal-gs-lambda-derivative-source.json`
- `raw/student/20260531T090000-sokal-gs-lambda-derivative.md`
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

_Proof source: `raw/student/20260531T090000-sokal-gs-lambda-derivative.md`._

## Tags

`application-candidate`, `derivative-test`, `generalized-stieltjes`, `open-problem-solved`, `proved`, `sokal`, `solved-source-open`, `source-open`, `theorem`
