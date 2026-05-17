---
id: mrw-e71e57d7cbd0
type: definition
title: Mellin-Planck partition function
aliases: ["mrw-e71e57d7cbd0", "Mellin-Planck partition function"]
status: proved
tags: [zeta-law, definition, proved, mellin, holder]
parents: []
refs: []
---

# Definition: Mellin-Planck partition function

## Statement

For \(s>1\), define
\[
M(s)=\Gamma(s)\zeta(s)=\int_0^\infty \frac{t^{s-1}}{e^t-1}\,dt.
\]
The associated probability law is
\[
\nu_s(dt)=\frac{t^{s-1}}{(e^t-1)M(s)}\,dt.
\]

## Proof

This records the standard Mellin transform identity for \(\Gamma(s)\zeta(s)\) and the normalized density used in the PDF.

## Depends on

## Used by

- [[wiki/nodes/mrw-8aa5f1703758|Generalized Holder inequality for Gamma zeta]]
- [[wiki/nodes/mrw-593af0548f67|Four-layer zeta-law framework]]

## Notes

- The PDF uses \(M\) as a continuous partition function whose log-convexity yields the Holder application.
