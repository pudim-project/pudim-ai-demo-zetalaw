---
id: "L-Scalar-matrix-case-refutes-universal-existence"
type: "lemma"
title: "Scalar case refutes universal matrix existence"
status: "proved"
tags: ["bridge-lemma", "endpoint-obstruction", "finite-certificate", "lemma", "matrix-means", "primitive-growth", "proved", "scalar-case", "true"]
parents: ["D-Finite-dimensional-l1-dual-certificate-language", "D-Endpoint-obstruction-certificate-language", "T-Pointwise-obstruction-certificate-principle"]
refs: ["librarian/audits/LA-20260613T1810-dlnv-matrix-power-mean-strict-app.json", "oracle/responses/OS-20260613T180145Z-oracle-response.md", "raw/student/20260613T1808-dlnv-matrix-power-mean-scalar-refutation.md", "raw/student/20260614T-v016-dlnv-public.md"]
---

# Lemma: Scalar case refutes universal matrix existence

## Statement

If a matrix existence assertion is universally quantified over all positive matrix sizes and all data satisfying its hypotheses, then an admissible one-dimensional scalar datum satisfying the same hypotheses and admitting no scalar solution refutes the universal matrix assertion.

## Dependencies

- [[wiki/nodes/D-Finite-dimensional-l1-dual-certificate-language|finite dimensional l1 primal representation coordinate atom dual linear functional certificate language]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]
- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]

## Proof and provenance references

- `librarian/audits/LA-20260613T1810-dlnv-matrix-power-mean-strict-app.json`
- `oracle/responses/OS-20260613T180145Z-oracle-response.md`
- `raw/student/20260613T1808-dlnv-matrix-power-mean-scalar-refutation.md`
- `raw/student/20260614T-v016-dlnv-public.md`

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

_Proof source: `raw/student/20260614T-v016-dlnv-public.md`._

## Tags

`bridge-lemma`, `endpoint-obstruction`, `finite-certificate`, `lemma`, `matrix-means`, `primitive-growth`, `proved`, `scalar-case`, `true`
