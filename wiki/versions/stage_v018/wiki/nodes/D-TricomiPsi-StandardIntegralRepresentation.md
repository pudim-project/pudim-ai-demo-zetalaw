---
id: "D-TricomiPsi-StandardIntegralRepresentation"
type: "definition"
title: "Tricomi Psi standard Laplace integral representation"
status: "proved"
tags: ["complete-monotonicity", "definition", "hypergeometric", "laplace-transform", "proved", "source-vocabulary", "strict-private-post-v016", "tricomi", "true"]
parents: ["O-TricomiPsiQuotient-CM-c-window-source-gate", "D-Laplace-kernel-and-tilted-moment-language"]
refs: ["oracle/responses/OS-20260620T1832Z-tricomi-psi-quotient-oracle-response.md", "raw/student/20260620T1840-tricomi-psi-quotient-counterexample.md"]
---

# Definition: Tricomi Psi standard Laplace integral representation

## Statement

For \(a>0\) and \(z>0\), the Tricomi confluent hypergeometric function satisfies \(\Psi(a,c,z)=\Gamma(a)^{-1}\int_0^\infty e^{-zt}t^{a-1}(1+t)^{c-a-1}\,dt\) whenever the displayed integral is interpreted in the source's standard admissible range. In particular, for the integer parameters used in the counterexample, the integral is an elementary positive Laplace integral.

## Dependencies

- [[wiki/nodes/O-TricomiPsiQuotient-CM-c-window-source-gate|Tricomi Psi quotient complete monotonicity c-window source gate]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `oracle/responses/OS-20260620T1832Z-tricomi-psi-quotient-oracle-response.md`
- `raw/student/20260620T1840-tricomi-psi-quotient-counterexample.md`

## Tags

`complete-monotonicity`, `definition`, `hypergeometric`, `laplace-transform`, `proved`, `source-vocabulary`, `strict-private-post-v016`, `tricomi`, `true`
