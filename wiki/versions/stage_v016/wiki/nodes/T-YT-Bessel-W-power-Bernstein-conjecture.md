---
id: "T-YT-Bessel-W-power-Bernstein-conjecture"
type: "theorem"
title: "Yang Tian Conjecture 3 Bessel W_nu x^tau Bernstein for tau in (0,1/2], nu > -1"
status: "proved"
tags: ["application-candidate", "bernstein", "bessel", "complete-monotonicity", "forage", "fresh-author", "proved", "source-open-solved", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-YT-Bessel-W-general-zero-partial-fraction"]
refs: ["librarian/audits/LA-20260528T140000-yt-bessel-w-attack-plan.json", "librarian/audits/LA-20260603T-yang-tian-bessel-w-full-conjecture.json", "raw/scout/sources/yang-tian-bessel-w-bernstein-conjecture.md", "raw/student/20260603T-yang-tian-bessel-w-full-conjecture.md", "scout/forage/inbox/FI-20260528T-next-loop-010.json", "wiki/notes/frontier-yt-bessel-w-bernstein.md"]
---

# Theorem: Yang Tian Conjecture 3 Bessel W_nu x^tau Bernstein for tau in (0,1/2], nu > -1

## Statement

For \(\tau\in(0,1/2]\) and \(\nu>-1\), prove that \(x\mapsto W_\nu(x^\tau)\), where \(W_\nu(x)=xI_\nu(x)/I_{\nu+1}(x)\), is a Bernstein function on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-YT-Bessel-W-general-zero-partial-fraction|Yang Tian Bessel W general zero partial fraction proves W_nu sqrt is Bernstein]]

## Proof and provenance references

- `librarian/audits/LA-20260528T140000-yt-bessel-w-attack-plan.json`
- `librarian/audits/LA-20260603T-yang-tian-bessel-w-full-conjecture.json`
- `raw/scout/sources/yang-tian-bessel-w-bernstein-conjecture.md`
- `raw/student/20260603T-yang-tian-bessel-w-full-conjecture.md`
- `scout/forage/inbox/FI-20260528T-next-loop-010.json`
- `wiki/notes/frontier-yt-bessel-w-bernstein.md`

## Proof

Put \(\mu=\nu+1>0\). The canonical product for the modified Bessel function gives, locally uniformly in \(z\),
\[
I_\mu(z)=\frac{(z/2)^\mu}{\Gamma(\mu+1)}
\prod_{n=1}^{\infty}\left(1+\frac{z^2}{j_{\mu,n}^2}\right),
\]
where \(j_{\mu,n}\) are the positive zeros of \(J_\mu\). Therefore
\[
z\frac{I_\mu'(z)}{I_\mu(z)}
=\mu+2\sum_{n=1}^{\infty}\frac{z^2}{z^2+j_{\mu,n}^2}.
\]
The recurrence
\[
I_\mu'(z)=I_{\mu-1}(z)-\frac{\mu}{z}I_\mu(z)
\]
then yields
\[
W_\nu(z)
=z\frac{I_{\mu-1}(z)}{I_\mu(z)}
=2\mu+2\sum_{n=1}^{\infty}\frac{z^2}{z^2+j_{\mu,n}^2}.
\]

Set \(s=z^2\). Then
\[
G_\nu(s):=W_\nu(\sqrt s)
=2(\nu+1)+2\sum_{n=1}^{\infty}\frac{s}{s+j_{\nu+1,n}^2}.
\]

Termwise differentiation is justified because \(j_{\nu+1,n}\sim \pi n\), so the differentiated sums converge locally uniformly on \((0,\infty)\). Thus
\[
G_\nu'(s)
=2\sum_{n=1}^{\infty}
\frac{j_{\nu+1,n}^2}{(s+j_{\nu+1,n}^2)^2}.
\]
For every \(k\ge0\),
\[
(-1)^k\frac{d^k}{ds^k}
\frac{j_{\nu+1,n}^2}{(s+j_{\nu+1,n}^2)^2}
=
(k+1)!\frac{j_{\nu+1,n}^2}{(s+j_{\nu+1,n}^2)^{k+2}}
\ge0.
\]
The locally uniformly convergent sum preserves these inequalities, hence \(G_\nu'\) is completely monotone and \(G_\nu\) is a Bernstein function.

If \(0<\tau\le1/2\), then \(x^{2\tau}\) is a Bernstein function. By Bernstein-function composition closure,
\[
x\mapsto W_\nu(x^\tau)=G_\nu(x^{2\tau})
\]
is a Bernstein function on \((0,\infty)\).

_Proof source: `raw/student/20260603T-yang-tian-bessel-w-full-conjecture.md`._

## Tags

`application-candidate`, `bernstein`, `bessel`, `complete-monotonicity`, `forage`, `fresh-author`, `proved`, `source-open-solved`, `theorem`
