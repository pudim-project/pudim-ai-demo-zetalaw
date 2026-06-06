---
id: "T-Bazhlekova-odd-derivative-polynomial-normal-form"
type: "theorem"
title: "Bazhlekova two term square root derivative polynomial normal form"
status: "proved"
tags: ["bazhlekova", "complete-monotonicity", "derivative-polynomial", "normal-form", "proved", "theorem"]
parents: ["T-Exact-finite-certificate-verification-principle"]
refs: ["librarian/audits/LA-20260601T015500-bazhlekova-two-term-gap-universal-student.json", "oracle/responses/ORACLE-OS-20260601T014500-bazhlekova-two-term-gap-universal-oracle-response.md", "raw/student/20260601T015500-bazhlekova-two-term-gap-universal.md", "raw/student/20260601T015500-bazhlekova-two-term-gap-universal.py", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova two term square root derivative polynomial normal form

## Statement

For \(h(s)=\sqrt{c s^a+d s^b}\), with \(c,d>0\), \(\Delta=a-b\), \(B=b/2\), and \(y=(c/d)s^\Delta\), the derivatives have the form \(h^{(n)}(s)=\sqrt d\,s^{B-n}(1+y)^{1/2-n}Q_n(y)\), where \(Q_0=1\) and \(Q_{n+1}=(B-n)(1+y)Q_n+\Delta y((1+y)Q_n'+(1/2-n)Q_n)\).

## Dependencies

- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `librarian/audits/LA-20260601T015500-bazhlekova-two-term-gap-universal-student.json`
- `oracle/responses/ORACLE-OS-20260601T014500-bazhlekova-two-term-gap-universal-oracle-response.md`
- `raw/student/20260601T015500-bazhlekova-two-term-gap-universal.md`
- `raw/student/20260601T015500-bazhlekova-two-term-gap-universal.py`
- `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`

## Proof

If for an odd \(n=2q+1\) there is \(y_0>0\) such that
\[
Q_n(y_0)<0,
\]
then for every \(c,d>0\) the point
\[
s_0=\left(\frac{d y_0}{c}\right)^{1/(a-b)}
\]
satisfies \(h^{(n)}(s_0)<0\).

A Bernstein function \(h\) has completely monotone derivative, hence for odd \(n\ge3\) it must satisfy \(h^{(n)}\ge0\). Thus the displayed sign proves that \(h\) is not Bernstein.

More directly for the Bazhlekova transform,
\[
F_x(s)=e^{-x h(s)}=\mathcal L\{w_t(x,\cdot)\}(s),
\]
we have
\[
F_x^{(n)}(s_0)=-x h^{(n)}(s_0)+O(x^2).
\]
For odd \(n\), complete monotonicity would require \(F_x^{(n)}(s_0)\le0\). If \(h^{(n)}(s_0)<0\), then \(F_x^{(n)}(s_0)>0\) for all sufficiently small \(x>0\), so \(w_t(x,\cdot)\) cannot be nonnegative.

The previous exact inner-gap example is recovered by the recurrence. For
\[
(a,b)=\left(\frac{28}{25},\frac1{50}\right),
\]
one has
\[
a-b=\frac{11}{10},\qquad
(a-1)^2+(b-1)^2=\frac{2437}{2500}<1,
\]
and
\[
Q_5(1)=-\frac{5570045943}{10000000000}<0.
\]
This matches the earlier value
\[
h^{(5)}(1)
=-\frac{5570045943\sqrt2}{320000000000}<0
\]
when \(c=d=1\).

The seventh derivative adds a new exact residual seed. For
\[
(a,b)=\left(\frac{107}{100},\frac1{100}\right),
\]
the point lies in the residual inner gap and exact Sturm counting gives no positive-root obstruction for \(Q_5\). But
\[
Q_7\left(\frac32\right)
=-\frac{56394696198326721417}{327680000000000000}<0.
\]

The ninth derivative adds another seed. For
\[
(a,b)=\left(\frac{53}{50},\frac1{100}\right),
\]
exact Sturm counting gives no positive-root obstruction for \(Q_5\) or \(Q_7\), but
\[
Q_9\left(\frac74\right)
=-\frac{3262653919060921278409379787}
{262144000000000000000000}<0.
\]

The finite \(5,7,9\) diagnostic does not cover the residual inner gap. At
\[
(a,b)=\left(\frac32,\frac25\right)
\]
we have
\[
0<b<a-1,\qquad a-b=\frac{11}{10}>1,\qquad
(a-1)^2+(b-1)^2=\frac{61}{100}<1.
\]
Exact Sturm counts show that \(Q_5,Q_7,Q_9\) have no positive roots. Since each has positive value at \(0\), each is positive on \(y>0\). Thus the fifth, seventh, and ninth derivative tests cannot decide this exponent pair.

The same noncoverage phenomenon also occurs at the near-boundary residual point
\[
(a,b)=\left(\frac{11}{10},\frac1{20}\right),
\qquad
(a-1)^2+(b-1)^2=\frac{73}{80}<1.
\]
Again \(Q_5,Q_7,Q_9\) have no positive roots and are positive at \(0\).

The derivative-polynomial normal form for \(h^{(n)}\).
The odd-derivative small-\(x\) obstruction criterion.
The exact fifth/seventh/ninth negative seeds above.
The exact finite \(5,7,9\) no-cover seeds above.

_Proof source: `raw/student/20260601T015500-bazhlekova-two-term-gap-universal.md`._

## Tags

`bazhlekova`, `complete-monotonicity`, `derivative-polynomial`, `normal-form`, `proved`, `theorem`
