---
id: "T-Ramanujan-integral-Stieltjes"
type: "theorem"
title: "Ramanujan integral I_R is Stieltjes"
status: "proved"
tags: ["application-candidate", "complete-monotonicity", "proved", "ramanujan-integral", "source-solving", "stieltjes", "theorem"]
parents: ["T-Ramanujan-density-logsquare-CM", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private Oracle response", "private scout artifact", "private proof note", "wiki/notes/frontier-ramanujan-integral-stieltjes.md"]
---

# Theorem: Ramanujan integral I_R is Stieltjes

## Statement

The Ramanujan integral \(I_R(x)=\int_0^\infty e^{-xt}\,dt/[t(\pi^2+\log^2 t)]\) is a Stieltjes function on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Ramanujan-density-logsquare-CM|Ramanujan log square density phi zero is completely monotone]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private scout artifact`
- `private proof note`
- `wiki/notes/frontier-ramanujan-integral-stieltjes.md`

## Proof

For \(u=\log t\),
\[
\int_0^1 e^{-au}\sin(\pi a)\,da
=\frac{\pi(1+e^{-u})}{u^2+\pi^2}.
\]
Substituting \(u=\log t\) gives
\[
\int_0^1 t^{-a}\sin(\pi a)\,da
=\frac{\pi(1+t^{-1})}{\pi^2+\log^2 t}.
\]
Therefore
\[
\phi_0(t)
=\frac{1}{t(\pi^2+\log^2 t)}
=\frac{1}{\pi(1+t)}\int_0^1 t^{-a}\sin(\pi a)\,da.
\]

For \(0<a<1\), \(t^{-a}\) is completely monotone because
\[
t^{-a}=\frac1{\Gamma(a)}\int_0^\infty e^{-ts}s^{a-1}\,ds.
\]
Also \(t\mapsto(1+t)^{-1}\) is completely monotone. Complete monotonicity is closed under products and positive mixtures, and \(\sin(\pi a)>0\) on \((0,1)\). Hence \(\phi_0\) is completely monotone.

If \(\phi\) is completely monotone and
\[
F(x)=\int_0^\infty e^{-xt}\phi(t)\,dt
\]
is finite for \(x>0\), then \(F\) is Stieltjes: write \(\phi(t)=\int_0^\infty e^{-ts}\,d\mu(s)\) and use Tonelli to obtain
\[
F(x)=\int_0^\infty\frac{d\mu(s)}{x+s}.
\]
Applying this to \(\phi_0\) proves that \(I_R\) is Stieltjes.

Finally, the source already proves that
\[
\widetilde I_R(x)=a+\int_0^\infty (1-e^{-xt})\phi_0(t)\,dt
\]
is a Bernstein function. The Levy density \(\phi_0\) is completely monotone, and it satisfies the Bernstein integrability condition
\[
\int_0^\infty (1\wedge t)\phi_0(t)\,dt<\infty.
\]
The standard complete-Bernstein criterion for Levy densities therefore gives that \(\widetilde I_R\) is a complete Bernstein function.

the CM closure product positive mixture
the Stieltjes density criterion S1
the CBF Levy density CM criterion
the Ramanujan density logsquare CM
the Ramanujan integral Stieltjes
the Ramanujan antiderivative complete Bernstein

the Ramanujan Turan window CM open problem

_Proof source: `private proof note`._

## Tags

`application-candidate`, `complete-monotonicity`, `proved`, `ramanujan-integral`, `source-solving`, `stieltjes`, `theorem`
