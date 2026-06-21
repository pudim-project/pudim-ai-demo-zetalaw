---
id: "T-From-Mills-all-L-moment-ratio-quadratic-bound"
type: "theorem"
title: "From Mills ratio all-L moment ratio quadratic upper bound"
status: "proved"
tags: ["all-L", "complete-monotonicity", "determinant-inequality", "mills-ratio", "moment-ratio", "proved", "source-solving", "theorem"]
parents: ["T-From-Mills-derivative-determinant-all-L", "D-Laplace-kernel-and-tilted-moment-language"]
refs: ["private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-from-mills-ratio.md"]
---

# Theorem: From Mills ratio all-L moment ratio quadratic upper bound

## Statement

Let \(M_L(t)=(-1)^L r^{(L)}(t)=\int_0^\infty u^L e^{-tu-u^2/2}\,du\) for the standard normal Mills ratio. For every \(L\ge0\) and \(t\ge0\), with \(m_L=M_{L+1}/M_L\), one has \(m_L(t)<U_L(t)\), where \(U_L(t)\) is the positive root \(\frac{\sqrt{t^2(t^2+4L+7)^2+4(L+1)(t^2+4L+8)(t^2+4L+6)}-t(t^2+4L+7)}{2(t^2+4L+8)}\).

## Dependencies

- [[wiki/nodes/T-From-Mills-derivative-determinant-all-L|Mills ratio all-L fourth-order determinant inequality]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `wiki/notes/frontier-from-mills-ratio.md`

## Proof

Set
\[
m_L(t)=\frac{M_{L+1}(t)}{M_L(t)}.
\]

The recurrence gives
\[
\frac{M_{L+2}}{M_L}=L+1-tm_L,
\]
\[
\frac{M_{L+3}}{M_L}=(t^2+L+2)m_L-t(L+1),
\]
and
\[
\frac{M_{L+4}}{M_L}=(L+1)(t^2+L+3)-t(t^2+2L+5)m_L.
\]

Substitution into the determinant inequality and expansion give
\[
(L+1)(t^2+4L+6)-t(t^2+4L+7)m_L-(t^2+4L+8)m_L^2>0.
\]

Equivalently,
\[
(t^2+4L+8)m_L^2+t(t^2+4L+7)m_L-(L+1)(t^2+4L+6)<0.
\]

Since \(m_L>0\), the positive root yields the uniform strict bound
\[
m_L(t)<U_L(t),
\]
where
\[
U_L(t)=
\frac{
\sqrt{t^2(t^2+4L+7)^2+4(L+1)(t^2+4L+8)(t^2+4L+6)}
-t(t^2+4L+7)
}
{2(t^2+4L+8)}.
\]

This is the determinant-to-bound extractor. It is a single theorem for every \(L\ge0\).

Define polynomials \(P_n(t)\) by
\[
P_0=1,\qquad P_1=t,\qquad P_{n+1}=tP_n+nP_{n-1}.
\]
Define \(B_n(t)\) by
\[
B_0=0,\qquad B_1=1,\qquad B_{n+1}=nB_{n-1}-tB_n.
\]

Then the same recurrence gives
\[
M_n(t)=(-1)^nP_n(t)r(t)+B_n(t).
\]

The ratio bound \(M_{L+1}<U_LM_L\) becomes
\[
\left((-1)^{L+1}P_{L+1}-(-1)^L U_LP_L\right)r
<U_LB_L-B_{L+1}.
\]

Since \(P_n(t)>0\) for \(t>0\) and \(P_{2j}(0)>0\), the coefficient has sign \((-1)^{L+1}\). Thus the bounds alternate:

For even \(L\ge0\),
\[
r(t)>
\frac{B_{L+1}(t)-U_L(t)B_L(t)}
{P_{L+1}(t)+U_L(t)P_L(t)}.
\]

For odd \(L\ge1\),
\[
r(t)<
\frac{U_L(t)B_L(t)-B_{L+1}(t)}
{P_{L+1}(t)+U_L(t)P_L(t)}.
\]

These formulas are valid at \(t=0\) by direct evaluation of the recurrences and for \(t>0\) by the positivity of \(M_L\).

_Proof source: `private proof note`._

## Tags

`all-L`, `complete-monotonicity`, `determinant-inequality`, `mills-ratio`, `moment-ratio`, `proved`, `source-solving`, `theorem`
