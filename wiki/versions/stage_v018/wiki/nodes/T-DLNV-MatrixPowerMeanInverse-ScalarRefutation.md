---
id: "T-DLNV-MatrixPowerMeanInverse-ScalarRefutation"
type: "theorem"
title: "Dinh-Le-Nguyen-Vo matrix power-mean inverse question is false"
status: "proved"
tags: ["application-candidate", "endpoint-obstruction", "finite-certificate", "matrix-means", "open-problem-solved", "operator-means", "proved", "scalar-counterexample", "source-solving", "strict-private-plus10", "theorem", "true"]
parents: ["L-Scalar-matrix-case-refutes-universal-existence", "L-ScalarPowerMean-Ratio-Endpoint", "O-DLNV-MatrixPowerMeanInverse-source-gate"]
refs: ["librarian/audits/LA-20260613T1810-dlnv-matrix-power-mean-strict-app.json", "oracle/responses/OS-20260613T180145Z-oracle-response.md", "raw/student/20260613T1808-dlnv-matrix-power-mean-scalar-refutation.md", "raw/student/20260614T-v016-dlnv-public.md"]
---

# Theorem: Dinh-Le-Nguyen-Vo matrix power-mean inverse question is false

## Statement

The literal Dinh--Le--Nguyen--Vo matrix power-mean inverse question is false. In the one-dimensional scalar case, the admissible data \(p=1\), \(q=2\), \(X=1\), and \(Y=2\) satisfy \(0<X<Y\), but the system \((a+b)/2=1\), \(((a^2+b^2)/2)^{1/2}=2\) has no nonnegative, hence no positive, scalar solution.

## Dependencies

- [[wiki/nodes/L-Scalar-matrix-case-refutes-universal-existence|Scalar case refutes universal matrix existence]]
- [[wiki/nodes/L-ScalarPowerMean-Ratio-Endpoint|Scalar power-mean ratio endpoint]]
- [[wiki/nodes/O-DLNV-MatrixPowerMeanInverse-source-gate|Dinh-Le-Nguyen-Vo matrix power-mean inverse source gate]]

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

## Do not claim

- Do not claim a classification of the corrected inverse problem with an added scalar or matrix feasibility window.
- Do not claim anything about unrelated Dinh-Ho-Le-Vo operator inequalities.
- Do not public-stage without user request.

## Tags

`application-candidate`, `endpoint-obstruction`, `finite-certificate`, `matrix-means`, `open-problem-solved`, `operator-means`, `proved`, `scalar-counterexample`, `source-solving`, `strict-private-plus10`, `theorem`, `true`
