---
id: mrw-a034fa3c9d7f
type: lemma
title: Uniform positive-axis curvature bound
aliases: ["mrw-a034fa3c9d7f", "Uniform positive-axis curvature bound"]
status: proved
tags: [zeta-law, lemma, proved, curvature]
parents: [mrw-1435777561a8]
refs: ["raw/20260517T155448Z-build-a-raw-pudim-wiki-for-the-zeta-law-entropy-modular-reso-bootstrap-import.md", "bootstrap/20260517T155423Z-zeta-law-pdf-extract.md"]
---

# Lemma: Uniform positive-axis curvature bound

## Statement

For every \(s\ge3\),
\[
(\log\zeta)''(s)=\operatorname{Var}_s(\log N)<\frac13.
\]

## Proof

By the zeta free-energy identity,
\[
(\log\zeta)''(s)
=\frac{\zeta''(s)}{\zeta(s)}
-\left(\frac{\zeta'(s)}{\zeta(s)}\right)^2
\le \frac{\zeta''(s)}{\zeta(s)}
\le \zeta''(s).
\]
For \(s\ge3\),
\[
\zeta''(s)=\sum_{m=2}^{\infty}\frac{(\log m)^2}{m^s}
\le
\sum_{m=2}^{\infty}\frac{(\log m)^2}{m^3}.
\]
The function \(x\mapsto(\log x)^2x^{-3}\) is decreasing for \(x\ge2\), so
\[
\sum_{m=2}^{\infty}\frac{(\log m)^2}{m^3}
\le
\frac{(\log2)^2}{8}
+\int_2^\infty\frac{(\log x)^2}{x^3}\,dx.
\]
A direct integration gives
\[
\int_2^\infty\frac{(\log x)^2}{x^3}\,dx
=\frac{(\log2)^2+\log2+\frac12}{8}.
\]
Thus
\[
(\log\zeta)''(s)
\le
\frac{2(\log2)^2+\log2+\frac12}{8}
<\frac13.
\]

## Depends on

- [[wiki/nodes/mrw-1435777561a8|Zeta free energy]]

## Used by

- [[wiki/nodes/mrw-6b7d94a697d7|Alzer-Kwong convexity and concavity pattern for reciprocal zeta]]

## Notes

- Promoted to `proved` by ingesting the original theory proof. This is the positive-axis curvature input for the reciprocal-zeta application.
