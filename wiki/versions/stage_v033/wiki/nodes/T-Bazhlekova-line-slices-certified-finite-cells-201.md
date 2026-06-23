---
id: "T-Bazhlekova-line-slices-certified-finite-cells-201"
type: "theorem"
title: "Bazhlekova line slices certified finite cells through 201 and high order obstruction intervals"
status: "proved"
tags: ["bazhlekova", "finite-certificate", "inner-gap", "line-split", "proved", "theorem"]
parents: ["T-Exact-finite-certificate-verification-principle"]
refs: ["librarian/audits/LA-20260601T025500-bazhlekova-island-split-student.json", "oracle/responses/ORACLE-OS-20260601T025500-bazhlekova-island-split-oracle-response.md", "raw/student/20260601T025500-bazhlekova-island-split.md", "raw/student/20260601T025500-bazhlekova-island-split.py", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova line slices certified finite cells through 201 and high order obstruction intervals

## Statement

On the Bazhlekova residual line slices \((3/2,b)\) and \((11/10,b)\), exact rational interval arithmetic certifies finite cells: \(R_n(y)>0\) for \(1\le n\le201\) on \(b\in[3999/10000,4001/10000]\) when \(a=3/2\), and on \(b\in[49/1000,51/1000]\) when \(a=11/10\); while \(Q_5(3)<0\) on \((a,b)=(3/2,[199/1000,201/1000])\), \(Q_{17}(18)<0\) on \((3/2,[2399/10000,2401/10000])\), \(Q_{85}(134)<0\) on \((3/2,[249999/1000000,250001/1000000])\), \(Q_9(2)<0\) on \((11/10,[199/10000,201/10000])\), and \(Q_{47}(16)<0\) on \((11/10,[2499/100000,2501/100000])\).

## Dependencies

- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `librarian/audits/LA-20260601T025500-bazhlekova-island-split-student.json`
- `oracle/responses/ORACLE-OS-20260601T025500-bazhlekova-island-split-oracle-response.md`
- `raw/student/20260601T025500-bazhlekova-island-split.md`
- `raw/student/20260601T025500-bazhlekova-island-split.py`
- `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`

## Proof

Let
\[
R_n(y)=(-1)^{n-1}Q_n(y)=\sum_{k=0}^n r_{n,k}y^k .
\]
The recurrence for \(Q_n\) gives the signed coefficient recurrence
\[
r_{n+1,k}
=
(n-B-\Delta k)r_{n,k}
+
\left(n-B+\Delta\left(n-k+\frac12\right)\right)r_{n,k-1},
\]
with missing coefficients interpreted as \(0\). This is the local audit engine for the top-edge coefficient tests.

The first AP candidate asked for an all-order proof of the finite pattern observed through order \(201\): either all coefficients of \(R_n\) are positive, or the only negative coefficient is the coefficient of \(y^{n-1}\), with the top quadratic controlled by a negative discriminant.

This statement is false as stated. At the no-cover seed
\[
(a,b)=\left(\frac32,\frac25\right),
\]
exact rational top-band recurrence gives
\[
r_{4482,4479}<0 .
\]
Since \(4479=4482-3\), this is a negative \(y^{n-3}\) coefficient, not the allowed \(y^{n-1}\) coefficient. The script verifies the sign exactly by tracking the rational ratio
\[
\frac{r_{n,n-3}}{r_{n,n}}
\]
and finds the first negative offset-\(3\) occurrence at \(n=4482\).

This does not refute plain Bernstein status at the seed: a high-degree coefficient-pattern break is not a witness that \(R_n(y)<0\) for some \(y>0\). It only kills the proposed elegant coefficient/discriminant induction in its current form.

the Bazhlekova no cover seeds all order coefficient discriminant pattern is refuted as stated, but the revised all-order positivity problem remains open.

The finite split-map branch did produce exact rational cells.

Finite positivity cells through order \(201\):
\[
a=\frac32,\qquad b\in\left[\frac{3999}{10000},\frac{4001}{10000}\right],
\]
and
\[
a=\frac{11}{10},\qquad b\in\left[\frac{49}{1000},\frac{51}{1000}\right].
\]
For both cells, interval arithmetic proves
\[
R_n(y)>0,\qquad y>0,\qquad 1\le n\le201,
\]
using the same coefficient/discriminant certificate as the pointwise no-cover seeds.

Obstruction cells:
\[
a=\frac32,\quad b\in\left[\frac{199}{1000},\frac{201}{1000}\right],
\qquad Q_5(3)<0,
\]
\[
a=\frac32,\quad b\in\left[\frac{2399}{10000},\frac{2401}{10000}\right],
\qquad Q_{17}(18)<0,
\]
\[
a=\frac32,\quad b\in\left[\frac{249999}{1000000},\frac{250001}{1000000}\right],
\qquad Q_{85}(134)<0,
\]
\[
a=\frac{11}{10},\quad b\in\left[\frac{199}{10000},\frac{201}{10000}\right],
\qquad Q_9(2)<0,
\]
and
\[
a=\frac{11}{10},\quad b\in\left[\frac{2499}{100000},\frac{2501}{100000}\right],
\qquad Q_{47}(16)<0.
\]
For odd orders \(R_n=Q_n\), so these interval witnesses feed directly into the admitted odd-derivative small-\(x\) obstruction criterion. Each obstruction cell gives uniform \(w_t\)-positivity failure for all \(c,d>0\) at the corresponding exponent interval.

the Bazhlekova line high order split map 3half 11tenth remains open as a full map problem, but the certified finite-cell node is true partial progress.

the Bazhlekova apparent island plain BF or inverse Laplace dichotomy remains candidate_open.

Route-kill node: the all-order single-negative-coefficient pattern fails at the seed \((3/2,2/5)\).
Finite split-map cell node: two finite positivity cells and five odd-derivative obstruction cells on the two requested line slices.

_Proof source: `raw/student/20260601T025500-bazhlekova-island-split.md`._

## Tags

`bazhlekova`, `finite-certificate`, `inner-gap`, `line-split`, `proved`, `theorem`
