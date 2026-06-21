---
id: "T-Bazhlekova-threshold-line-lower-order-replacement-cells-exact"
type: "theorem"
title: "Bazhlekova threshold line lower order rational replacement cells exact"
status: "proved"
tags: ["bazhlekova", "finite-certificate", "inner-gap", "interval-certificate", "line-split", "proved", "theorem"]
parents: ["T-Pointwise-obstruction-certificate-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private proof note", "private proof artifact", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova threshold line lower order rational replacement cells exact

## Statement

Exact rational interval arithmetic gives lower-order replacement cells near the Bazhlekova threshold regions: \(Q_{151}^{3/2,b}(269)<0\) for \(b\in[2509999/10000000,2510001/10000000]\), and \(Q_{131}^{11/10,b}(50)<0\) for \(b\in[25699/1000000,25701/1000000]\). Each cell gives an odd-derivative small-\(x\) complete-monotonicity obstruction for the corresponding line slice.

## Dependencies

- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `private proof artifact`
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

_Proof source: `private proof note`._

## Tags

`bazhlekova`, `finite-certificate`, `inner-gap`, `interval-certificate`, `line-split`, `proved`, `theorem`
