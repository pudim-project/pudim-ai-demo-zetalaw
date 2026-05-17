---
id: mrw-1ac4e44cbbad
type: theorem
title: Zeta-law successor entropy and modular resolution
aliases: ["mrw-1ac4e44cbbad", "Zeta-law successor entropy and modular resolution"]
status: proved
tags: [zeta-law, theorem, proved, entropy, modular]
parents: [mrw-43596105b428, mrw-538319137c76]
refs: ["raw/20260517T155448Z-build-a-raw-pudim-wiki-for-the-zeta-law-entropy-modular-reso-bootstrap-import.md", "bootstrap/20260517T155423Z-zeta-law-pdf-extract.md"]
---

# Theorem: Zeta-law successor entropy and modular resolution

## Statement

For every \(\beta>1\), define
\[
\Sigma(\beta)=\sum_{n=1}^{\infty}\rho_\beta(n)
\log\frac{\rho_\beta(n)}{\rho_\beta(n+1)}.
\]
Then
\[
\Sigma(\beta)=
\frac{\beta}{\zeta(\beta)}
\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{k}\zeta(\beta+k),
\]
and
\[
\Sigma(\beta)=\sup_{q\ge2}B_q(\beta)=\lim_{q\to\infty}B_q(\beta).
\]

## Proof

Since
\[
\frac{\rho_\beta(n)}{\rho_\beta(n+1)}
=\left(1+\frac1n\right)^\beta,
\]
we have
\[
\Sigma(\beta)=\frac{\beta}{\zeta(\beta)}
\sum_{n=1}^{\infty}n^{-\beta}\log\left(1+\frac1n\right).
\]
For \(0<x\le1\), use
\[
\log(1+x)=\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{k}x^k
\]
with Abel limiting at \(x=1\). Absolute convergence after summation against \(n^{-\beta}\) for \(\beta>1\) gives
\[
\Sigma(\beta)=
\frac{\beta}{\zeta(\beta)}
\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{k}\zeta(\beta+k).
\]

It remains to prove the modular formula. Fix \(q\ge2\). For each residue class \(a\), the log-sum inequality gives
\[
\sum_{\substack{n\ge1\\ n\equiv a\pmod q}}
\rho_\beta(n)\log\frac{\rho_\beta(n)}{\rho_\beta(n+1)}
\ge
\mu_{q,\beta}(a)
\log\frac{\mu_{q,\beta}(a)}
{\sum_{n\equiv a\pmod q}\rho_\beta(n+1)}.
\]
If \(a\ne0\), the denominator is \(\mu_{q,\beta}(a+1)\). If \(a=0\), it is \(\mu_{q,\beta}(1)-\rho_\beta(1)\le\mu_{q,\beta}(1)\). Summing over \(a\) yields
\[
\Sigma(\beta)\ge B_q(\beta)
\]
for every \(q\ge2\), hence \(\Sigma(\beta)\ge\sup_q B_q(\beta)\).

Conversely, fix \(M\in\mathbb N\). If \(q>M+1\), then the residue classes \(1,\ldots,M+1\) isolate the first \(M+1\) integers up to tails \(O_{\beta,M}(q^{-\beta})\):
\[
\mu_{q,\beta}(a)=\rho_\beta(a)+O_{\beta,M}(q^{-\beta})
\qquad(1\le a\le M+1).
\]
Also \(\mu_{q,\beta}(0)=q^{-\beta}\). All cyclic terms in \(B_q(\beta)\) are nonnegative except possibly the boundary term
\[
\mu_{q,\beta}(0)\log\frac{\mu_{q,\beta}(0)}{\mu_{q,\beta}(1)}
=O_\beta(q^{-\beta}\log q),
\]
which tends to zero. Therefore
\[
\liminf_{q\to\infty}B_q(\beta)
\ge
\sum_{n=1}^{M}\rho_\beta(n)\log\frac{\rho_\beta(n)}{\rho_\beta(n+1)}.
\]
Letting \(M\to\infty\) gives \(\liminf_q B_q(\beta)\ge\Sigma(\beta)\). Together with \(B_q(\beta)\le\Sigma(\beta)\), this proves the claimed limit and supremum identities.

## Depends on

- [[wiki/nodes/mrw-43596105b428|Riemann zeta probability law]]
- [[wiki/nodes/mrw-538319137c76|Modular residue distribution and successor entropy]]

## Used by

- [[wiki/nodes/mrw-b3e8267d43b5|Prime-modulus Dirichlet L-resolution]]
- [[wiki/nodes/mrw-593af0548f67|Four-layer zeta-law framework]]

## Notes

- Promoted to `proved` by ingesting the proof from the original theory PDF extract.
