---
id: "L-RealSeries-ImagAxis-Modulus-SecondCoefficient-Obstruction"
type: "lemma"
title: "Real-series imaginary-axis modulus second-coefficient obstruction"
status: "proved"
tags: ["bridge-lemma", "coefficient-obstruction", "endpoint-obstruction", "finite-certificate", "global-modulus-inequality", "lemma", "proved", "true"]
parents: ["D-Endpoint-obstruction-certificate-language", "D-Determinant-triangular-compression-language", "T-Special-function-normal-form-calculus-principle", "T-Pointwise-obstruction-certificate-principle", "T-Exact-finite-certificate-verification-principle"]
refs: ["oracle/responses/OS-20260613T234147Z-oracle-response.md", "raw/student/20260613T2346-kummer-modulus-second-coefficient.md"]
---

# Lemma: Real-series imaginary-axis modulus second-coefficient obstruction

## Statement

Let \(F(z)=1+Az+Bz^2+O(z^3)\) near \(0\), with \(A,B\in\mathbb R\). Then \(|F(it)|^2=1+(A^2-2B)t^2+O(t^4)\). In particular, if \(A^2-2B<0\), then \(|F(it)|<F(0)=1\) for all sufficiently small nonzero real \(t\).

## Dependencies

- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]
- [[wiki/nodes/D-Determinant-triangular-compression-language|Determinant and triangular compression language]]
- [[wiki/nodes/T-Special-function-normal-form-calculus-principle|Special-function normal-form calculus principle]]
- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `oracle/responses/OS-20260613T234147Z-oracle-response.md`
- `raw/student/20260613T2346-kummer-modulus-second-coefficient.md`

## Proof

For \(c\notin\{0,-1,-2,\ldots\}\), the standard Kummer series is
\[
{\rm M}(a,c,z)={}_1F_1(a;c;z)
=\sum_{n=0}^{\infty}\frac{(a)_n}{(c)_n}\frac{z^n}{n!}.
\]
Hence
\[
{\rm M}(a,c,z)
=1+\frac{a}{c}z+\frac{a(a+1)}{2c(c+1)}z^2+O(z^3).
\]

Let \(F(z)=1+Az+Bz^2+O(z^3)\) with real \(A,B\). Then
\[
F(it)=1+iAt-Bt^2+O(t^3),\qquad F(-it)=1-iAt-Bt^2+O(t^3),
\]
so
\[
|F(it)|^2=F(it)F(-it)=1+(A^2-2B)t^2+O(t^4).
\]
Consequently, if \(A^2-2B<0\), then \(|F(it)|<1=F(0)\) for all sufficiently small nonzero real \(t\).

Take
\[
\alpha=1,\qquad \beta=\frac52,\qquad c=\alpha-\beta=-\frac32.
\]
This is admissible because \(c\notin\{0,-1,-2,\ldots\}\). For
\[
F(z)={\rm M}(1,-3/2,z),
\]
the coefficients are
\[
A=\frac{1}{-3/2}=-\frac23,
\qquad
B=\frac{1\cdot2}{2(-3/2)(-1/2)}=\frac43.
\]
Thus
\[
A^2-2B=\frac49-\frac83=-\frac{20}{9}.
\]
Therefore
\[
|{\rm M}(1,-3/2,it)|^2=1-\frac{20}{9}t^2+O(t^4)<1
\]
for all sufficiently small nonzero real \(t\). Since \(\operatorname{Re}(it)=0\) and \({\rm M}(1,-3/2,0)=1\), this gives
\[
|{\rm M}(1,-3/2,it)|<1={\rm M}(1,-3/2,\operatorname{Re}(it)).
\]
This contradicts the source's proposed universal inequality.

Conclusion: the Garrappa--Gerhold--Popolizio--Simon Remark 6 Kummer \(M\) global modulus question has a negative answer.

Scope caveat: this does not prove or disprove the separate GGPS Conjecture 25 for the two-parameter Mittag-Leffler function \(E_{\alpha,\beta}\) and reciprocal complete monotonicity.

Verification:

Local symbolic check: \(c=-3/2\), \(A=-2/3\), \(B=4/3\), \(A^2-2B=-20/9\), and \({}_1F_1(1;-3/2;z)=1-2z/3+4z^2/3+O(z^3)\).

_Proof source: `raw/student/20260613T2346-kummer-modulus-second-coefficient.md`._

## Tags

`bridge-lemma`, `coefficient-obstruction`, `endpoint-obstruction`, `finite-certificate`, `global-modulus-inequality`, `lemma`, `proved`, `true`
