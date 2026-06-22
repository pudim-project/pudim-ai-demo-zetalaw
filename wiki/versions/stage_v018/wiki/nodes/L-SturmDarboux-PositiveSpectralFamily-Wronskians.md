---
id: "L-SturmDarboux-PositiveSpectralFamily-Wronskians"
type: "lemma"
title: "Sturm-Darboux positive spectral families have positive initial Wronskians"
status: "proved"
tags: ["bridge", "chebyshev-system", "determinant-positivity", "lemma", "primitive", "proved", "strict-private-post-v016", "sturm-darboux", "true", "wronskian-positivity"]
parents: ["D-Laplace-kernel-and-tilted-moment-language", "D-Rational-certificate-and-finite-obstruction-language"]
refs: ["raw/student/20260620T0445-besseli-realorder-stp-positive.md"]
---

# Lemma: Sturm-Darboux positive spectral families have positive initial Wronskians

## Statement

Let \(f_1,\ldots,f_m\) be positive solutions on \(\mathbb R\) of \(f_j''=(q+\lambda_j)f_j\), with \(\lambda_1<\cdots<\lambda_m\), and suppose the left endpoint asymptotics are ordered so that every two-function Wronskian tends to zero at \(-\infty\) and each Darboux transform preserves positive ordered left asymptotics. Then every initial Wronskian \(W(f_1,\ldots,f_k)\) is strictly positive on \(\mathbb R\), for \(1\le k\le m\).

## Dependencies

- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]
- D-Rational-certificate-and-finite-obstruction-language

## Proof and provenance references

- `raw/student/20260620T0445-besseli-realorder-stp-positive.md`

## Proof

For every \(m\ge 1\), every
\[
0<x_1<\cdots<x_m
\]
and every
\[
0\le s_1<\cdots<s_m,
\]
one has
\[
\det\big[I_{s_j}(x_i)\big]_{i,j=1}^m>0.
\]
Thus the modified-Bessel kernel \(K(x,s)=I_s(x)\) is strictly totally positive on \((0,\infty)\times[0,\infty)\). This answers the Buchstaber--Glutsyuk real-order open question affirmatively.

Set \(x=e^y\) and
\[
f_s(y)=I_s(e^y),\qquad y\in\mathbb R,\ s\ge0.
\]
The modified Bessel equation
\[
x^2I_s''(x)+xI_s'(x)-(x^2+s^2)I_s(x)=0
\]
becomes
\[
f_s''(y)=\big(e^{2y}+s^2\big)f_s(y).
\]
Also
\[
I_s(x)=\frac{(x/2)^s}{\Gamma(s+1)}(1+O(x^2))
\]
as \(x\downarrow0\), so for \(s>0\)
\[
f_s(y)=2^{-s}\Gamma(s+1)^{-1}e^{sy}(1+O(e^{2y}))
\]
as \(y\to-\infty\), while
\[
f_0(y)=1+O(e^{2y}).
\]

First take \(0\le a<b\). Since \(f_a,f_b>0\) and both solve the same scalar equation with spectral parameters \(a^2,b^2\),
\[
W(f_a,f_b)'=(b^2-a^2)f_af_b>0.
\]
The left endpoint asymptotics give \(W(f_a,f_b)(y)\to0\) as \(y\to-\infty\), including the endpoint case \(a=0\). Hence
\[
W(f_a,f_b)(y)>0\qquad (y\in\mathbb R).
\]

Now prove all initial Wronskians by Darboux induction. Let
\[
0\le s_1<\cdots<s_m
\]
and put \(p=f_{s_1}'/f_{s_1}\), \(A=D-p\). For \(j\ge2\),
\[
u_j=Af_{s_j}=\frac{W(f_{s_1},f_{s_j})}{f_{s_1}}>0.
\]
The Darboux transform gives
\[
u_j''=\big(q_1(y)+s_j^2\big)u_j,\qquad
q_1=e^{2y}-2(\log f_{s_1})''.
\]
Moreover \(u_j(y)\sim (s_j-s_1)c_j e^{s_jy}\) if \(s_1>0\), and \(u_j(y)\sim s_jc_je^{s_jy}\) if \(s_1=0\), with \(c_j=2^{-s_j}\Gamma(s_j+1)^{-1}>0\). Thus the transformed family again satisfies the same ordered positive spectral-family hypotheses.

The Wronskian identity
\[
W(f_{s_1},\ldots,f_{s_k})=f_{s_1}\,W(u_2,\ldots,u_k)
\]
follows by subtracting \((f_{s_j}/f_{s_1})\) multiples of the first column in the Wronskian matrix, or equivalently from \(Af=f_{s_1}(f/f_{s_1})'\). Since \(f_{s_1}>0\), induction on \(k\) gives
\[
W(f_{s_1},\ldots,f_{s_k})(y)>0
\]
for every \(1\le k\le m\) and every \(y\in\mathbb R\).

Positive initial Wronskians imply a strict extended complete Chebyshev system. For completeness, the local argument is as follows. If the determinant
\[
\det[f_{s_j}(y_i)]_{i,j=1}^m
\]
vanished at \(y_1<\cdots<y_m\), there would be a nontrivial linear combination \(\sum c_j f_{s_j}\) with \(m\) zeros. Repeated generalized Rolle reduction using the positive Wronskians gives a contradiction, since an \(m\)-term ECT family permits at most \(m-1\) zeros counted with multiplicity. The sign is determined by the confluent limit:
\[
\det[f_{s_j}(y_i)]_{i,j=1}^m
\sim
\frac{W(f_{s_1},\ldots,f_{s_m})(y)}{\prod_{r=0}^{m-1}r!}
\prod_{i<j}(y_j-y_i)>0.
\]
Therefore the determinant is positive for all \(y_1<\cdots<y_m\). Returning to \(x_i=e^{y_i}\) proves the claimed strict total positivity.

_Proof source: `raw/student/20260620T0445-besseli-realorder-stp-positive.md`._

## Tags

`bridge`, `chebyshev-system`, `determinant-positivity`, `lemma`, `primitive`, `proved`, `strict-private-post-v016`, `sturm-darboux`, `true`, `wronskian-positivity`
