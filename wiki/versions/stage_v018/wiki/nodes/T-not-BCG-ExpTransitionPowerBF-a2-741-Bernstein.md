---
id: "T-not-BCG-ExpTransitionPowerBF-a2-741-Bernstein"
type: "theorem"
title: "BCG exponential-transition power is not Bernstein at a2=741/1000"
status: "proved"
tags: ["beghin-cristofaro-garrappa", "bernstein-function", "high-order-derivative", "moving-point-certificate", "not-app", "pointwise-obstruction", "proved", "scarpi-derivative", "theorem", "true-negation"]
parents: ["O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold", "L-BCG-ExpTransitionPowerBF-FppOne-Obstruction"]
refs: ["oracle/responses/OS-20260611T0912Z-bcg-moving-point-live-oracle-response.md", "raw/oracle/RO-OS-20260611T0912Z-bcg-moving-point-live.json", "raw/student/20260611T0950-bcg-moving-point-high-order-obstruction.md"]
---

# Theorem: BCG exponential-transition power is not Bernstein at a2=741/1000

## Statement

Let \(F(s)=s^{(a_2c+a_1s)/(c+s)}\). For \(a_1=3/10\), \(c=2\), and \(a_2=741/1000\), the function \(F\) is not a Bernstein function on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold|Beghin-Cristofaro-Garrappa exponential-transition power Bernstein threshold]]
- [[wiki/nodes/L-BCG-ExpTransitionPowerBF-FppOne-Obstruction|BCG exponential-transition power BF pointwise second-derivative obstruction]]

## Proof and provenance references

- `oracle/responses/OS-20260611T0912Z-bcg-moving-point-live-oracle-response.md`
- `raw/oracle/RO-OS-20260611T0912Z-bcg-moving-point-live.json`
- `raw/student/20260611T0950-bcg-moving-point-high-order-obstruction.md`

## Proof

Let
\[
F(s)=s^{(a_2c+a_1s)/(c+s)}.
\]
For
\[
a_1=\frac{3}{10},\qquad c=2,\qquad a_2=\frac{741}{1000},
\]
the function \(F\) is not a Bernstein function on \((0,\infty)\).

Write
\[
\phi(s)=\log F(s)=a\log s+D\frac{\log s}{c+s},
\qquad
a=a_1,\quad D=c(a_2-a_1).
\]
For \(m\ge 1\),
\[
\phi^{(m)}(s)
=(-1)^{m-1}a(m-1)!s^{-m}
+D(-1)^{m-1}m!
\left[
\sum_{j=1}^{m}
\frac{1}{j\,s^j(c+s)^{m-j+1}}
-\frac{\log s}{(c+s)^{m+1}}
\right].
\]

Let \(B_m(s)=F^{(m)}(s)/F(s)\). Since \(F=e^\phi\), the complete Bell recurrence gives
\[
B_0(s)=1,
\qquad
B_{m+1}(s)=\sum_{k=0}^{m}\binom{m}{k}B_{m-k}(s)\phi^{(k+1)}(s).
\]
Because \(F(s)>0\), the Bernstein derivative condition is equivalent to
\[
(-1)^{m-1}B_m(s)\ge0
\qquad(m\ge1,\ s>0).
\]

At
\[
s=700,\qquad m=2475,
\]
with
\[
a=\frac{3}{10},\qquad c=2,\qquad D=2\left(\frac{741}{1000}-\frac{3}{10}\right)=\frac{441}{500},
\]
the recurrence gives
\[
(-1)^{2474}B_{2475}(700)
=-3.3578425062147697151758207999717379625463667042172829120262256967310992663257308473252515102523948775218510792413
\times 10^{274}.
\]
In particular,
\[
(-1)^{2474}F^{(2475)}(700)
=F(700)(-1)^{2474}B_{2475}(700)<0.
\]
This violates the necessary derivative-sign condition for Bernstein functions. Therefore \(F\) is not Bernstein.

The recurrence was replayed with Python decimal arithmetic at precisions \(80,100,120,150\). In every replay the signed value had exponent \(274\), the same leading digits, and negative sign:
\[
-3.3578425062147697151758207\ldots\times10^{274}.
\]
The sign margin is therefore numerically stable. A fully public rendering should include the recurrence and either the decimal transcript or a machine-checkable interval replay.

This proves one concrete parameter obstruction near the source transition. It does not classify the BCG Bernstein parameter region and does not prove the converse of any derivative condition.

_Proof source: `raw/student/20260611T0950-bcg-moving-point-high-order-obstruction.md`._

## Do not claim

- Do not claim the full BCG Bernstein threshold is solved.
- Do not claim the source relaxation solution is negative or nonmonotone from this Bernstein obstruction alone.
- Do not present this as an APP without a separate source-exact APP gate.

## Tags

`beghin-cristofaro-garrappa`, `bernstein-function`, `high-order-derivative`, `moving-point-certificate`, `not-app`, `pointwise-obstruction`, `proved`, `scarpi-derivative`, `theorem`, `true-negation`
