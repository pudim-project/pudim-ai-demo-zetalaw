---
id: mrw-a034fa3c9d7f
type: lemma
title: Uniform positive-axis curvature bound
aliases: ["mrw-a034fa3c9d7f", "Uniform positive-axis curvature bound"]
status: partial
tags: [zeta-law, lemma, partial, curvature]
parents: [mrw-1435777561a8]
refs: ["raw/20260517T155448Z-build-a-raw-pudim-wiki-for-the-zeta-law-entropy-modular-reso-bootstrap-import.md"]
---

# Lemma: Uniform positive-axis curvature bound

## Statement

The imported PDF states that for every \(s\ge3\),
\[
(\log\zeta)''(s)=\operatorname{Var}_s(\log N)<\frac13.
\]

## Evidence

The proof bounds \((\log\zeta)''(s)\le \zeta''(s)\), then estimates
\[
\zeta''(s)=\sum_{m=2}^{\infty}\frac{(\log m)^2}{m^s}
\le \sum_{m=2}^{\infty}\frac{(\log m)^2}{m^3}
\]
by a decreasing-function integral comparison.

## Depends on

- [[wiki/nodes/mrw-1435777561a8|Zeta free energy]]

## Used by

- [[wiki/nodes/mrw-6b7d94a697d7|Alzer-Kwong convexity and concavity pattern for reciprocal zeta]]

## Notes

- This should be audited carefully; it is the key curvature input for the Alzer-Kwong application.
