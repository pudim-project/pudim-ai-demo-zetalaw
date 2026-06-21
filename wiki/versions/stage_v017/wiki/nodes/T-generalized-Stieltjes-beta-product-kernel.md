---
id: "T-generalized-Stieltjes-beta-product-kernel"
type: "theorem"
title: "beta identity represents product of generalized Stieltjes kernels as order-sum kernel mixture"
status: "proved"
tags: ["beta-kernel", "bridge-patch", "generalized-stieltjes", "product-closure", "proved", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-Complete-monotonicity-closure-calculus-principle"]
refs: ["private librarian audit", "private Oracle response", "private scout artifact", "private proof note", "wiki/definitions/generalized-stieltjes-bernstein-order.md"]
---

# Theorem: beta identity represents product of generalized Stieltjes kernels as order-sum kernel mixture

## Statement

For \(\alpha,\beta>0\), \(s,t\ge0\), and \(x>0\), the product \((x+s)^{-\alpha}(x+t)^{-\beta}\) has the beta-mixture representation with kernel \((x+us+(1-u)t)^{-(\alpha+\beta)}\).

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private scout artifact`
- `private proof note`
- `wiki/definitions/generalized-stieltjes-bernstein-order.md`

## Proof

For \(\lambda>0\), a smooth positive function \(f\) belongs to \(\mathcal B_\lambda\) if
\[
x^{1-\lambda}f'(x)
\]
is completely monotone.

Koumandos--Pedersen prove that if \(f\in\mathcal B_\lambda\), then
\[
\frac{f(x)}{x^\lambda}
\]
is completely monotone.

For \(\lambda>0\), a function \(g\) belongs to \(\mathcal S_\lambda\) if
\[
g(x)=c+\int_0^\infty \frac{d\mu(t)}{(x+t)^\lambda},
\]
or equivalently
\[
g(x)=c+\int_0^\infty e^{-xt}t^{\lambda-1}\phi(t)\,dt
\]
with \(\phi\) completely monotone.

The product closure is
\[
\mathcal S_{\lambda_1}\mathcal S_{\lambda_2}\subseteq\mathcal S_{\lambda_1+\lambda_2}.
\]

For Sokal's generalized-Stieltjes tests
\[
F^{[\lambda]}_{n,k}(x)
=
(-1)^n
\sum_{j=0}^{k}\binom{k}{j}
\frac{\Gamma(n+k+\lambda)}{\Gamma(n+j+\lambda)}
x^j f^{(n+j)}(x),
\]
the formal exponential generating function in \(k\) is
\[
\sum_{k\ge0}F^{[\lambda]}_{n,k}(x)\frac{z^k}{k!}
=
(1-z)^{-(n+\lambda)}
(-1)^n
\sum_{j\ge0}x^j f^{(n+j)}(x)\frac{(z/(1-z))^j}{j!}.
\]
Thus
\[
\partial_\lambda^\ell F^{[\lambda]}_{n,k}(x)
=
\sum_{r=0}^{k-\ell}
\frac{k!}{r!}[z^{k-r}](-\log(1-z))^\ell
F^{[\lambda]}_{n,r}(x),
\]
with nonnegative coefficients. The integrated form is
\[
F^{[\lambda+\tau]}_{n,k}(x)
=
k!\sum_{r=0}^k
\frac{F^{[\lambda]}_{n,r}(x)}{r!}
[z^{k-r}](1-z)^{-\tau},
\qquad \tau\ge0,
\]
which directly realizes the weakening of Sokal's test conditions as the order grows.

For pure transforms, the local kernel proof uses
\[
(x+s)^{-\alpha}(x+t)^{-\beta}
=
\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}
\int_0^1
\frac{u^{\alpha-1}(1-u)^{\beta-1}}
{\bigl(x+us+(1-u)t\bigr)^{\alpha+\beta}}
\,du.
\]
Thus the representing measure for a product is the beta pushforward of
\[
d\mu(s)\,d\nu(t)\,u^{\alpha-1}(1-u)^{\beta-1}\,du
\]
under \((s,t,u)\mapsto us+(1-u)t\), with the normalizing factor
\[
\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}.
\]

If \(f_j\in\mathcal B_{\lambda_j}\), then
\[
\frac{(f_1f_2)'(x)}{x^{\lambda_1+\lambda_2-1}}
=
\frac{f_1'(x)}{x^{\lambda_1-1}}\frac{f_2(x)}{x^{\lambda_2}}
+
\frac{f_1(x)}{x^{\lambda_1}}\frac{f_2'(x)}{x^{\lambda_2-1}},
\]
so \(f_1f_2\in\mathcal B_{\lambda_1+\lambda_2}\) by complete-monotone product and positive-sum closure.

Koumandos--Pedersen define \(f\in\mathcal C_\alpha\) when \(x^\alpha f(x)\) is the Laplace transform of a decreasing logarithmically convex function. They prove
\[
f\in\mathcal C_\alpha\Longrightarrow \frac1f\in\mathcal B_{\alpha+1},
\]
and also that
\[
\frac{1}{x^{\alpha+1}f(x)}
\]
is completely monotone.

_Proof source: `wiki/definitions/generalized-stieltjes-bernstein-order.md`._

## Tags

`beta-kernel`, `bridge-patch`, `generalized-stieltjes`, `product-closure`, `proved`, `theorem`
