---
id: "T-YT-Bessel-W-general-zero-partial-fraction"
type: "theorem"
title: "Yang Tian Bessel W general zero partial fraction proves W_nu sqrt is Bernstein"
status: "proved"
tags: ["application-bridge", "bernstein-function", "bessel", "partial-fraction", "proved", "source-solving-tool", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-Bernstein-derivative-complete-monotonicity-criterion"]
refs: ["librarian/audits/LA-20260603T-yang-tian-bessel-w-full-conjecture.json", "raw/student/20260603T-yang-tian-bessel-w-full-conjecture.md", "wiki/notes/frontier-yang-tian-bessel-w-bernstein.md", "wiki/notes/frontier-yt-bessel-w-bernstein.md"]
---

# Theorem: Yang Tian Bessel W general zero partial fraction proves W_nu sqrt is Bernstein

## Statement

For every \(\nu>-1\), if \(j_{\nu+1,n}\) are the positive zeros of \(J_{\nu+1}\), then \(G_\nu(s)=W_\nu(\sqrt{s})\) satisfies \(G_\nu(s)=2(\nu+1)+2\sum_{n\ge1}s/(s+j_{\nu+1,n}^2)\) and \(G_\nu'(s)=2\sum_{n\ge1}j_{\nu+1,n}^2/(s+j_{\nu+1,n}^2)^2\). Consequently \(G_\nu\) is a Bernstein function on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-Bernstein-derivative-complete-monotonicity-criterion|T-Bernstein-derivative-complete-monotonicity-criterion]]

## Proof and provenance references

- `librarian/audits/LA-20260603T-yang-tian-bessel-w-full-conjecture.json`
- `raw/student/20260603T-yang-tian-bessel-w-full-conjecture.md`
- `wiki/notes/frontier-yang-tian-bessel-w-bernstein.md`
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

`application-bridge`, `bernstein-function`, `bessel`, `partial-fraction`, `proved`, `source-solving-tool`, `theorem`
