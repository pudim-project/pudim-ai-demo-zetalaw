---
id: "T-Kummer-M-Global-Modulus-Inequality-Fails-Alpha1-Beta5halves"
type: "theorem"
title: "Kummer M global modulus inequality fails at alpha one beta five halves"
status: "proved"
tags: ["application-candidate", "coefficient-obstruction", "endpoint-obstruction", "global-modulus-inequality", "kummer-function", "open-problem-solved", "proved", "source-solving", "special-functions", "strict-private-plus10", "theorem", "true"]
parents: ["D-GGPS-KummerM-Remark6-Question", "D-KummerM-LocalSeries", "L-RealSeries-ImagAxis-Modulus-SecondCoefficient-Obstruction", "O-Kummer-M-Global-Modulus-Inequality-source-gate"]
refs: ["oracle/responses/OS-20260613T234147Z-oracle-response.md", "raw/student/20260613T2346-kummer-modulus-second-coefficient.md"]
---

# Theorem: Kummer M global modulus inequality fails at alpha one beta five halves

## Statement

The Garrappa--Gerhold--Popolizio--Simon Remark 6 universal Kummer inequality is false. For \(\alpha=1\), \(\beta=5/2\), and all sufficiently small nonzero real \(t\), \(|{\rm M}(1,-3/2,it)|<1={\rm M}(1,-3/2,\operatorname{Re}(it))\).

## Dependencies

- [[wiki/nodes/D-GGPS-KummerM-Remark6-Question|GGPS Remark 6 Kummer M global modulus question]]
- [[wiki/nodes/D-KummerM-LocalSeries|Kummer M local series]]
- [[wiki/nodes/L-RealSeries-ImagAxis-Modulus-SecondCoefficient-Obstruction|Real-series imaginary-axis modulus second-coefficient obstruction]]
- [[wiki/nodes/O-Kummer-M-Global-Modulus-Inequality-source-gate|Kummer M global modulus inequality source gate]]

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

## Do not claim

- Do not claim GGPS Conjecture 25 for two-parameter Mittag-Leffler functions is solved.
- Do not claim any classification of Kummer modulus inequalities beyond this universal refutation.
- Do not claim public APP registry assignment.
- Do not public-stage without user request.

## Tags

`application-candidate`, `coefficient-obstruction`, `endpoint-obstruction`, `global-modulus-inequality`, `kummer-function`, `open-problem-solved`, `proved`, `source-solving`, `special-functions`, `strict-private-plus10`, `theorem`, `true`
