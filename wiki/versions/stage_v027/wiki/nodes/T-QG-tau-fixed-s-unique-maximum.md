---
id: "T-QG-tau-fixed-s-unique-maximum"
type: "theorem"
title: "Qi Guo tau fixed s has unique maximum"
status: "proved"
tags: ["calculus", "gamma-digamma", "proved", "qi-guo", "theorem", "threshold"]
parents: ["T-Polynomial-root-logderivative-localization-principle"]
refs: ["librarian/audits/LA-20260530T215800-qg-tau-threshold-supremum.json", "oracle/responses/ORACLE-FI-20260530T-elegance-040-oracle-forage-response.md", "raw/scout/FI-20260530T-elegance-040.md", "raw/student/20260530T215800-qg-tau-threshold-supremum.md", "wiki/notes/frontier-qg-tau-threshold.md"]
---

# Theorem: Qi Guo tau fixed s has unique maximum

## Statement

For each \(s\in\mathbb N\), the function \(t\mapsto \tau(s,t)\) has a unique maximum on \((0,\infty)\), equivalently the transformed equation \((1-y)^s(1+sy+s(s+1)y^2)=1\) has a unique root \(y_s\in(0,1)\) giving that maximum.

## Dependencies

- [[wiki/nodes/T-Polynomial-root-logderivative-localization-principle|Polynomial root and logarithmic-derivative localization principle]]

## Proof and provenance references

- `librarian/audits/LA-20260530T215800-qg-tau-threshold-supremum.json`
- `oracle/responses/ORACLE-FI-20260530T-elegance-040-oracle-forage-response.md`
- `raw/scout/FI-20260530T-elegance-040.md`
- `raw/student/20260530T215800-qg-tau-threshold-supremum.md`
- `wiki/notes/frontier-qg-tau-threshold.md`

## Proof

Let \(a_*>0\) be the unique positive root of
\[
e^{a_*}=1+a_*+a_*^2.
\]
Then
\[
\sup_{s\in\mathbb N,\ t>0}\tau(s,t)
=\frac{a_*}{1+a_*+a_*^2}
=0.298425607525639\ldots.
\]
The supremum is not attained.

For fixed \(s\ge1\), set
\[
y=\frac1{t+1}\in(0,1).
\]
Then
\[
\tau_s(y)=\frac{1-y-(1+sy)(1-y)^{s+1}}{sy}.
\]
Direct differentiation gives
\[
\tau_s'(y)=
\frac{(1-y)^s\{1+sy+s(s+1)y^2\}-1}{s y^2}.
\]
Let
\[
F_s(y)=(1-y)^s\{1+sy+s(s+1)y^2\}.
\]
Then
\[
F_s'(y)=
\frac{s(s+1)y(1-y)^s\bigl((s+2)y-1\bigr)}{y-1}.
\]
Thus \(F_s\) increases on \((0,1/(s+2))\) and decreases on \((1/(s+2),1)\). Since \(F_s(0)=1\) and \(F_s(1)=0\), the equation \(F_s(y)=1\) has exactly one root \(y_s\in(1/(s+2),1)\) apart from the endpoint \(0\), and \(\tau_s\) has the unique maximum at \(y_s\).

At the maximizing point,
\[
(1-y_s)^s\{1+s y_s+s(s+1)y_s^2\}=1
\]
and
\[
m_s:=\max_{t>0}\tau(s,t)
=\frac{(s+1)y_s(1-y_s)}{1+s y_s+s(s+1)y_s^2}.
\]

Treat \(s\) as a real parameter. The envelope derivative at the unique maximizer equals the partial derivative in \(s\):
\[
\frac{d}{ds}m(s)=\partial_s\tau_s(y_s).
\]
Using \(F_s(y_s)=1\), its sign is the opposite of
\[
H_s(y_s)
=y_s\{1+(s+1)y_s\}+(1+s y_s)\log(1-y_s).
\]
The root satisfies \(y_s\ge1/(s+1)\). Indeed, for \(s=1\) equality holds, and for \(s>1\)
\[
F_s\!\left(\frac1{s+1}\right)
=\left(\frac{s}{s+1}\right)^s\frac{3s+1}{s+1}>1.
\]
Equivalently, with \(x=1/s\), this is
\[
(1+x)^{1/x}<\frac{3+x}{1+x},
\]
which follows because
\[
\frac{d}{dx}\left[\log\frac{3+x}{1+x}-\frac{\log(1+x)}x\right]<0
\]
on \((0,1]\) and the expression vanishes at \(x=1\).

For \(y\ge1/(s+1)\),
\[
H_s'(y)
=1+2(s+1)y+s\log(1-y)-\frac{1+sy}{1-y}
<\frac{y(1-(s+2)y)}{1-y}<0,
\]
where \(\log(1-y)<-y\). Also
\[
H_s\!\left(\frac1{s+1}\right)
=\frac2{s+1}-\frac{2s+1}{s+1}\log\left(1+\frac1s\right)<0,
\]
using \(\log(1+u)>2u/(2+u)\). Hence \(H_s(y_s)<0\), so \(m(s)\) is strictly increasing.

Put \(a_s=s y_s\). The critical equation becomes
\[
\left(1-\frac{a_s}{s}\right)^s
\left(1+a_s+\left(1+\frac1s\right)a_s^2\right)=1.
\]
The numbers \(a_s\) are bounded above by \(a_*\). For \(s>a_*\),
\[
\log F_s(a_*/s)
\le -a_*-\frac{a_*^2}{2s}
  +a_*+\frac{a_*^2}{s e^{a_*}}<0,
\]
so \(F_s(a_*/s)<1\) and \(a_s<a_*\); the remaining small \(s\) are immediate. Therefore \(a_s\to a_*\), because every subsequential limit solves
\[
e^{-a}(1+a+a^2)=1.
\]
The equation \(e^a=1+a+a^2\) has exactly one positive root after \(0\): the function \(e^a-1-a-a^2\) first decreases and then, after its derivative has its unique positive zero, increases to \(+\infty\).

Consequently
\[
\lim_{s\to\infty}m_s
=\frac{a_*}{1+a_*+a_*^2}.
\]
Since \(m(s)\) is strictly increasing and \(s\) is finite in the source domain, no finite \((s,t)\) attains the limiting value. Thus the source's requested maximum should be read as a supremum.

\[
a_*=1.79328213290076\ldots,\qquad
\frac{a_*}{1+a_*+a_*^2}=0.298425607525639\ldots,
\]
which is consistent with the source's observation \(\tau_0>0.2980\).

_Proof source: `raw/student/20260530T215800-qg-tau-threshold-supremum.md`._

## Tags

`calculus`, `gamma-digamma`, `proved`, `qi-guo`, `theorem`, `threshold`
