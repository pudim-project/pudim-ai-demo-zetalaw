---
id: "L-ScalarPowerMean-Ratio-Endpoint"
type: "lemma"
title: "Scalar power-mean ratio endpoint"
status: "proved"
tags: ["bridge-lemma", "endpoint-obstruction", "finite-certificate", "lemma", "matrix-means", "proved", "ratio-bound", "scalar-power-mean", "true"]
parents: ["D-ScalarPowerMean-2Point", "D-Endpoint-obstruction-certificate-language", "T-Pointwise-obstruction-certificate-principle"]
refs: ["private librarian audit", "private Oracle response", "private proof note", "private proof note"]
---

# Lemma: Scalar power-mean ratio endpoint

## Statement

For \(0<p<q\) and \(a,b\ge0\), not both zero, the two-point scalar power means satisfy \(1\le M_q(a,b)/M_p(a,b)\le2^{1/p-1/q}\). In particular, any positive scalar solution of the two-equation \((p,q)\)-power-mean inverse problem with scalar data \(X,Y>0\) must satisfy \(Y/X\le2^{1/p-1/q}\).

## Dependencies

- [[wiki/nodes/D-ScalarPowerMean-2Point|Two-point scalar power means]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]
- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `private proof note`

## Proof

Take scalar data
\[
p=1,
\quad q=2,
\quad X=1,
\quad Y=2.
\]
If positive scalars \(a,b\) solved the two equations, then
\[
\frac{a+b}{2}=1,
\qquad
\left(\frac{a^2+b^2}{2}\right)^{1/2}=2.
\]
Thus \(a+b=2\) and \(a^2+b^2=8\). But for \(a,b\ge0\),
\[
a^2+b^2\le (a+b)^2=4,
\]
contradicting \(a^2+b^2=8\). Therefore the asserted universal inverse existence statement fails already in the one-dimensional scalar case.

_Proof source: `private proof note`._

## Tags

`bridge-lemma`, `endpoint-obstruction`, `finite-certificate`, `lemma`, `matrix-means`, `proved`, `ratio-bound`, `scalar-power-mean`, `true`
