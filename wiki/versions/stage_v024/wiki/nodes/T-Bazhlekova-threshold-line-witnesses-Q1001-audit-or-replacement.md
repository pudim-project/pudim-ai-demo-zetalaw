---
id: "T-Bazhlekova-threshold-line-witnesses-Q1001-audit-or-replacement"
type: "theorem"
title: "Bazhlekova threshold line witnesses Q1001 exact audit or replacement"
status: "proved"
tags: ["attack-plan", "bazhlekova", "finite-certificate", "high-order", "line-split", "proved", "theorem"]
parents: ["T-Exact-finite-certificate-verification-principle"]
refs: ["attack-plans/AP-20260601T034800-bazhlekova-wright-density-thresholds.json", "librarian/audits/LA-20260601T040500-bazhlekova-q1001-witness-audit-student.json", "raw/student/20260601T040500-bazhlekova-q1001-witness-audit.md", "raw/student/20260601T040500-bazhlekova-q1001-witness-audit.py", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova threshold line witnesses Q1001 exact audit or replacement

## Statement

Near the predicted top-cap threshold regions on the \((3/2,b)\) and \((11/10,b)\) line slices, either exact-audit the raw witnesses \(Q_{1001}^{3/2,63/250}(2876)<0\) and \(Q_{1001}^{11/10,13/500}(447)<0\), thickening any true witness into a rational \(b\)-interval, or replace them with lower-order exact rational witnesses that extend the certified line map toward the same thresholds.

## Dependencies

- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `attack-plans/AP-20260601T034800-bazhlekova-wright-density-thresholds.json`
- `librarian/audits/LA-20260601T040500-bazhlekova-q1001-witness-audit-student.json`
- `raw/student/20260601T040500-bazhlekova-q1001-witness-audit.md`
- `raw/student/20260601T040500-bazhlekova-q1001-witness-audit.py`
- `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`

## Proof

Use the standard Bazhlekova two-term normalization
\[
h(s)=s^{b/2}(1+s^{a-b})^{1/2}.
\]
The derivative polynomials \(Q_n(y)\), \(y=s^{a-b}\), are defined by
\[
h^{(n)}(s)
=s^{b/2-n}(1+y)^{1/2-n}Q_n(y).
\]
For sign testing set
\[
R_n(y)=(-1)^{n-1}Q_n(y).
\]
When \(n\) is odd, \(R_n=Q_n\).

The coefficient recurrence used in the local script is the same recurrence used by earlier line-map audits. If
\[
R_n(y)=\sum_k c_{n,k}y^k,\qquad \beta=\frac b2,\qquad \delta=a-b,
\]
then
\[
c_{n+1,k}
=(n-\beta-\delta k)c_{n,k}
\left(n-\beta+\delta\left(n-k+\frac12\right)\right)c_{n,k-1},
\]
with \(R_1(y)=\beta+(a/2)y\). This is an exact rational recurrence.

\[
Q_{1001}^{3/2,\,63/250}(2876)<0,
\]
and
\[
Q_{1001}^{11/10,\,13/500}(447)<0.
\]
The reproduced signs were:

\(a=3/2\), \(b=63/250\), \(y=2876\): sign \(-1\), numerator bit length \(28985\), denominator bit length \(8975\).
\(a=11/10\), \(b=13/500\), \(y=447\): sign \(-1\), numerator bit length \(27302\), denominator bit length \(9976\).

Because \(1001\) is odd, these are direct \(Q_{1001}<0\) witnesses. By the already admitted odd-derivative small-\(x\) criterion, each point gives a finite-parameter complete-monotonicity obstruction at the corresponding exponent pair.

The same replay script also searches the nearby threshold region for cheaper replacement witnesses and then certifies them by exact rational interval arithmetic. It proves:
\[
Q_{151}^{3/2,\,b}(269)<0
\quad\text{for}\quad
b\in
\left[
\frac{2509999}{10000000},
\frac{2510001}{10000000}
\right],
\]
and
\[
Q_{131}^{11/10,\,b}(50)<0
\quad\text{for}\quad
b\in
\left[
\frac{25699}{1000000},
\frac{25701}{1000000}
\right].
\]
Both orders are odd, so these are direct \(Q_n<0\) interval witnesses. They extend the certified rational line map toward the predicted high-order threshold regions while avoiding an order-\(1001\) interval computation.

_Proof source: `raw/student/20260601T040500-bazhlekova-q1001-witness-audit.md`._

## Tags

`attack-plan`, `bazhlekova`, `finite-certificate`, `high-order`, `line-split`, `proved`, `theorem`
